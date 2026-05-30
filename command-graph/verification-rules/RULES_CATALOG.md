# 核查规则全景目录 v2

基于 6 个领域（R1~R6）的规则挖掘结果，按 14 个算子族分类编排。
每条规则附原始证据、涉及命令、所属领域和严重度。

---

## 规则统计总览

| 领域 | 范围 | 显式规则 | 隐式规则 | 总计 |
|------|------|---------|---------|------|
| R1: 业务感知链 | 四三层匹配→七层→规则→动作→绑定 | 31 | 45 | 76 |
| R2: IP地址管理 | VPN→APN→POOL→SECTION→POOLGROUP→POOLGRPMAP | 12 | 25 | 37 |
| R3: QoS/计费/BWM | 计费链+带宽链+QoS链 | 18 | 19 | 37 |
| R4: 路径管理 | GTP/PFCP路径探测+黑白名单 | 7 | 7 | 14 |
| R5: 网络切片 | SNSSAI+接口绑定+专网分流 | 9 | 6 | 15 |
| R6: 可靠性/HA | 容灾组+DC通信+故障隔离+自愈 | 8 | 8 | 16 |
| **合计** | | **85** | **110** | **~195** |

---

## 算子族 1: 属性传播一致性（AP）

**定义**：沿引用链逐级检查属性值相等。上游对象的某属性值决定下游对象的约束。
**核查逻辑**：`for each ref(A→B): assert A.attr == B.attr`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| AP-01 | VPN 级联一致性：VPNINST→APN→POOL 的 VPNINSTNAME 必须一致 | R2 | VPNINST + APN + POOL | 显+隐 | "POOL 的 VPN 必须和 APN 的 VPN 一致" |
| AP-02 | SPECTYPE 兼容：RULE.RULESPECTYPE 必须与 USERPROFILE.UPSPECTYPE 一致才能绑定 | R1 | RULE + USERPROFILE + RULEBINDING | 显 | "DEFAULT类型的UserProfile只能绑定DEFAULT类型的Rule" |
| AP-03 | POOLBINDGROUP 中 POOLGROUPNAME 和 POOLNAME 对应的 VPN 必须一致 | R2 | POOLBINDGROUP + POOL + POOLGROUP | 显 | "同一个 POOLGROUP 下绑定的 POOL 必须属于同一个 VPN" |
| AP-04 | 切片标识 SST+SD 跨 SNSSAI/SNSSAIUPINTF/SNSSAIBWMUSRG 一致 | R5 | SNSSAI + SNSSAIUPINTF + SNSSAIBWMUSRG | 隐 | 多命令共用 SST+SD 作为引用键 |
| AP-05 | 容灾组 DRGROUPID/DRGROUPNAME 必须与本端对端节点一致 | R6 | DRGROUPINFO (本端+对端) | 显 | "DRGROUPID 和 DRGROUPNAME 必须与对端节点一致" |
| AP-06 | DRDCI 的对端 IP 必须与对端节点的本端 IP 一致 | R6 | DRDCI (本端+对端) | 隐 | LDRINSTID 和 PDRINSTID 互换关系 |
| AP-07 | DRDCI 的 HBINTERVAL 和 HBTIMES 本端对端应一致 | R6 | DRDCI (本端+对端) | 隐 | "否则一端先判定故障导致非对称倒换" |
| AP-08 | URRGROUP 中上行和下行的在线/离线计费类型应保持一致 | R3 | URRGROUP | 隐 | "否则部分流量无法计费" |
| AP-09 | RULE 的 CFGDOMAINNAME 应与引用的 FLOWFILTER/FLOWFILTERGRP 一致 | R1 | RULE + FLOWFILTER | 隐 | "否则可能跨域引用失败" |
| AP-10 | PCCPOLICYGRP 引用的 PCCACTIONPROP/URRGROUP/QOSPROP 应在同一配置域 | R1 | PCCPOLICYGRP + PCCACTIONPROP | 隐 | 从配置域分区语义推断 |
| AP-11 | PCCACTIONPROP 的上下行门控配置应一致 | R1 | PCCACTIONPROP | 显 | "报文动作需要上下行都配置且保持一致" |
| AP-12 | PBG-02: 向已有 POOL 的 POOLGROUP 添加新 POOL 时，VPN 必须与组内已有 POOL 一致 | R2 | POOLBINDGROUP | 隐 | 从增量一致性推断 |

---

## 算子族 2: 属性兼容约束（AC）

