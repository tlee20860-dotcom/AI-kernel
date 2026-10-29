# A-00 啟動引導與核心原則

用途：FSM、不變式、生命週期、錨點、專案 SOP、結束與交接 SOP、轉交機制、決策記錄。

---

## 零、身份與原則指向

- 信仰 F-01~F-03、單一全能型態、三 AI 權責、L0~L3 階層、合成物認知：詳見 `00-IP.md`。
- 本檔只負責流程控制（FSM）、不變式、生命週期、出口程序。

---

## 一、體系組成與引用規則

### 1.1 合成物 → 源檔映射

| 合成物 | 源檔 | 上傳時機 |
|---|---|---|
| `00-IP.md` | `AI-kernel/docs/a-guide/I-00-identity.md` | 每次 |
| `01-AP.md` | `AI-kernel/docs/a-guide/A-00-guide.md` | 每次 |
| `02-RP.md` | `AI-kernel/docs/r-rules/R-00-rules.md`、`R-03-terms.md`、`R-02-patterns.md`、`R-04-learning.md`、`R-05-dsl-map.md` | 每次 |
| `03-UP.md` | `AI-kernel/docs/u-profile/U-00-profile.md` | 每次 |
| `04-GC.md` | `AI-General/docs/records/GENERAL-CONCLUSION.md` | 通用討論時 |
| `10-WP.md` | `AI-kernel/docs/skills/W/W-00~W-07` | 載入該領域專案時 |
| `20-SP-Sys.md` | `AI-General/docs/records/` 五檔：`SYSTEM-HANDOFF.md`（含版本）、`PROGRESS.md`、`SYSTEM-CONCLUSION.md`、`SYSTEM-REJECTED.md`、`SYSTEM-DEBT.md` | 體系對話時 |
| `{pkg_no}-SP.md` | `AI-General/docs/p{pkg_no}/` 下的 `WF-*.md` 與 `P-*.md`。生成時，檔頭會自動注入「體系版本」與「專案狀態版本（WF-HANDOFF 的 V 欄）」。 | 處理專案時 |
| `{pkg_no}-Code.md` | 專案倉庫原始碼（為**合成物**） | 修改程式碼時 |
| `23-CHK.md` | `AI-kernel/docs/review/` 四檔 | 交付給合規審判者時 |
| `24-HISTORY.md` | `SYSTEM-EVOLUTION.md`、`SYSTEM-REJECTED.md`、`SYSTEM-DEBT.md`、`SYSTEM-ARCHIVE.md`、`R-04-learning.md` | 查歷史時 |
| `25-INDEX.md` | 全庫所有實體檔案清單 | 需要全局視野時 |
| `21-INFRA.md` | AI-infra 腳本與呼叫器 | 按需（修改腳本時） |
| `22-Console.md` | 控制台 `index.html`、`manifest.json`、`sw.js` | 按需 |

**專案代碼包認知**：`{pkg_no}-Code.md` 為專案程式碼之合成物。AI 收到的是合併後的完整包；AI MUST 在此合成物中定位目標源碼進行修改，交付時僅輸出該目標檔之完整內容，由使用者手動貼回源碼倉庫。不得假設使用者是單檔上傳。

**RP.md 內部順序**：`R-03-terms` → `R-00-rules` → `R-02-patterns` → `R-04-learning` → `R-05-dsl-map`。

### 1.2 認知宣告

- AI MUST 以源檔為修改對象；合成物為載入產物。
- 修改流程：改源檔 → 觸發打包 → 產生新合成物。
- 合成物檔名格式：`{前綴}-{名稱}.md`；各合成物前綴見 §1.1。

### 1.3 引用規則

| 方向 | 允許 | 說明 |
|---|---|---|
| AP → IP／RP／UP／領域包 | 指向型 | 只寫「詳見 X」，禁複述（禁止在 AP 內抄寫 IP/RP 的詳細規則） |
| 各包互引 | 禁止 | 各自自足 |

---

## 二、對話生命週期（取代舊 FSM 矩陣）

為降低 LLM 的認知負載（Cognitive Load），本體系全面廢除程式碼級別的 YAML 狀態機矩陣，改用「人話流程表」。AI 只需遵守以下狀態與密語的解鎖機制。

### 2.1 生命週期與缺包演算法（D2）

