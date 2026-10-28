## 📄 AI-kernel/docs/skills/W/W-00-startup.md

# W-00 領域啟動卡（Web App）

最後更新：2026-10-28
用途：Web App 領域的啟動卡（工具鏈 / 架構模式 / 慣例 / 載入方式）

---

> **【強制規則宣告】**
> 本 W 包（W-00 ~ W-07）為 Web App 領域之**強制性規則（Domain Rules）**。AI 處理所有 Web App 相關任務時，**MUST** 遵守本包規範。違反 W 包之架構契約（如 W-03）或 SOP，視同違反體系鐵律。

---

## 零、Web App 架構思考模型（給 AI 的思考框架）

在動手寫任何 Web App 程式碼之前，AI **MUST** 先問自己以下四個問題，並在方案中給出答案：

1. **資料會變嗎？（數據驅動思維）**
   - 如果 Excel 欄位或資料庫 Schema 日後會擴充，**絕對不准寫死 HTML 表格**。必須設計「動態 Schema」與「視圖配置」，讓畫面由資料自動生成。
2. **事件綁定在哪？（生命週期思維）**
   - 在 SPA（單頁應用）架構中，如果事件綁定在特定按鈕上，只要路由切換、DOM 重繪，事件就會死掉。
   - **標準解法**：一律使用「全域事件委派（Event Delegation）」，綁定在 `document` 上，透過 `data-action` 來辨識。
3. **在手機上能看嗎？（響應式思維）**
   - 表格在手機一定會擠壓變形。必須強制設定 `whitespace-nowrap` 與 `min-w-[120px]`，讓表格外層可以「左右滑動」。
4. **發生錯誤會全白嗎？（防呆與降級思維）**
   - `createIcons()` 或任何第三方 UI 庫的初始化，絕對不能放在綁定事件之前，否則報錯會讓按鈕全死。
   - 讀取設定檔時必須有 `Fallback`（預設值），不能因為資料庫少一個欄位就崩潰白屏。

---

## 一、領域定位

| 項目 | 內容 |
|---|---|
| 領域名稱 | Web App |
| 領域前綴 | W |
| 適用範圍 | 純 HTML / CSS / JS 前端 + Serverless 後端 |
| 適用專案 | 所有依循本體系之 Web App 專案 |

---

## 二、技能包清單

| # | 檔案 | 職責 |
|---|---|---|
| 0 | W-00-startup.md（本檔） | 領域啟動卡與架構思考模型 |
| 1 | W-01-firebase.md | Firebase RTDB 結構原則 |
| 2 | W-02-functions.md | Cloudflare Pages Functions 規則 |
| 3 | W-03-esmodule.md | 純前端 ES Module 架構（**含依賴方向鐵律與架構契約**） |
| 4 | W-04-pwa.md | PWA + Service Worker |
| 5 | W-05-schema.md | Web App 頁面規範與 UI 結構 |
| 6 | W-06-sop.md | Web App 通用任務 SOP（**含新專案零到一啟動 SOP**） |
| 7 | W-07-errors.md | Web App 通用錯誤與防呆 |

---

## 三、架構模式選擇矩陣

本體系支援兩種前端架構模式。建立新專案時，AI **MUST** 依下表引導 Ken 選擇，並將選擇結果記錄於專案初始化文件中。

| 維度 | Mode A：純 CDN（無構建） | Mode B：Vite 工程化（現代） |
|---|---|---|
| **適用場景** | 單頁展示、輕量工具、極簡活動頁。 | 複雜後台、多頁面 SPA、需大量 npm 套件之系統。 |
| **套件管理** | CDN 連結（貼在 HTML）。 | `npm install` + `package.json`。 |
| **Tailwind** | CDN 引入（全量載入）。 | 本地編譯（Tree-shaking，體積極小）。 |
| **開發體驗** | 需手動 F5 重整。 | 熱更新（HMR），存檔即時刷新。 |
| **依賴管理** | 全域汙染風險高，無別名。 | 支援 `@/` 別名，嚴格模組化。 |
| **部署流程** | 直接上傳靜態檔案。 | 需執行 `npm run build` 後上傳 `dist/`。 |
| **推薦情境** | 專案預估檔案 < 10 個。 | 專案預估檔案 > 10 個，或需串接多個 npm 套件（如 Excel、PDF）。 |

- **選擇 Mode B 時**：AI MUST 依照 `W-03` 中的「Vite 工程化基礎建設」章節建立 `package.json`、`vite.config.js`、`tailwind.config.js`、`postcss.config.js`。

---

## 四、工具鏈

| 層 | 技術 |
|---|---|
| 前端 | 純 HTML + CSS + ES Module JS（無框架） |
| 後端 | Cloudflare Pages Functions |
| 資料庫 | Firebase RTDB / Firestore |
| 認證 | Firebase Auth（或自訂帳密） |
| 部署 | Cloudflare Pages |
| 版控 | GitHub |

---

## 五、通用慣例

| # | 慣例 |
|---|---|
| 1 | 檔案結構：三層架構（資料 / 引擎 / 呈現） |
| 2 | SSOT 極大化 |
| 3 | 宣告式 > 命令式 |
| 4 | 檔案 ≤ 800 行 |
| 5 | 每個 .js / .html / .css / .md 結尾加 EOF |
| 6 | 無框架，不引入 React / Vue |

---

## 六、領域常見任務

| 任務 | 引用 |
|---|---|
| **新專案啟動** | W-06 §零 |
| 新增頁面 | W-03 + W-05 + W-06 §一 |
| 改資料結構 | W-01 |
| 改 Functions | W-02 |
| 改 PWA | W-04 |
| 改 Schema / UI | W-05 |

---

## 七、領域常見錯誤

| # | 錯誤 | 正確 |
|---|---|---|
| 1 | 用 process.env（CF Pages 不支援） | handler 參數 { env } |
| 2 | 移除既有 export（依賴模組崩潰） | 用 export let 保留 |
| 3 | 動態值用快照 | 內部讀 AppState |
| 4 | 動態注入未清空 | 先 textContent = '' |
| 5 | 全站結構改動未完整掃描 | 改前完整掃描 |
| 6 | UI 層反向依賴業務層 | 嚴格遵守 W-03 依賴契約 |
| 7 | SPA 按鈕點不到 | 改用全域事件委派（見 W-03） |
| 8 | 表格在手機破版 | 加上 whitespace-nowrap（見 W-05） |
| 9 | Excel 尾端垃圾資料 | 遇到空值 break（見 W-07） |

---

## 八、未來擴充提示

若需要新增 Web App 技術（如 WebSocket / Web Worker），新增 `W-08-xxx.md` 並更新本清單。

---

## 九、關聯檔案

| 主題 | 檔案 |
|---|---|
| 體系四檔 | `IP.md`、`AP.md`、`RP.md`、`UP.md` |
| Firebase RTDB | W-01-firebase.md |
| CF Pages Functions | W-02-functions.md |
| ES Module | W-03-esmodule.md |
| PWA + SW | W-04-pwa.md |
| Page Schema | W-05-schema.md |
| 通用 SOP | W-06-sop.md |
| 通用錯誤 | W-07-errors.md |

---

/* ═══ EOF ═══
F: AI-kernel/docs/skills/W/W-00-startup.md
V: 1792917101
W: UPGRADE-002
═══ */