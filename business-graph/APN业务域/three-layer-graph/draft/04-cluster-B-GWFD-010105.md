# APN 业务域命令图谱 · 簇B 样板：GWFD-010105 用户面地址分配（UDG）

> **文件定位**：`three-layer-graph/draft/04-cluster-B-GWFD-010105.md`
> **特性范围**：仅 GWFD-010105 用户面地址分配（UDG 侧），4 个激活子场景（基于APN/DNN、基于SMF、基于SMF+APN/DNN、基于RADIUS下发地址池名称）
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **结构对齐**：严格 follow 现有 `04-command-graph.md`（表格列、CMD-UDG-xxx 编号、小节组织、§5 参数表、§6 operates_on 边）
> **数据来源**：4 篇激活文档 + 参考信息 + 11 篇 MML 命令手册原文（路径见 §抽取核对清单）
> **铁律**：命令/参数 100% 来自原始产品文档原文，零编造。手册未定位的命令标注「⚠️手册未定位」。

---

## 0. 命令清单总览（GWFD-010105 用到的全部命令）

### 0.1 按命令类型分布

| 类型 | 命令数 | 命令清单 |
|------|-------|---------|
| 配置类（ADD/SET） | 11 | ADD POOL、ADD SECTION、ADD POOLGROUP、ADD POOLBINDGROUP、ADD POOLGRPMAP、ADD CONFLICTIP、ADD CPNODEID、SET APNADDRESSATTR、SET IPALLOCRULE、SET APNIPALLOCRULE、SET IPALLOCBYSMFGLBSW、SET ADDRESSATTR |
| 查询类（DSP） | 2 | DSP POOLUSAGE、DSP SECTIONUSAGE（调测查询类，本期略，不抽参数） |
| 前置依赖类（非本特性核心，但在激活脚本中出现） | 6 | ADD L3VPNINST、ADD VPNINSTAF、ADD VPNINST、ADD APN、ADD OSPF、ADD OSPFAREA、ADD OSPFNETWORK、ADD OSPFIMPORTROUTE（这些命令归属簇A/簇E，本文件不重复抽参数，仅在 §6 operates_on 边中标注引用关系） |

> **说明**：SET IPALLOCBYSMFSW（指定 SMF 分配开关）在「基于SMF分配地址」激活文档步骤 5.b 被引用为可选命令，但参考信息（命令清单）未列出，且其手册未在本特性文档树中定位。本文件在 §1 命令表中登记为 `CMD-UDG-010105-13`，标注「⚠️手册未定位（参考信息未列，激活文档引用）」，不抽参数。

### 0.2 ConfigObject 分布（本特性涉及）

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| 地址池体系 | 5 | POOL、SECTION、POOLGROUP、POOLBINDGROUP、POOLGRPMAP |
| 地址分配规则 | 4 | IPALLOCRULE、APNIPALLOCRULE、APNADDRESSATTR、ADDRESSATTR |
| SMF 分配子方式 | 2 | CPNODEID、IPALLOCBYSMFGLBSW |
| 冲突地址 | 1 | CONFLICTIP |
| 前置依赖（引用，非本特性拥有） | 3 | VPNINST、L3VPNINST、APN |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1 所有 MMLCommand。
> **声明**：本文件 §1 所有 MMLCommand 的 `status` 字段值均为 `active`（Schema §11.3 MMLCommand.status 必备）。GWFD-010105 所有正式命令均处于启用状态。
> **依据**：所有命令均在产品文档正式登记，无 `deprecated` 或 `planned` 状态。

---

## 1. MMLCommand 实例化（GWFD-010105，11 个核心配置命令 + 1 个未定位）

### 1.1 地址池体系（UDG，5个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-010105-01` | `ADD POOL` | ADD | POOL | ★UDG 本地地址池（POOLTYPE=LOCAL；高危命令：RELEASETIME 过大导致地址延迟释放）；本地/外部/组播三类型 | POOLNAME, POOLTYPE(LOCAL/EXTERNAL/MULTICAST), IPVERSION, IPLEASE, RELEASETIME, SINGLEIPFLAG, HASVPN, VPNINSTANCE, ALARMSWITCH, IMSSW, REDUNDFUNC, MASTERFLAG | EV-FK-06（GWFD-010105 激活文档）|
| `CMD-UDG-010105-02` | `ADD SECTION` | ADD | SECTION | 地址段（V4STARTIP/V6PREFIXSTART；★V6PREFIXLENGTH 49~64；一个地址池最多 64 段；本地 IPv4 段最多 32768 地址） | POOLNAME, SECTIONNUM, IPVERSION, V4STARTIP, V4ENDIP, V6PREFIXSTART, V6PREFIXEND, V6PREFIXLENGTH, MASK | EV-FK-06 |
| `CMD-UDG-010105-03` | `ADD POOLGROUP` | ADD | POOLGROUP | 地址池组（IPV4ALLOCPRIALG/IPV6ALLOCPRIALG 优先级算法开关） | POOLGRPNAME, IPV4ALLOCPRIALG, IPV6ALLOCPRIALG | EV-FK-06 |
| `CMD-UDG-010105-04` | `ADD POOLBINDGROUP` | ADD | POOLBINDGROUP | 地址池绑定到池组（PRIORITY 1~16，越小优先级越高；★UDG 命名 GROUP；每 VPN 每池组最多 16 V4+16 V6 池） | POOLGROUPNAME, POOLNAME, PRIORITY | EV-FK-06 |
| `CMD-UDG-010105-05` | `ADD POOLGRPMAP` | ADD | POOLGRPMAP | 池组映射（APN/SMF/LOCATIONGRPTYPE+LOCATIONGRPNAME/MCC+MNC 任意组合；★SMF/APN/LOCATION 至少选一种；不支持修改） | MAPPINGNAME, LOCATIONGRPTYPE(LAC/TAC), LOCATIONGRPNAME, APN, SMF, POOLGROUPNAME, MCC, MNC | EV-FK-06 |

### 1.2 地址分配规则（UDG，3个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-010105-06` | `SET IPALLOCRULE` | SET | IPALLOCRULE | ★全局三级地址分配规则（IPv4+IPv6 双规则集，共 12 参数；★含完整 IPv6 规则集 IPV6FIRSTRULESW/IPV6FIRSTRULE/IPV6SECRULESW/IPV6SECONDRULE/IPV6THIRDRULESW/IPV6THIRDRULE；初始值 FIRSTRULESW=ENABLE, FIRSTRULE=APN） | FIRSTRULESW, FIRSTRULE, SECONDRULESW, SECONDRULE, THIRDRULESW, THIRDRULE, IPV6FIRSTRULESW, IPV6FIRSTRULE, IPV6SECRULESW, IPV6SECONDRULE, IPV6THIRDRULESW, IPV6THIRDRULE | EV-FK-06 |
| `CMD-UDG-010105-07` | `SET APNIPALLOCRULE` | SET | APNIPALLOCRULE | APN 级地址分配规则（覆盖全局；★含 ALLOCATTR/IPV6ALLOCATTR=INHERIT|LOCAL 切换；初始值均 INHERIT；共 16 参数含完整 IPv6 规则集） | APN, ALLOCATTR(INHERIT/LOCAL), FIRSTRULESW, FIRSTRULE, SECONDRULESW, SECONDRULE, THIRDRULESW, THIRDRULE, IPV6ALLOCATTR(INHERIT/LOCAL), IPV6FIRSTRULESW, IPV6FIRSTRULE, IPV6SECRULESW, IPV6SECONDRULE, IPV6THIRDRULESW, IPV6THIRDRULE | EV-FK-06 |
| `CMD-UDG-010105-08` | `SET ADDRESSATTR` | SET | ADDRESSATTR | 全局地址分配属性（★RADIUS 下发地址池名称场景；V4/V6POOLWILDCARDSW 通配开关；RELEASETIME；V4/V6IPHOSTROUTE 主机路由发布；高危：与 AAA 不一致导致激活失败） | V4POOLWILDCARDSW, V6POOLWILDCARDSW, RELEASETIME, V4IPHOSTROUTE, V6IPHOSTROUTE | EV-FK-06 |

