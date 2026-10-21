# W-07 Web App 通用錯誤與防呆

最後更新：2026-10-21
Version: 1792581008
Writer: ai-system-20261021-004#8
用途：沉澱 Web App 開發過程中的通用錯誤與防範措施

---

## 一、通用開發錯誤（交付前檢查）

| # | 類型 | 防止做法 |
|---|---|---|
| 1 | 估算前未掃描實際檔數 | 先全域掃描（grep） |
| 2 | 「統一」誤解為各檔都改 | 統一 = 邏輯集中一處 |
| 3 | 未檢查現有 API 複用 | 先找複用機會 |
| 4 | 未思考集中層強制 | 優先改集中層 |
| 5 | 動態值用快照 | 內部讀取狀態（AppState） |
| 6 | 動態注入未清空 | 先執行 `textContent = ''` |
| 7 | 全站結構改動未完整掃描 | 完整掃描後才動 |
| 8 | 自我引入 bug | 交付前全鏈路檢查 |

---

## 二、Cloudflare Pages (CF Pages) 教條

| 教訓 | 說明 |
|---|---|
| Functions 路由 | 每個 URL 應對應獨立實體檔或統一 Catch-all |
| 不支援 shim | 用底線前綴（`_xxx.js`），避免跨檔 re-export |
| 靜態檔案 | 所有連結需帶 `.html` |
| _redirects | 不要對 `/` 加規則，避免無限迴圈 |
| 環境變數 | 走 handler `{ env }`，非 `process.env` |

---

## 三、Page Engine 與 ES Module 教條

| 教訓 | 說明 |
|---|---|
| customMount | 必須支援，供複雜邏輯逃生 |
| onDataChange | 必須支援非同步資料流 |
| 依賴圖 | key 與事件觸發必須一致 |
| undefined | derived 計算需容忍初始 undefined |
| 動態值 | 必須內部讀取最新狀態，不可快照 |
| 動態注入 | 需先清空既有內容 |
| esc 函式 | 必須從統一 `lib/dom.js` 導入 |
| format 函式 | 必須從統一 `lib/format.js` 導入 |
| 檔案搬移 | 必須全域搜尋並替換舊路徑 |
| 無補丁 | 寧願整檔重寫，減少修補風險 |

---

## 四、關聯檔案

| 主題 | 檔案 |
|---|---|
| 通用 SOP | W-06-sop.md |
| ES Module 架構 | W-03-esmodule.md |
| 體系學習日誌 | `R-04-learning.md` |

---

/* ═══ EOF ═══
F: W-07-errors.md
V: 1792581008
W: ai-system-20261021-004#8
═══ */