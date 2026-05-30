# Audit Report: UDG MML Command Graph Extraction Pipeline (Steps 1-4)

**Audit Date**: 2026-05-29
**Pipeline Scope**: 4580 files, 4577 command names, 15074 parameters, 2267 config objects

---

## Step 1: Command Inventory -- Quality Score: HIGH

### Data Summary
- **4581 rows** (header + 4580 data rows)
- **4577 unique command names** (3 files are non-command documents)
- **100% file existence** verified on 5 random samples

### Checks Performed

| Check | Result | Detail |
|-------|--------|--------|
| File paths valid | PASS | All 5 sampled files exist at the recorded absolute paths |
| Command name extraction | PASS | Names correctly extracted from filenames in format `Chinese Title (VERB OBJECT)_ID.md` |
| Operation verb parsing | PASS | Standard verbs (ADD/MOD/SET/RMV/LST/DSP/RTR etc.) correctly identified |
| Command object name | PASS | Object names correctly parsed as second token after verb |
| Classification path | PASS | Directory hierarchy correctly mapped to `service_category / service_domain / config_object_area` |
| Special file handling | PASS | 3 non-command files (MML command declaration, centralized config list/concept) properly flagged with empty command names and `dir_depth=0` |
| is_special_file | PASS | All 4580 rows set to `no` (no file is flagged as special; non-command files have empty command names instead) |

### Issues Found

**ISSUE S1-1 [MEDIUM]: 100 commands with empty operation_verb**
- 97 legitimate MML commands use non-standard verb patterns (EXP, EXC, GEN, COL, CHK, UBLK, BLK, TST, RBL, KIK, OPR, ULD, etc.)
- These are parsed with `operation_verb=""` and `command_object_name` set to the full command name (e.g., `EXP LOG` -> object_name=`EXP LOG`)
- **Impact**: Config object grouping still works correctly because the full command_name is used as the grouping key, but downstream verb-based CRUD classification must handle these special cases.
- **Examples**: `EXP LOG`, `EXC DNSCFGTASK`, `GEN DNSTASKID`, `COL APPINFORMATION`, `RBL LDPSESSION`, `KIK TTYUSER`

**ISSUE S1-2 [LOW]: 3 non-command files included in inventory**
- `MML命令申明_79861195.md`, `集中配置命令列表_83554991.md`, `集中配置概念_63936128.md`
- These have no command name, no classification path, and no meaningful metadata
- **Impact**: Minimal -- they are filtered out in subsequent steps. Could be excluded at scan time.

### Recommendations
- Consider expanding the verb extraction regex to cover non-standard MML verbs (EXP, EXC, GEN, COL, CHK, UBLK, BLK, TST, RBL, KIK, OPR, ULD, CLR, LCK, SYN, STP, SWP, DEA, DEL, GET).
- Optionally filter out non-command files at scan time to keep the inventory clean.

---

## Step 2: Command Metadata -- Quality Score: HIGH

### Data Summary
- **4580 rows** matching inventory
- **99.9%** have description
- **86.4%** have parameter table (622 commands have no parameters -- verified as correct)
- **99.9%** have usage examples
- **81.6%** have notes
- **49.1%** have output descriptions

### Verification: Sample Comparison with Original .md Files

**Sample 1: DSP DFSBUCKET** -- PASS
- Original: 5 sections (命令功能, 注意事项, 参数说明, 使用实例, 输出结果说明)
- Parsed: `sections_found` lists 5 sections, `section_count=5`
- Description matches: "该命令用于查询当前环境中桶的信息"
- Notes matches: "无"
- `applicable_nf` empty -- correct (original has no NF specification)

**Sample 2: MOD SRVCHAIN** -- PASS
- Original: 5 sections (命令功能, 注意事项, 操作用户权限, 参数说明, 使用实例)
- Parsed: `section_count=5`, all sections captured
- `applicable_nf: PGW-U,UPF` -- matches original "适用NF：PGW-U、UPF"
- Permissions: `G_1，管理员级别命令组；G_2，操作员级别命令组` -- matches

**Sample 3: EXC DNSCFGTASK** -- PASS
- Original: 5 sections captured correctly
- Description matches: "该命令用于进行部署任务、创建缓存、清除缓存等操作"
- `applicable_nf: CloudEPSN` -- matches original "适用NF：CloudEPSN"

### Issues Found