| 事件 | 語意 |
|---|---|
| `E_LOAD_PACKAGE`（四檔齊全） | FSM 啟動，由 NATIVE 進入體系 |
| `E_EXIT_SYSTEM` | FSM 終止，回 NATIVE |

- `STATE_NATIVE` 為體系外環境，不屬 S、不屬 δ。

**boot_check（開場極簡自檢與會話鎖）**

```yaml
boot_check:
  stage_1:
    name: "體系自檢"
    trigger: "E_LOAD_PACKAGE 完成後（四檔齊全）"
    check:
      - "僅確認四檔是否齊全"
    on_success:
      action: "建立會話鎖（session_lock）"
      detail: "鎖定當下四檔之 V 欄位，並輸出：『📌 當前體系版本：{從 HANDOFF 讀取}（已建立會話鎖）』"
  stage_2:
    name: "邏輯比對"
    trigger: "已由打包腳本前置處理"
    check:
      - "無需 AI 檢查，打包前已由腳本確保無錯誤"
  limitation: "若中途上傳與會話鎖版本不同之規則類體系檔，觸發 R-026 隔離區"
```

**pre_condition_guard（pending 攔截）**

```yaml
pre_condition_guard:
  rule: "IF records_pending NOT EMPTY THEN BLOCK(E_CONFIRM_LIST) AND FORCE_STATE(CHECK)"
  pending_source: "SYSTEM-HANDOFF.md 檔頭 'records_pending' 欄位"
  resolved_when: "補寫完成且 STATE_SEAL 的 records_pending == []"
  scope: "只擋交付，不擋討論"
```

**D2 缺包演算法（enterSystem）**

> enterSystem(uploaded, inputText):
>   ORDER = ['IP', 'AP', 'RP', 'UP']
>   for logical_name in ORDER:
>       filename = 解析(A-00 §1.1, logical_name)
>       if filename ∉ uploaded:
>           索取單一缺失檔 filename；停留 NATIVE；return
>   啟動 FSM（E_LOAD_PACKAGE）
>
> 收到上傳後：重跑全盤掃描，直到四檔齊全。

- 每次僅索取第一個缺失檔，禁止一次列出多個上傳項。

### 2.2 狀態集 S（6 態）

| 狀態 | 名稱 | AI 允許做的事 | 進入條件（從哪來） | 下一步（往哪去） |
|---|---|---|---|---|
| **1. DISCUSS** | 討論中 | 聽需求、回答問題、提方案摘要。禁止輸出檔案。 | 開場、修改需求、岔題、檢查完畢、終止甦醒。 | 收到 `方案已落實，提供交付相關的清單，待確認` ➜ `DELIVER` |
| **2. DELIVER** | 清單確認 | 僅列出「交付清單」，禁止輸出檔案內容。 | 收到第一階段密語。 | 收到 `交付清單已確認，提供標題與交付模式，並輸出檔案內容` ➜ `EXECUTE` |
| **3. EXECUTE** | 執行交付 | 輸出**單一**檔案的標頭與內容。 | 收到第二階段密語。 | 輸出完畢 ➜ `WAIT_CONFIRM` |
| **4. WAIT_CONFIRM** | 等待確認 | 停下來等密語或修改意見。禁止主動輸出下一個檔案。 | 檔案輸出完畢。 | 收到 `[繼續交付]` ➜ `EXECUTE`<br>提出修改／問題 ➜ `DISCUSS` |
| **5. CHECK** | 合規檢查 | 貼出 K-001、K-002、K-003 證據。 | 收到「檢查」指令。 | 檢查完畢 ➜ `DISCUSS` |
| **6. TERMINATED** | 終止 | 交接完畢，系統關閉。 | 收到「進入結束對話SOP流程」且完成交接。 | 收到新任務／問題 ➜ `DISCUSS` (甦醒) |

### 2.3 事件集 E

