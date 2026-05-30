# 核查规则挖掘工作记录

## 0. 工作目标

从 UDG（UPF）侧 MML 命令原始文档中系统性挖掘核查规则范式。

**目标用户**：需要评估"现网配置 + 动网配置"准确性的运维工程师。
**最终产出**：为后续核查算子设计提供依据的规则范式归纳。

---

## 1. 工作边界

### 命令范围

只看 **UDG（UPF）侧** MML 命令，判断标准：命令原始 md 文档存在于 `UDG MML命令/` 目录下。

### 两个专题来源

| 专题 | 文档根目录 |
|------|-----------|
| UDG业务感知专题 | `特性部署/业务专题/UDG业务感知专题/` |
| 5G Core 用户IP地址管理解决方案 | `特性部署/业务专题/5G Core 用户IP地址管理解决方案/` |

### 不做的事

- 不看 SMF/UNC 侧命令（CCT、CHFINIT、CHARGECTRL 等）
- 不看 VNRS 平台命令（ADD L3VPNINST、ADD OSPF 等）
- 不看 PCF 命令
- 不做代码实现，只做规则挖掘和归纳
- 不预设规则分类，从文档中归纳
- 不回看已有 CSV 产出（parameters.csv 等），直接读原始 md

---

## 2. 信息源（每条命令的三部分）

| # | 信息源 | 说明 |
|---|--------|------|
| 1 | 命令原始 md 文档 | 完整读取参数说明 + 注意事项 + 使用实例 |
| 2 | 专题文档中该命令出现的上下文 | 从专题 md 中找到命令被使用的场景、套餐脚本、前后文 |
| 3 | 关联命令的 md | 通过引用关系（"配置生成"、"前置条件"等）找到上下游命令，一并阅读 |

---

## 3. 命令清单与批次规划

### 批次 1：三四层识别→组合链（业务感知专题）

| 命令 | 配置对象 | 预期关联 |
|------|---------|---------|
| ADD FILTER | Filter | 被 ADD FLTBINDFLOWF 引用 |
| ADD IPLIST | IPList | 被 ADD FILTER 的 SVRIPLISTNAME 参数引用 |
| ADD FLOWFILTER | FlowFilter | 容器，绑定 Filter 和 Protocol |
| ADD FLTBINDFLOWF | FltBindFlowF | Filter 绑定到 FlowFilter |

### 批次 2：七层识别→组合链（业务感知专题）

| 命令 | 配置对象 | 预期关联 |
|------|---------|---------|
| ADD L7FILTER | L7Filter | 七层匹配条件 |
| ADD PROTBINDFLOWF | ProtBindFlowF | Protocol + L7Filter 绑定到 FlowFilter |
| ADD FLOWFILTERGRP | FlowFilterGroup | FlowFilter 分组 |

### 批次 3：规则→策略链（业务感知专题）

| 命令 | 配置对象 | 预期关联 |
|------|---------|---------|
| ADD RULE | Rule（含 CHARGINGRULE/BWMRULE/BLACKLISTRULE 等） | 核心规则对象 |
| ADD PCCPOLICYGRP | PCCPolicyGrp | PCC 策略组，被 Rule 引用 |

### 批次 4：动作→绑定→生效链（业务感知专题）

| 命令 | 配置对象 | 预期关联 |
|------|---------|---------|
| ADD PCCACTIONPROP | PCCActionProp | 动作属性 |
| ADD REDIRECT | Redirect | 重定向目标 |
| ADD IPFARMSERVER | IPFarmServer | IPFarm 服务器池 |
| ADD USERPROFILE | UserProfile | 用户配置文件，规则容器 |
| ADD RULEBINDING | RuleBinding | Rule 绑定到 UserProfile |
| SET URRGRPBINDING | URRGroupBinding | 设置默认 URR 组 |
| SET REFRESHSRV | RefreshSrv | 刷新生效 |

### 批次 5：VPN→APN→地址池链（IP地址管理专题）

| 命令 | 配置对象 | 预期关联 |
|------|---------|---------|
| ADD VPNINST | VPNInst | VPN 实例，被 APN/POOL 引用 |
| ADD APN | APN | APN 实例 |
| ADD POOL | Pool | 地址池 |
| ADD SECTION | Section | 地址段，引用 POOL |
| ADD TACGROUP | TACGroup | TAC 组 |
| ADD CPNODEID | CPNodeId | SMF 实例 |

### 批次 6：地址池组→映射链（IP地址管理专题）

| 命令 | 配置对象 | 预期关联 |
|------|---------|---------|
| ADD POOLGROUP | PoolGroup | 地址池组 |
| ADD POOLBINDGROUP | PoolBindGroup | 地址池绑定到组 |
| ADD POOLGRPMAP | PoolGrpMap | 地址池组映射关系 |

---

## 4. 每条命令的记录模板

```markdown
### [命令名]

#### 命令概要
（一句话说明这条命令做什么、在哪个配置对象上操作）

#### 参数契约
（从 md 中提取：参数名、必选性、类型、条件依赖、默认值、枚举值）
（重点关注条件必选/条件可选的前提条件）

#### 注意事项中的约束
（逐条列出注意事项中的显性约束）

#### 规则发现
| # | 规则描述 | 类型标签 | 显性/隐性 | 原文证据 |
|---|---------|---------|----------|---------|

#### 参数引用关系
（"配置生成"模式：参数 → 引用的命令.参数）
（从 config_principle 中提取）
```

---

## 5. 工作约束

- 每批次读完后写入本文档，作为长期工作记录
- 规则类型标签不预设，每批次结束后归纳本批次发现的类型
- 每条规则必须有原文证据（evidence_text）
- 隐性规则标注 `inferred`，并说明推断依据
- 全部批次完成后做最终规则类型归纳

---

## 6. 工作进度

| 批次 | 状态 | 命令数 | 规则数 |
|------|------|--------|--------|
| 1：三四层识别→组合 | 已完成 | 4 | 18 |
| 2-4：跨命令隐式关系（过滤器→规则→动作→绑定链） | 已完成 | 14 | 11类隐式关系 |
| 5-6：IP地址管理链（VPN→APN→POOL→SECTION→POOLGROUP→POOLGRPMAP） | 已完成 | 9 | 12类隐式关系 |

---

## 7. 最终规则类型归纳

（全部批次完成后填写）

---

## 8. 批次详细记录

---

### 批次 1：三四层识别→组合链（ADD FILTER / ADD IPLIST / ADD FLOWFILTER / ADD FLTBINDFLOWF）

---

#### ADD FILTER

**命令概要**：创建三四层过滤器（Filter），定义协议类型、IP地址、端口号等匹配条件。Filter 是业务感知识别层的基础对象，被 FlowFilter 通过 FLTBINDFLOWF 绑定引用。

**适用NF**：PGW-U、UPF

**参数契约**：

| 参数 | 必选性 | 类型 | 条件依赖 | 默认值 |
|------|--------|------|----------|--------|
| FILTERNAME | 必选 | string(1~63) | - | 无 |
| L34PROTTYPE | 必选 | enum(NUMBER/STRING) | - | 无 |
| L34PROTNUM | 条件必选 | integer(0~255) | L34PROTTYPE=NUMBER | 无 |
| L34PROTOCOL | 条件必选 | enum(ANY/ICMP/TCP/UDP/GRE) | L34PROTTYPE=STRING | ANY |
| MSIPMODE | 可选 | enum(IP/IPLIST) | - | NULL |
| MSIP | 条件必选 | IPv4 | MSIPMODE=IP | 无 |
| MSIPMASKTYPE | 条件必选 | enum(IPTYPE/LENGTHTYPE) | MSIPMODE=IP | 无 |
| MSIPMASKLEN | 条件必选 | integer(0~32) | MSIPMASKTYPE=LENGTHTYPE | 无 |
| MSIPMASK | 条件必选 | IPv4(反掩码) | MSIPMASKTYPE=IPTYPE | 无 |
| MSIPLISTNAME | 条件必选 | string(1~31) | MSIPMODE=IPLIST | 无 |
| SVRIPMODE | 可选 | enum(IP/HOSTNAME/IPLIST/DOMAIN) | - | NULL |
| SVRIP | 条件必选 | IPv4 | SVRIPMODE=IP | 无 |
| SVRIPMASKTYPE | 条件必选 | enum(IPTYPE/LENGTHTYPE) | SVRIPMODE=IP | 无 |
| SVRIPLISTNAME | 条件必选 | string(1~31) | SVRIPMODE=IPLIST | 无 |
| SVRIPMASKLEN | 条件必选 | integer(0~32) | SVRIPMASKTYPE=LENGTHTYPE | 无 |
| SVRIPMASK | 条件必选 | IPv4(反掩码) | SVRIPMASKTYPE=IPTYPE | 无 |
| HOSTNAME | 条件必选 | string(1~31) | SVRIPMODE=HOSTNAME 或 DOMAIN | 无 |
| DOMAINVALUE | 条件必选 | string(1~63) | SVRIPMODE=DOMAIN | 无 |
| HOSTPRIORITY | 条件可选 | integer(1~65535) | SVRIPMODE=DOMAIN | 无 |
| MSSTARTPORT | 可选 | integer(0~65535) | - | 0 |
| MSENDPORT | 可选 | integer(0~65535) | - | 65535 |
| SVRSTARTPORT | 可选 | integer(0~65535) | - | 0 |
| SVRENDPORT | 可选 | integer(0~65535) | - | 65535 |
| TOSCFGTYPE | 可选 | enum(CLASS/TOS_VALUE) | - | 无 |
| TOSCLASSTYPE | 条件必选 | enum(BE/CS1~CS7/AF11~AF43/EF) | TOSCFGTYPE=CLASS | 无 |
| TOSVALUE | 条件必选 | integer(0~63) | TOSCFGTYPE=TOS_VALUE | 无 |
| CFGDOMAINNAME | 可选 | string(1~31) | - | 无 |