**ISSUE S2-1 [LOW]: 622 commands lack parameter tables**
- These are genuine "parameterless" commands (e.g., LST queries with no filter parameters)
- Verified `LST SAAITRAINPARA` -- original .md confirms "参数说明：无"
- **Not a defect** -- these commands truly have no input parameters

### Recommendations
- None significant. Section parsing and content extraction are reliable.

---

## Step 3: Parameter Extraction -- Quality Score: MEDIUM

### Data Summary
- **15,074 parameters** extracted
- **required_type distribution**: optional 39.9%, mandatory 34.4%, conditional-mandatory 14.0%, conditional-optional 10.9%
- **value_type distribution**: other 43.4%, string 32.9%, ip_address 11.7%, enum 9.4%, integer_range 1.5%, unknown 0.9%, mac_address 0.2%

### Verification: Sample Comparison with Original .md Files

**Sample 1: MOD SRVCHAIN (3 params)** -- PASS
- Original .md has 3 params: SRVCHAINNAME (mandatory), UPSRVCHAINID (optional), DNSRVCHAINID (optional)
- Parsed: 3 params with correct identifiers, required_type, and value ranges
- SRVCHAINNAME: mandatory, string 1-31 -- matches
- UPSRVCHAINID: optional, 0-16777215 -- matches
- DNSRVCHAINID: optional, 0-16777215 -- matches

**Sample 2: DSP NATSESSION (6 params)** -- PASS
- QUERYTYPE: mandatory, enum (MSISDN/IMSI/IPV4/IPV6) -- matches
- MSISDN: conditional-mandatory when QUERYTYPE=MSISDN -- matches
- IMSI: conditional-mandatory when QUERYTYPE=IMSI -- matches
- VPNNAME: conditional-mandatory when QUERYTYPE=IPV4 or IPV6 -- matches
- IPV4: conditional-mandatory when QUERYTYPE=IPV4 -- matches
- IPV6: conditional-mandatory when QUERYTYPE=IPV6 -- matches
- `condition_deps_raw` correctly captures JSON dependencies

**Sample 3: EXC DNSCFGTASK (3 params)** -- PASS
- TASKACT: mandatory, enum with 7 values (INIT, DEPLOY, PRE_VERIFY, POST_VERIFY, CLEAR, QRYCACHE, QRYDB) -- matches
- TASKID: conditional-mandatory when TASKACT in INIT/DEPLOY/CLEAR -- matches
- SERVERNAME: conditional-mandatory when TASKACT=DEPLOY -- matches

### Issues Found

**ISSUE S3-1 [HIGH]: 133 parameters have `**参数标识**` markdown artifacts instead of real param_identifiers**
- Affects 133 unique commands across the dataset
- The param_identifier field contains markdown bold markers instead of actual parameter names
- These same 133 parameters also have empty `required_type` fields
- Root cause: Some .md files use a non-standard table format where the header row has `**参数标识**` instead of `参数标识`, causing the parser to extract the bolded header text as a parameter
- **Examples**: MOD DBRUMEM, RMV DBRUMEM, ADD DBRUMEM, LST DBRUMEM, SET DBUPGSTAGE, DSP DBUSERINFO
- **Impact**: These 133 parameters are effectively unusable -- they have no real identifier, no required_type, and no meaningful value

**ISSUE S3-2 [MEDIUM]: `value_type` is inconsistent for some patterns**
- 6542 params (43.4%) classified as "other" -- a catch-all category that likely contains extractable type info
- 142 params classified as "unknown" suggesting parsing failures
- Some value ranges like "1~255位字符" get classified as `integer_range` rather than `string`
- **Example**: `SET DNSINFO > CONFIGURATION` has `value_type=integer_range` but the range "1~255位字符" describes a string length, not an integer range

**ISSUE S3-3 [LOW]: RMV SRVCHAINNAME classified as optional**
- `RMV SRVCHAIN` has SRVCHAINNAME as optional, while `ADD SRVCHAIN` and `MOD SRVCHAIN` have it as mandatory
- This is actually **correct per the original docs** -- RMV commands often allow optional parameters for identification, but the design intent (you must specify what to delete) suggests it should arguably be mandatory
- This is a documentation consistency issue in the source, not a parsing error

### Recommendations
- **Priority 1**: Fix the 133 `**参数标识**` artifacts. Add a pre-processing step that strips markdown bold markers from table headers before parsing. Re-extract these commands.
- **Priority 2**: Improve `value_type` classification for the "other" catch-all (6542 params). Consider adding categories like `string_length_range`, `boolean`, `hex`, `ipv4_cidr`, etc.
- **Priority 3**: Review the 142 "unknown" value_type cases for parsing failures.

