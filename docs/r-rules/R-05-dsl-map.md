# R-05 規則 DSL 映射表

用途：將 R-00 之鐵律映射為結構化 DSL，或標「保留散文＋理由」；並映射 R-00 §七 審查機制。本檔為 Phase 1 前置交付物。

---

## 一、映射總表

| 編號 | 類別 | 映射方式 | 理由 |
|---|---|---|---|
| R-001 | 鐵律 | DSL | 狀態＋動作＋sandbox 可判 |
| R-002 | 鐵律 | DSL | 討論期禁輸出檔案內容，可判 |
| R-003 | 鐵律 | DSL | 同檔多改整合，可判 |
| R-004 | 鐵律 | DSL | 未確認禁編號，可判 |
| R-005 | 鐵律 | DSL | 修改前引用原文，可判 |
| R-006 | 鐵律 | DSL | 檔案數標示，可判 |
| R-007 | 鐵律 | 保留散文 | 判斷依結構、語氣，無 predicate 可核 |
| R-008 | 鐵律 | DSL | 交付後禁自印 K，可判 |
| R-009 | 鐵律 | DSL | 繁中，可掃描 |
| R-010 | 鐵律 | DSL | 完整檔交付＋單檔限制，可判 |
| R-011 | 鐵律 | DSL | 斷路器，含輸出位置與豁免剝奪 |
| R-012 | 鐵律 | DSL | 禁主動宣告結束，可判 |
| R-013 | 鐵律 | DSL | 交付後四選項，可判 |
| R-014 | 鐵律 | DSL | 五行標頭，可掃描 |
| R-015 | 鐵律 | 保留散文 | 權限階梯＋降級＋溢出三層，DSL 化易失真 |
| R-016 | 鐵律 | DSL | 四大危機分類，可判 |
| R-017 | 鐵律 | DSL | 專案缺 SOP 三選項，可判 |
| R-018 | 鐵律 | DSL | affected 多目標更新，可判 |
| R-019 | 鐵律 | DSL（checklist） | 觸發條件可列舉清單；「結構大變」保留語意判斷 |
| R-020 | 鐵律 | DSL | 破壞性操作需密語，可掃描 |
| R-021 | 鐵律 | DSL | 全域批次需密語，可掃描 |
| R-022 | 鐵律 | DSL | 強制中止觸發，可判 |
| R-024 | 鐵律 | DSL（checklist） | 重構地圖要素可列舉；「架構升級」保留語意判斷 |
| S-001 | 提問 | DSL（checklist） | 三欄可掃描 |
| S-002 | 提問 | DSL（checklist） | 集中層判定 |
| S-003 | 提問 | DSL（checklist） | 預設值判定 |
| S-004 | 提問 | DSL（checklist） | 版本引用 |
| S-005 | 提問 | DSL（checklist） | R-02 查閱 |
| S-006 | 提問 | DSL（checklist） | 關聯影響三項 |
| S-007 | 提問 | 保留散文 | 三事實需人判斷「何謂並發」 |
| K-001 | 檢查 | DSL | 六項事實證據，可列舉 |
| K-002 | 檢查 | DSL | 檔內搜尋，可掃描 |
| K-003 | 檢查 | DSL | 三項回歸，可列舉 |
| F-001 | 格式 | DSL | 六欄標頭，可掃描 |
| F-002 | 格式 | DSL | 路徑 Code Block，可掃描 |
| F-003 | 格式 | DSL | 三反引號包裹；含代碼塊時外層四反引號 |
| F-004 | 格式 | 保留散文 | 含例外條款，DSL 化反而更複雜 |
| F-005 | 格式 | DSL | EOF 三行，可掃描 |
| F-006 | 格式 | DSL | 狀態總表位置，可判 |
| F-007 | 格式 | DSL | Patch 廢除，可判 |
| F-008 | 格式 | DSL | 章節數＋行數＋嚴格無省略詞彙，可判；含 APPEND_ONLY |

**統計**：DSL 化 36 條；保留散文 4 條（R-007、R-015、S-007、F-004）。

### 1.1 R-00 其他區塊映射

