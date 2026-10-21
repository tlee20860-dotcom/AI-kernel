## FILE: docs/r-rules/R-03-terms.md
<<<<<<< OLD
V: 1792569000
W: ai-system-20261021-003#51
=======
V: 1792572000
W: ai-system-20261021-003#57
>>>>>>> NEW

## FILE: docs/r-rules/R-02-patterns.md
<<<<<<< OLD
V: 1792412000
W: ai-system-20261019-010#207
=======
V: 1792572000
W: ai-system-20261021-003#57
>>>>>>> NEW

## FILE: docs/r-rules/R-00-rules.md
<<<<<<< OLD
| MUST | 使用 Patch 模式 | OLD 字串唯一出現；單區塊內容 ≤3 行（EOF 替換區塊豁免）；不含空行；含 Emoji 或特殊符號確保唯一 | OLD 唯一且符合行數 | OLD 多次出現；區塊含空行 | 核對 OLD 唯一性 |
=======
| MUST | 使用 Patch 模式 | OLD 字串唯一出現；單區塊內容 ≤3 行（EOF 替換區塊豁免）；不含空行；含 Emoji 或特殊符號確保唯一；**每個被 Patch 的檔案必須附 EOF 替換區塊，更新 V 與 W** | OLD 唯一且符合行數；檔尾 Version 已更新 | OLD 多次出現；區塊含空行；Patch 後 Version 未變 | 核對 OLD 唯一性與 EOF Version |
>>>>>>> NEW

## FILE: docs/r-rules/R-00-rules.md
<<<<<<< OLD
V: 1792563000
W: ai-system-20261021-003#46
=======
V: 1792572000
W: ai-system-20261021-003#57
>>>>>>> NEW