### 1.3 APN 地址分配属性（UDG，1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-010105-09` | `SET APNADDRESSATTR` | SET | APNADDRESSATTR | ★APN 地址分配属性（高危；15 参数；含 SUPPORTIPV4/V6、IGNOREV4/V6POOLID、HOSTROUTEIP、IPTYPEFORDUALIP、CPCTRL、IPv6 RA 系列；★含 14 参数初始值表） | APN, SUPPORTIPV4, SUPPORTIPV6, FRAMEDROUTE, ANTISPOOFINGDL, ANTISPOOFINGUL, IPTYPEFORDUALIP, SINGLEADDRCAUSE, CPCTRL, IPV6RAMTUSW, IPV6MTU, IPV6RALIFETIME, HOSTROUTEIP, IGNOREV4POOLID, IGNOREV6POOLID | EV-FK-06 |

### 1.4 SMF 分配子方式（UDG，2个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-010105-10` | `ADD CPNODEID` | ADD | CPNODEID | SMF 的 NodeID（基于 SMF 分配场景；CPNODEIDTYPE 三类型 IPV4/IPV6/FQDN；★不同 SMF 实例 NODEID 不可相同；最大 64 记录） | CPNAME, CPNODEIDTYPE(IPV4/IPV6/FQDN), IPV4NODEID, IPV6NODEID, FQDNNODEID, LOCALEMERNODE | EV-FK-06 |
| `CMD-UDG-010105-11` | `SET IPALLOCBYSMFGLBSW` | SET | IPALLOCBYSMFGLBSW | 基于 SMF 分配全局开关（IPv4 SWITCH + IPv6 IPV6SWITCH 双开关；初始值均 DISABLE） | SWITCH, IPV6SWITCH | EV-FK-06 |
| `CMD-UDG-010105-13` | `SET IPALLOCBYSMFSW` | SET | IPALLOCBYSMFSW | 指定 SMF 分配开关（覆盖全局；激活文档步骤 5.b 引用） | ⚠️手册未定位（参考信息未列；激活文档引用 SMFID, SWITCH） | EV-FK-06 |

### 1.5 冲突地址（UDG，1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-010105-12` | `ADD CONFLICTIP` | ADD | CONFLICTIP | 冲突 IPv4 地址标识（★仅 IPv4；标识后不分配给用户；一个地址池最多 16 个冲突地址；已分配地址的冲突标识下次分配生效） | POOLNAME, IPADDRESS | EV-FK-06 |

### 1.6 查询类（调测查询类，本期略）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 说明 |
|--------------|----------------|--------|------------------|-------------------|------|
| `CMD-UDG-010105-Q1` | `DSP POOLUSAGE` | DSP | POOLUSAGE | 地址池使用率查询 | 调测查询类，本期略，不抽参数（参考信息列出） |
| `CMD-UDG-010105-Q2` | `DSP SECTIONUSAGE` | DSP | SECTIONUSAGE | 地址段使用率查询 | 调测查询类，本期略，不抽参数（参考信息列出） |

---

## 2. ConfigObject 实例化（12 个）

### 2.1 地址池体系（5个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-POOL-U` | POOL | UDG | entity | POOLNAME | POOLTYPE(LOCAL/EXTERNAL/MULTICAST), IPVERSION, IPLEASE, RELEASETIME, SINGLEIPFLAG, HASVPN, VPNINSTANCE, ALARMSWITCH, IMSSW, REDUNDFUNC, MASTERFLAG | belongs_to POOLGROUP（via POOLBINDGROUP）；refers_to VPNINST |
| `OBJ-SECTION` | SECTION | 共用 | entity | POOLNAME, SECTIONNUM | IPVERSION, V4STARTIP/V4ENDIP, V6PREFIXSTART/V6PREFIXEND, V6PREFIXLENGTH(49~64), MASK | belongs_to POOL |
| `OBJ-POOLGROUP` | POOLGROUP | UDG | composite | POOLGRPNAME | IPV4ALLOCPRIALG, IPV6ALLOCPRIALG | **contains** POOL（via POOLBINDGROUP） |
| `OBJ-POOLBINDGROUP` | POOLBINDGROUP | UDG | binding | POOLGROUPNAME, POOLNAME | PRIORITY(1~16) | links POOL to POOLGROUP |
| `OBJ-POOLGRPMAP-U` | POOLGRPMAP | UDG | binding | MAPPINGNAME | LOCATIONGRPTYPE(LAC/TAC), LOCATIONGRPNAME, APN, SMF, MCC, MNC | links (APN+SMF+LOCATION) to POOLGROUP |

### 2.2 地址分配规则（4个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-IPALLOCRULE-U` | IPALLOCRULE | UDG | entity | — | FIRSTRULE/SECONDRULE/THIRDRULE（IPv4）+ IPV6FIRSTRULE/IPV6SECONDRULE/IPV6THIRDRULE（IPv6） | — |
| `OBJ-APNIPALLOCRULE` | APNIPALLOCRULE | UDG | entity | APN | ALLOCATTR(INHERIT/LOCAL), IPV6ALLOCATTR(INHERIT/LOCAL), IPv4+IPv6 三级规则 | belongs_to APN（覆盖全局 IPALLOCRULE） |
| `OBJ-APNADDRESSATTR-U` | APNADDRESSATTR | UDG | entity | APN | SUPPORTIPV4/V6, IGNOREV4/V6POOLID, HOSTROUTEIP, IPTYPEFORDUALIP, CPCTRL, IPv6 RA 系列 | belongs_to APN |
| `OBJ-ADDRESSATTR` | ADDRESSATTR | UDG | entity | — | V4/V6POOLWILDCARDSW, RELEASETIME, V4/V6IPHOSTROUTE | —（全局属性，RADIUS 下发地址池名称场景） |

