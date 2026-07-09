# UPF网元对接三层图谱 · 第1层：业务图谱

> **文件定位**：`three-layer-graph/01-business-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §8 业务图谱
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化 UPF网元对接场景业务层对象（BD/NS/CS/DP/BR/SO）及其关系边
> **与原网元对接旧版的关系**：本文件为基于 `UDG初始配置与调测` 目录原生重构的完整版，不复用旧版产品特性引用式业务层组织。

---

## 0. 适用定义与来源

### 0.1 根定义
- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 网元对接场景知识来源
- `output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/`
- `three-layer-graph/00-overview.md`
- `three-layer-graph/02-feature-graph.md`
- `three-layer-graph/03-task-layer.md`
- `three-layer-graph/04-command-graph.md`

---

## 1. BusinessDomain + NetworkScenario

### 1.1 BusinessDomain

| 字段 | 值 |
|------|---|
| `domain_id` | `BD-ND` |
| `domain_name` | `网元对接` |
| `domain_summary` | 以网元初始配置目录为基础，描述 UDG 作为 UPF/PGW-U/SGW-U 完成开局接入、互联、组网和验证的工程知识域 |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01` |

> **域说明**：本业务域承载“初始开局对接”类知识，当前实例化子场景为 `NS-ND-UPF`，后续可继续挂接 SGW-U、PGW-U 或其他网元对接子场景。

### 1.2 NetworkScenario

