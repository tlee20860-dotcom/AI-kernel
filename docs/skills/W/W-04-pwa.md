# W-04 PWA + Service Worker 規則（Web App 通用）

最後更新：2026-10-30
用途：PWA + SW 通用規則與 iOS 相容性實作細節

---

## 一、Service Worker 策略

| 策略 | 用途 |
|---|---|
| network-first | 開發階段（保新鮮） |
| cache-first | 正式階段（保速度） |
| stale-while-revalidate | 折衷 |

**選擇建議**：依專案需求決定，通常開發期使用 network-first，正式期可切換為 cache-first。若採用 Vite 打包，建議使用 `vite-plugin-pwa` 自動生成 SW 檔。

### 1.1 實作防呆（跨域排除）
在實作 `fetch` 攔截時，**必須**排除跨域請求（如 Firebase API），否則會導致登入或資料庫連線失敗。
```javascript
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  
  // 💡 關鍵：排除跨域請求（如 Firebase API）與 Chrome 擴充功能
  if (url.origin !== location.origin) return;
  
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response.ok) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
        }
        return response;
      })
      .catch(() => {
        return caches.match(event.request);
      })
  );
});
```

---

## 二、靜態資源與版本管理

| 項目 | 說明 |
|---|---|
| SW_VERSION | 全站統一（每次部署必須更新版本號以觸發快取更新） |
| 更新 | 改版本號觸發更新 |

---

## 三、PWA 核心檔案規範

一個完整的 PWA 專案，根目錄必須包含以下檔案：

1. **`manifest.json`**：定義 App 名稱、啟動路徑、顯示模式（`standalone`）、主題色與圖示。
2. **`sw.js`**（Service Worker）：處理靜態資源快取與離線邏輯。
3. **圖示資料夾 (`public/icons/`)**：至少需包含圖示檔案。

### 3.1 圖示防呆與實作規範（實戰簡化版）

舊版規範要求提供多張圖示（192x192、512x512），但實戰發現這會增加設計與替換的麻煩。**現行標準做法：只需一張高解析度圖示**。

- **準備一張 `icon.png`**：尺寸為 `1024x1024`。
- **放置位置**：`public/icons/icon.png`。
- **`manifest.json` 設定**：
  ```json
  "icons": [
    {
      "src": "/icons/icon.png",
      "sizes": "1024x1024",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
  ```
  *(註：`purpose: "any maskable"` 允許 Android 系統自動裁切為圓形或其他形狀，避免留白。)*

### 3.2 `manifest.json` 標準結構

| 屬性 | 說明 | 範例 |
|---|---|---|
| `name` | 完整名稱 | `"UPGRADE-WO 生產進度控制台"` |
| `short_name` | 桌面圖示下方名稱 | `"UPGRADE"` |
| `start_url` | 啟動路徑 | `"/"` |
| `display` | 顯示模式 | `"standalone"`（隱藏瀏覽器網址列，像原生 App） |
| `theme_color` | 瀏覽器頂部顏色 | `"#6366F1"` |
| `background_color`| 啟動畫面背景色 | `"#F4F7FB"` |
| `icons` | 圖示陣列 | 見 3.1 規範 |

---

## 四、iOS 相容性實作（最重要防呆）

**痛點**：Android Chrome 只要加了 `manifest.json` 就能完美安裝；但 **iOS Safari 對 PWA 的支援較為破碎**，必須在 `index.html` 的 `<head>` 中額外加入專屬的 Meta 標籤，否則「加入主畫面」後依然會顯示網址列，無法全螢幕。

### 4.1 必須加入的 Meta 標籤

在 `index.html` 中補齊以下設定（**注意圖示路徑與 manifest 一致**）：

```html
<!-- iOS 專用 PWA Meta -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="UPGRADE">
<link rel="apple-touch-icon" href="/icons/icon.png">
```

### 4.2 註冊 Service Worker

必須在系統啟動時（如 `main.js`）加入以下程式碼註冊 SW：

```javascript
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').then(reg => {
      console.log('SW registered:', reg.scope);
    }).catch(err => {
      console.warn('SW registration failed:', err);
    });
  });
}
```

---

## 五、常見錯誤與防呆

| # | 錯誤 | 正確 |
|---|---|---|
| 1 | SW_VERSION 各檔不一致 | 統一版本號，每次部署更新 |
| 2 | 新增檔案未加入快取清單 | 使用打包工具自動生成快取清單 |
| 3 | 忘記更新版本 | 每次部署更新，否則使用者會看到舊畫面 |
| 4 | 只做 manifest 沒做 iOS meta | iOS 裝置無法全螢幕顯示 |
| 5 | 圖示路徑錯誤或缺失 | 必須確保 `public/icons/icon.png` 存在，否則安裝會失敗（顯示無法安裝此應用程式） |
| 6 | 跨域 API 被快取 | 在 `fetch` 中加入 `url.origin !== location.origin` 排除 |

---

## 六、關聯檔案

| 主題 | 檔案 |
|---|---|
| 本專案 SW 實作 | 詳見專案包（如 sw.js / manifest.json） |
| 事故日誌 | 詳見專案包（如 P-Errors.md） |

---

/* ═══ EOF ═══
F: AI-kernel/docs/skills/W/W-04-pwa.md
V: 1792928800
W: UPGRADE-004
═══ */