### 2.3 SMF 分配子方式 + 冲突地址（3个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-CPNODEID` | CPNODEID | UDG | entity | CPNAME | CPNODEIDTYPE(IPV4/IPV6/FQDN), IPV4NODEID, IPV6NODEID, FQDNNODEID, LOCALEMERNODE | refers_to POOLGRPMAP（SMF 分配子方式） |
| `OBJ-IPALLOCBYSMFGLBSW` | IPALLOCBYSMFGLBSW | UDG | entity | — | SWITCH(IPv4), IPV6SWITCH(IPv6) | activates OBJ-IPALLOCRULE（SMF 分配子方式） |
| `OBJ-CONFLICTIP` | CONFLICTIP | UDG | entity | POOLNAME, IPADDRESS | —（仅 IPv4） | belongs_to POOL |

---

## 3. ConfigObject 间关系边（§11.7）

### 3.1 contains 边（2条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| POOLGROUP | `contains` | POOL | UDG 地址池组包含地址池（via POOLBINDGROUP） |
| POOL | `contains` | SECTION | 地址池包含地址段（V4STARTIP/V6PREFIXSTART；V6PREFIXLENGTH 49~64） |

### 3.2 refers_to 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| POOL | `refers_to` | VPNINST | UDG 地址池引用 VPN 实例（HASVPN=ENABLE；一个地址池只能绑一个 VPN） |
| APN | `refers_to` | VPNINST / L3VPNINST | APN 引用 VPN（CR-APN-07：与地址池 VPN 必须一致） |
| CPNODEID | `refers_to` | POOLGRPMAP | SMF NodeID 引用池组映射（基于 SMF 分配子方式） |

### 3.3 depends_on 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| POOLGROUP | `depends_on` | POOL | UDG 地址池组依赖地址池存在（ADD POOLBINDGROUP 前必须 ADD POOLGROUP + ADD POOL） |
| SECTION | `depends_on` | POOL | 地址段依赖地址池存在（IPv4 本地池配置 VPN 必须在 SECTION 之前） |
| POOLGRPMAP | `depends_on` | POOLGROUP + CPNODEID/APN/TACGROUP/LACGROUP | 池组映射依赖池组+映射主体存在（手册注意事项明确） |

### 3.4 activates 边（1条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| OBJ-IPALLOCBYSMFGLBSW | `activates` | OBJ-IPALLOCRULE | 基于 SMF 分配全局开关激活三级规则（SMF 分配子方式；SET IPALLOCRULE 按 SMF 映射时必须配合 SET IPALLOCBYSMFSW） |

---

## 4. CommandRule 实例化（本特性相关，5条）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-010105-01` | SET IPALLOCRULE IPv6 规则集与 IPv4 对称 | `parameter_dependency` | explicit | config | parameter | CMD-UDG-010105-06 (SET IPALLOCRULE) | SET IPALLOCRULE 含完整 IPv6 规则集（IPV6FIRSTRULESW/IPV6FIRSTRULE/IPV6SECRULESW/IPV6SECONDRULE/IPV6THIRDRULESW/IPV6THIRDRULE），与 IPv4 规则集（FIRSTRULESW等）对称；条件必选：IPV6XRuleSW=ENABLE 时 IPV6XRule 必选；初始值 IPV6 规则未在手册初始值表列出（仅 IPv4 列出 FIRSTRULESW=ENABLE/FIRSTRULE=APN），IPv6 规则需显式配置 | IPv6 规则未配置导致 IPv6 地址分配回退到默认行为 | warning | EV-FK-06 |
| `CR-010105-02` | 规则字符串位域格式 APN-X&LOCATION-X&SMF-X | `syntax_rule` | explicit | config | parameter | SET IPALLOCRULE.FIRSTRULE / SET APNIPALLOCRULE.FIRSTRULE 等 | 规则字符串为位域类型，格式 `APN-X&LOCATION-X&SMF-X`，X 取 0 或 1（1=有效），条件间为与关系；例 `APN-1&LOCATION-0&SMF-1` 表示从 SMF+APN 映射范围分配；规则需与 POOLGRPMAP 映射条件一致 | 规则与映射不一致导致地址分配失败 | critical | EV-FK-06 |
| `CR-010105-03` | APN VPN 与地址池 VPN 必须一致 | `semantic_rule` | explicit | config | relation | OBJ-APN-U ↔ OBJ-POOL-U | ADD APN 的 VPNINSTANCE 必须与 ADD POOL 的 VPNINSTANCE 一致（手册原文：APN 已绑 VPN 时，地址池必须绑同一 VPN；IPv4 本地池配 VPN 必须在 SECTION 之前；地址池下有 SECTION 或已绑池组时禁止改 VPN） | VPN 不一致导致地址分配后路由不通 | critical | EV-FK-06 |
| `CR-010105-04` | SET ADDRESSATTR 与 AAA 策略必须一致 | `semantic_rule` | explicit | config | parameter | CMD-UDG-010105-08 (SET ADDRESSATTR) | SET ADDRESSATTR 的 V4/V6POOLWILDCARDSW、V4/V6IPHOSTROUTE 必须与 AAA 配置策略一致（手册原文：高危命令，参数配置策略和 AAA 保持一致，否则可能导致无法分配地址，用户激活失败） | 与 AAA 不一致导致用户激活失败 | critical | EV-FK-06 |
| `CR-010105-05` | ADD POOL 高危：RELEASETIME 过大导致地址延迟释放 | `runtime_check_rule` | explicit | restriction | parameter | CMD-UDG-010105-01.RELEASETIME (ADD POOL) | ADD POOL 为高危命令；POOLTYPE=LOCAL 且 RELEASETIME 过大时，用户地址延迟释放，可能导致地址池地址不足、用户激活失败；RELEASETIME=0 且 IPLEASE=ENABLE 时配置失败；建议 RELEASETIME>0 | 地址池耗尽导致用户激活失败 | warning | EV-FK-06 |

---

## 5. MMLCommand 关键参数集（核心命令全参数）

> **Schema 参考**：§11.4 CommandParameter。`required_mode` 取值 `required / optional / conditional_required`（Schema §11.4 必备字段）。本节 11 个核心命令的参数表已从手册原文抽取全量参数。