| 編號 | 類別 | 映射方式 | 理由 |
|---|---|---|---|
| R00-0.5 | 規則 | DSL | 廢除跳號＋EVOLUTION 記錄＋限制掃描範圍要求人類協助，可判 |
| R00-7.1 | 審查 | 保留散文 | 三 AI 模式與 CHK 合成物屬結構陳述，無單一 predicate |
| R00-7.2 | 審查 | DSL | 核／不核範圍可列舉 |
| R00-7.3 | 審查 | DSL | L1~L4 層級可列舉 |
| R00-7.4 | 審查 | DSL | LV-01~07 可判；LV-03「理由充分」部分保留散文 |
| R00-7.5 | 審查 | DSL | 升層條件可列舉 |
| R00-7.6 | 審查 | DSL | RV-01~04 可判 |
| 四檔豁免 | 規則 | DSL | 目標包 ∈ {IP,AP,RP,UP} → 熱更新，可判 |
| 混合包阻擋 | 規則 | DSL | input 包含合法與非法檔 → return reject |
| 歸檔 | 流程 | DSL（checklist） | 門檻可列舉 |

**詞表說明**：詞 34 名稱變更、詞 48~77 新增，SSOT 在 `R-03-terms.md`，本表不重複映射。

---

## 二、DSL 映射內容

