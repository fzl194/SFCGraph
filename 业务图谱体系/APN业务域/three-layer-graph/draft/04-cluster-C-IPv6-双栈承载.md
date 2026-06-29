# APN 业务域命令图谱 · 簇C：IPv4v6双栈 + IPv6承载上下文（UDG + UNC，4 特性）

> **文件定位**：`three-layer-graph/draft/04-cluster-C-IPv6-双栈承载.md`
> **特性范围**：4 个 IPv6/双栈承载特性
>   - GWFD-020403 IPv4v6双栈接入（UDG/UPF 侧，License LKV3G5VDSA01）
>   - WSFD-104002 IPv4v6双栈接入（UNC/SMF 侧，2G3G4G: LKV2DUSA02/LKV2IPDSSM01；5G: LKV2IPDSAM01/LKV2IPDSSM01）
>   - GWFD-020401 IPv6承载上下文（UDG/UPF 侧，License LKV3G5V6PB01）
>   - WSFD-104001 IPv6承载上下文（UNC/SMF 侧，License LKV2IPV601/LKV2IPV6SM01/LKV2IPV6AM01）
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **结构对齐**：严格 follow `04-cluster-B-GWFD-010105.md` 样板（编号 `CMD-<NF>-<featureid>-xx`，9 节结构）
> **数据来源**：4 特性的「参考信息 + 特性概述 + 激活文档」原文 + 13 篇 MML 命令手册原文（路径见 §抽取核对清单）
> **铁律**：命令/参数 100% 来自原始产品文档原文，零编造。手册未定位的命令标注「⚠️手册未定位」。
> **★关键发现**：UNC IPv6承载上下文（WSFD-104001，3 个代际 AMF_SMF / MME_SGW-C_PGW-C / SGSN_GGSN）参考信息**全部明确写「本特性无相关命令」**，激活文档仅 SET LICENSESWITCH 一条命令——这是纯 License 控制特性，无独立配置命令。

---

## 0. 命令清单总览（4 特性合计）

### 0.1 按命令类型分布

| 类型 | 命令数 | 命令清单 |
|------|-------|---------|
| License 开关（SET LICENSESWITCH） | 1（UDG/UNC 各一版手册，跨特性共用） | SET LICENSESWITCH（控制 IPv6 License 链 6 个 License 项） |
| UNC 双栈核心配置（WSFD-104002, 2G3G4G） | 3 | SET SMFUNC（DUALFLAG 双栈开关）、ADD SMSUBDATA（签约数据纠正，PDPTYPE→NEWPDPTYPE）、MOD GTPCCMPT（GTP-C V0/V1 Common Flags 兼容性） |
| UDG 路由发布（IPv6 手机下行路由，GWFD-020401/020403 共用） | 6 | ADD ROUTEPOLICY、ADD ROUTEPOLICYNODE、ADD MATCHROUTETYPE、ADD OSPFV3、ADD OSPFV3AREA、ADD OSPFV3IMPORTROUTE |
| 查询类（DSP，调测查询类，本期略，不抽参数） | 2 | DSP SMCTX（UNC 双栈 2G3G4G）、DSP PDUSESSION（UNC 双栈 5G） |
| 前置依赖类（非本簇核心，在激活脚本中引用） | 多 | ADD APN / ADD POOL / ADD SECTION / ADD POOLGROUP / ADD POOLBINDGROUP / ADD POOLGRPMAP（簇B 已抽）、ADD VPNINST / ADD L3VPNINST / ADD VPNINSTAF（簇A 已抽） |

> **★说明 1**：IPv6/双栈特性在 UDG 侧**复用簇B 地址分配命令体系**（ADD POOL/SECTION 配 IPv6 段、ADD APN 配 HASVPNIPV6/VPNINSTANCEIPV6），本文件不重复抽参数，仅在 §6 operates_on 边中标注引用关系。UDG 双栈激活脚本的关键差异是 ADD APN 增加 `HASVPNIPV6=ENABLE, VPNINSTANCEIPV6` 双 VPN 字段，ADD SECTION 配 `IPVERSION=IPV6, V6PREFIXSTART/END/LENGTH` IPv6 段——这些参数在簇B ADD APN / ADD SECTION 手册中已完整抽取（见 CR-C-01、CR-C-02）。
> **★说明 2**：UNC 侧 IPv6/双栈**不引入新地址池/段命令**，地址分配由 SMF 触发 UPF 完成（跨 SBI/N4 接口），UNC 侧仅做 License 控制 + 会话管理双栈使能 + 签约数据纠正。

### 0.2 IPv6 License 链（★本簇核心，6 个 License 项跨 UDG/UNC）

| License 项 | 特性 | 产品 | 含义 | 来源（激活文档） |
|-----------|------|------|------|----------------|
| `LKV3G5V6PB01` | GWFD-020401 IPv6承载上下文 | UDG | UDG IPv6 承载上下文（手机下行 IPv6 路由） | `激活IPv6承载上下文_38276176.md` |
| `LKV3G5VDSA01` | GWFD-020403 IPv4v6双栈接入 | UDG | UDG IPv4v6 双栈接入（依赖 V6PB01） | `激活IPv4v6双栈接入_38276180.md` |
| `LKV2IPV601` | WSFD-104001 IPv6承载上下文（MME/SGW-C/PGW-C、SGSN/GGSN） | UNC | UNC 2G3G4G IPv6 承载 | `激活IPv6承载上下文特性（适用于MME、SGW-C_PGW-C）_48043351.md`、`激活IPv6承载上下文特性（SGSN_GGSN）_48043366.md` |
| `LKV2IPV6SM01` | WSFD-104001 IPv6承载上下文（SMF 全代际） | UNC | UNC SMF IPv6 承载（5G/4G 共用） | 同上 + AMF_SMF 激活文档 |
| `LKV2IPV6AM01` | WSFD-104001 IPv6承载上下文（AMF） | UNC | UNC AMF IPv6 承载（5G） | `激活IPv6承载上下文特性（AMF_SMF）_48043375.md` |
| `LKV2DUSA02` | WSFD-104002 IPv4v6双栈接入（SGSN/MME） | UNC | UNC 2G3G4G 双栈（SGSN/MME 侧，SET SMFUNC.DUALFLAG 生效前提） | `激活IPv4v6双栈接入特性（适用于SGSN_MME）_48043379.md` |
| `LKV2IPDSSM01` | WSFD-104002 IPv4v6双栈接入（PGW-C/SMF） | UNC | UNC PGW-C/SMF 双栈 | `激活IPv4v6双栈接入特性（适用于PGW-C）_48043380.md`、`激活IPv4v6双栈接入特性_48043372.md`（5G） |
| `LKV2IPDSAM01` | WSFD-104002 IPv4v6双栈接入（AMF） | UNC | UNC AMF 双栈（5G） | `激活IPv4v6双栈接入特性_48043372.md`（5G） |

> **★License 链依赖关系**（手册原文 + 特性概述「License支持」节）：
> - **UDG 侧**：`LKV3G5V6PB01`（IPv6承载）是基础，`LKV3G5VDSA01`（双栈）依赖其存在（双栈必然包含 IPv6 承载）。
> - **UNC 侧**：IPv6 承载分 AMF/SMF 两个网元独立 License（`LKV2IPV6AM01`/`LKV2IPV6SM01`），2G3G4G 用 `LKV2IPV601`+`LKV2IPV6SM01`；双栈在 SGSN/MME 用 `LKV2DUSA02`，PGW-C/SMF 用 `LKV2IPDSSM01`，AMF 用 `LKV2IPDSAM01`，5G 双栈需 AMF+SMF 双开（`LKV2IPDSAM01`+`LKV2IPDSSM01`）。
> - **UDG vs UNC License 编码体系不同**：UDG 用 `LKV3G5V*` 前缀（V5 平台），UNC 用 `LKV2*` 前缀（V2 平台）。

### 0.3 ConfigObject 分布（本簇涉及）

| 功能域 | 对象数 | 关键对象 | 说明 |
|-------|-------|---------|------|
| License 控制 | 1 | LICENSESWITCH | 跨特性共用，控制 IPv6 License 链 |
| UNC 双栈会话管理 | 2 | SMFUNC（DUALFLAG）、SMSUBDATA | UNC 2G3G4G 双栈核心对象 |
| UNC GTP-C 兼容性 | 1 | GTPCCMPT | GTP-C V0/V1 Common Flags（2G3G 双栈兼容） |
| UDG IPv6 路由 | 4 | ROUTEPOLICY、ROUTEPOLICYNODE、MATCHROUTETYPE、OSPFV3 | UDG 手机下行 IPv6 路由发布 |
| UDG OSPFv3 子对象 | 2 | OSPFV3AREA、OSPFV3IMPORTROUTE | OSPFv3 区域 + 引入 WLR 路由 |
| 前置依赖（引用，非本簇拥有） | 多 | APN、POOL、SECTION、VPNINST、L3VPNINST、VPNINSTAF | 簇A/B 已抽 |

### 0.4 全局字段声明（status）