### 5.1 ADD POOL（UDG 地址池核心命令，13 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POOLNAME | string | 1~79 字节，由 `_`/`-`/数字/字母/`.` 组成，不能以 `.` 开头，无连续 `..`，不区分大小写 | `required` | 无 | 地址池名称 |
| POOLTYPE | enum | LOCAL / EXTERNAL / MULTICAST | `optional` | LOCAL | ★LOCAL=系统分配；EXTERNAL=外部地址；MULTICAST=组播地址 |
| IPVERSION | enum | IPV4 / IPV6 | `conditional_required` | IPV4 | POOLTYPE=EXTERNAL 或 LOCAL 时可选；IP 地址类型 |
| IPLEASE | enum | DISABLE / ENABLE | `conditional_required` | DISABLE | POOLTYPE=LOCAL 时可选；地址租约使能；★RELEASETIME=0 时不能 ENABLE |
| RELEASETIME | int | 0~86400 秒 | `conditional_required` | 10 | POOLTYPE=LOCAL 时可选；用户释放后地址等待释放时间；0=立即释放 |
| SINGLEIPFLAG | enum | DISABLE / ENABLE | `conditional_required` | DISABLE | POOLTYPE=LOCAL 时可选；小地址池标志（每子段一个地址）；★仅 IPv4 支持，IPv6 时 ENABLE 配置失败 |
| CHECKIPVALID | enum | DISABLE / ENABLE | `conditional_required` | DISABLE | POOLTYPE=EXTERNAL 时可选；检查外部地址合法性；★IPv6 地址池不支持白名单检查 |
| HASVPN | enum | DISABLE / ENABLE | `optional` | DISABLE | 绑定 VPN |
| VPNINSTANCE | string | 1~31，区分大小写，不支持空格 | `conditional_required` | 无 | HASVPN=ENABLE 时必填；引用 ADD VPNINST 生成；★与 APN VPN 必须一致 |
| ALARMSWITCH | enum | DISABLE / ENABLE | `conditional_required` | DISABLE | POOLTYPE=LOCAL 时可选；ALM-81216 地址池占用率超门限告警开关 |
| IMSSW | enum | DISABLE / ENABLE | `optional` | ENABLE | IMS 开关；IP 地址租约功能是否对 IMS 用户有效 |
| REDUNDFUNC | enum | DISABLE / ENABLE | `conditional_required` | DISABLE | POOLTYPE=EXTERNAL 时可选；静态地址用户路由冗余功能开关 |
| MASTERFLAG | enum | DISABLE / ENABLE | `conditional_required` | DISABLE | REDUNDFUNC=ENABLE 时可选；标识是否主用 UPF（GRE 冗余容灾场景） |

### 5.2 ADD SECTION（地址段，9 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POOLNAME | string | 1~79 字节，同 ADD POOL 命名规则 | `required` | 无 | 引用 ADD POOL 生成 |
| SECTIONNUM | int | 0~63 | `required` | 无 | 地址段号（一个地址池最多 64 段） |
| IPVERSION | enum | IPV4 / IPV6 | `required` | IPV4 | IP 地址类型 |
| V4STARTIP | IPv4 | IPv4 地址类型 | `conditional_required` | 无 | IPVERSION=IPV4 时必填；起始 IPv4（本地池每段最多 32768 地址，外部池 1048576） |
| V4ENDIP | IPv4 | IPv4 地址类型 | `conditional_required` | 无 | IPVERSION=IPV4 时必填；终止 IPv4（必须 ≥ 起始） |
| V6PREFIXSTART | IPv6 | X:X:X:X:X:X:X:X，冒分十六进制（不支持 0 位压缩/内嵌 IPv4） | `conditional_required` | 无 | IPVERSION=IPV6 时必填；起始前缀（本地/外部池每段最多 1048576 地址） |
| V6PREFIXEND | IPv6 | 同上 | `conditional_required` | 无 | IPVERSION=IPV6 时必填；终止前缀（必须 ≥ 起始；同一 VPN 下前缀段不可重叠） |
| V6PREFIXLENGTH | int | 49~64 | `conditional_required` | 无 | IPVERSION=IPV6 时必填；IPv6 前缀长度 |
| MASK | int | 5~15 | `optional` | 无 | 仅本地地址池；控制系统发布 wlr_ud 网段路由掩码长度（2^N）；不建议修改 |

### 5.3 ADD POOLGROUP（地址池组，3 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POOLGRPNAME | string | 1~79，不支持空格及 `#`/`$`/`&` 等，由 `_`/`-`/数字/字母/`.` 组成，无连续 `..`，不区分大小写 | `required` | 无 | 地址池组名称 |
| IPV4ALLOCPRIALG | enum | DISABLE / ENABLE | `optional` | DISABLE | IPv4 基于地址池优先级分配算法开关 |
| IPV6ALLOCPRIALG | enum | DISABLE / ENABLE | `optional` | DISABLE | IPv6 基于地址池优先级分配算法开关 |

### 5.4 ADD POOLBINDGROUP（地址池绑定到池组，3 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POOLGROUPNAME | string | 1~79，同 ADD POOLGROUP 命名规则 | `required` | 无 | 引用 ADD POOLGROUP 生成 |
| POOLNAME | string | 1~79 字节，同 ADD POOL 命名规则 | `required` | 无 | 引用 ADD POOL 生成 |
| PRIORITY | int | 1~16 | `optional` | 16 | 地址池优先级；★越小优先级越高；生效范围为池组内相同 VPN 的地址池 |

### 5.5 ADD POOLGRPMAP（池组映射，8 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| MAPPINGNAME | string | 1~79，同 ADD POOLGROUP 命名规则 | `required` | 无 | 映射规则名称 |
| LOCATIONGRPTYPE | enum | LAC / TAC | `optional` | 无 | 位置区组类型 |
| LOCATIONGRPNAME | string | 1~32 | `conditional_required` | 无 | LOCATIONGRPTYPE=TAC 或 LAC 时必填；引用 ADD TACGROUP/ADD LACGROUP 生成 |
| APN | string | 1~63，由 `-`/数字/字母/`.` 组成，无连续 `..`，不支持空格/`_`/`#`/`$`/`&` 等 | `optional` | 无 | 引用 ADD APN 生成 |
| SMF | string | 1~255，由 `_`/`-`/数字/字母/`.` 组成，无连续 `..`，不区分大小写 | `optional` | 无 | 引用 ADD CPNODEID 生成 |
| POOLGROUPNAME | string | 1~79，同 ADD POOLGROUP 命名规则 | `required` | 无 | 引用 ADD POOLGROUP 生成 |
| MCC | string | 3 位数字，000~999 | `conditional_required` | 无 | LOCATIONGRPTYPE=LAC 或 TAC 时可选；移动国家码 |
| MNC | string | 2 或 3 位数字，00~99 或 000~999 | `conditional_required` | 无 | LOCATIONGRPTYPE=LAC 或 TAC 时可选；移动网络号（长度取决于 ULI 信元 MNC 有效长度，不受 ADD MNCLEN 影响） |

> **★关键约束**（手册原文）：SMF/APN/LOCATIONGRPTYPE+LOCATIONGRPNAME+PLMN 至少选择输入一种；相同的映射参数组合只能映射一个地址池组；对象不支持修改。

### 5.6 ADD CONFLICTIP（冲突 IPv4 地址，2 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POOLNAME | string | 1~79 字节，同 ADD POOL 命名规则 | `required` | 无 | 引用 ADD POOL 生成 |
| IPADDRESS | IPv4 | IPv4 地址类型 | `required` | 无 | 冲突 IPv4 地址（★仅 IPv4；一个地址池最多 16 个冲突地址；已分配地址的冲突标识下次分配生效） |

