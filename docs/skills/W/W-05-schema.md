# W-05 Web App 頁面 Schema 與 UI 規範（Web App 通用）

最後更新：2026-10-21
Version: 1792581006
Writer: ai-system-20261021-004#6
用途：Page Schema 通用規範 + UI 結構與術語

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

## 九、UI 結構與術語（通用）

### 9.1 頁面結構層級
| 層級 | 術語 | 說明 | 範例 |
|---|---|---|---|
| L1 | Page（頁面） | 一個 .html | index.html |
| L2 | Section（區塊） | 頁面內垂直堆疊的功能區 | page-header / stats |
| L3 | Row（列） | Section 內水平排列 | toolbar row |
| L4 | Item（元素） | 最小單位 | button / select |

### 9.2 Section 類型
| 術語 | 中文 | 用途 | 標準位置 |
|---|---|---|---|
| page-banner | 提示橫幅 | 說明文字 | 頁面最上 |
| page-header | 頁首 | 標題 + 副標題 + 主要操作 | banner 之後 |
| page-header-actions | 頁首操作區 | 標題行右側 | page-header 內 |
| stats | 統計卡區 | 數字統計 | header 之後 |
| page-controls | 控制列 | 篩選 / 切換 / 年月 | stats 之後 |
| content | 內容區 | 表格 / 卡片 | 最底 |
| empty-state | 空狀態 | 無資料時顯示 | 內容區內 |

### 9.3 控制列元素
| 術語 | type | 用途 | 位置 |
|---|---|---|---|
| add | add | 新增按鈕 | toolbar 左 |
| export | export | 匯出按鈕 | page-header 右 / toolbar 右 |
| viewToggle | viewToggle | 卡片 / 表格切換 | 強制 body |
| viewSwitcher | viewSwitcher | 檢視切換 | body 全行 |
| sort | sort | 排序下拉 | 強制 body |
| year | year | 年份下拉 | body 左側 |
| month | month | 月份下拉 | body 左側 |
| filter | filter | 篩選器 | body 全行 |
| custom | custom | 自訂按鈕 | 依需求 |

### 9.4 頁面標準佈局
| 順序 | Section | 內容 |
|---|---|---|
| 1 | page-banner | banner（若有） |
| 2 | page-header | 標題 + 副標題 + 主要操作 |
| 3 | stats | 統計卡 |
| 4 | page-controls | 新增 / 切換 / 年月 / 篩選 |
| 5 | content | 表格 / 卡片 |

### 9.5 表頭互動
- 點欄位標題（首次）：升序。
- 點欄位標題（第二次）：降序。
- 點欄位標題（第三次）：清除排序。
- 點欄位旁的 🔽：開下拉面板進行篩選。

---

## 十、關聯檔案

| 主題 | 檔案 |
|---|---|
| ES Module 架構 | W-03-esmodule.md |
| 本專案頁面實作 | 詳見專案包（如 P-06 / P-07） |

---

/* ═══ EOF ═══
F: W-05-schema.md
V: 1792581006
W: ai-system-20261021-004#6
═══ */