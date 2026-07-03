# GWFD-020302 基于业务时长的计费 — pass-2(A 段重建)

> 串行第 9 个特性(A 段 6 步)。依据 `task-build-skill/procedures/compound-extraction.md` +
> `docs/superpowers/specs/2026-07-02-compound-feature-extraction-design.md`。
> **atom 层冻结**:task-0-* + atom 挂 rule/dp 只读,未改。

## 自审发现

### 形态判定:STEP-OK
- backbone 1-00001(计费三件套) / 1-00002(过滤链) / 1-00003(规则与用户模板绑定) / 1-00004(收尾)
  **全复用**,直挂 0-00019(SET LICENSESWITCH) license 前置。
- 无新建 compound、无新建 atom、无新建 feature DP(详见"时长计费差异如何表达")。

### 11 md 全读结论
1. **部署 md(部署UPF_79813617.md)**:操作步骤 1-12 + 数据规划表 4 场景(URL/IMS/any/异常),
   命令集与 2-00001 内容计费 backbone **字节级同构**(脚本每条 URR 行均注"此处以按流量计费为例",
   实际全用 VOLUME)。
2. **特性概述/参考信息**:License 82209823(SET LICENSESWITCH);依赖 GWFD-020301 内容计费 + SA-Basic;
   应用限制"不支持 CTP<—>QCT 计费方式切换"(SMF 侧行为,非 UPF 命令)。
3. **在线/离线/融合 三子场景 md**(69148029/69148032/33943344):**仅 1 段散文 + 重定向到**
   **GWFD-020300/010171/010173**,不携带额外 UPF 命令。
4. **在线/离线时长计费方式 md**(69148030/69148033):描述 QCT/连续 + CTP/DTP 计费方式,来源是
   **PGW-C/SMF 侧 `ADD DCCTEMPLATE.QCT` / `ADD OFCSRVTEMPLATE.TQM`** 参数——非 UDG UPF MML
   (mml_commands.jsonl 无此二命令),超出 nf=UDG 作用域。UDG UPF 仅按 OCS/SMF 下发的配额/信元统计时长。
5. **在线/离线时长计费流程 md**(69148031/69148034):业务流程图(PFCP/Gx/N4 信令),无 UPF MML。

### 复用判定证据(top-3,Jaccard + 相位)
| 候选 | 命中 backbone | Jaccard | 相位 intent | 推荐动作 |
|---|---|---|---|---|
| 三件套(URR/URRGROUP/PCCPOLICYGRP) | 1-00001 | **1.0** | 计费三件套(完全同义) | 复用 as-is |
| 过滤链(FILTER/FILTERIPV6/L7FILTER/FLOWFILTER/FLTBINDFLOWF/PROTBINDFLOWF) | 1-00002 | **1.0** | 过滤链(完全同义) | 复用 as-is |
| 规则与用户模板绑定(RULE/USERPROFILE/RULEBINDING) | 1-00003 | **1.0** | 规则与用户模板绑定(完全同义) | 复用 as-is |
| 收尾(SPECURRGRPLIST/URRGRPBINDING/REFRESHSRV) | 1-00004 | **1.0** | 收尾(完全同义) | 复用 as-is |

双闸全过:Jaccard≥0.75 **且**相位同义 → 复用。无新建 compound。

### 时长计费差异如何表达(三层判定)
- **参数级(atom DP,冻结)**:UPF 侧 metering 差异 = ADD URR 的 `OFFMETERINGTYPE`/`ONLMETERINGTYPE`
  取 TIME(而非 VOLUME)。由 atom 0-00001(ADD URR)挂的 DP 0-00001(option opt-offline/opt-online
  的 effect_detail 已含 "VOLUME/TIME/EVENT/FREE 取值")覆盖。**纯参数 impact(target_type=parameter)**,
  不改命令集出现/缺失 → 不进 variants 枚举(spec §4.2)。