**参数引用关系**：
- MSIPLISTNAME → ADD IPLIST.IPLISTNAME（"该参数使用ADD IPLIST命令配置生成"）
- SVRIPLISTNAME → ADD IPLIST.IPLISTNAME（"该参数使用ADD IPLIST命令配置生成"）

**规则发现**：

| # | 规则描述 | 类型标签 | 显性/隐性 | 原文证据 |
|---|---------|---------|----------|---------|
| F-01 | L34PROTTYPE=NUMBER 时 L34PROTNUM 必选；L34PROTTYPE=STRING 时 L34PROTOCOL 必选。二者互斥，只能选一种协议输入方式 | param_condition | 显性 | "前提条件：该参数在L34PROTTYPE配置为NUMBER/STRING时为必选参数" |
| F-02 | MSIPMODE 决定 IP 输入分支：IP→需配MSIP+MSIPMASKTYPE→进一步分支为IPTYPE(MSIPMASK)或LENGTHTYPE(MSIPMASKLEN)；IPLIST→需配MSIPLISTNAME | param_condition_chain | 显性 | 三级条件链，从参数描述中直接提取 |
| F-03 | SVRIPMODE 有4种分支：IP→SVRIP+SVRIPMASKTYPE；HOSTNAME→HOSTNAME；IPLIST→SVRIPLISTNAME；DOMAIN→HOSTNAME+DOMAINVALUE+可选HOSTPRIORITY | param_condition_multi | 显性 | 从参数条件依赖中直接提取 |
| F-04 | L34PROTOCOL=ICMP 或 GRE 时，不允许配置端口（MSSTARTPORT/MSENDPORT/SVRSTARTPORT/SVRENDPORT） | param_exclusion | 显性 | "当L34PROTOCOL选择为ICMP或GRE时，不允许配置端口" |
| F-05 | MSIPMASK 不允许配置为 255.255.255.255，等效做法是不配IP和掩码或设掩码长度为0 | param_value_forbidden | 显性 | "反掩码不支持配置为255.255.255.255" |
| F-06 | SVRIPMASK 不允许配置为 255.255.255.255，等效做法同上 | param_value_forbidden | 显性 | 同上 |
| F-07 | Filter+FilterIPv6 总记录数最大 150000 | capacity_rule | 显性 | "Filter和FilterIPv6的总记录数最大为150000" |
| F-08 | 配置记录数>85%规格时上报告警 | capacity_alert | 显性 | "配置记录数大于规格的85%时，上报ALM-135602215" |
| F-09 | 当指定 IP列表时，系统自动展开生成多个Filter。生成数量=手机IP列表IP数×服务器IP列表IP数 | derived_object_expansion | 显性 | "生成过滤器数目=手机IP列表名称的IP数目*服务器IP列表名称的IP数目" |
| F-10 | Filter 配置后需要 SET REFRESHSRV(REFRESHTYPE=USERPROFILE或ALL) 刷新才生效 | effect_timing_delayed | 显性 | "需要等待执行SET REFRESHSRV命令刷新后生效" |
| F-11 | SVRIPMODE=DOMAIN 时，会查询Host记录，如存在则关联已有Host，否则创建新Host（60s后生效） | domain_resolution_logic | 显性 | "会基于配置的DomainValue去查询Host记录...该Host将会在命令执行后60s生效" |
| F-12 | 上行/下行方向报文匹配时，MS/SVR 的 IP 和端口的含义互换（源↔目的） | semantic_direction_dependent | 显性 | 注意事项第4-5条详细说明 |
| F-13 | 建议一个业务匹配中的过滤器数目不超过500，否则性能显著恶化 | performance_warning | 显性 | "避免一个业务能匹配中的过滤器数目过多（超过500）" |
| F-14 | TOS 配置仅适用于 ACL 功能，不适用于计费策略和动作策略 | param_scope_restriction | 显性 | "TOS配置仅适用于ACL的相关功能，不适用于计费策略和动作策略" |

---

#### ADD IPLIST

**命令概要**：创建 IP 地址列表条目。同名的多条 ADD IPLIST 命令向同一列表追加不同 IP 条目。被 ADD FILTER 的 MSIPLISTNAME / SVRIPLISTNAME 参数引用。

**适用NF**：PGW-U、UPF

**参数契约**：

| 参数 | 必选性 | 类型 | 条件依赖 | 默认值 |
|------|--------|------|----------|--------|
| IPLISTNAME | 必选 | string(1~31) | - | 无 |
| IPVERSION | 必选 | enum(IPV4/IPV6) | - | 无 |
| IPV4ADDR | 条件必选 | IPv4 | IPVERSION=IPV4 | 无 |
| IPV6ADDR | 条件必选 | IPv6 | IPVERSION=IPV6 | 无 |
| MASKVALUE | 必选 | integer(0~128) | IPv4时范围0~32，IPv6时范围0~128 | 无 |
| CFGDOMAINNAME | 可选 | string(1~31) | - | 无 |

**参数引用关系**：
- 被 ADD FILTER.MSIPLISTNAME 引用
- 被 ADD FILTER.SVRIPLISTNAME 引用

**规则发现**：

| # | 规则描述 | 类型标签 | 显性/隐性 | 原文证据 |
|---|---------|---------|----------|---------|
| IL-01 | IPVERSION=IPV4 时 IPV4ADDR 必选，MASKVALUE 范围 0~32；IPVERSION=IPV6 时 IPV6ADDR 必选，MASKVALUE 范围 0~128 | param_condition | 显性 | "前提条件：该参数在IPVERSION配置为IPV4/IPV6时为必选参数" |
| IL-02 | MASKVALUE 的有效范围受 IPVERSION 约束：IPv4→0~32，IPv6→0~128 | param_range_conditional | 显性 | "IPVERSION为IPV4时，取值范围是0~32。IPVERSION为IPV6时，取值范围是0~128" |
| IL-03 | 同一 IPLISTNAME 下的 IP 地址不能重复添加 | uniqueness_constraint | 显性 | "如果该IPList中已经存在该IP地址，则提示记录已经存在" |
| IL-04 | 系统最多支持 500 条 IPList，每个 IPList 最多 200 个 IP 地址段，总绑定关系最多 20000 条 | capacity_rule | 显性 | "系统最多支持配置500条IPList，每个IPList最多支持配置200个IP地址段" |
| IL-05 | 向 IPList 添加 IP 后，如果 IPList 已被 Filter 绑定，会自动生成 Filter，消耗 Filter 规格 | derived_object_expansion | 显性 | "IPList如果被绑定到Filter中，系统会自动生成Filter" |
| IL-06 | IPLIST 配置后需要 SET REFRESHSRV 生效 | effect_timing_delayed | 显性 | "需要执行SET REFRESHSRV使当前配置生效" |
| IL-07 | MASKVALUE 配置过小会导致 IP 匹配范围变大，影响规则匹配 | performance_warning | 显性 | "MASKVALUE参数配置过小会导致ip匹配范围变大" |

---

#### ADD FLOWFILTER

**命令概要**：创建流过滤器（FlowFilter），作为组合容器。通过 ADD FLTBINDFLOWF 绑定三四层 Filter，通过 ADD PROTBINDFLOWF 绑定七层协议+过滤器。FlowFilter 是 Rule 的直接匹配条件。

**适用NF**：PGW-U、UPF

**参数契约**：

| 参数 | 必选性 | 类型 | 条件依赖 | 默认值 |
|------|--------|------|----------|--------|
| FLOWFILTERNAME | 必选 | string(1~63) | - | 无 |
| TETHERDETFLAG | 可选 | enum(NONE/DETECT_ONLY/FILTER/NOT_FILTER) | - | 无 |
| FLOWFILTERTYPE | 可选 | enum(USERCONFIG/EXTEROTTDB) | - | USERCONFIG |
| FILTERGRPNAME | 条件可选 | string(1~63) | FLOWFILTERTYPE=USERCONFIG | 无 |
| CFGDOMAINNAME | 可选 | string(1~31) | - | 无 |

**规则发现**：

| # | 规则描述 | 类型标签 | 显性/隐性 | 原文证据 |
|---|---------|---------|----------|---------|
| FF-01 | 最大记录数 100000，>90%规格上报告警 | capacity_rule | 显性 | "该命令最大记录数为100000" |
| FF-02 | FLOWFILTERTYPE=EXTEROTTDB 时，不允许修改属性，只允许删除该 FlowFilter | object_immutability | 显性 | "当指定该流过滤器属性为外置规则库定义，则不允许修改该属性，只允许删除该流过滤器" |
| FF-03 | 外置规则库定义的 FlowFilter 与 Filter 和 L7Filter 不共存 | object_exclusion | 显性 | "外置规则库定义属性的流过滤器同过滤器和七层过滤器不共存" |
| FF-04 | 同一个 FlowFilterGroup 内不允许绑定不同 FLOWFILTERTYPE 的 FlowFilter | consistency_rule | 显性 | "同一个流过滤器组不允许绑定外置规则库定义属性不同的流过滤器" |
| FF-05 | Rule、Filter、FlowFilter、UserProfile、URRGrpBinding 在特定组合下需要兜底配置，否则影响计费准确性 | cross_object_dependency | 显性 | "Rule、Filter、Flowfilter、Userprofile和URRGrpBinding相关配置在特定组合下需要兜底配置" |

