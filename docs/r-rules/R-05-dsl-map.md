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
| R-010 | 鐵律 | DSL | 三軌制交付＋單檔限制，可判 |
| R-011 | 鐵律 | DSL | 斷路器，含輸出位置與豁免剝奪 |
| R-012 | 鐵律 | DSL | 禁主動宣告結束，可判 |
| R-013 | 鐵律 | **（已廢除，由雙階段密語取代，無需交付後確認）** | — |
| R-014 | 鐵律 | DSL | 五行標頭，可掃描；含身份解耦 |
| R-015 | 鐵律 | 保留散文 | 權限階梯＋降級＋溢出三層，DSL 化易失真 |
| R-016 | 鐵律 | DSL | 四大危機分類，可判 |
| R-017 | 鐵律 | DSL | 專案缺 SOP 三選項，可判 |
| R-018 | 鐵律 | DSL | affected 多目標更新，可判 |
| R-019 | 鐵律 | DSL（checklist） | 觸發條件可列舉清單；獨立提問優先於清單 |
| R-022 | 鐵律 | DSL | 強制中止觸發，可判 |
| R-024 | 鐵律 | DSL（checklist） | 重構地圖要素可列舉；「架構升級」保留語意判斷 |
| R-025 | 鐵律 | DSL（checklist） | 防硬編碼，檢查邏輯標識符與映射表 |
| R-026 | 鐵律 | DSL | 會話鎖與隔離區；區分規則類與狀態包 |
| R-027 | 鐵律 | DSL（checklist） | 檢查點可列舉；同步對照表可掃描 |
| S-001 | 提問 | DSL（checklist） | 三欄可掃描 |
| S-002 | 提問 | DSL（checklist） | 集中層判定 |
| S-003 | 提問 | DSL（checklist） | 預設值判定 |
| S-004 | 提問 | DSL（checklist） | 版本引用 |
| S-005 | 提問 | DSL（checklist） | R-02 查閱 |
| S-006 | 提問 | DSL（checklist） | 關聯影響三項 |
| S-007 | 提問 | 保留散文 | 三事實需人判斷「何謂並發」 |
| K-001 | 檢查 | DSL | 七項事實證據，可列舉 |
| K-002 | 檢查 | DSL | 檔內搜尋，可掃描（含進度類紀錄檔豁免） |
| K-003 | 檢查 | DSL | 三層分工（CI／AI／人工），可列舉 |
| F-001 | 格式 | DSL | 七行標頭，可掃描 |
| F-002 | 格式 | DSL | 路徑 Code Block，可掃描 |
| F-003 | 格式 | DSL | 波浪號包裹；含代碼塊時外層禁四反引號 |
| F-004 | 格式 | 保留散文 | 含例外條款，DSL 化反而更複雜 |
| F-005 | 格式 | DSL | EOF 三行，含 V 為 10 位數、語言例外豁免、源檔邊界防呆 |
| F-006 | 格式 | DSL | 狀態總表位置，可判 |
| F-007 | 格式 | DSL | Patch 廢除，三軌制交付、APPEND 標記、PARTIAL_REPLACE 無條件 EOF |
| F-008 | 格式 | DSL | 章節數＋行數＋嚴格無省略＋lazyPatterns＋allow-delete，可判；含 APPEND_ONLY |
| I-11 | 不變式 | DSL | 會話鎖隔離範圍（規則類 vs SP-Sys） |
| I-12 | 不變式 | DSL | 事件子集關係 |

**統計**：DSL 化 44 條；保留散文 3 條（R-007、R-015、S-007）。

### 1.1 R-00 其他區塊映射

| 編號 | 類別 | 映射方式 | 理由 |
|---|---|---|---|
| R00-0.2 | 規則 | DSL | 禁用詞與可用詞清單，可掃描 |
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

**詞表說明**：詞 65、78、79、80、81、85、86、94、95、96、97 新增，SSOT 在 `R-03-terms.md`，本表不重複映射。密語 SSOT 在 `A-00 §2.3`，本表僅引用完整寫法。

---

## 二、DSL 映射內容

### 2.0 全域執行限制（Meta Scope）

```yaml
_meta:
  scope: "INTERNAL_COT_ONLY"
  description: "本區塊之偽代碼僅供 LLM 內部思維鏈（CoT）與條件判斷使用。嚴禁將 IF-THEN 語法、箭頭 `->` 或 `STOP_INFERENCE` 等標記輸出於對話正文中。"
  default_action: "ELSE -> PASS_THROUGH"
  linkage: "每條 DSL 觸發時，AI MUST 於內部連動 R-00 對應之 Counter-example 進行自檢。"
```

