## 📄 AI-kernel/docs/skills/W/W-02-functions.md

# W-02 Cloudflare Pages Functions 規則（Web App 通用）

最後更新：2026-10-25
Version: 1792901240
Writer: webapp-20261025-001#5
用途：CF Pages Functions 通用規則（跨專案）

---

## 一、檔案結構

| 規則 | 說明 |
|---|---|
| Catch-all 入口 | `[[path]].js` 統一分派，所有 `/api/*` 請求均由此進入 |
| 命名慣例（V2） | 直接命名：`config.js`、`helpers.js`、`handlers.js`。**不再強制底線前綴**（V1 的 `_config.js`、`_helpers.js` 為歷史遺產，V2 起改為直接命名） |
| 職責拆分 | 允許按職責拆檔：`handlers-core.js`（業務）、`handlers-report.js`（報表）、`handlers-admin.js`（管理），由 `handlers.js` 統一出口 |
| 統一出口 | `handlers.js` 用 `export * from './handlers-*.js'` 匯總，`[[path]].js` 只需 import `handlers.js` |
| re-export | **V2 實測可用**：CF Pages 支援 ES Module re-export。V1 的「禁 shim re-export」限制已解除，但仍應避免多層 re-export 鏈（≤ 2 層） |
| 禁止 | 禁止在 `functions/api/` 之外散落後端邏輯 |

---

## 二、環境變數

| 項目 | 說明 |
|---|---|
| 錯誤 | `process.env.DB_TARGET`（CF Pages 不支援） |
| 正確 | handler 參數 `{ env }` → `env.DB_TARGET` |
| 傳遞 | 每個 `onRequest*` 開頭呼叫 `initConfig(context.env)` |
| 生效條件 | 設定後必須重新部署 |

---

## 三、initConfig 模式（V2 標準）

| 步驟 | 動作 |
|---|---|
| 1 | `onRequest*` 開頭呼叫 `initConfig(context.env)` |
| 2 | `config.js` 用 `export let` 保留可變引用 |
| 3 | 其他模組 `import { FIREBASE_DB_URL } from './config.js'`（live binding） |
| 4 | `initConfig` 更新 `let` 值 → 所有 import 端同步更新 |

**禁止**：直接 `export const`（無法更新）。

**V2 實作範例**（`config.js`）：

```js
export let FIREBASE_DB_URL  = '...';
export let FIREBASE_API_KEY = '...';

export function initConfig(env) {
  const target = (env && env.DB_TARGET) || 'new';
  FIREBASE_DB_URL  = _DB_CONFIGS[target].url;
  FIREBASE_API_KEY = _DB_CONFIGS[target].apiKey;
}
```

---

## 四、路由規則

| 路徑 | 處理 |
|---|---|
| 靜態檔案 | 所有連結帶 `.html` |
| API | `/api/*` 由 `[[path]].js` 分派 |
| 根路徑 | `_redirects` 不要對 `/` 加規則 |

---

## 五、常見錯誤

| # | 錯誤 | 正確 |
|---|---|---|
| 1 | 每個 URL 對應獨立實體檔 | 用 Catch-all + 職責拆分檔 |
| 2 | 多層 re-export 鏈（> 2 層） | 控制在 1~2 層，`[[path]].js` → `handlers.js` → `handlers-*.js` |
| 3 | 忘記 `initConfig` | 每個 `onRequest*` 開頭必呼叫 |
| 4 | 移除既有 `export` | 用 `export let` 保留 |
| 5 | 設定後未重新部署 | 必須重部署才生效 |
| 6 | 在 `config.js` 用 `export const` 存 DB URL | 用 `export let` + `initConfig` |

---

## 六、Response 格式與錯誤碼

| 欄位 | 值 |
|---|---|
| ok | true / false |
| error | ERROR_CODE（失敗時） |
| message | 錯誤訊息（失敗時） |

**通用 ERROR_CODE 對照**：

| Code | HTTP | 說明 |
|---|---|---|
| UNAUTHORIZED | 401 | 未登入 |
| FORBIDDEN | 403 | 無權限 |
| MISSING_FIELDS | 400 | 缺少欄位 |
| INVALID_BODY | 400 | 無效 body |
| BAD_REQUEST | 400 | 請求錯誤 |
| NOT_FOUND | 404 | 找不到 |
| CONFLICT | 409 | 衝突 |
| INTERNAL | 500 | 內部錯誤 |

*(註：各專案可依業務需求額外定義專屬錯誤碼，如 `NAME_DUPLICATE`、`CODE_DUPLICATE`)*

---

## 七、V1 → V2 演進摘要

| 項目 | V1 | V2 |
|---|---|---|
| 檔名 | `_config.js`、`_helpers.js`、`_xxx.js` | `config.js`、`helpers.js`、`handlers-*.js` |
| 拆分方式 | 按業務域拆（`_admin.js`、`_bank.js`…） | 按職責拆（core / report / admin），由 `handlers.js` 匯總 |
| re-export | 禁止 | 允許（≤ 2 層） |
| 環境變數 | 混亂（`process.env` vs `{ env }`） | 統一走 `initConfig(env)` |
| 分派入口 | `[[path]].js` | `[[path]].js`（不變） |

---

## 八、關聯檔案

| 主題 | 檔案 |
|---|---|
| 本專案 API 契約 | 詳見專案包（如 `90-P-Data.md`） |
| 本專案事故 | 詳見專案包（如 `90-P-Errors.md`） |
| Firebase 結構 | W-01-firebase.md |
| 通用錯誤 | W-07-errors.md |

---

/* ═══ EOF ═══
F: W-02-functions.md
V: 1792901240
W: webapp-20261025-001#5
═══ */