**定义**：上游对象的某属性取值约束了下游对象的可选参数或可执行操作。
**核查逻辑**：`if A.attr == X: assert B in allowed_values(X)`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| AC-01 | POLICYTYPE 约束 L7 绑定：WEBPROXY/IPREDIR/SRV_TRIGGER/LBO 禁止引用有七层绑定的 FlowFilter | R1 | RULE + PROTBINDFLOWF | 显 | "当策略类型为WEBPROXY、IPREDIR、SRV_TRIGGER或LBO时，不允许配置绑定了七层协议的流过滤器" |
| AC-02 | POOL TYPE 约束后续使用：EXTERNAL 类型需通过 POOLGRPMAP→APN 关联才生效 | R2 | POOL + POOLGRPMAP + APN | 显 | "仅当该地址池绑定的地址池组通过 POOLGRPMAP 关联到 APN 时生效" |
| AC-03 | APN 的 HASVPN=ENABLE 时 VPNINSTNAME 必选，HASVPN=DISABLE 时 VPNINSTNAME 不生效 | R2 | APN | 显 | "前提条件：该参数在HASVPN配置为ENABLE时为必选参数" |
| AC-04 | URR 的 USAGERPTMODE=ONLINE 时 DFTQUOTAVOLUME 和 DFTQUOTATIME 必选 | R3 | ADD URR | 显 | "USAGERPTMODE=ONLINE 时 DFTQUOTAVOLUME 和 DFTQUOTATIME 必选" |
| AC-05 | BWMRULETYPE 约束 SERVICELEVEL 范围：SUBSCRIBER_DEFAULT/SPECIFIC ≤ 5；GROUP 级 ≤ 30 | R3 | BWMRULE + BWMCONTROLLER | 隐 | 从参数范围约束推断 |
| AC-06 | 容灾模式约束 DRSEPINTERFACE 可用性：冷备模式下 DRSEPINTERFACE 无意义 | R6 | DRGROUPINFO + DRSEPINTERFACE | 显 | "DRSEPINTERFACE 只用于热备容灾模式" |
| AC-07 | L7FILTER 的 METHODTYPE/ISREFEREREN 仅对 http/connection-wap1.x/connectionless-wap1.x 生效 | R1 | L7FILTER + PROTBINDFLOWF | 显 | 注意事项中协议限制说明 |
| AC-08 | L7FILTER 的 USERAGENT 仅对 http/connection-wap1.x/connectionless-wap1.x 生效 | R1 | L7FILTER + PROTBINDFLOWF | 显 | 注意事项中协议限制说明 |
| AC-09 | L7FILTER 的 XHEADERNAME 仅对 http 协议生效 | R1 | L7FILTER + PROTBINDFLOWF | 显 | 注意事项中协议限制说明 |
| AC-10 | APN 的 APPLAYERVOLUME=ENABLE 时需配合业务感知链使用 | R2 | APN + 业务感知链命令 | 显 | "APPLAYERVOLUME=ENABLE 时需配合业务感知链使用" |
| AC-11 | BWMRULEGLOBAL 只支持 TOS 类业务，不支持 SHAPING 控制器 | R3 | BWMRULEGLOBAL | 显 | "只支持 TOS 类业务，不支持 SHAPING 控制器" |
| AC-12 | SET UPGTPPATH 的 ECHOLISTSWITCH=ENABLE 时需要 ECHOLISTTYPE 配置 | R4 | SET UPGTPPATH | 显 | "ECHOLISTSWITCH=ENABLE 时需要 ECHOLISTTYPE 配置" |
| AC-13 | SET UPGTPPATH 的 DEACTIVEFLAG=ENABLE 时 ECHOTIME 必选 | R4 | SET UPGTPPATH | 显 | "DEACTIVEFLAG=ENABLE 时 ECHOTIME 必选" |
| AC-14 | SET UPGTPPATH 的 V1DATAECHOSW=ENABLE 时 LOGICINFTYPE 必选 | R4 | SET UPGTPPATH | 显 | "V1DATAECHOSW=ENABLE 时 LOGICINFTYPE 必选" |
| AC-15 | SNSSAIUPINTF 不支持 INSTANCE 数据面接口模式 | R5 | SNSSAIUPINTF | 显 | "SNSSAIUPINTF 不支持 INSTANCE 数据面接口模式" |
| AC-16 | SNSSAIUPINTF 默认接口(N3if1/1/0, Saif1/1/0)不能绑定 | R5 | SNSSAIUPINTF | 显 | "默认接口不能绑定" |
| AC-17 | SNSSAIUPINTF: MBS 会话的 n3mbif 不能绑定 | R5 | SNSSAIUPINTF | 显 | "MBS 会话的 n3mbif 不能绑定" |
| AC-18 | TOS 配置仅适用于 ACL 功能，不适用于计费策略和动作策略 | R1 | ADD FILTER | 显 | "TOS配置仅适用于ACL的相关功能" |
| AC-19 | 全局用户组只支持 TOS 类型业务 | R3 | BWMUSERGROUP | 显 | "全局用户组只支持 TOS 类型业务" |
| AC-20 | 不能绑定到默认或全局用户组 | R3 | APNBINDBWMUSRG | 显 | "不能绑定到默认或全局用户组" |
| AC-21 | DRDCI 的 VPNINSTANCE 必须已存在 | R6 | DRDCI | 显 | "VPNINSTANCE 必须已存在" |

---

## 算子族 3: 参数互斥（PE）

