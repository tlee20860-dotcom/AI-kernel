## 📄 AI-kernel/docs/skills/W/W-03-esmodule.md

# W-03 純前端 ES Module 架構（Web App 通用）

最後更新：2026-10-25
Version: 1792901600
Writer: webapp-20261025-001#16
用途：純 HTML + ES Module 架構通用原則與目錄配置（V2 版）

---

## 零、架構契約與依賴鐵律（MUST）

為了避免專案重蹈 V1 時期檔案膨脹與耦合的覆轍，AI 在撰寫或修改任何 Web App 程式碼時，必須嚴格遵守以下契約。

### 0.1 依賴方向（單向）

允許的依賴方向只能由上往下（箭頭代表可以 import）：

> `config/` ➜ `db/` ➜ `domain/` ➜ `ui/` ➜ `pages/`

### 0.2 架構契約表

| 編號 | Level | Trigger | Requirement | Counter-example（AI 的常見偷懶行為） |
|---|---|---|---|---|
| W03-R01 | **MUST NOT** | 撰寫或修改 `ui/*.js` | 禁止 import `domain/`、`db/`、`pages/`、`lib/`。UI 層只能依賴 `config/` 與 `ui/` 內部的其他檔案。 | 在 `ui/table.js` 裡面 import `lib/expense-modal.js` 來處理特殊按鈕；在 `ui/form.js` 直接引入 `db/write.js` 寫入資料。 |
| W03-R02 | **MUST NOT** | 撰寫或修改 `domain/*.js` | 禁止 import `ui/`、`pages/`。領域層只能依賴 `config/`、`db/`。 | 在 `domain/insurance.js` 裡面操作 DOM（如 `document.getElementById`）；在 `domain/settlement.js` 呼叫 `ui/toast.js` 顯示提示。 |
| W03-R03 | **MUST NOT** | 撰寫或修改 `pages/*.js` | 禁止 import 其他 `pages/*.js`。頁面之間不得互相依賴。 | 在 `pages/input-center.js` 裡面 import `pages/dashboard.js` 的函式來共用變數。 |
| W03-R04 | **MUST** | 涉及業務計算、金額、狀態轉換 | 必須寫在 `domain/` 的純函式中，禁止在 `pages/` 或 `ui/` 中直接寫複雜的 `for` 迴圈或 `reduce` 進行計算。 | 在 `pages/settlements.js` 裡面直接寫 `const total = list.reduce((s, r) => s + r.amount, 0)` 來算總額（應呼叫 `domain/settlement.js` 的函式）。 |
| W03-R05 | **MUST** | 新增實體表單或列表 | 必須呼叫 `ui/form.js` 的 `createForm()` 與 `ui/table.js` 的 `renderTable()`，禁止手寫 `<form>` 或 `<table>` HTML。 | 在 `pages/input-center.js` 直接寫死一段 `<form><input...></form>` HTML 標籤。 |
| W03-R06 | **MUST** | 撰寫涉及資料庫的頁面 | 只能透過 `db/read.js`（讀）、`db/write.js`（寫）或 `domain/api-client.js`（打 API）操作資料，禁止直接引入 Firebase SDK 的 `ref`, `set` 等。 | 在 `pages/portfolio.js` 直接 `import { ref, set } from 'https://...firebase...'` 並寫入資料。 |

### 0.3 交付前自檢清單（AI MUST 遵守）

AI 在輸出任何 `.js` 檔案前，**MUST** 檢查檔案頂部的所有 `import` 語句，確認沒有違反 `W03-R01` 至 `W03-R06`。若有違反，必須重構後才可輸出，不得以「為了方便」為由妥協。

---

## 一、分層架構（V2）

| 層 | 職責 | 目錄 |
|---|---|---|
| 設定層 | 常數、狀態、設定檔 | `config/` |
| 資料層 | Firebase RTDB 讀寫與監聽 | `db/`（read / write）、`config/firebase.js` |
| 領域層 | 業務邏輯（純函式）與 API 呼叫 | `domain/` |
| 呈現層 | 頁面模組與 UI 元件 | `pages/`、`ui/` |
| 路由層 | SPA 路由分派與啟動 | `engine/` |
| 工具層 | 通用輔助（無狀態） | `lib/`（需嚴格審查，避免濫用） |

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
V: 1792901600
W: webapp-20261025-001#16
═══ */