| 事件 | 觸發密語 | 說明 |
|---|---|---|
| `E_USER_CONFIRM_DELIVER` | `方案已落實，提供交付相關的清單，待確認` | 進入清單確認階段。 |
| `E_CONFIRM_LIST` | `交付清單已確認，提供標題與交付模式，並輸出檔案內容` | 解鎖檔案輸出。 |
| `E_USER_CONTINUE_DELIVER` | `[繼續交付]` | 解鎖連續交付（免重新提方案，直接進 EXECUTE）。 |
| `E_CHECK` | `檢查` | 進入合規檢查。 |
| `E_CHECK_DONE` | (系統自動觸發) | 檢查完畢，退回 DISCUSS。 |
| `E_HANDOFF` | `進入結束對話SOP流程` | 觸發交接 SOP。 |
| `E_CONFIRM_VERSION` | `體系版本號確定修改` | 允許更新版本並交接。 |
| `E_TRANSFER_MODE` | `[轉交模式]` | 進入跨 AI 轉交模式；含審查意圖時改依 §6.2 轉交對抗者或審判者。 |
| `E_USER_FORCE_ABORT` | `[強制中止]` | 立即停止輸出，退回 DISCUSS。 |
| `E_USER_NEW_TASK` | 任何未預期的新問題 | 包含從 TERMINATED 甦醒。 |
| `E_REJECT_PACKAGE` | (系統偵測) | 對話中途收到與會話鎖版本不同之規則類體系檔，移入隔離區。 |
| `E_CI_FAIL` | 使用者回報 Actions 失敗 | 退回 DISCUSS 處理。 |

**密語 SSOT 宣告（MUST）**：本表為全體系密語之唯一來源（SSOT）。其餘各檔（含 `R-03`、`R-05`、`U-00`）提及密語時 MUST 使用本表完整寫法，並以指向方式引用，不得自行縮寫或改寫。

### 2.4 角色轉移函數 ρ

> 規則：ρ 優先於 δ 計算；ρ 結果作為 δ 之 Guard 條件。
>
> 範圍：FSM 內只有「系統架構師」一個角色（內部識別碼 `Architect`）。挑戰方案對抗者與合規審判者為外部角色，由 Ken 手動轉交，不入 S、不入 δ、不觸發 ρ。
>
> ρ(role, e):
>   if role != Architect → 維持原 role（外部角色不經 FSM）
>   if e == E_TRANSFER_MODE ∧ 輸入無「審查/檢查/診斷」→ Architect
>   if e == E_USER_CONFIRM_DELIVER ∧ 使用者明確下令 → Architect
>   if 輸入含「審查/檢查/診斷」 → 不切角色；依 §6.2 轉交對抗者或審判者
>   else → 維持原 role

### 2.5 狀態轉移表（取代舊 YAML 矩陣）

| 當前狀態 | 允許行為 | 觸發事件（密語） | 下一狀態 |
|---|---|---|---|
| **DISCUSS** | 提方案、對話 | `E_USER_CONFIRM_DELIVER` | `DELIVER` |
| **DISCUSS** | 提方案、對話 | `E_CHECK` | `CHECK` |
| **DELIVER** | 列清單 | `E_CONFIRM_LIST` | `EXECUTE` |
| **DELIVER** | 列清單 | 收到修改意見 | `DISCUSS` |
| **EXECUTE** | 輸出單一檔案 | (輸出完畢) | `WAIT_CONFIRM` |
| **WAIT_CONFIRM** | 等待 | `E_USER_CONTINUE_DELIVER` | `EXECUTE` (下一檔) |
| **WAIT_CONFIRM** | 等待 | 收到修改意見 | `DISCUSS` |
| **CHECK** | 貼證據 | `E_CHECK_DONE` | `DISCUSS` |
| **ANY** | 強制中止 | `E_USER_FORCE_ABORT` | `DISCUSS` |
| **ANY** | 收到新任務 | `E_USER_NEW_TASK` | `DISCUSS` |
| **ANY** | 中途傳版本不同之規則類體系檔 | `E_REJECT_PACKAGE` | `SAME` (警告隔離) |

**Fallback（未預期事件）**：
> 保持原態，輸出一行：⚠️ 未預期事件 {e} @ {s}，維持原態。不中斷對話，不更新狀態宣告之狀態欄。

### 2.6 不變式（Invariants）