**定义**：两个参数不能同时取某些值组合。
**核查逻辑**：`assert not (A==X and B==Y)`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| PE-01 | IPLEASE=ENABLE 且 RELEASETIME=0 → 配置冲突，地址永不释放 | R2 | ADD POOL | 显 | "IPLEASE=ENABLE 时，RELEASETIME 必须大于 0" |
| PE-02 | PCCACTIONPROP 上下行方向不一致导致业务不通 | R1 | PCCACTIONPROP | 显 | "配置不一致可能导致业务不通" |
| PE-03 | GLBURRGROUP 绑定的 URR 的 METERINGTYPE 不能包含 EVENT | R3 | GLBURRGROUP | 显 | "GLBURRGROUP 绑定的 URR 的 METERINGTYPE 不能包含 EVENT" |
| PE-04 | QOSCAR 的 CAR 和 Shaping 不能同时使能 | R3 | QOSCAR | 显 | "CAR 和 Shaping 不能同时使能" |
| PE-05 | BWMRULE: 同一用户组下 TOS 业务类型不能相同 | R3 | BWMRULE | 显 | "同一用户组下 TOS 业务类型不能相同" |
| PE-06 | L34PROTOCOL=ICMP 或 GRE 时，不允许配置端口 | R1 | ADD FILTER | 显 | "当L34PROTOCOL选择为ICMP或GRE时，不允许配置端口" |
| PE-07 | MSIPMASK / SVRIPMASK 不允许配置为 255.255.255.255 | R1 | ADD FILTER | 显 | "反掩码不支持配置为255.255.255.255" |
| PE-08 | 外置规则库定义的 FlowFilter 与 Filter 和 L7Filter 不共存 | R1 | FLOWFILTER | 显 | "外置规则库定义属性的流过滤器同过滤器和七层过滤器不共存" |
| PE-09 | SET UPDEFAULTQUOTA.ENABLE 但 GLBURRGROUP 的配额 URR 未配 DFTQUOTAVOLUME → 默认配额无效 | R3 | UPDEFAULTQUOTA + URR | 隐 | 从配额传递链推断 |
| PE-10 | BWMRULE 时间段不能重叠且 ≥ 30分钟 | R3 | BWMRULE | 显 | "时间段不能重叠且 ≥ 30分钟" |
| PE-11 | BWMRULE 规则优先级不能重复 | R3 | BWMRULE | 显 | "规则优先级不能重复" |
| PE-12 | PCC 和 QOS 类型不能使用相同的 RULENAME | R1 | RULE | 显 | "PCC 和 QOS 类型不能使用相同的 RULENAME" |
| PE-13 | ADD RULE 和 ADD BLACKLISTRULE 共享 (RULENAME, POLICYTYPE) 命名空间 | R1 | RULE + BLACKLISTRULE | 显 | "ADD RULE 和 ADD BLACKLISTRULE 共享命名空间" |

---

## 算子族 4: 查找表覆盖度（LC）

**定义**：查找表（映射关系）必须覆盖所有可能的输入组合，否则某些场景查找失败。
**核查逻辑**：`for each input in domain: assert lookup(input) != null`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| LC-01 | POOLGRPMAP 的 (TAC+APN+SMF)→POOLGROUP 必须覆盖所有用户组合，否则无法分配 IP | R2 | POOLGRPMAP + POOLGROUP | 隐 | 没有匹配条目时用户无法获取 IP |
| LC-02 | PCCPOLICYGRP 多组合匹配：默认组合优先级最低，非默认组合按 ServiceProp 优先级 | R1 | PCCPOLICYGRP + SRVPBINDPCCPG | 显 | "如果PccPolicyGrp配置了多种组合，则匹配优先级取决于ServiceProp优先级" |
| LC-03 | ADC 切换链/环检测：ADC RULE 的 REPLACEUPNAME 构成的切换图不能有环 | R1 | RULE + USERPROFILE | 显 | "同一用户命中ADC类型最多切换10次" |
| LC-04 | BWM 用户组多维度绑定：APN/UserProfile/SNSSAI 三维度绑定，优先级最高的生效 | R3 | BWMUSERGROUP + 3种绑定命令 | 隐 | "多个 BwmUserGroup 时，优先级最高的生效" |
| LC-05 | 每个在用的 SNSSAI 应至少有一个 SNSSAIUPINTF 绑定（除非使用默认接口） | R5 | SNSSAI + SNSSAIUPINTF | 隐 | "未绑定的切片使用默认接口" |
| LC-06 | ECHOLISTTYPE=WHITE 但 ECHOIPLIST 为空 → 不对任何 IP 做探测 → 所有路径不可达 | R4 | UPGTPPATH + ECHOIPLIST | 隐 | 从黑白名单语义推断 |
| LC-07 | 用户不匹配任何 BWMUSERGROUP → 使用 DEFAULT_GROUP | R3 | BWMUSERGROUP | 隐 | 从默认组机制推断 |
| LC-08 | POOLGRPMAP 中 (通配, APN1, 通配) 和 (TAC1, APN1, SMF1) 共存时精确匹配优先 | R2 | POOLGRPMAP | 隐 | 从查找语义推断 |
| LC-09 | 同一 APN 的 IPv4 和 IPv6 地址需分别配置 POOLGRPMAP | R2 | POOLGRPMAP + POOLGROUP | 隐 | 从双栈语义推断 |
| LC-10 | GLBURRGROUP 未配置且用户未匹配任何 PCC 规则 → 无法计费 | R3 | GLBURRGROUP + PCCPOLICYGRP | 隐 | 从计费层级推断 |

---

## 算子族 5: 引用可达性（RR）

