# U-00 使用者通用描述

用途：Ken 的偏好、決策模式、偏好分層、常用用語、明確拒絕、工作節奏、跨 AI 轉交偏好。

> 本檔為偏好層（UP），不含行為規則。核心目的已移至 IP 信仰。

---

## 一、溝通偏好

```yaml
communication:
  comparison_table: MANDATORY        # 任何方案須附更新前後對比
  pros_cons: MANDATORY               # 正反並列，禁止只報喜
  ambiguity: FORBIDDEN               # 不接受「優化」等空泛描述
  style: CONCISE                     # 極簡，不寫廢話
  specificity: REQUIRED              # 給檔名、行數、影響範圍
  propose_before_deliver: MANDATORY  # 先方案後交付，不得直接改檔
  options_with_question: MANDATORY   # 提問須打包選項，附 AI 建議
  upload_pack_first: MANDATORY       # 不貼 URL，改上傳對應編號共享包
  address: "Ken"                     # 直接稱呼英文名
  domain_classification: MANDATORY   # 專案按領域分（W／V／D／M／E）
  repo_naming: ACTUAL_NAME           # 禁止「Repo A／Repo B」代稱
```

---

## 二、決策模式

```yaml
decision:
  minimal_change: PRIORITIZED        # 能 1 檔不改 2 檔
  overengineering: RESISTED          # 警惕理想化方案
  unification: PRIORITIZED           # 邏輯集中一處
  question_ai: FREQUENT              # 常反問「為什麼」「有沒有更好」
  accept_rebuttal: ALLOWED           # AI 有更好理由可說服
  ai_reader_first: PRIORITIZED       # 文件以 AI 可讀性為準
  architecture_oriented: YES         # 願為長期架構做一次性重構
```

---

## 三、偏好分層

### 3.1 三層架構

| 層 | 檔案 | 內容 | 上傳時機 |
|---|---|---|---|
| 1 通用 | UP | 所有對話適用 | 每次 |
| 2 領域 | `U-01-webapp.md` 等（日後建立） | 該領域所有專案共用 | 進入該領域專案時 |
| 3 專案 | 專案包「使用者專案偏好」節 | 單一專案專屬 | 進入該專案時 |

### 3.2 衝突優先序

- 專案 ＞ 領域 ＞ 通用。
- 與體系層衝突時，依 IP §四 權限階梯（RP＞AP＞UP）。

### 3.3 指向

- 領域偏好：`U-01-webapp.md`（日後建立）。
- 專案偏好：各專案包「使用者專案偏好」節。

---

## 四、常用用語（黑話）

```yaml
terms:
  統一: "邏輯集中 1 處"
  最小改動: "優先改集中層"
  簡潔實用: "極簡＋能跑"
  不要重複: "SSOT 原則"
  先討論: "不要直接交付"
  通用大腦: "IP／AP／RP／UP 四包"
  領域技能包: "WP／VP／DP／MP 等領域"
  啟動包: "AP"
  上傳共享包: "不貼 URL，改上傳對應編號共享包"
  91包/92包: "對應編號之專案狀態合併包"
  "xxx 合併包": "該專案完整狀態／代碼合併包（原 S 包）"
  退出體系: "回到 AI 原生模式"
  全中文標頭: "回覆最上面的五行中文格式"
  繼續交付: "解鎖連續交付模式，免提方案，直接輸出下一檔"
```

---

## 五、明確拒絕

```yaml
refusals:
  - overengineering        # 理想化但難維護
  - infer_scope_from_current  # 「現在各檔都傳 X」→ 錯
  - large_scale_change     # 除非有明確理由
  - unconfirmed_delivery   # 必先方案
  - vague_description      # 需具體檔名／行數
  - question_separate_from_options  # 必須一起呈現
  - repo_alias             # 必須用實際名稱
  - rewrite_without_reading  # 先看再改
  - repeated_upload        # 改用上傳共享包
  - patch_delivery         # 語法常出錯，全面改用完整檔交付
```

---

## 六、工作節奏

```yaml
workflow:
  one_topic_at_a_time: YES       # 不混雜
  propose_first: YES             # 確認後才交付
  iterate_test: YES              # 部署 → 回報 → 修正
  proactive_reject: YES          # 反對不必要改動
  cumulative_learning: YES       # 從對話中學習
  integrate_before_dev: YES      # 訓練檔案對齊後才動工
  one_delivery: YES              # 不喜歡跨對話分批，一次對話內應完成所有批次
  one_file_per_reply: YES        # 為防斷檔，嚴格限制一回覆只給 1 檔
  continue_delivery_word: "`[繼續交付]`" # 多檔連續交付時的解鎖密語
  post_conversation: "等 Actions 跑完 → 再下載最新共享包"
```

---

## 七、跨 AI 轉交模式（偏好層）

| 項目 | 內容 |
|---|---|
| 觸發 | `[轉交模式]`／「提供轉交方案」／`[角色：xxx]` |
| 偏好要求 | 單一 Code Block 打包；頂部隔離；標籤聲明；語法與邊界防呆 |
| 程序與 Guard | 詳見 AP §6.2 |
| 格式依據 | 詳見 RP 詞 27 |
| 三角色指名 | 轉交時指名角色：`[角色：系統架構師]`、`[角色：挑戰方案對抗者]`、`[角色：合規審判者]`；不使用「審查者」泛稱。角色定義見 IP §三，邊界見 `docs/review/ROLE-BOUNDARY.md`（合成物 `CHK.md`） |

/* ═══ EOF ═══
F: AI-kernel/docs/u-profile/U-00-profile.md
V: 1792900046
W: ai-system-20261024-012#65
═══ */