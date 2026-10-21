# W-03 純前端 ES Module 架構（Web App 通用）

最後更新：2026-10-21
Version: 1792581004
Writer: ai-system-20261021-004#4
用途：純 HTML + ES Module 架構通用原則與目錄配置

---

## 一、三層架構

| 層 | 職責 | 目錄 |
|---|---|---|
| 資料層 | Firebase RTDB | — |
| 引擎層 | page-engine / data-engine / render-engine | js/engines/ |
| 呈現層 | block / UI 元件 / DOM | js/blocks, js/ui |

**資料流**：

> Firebase RTDB → data-engine → page-engine → derived → block → DOM

---

## 二、核心架構原則

| 原則 | 說明 |
|---|---|
| SSOT 極大化 | 任何知識只存在一處 |
| 宣告式 > 命令式 | 頁面只描述「要什麼」 |
| 舊資料 100% 相容 | 讀取時 normalize |
| 操作邏輯不變 | 只改實作方式 |
| 無補丁 | 能宣告就不手寫 |

---

## 三、5 大 Registry

| Registry | 職責 |
|---|---|
| status-registry | 狀態系統 |
| entity-registry | 名稱解析 |
| label-registry | 顯示文字 |
| column-registry | 表格欄位 |
| constants | 全站常數 |

**附加**：page-metadata-registry

---

## 四、3 大引擎

| 引擎 | 職責 |
|---|---|
| page-engine | 解讀 Schema、生命週期、onDataChange |
| data-engine | Firebase 訂閱 + 衍生 |
| render-engine | 掛載 UI 區塊 |

---

## 五、5 大 Block

| Block | 職責 |
|---|---|
| stats-block | 統計卡 |
| list-block | 列表 |
| filter-block | 篩選列 |
| detail-block | 明細展開 |
| form-block | 表單 Modal |

---

## 六、Page Schema（見 W-05）

---

## 七、檔案規則

| 規則 | 說明 |
|---|---|
| 檔案 ≤ 800 行 | 超過拆檔 |
| 每檔獨立 | 不合併 |
| EOF 必加 | F/V/W 三行 |

---

## 八、標準目錄配置（通用）

| 目錄 | 建議檔數 | 內容職責 |
|---|---|---|
| `js/config` | 5~10 | 常數、環境配置、各類 Registry |
| `js/core` | 5~10 | 狀態管理 (state)、API 核心、登入驗證、共用工具 |
| `js/lib` | 10~20 | 通用邏輯（日期處理、格式化、Modal 封裝） |
| `js/engines` | 3 | page / data / render |
| `js/blocks` | 5 | stats / list / filter / detail / form |
| `js/ui` | 5~10 | 獨立 UI 元件（toast, modal, tabs） |
| `js/layout` | 3 | 外框佈局（navbar, sidebar, app-shell） |
| `js/entity` | 3~5 | 實體資料的解析、驗證與 Modal |
| `js/shared` | 5~15 | 跨頁面共用元件（表格、卡片） |
| `js/pages` | 依頁面數 | 各頁面的 Schema 定義 |
| `functions/api` | 依 API 數 | CF Pages Functions 後端邏輯 |
| `css/` | 4~6 | theme / layout / components / utilities |
| 根目錄 | — | `*.html` 頁面、`sw.js`、`manifest.json` |

---

## 九、關聯檔案

| 主題 | 檔案 |
|---|---|
| Page Schema | W-05-schema.md |
| PWA + SW | W-04-pwa.md |
| 本專案架構 | 詳見專案包（如 P-01-index.md） |

---

/* ═══ EOF ═══
F: W-03-esmodule.md
V: 1792581004
W: ai-system-20261021-004#4
═══ */