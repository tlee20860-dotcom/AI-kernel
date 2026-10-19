# W-05 Web App 頁面 Schema（Web App 通用）

最後更新：B34-3
Version: 1791899740
Batch: B34-3
Writer: A20261013-004#065
用途：Page Schema 通用規範

---

## 一、Schema 欄位

| 欄位 | 類型 | 說明 |
|---|---|---|
| title | string | 頁面標題 |
| data | object | Firebase 訂閱配置 |
| state | object | 響應式狀態初始值 |
| derived | object | 衍生資料計算 |
| blocks | array | UI 區塊 |
| onYearMonthChange | function | 年月變更 hook（可選） |
| customMount | function | 逃生艙（可選） |

---

## 二、data 配置

| 欄位 | 說明 |
|---|---|
| type | list / object / value / raw |
| path | 相對路徑（含 {key} / {__all__}） |
| transform | 資料轉換（可選） |
| params | 佔位符對應（可選） |

---

## 三、derived 配置

| 欄位 | 說明 |
|---|---|
| deps | 依賴的 data / state key 陣列 |
| compute | (ctx) => value 計算函式 |

---

## 四、blocks 常用類型

| type | 必要欄位 |
|---|---|
| stats | container, cards |
| list | container, rows, columns |
| filter | container, fields, bind |

---

## 五、ctx 提供

| 方法 | 用途 |
|---|---|
| ctx.onDataChange(fn) | 訂閱資料變更 |
| ctx.setState(path, val) | 設 state |
| ctx.invalidate(key) | 觸發重算 |

---

## 六、customMount 回傳

| 欄位 | 說明 |
|---|---|
| destroy | 清理函式 |

---

## 七、HTML 結構

| 元素 | 說明 |
|---|---|
| head | 4 個 CSS |
| body | app-shell > sidebar-root + main-area |
| main-area | navbar-root + content |
| content | page-header + 各 block container |
| scripts | lucide + modulepreload + type="module" |

---

## 八、常見錯誤

| # | 錯誤 | 正確 |
|---|---|---|
| 1 | derived 對 undefined 崩潰 | 加檢查 |
| 2 | customMount 未回傳 destroy | 必回傳 |
| 3 | 動態值用快照 | 內部讀 AppState |
| 4 | 動態注入未清空 | 先 textContent = '' |

---

## 九、關聯檔案

| 主題 | 檔案 |
|---|---|
| ES Module 架構 | W-03-esmodule.md |
| 本專案 Schema 實作 | js/pages/*.js |

---

/* ═══ EOF ═══
F: docs/W-05-schema.md
V: 1791899740
B(歷史): B34-3
W: A20261013-004#065
═══ */