### 2.1 映射內容

```yaml
rules_dsl:
  # ── 行為鐵律（R）──
  R-001:
    ref: "R-00 R-001"
    rule: >-
      IF state == DISCUSS AND action == OUTPUT_FILE_CONTENT
      THEN OUTPUT(propose_before_deliver) AND REQUIRE(E_USER_CONFIRM_DELIVER) AND REQUIRE(E_CONFIRM_LIST)
      ELSE -> PASS_THROUGH
  R-002:
    ref: "R-00 R-002"
    rule: "IF state == DISCUSS AND action == OUTPUT_FILE_CONTENT THEN FORBID(file_content) AND REQUIRE(change_list) ELSE -> PASS_THROUGH"
  R-003:
    ref: "R-00 R-003"
    rule: "IF target_file CONTAINS multiple_changes THEN REQUIRE(single_integrated_delivery) AND REQUIRE(section_count_match) ELSE -> PASS_THROUGH"
  R-004:
    ref: "R-00 R-004"
    rule: "IF project_unconfirmed THEN FORBID(emit_dialog_id) ELSE -> PASS_THROUGH"
  R-005:
    ref: "R-00 R-005"
    rule: "IF action == MODIFY_FILE THEN REQUIRE(cite_exact_section) AND REQUIRE(declare_100pct_preserve) ELSE -> PASS_THROUGH"
  R-006:
    ref: "R-00 R-006"
    rule: "IF proposing THEN REQUIRE(declare_file_count) AND IF file_count >= 2 THEN REQUIRE(reason_not_one) ELSE -> PASS_THROUGH"
  R-008:
    ref: "R-00 R-008"
    rule: "IF action == AFTER_DELIVERY THEN FORBID(auto_emit_K002) ELSE -> PASS_THROUGH"
  R-009:
    ref: "R-00 R-009"
    rule: "IF response == ANY THEN REQUIRE(lang == ZH_TW) AND REQUIRE(no_simplified_chars) ELSE -> PASS_THROUGH"
  R-010:
    ref: "R-00 R-010"
    rule: "IF action == DELIVER_FILE THEN REQUIRE(mode IN [FULL_FILE, APPEND_ONLY, PARTIAL_REPLACE]) AND REQUIRE(one_file_per_reply) AND REQUIRE(F-001_header_with_mode) ELSE -> PASS_THROUGH"
  R-011:
    ref: "R-00 R-011"
    rule: >-
      IF target_file == MISSING AND target_is_generic == false
      THEN OUTPUT('[斷路觸發 | 缺失實體檔] 需核對 {file}，暫停提供結論。') -> STOP_INFERENCE
      ELSE -> PASS_THROUGH
  R-012:
    ref: "R-00 R-012"
    rule: "IF any_time THEN FORBID(declare_conversation_end_unilaterally) ELSE -> PASS_THROUGH"
  R-014:
    ref: "R-00 R-014"
    rule: "IF response == ANY THEN ENFORCE_HEADER_FORMAT(lines=5, lang=ZH_TW) AND REQUIRE(role_state_decoupled) AND REQUIRE(questions_at_bottom) ELSE -> PASS_THROUGH"
  R-016:
    ref: "R-00 R-016"
    rule: "IF change_type IN [architecture, core_module, fsm, automation_script] THEN REQUIRE(adversarial_review_4_categories) ELSE -> PASS_THROUGH"
  R-017:
    ref: "R-00 R-017"
    rule: "IF end_signal AND project.handoff_sop == false THEN REQUIRE(options_A_B_C) ELSE -> PASS_THROUGH"
  R-018:
    ref: "R-00 R-018"
    rule: "IF end_signal AND delivery_list_contains_system_or_project THEN REQUIRE(update_each_affected_target) ELSE -> PASS_THROUGH"
  R-019:
    ref: "R-00 R-019"
    rule: "IF delivery_contains_structural_change IN [split_file, add_file, delete_file, new_pattern_or_role, fsm_or_layering_change, change_records_dir] THEN REQUIRE(independent_prompt_before_list) AND REQUIRE(prompt_evolution_record) ELSE -> PASS_THROUGH"
  R-022:
    ref: "R-00 R-022"
    rule: "IF event == E_USER_FORCE_ABORT THEN EXECUTE(stop_all_output) -> TRANSITION_TO(DISCUSS) ELSE -> PASS_THROUGH"
  R-024:
    ref: "R-00 R-024"
    rule: "IF requirement_contains(rewrite OR refactor OR restructure OR merge OR split OR upgrade) THEN REQUIRE(deliver_refactor_map_first) -> REQUIRE(wait_for_approval) -> STOP_INFERENCE ELSE -> PASS_THROUGH"
  R-025:
    ref: "R-00 R-025"
    rule: "IF document_or_code_contains(hardcoded_filename OR hardcoded_path) THEN FORBID(commit) AND REQUIRE(use_logical_identifier) ELSE -> PASS_THROUGH"
  R-026:
    ref: "R-00 R-026"
    rule: >-
      IF file_type IN [IP, AP, RP, UP] AND file_V != session_lock_V
      THEN FORBID(load_content) -> EXECUTE(move_to_quarantine) -> OUTPUT_WARNING
      ELSE_IF file_type == SP_SYS
      THEN APPLY(I-04_version_max_load)
      ELSE -> PASS_THROUGH
  R-027:
    ref: "R-00 R-027"
    rule: "IF modify_rule_in_R00 AND rule_is_checkable THEN REQUIRE(sync_all_checkpoints_in_same_delivery) AND REQUIRE(sync_table_in_summary) ELSE -> PASS_THROUGH"

  # ── 事前提問（S）──
  S-001: { ref: "R-00 S-001", rule: "IF proposing THEN REQUIRE(declare_three_columns) ELSE -> PASS_THROUGH" }
  S-002: { ref: "R-00 S-002", rule: "IF modifying_multi_callers THEN REQUIRE(declare_central_layer_decision) ELSE -> PASS_THROUGH" }
  S-003: { ref: "R-00 S-003", rule: "IF involving_params THEN REQUIRE(declare_default_value_decision) ELSE -> PASS_THROUGH" }
  S-004: { ref: "R-00 S-004", rule: "IF modifying_existing_file THEN REQUIRE(cite_original_version_or_section) ELSE -> PASS_THROUGH" }
  S-005: { ref: "R-00 S-005", rule: "IF architecture_design THEN REQUIRE(declare_checked_R02) ELSE -> PASS_THROUGH" }
  S-006: { ref: "R-00 S-006", rule: "IF cross_file_modification THEN REQUIRE(list_keywords) AND REQUIRE(affected_files) AND REQUIRE(confirmed_unaffected) ELSE -> PASS_THROUGH" }

  # ── 事後檢查（K）──
  K-001: { ref: "R-00 K-001", rule: "IF trigger == CHECK THEN REQUIRE(evidence_7_items) ELSE -> PASS_THROUGH" }
  K-002: { ref: "R-00 K-002", rule: "IF trigger == CHECK THEN REQUIRE(search_result_zero) ELSE -> PASS_THROUGH" }
  K-003: { ref: "R-00 K-003", rule: "IF trigger == CHECK THEN REQUIRE(three_layer_division_output) ELSE -> PASS_THROUGH" }

  # ── 不變式（I）──
  I-11: { ref: "A-00 I-11", rule: "IF session_lock_established AND receive_rule_file_diff_V THEN REQUIRE(quarantine) ELSE_IF receive_SP_SYS THEN APPLY(I-04) ELSE -> PASS_THROUGH" }
  I-12: { ref: "A-00 I-12", rule: "IF state == ANY THEN REQUIRE(SUBSET(§2.5_events, §2.3_events) AND SUBSET(§2.4_events, §2.3_events)) ELSE -> PASS_THROUGH" }

  # ── 格式規範（F）──
  F-001: { ref: "R-00 F-001", rule: "IF output == DELIVER THEN REQUIRE_HEADER(repo, path, type, mode, replace_relation, author, version) ELSE -> PASS_THROUGH" }
  F-002: { ref: "R-00 F-002", rule: "IF path_mentioned THEN REQUIRE(wrap_in_text_code_block) ELSE -> PASS_THROUGH" }
  F-003: { ref: "R-00 F-003", rule: "IF output == FILE_CONTENT THEN REQUIRE(wrap_in_tildes_with_lang) ELSE -> PASS_THROUGH" }
  F-005: { ref: "R-00 F-005", rule: "IF file_ext == '.md' THEN REQUIRE(EOF_tag) ELSE_IF file_ext == '.json' THEN REQUIRE(_EOF_key) ELSE -> PASS_THROUGH" }
  F-006: { ref: "R-00 F-006", rule: "IF has_modifications THEN REQUIRE(status_table_at_bottom) ELSE -> PASS_THROUGH" }
  F-007: { ref: "R-00 F-007", rule: "IF action == MODIFY_FILE THEN REQUIRE(mode IN [FULL_FILE, APPEND_ONLY, PARTIAL_REPLACE]) AND FORBID(patch_mode) ELSE -> PASS_THROUGH" }
  F-008: { ref: "R-00 F-008", rule: "IF mode == FULL_FILE THEN ENFORCE_STRUCTURAL_INTEGRITY AND FORBID(forbidden_words) ELSE -> PASS_THROUGH" }

  # ── FSM 密語事件（SSOT: A-00 §2.3）──
  E_USER_CONFIRM_DELIVER: "IF trigger_word == '方案已落實，提供交付相關的清單，待確認' THEN TRANSITION_TO(DELIVER)"
  E_CONFIRM_LIST: "IF trigger_word == '交付清單已確認，提供標題與交付模式，並輸出檔案內容' THEN TRANSITION_TO(EXECUTE)"
  E_USER_CONTINUE_DELIVER: "IF trigger_word == '[繼續交付]' THEN TRANSITION_TO(EXECUTE)"
  E_USER_FORCE_ABORT: "IF trigger_word == '[強制中止]' THEN TRANSITION_TO(DISCUSS)"
  E_TRANSFER_MODE: "IF trigger_word == '[轉交模式]' THEN TRANSITION_TO(TRANSFER)"

  # ── R-00 §七 審查機制 ──
  R00-7.2: "IF review THEN EXECUTE(file_content_check) ELSE -> PASS_THROUGH"
  R00-7.3: "IF review THEN DEFAULT(level == L1) ELSE -> PASS_THROUGH"
  R00-7.4: "IF level_upgraded THEN REQUIRE(record_CHK_id_and_reason) ELSE -> PASS_THROUGH"
  R00-7.5: "IF upgrade_condition_met THEN INCREASE_LEVEL ELSE -> PASS_THROUGH"
  R00-7.6: "IF repeat_check THEN REQUIRE(different_position) ELSE -> PASS_THROUGH"
```