**定义**：引用链终端必须有有效对象（非空壳、非悬空）。
**核查逻辑**：`for each ref(A→B): assert B exists and B.content != empty`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| RR-01 | 删除被引用对象后，绑定关系不会自动清除，产生悬空引用 | R1 | FLTBINDFLOWF + RMV FILTER | 隐 | 从引用关系语义推断 |
| RR-02 | FLOWFILTER 既没有 FLTBINDFLOWF 也没有 PROTBINDFLOWF → 空容器，永不匹配 | R1 | FLOWFILTER + FLTBINDFLOWF + PROTBINDFLOWF | 隐 | 从容器语义推断 |
| RR-03 | RULE(WEBPROXY/SMARTREDIRECT) 引用的 IPFarm 必须至少有一个 IPFARMSERVER | R1 | RULE + IPFARM + IPFARMSERVER | 隐 | 从服务器池语义推断 |
| RR-04 | GLBURRGROUP 未配置且无 PCC 规则匹配 → 无法计费 | R3 | GLBURRGROUP + PCCPOLICYGRP | 隐 | 从计费层级推断 |
| RR-05 | 热备模式下应有至少一个 DRDCI 通道，否则心跳无法传递 | R6 | DRGROUPINFO + DRDCI | 隐 | "热备模式下应有 DRDCI 通道" |
| RR-06 | SNSSAIUPINTF/SNSSAIBWMUSRG 引用的 SST+SD 必须在 SNSSAI 中已定义 | R5 | SNSSAI + SNSSAIUPINTF | 隐 | 从切片标识引用语义推断 |
| RR-07 | POOLGRPMAP 引用的 TACGROUPNAME/APNNAME/CPNODEIDNAME/POOLGROUPNAME 必须存在 | R2 | POOLGRPMAP + TACGROUP/APN/CPNODEID/POOLGROUP | 隐 | 从引用完整性推断 |
| RR-08 | POOLGRPMAP 引用的 POOLGROUP 必须有至少一个 POOLBINDGROUP | R2 | POOLGRPMAP + POOLGROUP + POOLBINDGROUP | 隐 | 从空组检测推断 |
| RR-09 | SET GLBEXTFILTER 配置的 EXTFLTNAME 如果被删除 → 全局过滤条件异常 | R1 | GLBEXTFILTER + EXTENDEDFILTER | 隐 | 从引用关系推断 |
| RR-10 | FLOWFILTERGRP 引用了空 FLOWFILTER → 匹配行为不确定 | R1 | FLOWFILTERGRP + FLOWFILTER | 隐 | 从分组语义推断 |
| RR-11 | 有 GLBEXTFILTER 配置但无重定向 RULE → GLBEXTFILTER 无意义 | R1 | GLBEXTFILTER + RULE | 隐 | 从双重过滤机制推断 |
| RR-12 | LOCAL 类型 POOL 必须有至少一个 SECTION 才能分配地址 | R2 | POOL + SECTION | 隐 | 从地址分配语义推断 |

---

## 算子族 6: 跨网元一致性（CN）

**定义**：同一逻辑对象在不同网元/平台上需保持一致。
**核查逻辑**：`assert local.config == remote.config`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| CN-01 | VPNINST↔L3VPNINST：UDG 侧的每个 VPNINST 必须在 VNRS 有对应的 L3VPNINST | R2 | VPNINST + L3VPNINST(VNRS) | 显 | "VPN 实例需要通过 ADD L3VPNINST 命令在 VNRS 平台同步配置" |
| CN-02 | IPFARMSERVER 地址需与 SMF 的 PCSCFIP 地址一致（P-CSCF 检测场景） | R1 | IPFARMSERVER + SMF PCSCFIP | 隐 | "IPFARMSERVER 地址需要与 SMF 的 PCSCFIP 地址一致" |
| CN-03 | DRGROUPINFO 本端 LDRINSTID = 对端 PDRINSTID，本端 PDRINSTID = 对端 LDRINSTID | R6 | DRGROUPINFO (本端+对端) | 隐 | LDRINSTID 和 PDRINSTID 互换关系 |
| CN-04 | SMF↔UPF 时间一致性：CUSTATECHK 校验 SMF/UPF 时钟偏差 | R3 | CUSTATECHK | 显 | "SMF 和 UPF 时间一致性校验" |
| CN-05 | CP↔UP 关键配置一致性：CUINCONSPOLICY 检查 CP/UP 配置 | R3 | CUINCONSPOLICY | 显 | "处理 CP 和 UP 关键配置不一致的策略" |
| CN-06 | VPNINST 删除前需先删除 VNRS 侧的 L3VPNINST | R2 | VPNINST + L3VPNINST(VNRS) | 隐 | 从删除顺序推断 |
| CN-07 | CUINCONSPOLICY.BYPASSSW=ENABLE 时允许不一致通过，可能导致计费错误 | R3 | CUINCONSPOLICY | 隐 | "BYPASSSW=ENABLE 时允许不一致通过" |
| CN-08 | CUSTATECHK 的 UTCDETECTMS 是 SMF/UPF 之间的时钟偏差容忍度，偏差过大→计费时间戳不准确 | R3 | CUSTATECHK | 显 | "UTCDETECTMS > 5000 可能导致计费时间戳不准" |

---

## 算子族 7: 平行维度独立（PD）