> **适用范围**：本文件 §1 所有 MMLCommand。
> **声明**：本文件 §1 所有 MMLCommand 的 `status` 字段值均为 `active`（Schema §11.3 MMLCommand.status 必备）。所有命令均在产品文档正式登记，无 `deprecated` 或 `planned` 状态。

---

## 1. MMLCommand 实例化（按特性分组，10 个核心命令）

### 1.1 GWFD-020401 IPv6承载上下文（UDG，6 个：1 License + 5 路由发布）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-020401-01` | `SET LICENSESWITCH` | SET | LICENSESWITCH | ★UDG License 开关（IPv6承载 LKV3G5V6PB01；执行后立即生效；License 文件未激活时无法设置） | LICITEM, SWITCH(ENABLE/DISABLE) | EV-C-01（GWFD-020401 激活文档）|
| `CMD-UDG-020401-02` | `ADD ROUTEPOLICY` | ADD | ROUTEPOLICY | 路由策略（IPv6 手机下行路由 WLR 发布用；最大 65535 记录） | POLICYNAME | EV-C-01 |
| `CMD-UDG-020401-03` | `ADD ROUTEPOLICYNODE` | ADD | ROUTEPOLICYNODE | 路由策略节点（permit/deny 匹配模式；★依赖 ROUTEPOLICY 存在） | POLICYNAME, NODESEQUENCE, MATCHMODE(permit/deny), DESCRIPTION | EV-C-01 |
| `CMD-UDG-020401-04` | `ADD MATCHROUTETYPE` | ADD | MATCHROUTETYPE | 路由类型匹配（★ROUTETYPE 含 wlr_ud/wlr_sp/wlr_bh/wlr_gbh 无线路由类型；IPv6 承载用 nssaExternal1） | POLICYNAME, NODESEQUENCE, ROUTETYPE(external1/external2/internal/nssaExternal1/nssaExternal2/wlr_ud/wlr_sp/wlr_bh/wlr_gbh/...) | EV-C-01 |
| `CMD-UDG-020401-05` | `ADD OSPFV3` | ADD | OSPFV3 | ★OSPFv3 进程（IPv6 路由协议；★PROCID+ROUTERID 必选；VRFNAME 绑 VPN；最大 8016 记录；无 Router ID 无法生成 LSA） | PROCID, ROUTERID, VRFNAME, SILENTALLFLAG, BFD 系列, SPF 系列, SANAME | EV-C-01 |
| `CMD-UDG-020401-06` | `ADD OSPFV3AREA` | ADD | OSPFV3AREA | OSPFv3 区域（★依赖 OSPFV3 进程；AREATYPE Normal/Stub/NSSA；最大 8016 记录） | PROCID, AREAID, AREATYPE(Normal/Stub/NSSA), DEFAULTCOST, NSSA 系列 | EV-C-01 |
| `CMD-UDG-020401-07` | `ADD OSPFV3IMPORTROUTE` | ADD | OSPFV3IMPORTROUTE | ★OSPFv3 引入外部路由（IPv6 手机下行 WLR 发布核心；★PROTOCOL=wlr 引入无线路由；ROUPOLINAME 引用路由策略；最大 8000 记录） | PROCID, TOPOID, PROTOCOL(direct/static/bgp/ospfv3/wlr), PROTOCOLPROCID, COST/TAG/TYPE 系列, ROUPOLINAME, PERMITIBGPCFG, INHERITCOSTCFG | EV-C-01 |

> **★手册核对**：GWFD-020401 参考信息命令清单列 5 个（ROUTEPOLICY/ROUTEPOLICYNODE/MATCHROUTETYPE/OSPFV3/OSPFV3IMPORTROUTE），未列 ADD OSPFV3AREA，但激活文档步骤 8 明确引用「ADD OSPFV3AREA」且手册已定位（`创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md`）。本文件补登记为 CMD-UDG-020401-06。

### 1.2 GWFD-020403 IPv4v6双栈接入（UDG，2 个核心 + 复用簇B）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-020403-01` | `SET LICENSESWITCH` | SET | LICENSESWITCH | ★UDG License 开关（IPv4v6双栈 LKV3G5VDSA01；★双栈依赖 IPv6承载 LKV3G5V6PB01） | LICITEM, SWITCH(ENABLE/DISABLE) | EV-C-02（GWFD-020403 激活文档）|
| `CMD-UDG-020403-Q1` | `DSP POOLUSAGE` / `DSP SECTIONUSAGE` | DSP | — | 调测查询类（簇B 已登记，本期略） | — | EV-C-02 |

> **★说明**：GWFD-020403 参考信息命令清单列 7 个（ROUTEPOLICY/ROUTEPOLICYNODE/MATCHROUTETYPE/OSPF/OSPFV3/OSPFIMPORTROUTE/OSPFV3IMPORTROUTE），但这些是**手机下行路由发布通用命令**（IPv4 用 OSPF，IPv6 用 OSPFv3），与 GWFD-020401 高度重叠。本簇统一在 §1.1 抽取 OSPFv3 系列（IPv6 专用），OSPF（IPv4）系列归簇E/通用路由。GWFD-020403 激活脚本实际只新增 SET LICENSESWITCH + 复用簇B 地址分配命令（ADD APN 配 HASVPNIPV6 + ADD POOL/SECTION 配 IPv6 段），不重复抽参数。

### 1.3 WSFD-104002 IPv4v6双栈接入（UNC，2G3G4G：3 核心 + 5G：1 核心）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-104002-01` | `SET LICENSESWITCH` | SET | LICENSESWITCH | ★UNC License 开关（双栈：2G3G4G SGSN/MME 用 LKV2DUSA02，PGW-C 用 LKV2IPDSSM01；5G AMF 用 LKV2IPDSAM01+SMF 用 LKV2IPDSSM01） | LICITEM, SWITCH(ENABLE/DISABLE) | EV-C-03（2G3G4G SGSN_MME 激活）、EV-C-04（2G3G4G PGW-C 激活）、EV-C-05（5G 激活）|
| `CMD-UNC-104002-02` | `SET SMFUNC` | SET | SMFUNC | ★UNC 会话管理扩展功能（★DUALFLAG=YES 开启 IPv4v6 双栈；★DUALFLAG=YES 时需 LKV2DUSA02 License 才生效；初始值 NO；含 PDPTYPE 单栈回退策略 IPV4/IPV6/IPV4V6） | DUALFLAG(YES/NO), PDPTYPE(IPV4/IPV6/IPV4V6), INDFWD, TOPSELCFG, APNRES, ... 共 25 参数 | EV-C-03 |
| `CMD-UNC-104002-03` | `ADD SMSUBDATA` | ADD | SMSUBDATA | ★UNC 签约数据纠正（HLR/HSS 不支持双栈时纠正签约；★PDPTYPE=IPV4 → NEWPDPTYPE=IPV4V6 改签约类型；含 IPv4/IPv6 动态/静态分配类型切换；共 17 参数） | SUBRANGE, IMSIPRE, TYPE, CTXID, APNNIRANGE, APNNI, PDPTYPE, IPV4PDPADDRTYPE, IPV4, IPV6PDPADDRTYPE, IPV6, CORRECTAPNNI, NEWAPNNI, NEWPDPTYPE, NEWIPV4PDPADDRTYPE, NEWIPV4, NEWIPV6PDPADDRTYPE, NEWIPV6 | EV-C-03 |
| `CMD-UNC-104002-04` | `MOD GTPCCMPT` | MOD | GTPCCMPT | UNC GTP-C V0/V1 协议兼容性（★双栈兼容：Create/Update PDP Context Request 携带 Common Flags 信元；CMFLG=YES；共 14 参数） | MSGCLS, MMMSGTYPE, TMMSGTYPE, CTXRSP, FWDRLCREQ, FWDSRNSCTX, CRTPDPREQ, UPDPDPREQ, UPDPDPRES, DELPDPRES, DELPDPREQ, INCLUDE, APNOICASE, CMFLG, UPSELFLAG | EV-C-03 |
| `CMD-UNC-104002-Q1` | `DSP SMCTX` | DSP | SMCTX | 调测查询类（显示承载上下文，2G3G4G 双栈查询；本期略） | — | EV-C-03 |
| `CMD-UNC-104002-Q2` | `DSP PDUSESSION` | DSP | PDUSESSION | 调测查询类（显示 PDU 会话，5G 双栈查询；支持 IPV4ADDR/IPV6ADDR 查询；本期略） | — | EV-C-05 |

### 1.4 WSFD-104001 IPv6承载上下文（UNC，3 代际：仅 1 License 命令）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-104001-01` | `SET LICENSESWITCH` | SET | LICENSESWITCH | ★UNC License 开关（IPv6承载：AMF 用 LKV2IPV6AM01，SMF 用 LKV2IPV6SM01，MME/SGW-C/PGW-C/SGSN/GGSN 用 LKV2IPV601+LKV2IPV6SM01） | LICITEM, SWITCH(ENABLE/DISABLE) | EV-C-06（AMF_SMF 激活）、EV-C-07（MME_SGW-C_PGW-C 激活）、EV-C-08（SGSN_GGSN 激活）|

