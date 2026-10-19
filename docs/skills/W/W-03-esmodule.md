# W-03 純前端 ES Module 架構（Web App 通用）

最後更新：B34-3
Version: 1791899620
Batch: B34-3
Writer: A20261013-004#065
用途：純 HTML + ES Module 架構通用原則

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
| EOF 必加 | F/V/B/W |

---

## 八、關聯檔案

| 主題 | 檔案 |
|---|---|
| Page Schema | W-05-schema.md |
| PWA + SW | W-04-pwa.md |
| 本專案架構 | P-01-index.md |

---

/* ═══ EOF ═══
F: docs/W-03-esmodule.md
V: 1791899620
B(歷史): B34-3
W: A20261013-004#065
═══ */