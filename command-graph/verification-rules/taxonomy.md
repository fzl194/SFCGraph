# 核查规则类型体系 v2

基于 6 个领域（业务感知、IP地址管理、QoS/计费/BWM、路径管理、网络切片、可靠性/HA）的规则挖掘结果。

---

## 1. 规则统计

| 领域 | 显式规则 | 隐式规则 | 总计 |
|------|---------|---------|------|
| R1: 业务感知链 | ~18 | 14类 | 32+ |
| R2: IP地址管理 | ~12 | 12类 | 24+ |
| R3: QoS/计费/BWM | 18 | 19 | 37 |
| R4: 路径管理 | 7 | 7 | 14 |
| R5: 网络切片 | 9 | 6 | 15 |
| R6: 可靠性/HA | 8 | 8 | 16 |
| **合计** | **~72** | **~66** | **~138** |

---

## 2. 算子族定义（v2）

### 族 1: 属性传播一致性（attribute_propagation）

**定义**：沿引用链逐级检查属性值相等。上游对象的某属性值决定下游对象的约束。
**核查逻辑**：`for each ref(A→B): assert A.attr == B.attr`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| AP-01 | VPN 级联：VPNINST→APN→POOL 的 VPN 一致 | R2 |
| AP-02 | SPECTYPE 兼容：USERPROFILE↔RULE↔RULEBINDING 的 SPECTYPE 匹配 | R1 |
| AP-03 | POOLBINDGROUP VPN 一致性 | R2 |
| AP-04 | 切片标识 SST+SD 跨命令一致性 | R5 |
| AP-05 | 容灾组 DRGROUPID/DRGROUPNAME 对端匹配 | R6 |
| AP-06 | DRDCI 对端 IP 与对端节点本端 IP 一致 | R6 |
| AP-07 | DRDCI 心跳参数本端对端一致 | R6 |
| AP-08 | URRGROUP 上下行计费类型一致性 | R3 |

### 族 2: 属性兼容约束（attribute_compatibility）

**定义**：上游对象的某属性取值约束了下游对象的可选参数或可执行操作。
**核查逻辑**：`if A.attr == X: assert B in allowed_values(X)`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| AC-01 | POLICYTYPE 约束 L7 绑定（某些策略类型禁用七层） | R1 |
| AC-02 | POOL TYPE 约束后续使用（EXTERNAL 需 POOLGRPMAP） | R2 |
| APN 高级属性影响下游（APPLAYERVOLUME→业务感知链） | R2 |
| AC-04 | USAGERPTMODE 决定 URR 哪些参数必选 | R3 |
| AC-05 | BWMRULETYPE 约束 SERVICELEVEL 范围 | R3 |
| AC-06 | 容灾模式约束 DRSEPINTERFACE 可用性 | R6 |

### 族 3: 参数互斥（parameter_exclusion）

**定义**：两个参数不能同时取某些值组合。
**核查逻辑**：`assert not (A==X and B==Y)`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| PE-01 | IPLEASE=ENABLE 且 RELEASETIME=0 → 冲突 | R2 |
| PE-02 | PCC 上下行方向不一致 | R1 |
| PE-03 | GLBURRGROUP 的 URR 不能含 EVENT 类型 | R3 |
| PE-04 | QOSCAR 的 CAR 和 Shaping 不能同时使能 | R3 |
| PE-05 | BWMRULE: 同组同 TOS 业务类型不能重复 | R3 |

### 族 4: 查找表覆盖度（lookup_coverage）

**定义**：查找表（映射关系）必须覆盖所有可能的输入组合，否则某些场景查找失败。
**核查逻辑**：`for each input in domain: assert lookup(input) != null`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| LC-01 | POOLGRPMAP (TAC+APN+SMF)→POOLGROUP 覆盖度 | R2 |
| LC-02 | PCCPOLICYGRP 多组合匹配覆盖 | R1 |
| LC-03 | ADC 切换链/环检测 | R1 |
| LC-04 | BWM 用户组多维度绑定(APN/UserProfile/SNSSAI) | R3 |
| LC-05 | 切片接口绑定覆盖（每在用 SNSSAI 至少一个 SNSSAIUPINTF） | R5 |
| LC-06 | ECHOIPLIST 白名单为空 → 所有路径不可达 | R4 |