- **feature DP**:无。本特性部署 md 仅走 backbone,无 feature 级可选命令(对比 2-00002 有
  URRFAILACTION/UPDEFAULTQUOTA/UPGLBCHGPARA 三可选,2-00003/04 各一可选 SET URRFAILACTION)。
  时长计费方式(QCT/CTP/DTP)是 SMF 侧行为,不构成本特性的 UPF 命令集分叉。
- **rule**:feature 挂 rule 0-00018(dependency_rule,license + 内容计费前置)已存在并核实正确,
  指向 0-00019 + 2-00001,OFFMETERINGTYPE/ONLMETERINGTYPE=TIME 由 DP 0-00001 option opt-offline/
  opt-online 覆盖。**无需新增 rule**(md 未揭示新约束:License 82209823 已由 0-00018 覆盖;
  CTP<—>QCT 切换限制是 SMF 侧非 UPF 命令约束)。

## 改动记录

| 文件 | 操作 | 说明 |
|---|---|---|
| `tasks/task-2-00009.yaml` | 编辑 | source_evidence_ids 补全 11 md 路径;notes 增 pass-2 分析;task_relations 复用 backbone(as-is,无新增边) |
| `task_rules/rule-0-00018.yaml` | 未改 | 已正确指向 0-00019 + 2-00001 + DP 0-00001 option |
| `decision_points/dp-0-00002.yaml` | 未改(本特性引用) | opt-basic-l34 option(2-00002 pass-2 新增,22 特性连锁)供本特性选 |
| `review/GWFD-020302-variants.yaml` | 新写 | 1 变体(opt-basic-l34 + opt-off) |
| `review/GWFD-020302-pass-2.md` | 新写 | 本文件 |
| `review/compound-review-queue-计费.md` | 追加 | 纯复用·无新事件记录(spec §10.1) |

## 复用判定证据(详见"自审发现"表)
4 候选全 Jaccard=1.0 + 相位完全同义 → 复用 as-is,无新建/演进 compound。

## 缺口
1. **【文档侧·非 Task 层错误】部署 md 任务示例全用 VOLUME,未展示 TIME**:与 2-00010(GWFD-020303
   流量)/2-00011(GWFD-020306 事件)的部署 md **字节级同构**,三者仅特性标题与预期 metering 语义不同。
   pass-1 已记录,pass-2 维持判定:按"特性语义"建 task(OFFMETERINGTYPE=TIME 由 DP 0-00001 option
   覆盖,命令序列可复现),命令层无差量证据。建议向文档 owner 反馈(三特性部署 md 合并或各自补全
   metering 示例)。**影响**:2-00009/10/11 三 feature task_intent 仅靠特性名语义区分。
2. **【atom 层缺口·冻结】SET SPECTRAFURRGRP 无 atom**:部署 md 步骤10"配置全局缺省URR组
   SET SPECTRAFURRGRP"在任务示例脚本(部署UPF_79813617.md L389)有 1 行,但 atom 层未建该 atom
   (mml_commands.jsonl 含该命令但 tasks/task-0-*.yaml 无)。A 段硬边界(atom 层冻结),本特性不新建。
   md_required 不含 SET SPECTRAFURRGRP,与 2-00001 pass-2 / 2-00003 / 2-00004 同族特性处理一致。
   已记录于 CONSOLIDATION-BACKLOG.md(atom 演进债),待 atom 层统一补建。
3. **【演进建议·不执行】ADD URR atom 0-00001 的 metering type 取值枚举**:当前 DP 0-00001 option
   effect_detail 已含 "VOLUME/TIME/EVENT/FREE 取值",本特性(TIME)已被覆盖,**无需演进**。仅记录:若
   未来需把 metering type 作为独立 DP(而非 OFF/ONLMETERINGTYPE 的取值),需 atom 0-00001 增 option。

## 人工校准
- 意见:(待人工填写)
  影响:2-00009 / rule-0-00018 / GWFD-020302-variants.yaml
  反哺Skill条款:(待人工填写)