---

#### ADD FLTBINDFLOWF

**命令概要**：将三四层过滤器（Filter）绑定到流过滤器（FlowFilter）。绑定后，匹配该 Filter 条件的报文可通过 FlowFilter 进入后续规则匹配。

**适用NF**：PGW-U、UPF

**参数契约**：

| 参数 | 必选性 | 类型 | 条件依赖 | 默认值 |
|------|--------|------|----------|--------|
| FLOWFILTERNAME | 必选 | string(1~63) | - | 无 |
| FILTERNAME | 必选 | string(1~63) | - | 无 |

**参数引用关系**：
- FLOWFILTERNAME → ADD FLOWFILTER.FLOWFILTERNAME（"该参数使用ADD FLOWFILTER命令配置生成"）
- FILTERNAME → ADD FILTER.FILTERNAME 或 ADD FILTERIPV6.FILTERNAME（"该参数使用ADD FILTER或者ADD FILTERIPV6命令配置生成"）

**规则发现**：

| # | 规则描述 | 类型标签 | 显性/隐性 | 原文证据 |
|---|---------|---------|----------|---------|
| BF-01 | 单个 FlowFilter 可以配置 Filter 和 FilterIPv6 总数为 5000 个 | capacity_rule | 显性 | "单个FlowFilter可以配置Filter和FilterIPv6总数为5000个" |
| BF-02 | 最大记录数 300000，>90%规格上报告警 | capacity_rule | 显性 | "该命令最大记录数为300000" |
| BF-03 | 绑定操作会导致用户匹配范围变化，可能影响性能 | performance_warning | 显性 | "该命令会导致用户匹配范围发生变化，可能导致性能下降" |
| BF-04 | 配置后需要 SET REFRESHSRV 刷新才对新数据流生效 | effect_timing_delayed | 显性 | "需要等待执行SET REFRESHSRV命令刷新后对新数据流生效" |
| BF-05（隐性） | FLOWFILTERNAME 和 FILTERNAME 都必须是已存在的配置对象实例。在执行 ADD FLTBINDFLOWF 前，ADD FLOWFILTER 和 ADD FILTER 必须已完成 | object_existence_prerequisite | 隐性(inferred) | 从"配置生成"表述和命令语义推断：绑定的两端都必须是已创建的对象 |

---

### 批次 1 规则类型归纳

从批次 1 的 4 条命令中发现了以下规则类型：

| 规则类型 | 说明 | 出现次数 |
|---------|------|---------|
| **param_condition** | 参数条件必选/可选：A=X 时 B 必选 | 4次（F-01, F-02, F-03, IL-01） |
| **param_condition_chain** | 多级条件链：A→B→C 三层分支 | 2次（F-02, F-03） |
| **param_exclusion** | 参数互斥：A=X 时不能配置 B | 1次（F-04） |
| **param_value_forbidden** | 参数值禁止：某参数不能取特定值 | 2次（F-05, F-06） |
| **param_range_conditional** | 参数取值范围受其他参数约束 | 1次（IL-02） |
| **param_scope_restriction** | 参数只在特定功能场景下有效 | 1次（F-14） |
| **capacity_rule** | 最大记录数/数量规格限制 | 4次（F-07, IL-04, FF-01, BF-02） |
| **capacity_alert** | 配置数量超阈值告警 | 1次（F-08） |
| **derived_object_expansion** | 配置一个对象自动衍生出多个对象，消耗系统规格 | 2次（F-09, IL-05） |
| **effect_timing_delayed** | 配置后需要额外操作才生效（SET REFRESHSRV） | 3次（F-10, IL-06, BF-04） |
| **performance_warning** | 性能风险提示（不是错误，但是警告） | 3次（F-13, IL-07, BF-03） |
| **uniqueness_constraint** | 同一集合内不能重复 | 1次（IL-03） |
| **object_existence_prerequisite** | 引用的对象必须已存在（隐性） | 1次（BF-05） |
| **object_immutability** | 某些对象创建后不可修改，只能删除 | 1次（FF-02） |
| **object_exclusion** | 不同类型的对象不能共存 | 1次（FF-03） |
| **consistency_rule** | 跨对象属性一致性 | 1次（FF-04） |
| **cross_object_dependency** | 多个对象特定组合下需要兜底配置 | 1次（FF-05） |
| **domain_resolution_logic** | 域名解析逻辑：先查已有Host，不存在则创建 | 1次（F-11） |
| **semantic_direction_dependent** | 参数语义取决于使用方向（上行/下行） | 1次（F-12） |

---

## 9. 跨命令隐式关系分析（核心价值）

> 以下规则均无法从单条命令文档中发现，必须同时阅读多条相关命令才能推导。
> 分析方法：将完整业务链的所有命令同时读取，从配置核查工程师的视角审视。

### 9.0 分析范围

本次分析覆盖业务感知完整链路，已读命令：

| 层级 | 命令 | 配置对象 |
|------|------|---------|
| 三四层匹配 | ADD FILTER, ADD IPLIST, ADD FILTERIPV6 | Filter, IPList |
| 七层匹配 | ADD L7FILTER | L7Filter |
| 扩展匹配 | ADD EXTENDEDFILTER | ExtendedFilter |
| 流过滤器容器 | ADD FLOWFILTER | FlowFilter |
| 三四层绑定 | ADD FLTBINDFLOWF | FltBindFlowF |
| 七层绑定 | ADD PROTBINDFLOWF | ProtBindFlowF |
| 流过滤器组 | ADD FLOWFILTERGRP | FlowFilterGroup |
| 全局过滤 | SET GLBEXTFILTER | GlbExtFilter |
| 规则 | ADD RULE | Rule |
| 动作属性 | ADD PCCACTIONPROP | PCCActionProp |
| 重定向 | ADD REDIRECT | Redirect |
| 用户模板 | ADD USERPROFILE | UserProfile |
| 规则绑定 | ADD RULEBINDING | RuleBinding |
| 刷新 | SET REFRESHSRV | RefreshSrv |

### 9.1 完整匹配语义链（match_semantics_chain）

**描述**：从用户到动作的完整匹配路径不在任何单一命令文档中描述，必须组装所有命令信息才能理解。

```
用户上线 → SMF下发 USERPROFILE
  → 该 UP 下绑定的所有 RULE（via RULEBINDING）
    → 每个 RULE 指定 FLOWFILTER 或 FLOWFILTERGRP 作为匹配条件
      → FLOWFILTER：
        ├─ FLTBINDFLOWF 绑定的 Filter（三四层匹配）
        │   └─ Filter 引用 IPLIST（IP地址集合）
        └─ PROTBINDFLOWF 绑定的 Protocol + L7Filter（七层匹配）
      → FLOWFILTERGRP：
        └─ 多个 FLOWFILTER 的 AND/OR/NOT 逻辑组合
    → 匹配成功后执行 RULE 的 POLICYTYPE 对应的策略动作
```

**匹配优先级规则**：同一 POLICYTYPE 的多个 RULE 匹配成功时，按 PRIORITY 选一个执行。不同 POLICYTYPE 独立匹配，可同时生效。

**核查场景**：验证一个 UserProfile 下所有绑定的 Rule 是否能正确匹配到预期的业务流。

**补充发现：PCC 策略链有隐藏的中间层**

```
RULE(PCC, POLICYNAME=X) 不是直接引用 PCCACTIONPROP，
而是引用 PCCPOLICYGRP(X)，PCCPOLICYGRP 内部再引用：
  → PCCACTIONPROP（门控+重定向，默认组合）
  → URRGROUP（计费规则）
  → QOSPROP（QoS 属性）
  → EXTENDPROP（扩展属性）
  → 最多 11 个组合（1 个默认 + 10 个按 ServiceProp 区分的非默认组合）

RULE(WEBPROXY, POLICYNAME=Y) 引用 IPFarm(Y)
  IPFarm 内部有多个 IPFARMSERVER（服务器池）

RULE(SMARTREDIRECT, POLICYNAME=Z) 引用 IPFarm(Z) 或 REDIRECT(Z)
```

这意味着：PCC 类型 RULE 的完整策略链是 RULE→PCCPOLICYGRP→(PCCACTIONPROP+URRGROUP+QOSPROP+EXTENDPROP)，比其他 POLICYTYPE 多了一层间接引用。PCCPOLICYGRP 支持 ServiceProp 匹配选择不同的策略组合，增加了匹配维度。

**与业务图谱的交叉验证**：业务图谱定义了 ConfigObject 链 Filter→L7Filter→FlowFilter→Rule→PCCActionProp→UserProfile→RuleBinding。实际命令链条验证：Filter→(FLTBINDFLOWF)→FlowFilter，L7Filter→(PROTBINDFLOWF)→FlowFilter，Rule→(PCCPOLICYGRP)→PCCActionProp，Rule→(RULEBINDING)→UserProfile。业务图谱漏掉了 PCCPOLICYGRP 这个中间层。