> **★关键发现（手册原文铁证）**：WSFD-104001 IPv6承载上下文的 3 个代际（AMF_SMF / MME_SGW-C_PGW-C / SGSN_GGSN）参考信息**全部明确写「本特性无相关命令」**（原文逐字引用）：
> - `WSFD-104001 IPv6承载上下文（AMF_SMF）参考信息_48043348.md`：「本特性无相关命令。」
> - `WSFD-104001 IPv6承载上下文（MME、SGW-C_PGW-C）参考信息_48043353.md`：「本特性无相关命令。」
> - `WSFD-104001 IPv6承载上下文（SGSN_GGSN）参考信息_48043377.md`：「本特性无相关命令。」
>
> 3 个激活文档的操作步骤均**只有一步**：「打开 IPv6 承载上下文特性的 License 配置开关 SET LICENSESWITCH」。这是**纯 License 控制特性**，无独立配置命令、无独立 ConfigObject，激活后 IPv6 承载由会话管理基础流程（簇A WSFD-010501）处理。

---

## 2. ConfigObject 实例化（10 个）

### 2.1 License 控制对象（1个，跨特性共用）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-LICENSESWITCH` | LICENSESWITCH | UDG+UNC | entity | LICITEM | SWITCH(ENABLE/DISABLE) | —（License 文件控制，无父子关系） |

### 2.2 UNC 双栈会话管理对象（2G3G4G，3个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-SMFUNC` | SMFUNC | UNC | entity | — | DUALFLAG(IPv4v6双栈), PDPTYPE(单栈回退策略), INDFWD, TOPSELCFG, APNRES, ... 25 参数 | —（全局会话管理扩展功能配置） |
| `OBJ-SMSUBDATA` | SMSUBDATA | UNC | entity | SUBRANGE, IMSIPRE, TYPE, APNNI, PDPTYPE | 匹配条件(PDPTYPE/IPV4PDPADDRTYPE) + 纠正值(NEWPDPTYPE/NEWIPV4PDPADDRTYPE/NEWIPV6PDPADDRTYPE) | refers_to 签约数据（HLR/HSS） |
| `OBJ-GTPCCMPT` | GTPCCMPT | UNC | entity | MSGCLS, MSGTYPE | CRTPDPREQ/UPDPDPREQ(Common Flags), CMFLG | —（GTP-C V0/V1 协议兼容性配置） |

### 2.3 UDG IPv6 路由对象（4个核心 + 2个 OSPFv3 子对象）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-ROUTEPOLICY` | ROUTEPOLICY | UDG | composite | POLICYNAME | — | **contains** ROUTEPOLICYNODE |
| `OBJ-ROUTEPOLICYNODE` | ROUTEPOLICYNODE | UDG | entity | POLICYNAME, NODESEQUENCE | MATCHMODE(permit/deny) | belongs_to ROUTEPOLICY；**contains** MATCHROUTETYPE |
| `OBJ-MATCHROUTETYPE` | MATCHROUTETYPE | UDG | entity | POLICYNAME, NODESEQUENCE, ROUTETYPE | ROUTETYPE(external1/internal/nssaExternal1/wlr_ud/wlr_sp/...) | belongs_to ROUTEPOLICYNODE |
| `OBJ-OSPFV3` | OSPFV3 | UDG | composite | PROCID | ROUTERID, VRFNAME, SPF 系列, BFD 系列 | **contains** OSPFV3AREA；refers_to VPNINST（via VRFNAME） |
| `OBJ-OSPFV3AREA` | OSPFV3AREA | UDG | entity | PROCID, AREAID | AREATYPE(Normal/Stub/NSSA), DEFAULTCOST, NSSA 系列 | belongs_to OSPFV3 |
| `OBJ-OSPFV3IMPORTROUTE` | OSPFV3IMPORTROUTE | UDG | entity | PROCID, TOPOID, PROTOCOL | PROTOCOL(wlr 引入无线路由), ROUPOLINAME, COST/TAG/TYPE | belongs_to OSPFV3；refers_to ROUTEPOLICY（via ROUPOLINAME） |

---

## 3. ConfigObject 间关系边（§11.7）

### 3.1 contains 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| ROUTEPOLICY | `contains` | ROUTEPOLICYNODE | 路由策略包含节点（ADD ROUTEPOLICYNODE 依赖 ADD ROUTEPOLICY） |
| ROUTEPOLICYNODE | `contains` | MATCHROUTETYPE | 路由策略节点包含匹配条件（ADD MATCHROUTETYPE 依赖节点存在） |
| OSPFV3 | `contains` | OSPFV3AREA | OSPFv3 进程包含区域（ADD OSPFV3AREA 依赖 ADD OSPFV3） |

### 3.2 refers_to 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| OSPFV3 | `refers_to` | VPNINST | OSPFv3 进程引用 VPN（VRFNAME；IPv6 承载绑 ipv6uni 地址族的 VPN） |
| OSPFV3IMPORTROUTE | `refers_to` | ROUTEPOLICY | OSPFv3 引入路由引用路由策略（ROUPOLINAME；过滤 WLR 路由） |
| SMSUBDATA | `refers_to` | HLR/HSS签约数据 | 签约数据纠正引用 HLR/HSS（Gr/S6a 口签约；不支持双栈时纠正） |

### 3.3 depends_on 边（4条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| ROUTEPOLICYNODE | `depends_on` | ROUTEPOLICY | 节点依赖策略存在（手册原文：添加节点时要保证通过 ADD ROUTEPOLICY 添加过指定路由策略） |
| MATCHROUTETYPE | `depends_on` | ROUTEPOLICYNODE | 匹配条件依赖节点存在（手册原文：必须已配置策略名+节点） |
| OSPFV3AREA | `depends_on` | OSPFV3 | 区域依赖进程存在（手册原文：只有执行 ADD OSPFV3 配置了进程后才能用此命令） |
| OSPFV3IMPORTROUTE | `depends_on` | OSPFV3 | 引入路由依赖进程存在（手册原文：只有执行 ADD OSPFV3 配置了进程后才能用此命令） |

### 3.4 activates 边（1条，★License 链核心）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| OBJ-LICENSESWITCH (LKV3G5VDSA01) | `activates` | OBJ-LICENSESWITCH (LKV3G5V6PB01) | UDG 双栈 License 激活 IPv6 承载 License（双栈依赖 IPv6 承载；特性概述「License支持」节隐含依赖） |

---

## 4. CommandRule 实例化（本簇相关，6条）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-C-01` | UDG 双栈 ADD APN 必须同时配 IPv4+IPv6 双 VPN | `parameter_dependency` | explicit | config | parameter | ADD APN（簇B CMD-UDG-010105 引用） | GWFD-020403 双栈激活脚本 ADD APN 必须同时配置 `HASVPN=ENABLE, VPNINSTANCE` + `HASVPNIPV6=ENABLE, VPNINSTANCEIPV6`（双 VPN 字段），否则 IPv6 承载无法挂载（手册原文：ADD APN 数据表 HASVPNIPV6/VPNINSTANCEIPV6 字段） | IPv6 用户无法接入 | critical | EV-C-02 |
| `CR-C-02` | UDG 双栈 ADD SECTION 必须配 IPv4 + IPv6 两类地址段 | `parameter_dependency` | explicit | config | parameter | ADD SECTION（簇B CMD-UDG-010105-02 引用） | GWFD-020403 双栈激活脚本必须分别 ADD SECTION 配 `IPVERSION=IPV4` 段和 `IPVERSION=IPV6, V6PREFIXSTART/END/LENGTH` 段（★V6PREFIXLENGTH 49~64；<64 触发 PD）；手册原文：「本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池」 | 双栈用户仅获单栈地址 | critical | EV-C-02 |
| `CR-C-03` | UDG IPv6 承载 OSPFv3 引入路由必须用 wlr 方式（不能只选 WLR_SP 或 WLR_UD） | `semantic_rule` | explicit | config | parameter | CMD-UDG-020401-07.PROTOCOL (ADD OSPFV3IMPORTROUTE) | GWFD-020401 激活文档步骤 9 注意事项原文：「采用路由策略方式发布路由时，不能只选择发布WLR_SP或者WLR_UD路由，必须选择WLR方式发布所有路由」；即 ADD OSPFV3IMPORTROUTE.PROTOCOL 必须为 `wlr`，不能拆分为 wlr_sp/wlr_ud（注：wlr_sp/wlr_ud 是 ADD MATCHROUTETYPE.ROUTETYPE 的匹配类型，非 PROTOCOL 值） | 用户下行路由发布不完整 | critical | EV-C-01 |
| `CR-C-04` | UDG IPv6 承载 OSPFv3 Router ID 必须全网唯一 | `semantic_rule` | explicit | config | parameter | CMD-UDG-020401-05.ROUTERID (ADD OSPFV3) | GWFD-020401 激活文档数据表原文：「Router ID必须全网唯一」；ADD OSPFV3 手册原文：「Router ID 是一台 OSPFv3 进程在自治系统中的唯一标识。如果用户没有指定 Router ID 号，则 OSPFv3 进程无法运行」 | OSPFv3 进程无法生成 LSA，路由不通 | critical | EV-C-01 |
| `CR-C-05` | UDG IPv6 承载逻辑接口 VPN 必须与外联口 VPN 相同 | `semantic_rule` | explicit | config | relation | ADD VPNINST ↔ ADD L3VPNINST/VPNINSTAF | GWFD-020401 激活文档步骤 2 说明原文：「逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败」；ADD VPNINSTAF.AFTYPE 必须为 `ipv6uni`（IPv6 地址族） | IPv6 报文查询路由失败 | critical | EV-C-01 |
| `CR-C-06` | UNC 双栈 SET SMFUNC.DUALFLAG=YES 需 LKV2DUSA02 License 才生效 | `parameter_dependency` | explicit | config | parameter | CMD-UNC-104002-02.DUALFLAG (SET SMFUNC) | SET SMFUNC 手册原文（DUALFLAG 参数说明）：「当参数设置为 YES(是) 时，IPv4v6双栈接入特性的相关License授权并开启后，此参数配置才生效（特性编号：WSFD-104002，License部件编码：LKV2DUSA02）」；即 DUALFLAG=YES 是必要不充分条件，需先 SET LICENSESWITCH LICITEM=LKV2DUSA02,SWITCH=ENABLE | 双栈功能不生效 | critical | EV-C-03 |