### 族 5: 引用可达性（reference_reachability）

**定义**：引用链终端必须有有效对象（非空壳、非悬空）。
**核查逻辑**：`for each ref(A→B): assert B exists and B.content != empty`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| RR-01 | 悬空引用（RULE→已删除 FLOWFILTER） | R1 |
| RR-02 | 空容器（FLOWFILTER 无绑定） | R1 |
| RR-03 | IPFarm→IPFARMSERVER 至少一个 | R1 |
| RR-04 | GLBURRGROUP 未配置且无 PCC 规则匹配 → 无法计费 | R3 |
| RR-05 | 热备模式应有 DRDCI 通道 | R6 |
| RR-06 | SNSSAIUPINTF/SNSSAIBWMUSRG 引用的 SST+SD 必须在 SNSSAI 中已定义 | R5 |

### 族 6: 跨网元一致性（cross_ne_consistency）

**定义**：同一逻辑对象在不同网元/平台上需保持一致。
**核查逻辑**：`assert local.config == remote.config`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| CN-01 | VPNINST↔L3VPNINST (UDG↔VNRS) | R2 |
| CN-02 | IPFARMSERVER↔SMF PCSCFIP | R1 |
| CN-03 | DRGROUPINFO 本端↔对端对称 | R6 |
| CN-04 | SMF↔UPF 时间一致性（CUSTATECHK） | R3 |
| CN-05 | CP↔UP 关键配置一致性（CUINCONSPOLICY） | R3 |

### 族 7: 平行维度独立（parallel_dimension）

**定义**：多个维度独立匹配，互不影响。
**核查逻辑**：`for each dimension: validate_independently()`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| PD-01 | 14 种 POLICYTYPE 独立匹配 | R1 |
| PD-02 | 漫游类型分区（HOME/ROAMING/VISITING 独立配置） | R3 |

### 族 8: 生效时机差异（effect_timing_gap）

**定义**：同一条链路上不同对象的变更生效机制不同，可能导致配置不一致。
**核查逻辑**：`for each obj in chain: if recently_modified(obj): check_effect_status(obj)`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| ET-01 | 业务感知链：手动刷新/60s自动/立即 三种生效 | R1 |
| ET-02 | IP地址管理链：POOL 立即 vs POOLGROUP 仅新用户 | R2 |
| ET-03 | QOSGLOBAL: 90 秒延迟 | R3 |
| ET-04 | QOSCAR: 仅新激活用户 | R3 |
| ET-05 | SNSSAIUPINTF: 仅新 PFCP 消息 | R5 |
| ET-06 | UPDEFAULTQUOTA: 仅承载更新或新激活用户 | R3 |

### 族 9: 地址空间约束（address_space）

**定义**：IP 地址/地址段的区间约束。
**核查逻辑**：区间重叠检测 + 掩码一致性检查

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| AS-01 | SECTION 地址重叠检测以 VPN 为作用域 | R2 |
| AS-02 | MASK 影响路由聚合 | R2 |

### 族 10: 双入口/多策略冲突（policy_conflict）

**定义**：多条独立的配置路径可能对同一对象产生冲突的控制策略。
**核查逻辑**：`for each target: collect_all_policies(target); detect_conflict()`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| PC-01 | GLBEXTFILTER + REDIRECT 双重过滤 | R1 |
| PC-02 | BWM 规则 vs QOSPROP 带宽冲突 | R3 |
| PC-03 | SET REFRESHSRV 刷新范围不覆盖所有对象 | R1 |

### 族 11: 分区可见性（partition_visibility）