### 5.7 ADD CPNODEID（SMF 的 NodeID，6 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| CPNAME | string | 1~255，由 `_`/`-`/数字/字母/`.` 组成，无连续 `..`，不区分大小写 | `required` | 无 | SMF 名称 |
| CPNODEIDTYPE | enum | IPV4 / IPV6 / FQDN | `optional` | 无 | CP NodeID 类型（三类型） |
| IPV4NODEID | IPv4 | IPv4 地址类型 | `conditional_required` | 无 | CPNODEIDTYPE=IPV4 时可选；IPv4 类型的 SMF Node Id（★不同 SMF 实例 NODEID 不可相同） |
| IPV6NODEID | IPv6 | IPv6 地址类型 | `conditional_required` | 无 | CPNODEIDTYPE=IPV6 时可选；IPv6 类型的 SMF Node Id |
| FQDNNODEID | string | 1~255，大小写字母/数字/`-`/`.`，大小写不敏感 | `conditional_required` | 无 | CPNODEIDTYPE=FQDN 时可选；FQDN 类型的 SMF Node Id |
| LOCALEMERNODE | enum | FALSE / TRUE | `optional` | FALSE | 本地应急接入节点 |

### 5.8 SET APNADDRESSATTR（APN 地址分配属性，15 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| APN | string | 1~63，由 `-`/数字/字母/`.` 组成，无连续 `..`，不支持空格/`_`/`#`/`$`/`&` 等 | `required` | 无 | 引用 ADD APN 生成 |
| SUPPORTIPV4 | enum | DISABLE / ENABLE | `optional` | 无（初始值 ENABLE） | 支持 IPv4（必须与网络规划一致） |
| SUPPORTIPV6 | enum | DISABLE / ENABLE | `optional` | 无（初始值 ENABLE） | 支持 IPv6 |
| FRAMEDROUTE | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | 手机后路由（允许手机后路由用户接入） |
| ANTISPOOFINGDL | enum | DISABLE / ENABLE | `optional` | 无（初始值 ENABLE） | 下行防欺诈 |
| ANTISPOOFINGUL | enum | DISABLE / ENABLE | `optional` | 无（初始值 ENABLE） | 上行防欺诈 |
| IPTYPEFORDUALIP | enum | IPV4 / IPV6 / IPV4V6 | `optional` | 无（初始值 IPv4v6） | 双栈用户返回的地址类型（必须与网络规划一致） |
| SINGLEADDRCAUSE | int | 1~255 | `optional` | 无（初始值 1） | 分配单栈地址时返回的原因值（1~63 N4 返回 1；64~255 返回配置值并删除会话） |
| CPCTRL | enum | DISABLE / ENABLE | `conditional_required` | 无（初始值 DISABLE） | IPTYPEFORDUALIP=IPV4V6 时可选；基于 CP 分配 IP 地址（Radius AAA 下发单栈时是否补分配另一类型） |
| IPV6RAMTUSW | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | RA 携带 MTU 选项开关 |
| IPV6MTU | int | 1280~9600 | `conditional_required` | 无（初始值 1800） | IPV6RAMTUSW=ENABLE 时可选；IPv6 MTU 值 |
| IPV6RALIFETIME | int | 3600~65535 秒 | `optional` | 无（初始值 65535） | IPv6 RA 消息路由生命周期 |
| HOSTROUTEIP | enum | DISABLE / ENABLE | `optional` | 无（初始值 ENABLE） | 主机地址（CP 使用主机地址接入；★静态地址用户激活相关） |
| IGNOREV4POOLID | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | 忽略 IPv4 地址池名开关（★RADIUS 下发地址池名称场景；ENABLE=忽略 SMF 下发，从本地池分配） |
| IGNOREV6POOLID | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | 忽略 IPv6 地址池名开关（同上） |

### 5.9 SET IPALLOCRULE（全局三级地址分配规则，★12 参数含完整 IPv6 规则集）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| FIRSTRULESW | enum | DISABLE / ENABLE | `optional` | 无（初始值 ENABLE） | IPv4 第一级规则开关 |
| FIRSTRULE | 位域 | `APN-X&LOCATION-X&SMF-X`，X=0或1 | `conditional_required` | 无（初始值 APN） | FIRSTRULESW=ENABLE 时必填；IPv4 第一级规则（条件间为与关系） |
| SECONDRULESW | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | IPv4 第二级规则开关 |
| SECONDRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无（初始值 NULL） | SECONDRULESW=ENABLE 时必填；IPv4 第二级规则 |
| THIRDRULESW | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | IPv4 第三级规则开关 |
| THIRDRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无（初始值 NULL） | THIRDRULESW=ENABLE 时必填；IPv4 第三级规则 |
| IPV6FIRSTRULESW | enum | DISABLE / ENABLE | `optional` | 无 | ★IPv6 第一级规则开关（初始值表未列出，需显式配置） |
| IPV6FIRSTRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无 | ★IPV6FIRSTRULESW=ENABLE 时必填；IPv6 第一级规则 |
| IPV6SECRULESW | enum | DISABLE / ENABLE | `optional` | 无 | ★IPv6 第二级规则开关 |
| IPV6SECONDRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无 | ★IPV6SECRULESW=ENABLE 时必填；IPv6 第二级规则 |
| IPV6THIRDRULESW | enum | DISABLE / ENABLE | `optional` | 无 | ★IPv6 第三级规则开关 |
| IPV6THIRDRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无 | ★IPV6THIRDRULESW=ENABLE 时必填；IPv6 第三级规则 |

> **★手册原文核对**：SET IPALLOCRULE 手册「参数说明」表共 12 行参数，IPv4 规则集 6 个 + IPv6 规则集 6 个（IPV6FIRSTRULESW/IPV6FIRSTRULE/IPV6SECRULESW/IPV6SECONDRULE/IPV6THIRDRULESW/IPV6THIRDRULE），完全对称。「使用实例」同时配置了 IPv4 和 IPv6 规则。初始值表仅列出 IPv4 的 6 个参数（FIRSTRULESW=ENABLE, FIRSTRULE=APN, 其余 DISABLE/NULL），IPv6 规则初始值未在表中列出（CR-010105-01 已标注）。

### 5.10 SET APNIPALLOCRULE（APN 级地址分配规则，16 参数含 ALLOCATTR 切换 + 完整 IPv6 规则集）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| APN | string | 1~63，同 SET APNADDRESSATTR.APN 命名规则 | `required` | 无 | 引用 ADD APN 生成 |
| ALLOCATTR | enum | INHERIT / LOCAL | `optional` | 无（初始值 INHERIT） | IPv4 分配属性（INHERIT=继承全局；LOCAL=使用本 APN 配置） |
| FIRSTRULESW | enum | DISABLE / ENABLE | `conditional_required` | 无 | ALLOCATTR=LOCAL 时可选；IPv4 第一级规则开关 |
| FIRSTRULE | 位域 | `APN-X&LOCATION-X&SMF-X` | `conditional_required` | 无 | FIRSTRULESW=ENABLE 时必填；IPv4 第一级规则 |
| SECONDRULESW | enum | DISABLE / ENABLE | `conditional_required` | 无 | ALLOCATTR=LOCAL 时可选；IPv4 第二级规则开关 |
| SECONDRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无 | SECONDRULESW=ENABLE 时必填 |
| THIRDRULESW | enum | DISABLE / ENABLE | `conditional_required` | 无 | ALLOCATTR=LOCAL 时可选；IPv4 第三级规则开关 |
| THIRDRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无 | THIRDRULESW=ENABLE 时必填 |
| IPV6ALLOCATTR | enum | INHERIT / LOCAL | `optional` | 无（初始值 INHERIT） | IPv6 分配属性（INHERIT=继承全局；LOCAL=使用本 APN 配置） |
| IPV6FIRSTRULESW | enum | DISABLE / ENABLE | `conditional_required` | 无 | IPV6ALLOCATTR=LOCAL 时可选；IPv6 第一级规则开关 |
| IPV6FIRSTRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无 | IPV6FIRSTRULESW=ENABLE 时必填 |
| IPV6SECRULESW | enum | DISABLE / ENABLE | `conditional_required` | 无 | IPV6ALLOCATTR=LOCAL 时可选；IPv6 第二级规则开关 |
| IPV6SECONDRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无 | IPV6SECRULESW=ENABLE 时必填 |
| IPV6THIRDRULESW | enum | DISABLE / ENABLE | `conditional_required` | 无 | IPV6ALLOCATTR=LOCAL 时可选；IPv6 第三级规则开关 |
| IPV6THIRDRULE | 位域 | 同 FIRSTRULE | `conditional_required` | 无 | IPV6THIRDRULESW=ENABLE 时必填 |