| 字段 | 值 |
|------|---|
| `scenario_id` | `NS-ND-UPF` |
| `scenario_name` | `UPF网元对接` |
| `scenario_summary` | 通过目录中的初始配置、组网对接、路由配置、典型实例和整网调测文档，完成 UDG 作为 UPF 用户面网元的端到端上线 |
| `judgment_basis` | 只要目标是基于 `UDG初始配置与调测` 目录完成开局准备、网管纳管、N4与用户面接口、会话接入、路由实施和 FirstCall 验证，即属于本场景 |
| `typical_outcome` | 网元可纳管、N4与用户面接口可用、会话接入可达、路由连通正确、FirstCall 成功 |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-TK-01`, `EV-TK-02`, `EV-TK-03`, `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-TK-07` |

#### 场景边界

**覆盖范围**：
- 产品：UDG
- 网元角色：UPF、PGW-U、SGW-U
- 目录模块：了解组网架构、License申请与加载、基础数据配置、网元和网管对接、组网对接配置、组网路由配置、典型配置实例、整网调测
- 接口：N4、Sa、Sc、Pa、S11-U、SGi/N6、Nupf
- 实施维度：基础就绪、纳管安全、控制面、用户面、会话接入、路由组网、实例调测

**不覆盖范围**：
- 纯业务感知场景下的计费、带宽控制、访问限制策略编排
- 非初始部署阶段的扩容、迁移、升级专项方案
- 未出现在当前目录中的产品外系统详细实现

---

## 2. ConfigurationSolution（5个方案闭包）

> **拆分依据**：完全按目录闭环拆分，不沿用产品原始 feature_code 作为业务层主轴。

### 2.1 CS-ND-01 架构与基础就绪

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-01` |
| `solution_name` | `架构与基础就绪` |
| `solution_summary` | 由“了解组网架构”“License申请与加载”“基础数据配置”“修改MTU值”组成的开局前置闭环 |
| `design_intent` | 先完成角色判定、License、NTP、网元身份、公共参数、MTU 等基础准备，再进入后续对接 |
| `core_mechanism_combo` | `架构认知 → License加载 → NTP/网元信息 → 公共参数 → MTU就绪` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-TK-02`, `EV-BS-01` |

**scopes**: global_bootstrap（开局全局前置）

**participants**:
- UDG（被配置网元，network_function）
- OM Portal（License与网元信息入口，external_system）
- U2020/MAE（License加载路径与纳管前置，external_system）
- OMC/FusionStage（NTP时间源，external_system）

**uses_feature**: ND-FEAT-01, ND-FEAT-02
**uses_semantic_object**: SO-ND-01, SO-ND-03, SO-ND-04, SO-ND-05, SO-ND-07, SO-ND-08
**constrained_by**: BR-ND-01

### 2.2 CS-ND-02 网管与安全接入

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-02` |
| `solution_name` | `网管与安全接入` |
| `solution_summary` | 由“配置网元和网管对接”与安全授权前置共同组成运维入口闭环 |
| `design_intent` | 让网元具备可纳管、可认证、可远程维护的运维接入能力 |
| `core_mechanism_combo` | `北向账号 → SNMPv3 → 适配层 → 创建网元 → 证书开关/二次授权` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-02`, `EV-BS-01` |

**scopes**: management_access（运维纳管边界）

**participants**:
- UDG（被纳管网元，network_function）
- MAE/U2020（网管平台，external_system）
- 北向运维账号（ops_actor）

**uses_feature**: ND-FEAT-03
**uses_semantic_object**: SO-ND-06, SO-ND-09, SO-ND-10, SO-ND-11
**constrained_by**: BR-ND-02

### 2.3 CS-ND-03 控制面与用户面对接

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-03` |
| `solution_name` | `控制面与用户面对接` |
| `solution_summary` | 由“组网对接配置”目录中的 N4、Sa、Sc、Pa、S11-U、SGi/N6、Nupf、会话接入组成业务承载闭环 |
| `design_intent` | 建立 UDG 与控制面、接入侧、中间侧、锚点侧和外部数据网的基本接口与会话能力 |
| `core_mechanism_combo` | `N4入口 → 用户面接口 → 切片/Nupf分支 → APN/地址池/分配规则` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-03`, `EV-BS-01` |

**scopes**: service_access（业务接入与承载边界）

**participants**:
- UDG/UPF（用户面网元，network_function）
- SMF/PGW-C/SGW-C（控制面，对端网元）
- 外部数据网/业务侧（external_side）

**uses_feature**: ND-FEAT-04, ND-FEAT-05, ND-FEAT-06
**uses_semantic_object**: SO-ND-02, SO-ND-12, SO-ND-13, SO-ND-14, SO-ND-15, SO-ND-16, SO-ND-17
**constrained_by**: BR-ND-03, BR-ND-04

### 2.4 CS-ND-04 路由组网实施

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-04` |
| `solution_name` | `路由组网实施` |
| `solution_summary` | 由“组网路由配置”目录所有分支组成，覆盖无NP卡、NP卡、网络加速卡、SDN、自动/手动、IPv4/IPv6/双栈等组网路径 |
| `design_intent` | 将不同组网分支收敛为稳定可执行的路由实施方案 |
| `core_mechanism_combo` | `VPN实例 → 外联口 → OSPF/BGP/静态 → BFD → GRE/IPsec/MPLS → 自动部署或级联口` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-BS-01` |

**scopes**: network_routing（路由组网边界）

**participants**:
- UDG/UPF（承载转发与路由执行，network_function）
- PE/DC-GW/对端路由器（peer_network）
- 自动部署辅助组件（ops_support）

**uses_feature**: ND-FEAT-07
**uses_semantic_object**: SO-ND-18, SO-ND-19, SO-ND-20, SO-ND-21, SO-ND-22, SO-ND-23, SO-ND-24
**constrained_by**: BR-ND-05, BR-ND-06, BR-ND-07

### 2.5 CS-ND-05 实例验证与整网调测

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-05` |
| `solution_name` | `实例验证与整网调测` |
| `solution_summary` | 由“典型配置实例”和“整网调测”构成，负责将前四个方案落到实例模板并完成验收 |
| `design_intent` | 用实例固化典型组合，用 FirstCall 调测验证整体有效性 |
| `core_mechanism_combo` | `实例模板比对 → 路由/会话验证 → NGPING/PING → SESSIONINFO → FirstCall验收` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-07`, `EV-BS-01` |

**scopes**: acceptance_validation（端到端验收边界）

**participants**:
- UDG/UPF（被验收对象，network_function）
- 调测工程师（ops_actor）
- 对端业务系统/测试终端（endpoint）

**uses_feature**: ND-FEAT-08
**uses_semantic_object**: SO-ND-25
**constrained_by**: BR-ND-08, BR-ND-09, BR-ND-10

---

## 3. DecisionPoint（16个）

| `decision_id` | `owner_layer` | `owner_ref_type` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `status` | `source_evidence_ids` |
|---------------|---------------|-------------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------|----------------------|
| `DP-ND-01` | `L1_business` | `Namespace` | `NS-ND-UPF` | UDG部署角色 | 当前 UDG 扮演 UPF、PGW-U、SGW-U 还是融合角色 | `["UPF","PGW-U","SGW-U","融合"]` | 进入架构认知阶段 | 决定接口范围和实例选择 | `active` | `EV-TK-01` |
| `DP-ND-02` | `L1_business` | `Namespace` | `NS-ND-UPF` | 接口抽象策略 | 业务接口采用抽象合一还是按参考点理解 | `["抽象合一","按参考点理解"]` | 进入架构认知阶段 | 影响业务接口命名与职责归属 | `active` | `EV-TK-01` |
| `DP-ND-03` | `L1_business` | `ConfigurationSolution` | `CS-ND-01` | License加载路径 | 通过 OM Portal 还是 U2020/MAE 加载 | `["OM Portal","U2020/MAE"]` | 基础就绪阶段 | 影响操作路径和附带系统 | `active` | `EV-TK-01` |
| `DP-ND-04` | `L1_business` | `ConfigurationSolution` | `CS-ND-02` | 网管接入方式 | 当前纳管链路以哪类管理面为主 | `["MAE/U2020","证书/匿名结合"]` | 纳管规划时 | 影响创建网元参数和证书前置 | `active` | `EV-TK-02` |
| `DP-ND-05` | `L1_business` | `ConfigurationSolution` | `CS-ND-03` | 是否需要Nupf | 当前场景是否需要 Nupf 服务化接口 | `["需要","不需要"]` | 进入接口规划时 | 影响是否进入 HTTPLE/HTTPLEGRP/SBIAPLE 分支 | `active` | `EV-TK-03` |
| `DP-ND-06` | `L1_business` | `ConfigurationSolution` | `CS-ND-03` | 用户面接口组合 | 当前业务面要启用哪些接口 | `["Sa/Sc/Pa","含S11-U","含SGi/N6","含Nupf"]` | 进入接口规划时 | 影响接口 task 组合 | `active` | `EV-TK-03` |
| `DP-ND-07` | `L1_business` | `ConfigurationSolution` | `CS-ND-03` | 地址分配主体 | 地址由 UDG 本地还是外部主体分配 | `["LOCAL","EXTERNAL"]` | 配置会话接入前 | 影响地址池和分配规则 | `active` | `EV-TK-03` |
| `DP-ND-08` | `L1_business` | `ConfigurationSolution` | `CS-ND-04` | 硬件形态 | 当前是无NP卡、NP卡直连PE还是网络加速卡 | `["无NP卡","NP卡直连PE","网络加速卡直连DC-GW"]` | 进入路由组网前 | 决定路由配置分支 | `active` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `DP-ND-09` | `L1_business` | `ConfigurationSolution` | `CS-ND-04` | SDN与否 | 当前组网是否为 SDN | `["非SDN","SDN"]` | 进入路由组网前 | 决定是否使用 DHCP/单臂BFD/BGP over静态 | `active` | `EV-TK-06` |
| `DP-ND-10` | `L1_business` | `ConfigurationSolution` | `CS-ND-04` | 部署方式 | 当前路由部署走自动还是手工 | `["自动部署","手动部署"]` | 进入路由组网前 | 决定 AUTOSCALING 模板或逐条 MML | `active` | `EV-TK-04`, `EV-TK-05` |
| `DP-ND-11` | `L1_business` | `ConfigurationSolution` | `CS-ND-04` | IP版本 | 当前组网是 IPv4、IPv6 还是双栈 | `["IPv4","IPv6","IPv4v6"]` | 进入地址规划时 | 决定命令、地址族和实例模板 | `active` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `DP-ND-12` | `L1_business` | `ConfigurationSolution` | `CS-ND-04` | 路由协议 | 采用哪类主路由方式 | `["OSPF/OSPFv3","静态路由+BFD","BGP over OSPF","BGP over静态","MPLS VPN"]` | 进入协议规划时 | 决定协议任务链 | `active` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `DP-ND-13` | `L1_business` | `ConfigurationSolution` | `CS-ND-04` | 隧道叠加 | 当前是否叠加 IPsec 或 GRE | `["无","IPsec","GRE","MPLS VPN"]` | 路由增强规划时 | 决定是否进入隧道配置任务 | `active` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `DP-ND-14` | `L1_business` | `ConfigurationSolution` | `CS-ND-04` | BFD模式 | 当前 BFD 采用双向还是单臂 | `["双向","单臂Echo"]` | 路由增强规划时 | 决定 BFD 参数值模式 | `active` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `DP-ND-15` | `L1_business` | `ConfigurationSolution` | `CS-ND-05` | 典型实例模板 | 当前最接近哪个目录实例模板 | `["OSPF自动IPv4","OSPFv3自动IPv6","静态手动IPv4","BGP over OSPFv3 IPv6","SDN IPv4","SDN IPv6","SDN 双栈"]` | 调测前 | 决定复用哪条实例链路 | `active` | `EV-TK-07` |
| `DP-ND-16` | `L1_business` | `ConfigurationSolution` | `CS-ND-05` | 调测异常分支 | 当前问题属于哪一类调测异常 | `["路由不通","BGP未建立","OSPF异常","会话未建立","拥塞"]` | 调测异常出现时 | 决定排障路径 | `active` | `EV-TK-07` |

---

## 4. BusinessRule（10条）

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` |
|-----------|-------------|-------------|------------------------|--------------------|--------------|---------------------|----------|----------------------|
| `BR-ND-01` | 先基础后对接 | `design_rule` | `explicit` | `design` | 必须先完成架构与基础就绪，再进入网管、接口和路由实施 | 后续配置链无稳定前提 | `active` | `EV-TK-01`, `EV-TK-02` |
| `BR-ND-02` | 先纳管后调测 | `design_rule` | `explicit` | `ops` | 网元没有完成可纳管闭环前，不进入整网调测阶段 | 调测结果不可复用且排障成本高 | `active` | `EV-TK-02`, `EV-TK-07` |
| `BR-ND-03` | N4是控制面入口 | `selection_rule` | `explicit` | `design` | N4 是控制面对接入口，不能跳过直接做用户面或路由验证 | 接口链路不完整 | `active` | `EV-TK-03` |
| `BR-ND-04` | 会话接入依赖接口完备 | `dependency_rule` | `explicit` | `design` | 会话接入必须建立在业务接口可达基础上 | APN/地址池配置后仍无法生效 | `active` | `EV-TK-03` |
| `BR-ND-05` | 路由实施服从组网分支 | `selection_rule` | `explicit` | `design` | 路由实施路径必须严格服从硬件、SDN、协议和部署方式组合 | 命令链混搭导致不可收敛 | `active` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `BR-ND-06` | 自动部署先关后开 | `runtime_check_rule` | `explicit` | `ops` | 自动部署模板必须遵守先关开关、后配模板、再开开关的闭环 | 模板不生效或状态异常 | `active` | `EV-TK-04` |
| `BR-ND-07` | SDN强依赖静态与DHCP | `restriction_rule` | `explicit` | `design` | SDN 分支不走 OSPF，依赖 DHCP、静态路由和单臂 BFD | 路由规划错误 | `active` | `EV-TK-06` |
| `BR-ND-08` | 实例优先作为实施模板 | `selection_rule` | `explicit` | `design` | 目录中的典型配置实例优先作为工程实施模板，不重新发明路径 | 实施口径不一致 | `active` | `EV-TK-07` |
| `BR-ND-09` | FirstCall是最终验收标志 | `acceptance_rule` | `explicit` | `acceptance` | 只有 FirstCall 和 SESSIONINFO 验证通过，场景才算闭环 | 不能判定上线完成 | `active` | `EV-TK-07` |
| `BR-ND-10` | 调测按异常类型分流 | `diagnosis_rule` | `explicit` | `ops` | 路由、协议、会话、拥塞要进入不同排障分支 | 排障路径混乱 | `active` | `EV-TK-07` |