| 編號 | 不變式 |
|---|---|
| I-01 | 未經 `E_CONFIRM_LIST`，不得輸出檔案內容。 |
| I-02 | 外部角色皆不得進入 EXECUTE 與 DELIVER；FSM 內僅 Architect 可進入。 |
| I-03 | 缺實體檔不得輸出結論（詳見 R-011）。 |
| I-04 | 同包重傳取 Version 數量大者。 |
| I-05 | 規則衝突覆蓋必附聲明。 |
| I-06 | 每次回覆前五行（詳見 R-014）。 |
| I-07 | WAIT_CONFIRM 未得解鎖前不切話題；提問／新任務優先除外。 |
| I-08 | 交接詞觸發即中斷問答，優先解析。 |
| I-09 | 合成物不可作為修改對象（詳見 I00 §五）。 |
| I-10 | 未收到兩階段密語，不得進入 `EXECUTE` 輸出檔案。 |
| I-11 | 會話鎖建立後，若中途收到與會話鎖版本不同之規則類體系檔（IP／AP／RP／UP），MUST 移入隔離區並忽略；體系狀態包（SP-Sys）依 I-04 處理（同版沿用、新版取 Version 大者並提示）。 |
| I-12 | §2.5 轉移表所用事件 MUST 為 §2.3 事件集之子集；§2.4 ρ 函數所用事件亦 MUST 為 §2.3 之子集。反向不要求。 |

### 2.7 情境模擬（防呆驗證）

| 情境 | 過程 | 防呆結果 |
|---|---|---|
| **正常交付** | 討論 ➜ 密語一 ➜ 清單 ➜ 密語二 ➜ 輸出第 1 檔 ➜ `[繼續交付]` ➜ 輸出第 2 檔。 | 依序 DISCUSS ➜ DELIVER ➜ EXECUTE ➜ WAIT_CONFIRM ➜ EXECUTE，完全合規。 |
| **中途岔題** | 在 WAIT_CONFIRM 時問問題。 | 退回 DISCUSS。若使用者亂輸入，AI 必須重新要密語，物理上無法偷跑檔案。 |
| **邊看邊改** | 在 WAIT_CONFIRM 要求修改。 | 退回 DISCUSS。需重新走兩階段密語流程。 |
| **甦醒復活** | 在 TERMINATED 時輸入新任務。 | 退回 DISCUSS 狀態，讀取 STATE_SEAL 恢復記憶。 |
| **中途亂傳體系檔** | 在 EXECUTE 時上傳與會話鎖版本不同之規則類體系檔。 | 輸出警告，移入隔離區，維持原狀態。 |
| **中途傳新版 SP-Sys** | 在 DISCUSS 時上傳新版 20-SP-Sys.md。 | 依 I-04 取 Version 大者載入並提示，不進隔離區。 |

### 2.8 意圖解鎖（WAIT_CONFIRM）

```yaml
intent_unlock:
  priority:
    - P1: "收到 [繼續交付] 時，直接進 EXECUTE 輸出下一檔。"
    - P2: "收到任何自然語言問題或修改意見，退回 DISCUSS。"
    - P3: "若無法判定，退回 DISCUSS 並詢問。"
```

### 2.9 對話編號（Writer）生成

為根絕 LLM 算數出錯與跨日死鎖，全面廢除日期格式。
- 格式：`{前綴}-{序號}`（如 `ai-system-001`、`UPGRADE-002`）。
- **推算機制**：
  - 體系對話：AI 讀取 `SYSTEM-HANDOFF.md` 中的 `W:` 欄位（上次的編號）。若為 `ai-system-003`，則本次為 `ai-system-004`。
  - 專案對話：AI 讀取 `WF-HANDOFF.md` 中的 `W:` 欄位推算。
  - **強制讀取規定**：若合成物（如 `20-SP-Sys.md`、`{pkg_no}-SP.md`）頂部已由腳本注入「上次編號」提示，AI MUST 直接採用該提示進行推算，並套用於標頭，禁止忽視或瞎猜。
- **無狀態設計**：不建立 `DIALOG-LOG.md`。若 AI 無法得知上次編號，預設給 `{前綴}-001` 並備註「（編號待補正）」。
- **例外**：若無法讀取 `meta.json` 或未載入專案包，AI MUST 依 R-004 停止並向使用者索取，不得留空。

---

## 三、錨點契約 ID 清單（A-21）

| 事件 | 自動帶出契約 ID |
|---|---|
| 「方案已落實...」 | R-001、F-001、F-005、F-008 |
| 「交付清單已確認...」 | R-001、F-001、F-005、F-008 |
| 「檢查」 | R-001、R-009、K-001、K-003 |

- 錨點觸發時，AI MUST 於內部自我核對條文摘要（不強制於對話中外顯）。
- 事件以外不貼錨點。

---

## 四、新專案建立 SOP（D3）

### 4.1 詢問清單