> **★关键约束**（手册原文）：禁止下发 ALLOCATTR=LOCAL 但不下发分配规则的配置；APNIPALLOCRULE 不配置时 ALLOCATTR 默认 INHERIT。

### 5.11 SET IPALLOCBYSMFGLBSW（基于 SMF 分配全局开关，2 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| SWITCH | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | IPv4 开关（基于 SMF 分配地址） |
| IPV6SWITCH | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | IPv6 开关（基于 SMF 分配地址） |

### 5.12 SET ADDRESSATTR（全局地址分配属性，5 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| V4POOLWILDCARDSW | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | IPv4 地址池通配功能开关（★RADIUS 下发地址池名称场景；需与 AAA 一致） |
| V6POOLWILDCARDSW | enum | DISABLE / ENABLE | `optional` | 无（初始值 DISABLE） | IPv6 地址池通配功能开关 |
| RELEASETIME | int | 0~86400 秒 | `optional` | 无（初始值 0） | 地址租期（0=按地址池配置 RELEASETIME 延迟释放） |
| V4IPHOSTROUTE | enum | DISABLE / ENABLE | `optional` | 无（初始值 ENABLE） | IPv4 主机路由发布开关（★DISABLE 可能导致下行包不通） |
| V6IPHOSTROUTE | enum | DISABLE / ENABLE | `optional` | 无（初始值 ENABLE） | IPv6 主机路由发布开关（★DISABLE 可能导致下行包不通） |

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

> **Schema 参考**：§11.7 `MMLCommand operates_on ConfigObject`。

### 6.1 GWFD-010105 核心命令（11条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD POOL (CMD-UDG-010105-01) | POOL | ★UDG 地址池（POOLTYPE=LOCAL） |
| ADD SECTION (CMD-UDG-010105-02) | SECTION | 地址段 |
| ADD POOLGROUP (CMD-UDG-010105-03) | POOLGROUP | 地址池组 |
| ADD POOLBINDGROUP (CMD-UDG-010105-04) | POOLBINDGROUP | 地址池绑定（UDG 命名 GROUP） |
| ADD POOLGRPMAP (CMD-UDG-010105-05) | POOLGRPMAP | 池组映射（APN/SMF/LOCATION 任意组合） |
| SET IPALLOCRULE (CMD-UDG-010105-06) | IPALLOCRULE | 全局三级地址分配规则（IPv4+IPv6 双规则集） |
| SET APNIPALLOCRULE (CMD-UDG-010105-07) | APNIPALLOCRULE | APN 级地址分配规则（覆盖全局） |
| SET ADDRESSATTR (CMD-UDG-010105-08) | ADDRESSATTR | 全局地址分配属性（RADIUS 下发地址池名称场景） |
| SET APNADDRESSATTR (CMD-UDG-010105-09) | APNADDRESSATTR | APN 地址分配属性 |
| ADD CPNODEID (CMD-UDG-010105-10) | CPNODEID | SMF 的 NodeID |
| SET IPALLOCBYSMFGLBSW (CMD-UDG-010105-11) | IPALLOCBYSMFGLBSW | 基于 SMF 分配全局开关 |
| ADD CONFLICTIP (CMD-UDG-010105-12) | CONFLICTIP | 冲突地址标识（仅 IPv4） |

### 6.2 前置依赖命令（引用，非本特性拥有，6条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD VPNINST（簇A） | VPNINST | VPN 实例（前置依赖） |
| ADD L3VPNINST（簇A） | L3VPNINST | L3VPN 实例（前置依赖） |
| ADD VPNINSTAF（簇A） | VPNINSTAF | VPN 地址族（IPv6 需 AFTYPE=ipv6uni） |
| ADD APN（簇A） | APN | APN/DNN 实例（跨域共用挂载点） |
| ADD OSPF / ADD OSPFAREA / ADD OSPFNETWORK / ADD OSPFIMPORTROUTE（簇E） | OSPF 系列 | 手机下行路由（引入 WLR） |

---

## 7. ★CommandRule governs MMLCommand 边表（§11.6 反向）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand / CommandParameter / ConfigObject`（反向：规则治理命令，非命令 has_rule）。

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-010105-01 | CMD-UDG-010105-06 (SET IPALLOCRULE) IPv6 规则集参数 | IPv6 规则集与 IPv4 对称，条件必选，初始值未列出需显式配置 |
| CR-010105-02 | SET IPALLOCRULE.FIRSTRULE + SET APNIPALLOCRULE.FIRSTRULE 等规则参数 | 位域格式 `APN-X&LOCATION-X&SMF-X`，需与 POOLGRPMAP 映射条件一致 |
| CR-010105-03 | OBJ-APN-U ↔ OBJ-POOL-U 关系 | VPN 必须一致（手册原文强约束） |
| CR-010105-04 | CMD-UDG-010105-08 (SET ADDRESSATTR) V4/V6POOLWILDCARDSW 等 | 与 AAA 策略必须一致（高危） |
| CR-010105-05 | CMD-UDG-010105-01.RELEASETIME (ADD POOL) | 高危：RELEASETIME 过大导致地址延迟释放 |

---

## 8. 使用实例脚本（保留手册原文，4 个激活子场景）

### 8.1 基于APN/DNN分配地址（来源：基于APN_DNN分配地址_72547232.md）