---

## Step 4: Config Object Discovery -- Quality Score: HIGH

### Data Summary
- **2,267 config objects** discovered
- **100% command coverage**: all 4577 named commands are grouped into config objects
- **392 objects (17.3%)** have full CRUD (ADD + LST/DSP/RTR + MOD + RMV/DEL)
- **1,038 objects (45.8%)** have only 1 command (query-only or single-action objects)
- **98 objects** have non-CRUD verbs in `other_commands` (BLK, CHG, CHK, CLB, CMP, CMT, CNL, etc.)

### Verification: Sample Object Grouping

**Sample 1: SRVCHAIN** -- PASS
- 4 commands: ADD SRVCHAIN, LST SRVCHAIN, MOD SRVCHAIN, RMV SRVCHAIN
- CRUD assignment: create=[ADD], read=[LST], update=[MOD], delete=[RMV]
- `has_full_crud=yes`, `parameter_count=3` (SRVCHAINNAME, UPSRVCHAINID, DNSRVCHAINID)
- Classification: SFIP管理 / 业务链配置
- All correct

**Sample 2: ABNTRAFFICDT** -- PASS
- 4 commands: ADD ABNTRAFFICDT, LST ABNTRAFFICDT, MOD ABNTRAFFICDT, RMV ABNTRAFFICDT
- CRUD assignment correct, `has_full_crud=yes`
- Classification: 用户面服务管理 / 业务防欺诈 / APN下终端异常下行流量检测开关
- Correct

**Sample 3: DFSBUCKET** -- PASS
- 1 command: DSP DFSBUCKET (query only)
- CRUD assignment: read=[DSP], no create/update/delete
- `has_full_crud=no`, correct

### CRUD Verb Distribution (total 4577 commands)

| Category | Count | Percentage |
|----------|-------|------------|
| Read (LST/DSP/RTR) | 2209 | 48.3% |
| Delete (RMV/DEL) | 616 | 13.5% |
| Create (ADD) | 580 | 12.7% |
| Update (SET) | 556 | 12.2% |
| Update (MOD) | 407 | 8.9% |
| Other | 208 | 4.5% |
| Execute (EXC) | 1 | 0.0% |

### Issues Found

**ISSUE S4-1 [MEDIUM]: 90 objects have `**参数标识**` markdown artifacts in `top_parameters`**
- These are the same commands affected by Issue S3-1
- The `top_parameters` field contains `["**参数标识**", "REAL_PARAM", ...]` instead of `["REAL_PARAM", ...]`
- **Impact**: Downstream schema generation and parameter analysis will include invalid entries

**ISSUE S4-2 [LOW]: 30 objects have trailing `/` in `classification_path`**
- Inconsistency: 2237 objects have clean paths, 30 end with ` /`
- **Examples**: CELL, CELLBINDGRP, DFSBUCKET
- **Impact**: Minor -- cosmetic inconsistency that could affect path matching

### Recommendations
- **Priority 1**: After fixing Issue S3-1, regenerate config objects to clean up the 90 affected `top_parameters` fields.
- **Priority 2**: Normalize `classification_path` to strip trailing slashes.

---

## Summary Scorecard

| Step | Quality Score | Critical Issues | High Issues | Medium Issues | Low Issues |
|------|--------------|-----------------|-------------|---------------|------------|
| Step 1: Command Inventory | **HIGH** | 0 | 0 | 1 | 1 |
| Step 2: Command Metadata | **HIGH** | 0 | 0 | 0 | 1 |
| Step 3: Parameter Extraction | **MEDIUM** | 0 | 1 | 1 | 1 |
| Step 4: Config Object Discovery | **HIGH** | 0 | 0 | 1 | 1 |

## Top Priority Actions

1. **Fix 133 markdown-artifact parameters** (Issue S3-1): Strip `**` markers from table headers before parsing. Re-extract affected commands. This is the single most impactful fix.
2. **Improve value_type classification** (Issue S3-2): Reduce the 43.4% "other" catch-all and 142 "unknown" entries by adding more specific type patterns.
3. **Normalize classification_path** (Issue S4-2): Strip trailing slashes from 30 config objects.
4. **Expand verb extraction** (Issue S1-1): Add non-standard MML verbs (EXP, EXC, GEN, COL, CHK, UBLK, etc.) to improve operation_verb coverage for the 100 commands currently parsed without a verb.