**定义**：配置按某种维度分区，不同分区的对象可能有引用限制。
**核查逻辑**：`for each cross-partition ref: assert allowed(partition_A, partition_B)`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| PV-01 | CFGDOMAINNAME 跨域引用限制 | R1 |
| PV-02 | 漫游类型分区配置协调 | R3 |
| PV-03 | 切片分区（不同切片绑定不同接口） | R5 |

### 族 12: 定量计算约束（quantitative_constraint）

**定义**：参数之间存在算术关系，需满足不等式或等式。
**核查逻辑**：`assert formula(params) holds`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| QC-01 | BCSRVLEVELPLY: CIRRate 之和 ≤ 10000 | R3 |
| QC-02 | BCSRVLEVELPLY: CIRRate×CIR ≤ PIRRate×PIR | R3 |
| QC-03 | PIR ≥ CIR (BWMCONTROLLER) | R3 |
| QC-04 | 心跳超时计算：HBINTERVAL × HBTIMES | R6 |
| QC-05 | 路径探测超时：T3RESPONSE × N3REQUEST | R4 |
| QC-06 | 告警阈值：RPTTHD > CLRTHD | R3/R4 |

### 族 13: 故障级联（failure_cascade）

**定义**：底层对象的故障会级联影响到上层对象。
**核查逻辑**：`for each dependency_chain: assert no_broken_link()`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| FC-01 | GTP 路径故障 → 用户去激活 | R4 |
| FC-02 | VPN 路由不可达 → 地址分配失败 | R2 |
| FC-03 | DRDCI 心跳失败 → 容灾倒换 | R6 |

### 族 14: 删除顺序保护（deletion_order）

**定义**：存在引用关系的对象必须按特定顺序删除。
**核查逻辑**：`for each delete(A): assert no_ref_to(A) exists`

**实例**：

| 实例ID | 规则 | 领域 |
|--------|------|------|
| DO-01 | 删除 SNSSAI 前需先删除 SNSSAIUPINTF/SNSSAIBWMUSRG | R5 |
| DO-02 | POOL 有 SECTION 时不能改 VPN | R2 |
| DO-03 | 被引用的 PCCPOLICYGRP 不允许删除 | R1 |

---

## 3. 从 R1/R2 到 R3-R6 的新增发现

| 新算子族 | 说明 | 首次出现 |
|---------|------|---------|
| 定量计算约束 (族12) | 参数间算术关系 | R3 (BCSRVLEVELPLY) |
| 故障级联 (族13) | 底层故障传播 | R4 (GTP路径) |
| 删除顺序保护 (族14) | 引用保护顺序 | R5 (SNSSAI) |

R1/R2 中的 12 个算子族 → R3-R6 扩展后变为 14 个。新增 2 个族。

---

## 4. 算子族的实现复杂度评估

| 族 | 输入 | 核查逻辑 | 实现难度 |
|----|------|---------|---------|
| 1 属性传播 | 引用图 + 属性值 | 图遍历 + 属性比较 | 低 |
| 2 属性兼容 | 引用图 + 属性值 + 兼容矩阵 | 条件判断 | 中 |
| 3 参数互斥 | 对象参数对 | 条件判断 | 低 |
| 4 查找覆盖 | 查找表定义 + 输入空间 | 枚举 + 查找测试 | 高 |
| 5 引用可达 | 引用图 | 图遍历 | 低 |
| 6 跨网元 | 本地+远端数据 | 数据比对 | 高（需跨系统数据） |
| 7 平行维度 | 维度定义 + 配置 | 独立验证 | 低 |
| 8 生效时机 | 变更时间 + 生效策略 | 时间比对 | 中 |
| 9 地址空间 | 地址区间列表 | 区间重叠 | 中 |
| 10 策略冲突 | 多策略来源 | 冲突检测 | 中 |
| 11 分区可见 | 分区定义 + 引用 | 跨区检查 | 中 |
| 12 定量计算 | 参数值 + 公式 | 算术验证 | 低 |
| 13 故障级联 | 依赖链 + 状态 | 链路检查 | 高 |
| 14 删除顺序 | 引用图 | 引用计数 | 低 |
