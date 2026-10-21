# W-01 Firebase RTDB 結構原則（Web App 通用）

最後更新：2026-10-21
Version: 1792581002
Writer: ai-system-20261021-004#2
用途：Firebase RTDB 通用結構原則（跨專案）

---

## 一、樹狀結構原則

| # | 原則 |
|---|---|
| 1 | 根節點分層（platform / families / 其他） |
| 2 | 家庭為獨立單位（families/{familyId}/） |
| 3 | 子節點按功能分類（members / expenses / ...） |
| 4 | 避免深層嵌套（≤ 6 層） |

---

## 二、路徑命名

| 規則 | 說明 |
|---|---|
| 小寫 + 底線 | expense_categories |
| 複數 | members / banks |
| 無縮寫 | expense_categories（非 exp_cat） |
| ID 用 push key | Firebase 自動生成 |

---

## 三、扁平化

| 概念 | 做法 |
|---|---|
| 1 對多 | 用路徑分隔，不用陣列 |
| 多對多 | 用索引節點 |
| 大資料 | 用子節點（避免單節點過大） |

---

## 四、索引節點

| 索引 | 用途 |
|---|---|
| platform/uid_index/{uid} | uid → familyId |
| platform/email_index/{account} | account → { uid, familyId } |

**原則**：索引只存對應關係，不存實體資料。

---

## 五、實時訂閱

| 模式 | 用途 |
|---|---|
| listen* | 持續訂閱（資料變更自動推送） |
| get*Once | 一次性讀取 |

**選擇原則**：

| 情境 | 用 |
|---|---|
| 頁面需即時更新 | listen |
| 一次性檢查 | once |
| 跨頁共用 | listen + registry 快取 |

---

## 六、讀寫分離

| 原則 | 說明 |
|---|---|
| 讀取 | normalize 舊資料 |
| 寫入 | 寫新格式 |
| 刪除 | 保留節點（軟刪除） |

---

## 七、限制

| 節點 | 建議上限 |
|---|---|
| 單筆列表 | ≤ 1000 筆 |
| 巢狀深度 | ≤ 6 層 |
| 單節點大小 | < 10 MB |

**超過時**：拆子節點或加索引。

---

## 八、關聯檔案

| 主題 | 檔案 |
|---|---|
| 本專案資料結構 | 詳見專案包（如 P-09-data.md） |
| 本專案 API | 詳見專案包（如 P-08-api.md） |

---

/* ═══ EOF ═══
F: W-01-firebase.md
V: 1792581002
W: ai-system-20261021-004#2
═══ */