**定义**：多个维度独立匹配，互不影响。
**核查逻辑**：`for each dimension: validate_independently()`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| PD-01 | 14 种 POLICYTYPE（PCC/BWM/HEADEN/WEBPROXY/...）独立匹配，不同类型可同时生效 | R1 | RULE | 显 | "不同 POLICYTYPE 独立匹配" |
| PD-02 | 漫游类型分区：HOME/ROAMING/VISITING 独立配置 UPDEFAULTQUOTA 和 QOSCAR | R3 | UPDEFAULTQUOTA + QOSCAR | 显 | "按 USERTYPE 分区" |
| PD-03 | 同一 POLICYTYPE 内多个 Rule 按优先级选取一个执行 | R1 | RULE | 显 | "同一 POLICYTYPE 内按 PRIORITY 选取" |
| PD-04 | RULEBINDING 不指定 POLICYTYPE 时，将同名不同类型的 Rule 全部绑定 | R1 | RULEBINDING | 显 | "不指定 POLICYTYPE 时全部绑定" |
| PD-05 | BWMRULE + BWMRULEGLOBAL 共享 5000 条配额 | R3 | BWMRULE + BWMRULEGLOBAL | 显 | "共享 5000 条配额" |
| PD-06 | 同一 SST+SD 绑定到不同 N3 接口时，流量可能分散到不同路径 | R5 | SNSSAIUPINTF | 隐 | 从多接口绑定语义推断 |

---

## 算子族 8: 生效时机差异（ET）

**定义**：同一条链路上不同对象的变更生效机制不同，可能导致配置不一致。
**核查逻辑**：`for each obj in chain: if recently_modified(obj): check_effect_status(obj)`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| ET-01 | Filter/FilterIPv6 需手动 SET REFRESHSRV 刷新才生效 | R1 | FILTER + REFRESHSRV | 显 | "需要等待执行SET REFRESHSRV命令刷新后生效" |
| ET-02 | L7FILTER/PROTBINDFLOWF/EXTENDEDFILTER 60s 自动生效 | R1 | L7FILTER + PROTBINDFLOWF | 显 | "60s 自动生效" |
| ET-03 | FLOWFILTERGRP 和 RULEBINDING 只对新激活用户生效 | R1 | FLOWFILTERGRP + RULEBINDING | 显 | "只对新激活用户生效" |
| ET-04 | SET REFRESHSRV 执行后 30s 内不允许修改 Filter 和被绑定的 IPList | R1 | REFRESHSRV | 显 | "30 秒内不允许修改" |
| ET-05 | POOL/SECTION/APN/VPNINST 立即生效；POOLGROUP/POOLBINDGROUP/POOLGRPMAP 仅对新用户 | R2 | 全链路命令 | 显 | 多命令注意事项对比 |
| ET-06 | QOSGLOBAL 90 秒延迟生效 | R3 | QOSGLOBAL | 显 | "90 秒延迟生效" |
| ET-07 | QOSCAR 仅对新激活用户生效 | R3 | QOSCAR | 显 | "仅对新激活用户生效" |
| ET-08 | SNSSAIUPINTF 只影响新的 PFCP 消息 | R5 | SNSSAIUPINTF | 显 | "只影响新的 PFCP 消息" |
| ET-09 | UPDEFAULTQUOTA 仅对承载更新或新激活用户生效 | R3 | UPDEFAULTQUOTA | 显 | "仅对承载更新或新激活用户生效" |
| ET-10 | 修改 Filter 后须 SET REFRESHSRV，但 L7FILTER 只需等 60s → 同链路生效机制不一致 | R1 | FILTER + L7FILTER | 隐 | 对比两条命令的生效说明 |
| ET-11 | SET REFRESHSRV 只管 Filter/FilterGroup/Acl/AclNode 的刷新，不管 L7FILTER/FLOWFILTERGRP | R1 | REFRESHSRV + 多命令 | 隐 | 对比刷新范围 |
| ET-12 | POOL 容量变更立即生效，但 POOLGROUP 分配策略仅对新用户 → 配置变更窗口风险 | R2 | SECTION + POOLGROUP | 隐 | 对比生效时机 |

---

## 算子族 9: 地址空间约束（AS）

**定义**：IP 地址/地址段的区间约束。
**核查逻辑**：区间重叠检测 + 掩码一致性检查

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| AS-01 | 同一 VPN 内任意两个 SECTION 的 [STARTIP, ENDIP] 区间不能重叠 | R2 | SECTION + POOL + VPNINST | 显 | "地址段不能与同一 VPN 实例下的其他地址段重叠" |
| AS-02 | SECTION 的 MASK 影响路由聚合效率，过小导致路由表膨胀 | R2 | SECTION | 显 | "MASK 影响路由聚合效率，过小会导致路由表膨胀" |
| AS-03 | IPv4 和 IPv6 的重叠检测是独立的（不同地址族） | R2 | SECTION | 隐 | 从地址空间语义推断 |
| AS-04 | 同一 POOL 下所有 SECTION 的 MASK 建议一致 | R2 | SECTION | 隐 | 从路由聚合语义推断 |
| AS-05 | MASK 越小，单个 ISU Pod 承载的地址越多 | R2 | SECTION | 隐 | 从 ISU 分布机制推断 |
| AS-06 | MULTICAST 类型 POOL 的地址段需满足组播地址范围 224.0.0.0~239.255.255.255 | R2 | POOL + SECTION | 隐 | 从组播语义推断 |

---

## 算子族 10: 多策略冲突（PC）

