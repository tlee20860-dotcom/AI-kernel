# W-08 Vue 3 與 Supabase 架構（Web App 通用）

最後更新：2026-11-06
用途：規範 Mode C（Vue 3 + Vite + Element Plus + Supabase）的架構準則與防呆經驗。

---

## 一、架構模式宣告（Mode C）

本體系除了原有的 Mode A（純 CDN）與 Mode B（Vite 純 JS），新增 **Mode C（現代框架 + BaaS）**。
適用於需要高互動性、複雜表單或關聯式資料庫報表的專案。

- **前端框架**：Vue 3 (Composition API) + Vite + Element Plus。
- **後端服務**：Supabase (PostgreSQL + Auth)。
- **部署**：Cloudflare Pages (靜態託管 + Functions 代理)。

---

## 二、核心防呆機制（必讀）

### 2.1 網路封鎖與代理轉發（R-026 變體）
電信商或特定網路環境常會封鎖 `*.supabase.co` 的 DNS 解析。
**解法**：不使用 Supabase 直連，一律透過 Cloudflare Pages Functions 進行反向代理。
- 建立 `functions/api/supabase/[[path]].js`。
- 前端 `supabase.js` 的 `supabaseUrl` 設為 `window.location.origin + '/api/supabase'`。

### 2.2 Cloudflare 代理的 530 崩潰
當 Worker 直接使用 `new Request(..., request)` 轉發帶有 Body 的請求時，會因為 Cloudflare 內部的內部標頭（如 `content-length`, `cf-connecting-ip`）衝突而報 530。
**解法**：
- 嚴格過濾白名單標頭（只留 `apikey`, `authorization`, `content-type` 等）。
- 使用 `request.arrayBuffer()` 或 `request.text()` 安全讀取 Body。
- 回傳 Response 前，刪除 `content-encoding` 與 `content-length`。

### 2.3 虛擬 Email 登入
若希望使用者輸入「帳號」（如 `admin`）而非完整的 Email，需在 `LoginView.vue` 中進行轉換：
`const virtualEmail = `${account}@your-domain.com``。
*注意：Supabase 拒絕 `.local` 結尾的信箱，請使用 `.com` 或 `.app`。*

---

## 三、手機端排版鐵律（Element Plus 專用）

Element Plus 預設偏向桌面端，需額外設定才能完美適配手機：
1. **側邊欄抽屜化**：使用 `transform: translateX(-100%)` 隱藏側邊欄，點擊漢堡選單時才滑出，並加上半透明遮罩。
2. **表格橫向滑動**：將 `<el-table>` 包在 `div.table-wrapper { overflow-x: auto; }` 中。
3. **彈窗三層架構**：`<el-dialog>` 在手機端設定 `width="90%"`，內容過長時依賴內部的滾動條，確保底部按鈕不被擠出畫面。
4. **Grid 轉 Flex**：首頁的統計卡片在電腦用 `grid`，在手機用 `flex` 並允許橫向滑動。

---

## 四、資料庫與權限（Supabase）

- **RLS 開啟**：確保所有資料表啟用 Row Level Security。
- **避免全量覆蓋**：更新資料時使用 `update()`，新增使用 `insert()`，避免使用 `upsert()` 時意外洗掉未傳入的欄位。
- **關聯計算**：善用前端 `computed` 進行跨表數據推算（如「保單月均 × 已繳月數 × 分配比例 = 基金成本」），減少後端 Function 的維護成本。

---

## 五、PWA 與快取

- 使用 `vite-plugin-pwa` 自動生成 `manifest.webmanifest` 與 `sw.js`。
- 確保在 `main.js` 中使用 `registerSW`，並設定 `onNeedRefresh` 提示使用者更新。
- 開發階段若遇「程式碼已更新但網頁未變」，請檢查 Service Worker 是否卡住，可透過無痕模式或 `?v=123` 強制刷新測試。

/* ═══ EOF ═══
F: AI-kernel/docs/skills/W/W-08-vue-supabase.md
V: 1793811800
W: ai-wa-fs-001
═══ */