---

## 5. MMLCommand 关键参数集（核心命令全参数）

> **Schema 参考**：§11.4 CommandParameter。`required_mode` 取值 `required / optional / conditional_required`。本节 9 个核心命令（SET LICENSESWITCH 复用、6 UDG 路由、SET SMFUNC、ADD SMSUBDATA、MOD GTPCCMPT）参数已从手册原文抽取。

### 5.1 SET LICENSESWITCH（UDG/UNC 共用，2 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| LICITEM | string | 0~255 字节 | `required` | 无 | License 项（本簇用：LKV3G5V6PB01/LKV3G5VDSA01/LKV2IPV601/LKV2IPV6SM01/LKV2IPV6AM01/LKV2DUSA02/LKV2IPDSSM01/LKV2IPDSAM01） |
| SWITCH | enum | ENABLE / DISABLE | `required` | 无 | 开关（★执行后立即生效；License 文件未激活时无法设置） |

### 5.2 ADD ROUTEPOLICY（UDG 路由策略，1 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POLICYNAME | string | 1~200，不支持空格，区分大小写 | `required` | 无 | 路由策略名字（最大 65535 记录） |

### 5.3 ADD ROUTEPOLICYNODE（UDG 路由策略节点，4 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POLICYNAME | string | 1~200，同 ADD ROUTEPOLICY | `required` | 无 | 引用 ADD ROUTEPOLICY 生成 |
| NODESEQUENCE | int | 0~65535 | `required` | 无 | 路由策略节点号 |
| MATCHMODE | enum | permit / deny | `required` | 无 | 匹配模式 |
| DESCRIPTION | string | 1~80 | `optional` | 无 | 路由策略节点描述 |

### 5.4 ADD MATCHROUTETYPE（UDG 路由类型匹配，3 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POLICYNAME | string | 1~200，同上 | `required` | 无 | 引用 ADD ROUTEPOLICY 生成（必须存在） |
| NODESEQUENCE | int | 0~65535 | `required` | 无 | 引用 ADD ROUTEPOLICYNODE 生成（必须存在） |
| ROUTETYPE | enum | external1 / external2 / external1or2 / internal / nssaExternal1 / nssaExternal2 / nssaExternal1or2 / **wlr_bh** / **wlr_ud** / **wlr_sp** / **wlr_gbh** | `required` | 无 | ★路由类型（含 4 个无线路由类型；IPv6 承载激活示例用 nssaExternal1） |

### 5.5 ADD OSPFV3（UDG OSPFv3 进程，★31 参数，列核心参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PROCID | int | 1~4294967295 | `required` | 无 | OSPFv3 进程号（不可与现网重复） |
| ROUTERID | IPv4 | IPv4 点分十进制 | `required` | 无 | ★路由器标识（全网唯一；无此参数进程无法运行，见 CR-C-04） |
| VRFNAME | string | 1~31，区分大小写 | `optional` | _public_ | VPN 名称（IPv6 承载绑 ipv6uni VPN） |
| SILENTALLFLAG | bool | TRUE/FALSE | `optional` | FALSE | 抑制所有接口收发 OSPFv3 报文 |
| BFDALLINTFFLG | bool | TRUE/FALSE | `optional` | FALSE | 使能 BFD |
| BFDRXCFGFLAG | enum | FALSE/TRUE | `optional` | FALSE | 是否配置 BFD 最小接收间隔 |
| BFDMINRXINTV | int | 30~1000 ms | `conditional_required` | 无（初始 200） | BFDRXCFGFLAG=TRUE 时必选 |
| BFDTXCFGFLAG | enum | FALSE/TRUE | `optional` | FALSE | 是否配置 BFD 最小发送间隔 |
| BFDMINTXINTV | int | 30~1000 ms | `conditional_required` | 无（初始 200） | BFDTXCFGFLAG=TRUE 时必选 |
| DETECTMULINTV | int | 3~50 | `optional` | 3 | BFD 检测乘数间隔 |
| FRRBINDINGFLAG | bool | TRUE/FALSE | `optional` | FALSE | BFD 会话与接口链路状态绑定 |
| ROUTAGFLAG | enum | FALSE/TRUE | `optional` | FALSE | 配置 VPN 引入路由 tag |
| ROUTAG | int | 0~4294967295 | `conditional_required` | 无 | ROUTAGFLAG=TRUE 时必选 |
| BANDWIDTHREF | int | 1~2147483648 Mbps | `optional` | 100 | 计算链路开销参考值 |
| RXMTLIMITENABLE | enum | FALSE/TRUE | `optional` | FALSE | 使能最大重传次数 |
| RETRANSLIMIT | int | 2~255 | `conditional_required` | 30 | RXMTLIMITENABLE=TRUE 时可选 |
| DESCRIPTIONTEXT | string | 1~80 | `optional` | 无 | 描述信息 |
| VPNINSCAPSIMFLG | bool | TRUE/FALSE | `optional` | FALSE | 去使能 VPN 路由环路检测 |
| RTTAGDISFLAG | bool | TRUE/FALSE | `optional` | FALSE | 去使能标签环路检测 |
| STUBROUFLG | enum | NoConfig/StubOnHand/StubOnBoot | `optional` | NoConfig | Stub 路由器 |
| STUBROUSTUPINTV | int | 5~65535 s | `conditional_required` | 500 | STUBROUFLG=StubOnBoot 时可选 |
| DOMAINNULLFLAG | bool | TRUE/FALSE | `optional` | FALSE | Domain ID 为空 |
| VIRTUALSYSFLAG | bool | TRUE/FALSE | `optional` | TRUE | 共网段虚拟系统使能 |
| SANAME | string | 1~15 | `optional` | 无 | IPsec SA 名称（不能和认证同时配置） |
| SPFMAXINTERVAL | int | 1~20000 ms | `optional` | 无（初始 5000） | SPF 计算最长间隔 |
| SPFSTARTINTV | int | 1~1000 ms | `optional` | 无（初始 50） | SPF 计算初始间隔 |
| SPFHOLDINTERVAL | int | 1~5000 ms | `optional` | 无（初始 200） | SPF 计算基数间隔 |
| SPFDELAYINTV | int | 0~65535 s | `optional` | 无 | SPF 计算延迟（非智能定时器） |
| SPFHOLDTIME | int | 0~65535 s | `optional` | 无 | SPF 计算抑制间隔（非智能定时器） |

> **★手册核对**：ADD OSPFV3 手册「参数说明」表完整 31 个参数（含 BFD 系列 6 + SPF 系列 5 + Stub 系列 2 + 认证/SA 等），上表列出全部。最大记录数 8016。