---

## 5. SemanticObject（25个）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `realized_by` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|--------------|-----------------------|
| `SO-ND-01` | 部署角色 | UDG 作为 UPF/PGW-U/SGW-U 的角色判定 | 部署角色说明 | `EV-TK-01` |
| `SO-ND-02` | 抽象接口映射 | N4if/Saif/Scif/Paif 等目录中的逻辑接口抽象 | 逻辑接口命名与参考点映射 | `EV-TK-01`, `EV-TK-03` |
| `SO-ND-03` | License路径 | OM Portal 与 U2020/MAE 两类加载路径 | License加载流程 | `EV-TK-01` |
| `SO-ND-04` | NTP双路时间源 | OMC 与 FusionStage 的双路时间同步 | `SET NTP` | `EV-TK-02` |
| `SO-ND-05` | 网元身份 | ME 名称、OM IP、物理 IP | `MOD ME`, `SET OMIP` | `EV-TK-02` |
| `SO-ND-06` | 二次授权 | 高危命令授权闭环 | `SET SECAUTH`, `ADD USRSECAUTH` | `EV-TK-02` |
| `SO-ND-07` | 公共参数集 | 公共参数配置中的全局参数集合 | `SET SIGDSCP` 等公共参数命令 | `EV-TK-02` |
| `SO-ND-08` | MTU层级 | Fabric、主接口、子接口的层级约束 | `SET FABRICMTU`, `MOD INTERFACE` | `EV-TK-02` |
| `SO-ND-09` | 北向纳管账号 | 北向登录与纳管入口 | 北向用户与纳管流程 | `EV-TK-02` |
| `SO-ND-10` | SNMPv3账号 | 网管 SNMPv3 的认证与加密密钥 | SNMPv3用户参数 | `EV-TK-02` |
| `SO-ND-11` | 适配层 | 网管适配层软件与接入方式 | 网元创建与适配配置 | `EV-TK-02` |
| `SO-ND-12` | N4接口 | 控制面 PFCP 对接接口 | `ADD VPNINST`, `ADD LOGICINF`, `SET UPINFO` | `EV-TK-03` |
| `SO-ND-13` | 用户面逻辑接口 | Sa/Sc/Pa/S11-U/Nupf/SGi_N6 等接口集合 | `ADD LOGICINF`, `ADD LOGICIP` | `EV-TK-03` |
| `SO-ND-14` | 切片绑定 | N3/Sa 接口的切片绑定能力 | `ADD SNSSAIUPINTF` | `EV-TK-03` |
| `SO-ND-15` | APN/DNN | 会话接入入口对象 | `ADD APN` | `EV-TK-03` |
| `SO-ND-16` | 地址池族 | POOL/SECTION/POOLGROUP/POOLGRPMAP 等地址对象族 | `ADD POOL`, `ADD SECTION`, `ADD POOLGROUP` | `EV-TK-03` |
| `SO-ND-17` | 地址分配规则 | IPALLOCRULE 规则对象 | `SET IPALLOCRULE` | `EV-TK-03` |
| `SO-ND-18` | 外联口 | 路由实施中的外部接口或子接口 | `ADD IPBINDVPN`, 外联口配置命令 | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `SO-ND-19` | VPN实例 | 路由与业务侧 VPN 容器 | `ADD VPNINSTAF`, `ADD L3VPNINST` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `SO-ND-20` | OSPF路由域 | OSPF/OSPFv3 进程与区域对象 | `ADD OSPF*`, `ADD OSPFV3*` | `EV-TK-04`, `EV-TK-05` |
| `SO-ND-21` | BGP路由域 | BGP VRF、地址族、对等体 | `SET BGP`, `ADD BGP*` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `SO-ND-22` | 静态路由域 | 静态路由与下一跳对象 | `ADD SRROUTE*` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `SO-ND-23` | BFD检测域 | 双向或单臂 BFD 的检测对象 | `SET BFD`, `ADD BFDSESSION` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `SO-ND-24` | 隧道叠加域 | IPsec/GRE/MPLS VPN 的叠加能力 | `ADD GRETUNNEL`, `SET MPLSSITE`, `ADD MPLSIF` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `SO-ND-25` | FirstCall验证结果 | 典型实例与整网调测中的最终验收结果 | `DSP SESSIONINFO`, `NGPING` | `EV-TK-07` |

