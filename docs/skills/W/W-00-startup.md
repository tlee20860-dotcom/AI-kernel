## 📄 AI-kernel/docs/skills/W/W-00-startup.md

# W-00 領域啟動卡（Web App）

最後更新：2026-10-25
用途：Web App 領域的啟動卡（工具鏈 / 慣例 / 載入方式）

---

> **【強制規則宣告】**
> 本 W 包（W-00 ~ W-07）為 Web App 領域之**強制性規則（Domain Rules）**。AI 處理所有 Web App 相關任務時，**MUST** 遵守本包規範。違反 W 包之架構契約（如 W-03）或 SOP，視同違反體系鐵律。

---

## 一、領域定位

| 項目 | 內容 |
|---|---|
| 領域名稱 | Web App |
| 領域前綴 | W |
| 適用範圍 | 純 HTML / CSS / JS 前端 + Serverless 後端 |
| 適用專案 | 所有依循本體系之 Web App 專案 |

---

## 二、技能包清單

| # | 檔案 | 職責 |
|---|---|---|
| 0 | W-00-startup.md（本檔） | 領域啟動卡 |
| 1 | W-01-firebase.md | Firebase RTDB 結構原則 |
| 2 | W-02-functions.md | Cloudflare Pages Functions 規則 |
| 3 | W-03-esmodule.md | 純前端 ES Module 架構（**含依賴方向鐵律與架構契約**） |
| 4 | W-04-pwa.md | PWA + Service Worker |
| 5 | W-05-schema.md | Web App 頁面規範與 UI 結構 |
| 6 | W-06-sop.md | Web App 通用任務 SOP（**含新專案零到一啟動 SOP**） |
| 7 | W-07-errors.md | Web App 通用錯誤與防呆 |

---

## 三、工具鏈

| 層 | 技術 |
|---|---|
| 前端 | 純 HTML + CSS + ES Module JS（無框架） |
| 後端 | Cloudflare Pages Functions |
| 資料庫 | Firebase RTDB |
| 認證 | Firebase Auth |
| 部署 | Cloudflare Pages |
| 版控 | GitHub |

---

## 四、通用慣例

| # | 慣例 |
|---|---|
| 1 | 檔案結構：三層架構（資料 / 引擎 / 呈現） |
| 2 | SSOT 極大化 |
| 3 | 宣告式 > 命令式 |
| 4 | 檔案 ≤ 800 行 |
| 5 | 每個 .js / .html / .css / .md 結尾加 EOF |
| 6 | 無框架，不引入 React / Vue |

---

## 五、領域常見任務

| 任務 | 引用 |
|---|---|
| **新專案啟動** | W-06 §零 |
| 新增頁面 | W-03 + W-05 + W-06 §一 |
| 改資料結構 | W-01 |
| 改 Functions | W-02 |
| 改 PWA | W-04 |
| 改 Schema / UI | W-05 |

---

## 六、領域常見錯誤

| # | 錯誤 | 正確 |
|---|---|---|
| 1 | 用 process.env（CF Pages 不支援） | handler 參數 { env } |
| 2 | 移除既有 export（依賴模組崩潰） | 用 export let 保留 |
| 3 | 動態值用快照 | 內部讀 AppState |
| 4 | 動態注入未清空 | 先 textContent = '' |
| 5 | 全站結構改動未完整掃描 | 改前完整掃描 |
| 6 | UI 層反向依賴業務層 | 嚴格遵守 W-03 依賴契約 |

---

## 七、未來擴充提示

若需要新增 Web App 技術（如 WebSocket / Web Worker），新增 `W-08-xxx.md` 並更新本清單。

---

## 八、關聯檔案

| 主題 | 檔案 |
|---|---|
| 體系四檔 | `IP.md`、`AP.md`、`RP.md`、`UP.md` |
| Firebase RTDB | W-01-firebase.md |
| CF Pages Functions | W-02-functions.md |
| ES Module | W-03-esmodule.md |
| PWA + SW | W-04-pwa.md |
| Page Schema | W-05-schema.md |
| 通用 SOP | W-06-sop.md |
| 通用錯誤 | W-07-errors.md |

---

/* ═══ EOF ═══
F: W-00-startup.md
V: 1792901630
W: webapp-20261025-001#19
═══ */