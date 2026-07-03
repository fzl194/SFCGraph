# Compound Review Queue — 计费域

> 攒批人审队列(spec §10)。每条事件含:类型(新建/演进)、爆炸半径(影响哪些 feature)、
> 证据(top-3 Jaccard + 相位)、Agent 推荐动作。人审通过 → active;驳回 → 回 inferred 重做。
> 纯复用 as-is 不入队(spec §10.1)。

---

## 【待审·变更】DP 0-00002 (compound 1-00002 挂) — 补全各 option 的 excludes

**触发特性**:2-00001 GWFD-020301(A 段 pass-2,2026-07-02)
**变更内容**:为 opt-url / opt-ims / opt-any / opt-abnormal 四个 option 补 `excludes` 子句,使
per-variant `active_commands` 精确收敛到 md_required:
- opt-url: + `excludes FILTERIPV6` (URL场景不用 IPv6 三四层 filter)
- opt-ims: + `excludes FILTER` (与 adds FILTERIPV6 互补)
- opt-any: + `excludes L7FILTER, PROTBINDFLOWF` (any 场景无七层)
- opt-abnormal: + `excludes FILTER, FILTERIPV6, L7FILTER, FLOWFILTER, FLTBINDFLOWF,
  PROTBINDFLOWF, RULE, USERPROFILE, RULEBINDING` (异常场景仅 URR/URRGROUP/PCCPOLICYGRP+
  SET URRGRPBINDING.DFTSIGURRGNAME,过滤链与规则绑定全免)

**原版问题**:只声明 adds 不声明 excludes → 结构并集 6 命令恒在,每个变体 md 实际只用子集 →
覆盖校验一律报"多"。

**爆炸半径**:**22 特性**(2-00001/2/3/4/5/6/9/10/11/12/14/15/16/17/18/30/31/32/33/50/89/91)
复用 1-00002 / 引用 0-00002。这些特性的覆盖校验需连锁重跑(SKILL §7.2)。本次演进仅精确化
excludes,不动 command_set / adds / decision_question,语义更准确,不应改变任一特性的有效变体集。

**证据**:
- md:部署UPF_28493406.md 数据规划表 表1(URL) / 表2(IMS) / 表3(any) / 表4(异常)
- 覆盖校验:演进前 5 变体中 4 个失败(多命令),演进后 5 变体全过
- 相位:DP 0-00002 相位仍是"过滤链/业务匹配场景",decision_question 不变

**Agent 推荐**:通过。本变更属"补漏",无新结构、无 decision_question 改动,且 per-variant
md_required 已被覆盖校验硬闸验证。

---

(后续待审事件按特性递增追加)

---

## 【待审·变更】DP 0-00002 (compound 1-00002 挂) — 补 opt-basic-l34 option

**触发特性**:2-00002 GWFD-020300(A 段 pass-2,2026-07-03)
**变更内容**:为 DP 0-00002 新增第 5 个 option `opt-basic-l34`(三四层基础场景):
- adds: ADD FILTER(IPv4 三四层)
- excludes: FILTERIPV6 / L7FILTER / PROTBINDFLOWF

**原因**:2-00001 的 4 option(URL/IMS/any/异常)全部假设 FILTER 必与 L7FILTER 或 FILTERIPV6 配对
(2-00001 md 4 场景列举)。但 2-00002/2-00003/2-00004 等"复用 backbone 仅承担计费方式差量"的特性
md 仅展示 IPv4 三四层 FILTER 基础配法(无 L7/IPv6),原 4 option 无一匹配 → 覆盖校验一律报
"多 L7FILTER/FILTERIPV6/PROTBINDFLOWF"。补 opt-basic-l34 收敛。

**爆炸半径**:**22 特性**(2-00001/2/3/4/5/6/9/10/11/12/14/15/16/17/18/30/31/32/33/50/89/91)
复用 1-00002 / 引用 0-00002。**但本次只新增 option 不改既有 option**,既存特性的变体集不变,
不应改变任一特性的有效变体集。已连锁重跑 2-00001 覆盖校验 ✓ 仍通过(新 option 不影响未选它的变体)。

**证据**:
- md:配置Gy接口在线计费_83167737.md 操作步骤3(仅三四层 FILTER,无 L7/IPv6 场景列举)
- 覆盖校验:演进前 2-00002 2 变体均失败(多 L7FILTER/FILTERIPV6/PROTBINDFLOWF),演进后 2 变体全过
- 相位:DP 0-00002 相位仍是"过滤链/业务匹配场景",decision_question 不变,仅扩 option 集