---

## 6. Scope（子对象，5个）

| `scope_name` | `scope_type` | `scope_summary` | 关联方案 |
|--------------|--------------|-----------------|----------|
| 开局全局前置 | `global_bootstrap` | 对全网元初始准备生效 | CS-ND-01 |
| 运维纳管边界 | `management_access` | 对纳管、维护与认证入口生效 | CS-ND-02 |
| 业务接入边界 | `service_access` | 对控制面、用户面、会话接入生效 | CS-ND-03 |
| 路由组网边界 | `network_routing` | 对协议、链路、组网分支生效 | CS-ND-04 |
| 端到端验收边界 | `acceptance_validation` | 对实例映射、调测和验收生效 | CS-ND-05 |

---

## 7. Participant（子对象，10个）

| `participant_name` | `participant_type` | `plane_or_side` | `responsibility_summary` | 关联方案 |
|--------------------|--------------------|-----------------|--------------------------|----------|
| UDG/UPF | `network_function` | `user_plane` | 作为用户面网元承载接口、会话、路由和调测执行 | CS-ND-01~05 |
| SMF/PGW-C/SGW-C | `network_function` | `control_plane` | 作为控制面对端完成 N4/PFCP 对接 | CS-ND-03 |
| OM Portal | `external_system` | `external` | License与网元基础信息入口 | CS-ND-01 |
| U2020/MAE | `external_system` | `external` | License加载路径与网管纳管平台 | CS-ND-01, CS-ND-02 |
| OMC/FusionStage | `external_system` | `external` | 提供 NTP 时间源 | CS-ND-01 |
| PE/DC-GW/对端路由器 | `peer_network` | `network_side` | 承接路由对接和外联互通 | CS-ND-04 |
| 外部数据网 | `peer_network` | `network_side` | 承接 SGi/N6 等业务出口 | CS-ND-03 |
| 自动部署辅助组件 | `ops_support` | `ops_side` | 提供自动部署模板和状态辅助 | CS-ND-04 |
| 调测工程师 | `ops_actor` | `ops_side` | 执行实例核查、调测和验收 | CS-ND-05 |
| 测试终端/对端业务系统 | `endpoint` | `terminal_side` | 发起 FirstCall 与连通性验证 | CS-ND-05 |