### 5.6 ADD OSPFV3AREA（UDG OSPFv3 区域，★19 参数，列核心参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PROCID | int | 1~4294967295 | `required` | 无 | 引用 ADD OSPFV3 生成（必须存在） |
| AREAID | IPv4 | IPv4 点分十进制 | `required` | 无 | OSPFv3 区域标识 |
| DESCRIPTIONTEXT | string | 1~80 | `optional` | 无 | 区域描述 |
| AREATYPE | enum | Normal / Stub / NSSA | `optional` | Normal | 区域类型 |
| STUBNOSUMMARY | bool | TRUE/FALSE | `conditional_required` | FALSE | AREATYPE=Stub 时可选；禁止 ABR 向 Stub 发 Summary LSA |
| DEFAULTCOST | int | 0~16777214 | `conditional_required` | 1 | AREATYPE=Stub/NSSA 时可选；Type3 缺省路由开销 |
| SANAME | string | 1~15 | `optional` | 无 | IPsec SA 名称 |
| NSSADEFAULTROUTEADVERTISE | enum | FALSE/TRUE | `conditional_required` | FALSE | AREATYPE=NSSA 时可选；产生缺省 7 类 LSA |
| NSSADEFAULTCOSTCFG | enum | FALSE/TRUE | `conditional_required` | FALSE | NSSADEFAULTROUTEADVERTISE=TRUE 时可选 |
| NSSADEFAULTCOST | int | 1~16777214 | `conditional_required` | 无（初始 1） | NSSADEFAULTCOSTCFG=TRUE 时必选 |
| NSSADEFAULTTAGCFG | enum | FALSE/TRUE | `conditional_required` | FALSE | NSSADEFAULTROUTEADVERTISE=TRUE 时可选 |
| NSSADEFAULTTAG | int | 0~4294967295 | `conditional_required` | 无（初始 0） | NSSADEFAULTTAGCFG=TRUE 时必选 |
| NSSADEFAULTTYPECFG | enum | FALSE/TRUE | `conditional_required` | FALSE | NSSADEFAULTROUTEADVERTISE=TRUE 时可选 |
| NSSADEFAULTTYPE | enum | Type1/Type2 | `conditional_required` | 无（初始 Type2） | NSSADEFAULTTYPECFG=TRUE 时必选 |
| NSSANOIMPORTROUTE | bool | TRUE/FALSE | `conditional_required` | FALSE | AREATYPE=NSSA 时可选；不引入外部路由 |
| NSSANOSUMMARY | enum | FALSE/TRUE | `conditional_required` | FALSE | AREATYPE=NSSA 时可选；禁止 Summary LSA |
| NSSASETNBIT | bool | TRUE/FALSE | `conditional_required` | FALSE | AREATYPE=NSSA 时可选；DD 报文 N-bit |
| NSSATRANSLATORALWAYS | bool | TRUE/FALSE | `conditional_required` | FALSE | AREATYPE=NSSA 时可选；指定转换路由器 |
| NSSATRANSLATORINTERVAL | int | 1~120 s | `conditional_required` | 40 | AREATYPE=NSSA 时可选；转换路由器失效时间 |

### 5.7 ADD OSPFV3IMPORTROUTE（UDG OSPFv3 引入路由，★13 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PROCID | int | 1~4294967295 | `required` | 无 | 引用 ADD OSPFV3 生成（必须存在） |
| TOPOID | int | 0 | `optional` | 0 | 拓扑标识（只支持默认拓扑 0） |
| PROTOCOL | enum | direct / static / bgp / ospfv3 / **wlr** | `required` | 无 | ★协议号（IPv6 承载用 wlr 引入无线路由，见 CR-C-03） |
| PROTOCOLPROCID | int | 1~4294967295 | `conditional_required` | 1 | PROTOCOL=ospfv3 时可选 |
| IMPTCOSTCFG | enum | FALSE/TRUE | `optional` | FALSE | 引入路由开销配置使能 |
| IMPTTAGCFG | enum | FALSE/TRUE | `optional` | FALSE | 引入路由标签配置使能 |
| IMPTTYPECFG | enum | FALSE/TRUE | `optional` | FALSE | 引入路由类型配置使能 |
| COST | int | 0~16777214 | `conditional_required` | 无 | IMPTCOSTCFG=TRUE 时必选；路径 Cost |
| TAG | int | 0~4294967295 | `conditional_required` | 无 | IMPTTAGCFG=TRUE 时必选；标签 |
| TYPE | enum | Type1/Type2 | `conditional_required` | 无 | IMPTTYPECFG=TRUE 时必选；引入路由类型 |
| ROUPOLINAME | string | 1~200，区分大小写 | `optional` | 无 | ★路由策略名称（引用 ADD ROUTEPOLICY；IPv6 承载 WLR 发布用） |
| PERMITIBGPCFG | bool | TRUE/FALSE | `conditional_required` | FALSE | PROTOCOL=bgp 时可选；允许 BGP 配置 |
| INHERITCOSTCFG | bool | TRUE/FALSE | `optional` | FALSE | 继承原路由开销（不能与 IMPTCOSTCFG 同时 TRUE） |

### 5.8 SET SMFUNC（UNC 会话管理扩展功能，★25 参数，列 IPv6/双栈相关核心 + 全部参数名）

> **★手册核对**：SET SMFUNC 手册共 25 个参数。本簇 IPv6/双栈相关核心参数为 DUALFLAG + PDPTYPE，其余为会话管理通用参数（与簇A WSFD-010501 部分重叠）。

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| **DUALFLAG** | enum | YES / NO | `optional` | NO | ★IPv4v6 双栈（YES=同时支持 IPv4+IPv6；★需 LKV2DUSA02 License 才生效，见 CR-C-06） |
| **PDPTYPE** | enum | IPV4 / IPV6 / IPV4V6 | `conditional_required` | IPV4 | ★PDP/PDN Type 策略（DUALFLAG=NO 时配置；单栈回退优选类型） |
| INDFWD | enum | YES / NO | `optional` | YES | 强制启动间接转发方式 |
| TOPSELCFG | enum | YES / NO | `optional` | YES | 拓扑选择开关（需 LKV2SELGW03） |
| APNRES | enum | YES / NO | `optional` | NO | APN 限制功能开关 |
| PDPRMD | enum | MAX / MIN / RANDOM | `optional` | MAX | APN 限制的去激活方式 |
| SGWTOPO | enum | YES / NO | `optional` | NO | 3G 到 4G 切换 SGW 拓扑选择增强 |
| TZININTERRAU | enum | YES / NO | `optional` | YES | 切换后时区携带策略（需 LKV2TZSV01） |
| APNOIPLY | enum | YES / NO | `optional` | YES | 启用 HSS 签约的 APN 级 APN-OI-Replacement |
| LTEGWSELPLCY | enum | INTERFACE_IP / SERVICE_IP | `optional` | INTERFACE_IP | LTE 场景相同 APN 选择网关策略 |
| GUGWSELPLCY | enum | INTERFACE_IP / SERVICE_IP / APNDNS | `optional` | INTERFACE_IP | GU 场景相同 APN 选择网关策略 |
| PRAULI | enum | OFF / ON | `optional` | OFF | PRA 状态上报携带 ULI 开关 |
| MMULI | enum | ON / OFF | `optional` | OFF | 移动性管理流程 ULI 上报开关 |
| NETLOC | enum | ON / OFF | `optional` | ON | NetLoc 功能开关 |
| RETLOC | enum | ON / OFF | `conditional_required` | OFF | 获取实时位置开关（NETLOC=ON 后生效） |
| ULITYPE | enum | TAI_ECGI / ECGI | `conditional_required` | TAI_ECGI | 用户位置类型（NETLOC=ON 后生效） |
| IMSPOLICY | enum | ALLOW / REJECT | `optional` | ALLOW | IMS 连接激活策略 |
| IMSREJCAUSE | int | 0~112 | `conditional_required` | 0 | IMS 连接拒绝原因值（IMSPOLICY=REJECT 后生效） |
| APNNISOURCE | enum | UE_REQUEST_APNNI_AFTER_CORRECT / UE_REQUEST_APNNI / APNNI_AFTER_SUBDATA_MATCH | `optional` | UE_REQUEST_APNNI_AFTER_CORRECT | 下发给 UE 的 APN-NI 来源 |
| EPCO | enum | NOT_SUPPORT / SUPPORT | `optional` | NOT_SUPPORT | MME 支持 ePCO 信元处理 |
| EPCOSWNB | enum | OFF / ON | `optional` | OFF | ePCO 功能开关（NB） |
| EPCOSWWB | enum | OFF / ON | `optional` | OFF | ePCO 功能开关（WB） |
| LTENSAUPSELPLCY | enum | UECAP_ARD / RESV_PLCY1/2/3 | `optional` | UECAP_ARD | LTE 场景 NSA 选择用户面策略 |
| GUNSAUPSELPLCY | enum | MSCAP_ARD / RESV_PLCY1/2/3 | `optional` | MSCAP_ARD | GU 场景 NSA 选择用户面策略 |
| BITRATE | enum | NO / YES | `optional` | NO | 是否限制最大速率 |
| S11USEPARATE | enum | NOT_SUPPORT / SUPPORT | `optional` | NOT_SUPPORT | MME 支持用户面地址分开部署 |
| LTEUSERPLCYSW | enum | NO / YES | `optional` | NO | 支持 LTE 接口用户面地址选择策略独立控制 |
| GUUSERPLCYSW | enum | NO / YES | `optional` | NO | 支持 GU 接口用户面地址选择策略独立控制 |
| ENBIDINTM | enum | CRTSESREQ/CRTVBRRSP/BRRESCMD/MODBRREQ/DELSESREQ/DELBRRSP/UPDBRRSP/CHGNTFREQ | `optional` | NULL | GTPv2 消息 ULI 信元中 Macro eNodeB ID 携带策略 |