### 9.2 策略类型平行宇宙（policy_type_parallel_universes）

**描述**：ADD RULE 有 14 种 POLICYTYPE（PCC, BWM, HEADEN, WEBPROXY, IPREDIR, SMARTREDIRECT, REMARK_FPI, SRV_TRIGGER, FIREWALL, ADC, QOS, WORKER, TRAFFICCLASS, LBO），每种是独立的匹配维度。

**隐式规则**：

| # | 规则 | 证据来源 |
|---|------|---------|
| PT-01 | 同一 POLICYTYPE 内，多个 Rule 按优先级选取一个执行 | ADD RULE 注意事项 |
| PT-02 | 不同 POLICYTYPE 可同时匹配生效，互不干扰 | ADD RULE 注意事项 |
| PT-03 | PCC 和 QOS 类型不能使用相同的 RULENAME | ADD RULE 注意事项 |
| PT-04 | ADD RULE 和 ADD BLACKLISTRULE 共享 (RULENAME, POLICYTYPE) 命名空间 | ADD RULE 注意事项 |
| PT-05 | RULEBINDING 不指定 POLICYTYPE 时，将同名不同类型的 Rule 全部绑定 | ADD RULEBINDING 参数说明 |

**核查场景**：
- 检查同 UP 同 POLICYTYPE 下 RULE 的 PRIORITY 是否唯一（避免重启后优先级不确定）
- 检查 PCC 和 QOS 类型无同名 RULENAME
- 检查 RULEBINDING 绑定时是否误绑了不需要的 POLICYTYPE

### 9.3 策略类型约束七层绑定（policy_type_l7filter_exclusion）

**描述**：某些 POLICYTYPE 不允许使用七层协议绑定，这是一个跨三层命令的隐式约束。

**证据链**：
- ADD RULE 说："当策略类型为WEBPROXY、IPREDIR、SRV_TRIGGER或LBO时，不允许配置绑定了七层协议和协议组的流过滤器"
- ADD PROTBINDFLOWF 创建了 FlowFilter 的七层协议绑定
- ADD FLTBINDFLOWF 创建了三四层绑定

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| PL7-01 | POLICYTYPE=WEBPROXY/IPREDIR/SRV_TRIGGER/LBO 的 RULE，引用的 FLOWFILTER 不能有 PROTBINDFLOWF 绑定 | RULE + PROTBINDFLOWF |
| PL7-02 | 上述 POLICYTYPE 的 RULE，引用的 FLOWFILTERGRP 中不能包含有七层绑定的 FLOWFILTER | RULE + FLOWFILTERGRP + PROTBINDFLOWF |
| PL7-03 | L7FILTER 的 METHODTYPE/ISREFEREREN 仅对 http/connection-wap1.x/connectionless-wap1.x 协议生效，其余协议不参与匹配 | L7FILTER + PROTBINDFLOWF |
| PL7-04 | L7FILTER 的 USERAGENT 仅对 http/connection-wap1.x/connectionless-wap1.x 协议生效，其余协议配置了也无法命中 | L7FILTER + PROTBINDFLOWF |
| PL7-05 | L7FILTER 的 XHEADERNAME 仅对 http 协议生效，其余协议配置了也无法命中 | L7FILTER + PROTBINDFLOWF |

**核查场景**：
- 对每个 RULE(POLICYTYPE=WEBPROXY)，检查其 FLOWFILTER 是否有 PROTBINDFLOWF 记录
- 对每个 PROTBINDFLOWF(protocol≠http) 检查对应 L7FILTER 是否配置了 METHODTYPE/USERAGENT 等无效参数

### 9.4 规格类型兼容链（spec_type_compatibility）

**描述**：RULE.RULESPECTYPE 和 USERPROFILE.UPSPECTYPE 必须匹配才能绑定，跨越三条命令。

**证据链**：
- ADD RULE: "DEFAULT类型的UserProfile只能绑定DEFAULT类型的Rule。SPECIFICATION_LIMITED类型的UserProfile只能绑定SPECIFICATION_LIMITED类型的Rule。"
- ADD USERPROFILE: 同样的描述
- ADD RULEBINDING: 同样的描述

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| ST-01 | RULE(RULESPECTYPE=DEFAULT) 只能通过 RULEBINDING 绑定到 USERPROFILE(UPSPECTYPE=DEFAULT) | RULE + USERPROFILE + RULEBINDING |
| ST-02 | RULE(RULESPECTYPE=SPECIFICATION_LIMITED) 只能绑定到 USERPROFILE(UPSPECTYPE=SPECIFICATION_LIMITED) | RULE + USERPROFILE + RULEBINDING |
| ST-03 | DEFAULT 类型 UP 最多绑 8000 个 Rule；SPECIFICATION_LIMITED 类型 UP 最多绑 100 个 | RULEBINDING 注意事项 |

**核查场景**：检查每个 RULEBINDING 记录，验证 RULE 的 RULESPECTYPE 与 USERPROFILE 的 UPSPECTYPE 一致。

### 9.5 生效时机层级不一致（effect_timing_chain_inconsistency）

**描述**：同一业务链中不同层级对象的生效机制不同，运维容易遗漏。

**跨命令汇总**：

| 对象 | 生效方式 | 来源命令 |
|------|---------|---------|
| Filter / FilterIPv6 | **需手动 SET REFRESHSRV** | SET REFRESHSRV |
| FilterGroup | **需手动 SET REFRESHSRV** | SET REFRESHSRV |
| FLTBINDFLOWF | 需 SET REFRESHSRV | FLTBINDFLOWF |
| L7FILTER | **60s 自动生效** | ADD L7FILTER |
| PROTBINDFLOWF | **60s 自动生效** | ADD PROTBINDFLOWF |
| EXTENDEDFILTER | **60s 自动生效** | ADD EXTENDEDFILTER |
| FLOWFILTER | 立即生效（未明确延迟） | - |
| FLOWFILTERGRP | **只对新激活用户生效** | ADD FLOWFILTERGRP |
| RULE | **立即生效** | ADD RULE |
| PCCACTIONPROP | **立即生效** | ADD PCCACTIONPROP |
| REDIRECT | **立即生效** | ADD REDIRECT |
| USERPROFILE | **立即生效** | ADD USERPROFILE |
| RULEBINDING | **只对新激活用户生效** | ADD RULEBINDING |
| SET GLBEXTFILTER | **立即生效** | SET GLBEXTFILTER |
| SET REFRESHSRV | **立即生效**（但 ACL 30s 后才生效） | SET REFRESHSRV |

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| ET-01 | 修改 Filter 后必须 SET REFRESHSRV，但 L7FILTER 修改只需等 60s | FILTER + L7FILTER + REFRESHSRV |
| ET-02 | SET REFRESHSRV 只管 Filter/FilterGroup/Acl/AclNode 的刷新，不管 L7FILTER/PROTBINDFLOWF/FLOWFILTERGRP | REFRESHSRV + L7FILTER + PROTBINDFLOWF |
| ET-03 | FLOWFILTERGRP 和 RULEBINDING 修改后，已在线用户需最长 1 小时才生效 | FLOWFILTERGRP + RULEBINDING |
| ET-04 | SET REFRESHSRV 执行后 30 秒内不允许修改 Filter 和被绑定的 IPList | REFRESHSRV |
| ET-05 | l7filter 被 https 协议绑定后，需要 60s 才生效（比普通 60s 更严格？） | L7FILTER 注意事项 |

**核查场景**：
- 检查配置变更脚本中，FILTER 变更后是否紧跟着 SET REFRESHSRV
- 检查变更时间窗口：如果改了 FLOWFILTERGRP + RULEBINDING，已在线用户的生效是否可接受
- 检查 SET REFRESHSRV 之后 30s 内是否有 FILTER 修改操作

### 9.6 空容器与悬空引用（dangling_reference_and_empty_container）

**描述**：跨命令引用关系中两类常见错误——被引用对象被删除但引用未清除（悬空引用），以及容器对象创建后未绑定任何子对象（空容器）。

**跨命令引用网络**：

