# R3: QoS/计费/BWM 控制链 — 规则挖掘

## 0. 探索范围

| 领域 | 命令数 | 核心ADD/SET命令 |
|------|--------|----------------|
| 计费控制（URR） | ~30 | ADD URR, ADD URRGROUP, SET GLBURRGROUP, SET UPDEFAULTQUOTA, SET UPURRCTRL, ADD SPECURRGRPLIST, SET CUINCONSPOLICY, SET CUSTATECHK |
| 带宽控制（BWM） | ~45 | ADD BWMRULE, ADD BWMSERVICE, ADD BWMCONTROLLER, ADD BWMUSERGROUP, ADD BCSRVLEVELPLY, ADD BWMRULEGLOBAL, ADD APNBINDBWMUSRG, ADD UPBINDBWMUSRG, ADD SNSSAIBWMUSRG |
| 用户QoS | ~30 | ADD QOSPROP, SET QOSCAR, SET QOSGLOBAL |

---

## 1. 命令链路图

### 1.1 计费链

```
ADD URR (使用率上报规则，基础原子)
  ├→ ADD URRGROUP (6个URR槽位：上行3个+下行3个)
  │    ├→ SET GLBURRGROUP (全局默认计费属性，引用URR)
  │    ├→ ADD SPECURRGRPLIST (特殊URR组，用于防欺诈等场景)
  │    └→ ADD PCCPOLICYGRP.URRGROUPNAME (已探索，每条PCC策略引用一个URR组)
  └→ SET UPDEFAULTQUOTA (按漫游类型配额开关: HOME/ROAMING/VISITING)
```

### 1.2 BWM 链

```
ADD BWMCONTROLLER (带宽控制器: CAR/SHAPING)
ADD BWMSERVICE (业务定义: TOS/NONTOS)
ADD CATEGORYPROP (分类属性，被BWMSERVICE引用)
ADD BWMUSERGROUP (用户组: DEFAULT_GROUP/SPECIFIC_GROUP)
  ├→ ADD APNBINDBWMUSRG (APN→用户组绑定)
  ├→ ADD UPBINDBWMUSRG (UserProfile→用户组绑定)
  └→ ADD SNSSAIBWMUSRG (切片→用户组绑定)
ADD BWMRULE (用户组规则: GROUP_DEFAULT/SUBSCRIBER_DEFAULT/GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC)
ADD BWMRULEGLOBAL (全局规则，仅TOS类型)
ADD BCSRVLEVELPLY (业务级别策略：按ServiceLevel分配带宽比例)
```

### 1.3 QoS 链

```
ADD QOSPROP (QoS属性: GBR/MBR/解耦开关/关键流检测)
  └→ ADD PCCPOLICYGRP.QOSPROPNAME (PCC策略引用QoS属性)
SET QOSGLOBAL (全局QoS配置: 90秒延迟生效)
SET QOSCAR (按漫游类型的CAR开关: HOME/ROAMING/VISITING)
```

---

## 2. 显式规则

| # | 规则 | 来源 | 严重度 |
|---|------|------|--------|
| R3-E01 | URR.USAGERPTMODE=ONLINE 时 DFTQUOTAVOLUME 和 DFTQUOTATIME 必选 | ADD URR | 错误 |
| R3-E02 | GLBURRGROUP 绑定的 URR 的 METERINGTYPE 不能包含 EVENT | SET GLBURRGROUP | 错误 |
| R3-E03 | URRGROUP 至少要有一个 UPURRNAME 或 DOWNURRNAME | ADD URRGROUP | 错误 |
| R3-E04 | BWMCONTROLLER: PIR ≥ CIR（两者都配时） | ADD BWMCONTROLLER | 错误 |
| R3-E05 | BCSRVLEVELPLY: 所有 CIRRate 之和 ≤ 100%（万分比） | ADD BCSRVLEVELPLY | 错误 |
| R3-E06 | BCSRVLEVELPLY: CIRRate×CIR ≤ PIRRate×PIR | ADD BCSRVLEVELPLY | 错误 |
| R3-E07 | BWMRULE + BWMRULEGLOBAL 共享 5000 条配额 | ADD BWMRULE/BWMRULEGLOBAL | 警告 |
| R3-E08 | BWMRULE: 同一用户组下 TOS 业务类型不能相同 | ADD BWMRULE | 错误 |
| R3-E09 | BWMRULE: 规则优先级不能重复 | ADD BWMRULE | 错误 |
| R3-E10 | BWMRULEGLOBAL: 只支持 TOS 类业务，不支持 SHAPING 控制器 | ADD BWMRULEGLOBAL | 错误 |
| R3-E11 | 用户组最多绑定 16 个 APN/UserProfile/切片 | ADD APNBINDBWMUSRG | 错误 |
| R3-E12 | 不能绑定到默认或全局用户组 | ADD APNBINDBWMUSRG | 错误 |
| R3-E13 | SET CUINCONSPOLICY: CHGATTRRPTTHD 必须 > CHGATTRCLRTHD | SET CUINCONSPOLICY | 错误 |
| R3-E14 | SET CUSTATECHK: UTCALMCLRTHD 必须 < UTCALMRPTTHD | SET CUSTATECHK | 错误 |
| R3-E15 | SET CUSTATECHK: UTCDETECTMS > 5000 可能导致计费时间戳不准 | SET CUSTATECHK | 警告 |
| R3-E16 | QOSCAR: CAR 和 Shaping 不能同时使能 | SET QOSCAR | 错误 |
| R3-E17 | BWMRULE: 时间段不能重叠且 ≥ 30分钟 | ADD BWMRULE | 错误 |
| R3-E18 | 全局用户组只支持 TOS 类型业务 | ADD BWMUSERGROUP | 错误 |