---

## 8. 业务图谱关系边

### 8.1 层级包含

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-ND` | `contains` | `NS-ND-UPF` |
| `NS-ND-UPF` | `instantiated_as` | `CS-ND-01` ~ `CS-ND-05` |

### 8.2 方案使用特性（uses_feature）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-ND-01` | `uses_feature` | `ND-FEAT-01`, `ND-FEAT-02` |
| `CS-ND-02` | `uses_feature` | `ND-FEAT-03` |
| `CS-ND-03` | `uses_feature` | `ND-FEAT-04`, `ND-FEAT-05`, `ND-FEAT-06` |
| `CS-ND-04` | `uses_feature` | `ND-FEAT-07` |
| `CS-ND-05` | `uses_feature` | `ND-FEAT-08` |

### 8.3 方案使用任务（uses_task）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-ND-01` | `uses_task` | `T-ND-01`, `T-ND-02`, `T-ND-03` |
| `CS-ND-02` | `uses_task` | `T-ND-04`, `T-ND-05` |
| `CS-ND-03` | `uses_task` | `T-ND-06`, `T-ND-07`, `T-ND-08`, `T-ND-09` |
| `CS-ND-04` | `uses_task` | `T-ND-10`, `T-ND-11`, `T-ND-12`, `T-ND-13` |
| `CS-ND-05` | `uses_task` | `T-ND-14` |