**Agent 推荐**:通过。本变更属"补 option"覆盖更多 md 形态,无 decision_question 改动,无既有 option
结构变更,且 per-variant md_required 已被覆盖校验硬闸验证。

---

## 【待审·新建】DP 0-00154 (feature 2-00002 挂) — 在线专属SET开关

**触发特性**:2-00002 GWFD-020300(A 段 pass-2,2026-07-03)
**新建内容**:feature 级 boolean DP,owner=UDG@20.15.2@Task@2-00002:
- decision_name: 是否配置在线专属可选命令
- decision_question: 在线计费部署后,是否追加可选的在线专属命令(默认配额/Credit Pooling/URR上报失败动作)?
- opt-off: excludes atom 0-00016/17/18(跳过 3 个在线可选 SET)
- opt-on: adds atom 0-00016/17/18(配 3 个在线可选 SET)

**原因**:md 操作步骤6-8 标注"可选",主示例脚本不含 3 个 SET 命令(opt-off 证实),步骤6-8 文字描述
提供 3 SET 可选项(opt-on 证实)。原版(pass-1, B 段同建)用 condition_ref=DP 0-00004(generalized
owner 4-00001, B 段作用域外),违反 spec §4.3 A 段不依赖作用域外 DP。本次 A 段重建收回特性内,
新建 feature 级 DP 0-00154 表达。与 2-00001 pass-2 防欺诈 DP 0-00003 同型(feature 级 boolean
+ opt-on/opt-off 切 atom 出现)。

**爆炸半径**:1 特性(仅 2-00002 owner)。DP 0-00004(generalized)opt-g-online 仍负责"是否叠加
2-00002 特性"(跨特性层),本 DP 在特性叠加后内部决定是否追加 3 个可选命令,与上层不冲突
(spec §5 同名决策可多层共存不合并)。

**规则交互**:rule 0-00011(UPDEFAULTQUOTA.DFTQTSWITCH 与 UPGLBCHGPARA.CREDITPOOLSW 不能同 ENABLE)
是配置值互斥约束,覆盖校验只校命令集,规则合规由 conditional_rule 在配置生成时强制。本 DP opt-on
adds 3 atom 同时,但实际配置值必须遵守 rule 0-00011(用户在 atom 0-00016 DFTQTSWITCH=DISABLE 或
atom 0-00017 CREDITPOOLSW=DISABLE 二选一,或两者全 DISABLE)。

**证据**:
- md:配置Gy接口在线计费_83167737.md 步骤6(可选 SET UPDEFAULTQUOTA)/步骤7(可选 SET UPGLBCHGPARA)/
  步骤8(可选 SET URRFAILACTION),主示例脚本无 3 SET(opt-off 证实),步骤文字提供可选项(opt-on 证实)
- 覆盖校验:2 变体(opt-off/opt-on)均通过

**Agent 推荐**:通过。新建 DP 表达 md 证实的可选命令开关,与既有 feature 级 boolean DP 同型,
覆盖校验已验证。

---

## 【待审·新建】DP 0-00155 (feature 2-00003 挂) — 离线专属SET开关

**触发特性**:2-00003 GWFD-010171(A 段 pass-2,2026-07-03)
**新建内容**:feature 级 boolean DP,owner=UDG@20.15.2@Task@2-00003:
- decision_name: 是否配置离线专属可选命令
- decision_question: 离线计费部署后,是否追加可选的离线专属命令(URR 上报失败动作 SET URRFAILACTION)?
- opt-off: excludes atom 0-00018(跳过 1 个离线可选 SET)
- opt-on: adds atom 0-00018(配 1 个离线可选 SET)

**原因**:md 操作步骤6 标注"可选",主示例脚本不含 SET URRFAILACTION(opt-off 证实),步骤6 文字描述
提供 SET URRFAILACTION 可选项(URR 上报失败动作,离线新业务场景下生效,opt-on 证实)。原版(pass-1,
B 段同建)用 condition_ref=DP 0-00004(generalized owner 4-00001, B 段作用域外),违反 spec §4.3
A 段不依赖作用域外 DP。本次 A 段重建收回特性内,新建 feature 级 DP 0-00155 表达。