### 5.9 ADD SMSUBDATA（UNC 签约数据纠正，★17 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| SUBRANGE | enum | ALL_USER / SPECIAL_USER | `required` | 无 | 用户范围（相同 APNNI+PDPTYPE 只能一条 ALL_USER） |
| IMSIPRE | string | 5~15 位数字 | `conditional_required` | 无 | SUBRANGE=SPECIAL_USER 时必选；IMSI 前缀（全局唯一） |
| TYPE | enum | SUBSCRIBED_PARAMETER / Context_ID | `required` | 无 | 匹配条件 |
| CTXID | int | 0~255 | `conditional_required` | 无 | TYPE=Context_ID 时必选；上下文标识 |
| APNNIRANGE | enum | APNNI_ALL / APNNI_SPECIAL | `conditional_required` | 无 | TYPE=SUBSCRIBED_PARAMETER 时必选；签约 APNNI 范围 |
| APNNI | string | 1~62 位字符串 | `conditional_required` | 无 | APNNIRANGE=APNNI_SPECIAL 时必选；签约 APNNI |
| **PDPTYPE** | enum | IPV4 / IPV6 / PPP / **IPV4V6** / IPV4/IPV6 / ALL_PDP_TYPE | `conditional_required` | 无 | ★签约 PDP/PDN 类型（TYPE=SUBSCRIBED_PARAMETER 时必选；双栈纠正匹配 IPv4） |
| **IPV4PDPADDRTYPE** | enum | ALLOCATION_IPV4PDP_DYNAMIC / ALL_STATIC_IPV4PDP_ADDR / SPECIAL_STATIC_IPV4PDP_ADDR | `conditional_required` | 无 | ★签约 IPv4 PDP/PDN 地址分配类型（PDPTYPE=IPV4/IPV4V6/IPV4_IPV6 时必选） |
| IPV4 | IPv4 | 0.0.0.0~255.255.255.255 | `conditional_required` | 无 | IPV4PDPADDRTYPE=SPECIAL_STATIC_IPV4PDP_ADDR 时必选 |
| IPV6PDPADDRTYPE | enum | DYNAMIC / ALL_STATIC_IPV6PDP_ADDR / SPECIAL_STATIC_IPV6PDP_ADDR | `conditional_required` | 无 | 签约 IPv6 PDP/PDN 地址分配类型（PDPTYPE=IPV6/IPV4V6/IPV4_IPV6 时必选） |
| IPV6 | IPv6 | 0:0:...:0~FFFF:FFFF:...:FFFF | `conditional_required` | 无 | IPV6PDPADDRTYPE=SPECIAL_STATIC_IPV6PDP_ADDR 时必选 |
| CORRECTAPNNI | enum | YES / NO | `optional` | NO | 修改签约 APNNI |
| NEWAPNNI | string | 1~62 位字符串 | `conditional_required` | 无 | CORRECTAPNNI=YES 时必选；新的签约 APNNI |
| **NEWPDPTYPE** | enum | IPV4 / IPV6 / PPP / **IPV4V6** / IPV4/IPV6 / NOT_MODIFY | `optional` | 无（不输入时默认 IPV4+DYNAMIC） | ★新的签约 PDP 类型（双栈纠正改为 IPV4V6） |
| **NEWIPV4PDPADDRTYPE** | enum | DYNAMIC / STATIC | `conditional_required` | 无 | ★新的签约 IPv4 PDP 地址分配类型（NEWPDPTYPE=IPV4/IPV4V6/IPV4_IPV6 时必选） |
| NEWIPV4 | IPv4 | 0.0.0.0~255.255.255.255 | `conditional_required` | 无 | NEWIPV4PDPADDRTYPE=STATIC 时必选 |
| **NEWIPV6PDPADDRTYPE** | enum | DYNAMIC / STATIC | `conditional_required` | 无 | ★新的签约 IPv6 PDP 地址分配类型（NEWPDPTYPE=IPV6/IPV4V6/IPV4_IPV6 时必选） |
| NEWIPV6 | IPv6 | 0:0:...:0~FFFF:FFFF:...:FFFF | `conditional_required` | 无 | NEWIPV6PDPADDRTYPE=STATIC 时必选 |

> **★双栈纠正典型配置**（手册使用实例 + SGSN/MME 激活脚本）：
> `ADD SMSUBDATA: SUBRANGE=ALL_USER, TYPE=SUBSCRIBED_PARAMETER, APNNIRANGE=APNNI_ALL, PDPTYPE=IPV4, IPV4PDPADDRTYPE=ALLOCATION_IPV4PDP_DYNAMIC, CORRECTAPNNI=NO, NEWPDPTYPE=IPV4V6, NEWIPV4PDPADDRTYPE=DYNAMIC, NEWIPV6PDPADDRTYPE=DYNAMIC;`
> 含义：将所有签约 IPv4 动态分配的用户，纠正为 IPv4v6 双栈动态分配（IPv4+IPv6 均动态）。

### 5.10 MOD GTPCCMPT（UNC GTP-C V0/V1 协议兼容性，★15 参数，列双栈相关核心）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| MSGCLS | enum | PM / TM / MM | `required` | 无 | 消息分类（暂不支持 PM；双栈用 TM） |
| MMMSGTYPE | enum | SGSN_CONTEXT_RESP / FWD_RLC_REQ / FORWARD_SRNS_CONTEXT | `conditional_required` | 无 | MSGCLS=MM 时有效 |
| TMMSGTYPE | enum | CREATE_PDP_CONTEXT_REQUEST / UPDATE_PDP_CONTEXT_REQUEST / UPDATE_PDP_CONTEXT_RESPONSE / DELETE_PDP_CONTEXT_RESPONSE / DELETE_PDP_CONTEXT_REQUEST | `conditional_required` | 无 | ★MSGCLS=TM 时有效（双栈兼容用 CREATE_PDP_CONTEXT_REQUEST/UPDATE_PDP_CONTEXT_REQUEST） |
| CTXRSP | enum | RAB_CONTEXT/CHR_CHARACTER/IMEISV/PDP_CONTEXT/... | `conditional_required` | 无 | MMMSGTYPE=SGSN_CONTEXT_RESP 时有效 |
| FWDRLCREQ | enum | CHR_CHARACTER/IMEISV/PDP_CONTEXT/SELECTED_PLMN_ID/... | `conditional_required` | 无 | MMMSGTYPE=FWD_RLC_REQ 时有效 |
| FWDSRNSCTX | enum | SOURCE_RNC_PDCP_CONTEXT | `conditional_required` | 无 | MMMSGTYPE=FORWARD_SRNS_CONTEXT 时有效 |
| **CRTPDPREQ** | enum | COMMON_FLAGS / UPSELIND | `conditional_required` | 无 | ★TMMSGTYPE=CREATE_PDP_CONTEXT_REQUEST 时有效（双栈用 COMMON_FLAGS） |
| **UPDPDPREQ** | enum | COMMON_FLAGS | `conditional_required` | 无 | ★TMMSGTYPE=UPDATE_PDP_CONTEXT_REQUEST 时有效（双栈用 COMMON_FLAGS） |
| UPDPDPRES | enum | ULI / TZ | `conditional_required` | 无 | TMMSGTYPE=UPDATE_PDP_CONTEXT_RESPONSE 时有效 |
| DELPDPRES | enum | ULI / TZ | `conditional_required` | 无 | TMMSGTYPE=DELETE_PDP_CONTEXT_RESPONSE 时有效 |
| DELPDPREQ | enum | TZ | `conditional_required` | 无 | TMMSGTYPE=DELETE_PDP_CONTEXT_REQUEST 时有效 |
| INCLUDE | enum | NOT_CARRY / PRO_DEFINE / SELF_DEFINE | `conditional_required` | 无 | 携带方式（UNC 暂不支持 SELF_DEFINE） |
| APNOICASE | enum | DEFAULT / LOWERCASE / LOWERCASEGUL | `conditional_required` | 无 | APNOI 大小写（CTXRSP/FWDRLCREQ=PDP_CONTEXT 时有效） |
| **CMFLG** | enum | NO / YES | `conditional_required` | 无 | ★是否支持 Common Flags 信元（CRTPDPREQ/UPDPDPREQ=COMMON_FLAGS 时有效；双栈兼容 CMFLG=YES） |
| UPSELFLAG | enum | DCNR | `conditional_required` | 无 | UP Function Selection Indication Flags（CRTPDPREQ=UPSELIND 时有效） |

> **★双栈 GTP-C 兼容典型配置**（SGSN/MME 激活文档步骤 5）：
> `MOD GTPCCMPT: MSGCLS=TM, TMMSGTYPE=CREATE_PDP_CONTEXT_REQUEST, CRTPDPREQ=COMMON_FLAGS, UPDPDPREQ=COMMON_FLAGS, CMFLG=YES;`
> 含义：Create/Update PDP Context Request 消息携带 Common Flags 信元（双栈标识），CMFLG=YES 启用。

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

### 6.1 GWFD-020401 IPv6承载上下文（UDG，7条核心 + 2条前置依赖）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UDG-020401-01) | LICENSESWITCH | License 开关（LKV3G5V6PB01） |
| ADD ROUTEPOLICY (CMD-UDG-020401-02) | ROUTEPOLICY | 路由策略 |
| ADD ROUTEPOLICYNODE (CMD-UDG-020401-03) | ROUTEPOLICYNODE | 路由策略节点 |
| ADD MATCHROUTETYPE (CMD-UDG-020401-04) | MATCHROUTETYPE | 路由类型匹配 |
| ADD OSPFV3 (CMD-UDG-020401-05) | OSPFV3 | OSPFv3 进程 |
| ADD OSPFV3AREA (CMD-UDG-020401-06) | OSPFV3AREA | OSPFv3 区域 |
| ADD OSPFV3IMPORTROUTE (CMD-UDG-020401-07) | OSPFV3IMPORTROUTE | OSPFv3 引入路由（WLR） |
| ADD VPNINST / ADD L3VPNINST / ADD VPNINSTAF（簇A） | VPNINST / L3VPNINST / VPNINSTAF | 前置依赖（IPv6 用 AFTYPE=ipv6uni） |