```
FLOWFILTERGRP.FLOWFILTERNAME ←→ ADD FLOWFILTER.FLOWFILTERNAME
PROTBINDFLOWF.FLOWFILTERNAME ←→ ADD FLOWFILTER.FLOWFILTERNAME
FLTBINDFLOWF.FLOWFILTERNAME ←→ ADD FLOWFILTER.FLOWFILTERNAME
FLTBINDFLOWF.FILTERNAME ←→ ADD FILTER.FILTERNAME / ADD FILTERIPV6.FILTERNAME
PROTBINDFLOWF.L7FILTERNAME ←→ ADD L7FILTER.L7FILTERNAME
RULE.FLOWFILTERNAME ←→ ADD FLOWFILTER.FLOWFILTERNAME
RULE.FLWFLTRGRPNAME ←→ ADD FLOWFILTERGRP.FLWFLTRGRPNAME
RULE.POLICYNAME ←→ 根据 POLICYTYPE 不同引用不同对象
RULEBINDING.RULENAME ←→ ADD RULE.RULENAME
RULEBINDING.USERPROFILENAME ←→ ADD USERPROFILE.USERPROFILENAME
PCCACTIONPROP.UPINITREDIRNM ←→ ADD REDIRECT.REDIRECTNAME
PCCACTIONPROP.DNINITREDIRNM ←→ ADD REDIRECT.REDIRECTNAME
SET GLBEXTFILTER.EXTFLTNAME1~5 ←→ ADD EXTENDEDFILTER.EXTFLTNAME
```

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| DR-01 | 删除被引用对象（如 RMV FILTER）后，FLTBINDFLOWF 中的绑定关系不会自动清除，产生悬空引用 | FLTBINDFLOWF + RMV FILTER |
| DR-02 | FLOWFILTER 既没有 FLTBINDFLOWF 也没有 PROTBINDFLOWF 绑定时，是空容器，永远不会匹配 | FLOWFILTER + FLTBINDFLOWF + PROTBINDFLOWF |
| DR-03 | FLOWFILTERGRP 引用了空 FLOWFILTER 时，该 FlowFilter 在匹配时行为不确定（可能全匹配也可能不匹配，取决于逻辑分组） | FLOWFILTERGRP + FLOWFILTER |
| DR-04 | SET GLBEXTFILTER 配置的 EXTFLTNAME 如果被 RMV EXTENDEDFILTER 删除，全局过滤条件异常 | GLBEXTFILTER + EXTENDEDFILTER |
| DR-05 | 所有引用关系的名称匹配是不区分大小写的，但名称长度在创建和引用端必须兼容 | 所有命令 |

**核查场景**：
- 对所有绑定关系表（FLTBINDFLOWF、PROTBINDFLOWF、RULEBINDING 等），验证被引用对象存在
- 对所有 FLOWFILTER，检查是否至少有一个绑定（FLTBINDFLOWF 或 PROTBINDFLOWF）
- 对所有 FLOWFILTERGRP，检查引用的 FLOWFILTER 是否为空容器

### 9.7 重定向双入口过滤（dual_level_redirect_filtering）

**描述**：重定向动作有双重过滤机制，这一关系跨越 SET GLBEXTFILTER + ADD REDIRECT + ADD PCCACTIONPROP + ADD RULE 四条命令。

**证据链**：
- SET GLBEXTFILTER：控制全局重定向过滤条件，"绑定重定向动作过滤条件，只有符合扩展过滤器的条件，才能执行重定向动作"
- ADD RULE(POLICYTYPE=PCC) → PCCACTIONPROP → UPINITREDIRNM/DNINITREDIRNM → REDIRECT
- ADD RULE(POLICYTYPE=SMARTREDIRECT) → POLICYNAME → IPFarm/REDIRECT
- SET GLBEXTFILTER 默认全 NULL = 所有流量都执行重定向

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| DL-01 | 有重定向 RULE 但无 GLBEXTFILTER 配置时，所有匹配 RULE 的流量都会被重定向（默认全匹配） | RULE + GLBEXTFILTER |
| DL-02 | 有 GLBEXTFILTER 配置但无重定向 RULE 时，GLBEXTFILTER 无意义 | GLBEXTFILTER + RULE |
| DL-03 | GLBEXTFILTER 最多 3 个 AND 类型，总共 5 个扩展过滤器 | GLBEXTFILTER 注意事项 |
| DL-04 | ADC 类型 RULE 的 REPLACEUPNAME 引用的 USERPROFILE 不应包含当前 RULE 的绑定 | RULE + RULEBINDING + USERPROFILE |

**核查场景**：
- 检查是否存在重定向 RULE 但没有配置 GLBEXTFILTER（可能是预期行为，但应提示）
- 检查 ADC RULE 的 REPLACEUPNAME 是否形成循环切换链

### 9.8 ADC 用户模板切换链（adc_userprofile_switch_chain）

**描述**：ADC 类型 RULE 的 REPLACEUPNAME 可以触发用户模板切换，产生隐式的循环风险。

**证据链**：
- ADD RULE：REPLACEUPNAME "使用ADD USERPROFILE命令配置生成"，"不应将此规则绑定到ReplaceUpName对应的userprofile下"
- ADD RULE："同一用户命中ADC类型...最多切换10次。同一用户切换过用户模板后，会忽略后续SMF下发的用户模板。"

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| ADC-01 | ADC RULE 不能绑定到 REPLACEUPNAME 对应的 USERPROFILE 下（显式约束，但跨 3 条命令） | RULE + RULEBINDING + USERPROFILE |
| ADC-02 | 如果存在切换链 UP_A→UP_B→UP_A，会无限循环直到 10 次上限，之后忽略 SMF 下发 | RULE + USERPROFILE |
| ADC-03 | 切换后用户会忽略后续 SMF 下发的用户模板，可能影响正常业务 | RULE 注意事项 |

**核查场景**：构建所有 ADC RULE 的切换图 (USERPROFILE → REPLACEUPNAME)，检测是否存在环路。

### 9.9 PCC 动作属性方向一致性（pcc_direction_consistency）

**描述**：PCCACTIONPROP 的上下行门控配置不一致可能导致业务不通。

**证据**：ADD PCCACTIONPROP 注意事项："报文动作需要上下行都配置且保持一致，配置不一致可能导致业务不通。"

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| PCC-01 | UPINITUPGATE 应与 DNINITUPGATE 一致（除非有意设计上下行不同行为） | PCCACTIONPROP |
| PCC-02 | UPINITDNGATE 应与 DNINITDNGATE 一致 | PCCACTIONPROP |
| PCC-03 | 如果配置了 UPINITREDIRNM，应同时考虑 DNINITREDIRNM | PCCACTIONPROP |

### 9.10 配置完整性兜底规则（configuration_completeness_fallback）

**描述**：多条命令都提到"兜底配置"但从未明确定义什么是兜底配置。

**证据**：
- ADD RULE："Rule、Filter、Flowfilter、Userprofile和URRGrpBinding相关配置在特定组合下需要兜底配置，否则可能会影响计费准确性。"
- ADD USERPROFILE："Rule、filter、flowfilter和缺省URR相关配置在特定组合下需要兜底配置，当前没有检查手段，影响计费准确性"

**隐式规则**：这是一个系统级的隐式规则，虽然没有明确定义"特定组合"和"兜底配置"的内容，但它暗示了 RULE + FILTER + FLOWFILTER + USERPROFILE + URRGRPBINDING 之间存在一个未文档化的完整性约束。

**核查场景**：这需要在实际配置核查中通过经验和案例积累来完善，属于第二阶段的深度核查规则。

### 9.11 隐式关系类型归纳

| 隐式关系类型 | 说明 | 发现条目 |
|-------------|------|---------|
| **match_semantics_chain** | 完整匹配语义链（跨 6 层对象） | 9.1 |
| **policy_type_parallel_universes** | 策略类型是独立匹配维度 | 9.2 |
| **policy_type_l7filter_exclusion** | 某些策略类型禁止七层绑定 | 9.3 |
| **spec_type_compatibility** | 规格类型跨命令兼容 | 9.4 |
| **effect_timing_chain_inconsistency** | 生效机制跨层级不一致 | 9.5 |
| **dangling_reference** | 悬空引用检测 | 9.6 |
| **empty_container** | 空容器检测 | 9.6 |
| **dual_level_redirect_filtering** | 重定向双入口过滤 | 9.7 |
| **adc_userprofile_switch_chain** | ADC 用户模板切换链/环检测 | 9.8 |
| **pcc_direction_consistency** | PCC 上下行方向一致性 | 9.9 |
| **configuration_completeness_fallback** | 未文档化的兜底配置完整性 | 9.10 |
| **cfgdomain_partitioning** | 配置域分区机制与跨域引用限制 | 9.12 |
| **ipfarm_reference_chain** | IPFarm 跨命令引用链（WEBPROXY/SMARTREDIRECT） | 9.13 |
| **pccpolicygrp_multi_combination** | PCC 策略组多组合匹配机制 | 9.14 |

### 9.12 配置域分区机制（cfgdomain_partitioning）

**描述**：多条命令都有 CFGDOMAINNAME 参数，这是一个跨命令的对象分区机制。不同配置域的对象可能互不可见或存在引用限制。

**证据**：以下命令都有 CFGDOMAINNAME 参数：
- ADD FILTER, ADD FLOWFILTER, ADD FLTBINDFLOWF, ADD PROTBINDFLOWF
- ADD FLOWFILTERGRP, ADD L7FILTER, ADD EXTENDEDFILTER
- ADD RULE, ADD PCCACTIONPROP, ADD PCCPOLICYGRP, ADD REDIRECT
- ADD USERPROFILE, ADD RULEBINDING

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| CD-01 | RULE 的 CFGDOMAINNAME 应与引用的 FLOWFILTER/FLOWFILTERGRP 的 CFGDOMAINNAME 一致，否则可能跨域引用失败 | RULE + FLOWFILTER |
| CD-02 | PCCPOLICYGRP 引用的 PCCACTIONPROP/URRGROUP/QOSPROP 应在同一配置域内 | PCCPOLICYGRP + PCCACTIONPROP |
| CD-03 | RULEBINDING 的 USERPROFILE 和 RULE 是否需要同域？（需验证） | RULEBINDING + USERPROFILE + RULE |

**核查场景**：检查跨域引用是否被系统允许，如果不允许则需检测所有引用关系中 CFGDOMAINNAME 的一致性。