```
//配置VPN实例。
ADD L3VPNINST:VRFNAME="vpn1";
ADD VPNINSTAF:VRFNAME="vpn1",AFTYPE=ipv4uni,VRFRD=100:1;

//基于APN使能地址分配属性。
ADD VPNINST:VPNINSTANCE="vpn1";
ADD APN:APN="apn-test1",HASVPN=ENABLE,VPNINSTANCE="vpn1";
SET APNADDRESSATTR:APN="apn-test1",SUPPORTIPV4=ENABLE,SUPPORTIPV6=ENABLE;

//配置地址池。
ADD POOL:POOLNAME="testpool1",POOLTYPE=LOCAL,HASVPN=ENABLE,VPNINSTANCE="vpn1";
ADD SECTION:POOLNAME="testpool1",SECTIONNUM=1,IPVERSION=IPV4,V4STARTIP="10.10.1.1",V4ENDIP="10.10.1.10";

//配置地址池绑定到地址池组。
ADD POOLGROUP: POOLGRPNAME="poolgroup1";
ADD POOLBINDGROUP: POOLGROUPNAME="poolgroup1", POOLNAME="testpool1";
ADD CONFLICTIP:POOLNAME="testpool1",IPADDRESS="10.1.1.1";

//配置APN与地址池组的映射关系。
ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-test1", POOLGROUPNAME="poolgroup1";

//配置地址分配规则。
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

//配置手机下行路由。
ADD OSPF: PROCID=100, VRFNAME="vpn1", SCHEMAROUID="10.10.10.1", LSAARRMAXINTV=1000, LSAARRSTARINTV=500, LSAARRHLDINTV=500;
ADD OSPFAREA:PROCID=100,AREAID="0.0.0.0";
ADD OSPFNETWORK:PROCID=100,AREAID="0.0.0.0", IPADDRESS="10.13.21.0", WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE:PROCID=100,TOPOID=0,PROTOCOL=wlr;
```

### 8.2 基于SMF分配地址（来源：基于SMF分配地址_87605805.md，关键差异：ADD CPNODEID + SET IPALLOCBYSMFGLBSW）

```
//配置SMF实例与地址池组的映射关系。
ADD CPNODEID: CPNAME="smfnode1", IPV4NODEID="10.0.0.1", IPV6NODEID="FC00:1111:1001:0001:0100:1100:0000:0001", FQDNNODEID="consumer.huawei.com";
ADD POOLGRPMAP: MAPPINGNAME="mapping1", SMF="smfnode1", POOLGROUPNAME="poolgroup1";

//配置地址分配规则。
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-0&LOCATION-0&SMF-1, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

//配置基于SMF分配地址的开关。
SET IPALLOCBYSMFGLBSW: SWITCH=ENABLE;
```

### 8.3 基于SMF+APN/DNN分配地址（来源：基于SMF+APN_DNN分配地址_87787640.md，关键差异：二级规则 + 优先级算法）

```
//配置SMF实例、APN/DNN实例与地址池组的映射关系。
ADD CPNODEID: CPNAME="smfnode1", IPV4NODEID="10.0.0.1", IPV6NODEID="FC00:1111:1001:0001:0100:1100:0000:0001", FQDNNODEID="consumer.huawei.com";
ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-test1", SMF="smfnode1", POOLGROUPNAME="poolgroup1";
ADD POOLGRPMAP: MAPPINGNAME="mapping2", SMF="smfnode1", POOLGROUPNAME="poolgroup2";

//配置地址分配规则（二级规则）。
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-1, SECONDRULESW=ENABLE, SECONDRULE=APN-0&LOCATION-0&SMF-1, THIRDRULESW=DISABLE;

SET IPALLOCBYSMFGLBSW: SWITCH=ENABLE;
```

### 8.4 基于RADIUS下发地址池名称分配地址（来源：基于RADIUS下发地址池名称分配地址_13796101.md，关键差异：IGNOREV4/V6POOLID + SET ADDRESSATTR + SET APNIPALLOCRULE）

```
//基于RADIUS下发地址池名称使能地址分配属性。
ADD APN:APN="apn-test1",HASVPN=ENABLE,VPNINSTANCE="vpn1";
SET APNADDRESSATTR:APN="apn-test1",SUPPORTIPV4=ENABLE,SUPPORTIPV6=ENABLE,IGNOREV4POOLID=DISABLE,IGNOREV6POOLID=DISABLE;

//配置APN与地址池组的映射关系。
ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-test1", POOLGROUPNAME="poolgroup1";

//配置地址分配规则（基于APN，非全局）。
SET APNIPALLOCRULE: APN="apn-test1",ALLOCATTR=LOCAL,FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

//配置地址池名称使能通配功能。
SET ADDRESSATTR: V4POOLWILDCARDSW=ENABLE, V6POOLWILDCARDSW=ENABLE;
```

---

## 9. 抽取核对清单

### 9.1 配置类命令参数行数与来源手册路径

