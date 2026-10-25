## 📄 AI-kernel/docs/skills/W/W-03-esmodule.md

# W-03 純前端 ES Module 架構（Web App 通用）

最後更新：2026-10-25
Version: 1792901250
Writer: webapp-20261025-001#6
用途：純 HTML + ES Module 架構通用原則與目錄配置（V2 版）

---

## 一、分層架構（V2）

| 層 | 職責 | 目錄 |
|---|---|---|
| 資料層 | Firebase RTDB 讀寫與監聽 | `db/`（read / write）、`config/firebase.js` |
| 領域層 | 業務邏輯（純函式）與 API 呼叫 | `domain/` |
| 路由層 | SPA 路由分派與啟動 | `engine/` |
| 呈現層 | 頁面模組與 UI 元件 | `pages/`、`ui/` |
| 設定層 | 常數、狀態、設定檔 | `config/` |

**資料流（V2）**：

> Firebase RTDB → `db/read.js` → `pages/*.js`（render）→ `ui/*`（DOM）
> `config/state.js`（AppState）⇄ 全域事件總線 ⇄ 各頁面監聽

**與 V1 的差異**：

| 項目 | V1 | V2 |
|---|---|---|
| 主體 | page-engine 解讀 Schema | 頁面模組自行 render |
| 資料流 | data-engine 衍生 → block | 頁面直接讀 db → 渲染 |
| 元件 | blocks（stats/list/filter…） | ui（table/cards/form/modal…） |
| 路由 | 多 HTML + 各頁入口 | SPA + Hash 路由（`engine/router.js`） |
| 業務邏輯 | lib/ + engines/ | `domain/`（純函式抽離） |

---

## 二、核心架構原則

| 原則 | 說明 |
|---|---|
| SSOT 極大化 | 任何知識只存在一處 |
| 舊資料 100% 相容 | 讀取時 `normalize`（如 `config/status.js` 的 `LEGACY_MAP`） |
| 讀寫分離 | `db/read.js`（`listen` / `getOnce`）、`db/write.js`（`set` / `update` / `push` / `remove`） |
| 純函式業務邏輯 | `domain/*.js` 不碰 DOM、不碰 Firebase，方便單元測試 |
| 狀態集中 | `config/state.js` 單一 AppState，含事件總線 |
| 防注入 | 所有 HTML 插值必經 `ui/format.js` 的 `esc()` |
| 無框架 | 不引入 React / Vue / Svelte |

---

## 三、Registry 與設定檔（V2）

| 檔案 | 職責 |
|---|---|
| `config/constants.js` | 全站常數、路由表 `ROUTES`、側邊欄 `SIDEBAR_GROUPS`、角色 `ROLES` |
| `config/state.js` | `AppState`：使用者、家庭、年月、主題、檢視模式、事件總線 |
| `config/firebase.js` | Firebase 初始化、環境切換（old／new）、`IS_READONLY` |
| `config/entity-registry.js` | 實體名稱解析（`resolveName`）、列表快取 |
| `config/columns.js` | 表格欄位定義 `COLUMNS` 與解析器 `RESOLVERS` |
| `config/status.js` | 狀態代碼、舊資料相容映射、`normalize`／`label`／`badgeClass` |
| `config/app-config.js` | 平台預設與家庭覆寫合併（`getOptions`／`getYearRange`／`getUIConstants`） |

**與 V1 的差異**：V1 的 `status-registry`、`entity-registry`、`label-registry`、`column-registry` 四大 Registry，在 V2 中合併為上述檔案；`label-registry` 的功能併入 `status.js` 的 `label()`。

---

## 四、核心引擎（V2）

| 檔案 | 職責 |
|---|---|
| `engine/main.js` | 系統啟動、`onAuthStateChanged`、初始化 AppState／Config／EntityRegistry |
| `engine/router.js` | Hash 路由分派、路由守衛、頁面載入與銷毀 |

**與 V1 的差異**：V1 的 `page-engine`／`data-engine`／`render-engine` 三大引擎已廢除。V2 中由頁面模組自行掌控生命週期，路由僅負責載入與掛載。

---

## 五、頁面與 UI（V2）

### 5.1 頁面模組