### 9.13 IPFarm 跨命令引用链（ipfarm_reference_chain）

**描述**：IPFarm 被 WEBPROXY 和 SMARTREDIRECT 两种策略类型引用，但 IPFarm 自身还有 IPFARMSERVER 子对象。

**证据链**：
- ADD RULE(POLICYTYPE=WEBPROXY) → POLICYNAME = IPFarm名称
- ADD RULE(POLICYTYPE=SMARTREDIRECT) → POLICYNAME = IPFarm名称（CaptivePortal场景）
- ADD IPFARM 创建 IPFarm，ADD IPFARMSERVER 在 IPFarm 下添加服务器
- IPFARMSERVER 有 DEFAULTACT(BLOCK/PASS) 参数，仅对 CaptivePortal 生效

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| IF-01 | RULE(WEBPROXY) 引用的 IPFarm 必须至少有一个 IPFARMSERVER | RULE + IPFARM + IPFARMSERVER |
| IF-02 | IPFARMSERVER 的 IPVERSION 必须与 IPFarm 的虚拟 IP 类型一致 | IPFARMSERVER 注意事项 |
| IF-03 | IPFarm 用于 P-CSCF 检测时，IPFARMSERVER 地址需要与 SMF 的 PCSCFIP 地址一致（跨网元一致性） | IPFARMSERVER 注意事项 |
| IF-04 | IPFARMSERVER 的 URL 如果缺省，则使用 IP 地址作为 URL | IPFARMSERVER 注意事项 |
| IF-05 | RULE(SMARTREDIRECT) 的 POLICYNAME 可能是 IPFarm 名称或 REDIRECT 名称，两种引用路径不同 | RULE + IPFARM + REDIRECT |

**核查场景**：
- 检查所有 RULE(WEBPROXY/SMARTREDIRECT) 引用的 POLICYNAME 是否对应有效的 IPFarm（有 IPFARMSERVER）
- 检查 IPFARM 下是否有空的 IPFARMSERVER（无服务器不可用）

### 9.14 PCCPOLICYGRP 多组合匹配（pccpolicygrp_multi_combination）

**描述**：PCCPOLICYGRP 支持基于 ServiceProp 选择不同策略组合，增加了核查复杂度。

**证据**：ADD PCCPOLICYGRP 注意事项：
- "PccPolicyGrp中最多可以配置十一个组合。一个默认组合，十个非默认组合"
- "非默认组合以ServiceProp作为组合的标识，通过ADD SRVPBINDPCCPG添加"
- "如果PccPolicyGrp配置了多种组合，则匹配优先级取决于SrvPBindPccPG下配置的ServiceProp优先级。默认组合的优先级最低"

**隐式规则**：

| # | 规则 | 涉及命令 |
|---|------|---------|
| PC-01 | PCCPOLICYGRP 可以只有默认组合（无 PCCACTIONPROP/URRGROUP/QOSPROP），此时策略为空 | PCCPOLICYGRP |
| PC-02 | 非默认组合需要额外的 ADD SRVPBINDPCCPG 命令创建，这意味着 PCC 策略链可能涉及更多命令 | PCCPOLICYGRP + SRVPBINDPCCPG |
| PC-03 | 被绑定的 PCCPOLICYGRP 不允许删除（跨 RULE 的引用保护） | PCCPOLICYGRP 注意事项 |
| PC-04 | PCCPOLICYGRP 内 PCCACTIONPROP 引用的 REDIRECT，与 SET GLBEXTFILTER 构成双重过滤 | PCCPOLICYGRP + PCCACTIONPROP + REDIRECT + GLBEXTFILTER |

**核查场景**：
- 检查 PCCPOLICYGRP 是否至少配置了一个有意义的策略组件（PCCACTIONPROP 或 URRGROUP）
- 检查 PCCPOLICYGRP 被引用但所有组合都是空策略的情况

---

## 10. IP 地址管理链跨命令隐式关系分析

### 10.1 VPN 级联一致性（vpn_cascade_consistency）

**描述**：IP 地址管理链的核心对象都绑定到 VPN 实例，形成一条 VPN 一致性级联链。从 VPNINST 出发，APN、POOL、SECTION 逐层引用 VPN，任何一层 VPN 不一致都会导致地址分配或路由异常。

**级联链**：
```
VPNINST (创建 VPN)
  └→ APN (HASVPN=ENABLE 时 VPNINSTNAME 必选)
       └→ POOL (VPNINSTNAME 必选，必须与 APN 的 VPN 一致)
            └→ SECTION (继承 POOL 的 VPN 作用域)
```

**证据**：
- ADD APN：HASVPN=ENABLE 时 VPNINSTNAME 为条件必选
- ADD POOL：VPNINSTNAME 为必选参数，注意事项写明"POOL 的 VPN 必须和 APN 的 VPN 一致"
- ADD SECTION：不直接指定 VPN，但地址重叠检测以 VPN 为作用域

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| VPN-01 | APN 的 HASVPN=ENABLE 但未配置 VPNINSTNAME → 地址分配失败 | ADD APN | 显性（注意事项） |
| VPN-02 | POOL 的 VPNINSTNAME 与关联 APN 的 VPNINSTNAME 不一致 → 地址路由不可达 | ADD POOL + ADD APN | 显性（注意事项） |
| VPN-03 | POOL 绑定了 SECTION 后，不允许修改 POOL 的 VPNINSTNAME | ADD POOL 注意事项 | 显性 |
| VPN-04 | POOL 已绑定到 POOLGROUP（通过 POOLBINDGROUP），不允许修改 POOL 的 VPNINSTNAME | ADD POOL + ADD POOLBINDGROUP | 隐性（推理：VPN变更会破坏组内一致性） |
| VPN-05 | SECTION 地址重叠检测的作用域是同一 VPN 内（非同一 POOL） | ADD SECTION + ADD POOL | 隐性（从地址空间语义推断） |

### 10.2 VPN 跨网元一致性（vpn_cross_ne_consistency）

**描述**：UDG 侧创建的 VPNINST 必须与 VNRS 平台的 L3VPNINST 保持一致。这是跨网元的隐式约束。

**证据**：
- ADD VPNINST 注意事项："VPN 实例需要通过 ADD L3VPNINST 命令在 VNRS 平台同步配置"
- "如果 UDG 侧存在 VPN 实例但 VNRS 侧不存在，会导致路由不可达"

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| VPN-XNE-01 | UDG 的每个 VPNINST 必须在 VNRS 有对应的 L3VPNINST | ADD VPNINST（跨网元） | 显性（注意事项） |
| VPN-XNE-02 | VPNINST 删除前需先删除 VNRS 侧的 L3VPNINST（或确认无引用） | ADD VPNINST（跨网元） | 隐性（推理：删除顺序） |

**核查场景**：比对 UDG VPNINST 列表与 VNRS L3VPNINST 列表，找出只在单侧存在的 VPN。

### 10.3 地址段重叠检测作用域（address_overlap_scope）

**描述**：SECTION 的 IP 地址重叠检测不是以 POOL 为作用域，而是以 VPN 为作用域。同一 VPN 内不同 POOL 的 SECTION 地址也不允许重叠。

**证据**：
- ADD SECTION 注意事项："地址段不能与同一 VPN 实例下的其他地址段重叠"
- ADD SECTION 有 STARTIP 和 ENDIP 参数，但没有独立的 VPN 参数——VPN 继承自 POOL

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| AO-01 | 同一 VPN 内任意两个 SECTION 的 [STARTIP, ENDIP] 区间不能重叠 | ADD SECTION + ADD POOL + ADD VPNINST | 显性（注意事项） |
| AO-02 | IPv4 和 IPv6 的重叠检测是独立的（不同地址族） | ADD SECTION | 隐性（从地址空间语义推断） |
| AO-03 | MASK 不同的 SECTION 即使地址范围相同也不算重叠（CIDR 语义） | ADD SECTION | 隐性（需验证系统行为） |

### 10.4 地址池类型约束（pool_type_constraints）

**描述**：POOL 有三种类型（LOCAL/EXTERNAL/MULTICAST），不同类型的 POOL 在后续使用中受到不同约束。

**证据**：
- ADD POOL：POOLTYPE 枚举值 LOCAL/EXTERNAL/MULTICAST
- ADD POOL 注意事项：EXTERNAL 类型的地址池"仅当该地址池绑定的地址池组通过 POOLGRPMAP 关联到 APN 时生效"
- ADD SECTION：每个 POOL 最多 64 个 SECTION

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| PT-01 | EXTERNAL 类型的 POOL 如果没有通过 POOLGRPMAP→APN 关联，则不会生效 | ADD POOL + ADD POOLGRPMAP + ADD APN | 显性（注意事项） |
| PT-02 | LOCAL 类型的 POOL 必须有至少一个 SECTION 才能分配地址 | ADD POOL + ADD SECTION | 隐性（推理：空池无法分配） |
| PT-03 | MULTICAST 类型 POOL 的地址段需满足组播地址范围（224.0.0.0~239.255.255.255） | ADD POOL + ADD SECTION | 隐性（从组播语义推断） |

### 10.5 地址池组映射多维度查找（poolgrpmap_multidim_lookup）