**定义**：多条独立的配置路径可能对同一对象产生冲突的控制策略。
**核查逻辑**：`for each target: collect_all_policies(target); detect_conflict()`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| PC-01 | GLBEXTFILTER + REDIRECT 双重过滤：有重定向 RULE 但无 GLBEXTFILTER → 所有匹配流量都被重定向 | R1 | GLBEXTFILTER + RULE + REDIRECT | 隐 | "只有符合扩展过滤器的条件，才能执行重定向动作" |
| PC-02 | BWM 规则 vs QOSPROP 带宽冲突：两者同时匹配时以 QOSPROP 为准，但表明配置冗余 | R3 | BWMRULE + QOSPROP + PCCPOLICYGRP | 显 | "When both BWM Rule and QoSProp-bound PCC Rule match, use QOSPROP" |
| PC-03 | SET REFRESHSRV 刷新范围不覆盖 L7FILTER/FLOWFILTERGRP 等对象 | R1 | REFRESHSRV + 多命令 | 隐 | 对比刷新范围 |
| PC-04 | 同一漫游类型的 UPDEFAULTQUOTA 和 QOSCAR 配置应协调（默认配额启用但 QoS 限速→体验差） | R3 | UPDEFAULTQUOTA + QOSCAR | 隐 | 两者作用于同一分区维度 |
| PC-05 | VISITING 类型的用户通常没有在线计费，UPDEFAULTQUOTA 应为 DISABLE | R3 | UPDEFAULTQUOTA | 隐 | 从业务语义推断 |
| PC-06 | CUINCONSPOLICY.BYPASSSW=ENABLE 允许 CP/UP 不一致通过，可能导致计费错误 | R3 | CUINCONSPOLICY | 隐 | 从风险控制角度推断 |
| PC-07 | ADC RULE 不能绑定到 REPLACEUPNAME 对应的 USERPROFILE 下（否则形成自引用） | R1 | RULE + RULEBINDING + USERPROFILE | 显 | "不应将此规则绑定到ReplaceUpName对应的userprofile下" |

---

## 算子族 11: 分区可见性（PV）

**定义**：配置按某种维度分区，不同分区的对象可能有引用限制。
**核查逻辑**：`for each cross-partition ref: assert allowed(partition_A, partition_B)`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| PV-01 | CFGDOMAINNAME 跨域引用限制：RULE 与 FLOWFILTER 不在同一配置域可能导致引用失败 | R1 | RULE + FLOWFILTER + 多命令 | 隐 | 多命令均有 CFGDOMAINNAME 参数 |
| PV-02 | 漫游类型分区配置协调：HOME/ROAMING/VISITING 的配置需分别完整 | R3 | UPDEFAULTQUOTA + QOSCAR | 显 | "按 USERTYPE 分区" |
| PV-03 | 切片分区：不同切片（SST+SD）绑定不同 N3 接口 | R5 | SNSSAI + SNSSAIUPINTF | 隐 | 从接口绑定语义推断 |
| PV-04 | DRDCI 使用的 VPN 实例应与容灾对端可达（跨 DC 的 VPN 路由正确） | R6 | DRDCI + VPNINST | 隐 | 从跨 DC 通信需求推断 |

---

## 算子族 12: 定量计算约束（QC）

**定义**：参数之间存在算术关系，需满足不等式或等式。
**核查逻辑**：`assert formula(params) holds`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| QC-01 | BCSRVLEVELPLY: 所有 CIRRate 之和 ≤ 10000（万分比，即 100%） | R3 | BCSRVLEVELPLY | 显 | "所有 BCSrvLevelPly 的 CIRRate 之和 ≤ 100%" |
| QC-02 | BCSRVLEVELPLY: CIRRate×CIR ≤ PIRRate×PIR | R3 | BCSRVLEVELPLY | 显 | "CIRRate×CIR ≤ PIRRate×PIR" |
| QC-03 | PIR ≥ CIR（BWMCONTROLLER 两者都配时） | R3 | BWMCONTROLLER | 显 | "PIR ≥ CIR" |
| QC-04 | DRDCI 心跳超时 = HBINTERVAL × 100ms × HBTIMES，最大 300s | R6 | DRDCI | 隐 | "HBINTERVAL: 心跳间隔（1-100，单位 100ms），HBTIMES: 重试次数（1-30）" |
| QC-05 | GTP 路径探测超时 ≈ T3RESPONSE × N3REQUEST + ECHOINTERVAL | R4 | UPGTPPATH | 隐 | "T3RESPONSE: 1-20秒，N3REQUEST: 1-6次，ECHOINTERVAL: 60-3600秒" |
| QC-06 | SET CUINCONSPOLICY: CHGATTRRPTTHD 必须 > CHGATTRCLRTHD | R3 | CUINCONSPOLICY | 显 | "CHGATTRRPTTHD 必须 > CHGATTRCLRTHD" |
| QC-07 | SET CUSTATECHK: UTCALMCLRTHD 必须 < UTCALMRPTTHD | R3 | CUSTATECHK | 显 | "UTCALMCLRTHD 必须 < UTCALMRPTTHD" |
| QC-08 | 所有 ServiceLevel 的 CIRRate 之和应 < 10000（留余量给尽力而为流量） | R3 | BCSRVLEVELPLY | 隐 | 从资源分配推断 |
| QC-09 | 控制器 CTRLTYPE=SHAPING 时 RATE 应 ≥ 所有 ServiceLevel 的 CIRRate 对应速率之和 | R3 | BWMCONTROLLER + BCSRVLEVELPLY | 隐 | 从定量一致性推断 |
| QC-10 | HBINTERVAL × HBTIMES 设得太大 → 故障发现慢 | R6 | DRDCI | 隐 | "最大检测时间 = 10s × 30 = 300s" |
| QC-11 | DEACTIVEFLAG=ENABLE 但 ECHOTIME 设置过小 → 短暂网络波动导致大规模用户去激活 | R4 | UPGTPPATH | 隐 | 从风险控制角度推断 |

