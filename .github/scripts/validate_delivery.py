#!/usr/bin/env python3
"""交付驗證腳本（增量、配置驅動、嚴格攔截、精準行號）"""

import os
import re
import sys
import json
import subprocess
import fnmatch

# 預設配置（若讀不到主配置檔時使用）
DEFAULT_CONFIG = {
    "ignore_patterns": ["external/old-AI-WA-FAMILY/*", "external/AI-OS/*"],
    "forbidden_words": ["略", "保留原樣", "同上", "與前相同", "內容不變", "（省略）", "（程式碼略）", "...", "…", "參考前文", "其餘同前"],
    "simplified_chars": ["体", "实", "发", "档", "权", "检", "查", "网", "页", "库", "选", "项", "标", "准", "记", "录", "历", "史", "进", "化", "设", "计", "对", "应", "当", "总", "结", "归", "纳", "务", "动", "态", "统", "过", "将", "来", "并", "且"],
    "file_specific_rules": {}
}

CONFIG_PATH = "AI-kernel/docs/r-rules/validate-config.json"

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"[WARN] 配置文件格式錯誤，使用預設配置。錯誤：{e}")
    return DEFAULT_CONFIG

def get_changed_files():
    changed_env = os.environ.get("CHANGED_FILES", "").strip()
    if changed_env:
        return [f.strip() for f in changed_env.splitlines() if f.strip() and os.path.exists(f.strip())]
    try:
        # 預設抓取最後一次 commit 的變更 (Git diff)
        out = subprocess.check_output(["git", "diff", "--name-only", "HEAD~1", "HEAD"], text=True, stderr=subprocess.DEVNULL)
        return [f.strip() for f in out.splitlines() if f.strip() and os.path.exists(f.strip())]
    except Exception:
        return []

def get_diff_stats():
    try:
        out = subprocess.check_output(["git", "diff", "--numstat", "HEAD~1", "HEAD"], text=True, stderr=subprocess.DEVNULL)
        stats = {}
        for line in out.splitlines():
            parts = line.split('\t')
            if len(parts) == 3:
                added, deleted, filename = parts
                stats[filename] = {"added": int(added) if added.isdigit() else 0, "deleted": int(deleted) if deleted.isdigit() else 0}
        return stats
    except Exception:
        return {}

def is_ignored(path, config):
    for pattern in config.get("ignore_patterns", []):
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def check_eof(content):
    # 適用於 .md
    m = re.search(r"F:\s*([^\s\n]+)\s*\nV:\s*(\d+)\s*\nW:\s*([^\s\n]+)", content[-1500:])
    if m:
        if len(m.group(2)) != 10:
            return f"V 欄位不是 10 位數（{m.group(2)}）", m.group(3)
        return None, m.group(3)
    return "缺少 EOF（F/V/W）", "Unknown"

def check_eof_json(content):
    try:
        data = json.loads(content)
        if "_EOF" in data and "F" in data["_EOF"] and "V" in data["_EOF"] and "W" in data["_EOF"]:
            v = str(data["_EOF"]["V"])
            if len(v) != 10:
                return f"_EOF.V 不是 10 位數（{v}）", data["_EOF"]["W"]
            return None, data["_EOF"]["W"]
        return "缺少 _EOF 鍵值對", "Unknown"
    except json.JSONDecodeError:
        return "JSON 語法錯誤", "Unknown"

def check_eof_code(content):
    # 適用於 .js/.css/.html/.py/.sh 等
    tail = content[-500:]
    m = re.search(r"(?:/\*|#|<!--)\s*[═=]*\s*EOF\s*[═=]*\s*\n?.*?F:\s*([^\s\n]+)\s*\n?.*?V:\s*(\d+)\s*\n?.*?W:\s*([^\s\n]+)", tail, re.S)
    if m:
        if len(m.group(2)) != 10:
            return f"V 欄位不是 10 位數（{m.group(2)}）", m.group(3)
        return None, m.group(3)
    return "缺少註解包裹的 EOF（F/V/W）", "Unknown"

def check_content_lines(content, config, specific_rule):
    problems = []
    lines = content.splitlines()
    is_in_code_block = False
    
    # 檢查禁用詞與簡體字
    for i, line in enumerate(lines, 1):
        # 簡單的 Markdown 代碼塊標記判斷，避開代碼內容
        if line.strip().startswith("```") or line.strip().startswith("~~~"):
            is_in_code_block = not is_in_code_block
            continue
            
        if is_in_code_block:
            continue

        if specific_rule.get("check_forbidden_words", True):
            for word in config.get("forbidden_words", []):
                if word in line:
                    problems.append(f"第 {i} 行：發現禁用詞彙「{word}」")
                    
        if specific_rule.get("check_simplified", True):
            for word in config.get("simplified_chars", []):
                if word in line:
                    problems.append(f"第 {i} 行：發現疑似簡體字「{word}」")
                    
    return problems

def main():
    config = load_config()
    targets = get_changed_files()
    
    if not targets:
        print("[SUMMARY] 無變更檔案，跳過檢查。")
        sys.exit(0)

    diff_stats = get_diff_stats()
    total = 0
    bad = 0
    warn = 0
    report = []

    # 判斷是否允許刪減
    allow_delete = os.environ.get("ALLOW_DELETE", "").lower() == "true"
    if not allow_delete:
        try:
            commit_msg = subprocess.check_output(["git", "log", "-1", "--pretty=%B"], text=True, stderr=subprocess.DEVNULL)
            if "[allow-delete]" in commit_msg:
                allow_delete = True
        except Exception:
            pass

    for path in targets:
        if is_ignored(path, config):
            print(f"[SKIP] 命中白名單：{path}")
            continue

        # 行數異常減少檢查
        stats = diff_stats.get(path, {})
        if stats.get("deleted", 0) > 30 and not allow_delete:
            report.append(f"[WARN] {path}: 異常減少 {stats['deleted']} 行，且無 [allow-delete] 標記。")
            warn += 1

        if not path.endswith((".md", ".py", ".js", ".css", ".html", ".yml", ".json", ".sh")):
            continue
            
        total += 1
        try:
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
        except Exception as exc:
            report.append(f"[ERROR] {path}: 讀取失敗（{exc}）")
            bad += 1
            continue

        # 取得特定檔案規則
        specific_rule = config.get("file_specific_rules", {}).get(path, {})

        # EOF 檢查
        if path.endswith(".json"):
            eof_err, writer = check_eof_json(content)
        elif path.endswith(".md"):
            eof_err, writer = check_eof(content)
        else:
            eof_err, writer = check_eof_code(content)

        if eof_err:
            report.append(f"[ERROR] {path} (編寫者: {writer})\n  - {eof_err}")
            bad += 1

        # 內容掃描
        content_errs = check_content_lines(content, config, specific_rule)
        for err in content_errs:
            report.append(f"[ERROR] {path} (編寫者: {writer})\n  - {err}")
            bad += 1

    print(f"[SUMMARY] 增量檢查 {total} 檔，錯誤 {bad} 項，警告 {warn} 項。")
    if report:
        print("\n--- 檢查報告 ---")
        for r in report:
            print(r)

    # 若為嚴格模式且有錯誤，則中斷
    mode = os.environ.get("VALIDATE_MODE", "strict").lower()
    if bad > 0 and mode == "strict":
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
/* ═══ EOF ═══
F: AI-infra/.github/scripts/validate_delivery.py
V: 1792904400
W: ai-system-20261026-002#13
═══ */