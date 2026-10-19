# W-04 PWA + Service Worker 規則（Web App 通用）

最後更新：B34-3
Version: 1791899680
Batch: B34-3
Writer: A20261013-004#065
用途：PWA + SW 通用規則

---

## 一、Service Worker 策略

| 策略 | 用途 |
|---|---|
| network-first | 開發階段（保新鮮） |
| cache-first | 正式階段（保速度） |
| stale-while-revalidate | 折衷 |

**本專案選擇**：network-first（ADR-011）。

---

## 二、靜態資源

| 項目 | 說明 |
|---|---|
| STATIC_ASSETS | 清單集中一處 |
| 版本 | SW_VERSION 統一 |
| 更新 | 改版本號觸發更新 |

---

## 三、版本管理

| 項目 | 規則 |
|---|---|
| SW_VERSION | 全站統一 |
| STATIC_ASSETS | 新增檔案必加入 |
| 部署後 | 使用者訪問 2 次才生效（network-first） |

---

## 四、常見錯誤

| # | 錯誤 | 正確 |
|---|---|---|
| 1 | SW_VERSION 各檔不一致 | 統一 |
| 2 | 新增檔案未加 STATIC_ASSETS | 必加 |
| 3 | 忘記更新版本 | 每次部署更新 |

---

## 五、關聯檔案

| 主題 | 檔案 |
|---|---|
| 本專案 SW | sw.js / manifest.json |
| 事故日誌 | P-10-incident.md |

---

/* ═══ EOF ═══
F: docs/W-04-pwa.md
V: 1791899680
B(歷史): B34-3
W: A20261013-004#065
═══ */