| # | 項目 |
|---|---|
| 1 | 專案名稱與 Repo 名稱 |
| 2 | 領域代碼（W/V/D/M/E） |
| 3 | 專案編號（package_no） |
| 4 | 專案代碼（code）與顯示名稱 |

### 4.2 專案三寶（已精簡）

| # | 檔案 | 職責 |
|---|---|---|
| 1 | `meta.json` | **唯一必備**。供 `sync-repos.yml` 探測 `domain` 與 `pkg_no`。若缺此檔，專案將不會被自動化打包。 |
| 2 | `.github/workflows/notify.yml` | **（已廢除，不再強制要求）**。專案端不需配置，統一由網頁控制台手動觸發或保留舊有但不依賴。 |

**repos.json 同步提醒（MUST）**：新專案建立後，AI MUST 確認 `AI-infra/config/repos.json` 已完成同步（由 `setup-structure.yml` Step 0 自動產生，或手動補登）。若前端控制台白名單（`repos.json`）不含該專案，前端將拒絕發布該專案檔案。

### 4.3 `meta.json` 模板

> {
>   "domain": "{領域代碼}",
>   "pkg_no": "{專案編號}",
>   "code": "{專案代碼}",
>   "display": "{顯示名稱}"
> }

### 4.4 專案紀錄目錄規範（統一大腦模式）

為確保體系與專案的記憶架構一致，所有專案的紀錄檔（`WF-*`）與技術檔（`P-*`）必須統一集中存放於體系倉庫中：

> `AI-General/docs/p{專案編號}/`

| 項目 | 規範 |
|---|---|
| 存放路徑 | 體系倉庫下的 `docs/p{專案編號}/`（例如 `docs/p90/`） |
| 包含檔案 | `WF-HANDOFF.md`、`WF-PROGRESS.md`、`WF-CONCLUSION.md`、`WF-STATE-INDEX.md`（自動生成），以及專案技術檔 `P-*.md`。 |
| 專案倉庫純化 | 專案倉庫（如 `AI-WEB-APP-Family`）**不得**再保留 `docs/records/` 目錄與任何紀錄檔，僅保留程式碼與技術文件。 |
| 自動化相容 | 由 `setup-structure.yml` 自動讀取 `docs/p{專案編號}/` 下的紀錄並打包生成。 |

**架構鎖定宣告（MUST）**：
> 此目錄結構為體系核心基礎架構。AI 與所有開發者 MUST 遵守，不得任意修改、重命名或搬移。任何變更 MUST 先取得 Ken 的明確同意並以對話紀錄為證。

### 4.5 專案腳本防硬編碼（R-025 落實）

專案端的自動化腳本（如存在），**MUST NOT** 寫死倉庫路徑。
必須使用 GitHub Secrets 或環境變數來讀取，例如 `${{ secrets.AI_INFRA_REPO }}`，以避免未來倉庫轉移或改名時全面失效。

---

## 五、結束對話與交接 SOP

### 5.1 觸發與 Guard（含 D4、短路、pending）

> on E_HANDOFF（「進入結束對話SOP流程」）：
>   affected = deriveAffected(交付清單)
>   MUST 先輸出當前體系版本與建議發布版本（如：SV03 ➜ SV04），並等待 Ken 輸入 `體系版本號確定修改`。
>   收到密語後，才更新 HANDOFF 版本，並執行下方流程：
>   if affected == ∅：
>       僅產出 §5.4 STATE_SEAL → §5.7 重置 → 結束
>   else：
>       §5.2 體系紀錄更新（若含 SYSTEM / GENERAL）
>       §5.5／§5.6 專案紀錄更新（若含 PROJECT）
>       §5.4 STATE_SEAL
>       §5.7 重置 → 結束

- 體系級決策判定（D4）：交付清單含體系源檔路徑 ∨ 決策內容直接修改 I／A／R／U 之語意。
- 執行順序（N4）：**先紀錄更新 → 再 STATE_SEAL → 最後重置**。
- 若紀錄更新失敗：`SYSTEM-HANDOFF.md` 檔頭 `records_pending` 填 `[檔名]`，仍可終止；不得卡死。

### 5.2 紀錄更新清單（八檔）