---

## 算子族 13: 故障级联（FC）

**定义**：底层对象的故障会级联影响到上层对象。
**核查逻辑**：`for each dependency_chain: assert no_broken_link()`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| FC-01 | GTP 路径故障 → 用户去激活（DEACTIVEFLAG=ENABLE 时） | R4 | UPGTPPATH | 显 | "DEACTIVEFLAG=ENABLE 时路径故障触发用户去激活" |
| FC-02 | VPN 路由不可达 → 地址分配失败 | R2 | VPNINST + APN + POOL | 隐 | 从地址分配依赖推断 |
| FC-03 | DRDCI 心跳失败 → 容灾倒换 | R6 | DRDCI + DRGROUPINFO | 隐 | 从容灾机制推断 |
| FC-04 | DEACTIVEFLAG=DISABLE 时路径故障仅告警，用户保持连接但可能无法正常传输数据 | R4 | UPGTPPATH | 隐 | 从功能缺失角度推断 |
| FC-05 | GLBURRGROUP 未配置且用户无 PCC 匹配 → 计费数据丢失 | R3 | GLBURRGROUP + PCCPOLICYGRP | 隐 | 从计费链完整性推断 |

---

## 算子族 14: 删除顺序保护（DO）

**定义**：存在引用关系的对象必须按特定顺序删除。
**核查逻辑**：`for each delete(A): assert no_ref_to(A) exists`

| # | 规则 | 领域 | 涉及命令 | 显/隐 | 原文证据 |
|---|------|------|---------|-------|---------|
| DO-01 | 删除 SNSSAI 前，需先删除引用它的 SNSSAIUPINTF 和 SNSSAIBWMUSRG | R5 | SNSSAI + SNSSAIUPINTF + SNSSAIBWMUSRG | 隐 | 从引用保护推断 |
| DO-02 | POOL 有 SECTION 时不能改 VPN | R2 | POOL + SECTION | 显 | "POOL 有 SECTION 时不允许修改 VPNINSTNAME" |
| DO-03 | 被引用的 PCCPOLICYGRP 不允许删除 | R1 | PCCPOLICYGRP + RULE | 显 | "被绑定的 PCCPOLICYGRP 不允许删除" |
| DO-04 | VPNINST 删除前需先删除 VNRS 侧的 L3VPNINST | R2 | VPNINST + L3VPNINST(VNRS) | 隐 | 从跨网元删除顺序推断 |
| DO-05 | FLOWFILTERTYPE=EXTEROTTDB 时，不允许修改属性，只允许删除 | R1 | FLOWFILTER | 显 | "不允许修改该属性，只允许删除" |

---

## 未分类：容量/规格规则

| # | 规则 | 领域 | 涉及命令 | 原文证据 |
|---|------|------|---------|---------|
| CAP-01 | Filter+FilterIPv6 总记录数最大 150000 | R1 | ADD FILTER | "Filter和FilterIPv6的总记录数最大为150000" |
| CAP-02 | 配置记录数 >85% 规格时上报告警 | R1 | ADD FILTER | "配置记录数大于规格的85%时，上报ALM-135602215" |
| CAP-03 | 系统最多 500 条 IPList，每个最多 200 个 IP 地址段，总绑定 20000 条 | R1 | ADD IPLIST | "系统最多支持配置500条IPList" |
| CAP-04 | FLOWFILTER 最大记录数 100000 | R1 | ADD FLOWFILTER | "最大记录数为100000" |
| CAP-05 | FLTBINDFLOWF 最大记录数 300000 | R1 | ADD FLTBINDFLOWF | "最大记录数为300000" |
| CAP-06 | 单个 FlowFilter 最多 5000 个 Filter | R1 | ADD FLTBINDFLOWF | "单个FlowFilter可以配置Filter和FilterIPv6总数为5000个" |
| CAP-07 | 每个 POOL 最多 64 个 SECTION | R2 | ADD SECTION | "每个 POOL 最多 64 个 SECTION" |
| CAP-08 | 每个 VPN 下每个 POOLGROUP 最多 16 个 POOL | R2 | ADD POOLBINDGROUP | "每个 VPN 下每个 POOLGROUP 最多绑定 16 个 POOL" |
| CAP-09 | BWMRULE + BWMRULEGLOBAL 共享 5000 条配额 | R3 | BWMRULE/BWMRULEGLOBAL | "共享 5000 条配额" |
| CAP-10 | 用户组最多绑定 16 个 APN/UserProfile/切片 | R3 | APNBINDBWMUSRG | "用户组最多绑定 16 个" |
| CAP-11 | DRDCI 最大 16 条记录 | R6 | ADD DRDCI | "最大 16 条记录" |
| CAP-12 | DRSEPINTERFACE 最大 65535 条 | R6 | ADD DRSEPINTERFACE | "最大 65535 条" |
| CAP-13 | ECHOIPLIST 最大 200 条 | R4 | ADD ECHOIPLIST | "最大 200 条" |
| CAP-14 | SNSSAI 最大 8192 条 | R5 | ADD SNSSAI | "最大 8192 条" |
| CAP-15 | SLICEINSTINFO 最大 128 条 | R5 | ADD SLICEINSTINFO | "最大 128 条" |
| CAP-16 | URRGROUP 至少要有一个 UPURRNAME 或 DOWNURRNAME | R3 | ADD URRGROUP | "至少要有一个 UPURRNAME 或 DOWNURRNAME" |
| CAP-17 | DRGROUPINFO 只允许 1 条记录 | R6 | ADD DRGROUPINFO | "只允许 1 条记录" |
| CAP-18 | ECHOINTERVAL 范围 60-3600 秒 | R4 | SET UPGTPPATH | "ECHOINTERVAL 范围 60-3600 秒" |
| CAP-19 | N3REQUEST 范围 1-6 | R4 | SET UPGTPPATH | "N3REQUEST 范围 1-6" |
| CAP-20 | T3RESPONSE 范围 1-20 秒 | R4 | SET UPGTPPATH | "T3RESPONSE 范围 1-20 秒" |
| CAP-21 | SNSSAI 的 SST 必须在 0-255 范围内 | R5 | ADD SNSSAI | "SST 必须在 0-255 范围内" |
| CAP-22 | SNSSAI 的 SD 必须是 6 位十六进制 | R5 | ADD SNSSAI | "SD 必须是 6 位十六进制" |