**与 2-00002 DP 0-00154 的对偶关系**:0-00154(在线)opt-on 切 3 个 SET(UPDEFAULTQUOTA/
UPGLBCHGPARA/URRFAILACTION),本 DP opt-on 只切 1 个 SET(URRFAILACTION——md 唯一标注"离线"字样的
可选命令)。差异源于 md:在线计费 md 步骤6-8 列 3 可选 SET,离线计费 md 步骤6 仅列 1 可选 SET。
atom 0-00018(SET URRFAILACTION)由在线/离线两类特性复用,但每特性独立决定是否追加(spec §5
同名决策可多层共存不合并;§4.2 按 md 收口)。

**爆炸半径**:1 特性(仅 2-00003 owner)。DP 0-00004(generalized)opt-g-offline 仍负责"是否叠加
2-00003 特性"(跨特性层),本 DP 在特性叠加后内部决定是否追加该可选命令,与上层不冲突。

**规则交互**:atom 0-00018 自挂的 rule 0-00119(cardinality 最大记录数1 + 高危漏计费风险提示)
与 DP 0-00051(conditional_required: HOLDINGTIME 前提 RETRYFAILACT=BLOCK 或 CONTINUE)是命令级
审查已闭环的约束,覆盖校验只校命令集出现/缺失,参数合规由 atom 层规则强制。

**证据**:
- md:配置Ga接口离线计费_31927856.md 步骤6(可选 SET URRFAILACTION,主示例脚本无该 SET → opt-off
  证实,步骤文字提供可选项 → opt-on 证实)
- 覆盖校验:2 变体(opt-off/opt-on)均通过

**Agent 推荐**:通过。新建 DP 表达 md 证实的可选命令开关,与 2-00002 DP 0-00154 同型对偶,
覆盖校验已验证。

---

## 【待审·新建】DP 0-00156 (feature 2-00004 挂) — 融合可选SET开关

**触发特性**:2-00004 GWFD-010173(A 段 pass-2,2026-07-03)
**新建内容**:feature 级 boolean DP,owner=UDG@20.15.2@Task@2-00004:
- decision_name: 是否配置融合计费可选 URR 上报失败动作
- decision_question: 融合计费部署后,是否追加可选的 SET URRFAILACTION(URR 上报失败动作,业务被阻塞时放通)?
- opt-off: excludes atom 0-00018(跳过 1 个融合可选 SET)
- opt-on: adds atom 0-00018(配 1 个融合可选 SET,RETRYFAILACT=CONTINUE)

**原因**:md 主示例部署脚本(部署UPF_79654301.md §任务示例)仅走 backbone(无 SET 命令) → opt-off
证实;调测 md(91966529.md)步骤 8 说明 文字描述"当业务被阻塞时,如果想要放通业务,请执行 SET
URRFAILACTION 命令,配置 RETRYFAILACT 参数为 CONTINUE" → opt-on 证实。原版(pass-1, B 段同建)无
特性级 DP,可选 atom 挂载缺位。本次 A 段重建新建 feature 级 DP 0-00156 表达。

**与 2-00002 DP 0-00154 / 2-00003 DP 0-00155 的对偶关系**:0-00154(在线)opt-on 切 3 SET
(UPDEFAULTQUOTA/UPGLBCHGPARA/URRFAILACTION),0-00155(离线)opt-on 切 1 SET(URRFAILACTION),
本 DP(融合)opt-on 亦只切 1 SET(URRFAILACTION——md 唯一在调测步骤标注的可选命令)。3 特性复用
atom 0-00018(SET URRFAILACTION),但每特性独立决定是否追加(spec §5 同名决策可多层共存不合并;
§4.2 按 md 收口——每特性按自身 md 支持的 option 子集枚举)。

**爆炸半径**:1 特性(仅 2-00004 owner)。DP 0-00004(generalized)opt-g-converged 仍负责"是否叠加
2-00004 特性"(跨特性层),本 DP 在特性叠加后内部决定是否追加该可选命令,与上层不冲突。

**规则交互**:atom 0-00018 自挂的 rule 0-00119(cardinality 最大记录数1 + 高危漏计费风险提示)
与 DP 0-00051(conditional_required: HOLDINGTIME 前提 RETRYFAILACT=BLOCK 或 CONTINUE)是命令级
审查已闭环的约束,覆盖校验只校命令集出现/缺失,参数合规由 atom 层规则强制。融合 URRGROUP 在线+
离线共存(consistency_rule 0-00001)与 RGAPPLIED=DEFAULT 不能共存(conditional_rule 0-00002)
是 1-00001 挂的命令级约束,本 DP 不涉及。