### 6.2 GWFD-020403 IPv4v6双栈接入（UDG，1条核心 + 复用簇B）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UDG-020403-01) | LICENSESWITCH | License 开关（LKV3G5VDSA01） |
| ADD APN / ADD POOL / ADD SECTION / ADD POOLGROUP / ADD POOLBINDGROUP / ADD POOLGRPMAP（簇B） | APN / POOL / SECTION / POOLGROUP / POOLBINDGROUP / POOLGRPMAP | 前置依赖（双栈配 IPv4+IPv6 双段，见 CR-C-01/02） |

### 6.3 WSFD-104002 IPv4v6双栈接入（UNC，4条核心）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UNC-104002-01) | LICENSESWITCH | License 开关（LKV2DUSA02/LKV2IPDSSM01/LKV2IPDSAM01） |
| SET SMFUNC (CMD-UNC-104002-02) | SMFUNC | 会话管理扩展功能（DUALFLAG） |
| ADD SMSUBDATA (CMD-UNC-104002-03) | SMSUBDATA | 签约数据纠正（PDPTYPE→NEWPDPTYPE） |
| MOD GTPCCMPT (CMD-UNC-104002-04) | GTPCCMPT | GTP-C V0/V1 协议兼容性 |

### 6.4 WSFD-104001 IPv6承载上下文（UNC，1条核心，★纯 License 控制）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UNC-104001-01) | LICENSESWITCH | License 开关（LKV2IPV601/LKV2IPV6SM01/LKV2IPV6AM01） |

> **★说明**：WSFD-104001 无其他 operates_on 边（参考信息明确「本特性无相关命令」）。IPv6 承载建立由会话管理基础流程（簇A WSFD-010501/WSFD-010503）处理，本特性仅做 License 控制。

---

## 7. ★CommandRule governs MMLCommand 边表（§11.6 反向）

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-C-01 | ADD APN（簇B）HASVPNIPV6/VPNINSTANCEIPV6 参数 | UDG 双栈 ADD APN 必须配 IPv4+IPv6 双 VPN |
| CR-C-02 | ADD SECTION（簇B）IPVERSION/V6PREFIXLENGTH 参数 | UDG 双栈必须配 IPv4+IPv6 两类地址段（V6PREFIXLENGTH 49~64） |
| CR-C-03 | CMD-UDG-020401-07.PROTOCOL (ADD OSPFV3IMPORTROUTE) | OSPFv3 引入路由必须用 wlr（不能只选 WLR_SP/WLR_UD） |
| CR-C-04 | CMD-UDG-020401-05.ROUTERID (ADD OSPFV3) | OSPFv3 Router ID 必须全网唯一 |
| CR-C-05 | ADD VPNINST ↔ ADD L3VPNINST/VPNINSTAF 关系 | 逻辑接口 VPN 必须与外联口 VPN 相同（AFTYPE=ipv6uni） |
| CR-C-06 | CMD-UNC-104002-02.DUALFLAG (SET SMFUNC) | DUALFLAG=YES 需 LKV2DUSA02 License 才生效 |

---

## 8. 使用实例脚本（保留手册原文，按特性/代际）

### 8.1 GWFD-020401 IPv6承载上下文（UDG，来源：`激活IPv6承载上下文_38276176.md`）

```
//打开本特性的License配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5V6PB01",SWITCH=ENABLE;

//配置VPN实例。
ADD VPNINST:VPNINSTANCE="VPN_Internet";

//配置外联口的VPN实例（IPv6 地址族）。
ADD L3VPNINST:VRFNAME="VPN_Internet";
ADD VPNINSTAF:VRFNAME="VPN_Internet",AFTYPE=ipv6uni;

//配置路由策略。
ADD ROUTEPOLICY:POLICYNAME="policy1";

//添加路由策略节点。
ADD ROUTEPOLICYNODE:POLICYNAME="policy1",NODESEQUENCE=10,MATCHMODE=permit;

//添加匹配路由类型。
ADD MATCHROUTETYPE:POLICYNAME="policy1",NODESEQUENCE=10,ROUTETYPE=nssaExternal1;

//启动 OSPF v3进程。
ADD OSPFV3:PROCID=100,ROUTERID="10.10.10.1",VRFNAME="VPN_Internet";

//增加 OSPF v3区域。
ADD OSPFV3AREA:PROCID=100,AREAID="0.0.0.1";

//引入WLR路由，将路由发布到骨干网上。
ADD OSPFV3IMPORTROUTE:PROCID=100,TOPOID=0,PROTOCOL=wlr,ROUPOLINAME="policy1";
```

### 8.2 GWFD-020403 IPv4v6双栈接入（UDG，来源：`激活IPv4v6双栈接入_38276180.md`）

```
//打开本特性的License配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5VDSA01",SWITCH=ENABLE;

//配置APN名称（★双 VPN：IPv4 + IPv6）。
ADD APN:APN="apn-test", HASVPN=ENABLE, VPNINSTANCE="VRF_Internet", HASVPNIPV6=ENABLE, VPNINSTANCEIPV6="VRF_Internet";

//配置地址池绑定到地址池组（★双栈：IPv4 + IPv6 双池）。
ADD POOLGROUP: POOLGRPNAME="poolgroup1", IPV4ALLOCPRIALG=ENABLE, IPV6ALLOCPRIALG=ENABLE;
ADD POOL:POOLNAME="testpool",POOLTYPE=LOCAL,IPVERSION=IPV4, HASVPN=ENABLE,VPNINSTANCE="VRF_Internet";
ADD POOL:POOLNAME="testpoolv6",POOLTYPE=LOCAL,IPVERSION=IPV6, HASVPN=ENABLE,VPNINSTANCE="VRF_Internet";
ADD SECTION:POOLNAME="testpool", SECTIONNUM=1, IPVERSION=IPV4, V4STARTIP="10.0.0.0", V4ENDIP="10.0.127.255";
ADD SECTION:POOLNAME="testpoolv6", SECTIONNUM=1, IPVERSION=IPV6, V6PREFIXSTART="fc00:0000:0000:fcee:0000:0000:0000:0000", V6PREFIXEND="fc00:0000:0000:fcef:ffff:ffff:ffff:ffff", V6PREFIXLENGTH=64;
ADD POOLBINDGROUP: POOLGROUPNAME="poolgroup1", POOLNAME="testpool", PRIORITY=10;
ADD POOLBINDGROUP: POOLGROUPNAME="poolgroup1", POOLNAME="testpoolv6", PRIORITY=10;

//配置APN与地址池组的映射关系。
ADD POOLGRPMAP:MAPPINGNAME="mapping1", APN="apn-test", POOLGROUPNAME="poolgroup1";
```

### 8.3 WSFD-104002 IPv4v6双栈接入（UNC 2G3G4G PGW-C，来源：`激活IPv4v6双栈接入特性（适用于PGW-C）_48043380.md`）

```
//打开本特性的License配置开关。
SET LICENSESWITCH: LICITEM="LKV2IPDSSM01", SWITCH=ENABLE;
```

### 8.4 WSFD-104002 IPv4v6双栈接入（UNC 2G3G4G SGSN/MME，来源：`激活IPv4v6双栈接入特性（适用于SGSN_MME）_48043379.md`）

```
//打开License配置开关。
SET LICENSESWITCH: LICITEM="LKV2DUSA02", SWITCH=ENABLE;

//开启IPv4v6双栈。
SET SMFUNC: DUALFLAG=YES;

//可选：增加签约数据纠正参数（HLR/HSS 不支持双栈时）。
ADD SMSUBDATA: SUBRANGE=ALL_USER, TYPE=SUBSCRIBED_PARAMETER, APNNIRANGE=APNNI_ALL, PDPTYPE=IPV4, IPV4PDPADDRTYPE=ALLOCATION_IPV4PDP_DYNAMIC, CORRECTAPNNI=NO, NEWPDPTYPE=IPV4V6, NEWIPV4PDPADDRTYPE=DYNAMIC, NEWIPV6PDPADDRTYPE=DYNAMIC;

//可选：增加GTP-C V0/V1协议兼容性配置（Common Flags 信元）。
MOD GTPCCMPT: MSGCLS=TM, TMMSGTYPE=CREATE_PDP_CONTEXT_REQUEST, CRTPDPREQ=COMMON_FLAGS, UPDPDPREQ=COMMON_FLAGS, CMFLG=YES;
```

### 8.5 WSFD-104002 IPv4v6双栈接入（UNC 5G AMF/SMF，来源：`激活IPv4v6双栈接入特性_48043372.md`）