---

## 未分类：高危/风险警告

| # | 规则 | 领域 | 涉及命令 | 原文证据 |
|---|------|------|---------|---------|
| RISK-01 | DRDCI 是高危命令，可能导致业务中断 | R6 | ADD DRDCI | "DRDCI 是高危命令" |
| RISK-02 | SNSSAIUPINTF 是高危命令，变更可能导致业务中断 | R5 | ADD SNSSAIUPINTF | "SNSSAIUPINTF 是高危命令" |
| RISK-03 | 建议一个业务匹配中的过滤器数目不超过 500 | R1 | ADD FILTER | "避免一个业务能匹配中的过滤器数目过多（超过500）" |
| RISK-04 | 向 IPList 添加 IP 后，如果被 Filter 绑定，会自动生成 Filter，消耗规格 | R1 | ADD IPLIST | "IPList如果被绑定到Filter中，系统会自动生成Filter" |
| RISK-05 | MASKVALUE 配置过小会导致 IP 匹配范围变大 | R1 | ADD IPLIST | "MASKVALUE参数配置过小会导致ip匹配范围变大" |
| RISK-06 | FLTBINDFLOWF 绑定操作可能导致性能下降 | R1 | ADD FLTBINDFLOWF | "可能导致性能下降" |
| RISK-07 | DRGROUPINFO 只用于冷备/热备容灾模式 | R6 | ADD DRGROUPINFO | "只用于冷备/热备容灾模式" |
| RISK-08 | DRDCI 使用的 VPN 实例应与容灾对端可达 | R6 | DRDCI + VPNINST | 隐 |
| RISK-09 | CUSTATECHK: UTCDETECTMS > 5000 可能导致计费时间戳不准 | R3 | CUSTATECHK | "UTCDETECTMS > 5000 可能导致计费时间戳不准" |
| RISK-10 | ECHOLISTTYPE=BLACK 时，所有不在名单内的 IP 都会被探测 | R4 | SET UPGTPPATH | 隐 |
| RISK-11 | UAC 路径参数应与普通路径参数协调 | R4 | SET UPGTPPATH | 隐 |
| RISK-12 | 同一用户切换 ADC 用户模板后，会忽略后续 SMF 下发的用户模板 | R1 | RULE | "同一用户切换过用户模板后，会忽略后续SMF下发的用户模板" |

---

## 规则 → 算子族映射汇总

| 算子族 | 规则数 | 覆盖领域 | 实现难度 |
|--------|--------|---------|---------|
| 1 属性传播一致性 (AP) | 12 | R1-R6 | 低 |
| 2 属性兼容约束 (AC) | 21 | R1-R6 | 中 |
| 3 参数互斥 (PE) | 13 | R1-R3 | 低 |
| 4 查找表覆盖度 (LC) | 10 | R1-R5 | 高 |
| 5 引用可达性 (RR) | 12 | R1-R6 | 低 |
| 6 跨网元一致性 (CN) | 8 | R1-R3,R6 | 高 |
| 7 平行维度独立 (PD) | 6 | R1,R3,R5 | 低 |
| 8 生效时机差异 (ET) | 12 | R1-R3,R5 | 中 |
| 9 地址空间约束 (AS) | 6 | R2 | 中 |
| 10 多策略冲突 (PC) | 7 | R1,R3 | 中 |
| 11 分区可见性 (PV) | 4 | R1,R3,R5,R6 | 中 |
| 12 定量计算约束 (QC) | 11 | R3-R4,R6 | 低 |
| 13 故障级联 (FC) | 5 | R2-R4,R6 | 高 |
| 14 删除顺序保护 (DO) | 5 | R1-R2,R5 | 低 |
| 容量/规格 | 22 | R1-R6 | 低 |
| 高危/风险 | 12 | R1-R6 | 低 |
| **合计** | **~176** | | |