**描述**：POOLGRPMAP 是 IP 地址分配的核心查找表，将用户特征（TAC+APN+SMF）映射到地址池组（POOLGROUP），再通过 POOLBINDGROUP 找到具体 POOL。这是一个三维度查找，每个维度都可能缺失导致分配失败。

**查找链**：
```
用户上线 → TAC → TACGROUP (可选)
        → APN → 确定 VPN
        → SMF → CPNODEID
        → POOLGRPMAP(TAC+APN+SMF) → POOLGROUP
                                     → POOLBINDGROUP → POOL(多个，按优先级)
                                                      → SECTION → 分配 IP
```

**证据**：
- ADD POOLGRPMAP：8 个参数，TACGROUPNAME/APNNAME/CPNODEIDNAME 三个查找键，POOLGROUPNAME 是查找结果
- ADD POOLBINDGROUP：将 POOL 绑定到 POOLGROUP，有 PRIORITY 参数决定分配优先级
- ADD POOLGROUP：定义分配算法（PRIORDER/LOADBALANCE/FORWARD），IPv4/IPv6 各自独立配置

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| PM-01 | POOLGRPMAP 的三个查找键中，APNNAME 对应的 APN 必须存在且 HASVPN=ENABLE 时 VPN 已配置 | ADD POOLGRPMAP + ADD APN | 隐性（引用完整性） |
| PM-02 | POOLGRPMAP 引用的 TACGROUPNAME 必须对应存在的 TACGROUP | ADD POOLGRPMAP + ADD TACGROUP | 隐性（引用完整性） |
| PM-03 | POOLGRPMAP 引用的 CPNODEIDNAME 必须对应存在的 CPNODEID | ADD POOLGRPMAP + ADD CPNODEID | 隐性（引用完整性） |
| PM-04 | POOLGRPMAP 引用的 POOLGROUPNAME 必须存在且有至少一个 POOLBINDGROUP | ADD POOLGRPMAP + ADD POOLGROUP + ADD POOLBINDGROUP | 隐性（空组检测） |
| PM-05 | POOLBINDGROUP 中同一 VPN 下每个 POOLGROUP 最多绑定 16 个 POOL | ADD POOLBINDGROUP 注意事项 | 显性 |
| PM-06 | POOLBINDGROUP 中绑定的 POOL 的 VPN 必须与 APN 的 VPN 一致 | ADD POOLBINDGROUP + ADD POOL + ADD APN | 隐性（从 VPN 级联推断） |
| PM-07 | 当 POOLGROUP 的分配算法为 PRIORDER 时，PRIORITY 参数决定分配顺序；LOADBALANCE 时按负载均衡 | ADD POOLGROUP + ADD POOLBINDGROUP | 显性 |
| PM-08 | POOLGRPMAP 中 TACGROUPNAME 为空时表示匹配所有 TAC（通配符语义） | ADD POOLGRPMAP | 隐性（从默认行为推断） |

### 10.6 生效时机一致性（ip_address_effect_timing）

**描述**：IP 地址管理链中各对象的生效时机存在差异，可能导致配置变更后不一致。

**证据**：
- ADD POOL / ADD SECTION："立即生效"
- ADD APN："立即生效"
- ADD VPNINST："立即生效"
- ADD POOLGROUP / ADD POOLBINDGROUP / ADD POOLGRPMAP："仅对后续新上线的用户生效，不影响已在线用户"

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| ET-01 | POOL 容量变更（增加 SECTION）立即生效，但 POOLGROUP 分配策略变更仅对新用户生效 | ADD SECTION + ADD POOLGROUP | 隐性（对比生效时机） |
| ET-02 | 已在线用户的 IP 地址不受 POOLGRPMAP 变更影响，即使用户原本的 POOL 已被删除 | ADD POOLGRPMAP | 隐性（推理：影响范围） |
| ET-03 | POOL 的 VPN 变更"立即生效"，但如果 SECTION 存在则不允许变更（保护机制） | ADD POOL | 显性 |

### 10.7 参数冲突依赖（iplease_releasetime_conflict）

**描述**：ADD POOL 的 IPLEASE 和 RELEASETIME 参数存在隐式冲突依赖。

**证据**：
- ADD POOL：IPLEASE 枚举值 ENABLE/DISABLE，RELEASETIME 取值 0~100000000 秒
- ADD POOL 注意事项："IPLEASE=ENABLE 时，RELEASETIME 必须大于 0"
- ADD POOL 注意事项："IPLEASE=DISABLE 时，RELEASETIME 不生效"

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| IC-01 | IPLEASE=ENABLE 且 RELEASETIME=0 → 配置冲突，地址永远不会释放 | ADD POOL | 显性（注意事项） |
| IC-02 | IPLEASE=DISABLE 且 RELEASETIME>0 → RELEASETIME 无意义但不报错 | ADD POOL | 隐性（推理：无效配置） |

### 10.8 SECTION MASK 路由聚合影响（section_mask_routing）

**描述**：ADD SECTION 的 MASK 参数不仅控制子网掩码，还影响 ISU Pod 的路由聚合和地址分布。

**证据**：
- ADD SECTION：MASK 参数默认值取决于 POOL 的地址类型
- ADD SECTION 注意事项："MASK 影响路由聚合效率，过小的 MASK 会导致路由表膨胀"
- ADD SECTION："同一 POOL 下不同 SECTION 的 MASK 可以不同"

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| SM-01 | 同一 POOL 下所有 SECTION 的 MASK 建议一致，否则可能影响路由聚合效率 | ADD SECTION | 隐性（从路由聚合语义推断） |
| SM-02 | SECTION 的 MASK 必须 ≥ POOL 类型的最小掩码要求 | ADD SECTION + ADD POOL | 隐性（需验证系统约束） |
| SM-03 | ISU Pod 数量与 SECTION 的 MASK 直接相关——MASK 越小，单个 Pod 承载的地址越多 | ADD SECTION | 隐性（从 ISU 分布机制推断） |

### 10.9 APN 高级属性跨命令影响（apn_advanced_attrs）

**描述**：ADD APN 的多个高级属性影响下游命令的行为，但这些影响是分散在不同命令的注意事项中的。

**证据**：
- ADD APN：APPLAYERVOLUME 枚举 ENABLE/DISABLE — 控制是否启用应用层流量统计
- ADD APN：HASVPN / HASVPNIPV6 — 控制 VPN 绑定是否必选
- ADD APN 注意事项："APPLAYERVOLUME=ENABLE 时需配合业务感知链使用"
- ADD APN："APN 的 VPN 配置影响 POOL 的 VPN 选择"

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| AA-01 | APN 的 APPLAYERVOLUME=ENABLE 但未配置业务感知链（FLOWFILTER/RULE 等）→ 统计无效 | ADD APN + 业务感知链命令 | 隐性（跨链依赖） |
| AA-02 | APN 的 HASVPN=ENABLE 但 VPNINSTNAME 为空 → POOL 创建时会因 VPN 不匹配失败 | ADD APN + ADD POOL | 隐性（级联依赖） |
| AA-03 | APN 的 HASVPNIPV6=ENABLE 但 VPNINSTNAMEIPV6 为空 → IPv6 地址分配失败 | ADD APN + ADD POOL | 隐性（级联依赖） |

### 10.10 地址池组 VPN 一致性（poolbindgroup_vpn_consistency）

**描述**：POOLBINDGROUP 将 POOL 绑定到 POOLGROUP 时，同一个 POOLGROUP 下所有 POOL 的 VPN 必须一致。

**证据**：
- ADD POOLBINDGROUP 注意事项："同一个 POOLGROUP 下绑定的 POOL 必须属于同一个 VPN"
- ADD POOLBINDGROUP："每个 VPN 下每个 POOLGROUP 最多绑定 16 个 POOL"

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| PBG-01 | POOLBINDGROUP 中 POOLGROUPNAME 和 POOLNAME 对应的 VPN 必须一致 | ADD POOLBINDGROUP + ADD POOL + ADD POOLGROUP | 显性（注意事项） |
| PBG-02 | 向已有 POOL 的 POOLGROUP 添加新 POOL 时，新 POOL 的 VPN 必须与组内已有 POOL 一致 | ADD POOLBINDGROUP | 隐性（推理：增量一致性） |

### 10.11 POOLGRPMAP 完整性矩阵（poolgrpmap_completeness）

**描述**：POOLGRPMAP 需要覆盖所有可能的 (TAC, APN, SMF) 组合，否则某些用户上线时找不到地址池。

**证据**：
- ADD POOLGRPMAP：TACGROUPNAME/APNNAME/CPNODEIDNAME 三个维度可独立为空（通配）
- 空的组合维度表示通配所有值

**隐式规则**：

| # | 规则 | 涉及命令 | 显/隐 |
|---|------|---------|-------|
| PCM-01 | 如果没有 POOLGRPMAP 条目匹配用户的 (TAC, APN, SMF) 组合 → 用户无法获取 IP 地址 | ADD POOLGRPMAP | 隐性（推理：查找失败） |
| PCM-02 | POOLGRPMAP 中存在 (通配, APN1, 通配) 和 (TAC1, APN1, SMF1) 两条记录时，后者优先（精确匹配优先） | ADD POOLGRPMAP | 隐性（从查找语义推断） |
| PCM-03 | 同一 APN 的 IPv4 和 IPv6 地址需要分别配置 POOLGRPMAP（或使用 IPv4/IPv6 双栈 POOLGROUP） | ADD POOLGRPMAP + ADD POOLGROUP | 隐性（双栈语义） |