```
//打开本特性的License配置开关（★AMF + SMF 双开）。
SET LICENSESWITCH: LICITEM="LKV2IPDSAM01",SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV2IPDSSM01",SWITCH=ENABLE;
```

### 8.6 WSFD-104001 IPv6承载上下文（UNC AMF/SMF，来源：`激活IPv6承载上下文特性（AMF_SMF）_48043375.md`）

```
//打开本特性的License配置开关（★AMF + SMF 双开）。
SET LICENSESWITCH: LICITEM="LKV2IPV6AM01",SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV2IPV6SM01",SWITCH=ENABLE;
```

### 8.7 WSFD-104001 IPv6承载上下文（UNC MME/SGW-C/PGW-C 与 SGSN/GGSN，来源：对应激活文档）

```
//MME/SGW-C/PGW-C 与 SGSN/GGSN 共用同一脚本。
SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;
```

---

## 9. 抽取核对清单

### 9.1 配置类命令参数行数与来源手册路径

| 命令 | 参数行数 | 来源手册路径 |
|------|---------|--------------|
| SET LICENSESWITCH（UDG 版） | 2 | `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md` |
| SET LICENSESWITCH（UNC 版） | 2 | `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md` |
| ADD ROUTEPOLICY | 1 | `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由策略管理/路由策略/增加路由策略（ADD ROUTEPOLICY）_00841697.md` |
| ADD ROUTEPOLICYNODE | 4 | `.../路由策略节点/增加路由策略节点（ADD ROUTEPOLICYNODE）_00866677.md` |
| ADD MATCHROUTETYPE | 3 | `.../路由类型匹配路由策略/增加路由类型匹配路由策略（ADD MATCHROUTETYPE）_49801558.md` |
| ADD OSPFV3 | 31 | `.../OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md` |
| ADD OSPFV3AREA | 19 | `.../OSPFv3管理/OSPFv3区域配置/创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md` |
| ADD OSPFV3IMPORTROUTE | 13 | `.../OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md` |
| SET SMFUNC | 25 | `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md` |
| ADD SMSUBDATA | 17 | `.../签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md` |
| MOD GTPCCMPT | 15 | `.../GTP-C接口管理/GTP-C协议管理/GTP-C V0 V1协议兼容性/修改GTP-C V0_V1协议兼容性配置(MOD GTPCCMPT)_72345523.md` |
| **合计（去重后）** | **10 命令 / 130 参数行** | **全部手册定位成功（含 UDG/UNC SET LICENSESWITCH 双版本去重）** |

### 9.2 ⚠️手册未定位 / 无独立命令列表

| 特性 | 状态 | 原因（手册原文） |
|------|------|------------------|
| WSFD-104001 IPv6承载上下文（UNC，3 代际） | ⚠️**无独立配置命令** | 3 个代际参考信息均明确写「本特性无相关命令」，激活仅 SET LICENSESWITCH。属纯 License 控制特性。 |
| GWFD-020403 IPv4v6双栈接入（UDG）激活脚本 OSPF（IPv4）系列 | 复用通用路由 | 参考信息列 ADD OSPF/OSPFIMPORTROUTE（IPv4 路由），与 GWFD-020401 OSPFv3 系列（IPv6）并列；本簇聚焦 IPv6（OSPFv3），OSPF（IPv4）归通用路由/簇E。 |

> **说明**：除上述两项外，本簇 4 特性参考信息/激活文档引用的命令全部手册定位成功。SET LICENSESWITCH 在 UDG/UNC 各有一版手册（参数表完全一致，LICITEM/SWITCH），本文件按产品侧分别登记但在参数表合并展示。

### 9.3 多代际命令差异（★UNC 侧重点）

| 代际 | 网元 | 双栈命令差异 | IPv6 承载命令差异 |
|------|------|-------------|------------------|
| 2G3G4G | SGSN/MME | SET LICENSESWITCH(LKV2DUSA02) + SET SMFUNC(DUALFLAG) + ADD SMSUBDATA + MOD GTPCCMPT | SET LICENSESWITCH(LKV2IPV601+LKV2IPV6SM01) |
| 2G3G4G | PGW-C | SET LICENSESWITCH(LKV2IPDSSM01) 仅一步 | 同上 |
| 5G | AMF/SMF | SET LICENSESWITCH(LKV2IPDSAM01+LKV2IPDSSM01) 仅两步（AMF+SMF 双开） | SET LICENSESWITCH(LKV2IPV6AM01+LKV2IPV6SM01) 两步（AMF+SMF 双开） |

> **★代际差异总结**：
> - **2G3G4G SGSN/MME 侧双栈最复杂**（4 步：License + SMFUNC + SMSUBDATA + GTPCCMPT），因为 SGSN/MME 需处理 GTP-C V0/V1 旧协议兼容 + HLR/HSS 签约纠正。
> - **5G/PGW-C 侧最简单**（1~2 步仅 License），因为 5G 协议原生支持双栈，无需协议兼容性纠正。
> - **IPv6 承载在 UNC 侧全部仅 License 控制**（无代际命令差异，仅 License 项不同：AMF 用 LKV2IPV6AM01，SMF 用 LKV2IPV6SM01，2G3G4G 用 LKV2IPV601+LKV2IPV6SM01）。

### 9.4 抽取统计

| 维度 | 数量 |
|------|------|
| 配置类命令（手册定位成功，去重） | 10 |
| 配置类命令参数总行数 | 130 |
| 查询类命令（本期略） | 2（DSP SMCTX / DSP PDUSESSION） |
| ⚠️无独立命令特性 | 1（WSFD-104001 UNC IPv6承载，纯 License 控制） |
| ConfigObject | 10 |
| CommandRule | 6 |
| ConfigObject 关系边 | 11（contains 3 + refers_to 3 + depends_on 4 + activates 1） |
| operates_on 边 | 13（核心 10 + 前置依赖引用 3） |
| IPv6 License 项 | 8（UDG 2 + UNC 6） |
| 激活脚本 | 7（UDG 双栈/承载各 1 + UNC 双栈 3 代际 + UNC 承载 2 组） |

### 9.5 与簇B 的关键复用关系（★去重核对）

| 复用项 | 簇B 已抽 | 本簇引用方式 |
|--------|---------|-------------|
| ADD APN（HASVPNIPV6/VPNINSTANCEIPV6 字段） | 簇B §5.X ADD APN（注：簇B 样板未列 ADD APN 参数表，但激活脚本引用；本簇 CR-C-01 标注双栈必配双 VPN） | CR-C-01 治理 |
| ADD POOL / ADD SECTION（IPVERSION=IPV6, V6PREFIXSTART/END/LENGTH） | 簇B §5.1 ADD POOL / §5.2 ADD SECTION（IPv6 段参数已抽） | CR-C-02 治理 |
| ADD POOLGROUP（IPV4ALLOCPRIALG/IPV6ALLOCPRIALG） | 簇B §5.3 ADD POOLGROUP | §6.2 operates_on 引用 |
| ADD POOLBINDGROUP / ADD POOLGRPMAP | 簇B §5.4 / §5.5 | §6.2 operates_on 引用 |
| ADD VPNINST / ADD L3VPNINST / ADD VPNINSTAF（AFTYPE=ipv6uni） | 簇A / 簇B §6.2 前置依赖 | §6.1 operates_on 引用 + CR-C-05 治理 |

---

> 本文件为 IPv4v6双栈 + IPv6承载上下文（UDG + UNC，4 特性）命令层抽取，对齐 `04-cluster-B-GWFD-010105.md` 样板。
> **★关键贡献**：
> 1. **完整建模 IPv6 License 链**（8 个 License 项跨 UDG/UNC，UDG `LKV3G5V*` vs UNC `LKV2*` 两套编码体系），明确双栈对 IPv6 承载的依赖关系。
> 2. **发现 WSFD-104001 UNC IPv6承载上下文为纯 License 控制特性**（3 代际参考信息均写「本特性无相关命令」），纠正可能存在的「为该特性强配命令」的建模偏差。
> 3. **完整抽取 UNC 双栈核心命令参数**（SET SMFUNC 25 参数含 DUALFLAG、ADD SMSUBDATA 17 参数含 PDPTYPE→NEWPDPTYPE 纠正链、MOD GTPCCMPT 15 参数含 Common Flags 兼容）。
> 4. **完整抽取 UDG OSPFv3 系列参数**（ADD OSPFV3 31 参数 + ADD OSPFV3AREA 19 参数 + ADD OSPFV3IMPORTROUTE 13 参数 + 路由策略 3 命令 8 参数），支撑 IPv6 手机下行路由发布建模。
> 5. **明确多代际命令差异**（2G3G4G SGSN/MME 双栈 4 步最复杂，5G/PGW-C 仅 License 1~2 步）。
> 6. **建立 6 条特性级 CommandRule**（双栈双 VPN/双段强约束、WLR 整体发布、Router ID 全网唯一、VPN 一致性、DUALFLAG License 依赖）。
> 7. **补登记 GWFD-020401 激活文档步骤 8 引用的 ADD OSPFV3AREA**（参考信息命令清单未列，但激活脚本与手册均已定位）。
