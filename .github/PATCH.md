## FILE: AI-kernel/docs/r-rules/R-00-rules.md
<<<<<<< OLD
| MUST | 所有回覆 | 前四行：<br>1. `# {序號}`<br>2. Code Block 包裹 `🆔 {對話編號}`<br>3. `[角色: {Reviewer/Builder} \| {英文狀態} \| {中文描述}]`<br>4. `執行：{動作描述}`<br>**體系外 NATIVE 時，第三行固定 `[Reviewer \| STATE_NATIVE \| AI 原生模式]`。** | 前四行格式完全相符 | 未分行、未包裹、順序錯誤、合併動作與狀態 | 檢查前四行 |
=======
| MUST | 所有回覆 | 前五行（全中文）：<br>1. `# {序號}`<br>2. Code Block 包裹 `🆔 {對話編號}`<br>3. `{中文身份}`（如：體系結構師、Webapp 開發者）<br>4. `({中文權責}){中文狀態}`（如：`(審查者)討論中`、`(執行者)交付中`）<br>5. `執行：{動作描述}`<br>**體系外 NATIVE 時，第三、四行固定為 `通用助手` 與 `(審查者)原生模式`。** | 前五行格式完全相符（全中文） | 未分行、未包裹、順序錯誤、合併動作與狀態、夾雜英文狀態 | 檢查前五行 |
>>>>>>> NEW

<<<<<<< OLD
/* ═══ EOF ═══
F: AI-kernel/docs/r-rules/R-00-rules.md
V: 1792582000
W: ai-system-20261021-004#30
═══ */
=======
/* ═══ EOF ═══
F: AI-kernel/docs/r-rules/R-00-rules.md
V: 1792589100
W: ai-system-20261021-005#6
═══ */
>>>>>>> NEW

## FILE: AI-kernel/docs/r-rules/R-03-terms.md
<<<<<<< OLD
| 40 | 體系四檔 | 合成物 `IP.md`＋`AP.md`＋`RP.md`＋`UP.md`；上傳即進體系；`SP.md` 僅紀錄 | A00 §1.1 |
=======
| 40 | 體系四檔 | 合成物 `IP.md`＋`AP.md`＋`RP.md`＋`UP.md`；上傳即進體系；`SP.md` 僅紀錄 | A00 §1.1 |
| 41 | 啟動標籤 | 使用者輸入 `[身份: xxx]` 觸發啟動沙盒切換 | A00 §2.10 |
| 42 | 自動識別 | 系統掃描上傳檔名（如 `90-`），自動判定領域分身 | A00 §2.10 |
| 43 | 元系統沙盒（Meta Sandbox） | Tier-0 體系結構師專用，允許寫入體系源檔 | A00 §2.11 |
| 44 | 快速開發沙盒（Fast Dev） | Tier-1 領域開發者專用，放寬 R-001 防呆 | A00 §2.11 |
| 45 | 嚴格審查沙盒（Strict Review） | 預設模式，強制執行所有體系防呆 | A00 §2.11 |
| 46 | 動態能力控制（CCL） | 依沙盒類型動態調整防呆與權限 | A00 §2.11 |
| 47 | 全中文標頭 | R-014 規定的五行回覆格式，全中文呈現 | R-014 |
>>>>>>> NEW

<<<<<<< OLD
/* ═══ EOF ═══
F: AI-kernel/docs/r-rules/R-03-terms.md
V: 1792575600
W: ai-system-20261021-003#61
═══ */
=======
/* ═══ EOF ═══
F: AI-kernel/docs/r-rules/R-03-terms.md
V: 1792589101
W: ai-system-20261021-005#6
═══ */
>>>>>>> NEW

## FILE: AI-kernel/docs/u-profile/U-00-profile.md
<<<<<<< OLD
| 「退出體系」 | 回到 AI 原生模式 |
=======
| 「退出體系」 | 回到 AI 原生模式 |
| 「自動識別」 | 系統看檔名自動切換身份，不用打指令 |
| 「沙盒」 | AI 當下的防呆模式（體系、開發、嚴格） |
| 「全中文標頭」 | 回覆最上面的五行中文格式 |
>>>>>>> NEW

<<<<<<< OLD
/* ═══ EOF ═══
F: AI-kernel/docs/u-profile/U-00-profile.md
V: 1792566000
W: ai-system-20261021-003#50
═══ */
=======
/* ═══ EOF ═══
F: AI-kernel/docs/u-profile/U-00-profile.md
V: 1792589102
W: ai-system-20261021-005#6
═══ */
>>>>>>> NEW