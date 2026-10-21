# W-02 Cloudflare Pages Functions 規則（Web App 通用）

最後更新：2026-10-21
Version: 1792581003
Writer: ai-system-20261021-004#3
用途：CF Pages Functions 通用規則（跨專案）

---

## 一、檔案結構

| 規則 | 說明 |
|---|---|
| 底線前綴 | _config.js / _helpers.js / _admin.js |
| Catch-all | [[path]].js 統一分派 |
| 禁止獨立 xxx.js | 用底線前綴 |
| 禁止 shim re-export | CF 不支援跨檔 re-export |

---

## 二、環境變數

| 項目 | 說明 |
|---|---|
| 錯誤 | process.env.DB_TARGET |
| 正確 | handler 參數 { env } → env.DB_TARGET |
| 傳遞 | 每個 onRequest* 開頭呼叫 initConfig(env) |
| 生效條件 | 設定後必須重新部署 |

---

## 三、initConfig 模式

| 步驟 | 動作 |
|---|---|
| 1 | onRequest 開頭呼叫 initConfig(context.env) |
| 2 | _config.js 用 export let 保留舊引用 |
| 3 | 其他模組 import 該 let（live binding） |
| 4 | initConfig 更新 let 值 → 所有引用同步更新 |

**禁止**：直接 export const（無法更新）。

---

## 四、路由規則

| 路徑 | 處理 |
|---|---|
| 靜態檔案 | 所有連結帶 .html |
| API | /api/* 由 [[path]].js 分派 |
| 根路徑 | _redirects 不要對 / 加規則 |

---

## 五、常見錯誤

| # | 錯誤 | 正確 |
|---|---|---|
| 1 | 每個 URL 對應獨立實體檔 | 用 Catch-all + 底線前綴 |
| 2 | 用 shim re-export | 直接用底線檔 |
| 3 | 忘記 initConfig | 每個 onRequest 開頭必呼叫 |
| 4 | 移除既有 export | 用 export let 保留 |
| 5 | 設定後未重新部署 | 必須重部署才生效 |

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

*(註：各專案可依業務需求額外定義專屬錯誤碼，如 NAME_DUPLICATE)*

---

## 七、關聯檔案

| 主題 | 檔案 |
|---|---|
| 本專案 API 契約 | 詳見專案包（如 P-08-api.md） |
| 本專案事故 | 詳見專案包（如 P-10-incident.md） |
| Firebase 結構 | W-01-firebase.md |

---

/* ═══ EOF ═══
F: W-02-functions.md
V: 1792581003
W: ai-system-20261021-004#3
═══ */