---

## 3. 隐式规则

### 3.1 计费层级与配额传递（hierarchical_quota_fallback）

**发现**：计费配置存在三层层级关系：全局默认(GLBURRGROUP) → PCC策略级(PCCPOLICYGRP.URRGROUPNAME) → 特殊场景(SPECURRGRPLIST)。当用户没有匹配到任何 PCC 规则时，使用 GLBURRGROUP 作为兜底。

**证据**：
- SET GLBURRGROUP：全局默认计费属性，只有 1 条记录
- ADD PCCPOLICYGRP：每条 PCC 策略可以指定自己的 URRGROUPNAME
- SET UPDEFAULTQUOTA：按漫游类型控制是否给默认配额

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R3-I01 | 如果 GLBURRGROUP 未配置且用户未匹配任何 PCC 规则 → 无法计费 | GLBURRGROUP + PCCPOLICYGRP | 引用可达性 |
| R3-I02 | SET UPDEFAULTQUOTA.ENABLE 但 GLBURRGROUP 的配额 URR 未配 DFTQUOTAVOLUME → 默认配额无效 | UPDEFAULTQUOTA + URR | 参数互斥 |
| R3-I03 | URRGROUP 中上行和下行的在线/离线计费类型应保持一致（否则部分流量无法计费） | URRGROUP | 一致性 |

### 3.2 BWM 用户组多维度绑定（multi_dimension_binding）

**发现**：BWMUSERGROUP 通过 APN/UserProfile/SNSSAI 三个维度绑定用户，与 POOLGRPMAP 的 (TAC+APN+SMF) 三维度查找是同一模式。

**证据**：
- ADD APNBINDBWMUSRG：APN→用户组
- ADD UPBINDBWMUSRG：UserProfile→用户组
- ADD SNSSAIBWMUSRG：切片→用户组
- 注意事项："多个 BwmUserGroup 时，优先级最高的生效"

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R3-I04 | 用户同时匹配多个 BWMUSERGROUP（通过不同维度）时，仅 USERGROUPPRI 最高者生效 | BWMUSERGROUP + 3种绑定 | 查找表覆盖度 |
| R3-I05 | 用户不匹配任何 BWMUSERGROUP → 使用 DEFAULT_GROUP | BWMUSERGROUP | 查找表覆盖度 |
| R3-I06 | 同一用户组通过 APN、UserProfile、SNSSAI 绑定的用户共享同一组规则和配额 | 3种绑定命令 | 一致性 |

### 3.3 BWM 规则优先级分层解析（priority_hierarchy_resolution）

**发现**：BWM 有多层优先级机制：用户组优先级(USERGROUPPRI) → 规则优先级(BWMRULEPRI) → 业务级别(SERVICELEVEL) → 控制器级别(BCSRVLEVELPLY)。这是一个四级嵌套的优先级解析。

**证据**：
- ADD BWMUSERGROUP: USERGROUPPRI 跨组优先级
- ADD BWMRULE: BWMRULEPRI 组内规则优先级
- ADD BWMCONTROLLER: SRVLEVELSPEC 业务级别规格
- ADD BCSRVLEVELPLY: 按 ServiceLevel 分配带宽比例

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R3-I07 | 4层优先级必须完整配置才能正确生效：用户组→规则→业务→控制器 | BWM全链 | 层级完整性 |
| R3-I08 | BWMRULETYPE=SUBSCRIBER_DEFAULT/SPECIFIC 的 SERVICELEVEL ≤ 5；GROUP 级 ≤ 30 | BWMRULE + BWMCONTROLLER | 属性兼容约束 |
| R3-I09 | BCSRVLEVELPLY 的 CIRRate 之和 > 10000 时，低优先级 ServiceLevel 无法获得承诺带宽 | BCSRVLEVELPLY | 资源分配约束 |