### 8.4 决策点归属（has_decision）

| 起点 | 关系 | 终点 |
|------|------|------|
| `NS-ND-UPF` | `has_decision` | `DP-ND-01`, `DP-ND-02` |
| `CS-ND-01` | `has_decision` | `DP-ND-03` |
| `CS-ND-02` | `has_decision` | `DP-ND-04` |
| `CS-ND-03` | `has_decision` | `DP-ND-05`, `DP-ND-06`, `DP-ND-07` |
| `CS-ND-04` | `has_decision` | `DP-ND-08`, `DP-ND-09`, `DP-ND-10`, `DP-ND-11`, `DP-ND-12`, `DP-ND-13`, `DP-ND-14` |
| `CS-ND-05` | `has_decision` | `DP-ND-15`, `DP-ND-16` |

### 8.5 业务规则约束（constrained_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-ND-01` | `constrained_by` | `BR-ND-01` |
| `CS-ND-02` | `constrained_by` | `BR-ND-02` |
| `CS-ND-03` | `constrained_by` | `BR-ND-03`, `BR-ND-04` |
| `CS-ND-04` | `constrained_by` | `BR-ND-05`, `BR-ND-06`, `BR-ND-07` |
| `CS-ND-05` | `constrained_by` | `BR-ND-08`, `BR-ND-09`, `BR-ND-10` |