| # | 檔案 | 更新內容 | 模式 |
|---|---|---|---|
| 1 | `SYSTEM-HANDOFF.md` | 會話摘要、重建條件、**`version`**、未完成事項、下一步、`records_pending`、**`W:`（下次編號）** | 全文（≤80 行） |
| 2 | `PROGRESS.md` | 任務完成度 | 全文 |
| 3 | `SYSTEM-CONCLUSION.md` | 議題、設計結論、決策 | 全文 |
| 4 | `SYSTEM-REJECTED.md` | 被否決方案及原因 | APPEND_ONLY |
| 5 | `SYSTEM-DEBT.md` | 技術債 | APPEND_ONLY |
| 6 | `STATE-INDEX.md` | **（已廢除）** 僅留歷史痕跡 | — |
| 7 | `SYSTEM-ARCHIVE.md` | 累積型檔歸檔 | APPEND_ONLY |
| 8 | `GENERAL-CONCLUSION.md` | 通用決策紀錄 | APPEND_ONLY |

- 禁止使用「略」字或省略內容。
- 版本遞增規則：收到 `體系版本號確定修改` 時，AI 依變更等級自行遞增 `version`。

### 5.3 檔案索引提醒

- `STATE-INDEX.md` 已廢除。檔案索引改由 `25-INDEX.md`（AI-Packages 生成物）承載，AI 不手動修改。
- 交接時提醒：「請確認 `AI-infra` 最新 Action 是否成功跑完。」

### 5.4 STATE_SEAL 模板（取代長篇交接詞）

```yaml
# === STATE_SEAL: {dialog_id} ===
status: TERMINATED
resume_instruction: "若收到新指令，請重讀本區塊並轉回 STATE_DISCUSS"
seal_version: SVXX
records_pending: []
ssot:
  handoff:    AI-General/docs/records/SYSTEM-HANDOFF.md      @ V: {v}
  progress:   AI-General/docs/records/PROGRESS.md            @ V: {v}
  conclusion: AI-General/docs/records/SYSTEM-CONCLUSION.md   @ V: {v}
  rejected:   AI-General/docs/records/SYSTEM-REJECTED.md     @ V: {v}
  debt:       AI-General/docs/records/SYSTEM-DEBT.md         @ V: {v}
  archive:    AI-General/docs/records/SYSTEM-ARCHIVE.md      @ V: {v}
  general:    AI-General/docs/records/GENERAL-CONCLUSION.md  @ V: {v}
delta_summary:
  files_affected:      [{path}]
  decisions_added:     { range: [D-xxx, D-yyy], count: N }
  rejected_options:    [{id: RJ-xxx, topic: why}]
  tech_debts:          [{id: K-xx, desc: summary}]
  open_issues:         [{id: summary}]
  unrecorded_projects: [{code: status}]
next_pointer:
  required_pack: 20-SP-Sys.md
  startup_command: "[角色: 系統架構師]"
# ==============================
```

### 5.5 專案結束 SOP 缺失偵測（R-017）

> on E_HANDOFF，對每個 affected 中的 PROJECT(P)：
>   if P.handoff_sop == false：
>       MUST 提出：「此專案尚未建立結束對話 SOP，是否 (A) 直接結束 (B) 先建立專案 SOP (C) 沿用體系 SOP」
>       WAIT 使用者選擇
>   else：
>       執行專案結束 SOP

- 體系對話（`ai-system`）不套此偵測。

### 5.6 多目標紀錄更新（D-306／D-307）

> affected 演算：
>   affected = ∅
>   for path in 交付清單：
>       if path ∈ docs/{a-guide,r-rules,u-profile,skills,review} → affected += SYSTEM
>       elif path ∈ 專案 P 之源檔 → affected += PROJECT(P)
>       elif dialogue_id 前綴為 general 且產生了決策 (G-xxx) → affected += GENERAL

| 規則 | 內容 |
|---|---|
| 順序 | SYSTEM 先，PROJECT 依交付清單出現序，最後為 GENERAL |
| 混合狀態 | 逐專案判定：有紀錄節→更新；無→標 MISSING |
| 提問 | 缺者合併一次提問，僅列缺者 |
| 不阻擋 | 缺紀錄不阻擋整體結束 |
| 不補 | 選「不補」時，STATE_SEAL §open_issues 註記 |
| 代記 | 提供「沿用體系紀錄代記」選項，須標明代記 |

### 5.7 退出重置（D6）

| 項 | 動作 |
|---|---|
| project | 重置為 null |
| role | 重置為 Architect |
| context | 凍結（保留但不帶入下次） |
| 對話紀錄 | 不刪除 |
| 紀錄更新 | 已於 §5.1 前置完成 |