### 10.12 IP 地址管理链隐式关系归纳

| 隐式关系类型 | 说明 | 发现条目 |
|-------------|------|---------|
| **vpn_cascade_consistency** | VPN 一致性逐级传递 | 10.1 |
| **vpn_cross_ne_consistency** | VPN 跨网元一致性 | 10.2 |
| **address_overlap_scope** | 地址重叠检测以 VPN 为作用域 | 10.3 |
| **pool_type_constraints** | POOL 类型影响后续使用约束 | 10.4 |
| **poolgrpmap_multidim_lookup** | 三维度查找表完整性 | 10.5 |
| **ip_address_effect_timing** | 生效时机差异 | 10.6 |
| **iplease_releasetime_conflict** | 参数冲突依赖 | 10.7 |
| **section_mask_routing** | MASK 影响路由聚合 | 10.8 |
| **apn_advanced_attrs** | APN 高级属性跨命令影响 | 10.9 |
| **poolbindgroup_vpn_consistency** | 地址池组 VPN 一致性 | 10.10 |
| **poolgrpmap_completeness** | 映射矩阵完整性覆盖 | 10.11 |

---

## 11. 全链路整体分析

### 11.1 两条链路的交叉点

业务感知链与 IP 地址管理链存在以下交叉：

| 交叉点 | 业务感知侧 | IP 地址管理侧 | 交叉含义 |
|--------|-----------|-------------|---------|
| APN | ADD RULE 可按 APN 匹配 | ADD APN 定义 APN | APN 是两条链的公共对象 |
| VPN | RULE/FILTER 不直接涉及 VPN | 整条链绑定 VPN | VPN 隔离影响业务感知策略可见性 |
| POOL | ADD RULE(CHARGING) 的计费统计对象 | ADD POOL 的地址分配 | 计费与地址分配的关系 |
| USERPROFILE | 业务感知匹配入口 | IP 地址分配的对象 | 用户上线同时触发两条链 |

**关键洞察**：用户上线时，两条链并行执行：
1. **IP 地址管理链**：TAC+APN+SMF → POOLGRPMAP → POOLGROUP → POOL → SECTION → 分配 IP
2. **业务感知链**：USERPROFILE → RULEBINDING → RULE → FLOWFILTER → FILTER → 匹配动作

两条链通过 APN 和 USERPROFILE 产生关联。

### 11.2 CFGDOMAINNAME 在 IP 地址管理链中的角色

与业务感知链类似，IP 地址管理链的部分命令也有 CFGDOMAINNAME 参数。但在 IP 地址管理链中，CFGDOMAINNAME 的作用域划分可能与业务感知链不同：
- 业务感知链：CFGDOMAINNAME 用于策略分组和可见性控制
- IP 地址管理链：CFGDOMAINNAME 的作用需进一步验证（部分命令可能不支持该参数）

### 11.3 跨链隐式规则

| # | 规则 | 涉及链路 | 显/隐 |
|---|------|---------|-------|
| XL-01 | APN 的 APPLAYERVOLUME=ENABLE 时，需要业务感知链完整配置才有效 | 业务感知 + IP 地址管理 | 隐性 |
| XL-02 | APN 配置了 VPN 但业务感知链的 RULE 没有考虑 VPN 隔离 → 可能导致策略不生效 | 业务感知 + IP 地址管理 | 隐性 |
| XL-03 | POOL 的 EXTERNAL 类型需要 POOLGRPMAP 绑定 APN，同时 APN 的业务感知策略需配合 | IP 地址管理 + 业务感知 | 隐性 |
| XL-04 | 用户删除时 IP 地址释放受 IPLEASE/RELEASETIME 控制，与业务感知链的 URR 计费统计有关联 | IP 地址管理 + 业务感知（URR） | 隐性 |

### 11.4 全部隐式关系类型总归纳（两链合并）

| # | 隐式关系类型 | 链路 | 条目 |
|---|-------------|------|------|
| 1 | match_semantics_chain | 业务感知 | 9.1 |
| 2 | policy_type_parallel_universes | 业务感知 | 9.2 |
| 3 | policy_type_l7filter_exclusion | 业务感知 | 9.3 |
| 4 | spec_type_compatibility | 业务感知 | 9.4 |
| 5 | effect_timing_chain_inconsistency | 业务感知 | 9.5 |
| 6 | dangling_reference | 业务感知 | 9.6 |
| 7 | empty_container | 业务感知 | 9.6 |
| 8 | dual_level_redirect_filtering | 业务感知 | 9.7 |
| 9 | adc_userprofile_switch_chain | 业务感知 | 9.8 |
| 10 | pcc_direction_consistency | 业务感知 | 9.9 |
| 11 | configuration_completeness_fallback | 业务感知 | 9.10 |
| 12 | cfgdomain_partitioning | 业务感知 | 9.12 |
| 13 | ipfarm_reference_chain | 业务感知 | 9.13 |
| 14 | pccpolicygrp_multi_combination | 业务感知 | 9.14 |
| 15 | vpn_cascade_consistency | IP 地址管理 | 10.1 |
| 16 | vpn_cross_ne_consistency | IP 地址管理 | 10.2 |
| 17 | address_overlap_scope | IP 地址管理 | 10.3 |
| 18 | pool_type_constraints | IP 地址管理 | 10.4 |
| 19 | poolgrpmap_multidim_lookup | IP 地址管理 | 10.5 |
| 20 | ip_address_effect_timing | IP 地址管理 | 10.6 |
| 21 | iplease_releasetime_conflict | IP 地址管理 | 10.7 |
| 22 | section_mask_routing | IP 地址管理 | 10.8 |
| 23 | apn_advanced_attrs | IP 地址管理 | 10.9 |
| 24 | poolbindgroup_vpn_consistency | IP 地址管理 | 10.10 |
| 25 | poolgrpmap_completeness | IP 地址管理 | 10.11 |
| 26 | cross_chain_dependency | 跨链 | 11.3 |

### 11.5 隐式关系的共性模式

从 26 类隐式关系中，可以归纳出以下共性模式：

**模式 A：级联一致性（Cascade Consistency）**
- 特征：上游对象的属性决定下游对象的约束
- 案例：VPN 级联、SPECTYPE 兼容性、策略类型→L7 绑定
- 核查算子设计：沿引用链逐级验证属性一致性

**模式 B：查找完整性（Lookup Completeness）**
- 特征：查找表必须覆盖所有可能的输入组合
- 案例：POOLGRPMAP 矩阵、PCCPOLICYGRP 多组合、ADC 切换链
- 核查算子设计：枚举输入空间，检查查找表覆盖度

**模式 C：引用可达性（Reference Reachability）**
- 特征：引用链终端必须有有效对象
- 案例：悬空引用、空容器、IPFarm→IPFARMSERVER
- 核查算子设计：图遍历，检测无出边或无入边的节点

**模式 D：生效时机差异（Effect Timing Gap）**
- 特征：同一链路中不同对象的变更生效机制不同
- 案例：IP 地址管理链（立即/新用户）、业务感知链（手动刷新/60s 自动）
- 核查算子设计：标记最近变更的对象，检查链路中是否存在已变更但未生效的对象

**模式 E：互斥与冲突（Mutual Exclusion）**
- 特征：两个参数或对象不能同时存在或值冲突
- 案例：IPLEASE vs RELEASETIME、上下行方向一致性
- 核查算子设计：成对检查冲突条件

**模式 F：跨网元一致性（Cross-NE Consistency）**
- 特征：同一逻辑对象在不同网元上需保持一致
- 案例：VPNINST↔L3VPNINST、IPFARMSERVER↔SMF PCSCFIP
- 核查算子设计：跨网元数据比对

### 11.6 核查规则密度分析

按"每条命令平均发现的隐式规则数"排序，规则密度最高的命令：

| 排名 | 命令 | 直接隐式规则数 | 原因 |
|------|------|--------------|------|
| 1 | ADD POOLGRPMAP | 8 | 三维度查找表，完整性复杂 |
| 2 | ADD RULE | 6+ | 14 种策略类型，跨对象引用 |
| 3 | ADD PCCPOLICYGRP | 4 | 多组合机制，中间层 |
| 4 | ADD POOL | 5 | VPN 约束、类型约束、参数冲突 |
| 5 | ADD APN | 4 | 双栈 VPN、高级属性影响 |

**规律**：规则密度与以下因素正相关：
1. 参数数量（更多参数 = 更多约束组合）
2. 引用关系数量（引用其他对象 = 跨命令约束）
3. 条件必选参数数量（更多条件 = 更多依赖链）

### 11.7 下一步建议

1. **补全批次 1 的单命令详细记录**：当前批次 1 有完整的参数契约和规则表，但批次 2-4 只做了跨命令分析，缺少单命令记录
2. **扩展到第三条链**：QoS/URR 计费链可能还有独立的隐式关系
3. **构建核查算子原型**：基于 6 种共性模式，设计可复用的核查算子框架
4. **与业务图谱交叉验证**：将发现的隐式关系与业务图谱的 ConfigObject 层级对比，找出业务图谱遗漏的关系
5. **专题文档补充**：读取两个专题文档中命令使用的套餐脚本，验证隐式规则在实际部署中的表现
