## 📄 AI-kernel/docs/skills/W/W-05-schema.md

# W-05 Web App 頁面規範與 UI 結構（Web App 通用）

最後更新：2026-10-28
用途：V2 命令式頁面模組規範 + UI 結構與術語（通用，含行動端排版鐵律）

---

## 零、頁面渲染鐵律（MUST）

經歷過專案實戰，Web App 的頁面渲染必須遵守以下規範，避免手機破版或資料顯示不全。

### 0.1 行動端表格排版（防破版）
在手機窄螢幕上，表格如果沒有設定最小寬度，會導致文字被嚴重擠壓變形（例如「交貨日期」變成直排）。
- **解法**：表格外層必須有 `overflow-x-auto`（允許橫向滑動），且 `<th>` 與 `<td>` 必須加上 `whitespace-nowrap`（強制不換行）與 `min-w-[120px]`（最小寬度）。
- **禁止**：禁止讓表格在不設定寬度的情況下自動縮放。

### 0.2 數據驅動渲染（防寫死）
- 頁面模組**絕對禁止**手寫 `<table>` 的欄位結構。必須接收來自系統設定的 `visibleFields`，透過 `map()` 動態生成表頭與資料列。
- 若傳入的欄位陣列為空，必須有 `Fallback` 機制（例如至少顯示「單號」與「狀態」）。

---

## 一、頁面模組（V2 標準）

V2 起，所有頁面採**命令式模組**，每個 `pages/*.js` 匯出單一物件：

```js
export default {
  async render() { /* 繪製與綁定事件 */ },
  destroy() { /* 清理監聽器、取消訂閱 */ }
};
```

| 方法 | 職責 | 必填 |
|---|---|---|
| `render()` | 繪製頁面骨架、載入資料、綁定事件 | 是 |
| `destroy()` | 移除 `addEventListener`、取消 `AppState.on` 訂閱、清除計時器 | 是（若無監聽則可空實作） |

---

## 二、V1 Schema 遺產（供歷史追溯，非 V2 強制）

> 以下為 V1 Schema 架構的欄位定義，僅供舊專案參考。**V2 新專案不得再使用 Schema 宣告式**，改用 §一 的命令式模組。

### 2.1 Schema 欄位（V1）

| 欄位 | 類型 | 說明 |
|---|---|---|
| `title` | string | 頁面標題 |
| `data` | object | Firebase 訂閱配置 |
| `state` | object | 響應式狀態初始值 |
| `derived` | object | 衍生資料計算 |
| `blocks` | array | UI 區塊 |

### 2.2 data 配置（V1）

| 欄位 | 說明 |
|---|---|
| `type` | list / object / value / raw |
| `path` | 相對路徑（含 `{key}` / `{__all__}`） |
| `transform` | 資料轉換（可選） |
| `params` | 佔位符對應（可選） |

### 2.3 derived 配置（V1）

| 欄位 | 說明 |
|---|---|
| `deps` | 依賴的 data / state key 陣列 |
| `compute` | `(ctx) => value` 計算函式 |

### 2.4 blocks 常用類型（V1）

| type | 必要欄位 |
|---|---|
| stats | container, cards |
| list | container, rows, columns |
| filter | container, fields, bind |

---

## 三、V2 頁面標準流程

> 以下為 V2 命令式頁面的建議實作流程，對應 `pages/*.js` 的 `render()`。

| 步 | 動作 | 說明 |
|---|---|---|
| 1 | 準備 `headerActions` HTML（按鈕、連結） | 放在頁首右側 |
| 2 | 準備 `controlsHtml`（Tab／年月／檢視切換／篩選） | 放在統計卡下方 |
| 3 | 呼叫 `renderPageLayout({ title, headerActions, stats, controls, listContainerId })` | 由 `ui/layout.js` 統一繪製骨架 |
| 4 | 綁定控制列事件（`renderYearMonth`／`renderViewToggle`） | 事件回呼內呼叫 `_loadData()` 或 `_renderList()` |
| 5 | 訂閱資料（`listen*` 或 `AppState.on`） | 記錄 unsubscribe 供 `destroy()` 清理 |
| 6 | 渲染列表（呼叫 `order-view.js` 或 `renderTable`） | 依狀態與設定動態生成 |
| 7 | 在 `destroy()` 中釋放所有訂閱與監聽 | 防止記憶體洩漏 |

---

## 四、HTML 結構（V2 SPA 單頁）

| 元素 | 說明 |
|---|---|
| `<head>` | 2 個 CSS（`theme.css` + `app.css`）、`manifest.json`、PWA meta |
| `<body>` | `#app-loading`（初始載入動畫）、`#app-root`（SPA 掛載點） |
| `<script>` | 圖示庫（defer）、`engine/main.js`（module） |

**骨架生成**：`ui/layout.js` 的 `initLayout()` 會在 `#app-root` 內生成 `<div class="app-shell">`，包含側邊欄、navbar、`#app-content`。各頁面只需往 `#app-content` 填充內容。

---

## 五、UI 結構與術語（通用，V2 保留）

### 5.1 頁面結構層級

| 層級 | 術語 | 說明 | 範例 |
|---|---|---|---|
| L1 | Page（頁面） | 一個 SPA 路由 | `/dashboard` |
| L2 | Section（區塊） | 頁面內垂直堆疊的功能區 | page-header / stats |
| L3 | Row（列） | Section 內水平排列 | toolbar row |
| L4 | Item（元素） | 最小單位 | button / select |

### 5.2 Section 類型

| 術語 | 中文 | 用途 | 標準位置 |
|---|---|---|---|
| page-banner | 提示橫幅 | 說明文字 | 頁面最上 |
| page-header | 頁首 | 標題 + 副標題 + 主要操作 | banner 之後 |
| page-header-actions | 頁首操作區 | 標題行右側 | page-header 內 |
| stats | 統計卡區 | 數字統計 | header 之後 |
| page-controls | 控制列 | 篩選 / 切換 / 年月 | stats 之後 |
| content | 內容區 | 表格 / 卡片 | 最底 |
| empty-state | 空狀態 | 無資料時顯示 | 內容區內 |

### 5.3 控制列元素

| 術語 | type | 用途 | 位置 |
|---|---|---|---|
| add | add | 新增按鈕 | toolbar 左 |
| export | export | 匯出按鈕 | page-header 右 / toolbar 右 |
| viewToggle | viewToggle | 卡片 / 表格切換 | 強制 body |
| sort | sort | 排序下拉 | 強制 body |
| filter | filter | 篩選器 | body 全行 |

### 5.4 頁面標準佈局

| 順序 | Section | 內容 |
|---|---|---|
| 1 | page-banner | banner（若有） |
| 2 | page-header | 標題 + 副標題 + 主要操作 |
| 3 | stats | 統計卡 |
| 4 | page-controls | 新增 / 切換 / 篩選 |
| 5 | content | 表格 / 卡片 |

---

## 六、關聯檔案

| 主題 | 檔案 |
|---|---|
| ES Module 架構（V2） | W-03-esmodule.md |
| Cloudflare Functions | W-02-functions.md |
| 通用錯誤與防呆 | W-07-errors.md |

---

/* ═══ EOF ═══
F: AI-kernel/docs/skills/W/W-05-schema.md
V: 1792917400
W: UPGRADE-002
═══ */