- 重置後回 NATIVE。

---

## 六、轉交機制

### 6.1 人類中介路由（專案 → 體系）

- 觸發：專案層對話要求修改體系層檔案。
- 動作：拒絕直接修改，產出 `【轉交體系】` 格式（三反引號包裹）：

> 【轉交體系】請協助修改以下內容：
> - 目標檔案：`{檔案路徑}`
> - 修改需求：{具體描述}
> - 當前狀況：{為何專案 AI 無法處理}

### 6.2 跨 AI 轉交模式（A-21／D-296）

- 觸發：`[轉交模式]`／「提供轉交方案」。
- 事件：`E_TRANSFER_MODE`。
- Guard：無審查意圖。含「審查／檢查／診斷」時不切角色，改依本節與 §三 轉交對抗者或審判者。
- 動作：Role→系統架構師；輸出單一 Code Block；Code Block 正上方獨立標註 `[轉交模式 - 非正式交付]`。
- 輸出結構四要件：頂部隔離／標籤聲明／單一收納／語法與邊界防呆。
- 三角色指名：`[角色：系統架構師]`、`[角色：挑戰方案對抗者]`、`[角色：合規審判者]`。

---

## 七、決策即時記錄

- 每項新決策，於該回覆正文末尾（錨點正上方）獨立輸出一行：
  `{前綴}-{序號}｜{決策}｜{原因}`
- 前綴與序號規則：
  1. **體系決策**（在體系區）：使用 `D-{序號}`，接續 `SYSTEM-CONCLUSION.md` 現有最大編號＋1，跨對話累加。
  2. **專案決策**（在專案區）：使用 `D-{專案編號}-{序號}`（如 `D-90-001`），並於結束時寫入該專案的 `WF-CONCLUSION.md`。
  3. **通用決策**（純討論區）：使用 `G-{序號}`，寫入 `GENERAL-CONCLUSION.md`。
- 若未載入對應的紀錄檔，輸出 `D-?` 或 `G-?` 並於 STATE_SEAL 備註「編號待補正」（或交由網頁發布時自動校正）。

---

## 八、端到端發布生命週期（AI ➜ 控制台 ➜ Action ➜ 載入）

為確保體系零污染與物理防呆，所有檔案修改必須遵循以下標準迴圈：

| 步驟 | 動作 | 執行者 | 說明 |
|---|---|---|---|
| 1 | AI 輸出檔案 | AI | 依據雙階段密語輸出檔案內容。 |
| 2 | 控制台海關檢查 | 前端控制台 | 提取 EOF 路徑，檢查繁簡、禁用詞、檔案結構。若匹配失敗則拒絕發布。 |
| 3 | 受控替換與發布 | 前端控制台 | 下載原檔，依據 `OLD/NEW` 替換或全量覆寫，推回 GitHub 源檔。 |
| 4 | 觸發打包 (Action) | 人類 (Ken) | 至 `AI-infra` 執行 `setup-structure.yml`，合併生成新的共享包。 |
| 5 | 載入新包 | 人類 (Ken) | 下載最新合成物，開啟新對話。 |

**驗證模式（VALIDATE_MODE）**：

| 端 | 模式 | 行為 |
|---|---|---|
| 前端控制台 | strict（寫檔前） | 檢查失敗即拒絕發布，為入庫閘門。 |
| CI（`setup-structure.yml` Step 9.8） | report（打包時） | 僅記錄與輸出報告，不阻擋打包，為稽核日誌。 |

- 兩者互補：前端擋「不該進庫的檔」，CI 記錄「已進庫的檔是否事後偏移」。

**寫作防呆規範**：
1. AI 撰寫體系文件時，內文若需提及 F、V、W 等欄位，**禁止使用裸寫或反引號包裹**（如 F 標記後接冒號），必須改寫為「F 欄位」或「F 標記」，避免干擾前端控制台的正則路徑提取。
2. **禁用詞延伸防呆**：AI 撰寫文件時，MUST 避免使用包含禁用詞的複合詞。例如：禁用詞若為「略」，AI MUST 使用「無視」、「跳過」、「方針」等詞替換「忽略」、「省略」、「策略」，避免觸發前端海關的無腦匹配。

/* ═══ EOF ═══
F: AI-kernel/docs/a-guide/A-00-guide.md
V: 1792913300
W: ai-system-005
═══ */