### 3.4 BWM vs QoS 冲突（policy_conflict）

**发现**：当用户的 BWM 规则和 PCC 策略中的 QOSPROP 同时匹配时，系统以 QOSPROP 为准作为 PDP 级带宽。这是一个策略冲突解决机制。

**证据**：
- ADD QOSPROP 注意事项："When both BWM Rule and QoSProp-bound PCC Rule match, use QOSPROP as PDP level bandwidth"
- 这意味着两条独立的配置路径可能产生冲突

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R3-I10 | BWM 规则和 QOSPROP 不应配置冲突的带宽值（虽然系统有解决机制，但表明配置冗余） | BWMRULE + QOSPROP + PCCPOLICYGRP | 策略冲突 |
| R3-I11 | SET QOSCAR 按 USERTYPE 配置，与 SET UPDEFAULTQUOTA 按 USERTYPE 配置是同一分区维度 | QOSCAR + UPDEFAULTQUOTA | 漫游分区一致性 |

### 3.5 带宽资源配额分割（resource_quota_partitioning）

**发现**：BCSRVLEVELPLY 将控制器总带宽按比例分配给不同 ServiceLevel，这是一个定量约束。

**证据**：
- ADD BCSRVLEVELPLY: CIRRate, PIRRate, ShapRate 都是万分比
- "所有 BCSrvLevelPly 的 CIRRate 之和 ≤ 100%"
- "CIRRate×CIR ≤ PIRRate×PIR"

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R3-I12 | 所有 ServiceLevel 的 CIRRate 之和应 < 10000（留余量给尽力而为流量） | BCSRVLEVELPLY | 资源分配 |
| R3-I13 | 控制器 CTRLTYPE=SHAPING 时 RATE 值应 ≥ 所有 ServiceLevel 的 CIRRate 对应速率之和 | BWMCONTROLLER + BCSRVLEVELPLY | 定量一致性 |

### 3.6 CP-UP 配置一致性（cp_up_consistency）

**发现**：SET CUINCONSPOLICY 和 SET CUSTATECHK 提供了 SMF/PGW-C 与 UPF/PGW-U 之间的配置一致性检查能力。这是核查领域本身的基础设施。

**证据**：
- SET CUINCONSPOLICY: 处理 CP 和 UP 关键配置不一致的策略
- SET CUSTATECHK: SMF 和 UPF 时间一致性校验
- DSP CUINCONSCONFIG: 显示不一致的关键配置

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R3-I14 | CUINCONSPOLICY.BYPASSSW=ENABLE 时允许不一致通过，可能导致计费错误 | CUINCONSPOLICY | 风险控制 |
| R3-I15 | CUSTATECHK 的 UTCDETECTMS 是 SMF/UPF 之间的时钟偏差容忍度，偏差过大→计费时间戳不准确 | CUSTATECHK | 跨系统一致性 |

### 3.7 漫游类型分区配置（roaming_type_partitioning）

**发现**：多个全局配置按漫游类型(HOME/ROAMING/VISITING)分区，不同分区独立配置。

**证据**：
- SET UPDEFAULTQUOTA: 按 USERTYPE 分区
- SET QOSCAR: 按 USERTYPE 分区
- 两者独立配置但作用于同一分区维度

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R3-I16 | 同一漫游类型的 UPDEFAULTQUOTA 和 QOSCAR 配置应协调（默认配额启用但 QoS 限速→用户体验差） | UPDEFAULTQUOTA + QOSCAR | 跨命令协调 |
| R3-I17 | VISITING 类型的用户通常没有在线计费，UPDEFAULTQUOTA 应为 DISABLE | UPDEFAULTQUOTA | 业务语义约束 |

### 3.8 生效时机差异（effect_timing_variations）

**发现**：本领域内有多种生效时机。

**证据**：
- QOSGLOBAL: 90 秒延迟生效
- QOSCAR: 仅对新激活用户生效
- BWMRULE 等: 立即生效
- UPDEFAULTQUOTA: 仅对承载更新或新激活用户生效

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R3-I18 | 修改 QOSGLOBAL 后 90 秒内 QoS 功能可能不一致 | QOSGLOBAL | 生效时机 |
| R3-I19 | 修改 QOSCAR 后已在线用户不受影响，新用户可能体验差异 | QOSCAR | 生效时机 |