---

## 三、保留散文清單與理由

| 編號 | 規則 | 保留理由 |
|---|---|---|
| R-007 | AI 讀者優先 | 判斷依「是否含結構化元素」「段落有無廢話開場」，屬質性判斷，predicate 化會失真 |
| R-015 | 原生知識與 SOP 衝突 | 含權限階梯、降級、架構溢出三層，DSL 化後難以表達「宣告位置」與「取得許可」的順序關係 |
| S-007 | 防護前提確認 | 「何謂並發」「何謂必然」需人判斷，非機械可判 |
| R00-7.1 | 三 AI 模式與 CHK 合成物 | 屬結構陳述，無單一 predicate；角色邊界由 CHK.md 承載 |

**另 2 條說明**：R-011 與 F-008 雖已 DSL 化，但含嵌套條件（R-011 的 keyword_list、F-008 的 APPEND_ONLY），屬「部分 DSL」，仍需散文補充邊界案例。

---

## 四、維護規則

| 時機 | 動作 |
|---|---|
| R-00 新增／修改規則 | 本表同步更新映射 |
| R-00 新增可檢查條文 | 本表同步新增對應 DSL，並依 R-027 精神同步檢查點 |
| 某條 DSL 實測誤判率高 | 降級為散文＋理由 |
| 某條散文可形式化 | 升級為 DSL |
| R-00 §七 子節變動 | 同步 §1.1 與 §二 `R00-7.x` |
| R-03 詞表變動 | 不重複映射，由 R-03 自身保證 |
| A-00 §2.3 密語變動 | 同步 §二 FSM 密語事件區塊 |
| A-00 §2.6 不變式變動 | 同步 §二 I 區塊 |

---

## 五、與 R-00 的關係

- 本表為 **索引與映射**，不取代 R-00。
- R-00 仍為規則 SSOT；本表僅供 AI 快速掃描與 Phase 1 重寫依據。
- 詞表 SSOT 在 R-03，本表不重複映射詞表。
- 密語 SSOT 在 A-00 §2.3，本表引用完整寫法，不另行定義。
- 衝突時以 R-00 為準（依 R-03 §二「本表與 R-00 衝突以 R-00 為準」）。

/* ═══ EOF ═══
F: AI-kernel/docs/r-rules/R-05-dsl-map.md
V: 1792914700
W: ai-system-005
═══ */