**证据**:
- md:调测融合计费的费率标识_91966529.md 步骤8(可选 SET URRFAILACTION,主示例部署脚本无该 SET
  → opt-off 证实,步骤文字提供可选项 → opt-on 证实);部署UPF_79654301.md §任务示例(仅 backbone)
- 覆盖校验:5 变体(4 场景 opt-off + 1 场景 opt-on)均通过

**Agent 推荐**:通过。新建 DP 表达 md 证实的可选命令开关,与 2-00002/03 同型对偶,覆盖校验已验证。


---

## 【纯复用·无新事件】2-00005 GWFD-020351 PCC基本功能(A 段 pass-2,2026-07-03)

**触发特性**:2-00005 GWFD-020351(串行第 5 个)
**事件类型**:纯复用 as-is(spec §10.1 自动放行,**不入队**)。本节为透明记录。

**复用结构**:
- 1-00002 过滤链 + DP 0-00002=opt-basic-l34(md any-to-any 三四层,与 2-00002/03/04 同型)
- 1-00003 规则与用户模板绑定(as-is,Jaccard 1.0)
- 直挂 atom:0-00019(LICENSESWITCH)/ 0-00003(PCCPOLICYGRP)/ 0-00015(REFRESHSRV, must_be_last)

**不复用项**:
- 1-00001 计费三件套:PCC 是策略控制特性,md 操作步骤不含 URR/URRGROUP;URRGROUPNAME 仅 PCCPOLICYGRP 参数级可选(rule 0-00014 覆盖)
- 1-00004 收尾:计费专属,本特性直挂 REFRESHSRV

**变体表达**:
- DP 0-00007(动态/本地 PCC,feature 2-00005 owner)纯参数 changes_scope,命令集不变,不进覆盖枚举
- 覆盖校验:1 变体,exit 0(结构 12 / md_required 9 / DP 收敛 3)

**无 compound/DP 新建或演进**:本特性不引入结构性变更,compound-review-queue 不增加待审条目。
覆盖校验已把关,符合 spec §10.1 纯复用自动放行。

---

## 【纯复用·无新事件】2-00009 GWFD-020302 基于业务时长的计费(A 段 pass-2,2026-07-03)

**触发特性**:2-00009 GWFD-020302(串行第 9 个)
**事件类型**:纯复用 as-is(spec §10.1 自动放行,**不入队**)。本节为透明记录。

**复用结构**(4 backbone 全复用,Jaccard=1.0):
- 1-00001 计费三件套(as-is)
- 1-00002 过滤链 + DP 0-00002=opt-basic-l34(IPv4 三四层基础,与 2-00002/03/04/05 同型)
- 1-00003 规则与用户模板绑定(as-is)
- 1-00004 收尾(as-is)
- 直挂 atom:0-00019(SET LICENSESWITCH,license 82209823 前置)

**时长计费差异的表达(不进命令集枚举)**:
- UPF 侧 metering 差异(OFF/ONLMETERINGTYPE=TIME)= atom 0-00001(ADD URR)参数级,由 atom DP 0-00001
  option(opt-offline/opt-online effect_detail 已含 VOLUME/TIME/EVENT/FREE 取值)覆盖。纯参数 impact,
  不改命令集出现/缺失 → 不进 variants 枚举(spec §4.2)。
- 时长计费方式(QCT/连续/CTP/DTP)= PGW-C/SMF 侧 ADD DCCTEMPLATE.QCT / ADD OFCSRVTEMPLATE.TQM
  (在线/离线时长计费方式 md 69148030/69148033 明示),非 UDG UPF MML(mml_commands.jsonl 无此二命令),
  超出 nf=UDG 作用域,不构成本特性 UPF 命令集分叉。
- 在线/离线/融合 三子场景 md 仅散文 + 重定向到 GWFD-020300/010171/010173,无额外 UPF 命令。
- 无 feature 级可选命令(对比 2-00002 三可选 / 2-00003/04 各一可选)→ 无 feature DP。

**变体表达**:
- 1 变体(DP 0-00002=opt-basic-l34 + DP 0-00003=opt-off)
- 覆盖校验:exit 0(结构 16 / md_required 12 / DP 收敛 4)
- 防欺诈分叉(0-00003 on/off)由 2-00001 pass-2 承载,本特性不重复枚举(spec §5 不合并)
- generalized DP 0-00004(B 段作用域外)负责"是否叠加 2-00002/03/04",本特性只承担"时长"差量