```yaml
rules_dsl:
  # ── 行為鐵律（R）──
  R-001: "IF state == DISCUSS AND action == OUTPUT_FILE_CONTENT THEN REQUIRE(propose_before_deliver) AND REQUIRE(E_USER_CONFIRM_DELIVER_received OR E_USER_CONTINUE_DELIVER_received)"
  R-002: "IF state == DISCUSS AND action == OUTPUT_FILE_CONTENT THEN FORBID(file_content) AND REQUIRE(change_list)"
  R-003: "IF target_file CONTAINS multiple_changes THEN REQUIRE(single_integrated_delivery) AND REQUIRE(section_count_match)"
  R-004: "IF project_unconfirmed THEN FORBID(emit_dialog_id)"
  R-005: "IF action == MODIFY_FILE THEN REQUIRE(cite_exact_section AND declare_100pct_preserve)"
  R-006: "IF proposing THEN REQUIRE(declare_file_count) AND IF file_count >= 2 THEN REQUIRE(reason_not_one)"
  R-008: "IF action == AFTER_DELIVERY THEN FORBID(auto_emit_K002)"
  R-009: "IF response == ANY THEN REQUIRE(lang == ZH_TW AND no_simplified_chars)"
  R-010: "IF action == DELIVER_FILE THEN REQUIRE(mode == FULL_FILE) AND REQUIRE(one_file_per_reply) AND REQUIRE(F-001_header_with_mode)"
  R-011:
    trigger: "target_file == MISSING AND target_is_generic == false"
    generic_declaration: "MUST DECLARE domain_classification"
    physical_negation_rule: "IF input_contains(ANY of keyword_list) THEN target_is_generic = false"
    keyword_list:
      extensions: [".js", ".mjs", ".ts", ".yml", ".yaml", ".json", ".html", ".css", ".md", ".py", ".sh", ".env"]
      path_patterns: ["/", "\\", "docs/", "src/", ".github/"]
      variable_patterns: ["camelCase", "snake_case", "SCREAMING_CASE", "const ", "let ", "var "]
      explicit_names: ["entity-registry", "setup-structure", "notify.yml", "meta.json"]
    output_position: FIRST_SENTENCE_OF_BODY
    required_line: "[斷路觸發 | 缺失實體檔] 需核對 {file}，暫停提供結論。"
    forbidden_outputs: [conclusion, assumption, debug_steps, fix_code]
    exemption:
      allowed_if: "generic_topic AND user_asked_back_first == true"
      revoked_if: "input_contains(ANY of keyword_list)"
  R-012: "IF any_time THEN FORBID(declare_conversation_end_unilaterally)"
  R-013: "IF action == AFTER_DELIVERY THEN REQUIRE(options_A_B_C_D_with_plain_explanation) AND PAUSE"
  R-014: "IF response == ANY THEN ENFORCE_HEADER_FORMAT(lines=5, lang=ZH_TW) AND IF prompt_word_given THEN REQUIRE(separate_code_block)"
  R-016: "IF change_type IN [architecture, core_module, fsm, automation_script] THEN REQUIRE(adversarial_review_4_categories)"
  R-017: "IF end_signal AND project.handoff_sop == false THEN REQUIRE(options_A_B_C)"
  R-018: "IF end_signal AND delivery_list_contains_system_or_project THEN REQUIRE(update_each_affected_target)"
  R-019: "IF delivery_contains_structural_change IN [split_file, add_file, delete_file, new_pattern_or_role, fsm_or_layering_change, change_records_dir] THEN REQUIRE(list_structural_changes AND prompt_evolution_record) AND IF change_records_dir THEN REQUIRE(E_USER_ARCH_CHANGE_received)"
  R-020: "IF action == DESTRUCTIVE_OPERATION THEN REQUIRE(E_USER_DESTRUCTIVE_OP_received)"
  R-021: "IF action == GLOBAL_BATCH_MODIFY THEN REQUIRE(E_USER_GLOBAL_BATCH_received)"
  R-022: "IF event == E_USER_FORCE_ABORT THEN EXECUTE(stop_all_output AND transition_to_DISCUSS)"
  R-024: "IF requirement_contains(rewrite OR refactor OR restructure OR merge OR split OR upgrade) THEN REQUIRE(deliver_refactor_map_first AND wait_for_approval) AND FORBID(code_delivery_before_approval)"

  # ── 事前提問（S）──
  S-001: "SHALL declare three columns: file_count, existing_rule_hit, disposition; new_addition_requires_reason"
  S-002: { rule: "SHALL declare central_layer_decision: yes/no, reason if no" }
  S-003: { rule: "SHALL declare default_value_decision: yes/no" }
  S-004: { rule: "SHALL cite original version or section before modifying existing file" }
  S-005: { rule: "SHALL declare checked_R02: yes/no; if no, check first" }
  S-006: { rule: "MUST list keywords, affected files with sync notes, confirmed-unaffected files" }

  # ── 事後檢查（K）──
  K-001: "IF trigger == CHECK OR START_DELIVERY THEN REQUIRE(evidence_6_items: [R-001, R-005, R-009, R-011, F-005, F-008])"
  K-002: "IF trigger == CHECK THEN REQUIRE(search_result: ['✅','已交付','狀態總表']) == 0"
  K-003: "IF trigger == CHECK OR START_DELIVERY THEN REQUIRE(three_checks: state_set_match, term_numbers_continuous, cross_package_refs_valid)"

  # ── 格式規範（F）──
  F-001: "IF output == DELIVER THEN REQUIRE_HEADER(repo, path, type, mode, replace_relation, author, version)"
  F-002: "IF path_mentioned THEN REQUIRE(wrap_in_text_code_block AND relative_path AND full_filename)"
  F-003: "IF output == FILE_CONTENT THEN REQUIRE(wrap_in_backticks_with_lang) AND IF content_contains_code_block THEN REQUIRE(outer_fence == four_backticks)"
  F-005: "IF output == FILE_DELIVERY THEN REQUIRE(EOF_TAG_and_no_duplicate_version_in_content)"
  F-006: "IF has_modifications THEN REQUIRE(status_table_at_bottom)"
  F-007: "IF action == MODIFY_FILE THEN REQUIRE(full_file_delivery) AND FORBID(patch_mode)"
  F-008:
    rule: "IF mode == FULL_FILE THEN ENFORCE_STRUCTURAL_INTEGRITY AND FORBID(forbidden_words) ELSE_IF mode == APPEND_ONLY THEN ENFORCE_RANGE_CONTINUITY"
    forbidden_words: ["略", "保留原樣", "同上", "與前相同", "內容不變", "（省略）", "（程式碼略）", "...", "…", "參考前文", "其餘同前"]
    append_only_scope: [SYSTEM-DECISIONS.md, SYSTEM-REJECTED.md, SYSTEM-DEBT.md, SYSTEM-ARCHIVE.md]
    append_only_checks:
      - "ID 連續性：新增區段 ID 接續既有最大號"
      - "EOF 存在"
      - "不檢查全文章節數與行數對比"

  # ── FSM 密語事件 ──
  E_USER_CONFIRM_DELIVER: "觸發詞 == '方案已定案可交付'"
  E_USER_CONTINUE_DELIVER: "觸發詞 == '[繼續交付]'"
  E_USER_DESTRUCTIVE_OP: "觸發詞 == '[授權執行破壞性操作]'"
  E_USER_GLOBAL_BATCH: "觸發詞 == '[授權全域批次修改]'"
  E_USER_FORCE_ABORT: "觸發詞 == '[強制中止]'"

  # ── R-00 §七 審查機制 ──
  R00-7.2:
    rule: "核檔案內容、檔案內部格式、跨檔同步、是否引混亂"
    exclude: "交付外層 Code block、交付標頭、對話層格式、一鍵貼上完整性"
  R00-7.3: "IF review THEN DEFAULT(level == L1); available: [L1, L2, L3, L4]"
  R00-7.4:
    LV-01: "未特別指示 → L1"
    LV-02: "符合升層條件即升，取最高"
    LV-03: "審判者只能建議升層，須附理由"
    LV-04: "Ken 可任一時點指定層級"
    LV-05: "升層須記錄 CHK-id｜層級：Lx（理由：…）"
    LV-06: "未升層視為 L1"
    LV-07: "審判者不得自行升層或降層"
  R00-7.5:
    upgrade_conditions:
      cross_file_sync: L2
      add_or_delete_section: L2
      fsm_state_role: L3
      rule_conflict_exemption: L3
      ken_requests_repeat: L3
      cross_file_and_core_rule: L4
      ken_explicit: EXPLICIT
  R00-7.6:
    RV-01: "Ken 可要求同一項再給一組前中後"
    RV-02: "第二次三個位置不得與第一次全同"
    RV-03: "全同 → 標記疑似未真讀，改 FAIL 或人工核"
    RV-04: "審判者不得拒絕重複要求"
```