### 8.6 语义对象使用（uses_semantic_object）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-ND-01` | `uses_semantic_object` | `SO-ND-01`, `SO-ND-03`, `SO-ND-04`, `SO-ND-05`, `SO-ND-07`, `SO-ND-08` |
| `CS-ND-02` | `uses_semantic_object` | `SO-ND-06`, `SO-ND-09`, `SO-ND-10`, `SO-ND-11` |
| `CS-ND-03` | `uses_semantic_object` | `SO-ND-02`, `SO-ND-12`, `SO-ND-13`, `SO-ND-14`, `SO-ND-15`, `SO-ND-16`, `SO-ND-17` |
| `CS-ND-04` | `uses_semantic_object` | `SO-ND-18`, `SO-ND-19`, `SO-ND-20`, `SO-ND-21`, `SO-ND-22`, `SO-ND-23`, `SO-ND-24` |
| `CS-ND-05` | `uses_semantic_object` | `SO-ND-25` |

### 8.7 决策点影响（selects / sets_value_pattern）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| `DP-ND-01` | `selects` | `ND-FEAT-04` / `ND-FEAT-05` | 角色不同决定接口集合裁剪 |
| `DP-ND-05` | `selects` | `T-ND-08` | 是否进入 Nupf 服务化接口任务 |
| `DP-ND-07` | `sets_value_pattern` | `IPAllocRule.MODE` | `LOCAL` 或 `EXTERNAL` |
| `DP-ND-09` | `selects` | `T-ND-11` / `T-ND-12` | SDN 分支限制协议链和 BFD 模式 |
| `DP-ND-10` | `selects` | `T-ND-13` | 自动或手工部署决定模板链 |
| `DP-ND-12` | `sets_value_pattern` | `RoutingProtocolFamily` | OSPF/OSPFv3/BGP/静态/MPLS VPN |
| `DP-ND-15` | `selects` | `T-ND-14` | 选择实例模板进入调测链 |

---

## 9. 端到端方案链路

### 9.1 CS-ND-01 到 CS-ND-02
```text
架构认知与角色确认
→ License加载
→ NTP/网元信息/公共参数/MTU
→ 二次授权与证书前置
→ 网管纳管
```

### 9.2 CS-ND-03 控制面与用户面对接
```text
N4接口
→ 用户面逻辑接口
→ Nupf/切片可选分支
→ APN/DNN
→ 地址池/地址段/地址分配规则
```

### 9.3 CS-ND-04 到 CS-ND-05
```text
VPN与外联口基础
→ 路由协议
→ BFD/隧道叠加
→ 自动部署或级联口
→ 典型实例映射
→ SESSIONINFO/NGPING/FirstCall验收
```

---

## 10. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| BusinessDomain | 1 | BD-ND |
| NetworkScenario | 1 | NS-ND-UPF |
| ConfigurationSolution | 5 | CS-ND-01~05 |
| DecisionPoint | 16 | DP-ND-01~16 |
| BusinessRule | 10 | BR-ND-01~10 |
| SemanticObject | 25 | SO-ND-01~25 |
| Scope（子对象） | 5 | - |
| Participant（子对象） | 10 | - |
| **业务层对象总计** | **73** | - |

---

> 本文件为 UPF网元对接场景三层图谱第1层。第2层特性图谱、第3层任务原子层、第4层命令图谱、第5层跨层映射、第6层证据索引见同目录其他文件。