**缺口(非 Task 层错误,不影响放行)**:
- 文档侧:部署 md 任务示例全用 VOLUME(与 2-00010/11 字节级同构),按特性语义建 task,命令层无差量
- atom 层:SET SPECTRAFURRGRP(部署 md 步骤10)无 atom,A 段冻结,md_required 不列,与同族一致

**无 compound/DP 新建或演进**:本特性不引入结构性变更,不增加待审条目。覆盖校验已把关,符合
spec §10.1 纯复用自动放行。

---

## 【纯复用·无新事件】2-00010 GWFD-020303 基于业务流量的计费(A 段 pass-2,2026-07-03)

**触发特性**:2-00010 GWFD-020303(串行第 10 个,10 特性收尾)
**事件类型**:纯复用 as-is(spec §10.1 自动放行,**不入队**)。本节为透明记录。

**复用结构**(4 backbone 全复用,Jaccard=1.0):
- 1-00001 计费三件套(as-is)
- 1-00002 过滤链 + DP 0-00002=opt-basic-l34(IPv4 三四层基础,与 2-00009/02/03/04/05 同型)
- 1-00003 规则与用户模板绑定(as-is)
- 1-00004 收尾(as-is)
- 直挂 atom:0-00019(SET LICENSESWITCH,license 82209824 LKV3G5VBCS01 前置)

**流量计费差异的表达(不进命令集枚举)**:
- UPF 侧 metering 差异(OFF/ONLMETERINGTYPE=VOLUME)= atom 0-00001(ADD URR)参数级,由 atom DP 0-00001
  option(opt-offline/opt-online effect_detail 已含 VOLUME/TIME/EVENT/FREE 取值)覆盖。纯参数 impact,
  不改命令集出现/缺失 → 不进 variants 枚举(spec §4.2)。
- **关键:VOLUME 是内容计费默认形态,本特性连参数级差量都没有**(对比 2-00009 时长计费至少在
  metering=TIME 有参数值差量)。命令集与参数值均与 2-00001 内容计费 100% 一致。
- 流量计费的统计由 UNC 话单(datavolumeFBCUplink/Downlink)/ OCS CCA 信元(CC-Total-Octets)/
  CHF 信元(totalVolume/uplinkVolume/downlinkVolume)承载(特性概述 §原理概述),非 UDG UPF MML,
  不构成本特性的 UPF 命令集分叉。
- 无 feature 级可选命令(对比 2-00002 三可选 / 2-00003/04 各一可选)→ 无 feature DP。

**变体表达**:
- 1 变体(DP 0-00002=opt-basic-l34 + DP 0-00003=opt-off)
- 覆盖校验:exit 0(结构 16 / md_required 13 / DP 收敛 3:FILTERIPV6/L7FILTER/PROTBINDFLOWF
  被 opt-basic-l34 excludes + SPECURRGRPLIST 被 opt-off excludes)
- 防欺诈分叉(0-00003 on/off)由 2-00001 pass-2 承载,本特性不重复枚举(spec §5 不合并)
- generalized DP 0-00004(B 段作用域外)负责"是否叠加 2-00002/03/04",本特性只承担"流量"差量
  (实为默认形态),与上层不冲突

**与 2-00009(时长计费)的同构关系**:二者部署 md 任务示例字节级相同(均用 VOLUME,2-00009 notes
明示"与 2-00010 字节级同构"),仅特性标题/预期 metering 语义不同。2-00009 在 metering=TIME 有参数值
差量(TIME≠默认),本特性 VOLUME=默认值无差量。两者 task_intent 各自按特性语义建,命令层无差量证据。

**缺口(非 Task 层错误,不影响放行)**:
- 文档侧:部署 md 任务示例全用 VOLUME(与 2-00009 字节级同构),作为"流量计费"特性示例自洽
  (VOLUME 即本特性语义),无文档缺口
- atom 层:SET SPECTRAFURRGRP(部署 md 步骤10)无 atom,A 段冻结,md_required 不列,与同族一致

**无 compound/DP 新建或演进**:本特性不引入结构性变更,不增加待审条目。覆盖校验已把关,符合
spec §10.1 纯复用自动放行。10 特性 A 段全部完成,计费域攒批人审队列含 5 待审条目(2 变更 + 3 新建 DP),
1 透明记录(2-00005),2 纯复用记录(2-00009/10)。