| 命令 | 参数行数 | 来源手册路径（相对 `output/UDG_Product_Documentation_CH_20.15.2/`） |
|------|---------|----------------------------------------------------------------|
| ADD POOL | 13 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/添加地址池（ADD POOL）_82837132.md` |
| ADD SECTION | 9 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址段配置/添加地址池IP地址段（ADD SECTION）_82837114.md` |
| ADD POOLGROUP | 3 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池组/添加地址池组（ADD POOLGROUP）_82837138.md` |
| ADD POOLBINDGROUP | 3 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池绑定地址池组/绑定地址池到地址池组（ADD POOLBINDGROUP）_82837143.md` |
| ADD POOLGRPMAP | 8 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池组映射关系/添加地址池组映射关系（ADD POOLGRPMAP）_82837148.md` |
| ADD CONFLICTIP | 2 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/冲突地址管理/IPv4冲突地址管理/添加本地地址池中冲突IPv4地址（ADD CONFLICTIP）_82837120.md` |
| ADD CPNODEID | 6 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/SMF属性/添加SMF的NodeID（ADD CPNODEID）_16780315.md` |
| SET APNADDRESSATTR | 15 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/APN的地址分配属性配置/设置ApnAddressAttr配置（SET APNADDRESSATTR）_82837173.md` |
| SET IPALLOCRULE | 12 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址分配规则/设置地址分配规则（SET IPALLOCRULE）_82837152.md` |
| SET APNIPALLOCRULE | 16 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/基于APN的地址分配规则/基于APN配置地址分配规则（SET APNIPALLOCRULE）_82837165.md` |
| SET IPALLOCBYSMFGLBSW | 2 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/基于SMF分配地址开关/设置基于SMF分配地址全局开关（SET IPALLOCBYSMFGLBSW）_82837157.md` |
| SET ADDRESSATTR | 5 | `OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/全局地址分配属性配置/设置全局地址分配属性（SET ADDRESSATTR）_06561538.md` |
| **合计** | **94 参数行** | 12 命令全部手册定位成功 |

### 9.2 ⚠️手册未定位列表

| 命令 | 状态 | 原因 |
|------|------|------|
| `SET IPALLOCBYSMFSW`（指定 SMF 分配开关） | ⚠️手册未定位 | 参考信息（命令清单）未列出；仅在「基于SMF分配地址」激活文档步骤 5.b 作为可选命令引用（参数 SMFID, SWITCH 为推断，非手册原文）。本文件登记为 `CMD-UDG-010105-13`，不抽参数。 |

> **说明**：除 SET IPALLOCBYSMFSW 外，本特性参考信息列出的全部命令（ADD POOL/SECTION/POOLGROUP/POOLBINDGROUP/POOLGRPMAP + DSP POOLUSAGE/SECTIONUSAGE）手册均已定位。SET IPALLOCRULE/APNIPALLOCRULE/APNADDRESSATTR/ADDRESSATTR/IPALLOCBYSMFGLBSW/CPNODEID/CONFLICTIP 虽未在参考信息命令清单中列出，但在 4 个激活文档中明确引用，手册均已定位。

### 9.3 与现有 04-command-graph.md 的关键差异（★重点核对项）

| 差异项 | 现有 04 | 本样板（draft） | 影响 |
|--------|---------|----------------|------|
| **SET IPALLOCRULE IPv6 规则集** | ★**丢失**：§1.4 CMD-UDG-019 关键参数仅列 IPv4 规则（FIRSTRULESW/FIRSTRULE/SECONDRULESW/SECONDRULE/THIRDRULESW/THIRDRULE），**未含 IPv6 规则集**（IPV6FIRSTRULESW/IPV6FIRSTRULE/IPV6SECRULESW/IPV6SECONDRULE/IPV6THIRDRULESW/IPV6THIRDRULE） | ★**补齐**：§5.9 完整抽取 12 参数（IPv4 6 + IPv6 6），含条件必选（XRuleSW=ENABLE 时 XRule 必选）+ 初始值（FIRSTRULESW=ENABLE, FIRSTRULE=APN）+ 位域格式 `APN-X&LOCATION-X&SMF-X` + CR-010105-01 标注 IPv6 初始值未在手册表列出 | IPv6 地址分配规则配置完整性 |
| **SET APNIPALLOCRULE** | §1.4 CMD-UDG-020 关键参数仅列 `APN, FIRSTRULE, ...`（省略） | §5.10 完整抽取 16 参数（含 ALLOCATTR/IPV6ALLOCATTR=INHERIT\|LOCAL 切换 + IPv4+IPv6 完整规则集） | APN 级规则覆盖全局的完整建模 |
| **SET APNADDRESSATTR** | §1.3 CMD-UDG-013 关键参数列 6 个（APN/SUPPORTIPV4/V6/IGNOREV4V6POOLID/HOSTROUTEIP） | §5.8 完整抽取 15 参数（含 FRAMEDROUTE/ANTISPOOFINGDL/UL/IPTYPEFORDUALIP/SINGLEADDRCAUSE/CPCTRL/IPV6RA 系列等 9 个原缺参数）+ 14 参数初始值表 | APN 地址分配属性完整建模 |
| **ADD POOL** | §1.3 CMD-UDG-014 关键参数列 5 个（POOLNAME/POOLTYPE/IPVERSION/HASVPN/VPNINSTANCE） | §5.1 完整抽取 13 参数（含 IPLEASE/RELEASETIME/SINGLEIPFLAG/CHECKIPVALID/ALARMSWITCH/IMSSW/REDUNDFUNC/MASTERFLAG 等 8 个原缺参数）+ POOLTYPE 三类型（LOCAL/EXTERNAL/**MULTICAST**，原 04 仅 LOCAL/EXTERNAL） | 地址池完整建模 + MULTICAST 类型 |
| **ADD CPNODEID** | §1.4 CMD-UDG-021 关键参数仅列 `NODEID`（错误：手册无 NODEID 参数，实为 CPNAME + CPNODEIDTYPE + 三类型 NODEID） | §5.7 完整抽取 6 参数（CPNAME/CPNODEIDTYPE/IPV4NODEID/IPV6NODEID/FQDNNODEID/LOCALEMERNODE），纠正参数名 | ★参数名纠正（NODEID → CPNAME + 三类型） |
| **ADD POOLGRPMAP** | §1.4 CMD-UDG-018 关键参数列 3 个（MAPPINGNAME/APN/POOLGROUPNAME） | §5.5 完整抽取 8 参数（含 SMF/LOCATIONGRPTYPE/LOCATIONGRPNAME/MCC/MNC，支撑基于 SMF/位置分配子方式） | 池组映射完整建模 |
| **ADD CONFLICTIP** | §1.4 CMD-UDG-024-1/024-2 拆分为 CONFLICTIP（IPv4）+ CONFLICTIPV6（IPv6）两条命令 | §5.6 手册原文仅 ADD CONFLICTIP（IPv4，参数 POOLNAME/IPADDRESS）；**手册未定位 ADD CONFLICTIPV6 命令**（参考信息也未列），原 04 的 CMD-UDG-024-2 ADD CONFLICTIPV6 疑为推导，需复核 | ★CONFLICTIPV6 命令存在性存疑 |
| **SET ADDRESSATTR** | 原 04 §1 未单独登记（仅在 UNC 侧 CMD-UNC-016-3 出现同名 SET ADDRESSATTR，关键参数错误标为 `FIRSTRULE, ...`） | §5.12 完整抽取 5 参数（V4/V6POOLWILDCARDSW/RELEASETIME/V4/V6IPHOSTROUTE），纠正用途（全局地址分配属性，非地址分配规则）；UDG 侧 RADIUS 下发地址池名称场景核心命令 | ★UDG 侧 SET ADDRESSATTR 补登记 + 参数纠正 |
| **SET IPALLOCBYSMFGLBSW** | §1.4 CMD-UDG-022 关键参数仅列 `SWITCH`（缺 IPV6SWITCH） | §5.11 完整抽取 2 参数（SWITCH IPv4 + IPV6SWITCH IPv6 双开关） | IPv6 SMF 分配开关补齐 |
| **CommandRule** | 原 04 未针对 GWFD-010105 建立特性级 CR（CR-APN-01~18 为跨特性汇总） | §4 建立 5 条特性级 CR-010105-01~05（IPv6 规则集对称/位域格式/VPN 一致/AAA 一致/RELEASETIME 高危） | 特性级规则治理细化 |

### 9.4 抽取统计

| 维度 | 数量 |
|------|------|
| 配置类命令（手册定位成功） | 12 |
| 配置类命令参数总行数 | 94 |
| 查询类命令（本期略） | 2（DSP POOLUSAGE / DSP SECTIONUSAGE） |
| ⚠️手册未定位命令 | 1（SET IPALLOCBYSMFSW） |
| ConfigObject | 12 |
| CommandRule | 5 |
| ConfigObject 关系边 | 9（contains 2 + refers_to 3 + depends_on 3 + activates 1） |
| operates_on 边 | 11（核心）+ 6（前置依赖引用） |
| 激活子场景脚本 | 4（基于APN/SMF/SMF+APN/RADIUS） |

---

> 本文件为 GWFD-010105 用户面地址分配（UDG）命令层抽取样板，作为后续特性（簇A/C/D/E/F）的参照模板。
> **★关键贡献**：①补齐 SET IPALLOCRULE 完整 IPv6 规则集（6 参数，原 04 丢失）；②纠正 ADD CPNODEID 参数名（NODEID → CPNAME+三类型）；③补登记 UDG 侧 SET ADDRESSATTR（原 04 仅 UNC 侧且参数错误）；④发现 ADD CONFLICTIPV6 命令存在性存疑（手册+参考信息均未定位，原 04 CMD-UDG-024-2 疑为推导）；⑤建立 5 条特性级 CommandRule。