每個 `pages/*.js` 匯出單一物件，採命令式介面：

```js
export default {
  async render() { /* 繪製與綁定事件 */ },
  destroy() { /* 清理監聽器、取消訂閱 */ }
};
```

**與 V1 的差異**：V1 頁面為宣告式 Schema（`title`／`data`／`state`／`derived`／`blocks`／`customMount`），由 page-engine 解讀。V2 改為命令式模組，Schema 不再強制。

### 5.2 UI 元件

| 檔案 | 職責 |
|---|---|
| `ui/layout.js` | App Shell 骨架、`renderPageLayout` 統一頁面排版、`updateNavbar` |
| `ui/table.js` | `renderTable`（表格）、`renderCards`（卡片） |
| `ui/form.js` | `createForm` 動態表單建構器 |
| `ui/modal.js` | `openModal`／`closeModal`／`openConfirm`／`openPrompt` |
| `ui/toast.js` | `showToast` 全域提示 |
| `ui/controls.js` | `renderYearMonth`／`renderViewToggle`／`renderFilterBar` |
| `ui/format.js` | `esc`／`formatHKD`／`formatNumber`／`todayISO`／`debounce` |

**與 V1 的差異**：V1 的 `blocks/`（stats／list／filter／detail／form）已廢除，功能併入 `ui/table.js` 與 `ui/form.js`，並由 `renderPageLayout` 統一外框。

---

## 六、檔案規則

| 規則 | 說明 |
|---|---|
| 檔案 ≤ 800 行 | 超過拆檔 |
| 每檔獨立 | 不合併 |
| EOF 必加 | `.md` 用三行（F／V／W）；`.js`／`.css` 用語言支援的註解包裹；`.json` 豁免 |
| import 路徑 | 相對路徑，不用絕對路徑或 CDN 別名（Firebase SDK 除外，走 `https://www.gstatic.com/...`） |
| 事件監聽 | 頁面 `destroy()` 必須移除所有 `addEventListener`／`AppState.on` 訂閱 |

---

## 七、標準目錄配置（V2）

| 目錄 | 建議檔數 | 內容職責 |
|---|---|---|
| `admin/` | 1~3 | 平台管理員專用頁面（如 `admin.js`） |
| `config/` | 5~10 | 常數、狀態、Firebase、EntityRegistry、欄位定義、狀態系統、App Config |
| `db/` | 2~3 | `read.js`（監聽與讀取）、`write.js`（寫入與防呆）、`index.js`（統一出口） |
| `domain/` | 4~8 | 純函式業務邏輯（`insurance`／`settlement`／`fund`／`bank`）、`api-client.js`、`auth.js` |
| `engine/` | 2 | `main.js`（啟動）、`router.js`（路由） |
| `pages/` | 依頁面數 | 各頁面模組（命令式 `render`／`destroy`） |
| `ui/` | 5~10 | 佈局、表格、表單、Modal、Toast、控制列、格式化 |
| `css/` | 2~6 | `theme.css`（變數與重置）、`app.css`（元件樣式）、可選 `pages/*.css` |
| `functions/api/` | 依 API 數 | CF Pages Functions（`[[path]].js` + `config.js`／`helpers.js`／`handlers*.js`） |
| `icons/` | 1~3 | PWA 圖示 |
| 根目錄 | — | `index.html`（SPA 唯一入口）、`sw.js`、`manifest.json`、`meta.json` |

**與 V1 的差異**：V1 的 `js/config`／`js/core`／`js/lib`／`js/engines`／`js/blocks`／`js/ui`／`js/layout`／`js/entity`／`js/shared`／`js/pages` 十層結構已簡化為 V2 的扁平結構；HTML 由多頁改為單頁 SPA。

---

## 八、關聯檔案

| 主題 | 檔案 |
|---|---|
| Page Schema 與 UI 規範 | W-05-schema.md |
| PWA + SW | W-04-pwa.md |
| Cloudflare Functions | W-02-functions.md |
| 本專案架構 | 詳見專案包（如 `90-P-Map.md`） |

---

/* ═══ EOF ═══
F: W-03-esmodule.md
V: 1792901250
W: webapp-20261025-001#6
═══ */