---

## 三、保留散文清單與理由

| 編號 | 規則 | 保留理由 |
|---|---|---|
| R-007 | AI 讀者優先 | 判斷依「是否含結構化元素」「段落有無廢話開場」，屬質性判斷，predicate 化會失真 |
| R-015 | 原生知識與 SOP 衝突 | 含權限階梯、降級、架構溢出三層，DSL 化後難以表達「宣告位置」與「取得許可」的順序關係 |
| S-007 | 防護前提確認 | 「何謂並發」「何謂必然」需人判斷，非機械可判 |
| F-004 | 內層防呆 | 含 md 檔內 YAML 的四反引號例外，DSL 化後條件分支比原文更長 |
| R00-7.1 | 三 AI 模式與 CHK 合成物 | 屬結構陳述，無單一 predicate；角色邊界由 CHK.md 承載 |

**另 2 條說明**：R-011 與 F-008 雖已 DSL 化，但含嵌套條件（R-011 的 keyword_list、F-008 的 APPEND_ONLY），屬「部分 DSL」，仍需散文補充邊界案例。

---

## 四、維護規則

| 時機 | 動作 |
|---|---|
| R-00 新增／修改規則 | 本表同步更新映射 |
| 某條 DSL 實測誤判率高 | 降級為散文＋理由 |
| 某條散文可形式化 | 升級為 DSL |
| R-00 §七 子節變動 | 同步 §1.1 與 §二 `R00-7.x` |
| R-03 詞表變動 | 不重複映射，由 R-03 自身保證 |

---

## 五、與 R-00 的關係

- 本表為 **索引與映射**，不取代 R-00。
- R-00 仍為規則 SSOT；本表僅供 AI 快速掃描與 Phase 1 重寫依據。
- 詞表 SSOT 在 R-03，本表不重複映射詞表。
- 衝突時以 R-00 為準（依 R-03 §二「本表與 R-00 衝突以 R-00 為準」）。

/* ═══ EOF ═══
F: AI-kernel/docs/r-rules/R-05-dsl-map.md
V: 1792900043
W: ai-system-20261024-012#62
═══ */