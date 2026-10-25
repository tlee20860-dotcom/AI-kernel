## 📄 AI-kernel/docs/skills/W/W-05-schema.md

# W-05 Web App 頁面規範與 UI 結構（Web App 通用）

最後更新：2026-10-25
Version: 1792901260
Writer: webapp-20261025-001#7
用途：V2 命令式頁面模組規範 + UI 結構與術語（通用）

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

**與 V1 的差異**：V1 頁面為宣告式 Schema（`title`／`data`／`state`／`derived`／`blocks`／`customMount`），由 `page-engine` 解讀；V2 廢除 `page-engine`，改由頁面模組自行掌控生命週期，路由僅負責載入與掛載。

---

## 二、V1 Schema 遺產（供歷史追溯，非 V2 強制）

> 以下 §二～§六 為 V1 Schema 架構的欄位定義，僅供舊專案參考。**V2 新專案不得再使用 Schema 宣告式**，改用 §一 的命令式模組。

### 2.1 Schema 欄位（V1）

| 欄位 | 類型 | 說明 |
|---|---|---|
| `title` | string | 頁面標題 |
| `data` | object | Firebase 訂閱配置 |
| `state` | object | 響應式狀態初始值 |
| `derived` | object | 衍生資料計算 |
| `blocks` | array | UI 區塊 |
| `onYearMonthChange` | function | 年月變更 hook（可選） |
| `customMount` | function | 逃生艙（可選） |

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

### 2.5 ctx 提供（V1）

| 方法 | 用途 |
|---|---|
| `ctx.onDataChange(fn)` | 訂閱資料變更 |
| `ctx.setState(path, val)` | 設 state |
| `ctx.invalidate(key)` | 觸發重算 |

### 2.6 customMount 回傳（V1）

| 欄位 | 說明 |
|---|---|
| `destroy` | 清理函式 |

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
| 6 | 渲染列表（`renderTable` 或 `renderCards`） | 依 `AppState.getCurrentView()` 選擇 |
| 7 | 在 `destroy()` 中釋放所有訂閱與監聽 | 防止記憶體洩漏 |

**頁面骨架範例**：

```js
export default {
  _unsub: null,

  async render() {
    renderPageLayout({
      title: '頁面標題',
      headerActions: '<button id="btn-add">新增</button>',
      stats: [],                          // 或傳入 cards 陣列
      controls: '<div id="view-toggle"></div>',
      listContainerId: 'page-list-container',
    });

    renderViewToggle('view-toggle', () => this._renderList());

    this._unsub = listenAllExpenses((list) => {
      this._data = list;
      this._renderList();
    });
  },

  _renderList() { /* renderTable or renderCards */ },

  destroy() {
    if (this._unsub) { this._unsub(); this._unsub = null; }
  }
};
```

---

## 四、HTML 結構（V2 SPA 單頁）

| 元素 | 說明 |
|---|---|
| `<head>` | 2 個 CSS（`theme.css` + `app.css`）、`manifest.json`、PWA meta |
| `<body>` | `#app-loading`（初始載入動畫）、`#app-root`（SPA 掛載點） |
| `<script>` | lucide（defer）、`engine/main.js`（module） |

**與 V1 的差異**：V1 為多頁 HTML（`index.html`、`insurance.html`、`portfolio.html` 等），每頁各自引入 4 個 CSS 與多個 JS；V2 改為單一 `index.html`，其餘頁面由 SPA 路由動態載入。

**骨架生成**：`ui/layout.js` 的 `initLayout()` 會在 `#app-root` 內生成 `<div class="app-shell">`，包含側邊欄、navbar、`#app-content`。各頁面只需往 `#app-content` 填充內容。

---

## 五、常見錯誤（V2）

| # | 錯誤 | 正確 |
|---|---|---|
| 1 | `destroy()` 未釋放監聽器 | 必須記錄 unsubscribe 並在 `destroy()` 呼叫 |
| 2 | 動態值用快照 | 內部讀取 `AppState.getYearMonth()`，不可在 mount 時快照一次 |
| 3 | 事件監聽累積 | 同一容器重複綁定時，用 `onclick` 屬性賦值或先 `removeEventListener` |
| 4 | 動態注入未清空 | 先 `container.innerHTML = ''` 或 `textContent = ''` |
| 5 | 在頁面模組直接操作 Firebase | 走 `db/read.js`／`db/write.js`／`domain/api-client.js` |
| 6 | 未匯出 `render` | 路由會拋出「頁面模組未匯出 render」錯誤 |
| 7 | 在 `render()` 內同步阻塞等待資料 | 先繪製骨架，再非同步載入資料 |

---

## 六、UI 結構與術語（通用，V2 保留）

### 6.1 頁面結構層級

| 層級 | 術語 | 說明 | 範例 |
|---|---|---|---|
| L1 | Page（頁面） | 一個 SPA 路由 | `/dashboard` |
| L2 | Section（區塊） | 頁面內垂直堆疊的功能區 | page-header / stats |
| L3 | Row（列） | Section 內水平排列 | toolbar row |
| L4 | Item（元素） | 最小單位 | button / select |

### 6.2 Section 類型

| 術語 | 中文 | 用途 | 標準位置 |
|---|---|---|---|
| page-banner | 提示橫幅 | 說明文字 | 頁面最上 |
| page-header | 頁首 | 標題 + 副標題 + 主要操作 | banner 之後 |
| page-header-actions | 頁首操作區 | 標題行右側 | page-header 內 |
| stats | 統計卡區 | 數字統計 | header 之後 |
| page-controls | 控制列 | 篩選 / 切換 / 年月 | stats 之後 |
| content | 內容區 | 表格 / 卡片 | 最底 |
| empty-state | 空狀態 | 無資料時顯示 | 內容區內 |

### 6.3 控制列元素

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

### 6.4 頁面標準佈局

| 順序 | Section | 內容 |
|---|---|---|
| 1 | page-banner | banner（若有） |
| 2 | page-header | 標題 + 副標題 + 主要操作 |
| 3 | stats | 統計卡 |
| 4 | page-controls | 新增 / 切換 / 年月 / 篩選 |
| 5 | content | 表格 / 卡片 |

> V2 中，上述 1~5 由 `ui/layout.js` 的 `renderPageLayout()` 統一繪製。頁面只需傳入 `title`、`headerActions`、`stats`、`controls`、`listContainerId`。

### 6.5 表頭互動

- 點欄位標題（首次）：升序。
- 點欄位標題（第二次）：降序。
- 點欄位標題（第三次）：清除排序。
- 點欄位旁的 🔽：開下拉面板進行篩選。

---

## 七、關聯檔案

| 主題 | 檔案 |
|---|---|
| ES Module 架構（V2） | W-03-esmodule.md |
| Cloudflare Functions | W-02-functions.md |
| 通用錯誤與防呆 | W-07-errors.md |
| 本專案頁面實作 | 詳見專案包（如 `90-P-Map.md`） |

---

/* ═══ EOF ═══
F: W-05-schema.md
V: 1792901260
W: webapp-20261025-001#7
═══ */