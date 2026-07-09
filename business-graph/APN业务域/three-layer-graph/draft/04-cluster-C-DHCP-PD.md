# APN 业务域命令图谱 · 簇C-DHCP/PD：WSFD-104413 DHCP功能 / WSFD-104005 DHCPv6地址分配 / GWFD-020406 IPv6 Prefix Delegation(UDG) / WSFD-104004 IPv6前缀代理(UNC)

> **文件定位**：`three-layer-graph/draft/04-cluster-C-DHCP-PD.md`
> **特性范围**：4 个特性
> - **WSFD-104413 DHCP功能（UNC, SMF/PGW-C/GGSN）**：UNC 作为 DHCPv4 Client，从外置 DHCP Server 获取 IPv4 地址/DNS/P-CSCF 分配给用户。License=LKV3W9DHCP12
> - **WSFD-104005 DHCPv6地址分配（UNC, SMF/PGW-C/GGSN）**：UNC 作为 DHCPv6 Client，从外置 DHCPv6 Server 获取 IPv6 地址/DNS/P-CSCF。License=LKV3W9V6AA11
> - **GWFD-020406 IPv6 Prefix Delegation（UDG, PGW-U/UPF）**：UDG 为用户分配携带 IPv6 地址前缀长度（49~63）的 IPv6 地址，使 MS/UE 作为无线移动路由器。License=LKV3G5P6PD01
> - **WSFD-104004 IPv6前缀代理（UNC, SMF/PGW-C/GGSN）**：UNC 本地地址池或 RADIUS 方式分配 IPv6 delegated-prefix。License=LKV3W9V6PD11
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **结构对齐**：严格 follow 样板 `04-cluster-B-GWFD-010105.md`（9 节结构、表格列、CMD-<NF>-<featureid>-xx 编号）
> **数据来源**：4 个特性的特性概述/参考信息 + 激活文档（DHCP/DHCPv6 文档缺口，见 §9.2）+ 5 个 DHCP 专属 MML 手册 + ADD ADDRPOOL（UNC）手册（路径见 §抽取核对清单）
> **铁律**：命令/参数 100% 来自原始产品文档原文，零编造。手册未定位的命令标注「⚠️手册未定位」。DHCP/DHCPv6 文档缺口（无激活脚本）在 §8/§9 显式标注 draft。

---

## 0. 命令清单总览（簇C 4 个特性用到的全部命令）

### 0.1 按命令类型分布

| 类型 | 命令数 | 命令清单 |
|------|-------|---------|
| DHCP 专属配置类（ADD/SET，UNC） | 5 | ADD DHCPSERVERGRP、ADD DHCPSERVER、ADD DHCPBINDPOOLGRP、ADD AGENTIP、SET DHCPPARAREQ |
| 跨簇引用配置类（非本簇首次拥有，在簇A/B 已抽取） | 6 | ADD ADDRPOOL（簇B，UNC 地址池）、ADD APN（簇A）、SET APNADDRESSATTR（簇B）、SET IPALLOCRULE（簇B）、MOD APN（簇A）、ADD VPNINST（簇A） |
| UDG PD 场景地址池配置类（簇B 已抽取，PD 通过参数触发） | 5 | ADD POOL、ADD SECTION、ADD POOLGROUP、ADD POOLBINDGROUP、ADD POOLGRPMAP（均簇B，PD 无专属命令，由 ADD SECTION.V6PREFIXLENGTH<64 触发） |
| UDG PD 路由配置类（IPv6 下行路由，引用簇E） | 4 | ADD OSPFV3、ADD OSPFV3AREA、ADD OSPFV3INTERFACE、ADD OSPFV3IMPORTROUTE（IPv6 OSPFv3 路由，与簇E IPv4 OSPF 并列，本文件登记为引用） |
| 维护类（RMV/LST/MOD，本期略） | 多 | 参考/激活文档列出 RMV/LST 系列（DHCP RMV 系列、ADDRPOOL MOD/LST、APN MOD/LST、VPNINST LST 等），本期不抽参数 |

> **说明**：DHCP/DHCPv6 两个特性的参考信息命令清单**完全相同**（ADD VPNINST/ADDRPOOL/AGENTIP/DHCPSERVERGRP/DHCPSERVER/DHCPBINDPOOLGRP/APN + SET APNADDRESSATTR/IPALLOCRULE + SET DHCPPARAREQ），区别仅在适用 IP 类型（V4/V6）与 License。SET DHCPPARAREQ 仅在特性概述正文引用（参考信息命令清单未单列），手册已定位。
> **PD 关键点**：UDG/UNC 的 IPv6 前缀代理**无 PD 专属命令**——UDG 通过 ADD SECTION.V6PREFIXLENGTH 取 49~63（<64）触发 PD；UNC 通过 ADD ADDRPOOL(IPv6)+SET APNADDRESSATTR.IPV6ALLOCTYPE=LOCAL 触发本地前缀代理，或 Radius 方式触发。PD 的"命令"实为现有地址池/APN 属性命令的特定取值组合。

### 0.2 ConfigObject 分布（本簇涉及）

| 功能域 | 对象数 | 关键对象 | 所属 |
|-------|-------|---------|------|
| DHCP 服务器体系 | 4 | DHCPSERVERGRP、DHCPSERVER、DHCPBINDPOOLGRP、AGENTIP | UNC（WSFD-104413/104005） |
| DHCP 请求信元 | 1 | DHCPPARAREQ | UNC（WSFD-104413/104005） |
| 地址池（引用簇B） | 2 | ADDRPOOL（UNC）、POOL（UDG） | 簇B |
| APN 地址分配属性（引用簇B） | 1 | APNADDRESSATTR | 簇B（SET APNADDRESSATTR.IPV6ALLOCTYPE=LOCAL 触发 PD-UNC） |
| IPv6 路由（引用簇E） | 1 | OSPFV3 | 簇E（PD-UDG 下行路由） |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1 所有 MMLCommand。
> **声明**：本文件 §1 所有 MMLCommand 的 `status` 字段值均为 `active`（Schema §11.3 MMLCommand.status 必备）。簇C 所有正式命令均处于启用状态。
> **依据**：所有命令均在产品文档正式登记，无 `deprecated` 或 `planned` 状态。

---

## 1. MMLCommand 实例化（簇C，5 个 DHCP 专属配置命令 + 跨簇引用登记）

### 1.1 DHCP 服务器体系（UNC，4个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-104413-01` | `ADD DHCPSERVERGRP` | ADD | DHCPSERVERGRP | ★UNC DHCP 服务器组（IPVERSION IPV4/IPV6；REQLEASETIME 租约 0/16~192 小时；RETRYINTVAL 超时重发 1~10s；RETRYTIMES 重发 0~5；HASVPN 绑 VPN；最多 1000 记录） | GROUPNAME, IPVERSION(IPV4/IPV6), REQLEASETIME, RETRYINTVAL, RETRYTIMES, HASVPN, VPNINSTANCE | EV-CD-01（DHCP 手册）|
| `CMD-UNC-104413-02` | `ADD DHCPSERVER` | ADD | DHCPSERVER | ★DHCP 服务器 IP（一主一备，必须先主后备；ISPRIMARY；IPVERSION；V4IPADDRESS/V6IPADDRESS；★同组主备 IPv4 不可相同、IPv6 子网前缀不可相同；WALVALUE 整机每秒最大消息数；最多 2000 记录） | GROUPNAME, ISPRIMARY, IPVERSION(IPV4/IPV6), V4IPADDRESS, V6IPADDRESS, WALVALUE | EV-CD-01 |
| `CMD-UNC-104413-03` | `ADD DHCPBINDPOOLGRP` | ADD | DHCPBINDPOOLGRP | ★远端地址池组与 DHCP 服务器组绑定（POOLGRPNAME 引用 ADD ADDRPOOLGRP；GROUPNAME 引用 ADD DHCPSERVERGRP；★每个远端地址池组最多绑一个 DHCP 服务器组；一个 DHCP 服务器组可被多个远端地址池组绑定；修改需先 RMV；最多 6000 记录） | POOLGRPNAME, GROUPNAME | EV-CD-01 |
| `CMD-UNC-104413-04` | `ADD AGENTIP` | ADD | AGENTIP | ★远端地址池代理 IP（DHCP Server 按代理 IP 找同网段地址池分配；SECTIONNUM 0~63/65535；IPVERSION；V4AGENTIP 仅 ABC 类/V6AGENTIP 非组播链路本地环回；★SECTIONNUM=65535 表示无效→主机路由发布；前置：先 ADD ADDRPOOL；最多 6000 记录） | POOLNAME, SECTIONNUM, IPVERSION(IPV4/IPV6), V4AGENTIP, V6AGENTIP | EV-CD-01 |

### 1.2 DHCP 请求信元（UNC，1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-104413-05` | `SET DHCPPARAREQ` | SET | DHCPPARAREQ | ★DHCPv4/v6 请求信元参数（V4/V6 DNS + V4/V6 P-CSCF 四开关；★初始记录 V4DNSSERVER=ENABLE, V4PCSCFSERVER=DISABLE, V6DNSSERVER=ENABLE, V6PCSCFSERVER=DISABLE；不输入保持当前配置） | V4DNSSERVER, V4PCSCFSERVER, V6DNSSERVER, V6PCSCFSERVER | EV-CD-01 |

### 1.3 跨簇引用命令（非本簇首次拥有，登记 operates_on 边，不重复抽参数）

| `command_id` | `command_name` | `verb` | `object_keyword` | 本簇用法 | 归属 |
|--------------|----------------|--------|------------------|----------|------|
| `CMD-UNC-B-ADDRPOOL` | `ADD ADDRPOOL` | ADD | ADDRPOOL | ★DHCP: POOLTYPE=DHCP 创建远端地址池；★PD-UNC: IPVERSION=IPv6 + POOLTYPE=Local 创建 IPv6 前缀代理地址池（簇B 已抽全参数） | 簇B |
| `CMD-UNC-B-APNADDRATTR` | `SET APNADDRESSATTR` | SET | APNADDRESSATTR | ★DHCP: 使能 SUPPORTIPV4/V6；★PD-UNC: IPV6ALLOCTYPE=LOCAL 触发本地 IPv6 前缀代理（簇B 已抽全参数） | 簇B |
| `CMD-UNC-B-IPALLOCRULE` | `SET IPALLOCRULE` | SET | IPALLOCRULE | DHCP 地址分配规则（簇B 已抽全参数） | 簇B |
| `CMD-UDG-B-POOL` | `ADD POOL` | ADD | POOL | ★PD-UDG: POOLTYPE=EXTERNAL + IPVERSION=IPV6 + HASVPN=ENABLE + CHECKIPVALID=ENABLE 创建 PD 外部地址池（簇B 已抽全参数） | 簇B |
| `CMD-UDG-B-SECTION` | `ADD SECTION` | ADD | SECTION | ★PD-UDG 触发关键：V6PREFIXLENGTH 取 49~63（<64）→ 该地址池采用 IPv6 Prefix Delegation 方式分配（簇B 已抽全参数） | 簇B |
| `CMD-UDG-B-POOLGRPMAP` | `ADD POOLGRPMAP` | ADD | POOLGRPMAP | PD-UDG 池组映射（簇B 已抽全参数） | 簇B |

---

## 2. ConfigObject 实例化（本簇新对象 5 个 + 引用 3 个）

### 2.1 DHCP 服务器体系（UNC，4个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-DHCPSERVERGRP` | DHCPSERVERGRP | UNC | composite | GROUPNAME | IPVERSION, REQLEASETIME, RETRYINTVAL, RETRYTIMES, HASVPN, VPNINSTANCE | **contains** DHCPSERVER（一主一备）；refers_to VPNINST |
| `OBJ-DHCPSERVER` | DHCPSERVER | UNC | entity | GROUPNAME, ISPRIMARY, IPVERSION | V4IPADDRESS/V6IPADDRESS, WALVALUE | belongs_to DHCPSERVERGRP |
| `OBJ-DHCPBINDPOOLGRP` | DHCPBINDPOOLGRP | UNC | binding | POOLGRPNAME, GROUPNAME | — | links ADDRPOOLGRP to DHCPSERVERGRP（每远端池组最多绑一个 DHCP 组） |
| `OBJ-AGENTIP` | AGENTIP | UNC | entity | POOLNAME, IPVERSION | SECTIONNUM(0~63/65535), V4AGENTIP/V6AGENTIP | belongs_to ADDRPOOL（远端地址池代理 IP） |

### 2.2 DHCP 请求信元（UNC，1个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-DHCPPARAREQ` | DHCPPARAREQ | UNC | entity | — | V4DNSSERVER, V4PCSCFSERVER, V6DNSSERVER, V6PCSCFSERVER | —（全局 DHCP 请求信元参数） |

### 2.3 跨簇引用对象（不重复建模）

| `object_id` | `object_name` | `product_side` | `object_kind` | 本簇用法 | 归属 |
|-------------|---------------|----------------|---------------|----------|------|
| `OBJ-ADDRPOOL-U` | ADDRPOOL | UNC | entity | DHCP: POOLTYPE=DHCP；PD-UNC: IPVERSION=IPv6 | 簇B |
| `OBJ-APNADDRESSATTR-U` | APNADDRESSATTR | UNC | entity | PD-UNC: IPV6ALLOCTYPE=LOCAL 触发 | 簇B |
| `OBJ-POOL-U` | POOL | UDG | entity | PD-UDG: POOLTYPE=EXTERNAL + IPv6 | 簇B |
| `OBJ-OSPFV3` | OSPFV3 | UDG | composite | PD-UDG 下行 IPv6 路由 | 簇E |

---

## 3. ConfigObject 间关系边（§11.7）

### 3.1 contains 边（1条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| DHCPSERVERGRP | `contains` | DHCPSERVER | DHCP 服务器组包含 DHCP 服务器（一主一备；必须先主后备） |

### 3.2 refers_to 边（2条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| DHCPSERVERGRP | `refers_to` | VPNINST | DHCP 服务器组绑定 VPN（HASVPN=ENABLE；与 ADDRPOOL VPN 一致） |
| AGENTIP | `refers_to` | ADDRPOOL | 代理 IP 引用远端地址池（前置：先 ADD ADDRPOOL） |

### 3.3 links 边（1条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| DHCPBINDPOOLGRP | `links` | ADDRPOOLGRP ↔ DHCPSERVERGRP | 远端地址池组与 DHCP 服务器组绑定（每远端池组最多绑一个 DHCP 组；一个 DHCP 组可被多远端池组绑） |

### 3.4 depends_on 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| DHCPSERVER | `depends_on` | DHCPSERVERGRP | DHCP 服务器依赖服务器组存在（手册原文：先 ADD DHCPSERVERGRP） |
| DHCPBINDPOOLGRP | `depends_on` | DHCPSERVER + ADDRPOOLGRP | 绑定关系依赖 DHCP 服务器与远端地址池组均存在（手册原文：使用前必须 ADD DHCPSERVER） |
| AGENTIP | `depends_on` | ADDRPOOL | 代理 IP 依赖远端地址池存在（手册原文：配置代理 IP 前先 ADD ADDRPOOL） |

---

## 4. CommandRule 实例化（本簇相关，5条）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-CD-01` | ADD DHCPSERVER 主备服务器 IP 不可相同 | `semantic_rule` | explicit | config | parameter | CMD-UNC-104413-02 (ADD DHCPSERVER) V4IPADDRESS/V6IPADDRESS | 同一 DHCP 服务器组下的主、备 DHCP 服务器：IPv4 地址不能相同；IPv6 子网前缀不能相同（手册原文强约束）。且必须先配置主 DHCP 服务器（ISPRIMARY=ENABLE），后配置备 DHCP 服务器 | 主备 IP 相同导致 DHCP 服务器配置冲突 | critical | EV-CD-01 |
| `CR-CD-02` | DHCP 服务器组/地址池 VPN 必须一致 | `semantic_rule` | explicit | config | relation | OBJ-DHCPSERVERGRP ↔ OBJ-ADDRPOOL-U | ADD DHCPSERVERGRP 的 VPNINSTANCE 必须与 ADD ADDRPOOL 的 VPNINSTANCE 一致（DHCP 场景地址池与服务器组同 VPN；手册原文 ADD DHCPSERVERGRP.HASVPN/VPNINSTANCE 引用 ADD VPNINST） | VPN 不一致导致 DHCP 地址分配失败 | critical | EV-CD-01 |
| `CR-CD-03` | ADD DHCPBINDPOOLGRP 远端池组最多绑一个 DHCP 组 | `cardinality_rule` | explicit | config | relation | OBJ-DHCPBINDPOOLGRP | 每个远端地址池组最多可以绑定一个 DHCP 服务器组；一个 DHCP 服务器组可以被多个远端地址池组绑定。修改需先 RMV DHCPBINDPOOLGRP 删除原关联，再 ADD 关联新组（手册原文） | 违反基数导致绑定失败 | warning | EV-CD-01 |
| `CR-CD-04` | SET DHCPPARAREQ 初始记录与 DNS/P-CSCF 获取 | `parameter_dependency` | explicit | config | parameter | CMD-UNC-104413-05 (SET DHCPPARAREQ) | 系统部署完成后已存在初始记录：V4DNSSERVER=ENABLE, V4PCSCFSERVER=DISABLE, V6DNSSERVER=ENABLE, V6PCSCFSERVER=DISABLE。若需 DHCP 过程获取 P-CSCF，必须 SET V4PCSCFSERVER/V6PCSCFSERVER=ENABLE。不输入参数时保持当前配置不变（手册原文）。★DHCP 过程仅支持获取 P-CSCF 地址，不支持获取 P-CSCF 域名（特性概述应用限制） | P-CSCFSW 未使能导致 DHCP 过程不获取 P-CSCF | warning | EV-CD-01 |
| `CR-CD-05` | PD-UDG 触发条件：V6PREFIXLENGTH<64 | `parameter_dependency` | explicit | config | parameter | CMD-UDG-B-SECTION.V6PREFIXLENGTH (ADD SECTION) | IPv6 Prefix Delegation 触发条件：ADD SECTION 的 V6PREFIXLENGTH 取值 49~63（<64，不包含 64）→ 该地址池采用 IPv6 Prefix Delegation 方式分配（激活文档原文）。★本地地址池方式为用户分配 IPv6 delegated-prefix 时，同一 APN 下的 IPv6 delegated-prefix 长度必须相同；外部网元（SMF/RADIUS）分配时同一 APN 下长度可不同（特性概述应用限制）。★PD 不支持从 DHCP Server 获取并分配 IPv6 delegated-prefix（特性概述说明） | V6PREFIXLENGTH 配置不当导致 PD 不触发或前缀长度不一致 | critical | EV-CD-02（PD-UDG 激活文档） |

---

## 5. MMLCommand 关键参数集（本簇 5 个 DHCP 专属命令全参数）

> **Schema 参考**：§11.4 CommandParameter。`required_mode` 取值 `required / optional / conditional_required`（Schema §11.4 必备字段）。跨簇引用命令（ADD ADDRPOOL/SET APNADDRESSATTR/SET IPALLOCRULE 等）参数见簇B，本节不重复。

### 5.1 ADD DHCPSERVERGRP（DHCP 服务器组，7 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| GROUPNAME | string | 1~31，不支持空格，不区分大小写 | `required` | 无 | DHCP 服务器组名称 |
| IPVERSION | enum | IPV4 / IPV6 | `required` | 无 | ★IP 地址类型（IPV4→WSFD-104413；IPV6→WSFD-104005） |
| REQLEASETIME | int | 0, 16~192 小时 | `optional` | 0 | DHCP 服务器组的地址租期（小时） |
| RETRYINTVAL | int | 1~10 秒 | `optional` | 3 | 向 DHCP 服务器发送消息的超时时间 |
| RETRYTIMES | int | 0~5 | `optional` | 3 | 向 DHCP 服务器发送消息的重发次数 |
| HASVPN | enum | DISABLE / ENABLE | `optional` | DISABLE | 绑定 VPN |
| VPNINSTANCE | string | 1~31，不支持空格，区分大小写 | `conditional_required` | 无 | HASVPN=ENABLE 时必填；引用 ADD VPNINST 生成；★与 ADDRPOOL VPN 一致 |

> **手册原文核对**：注意事项明确「执行后立即生效；通过 ADD DHCPSERVER 设置具体信息；通过 ADD DHCPBINDPOOLGRP 设置绑定关系；最多 1000 条记录」。

### 5.2 ADD DHCPSERVER（DHCP 服务器 IP，6 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| GROUPNAME | string | 1~31，不支持空格，不区分大小写 | `required` | 无 | 引用 ADD DHCPSERVERGRP 生成 |
| ISPRIMARY | enum | DISABLE / ENABLE | `required` | 无 | ★是否为主 DHCP 服务器（必须先主后备） |
| IPVERSION | enum | IPV4 / IPV6 | `required` | 无 | IP 地址类型 |
| V4IPADDRESS | IPv4 | IPv4 地址类型 | `conditional_required` | 无 | IPVERSION=IPV4 时必填；★同组主备 IPv4 不可相同 |
| V6IPADDRESS | IPv6 | IPv6 地址类型（非组播/链路本地/环回/未指定） | `conditional_required` | 无 | IPVERSION=IPV6 时必填；★同组主备 IPv6 子网前缀不可相同 |
| WALVALUE | int | 0~65535 | `optional` | 0 | 整机（UNC）每秒发送给该 DHCP 服务器的最大消息数；0=不控制 |

> **手册原文核对**：注意事项明确「前置：先 ADD DHCPSERVERGRP；一主一备，必须先主后备；最多 2000 条记录」。

### 5.3 ADD DHCPBINDPOOLGRP（远端地址池组与 DHCP 服务器组绑定，2 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POOLGRPNAME | string | 1~79，不支持空格及 `#`/`$`/`&`/`_` 等，由 `-`/数字/字母/`.` 组成，不以 `.` 开头，无连续 `..`，不区分大小写 | `required` | 无 | 引用 ADD ADDRPOOLGRP 生成 |
| GROUPNAME | string | 1~31，不支持空格，不区分大小写 | `required` | 无 | 引用 ADD DHCPSERVERGRP 生成 |

> **手册原文核对**：注意事项明确「每远端地址池组最多绑一个 DHCP 服务器组；一个 DHCP 服务器组可被多个远端地址池组绑定；前置：先 ADD DHCPSERVER；修改需先 RMV；最多 6000 条记录」。

### 5.4 ADD AGENTIP（远端地址池代理 IP，5 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POOLNAME | string | 1~79，不支持空格及 `#`/`$`/`&` 等，由 `-`/`_`/数字/字母/`.` 组成，不以 `.` 开头，不区分大小写 | `required` | 无 | 引用 ADD ADDRPOOL 生成 |
| SECTIONNUM | int | 0~63, 65535 | `optional` | 65535 | 地址段号；★65535 表示无效→DHCP 分配地址采用主机路由方式发布 |
| IPVERSION | enum | IPV4 / IPV6 | `required` | 无 | IP 地址类型 |
| V4AGENTIP | IPv4 | IPv4 地址类型（仅 A/B/C 类） | `conditional_required` | 无 | IPVERSION=IPV4 时必填；DHCPv4 Server 按此 V4AGENTIP 在同网段地址池分配 |
| V6AGENTIP | IPv6 | IPv6 地址类型（非组播/链路本地/环回/未指定） | `conditional_required` | 无 | IPVERSION=IPV6 时必填；DHCPv6 Server 按此 V6AGENTIP 在同网段地址池分配 |

> **手册原文核对**：命令功能明确「DHCP 服务器查找包含该代理 IP 地址的地址池，按 DHCP 服务器上的分配策略分配 IP 给 UNC，再由 UNC 下发给 UE」。注意事项明确「前置：先 ADD ADDRPOOL；最多 6000 条记录」。

### 5.5 SET DHCPPARAREQ（DHCPv4/v6 请求信元参数，4 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| V4DNSSERVER | enum | DISABLE / ENABLE | `optional` | 无（初始记录 ENABLE） | DHCPv4 消息是否请求 DNS 服务器地址 |
| V4PCSCFSERVER | enum | DISABLE / ENABLE | `optional` | 无（初始记录 DISABLE） | DHCPv4 消息是否请求 P-CSCF 服务器地址（Domain Name Server Option / SIP Server DHCP Option） |
| V6DNSSERVER | enum | DISABLE / ENABLE | `optional` | 无（初始记录 ENABLE） | DHCPv6 消息是否请求 DNS 服务器地址（DNS Recursive Name Server Option） |
| V6PCSCFSERVER | enum | DISABLE / ENABLE | `optional` | 无（初始记录 DISABLE） | DHCPv6 消息是否请求 P-CSCF 服务器地址（SIP Servers IPv6 Address List） |

> **★手册原文核对**：系统部署完成后已存在初始记录（V4DNSSERVER=ENABLE, V4PCSCFSERVER=DISABLE, V6DNSSERVER=ENABLE, V6PCSCFSERVER=DISABLE）。不输入参数时保持当前配置不变（可通过 LST DHCPPARAREQ 查询）。★DHCP Discover/Solicit 消息 Parameter Request List / Option Request Option 携带对应选项（特性概述原理概述）。

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

### 6.1 簇C 核心命令（DHCP 专属，5条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD DHCPSERVERGRP (CMD-UNC-104413-01) | DHCPSERVERGRP | DHCP 服务器组 |
| ADD DHCPSERVER (CMD-UNC-104413-02) | DHCPSERVER | DHCP 服务器 IP（一主一备） |
| ADD DHCPBINDPOOLGRP (CMD-UNC-104413-03) | DHCPBINDPOOLGRP | 远端池组与 DHCP 组绑定 |
| ADD AGENTIP (CMD-UNC-104413-04) | AGENTIP | 远端地址池代理 IP |
| SET DHCPPARAREQ (CMD-UNC-104413-05) | DHCPPARAREQ | DHCPv4/v6 请求信元参数 |

### 6.2 跨簇引用命令（6条，参数与归属见簇A/B/E）

| MMLCommand | operates_on -> ConfigObject | 本簇用法 | 归属 |
|------------|---------------------------|----------|------|
| ADD ADDRPOOL (CMD-UNC-B-ADDRPOOL) | ADDRPOOL | DHCP: POOLTYPE=DHCP；PD-UNC: IPv6+Local | 簇B |
| SET APNADDRESSATTR (CMD-UNC-B-APNADDRATTR) | APNADDRESSATTR | DHCP: SUPPORTIPV4/V6；PD-UNC: IPV6ALLOCTYPE=LOCAL | 簇B |
| SET IPALLOCRULE (CMD-UNC-B-IPALLOCRULE) | IPALLOCRULE | DHCP 地址分配规则 | 簇B |
| ADD APN (CMD-UNC-A-APN) | APN | DHCP/PD APN 实例 | 簇A |
| MOD APN (CMD-UNC-A-APN-MOD) | APN | PD-UNC: HASVPNIPV6=ENABLE, VPNINSTANCEIPV6 | 簇A |
| ADD POOL/SECTION/POOLGRPMAP (CMD-UDG-B-*) | POOL/SECTION/POOLGRPMAP | PD-UDG: EXTERNAL+IPv6, V6PREFIXLENGTH<64 | 簇B |
| ADD OSPFV3/AREA/INTERFACE/IMPORTROUTE (CMD-UDG-E-*) | OSPFV3 系列 | PD-UDG 手机下行 IPv6 路由（引入 wlr） | 簇E |

---

## 7. ★CommandRule governs MMLCommand 边表（§11.6 反向）

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-CD-01 | CMD-UNC-104413-02 (ADD DHCPSERVER) V4IPADDRESS/V6IPADDRESS | 主备 IP 不可相同；必须先主后备 |
| CR-CD-02 | OBJ-DHCPSERVERGRP ↔ OBJ-ADDRPOOL-U 关系 | DHCP 服务器组与地址池 VPN 必须一致 |
| CR-CD-03 | OBJ-DHCPBINDPOOLGRP | 远端池组最多绑一个 DHCP 组；修改需先 RMV |
| CR-CD-04 | CMD-UNC-104413-05 (SET DHCPPARAREQ) | 初始记录 DNS=ENABLE/P-CSCF=DISABLE；DHCP 仅支持获取 P-CSCF 地址不支持域名 |
| CR-CD-05 | CMD-UDG-B-SECTION.V6PREFIXLENGTH (ADD SECTION) | V6PREFIXLENGTH<64（49~63）触发 PD；本地池同 APN 前缀长度必须相同；PD 不支持 DHCP 方式 |

---

## 8. 使用实例脚本（保留手册原文）

### 8.1 DHCPv4 服务器组配置（来源：ADD DHCPSERVERGRP/DHCPSERVER/DHCPBINDPOOLGRP 手册使用实例）

```
//创建DHCP服务器组。
ADD DHCPSERVERGRP:GROUPNAME="testgrp",IPVERSION=IPV4,HASVPN=DISABLE;

//为DHCP服务器组添加主DHCP服务器。
ADD DHCPSERVER:GROUPNAME="group1",ISPRIMARY=ENABLE,IPVERSION=IPV4,V4IPADDRESS="10.1.1.1";

//将远端地址池组与DHCP服务器组关联（前置：先配置 ADDRPOOLGRP + DHCPSERVER）。
ADD DHCPBINDPOOLGRP:POOLGRPNAME="poolgrp1",GROUPNAME="group1";
```

### 8.2 远端地址池代理 IP 配置（来源：ADD AGENTIP 手册使用实例）

```
//配置远端地址池testpool的代理地址（前置：先 ADD ADDRPOOL）。
ADD AGENTIP:POOLNAME="testpool",SECTIONNUM=0,IPVERSION=IPV4,V4AGENTIP="10.10.110.1";
```

### 8.3 DHCP 请求信元配置（来源：SET DHCPPARAREQ 手册使用实例）

```
//指定DHCPv4/v6消息中DNS与P-CSCF服务器地址均使能。
SET DHCPPARAREQ:V4DNSSERVER=ENABLE,V4PCSCFSERVER=ENABLE,V6DNSSERVER=ENABLE,V6PCSCFSERVER=ENABLE;
```

### 8.4 ⚠️DHCP/DHCPv6 完整激活脚本（文档缺口，draft 重建）

> **⚠️文档缺口标注**：WSFD-104413 DHCP功能 / WSFD-104005 DHCPv6地址分配 两个特性**仅有特性概述+参考信息，无激活文档**。以下脚本为依据参考信息命令清单 + 5 个 DHCP 手册使用实例 + 特性概述原理**重建的 draft**，非产品文档原文。完整激活流程需补充产品文档后复核。

```
//【文档缺口·draft重建】WSFD-104413 DHCP功能 / WSFD-104005 DHCPv6地址分配 激活脚本
//依据：参考信息命令清单（ADD VPNINST/ADDRPOOL/AGENTIP/DHCPSERVERGRP/DHCPSERVER/DHCPBINDPOOLGRP/APN + SET APNADDRESSATTR/IPALLOCRULE/DHCPPARAREQ）
//      + 特性概述（UNC 作为 DHCP/DHCPv6 Client，携带代理 IP 向 DHCP Server 申请）

//步骤1：配置VPN实例（引用簇A）。
ADD VPNINST:VPNINSTANCE="vpn1";

//步骤2：配置远端地址池（POOLTYPE=DHCP，引用簇B ADD ADDRPOOL）。
ADD ADDRPOOL:POOLNAME="dhcppool1",IPVERSION=IPv4,POOLTYPE=DHCP,HASVPN=Enable,VPNINSTANCE="vpn1";

//步骤3：配置远端地址池代理IP（本簇 ADD AGENTIP）。
ADD AGENTIP:POOLNAME="dhcppool1",SECTIONNUM=0,IPVERSION=IPV4,V4AGENTIP="10.10.110.1";

//步骤4：配置DHCP服务器组（本簇 ADD DHCPSERVERGRP）。
ADD DHCPSERVERGRP:GROUPNAME="dhcpgrp1",IPVERSION=IPV4,HASVPN=Enable,VPNINSTANCE="vpn1";

//步骤5：配置DHCP服务器（一主一备，本簇 ADD DHCPSERVER）。
ADD DHCPSERVER:GROUPNAME="dhcpgrp1",ISPRIMARY=ENABLE,IPVERSION=IPV4,V4IPADDRESS="10.1.1.1";

//步骤6：绑定远端地址池组与DHCP服务器组（本簇 ADD DHCPBINDPOOLGRP，前置先配置 ADDRPOOLGRP）。
ADD DHCPBINDPOOLGRP:POOLGRPNAME="remotegrp1",GROUPNAME="dhcpgrp1";

//步骤7：配置APN与地址分配属性（引用簇A/簇B）。
ADD APN:APN="apn-dhcp";
SET APNADDRESSATTR:APN="apn-dhcp",SUPPORTIPV4=ENABLE;

//步骤8：配置DHCP请求信元（本簇 SET DHCPPARAREQ，可选，获取DNS/P-CSCF）。
SET DHCPPARAREQ:V4DNSSERVER=ENABLE,V4PCSCFSERVER=ENABLE;

//步骤9：配置地址分配规则（引用簇B SET IPALLOCRULE）。
SET IPALLOCRULE:FIRSTRULESW=ENABLE,FIRSTRULE=APN-1&LOCATION-0&SMF-0;
```

> **DHCPv6 差异**（WSFD-104005）：IPVERSION=IPv6 / V6IPADDRESS / V6AGENTIP / SUPPORTIPV6，其余命令结构相同。

### 8.5 GWFD-020406 IPv6 Prefix Delegation 激活脚本（UDG，来源：激活外部网元地址分配文档原文）

```
//打开License配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5P6PD01",SWITCH=ENABLE;  // draft推断格式，激活文档原文仅说"打开License开关"

//配置外部地址分配时的白名单检测功能。
ADD VPNINST:VPNINSTANCE="vpn1";

ADD POOLGROUP:POOLGRPNAME="poolgroup1";

//★PD关键：POOLTYPE=EXTERNAL + IPVERSION=IPV6 + V6PREFIXLENGTH=63（<64触发PD）
ADD POOL:POOLNAME="testpool",POOLTYPE=EXTERNAL,IPVERSION=IPV6,CHECKIPVALID=ENABLE,HASVPN=ENABLE,VPNINSTANCE="vpn1";
ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="fc00:0000:0000:fcee:0000:0000:0000:0000",V6PREFIXEND="fc00:0000:0000:fcef:ffff:ffff:ffff:ffff",V6PREFIXLENGTH=63;

ADD POOLBINDGROUP:POOLGROUPNAME="poolgroup1",POOLNAME="testpool";

ADD APN:APN="apn-test",HASVPN=ENABLE,VPNINSTANCE="vpn1";

ADD POOLGRPMAP:MAPPINGNAME="mapping1",APN="apn-test",POOLGROUPNAME="poolgroup1";

//配置手机下行路由（IPv6 OSPFv3）。
ADD OSPFV3:PROCID=6,VRFNAME="vpn1",ROUTERID="10.8.25.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
ADD OSPFV3AREA:PROCID=6,AREAID="0.0.0.5";
ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk1.1",DRPRI=0,VIRTUALSYSFLAG=TRUE,CFGROUTERIDFLAG=FALSE;
ADD OSPFV3IMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr;
```

### 8.6 WSFD-104004 IPv6前缀代理 激活脚本（UNC，来源：激活IPv6前缀代理文档原文）

```
//打开本特性的License配置开关。
SET LICENSESWITCH:LICITEM="LKV3W9V6PD11",SWITCH=ENABLE;

//创建IPv6 VPN实例。
ADD VPNINST:VPNINSTANCE="vpn1";
ADD L3VPNINST:VRFNAME="vpn1";
ADD VPNINSTAF:VRFNAME="vpn1",AFTYPE=ipv6uni;
MOD VPNINSTAF:VRFNAME="vpn1",AFTYPE=ipv6uni,VRFRD="65512:2";

//配置本地地址池分配IPv6代理前缀（★PD-UNC：IPVERSION=IPv6 + POOLTYPE=Local）。
ADD ADDRPOOL:POOLNAME="pool01",POOLTYPE=Local,IPVERSION=IPv6,HASVPN=Enable,VPNINSTANCE="vpn1";

//配置APN下的IP地址分配属性（★PD-UNC触发：IPV6ALLOCTYPE=LOCAL）。
ADD APN:APN="huawei.com";
SET APNADDRESSATTR:APN="huawei.com",IPV6ALLOCTYPE=LOCAL;
MOD APN:APN="huawei.com",HASVPNIPV6=ENABLE,VPNINSTANCEIPV6="vpn1";
```

---

## 9. 抽取核对清单

### 9.1 配置类命令参数行数与来源手册路径

| 命令 | 参数行数 | 来源手册路径（相对 `output/UNC 20.15.2 产品文档(裸机容器) 05/`） |
|------|---------|----------------------------------------------------------------|
| ADD DHCPSERVERGRP | 7 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/DHCP服务器组/增加DHCP服务器组（ADD DHCPSERVERGRP）_32304093.md` |
| ADD DHCPSERVER | 6 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/DHCP服务器/增加DHCP服务器（ADD DHCPSERVER）_86984444.md` |
| ADD DHCPBINDPOOLGRP | 2 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/DHCP服务器绑定/增加DHCP服务器组与地址池组绑定关系（ADD DHCPBINDPOOLGRP）_32382543.md` |
| ADD AGENTIP | 5 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/代理IP管理/增加远端地址池代理IP信息（ADD AGENTIP）_32224047.md` |
| SET DHCPPARAREQ | 4 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/DHCP请求信元参数信息/设置向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息（SET DHCPPARAREQ）_32224051.md` |
| ADD ADDRPOOL（引用簇B，UNC 地址池） | 12 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md` |
| **合计（本簇专属）** | **24 参数行** | 5 命令全部手册定位成功 |

### 9.2 ⚠️手册未定位 / 文档缺口列表

| 命令/场景 | 状态 | 原因 |
|-----------|------|------|
| **WSFD-104413 DHCP功能激活文档** | ⚠️文档缺口 | 该特性仅有「特性概述 + 参考信息」2 个文件，**无激活文档**（产品文档树未提供）。§8.4 激活脚本为依据命令清单+手册实例+原理重建的 draft，非原文。激活流程需补充产品文档后复核。 |
| **WSFD-104005 DHCPv6地址分配激活文档** | ⚠️文档缺口 | 同上，仅 2 文件无激活文档。§8.4 DHCPv6 部分为 draft 重建。 |
| SET LICENSESWITCH（DHCP/PD License 开关命令） | ⚠️参数未抽取 | 4 个特性激活文档均引用 SET LICENSESWITCH 打开 License 开关，但该命令属 License 管理通用命令（非本簇特性专属），参数（LICITEM/SWITCH）仅在 PD-UNC 激活脚本中出现完整实例，DHCP/DHCPv6 激活文档缺失故未抽 DHCP 的 LICITEM 取值（DHCP=LKV3W9DHCP12, DHCPv6=LKV3W9V6AA11 来自特性概述 License 章节，非 SET 命令参数）。 |
| GWFD-020406 PD 激活本地地址池文档 | ⚠️文档缺失 | UDG PD 文档树仅列出 4 文件（概述/外部网元激活/调测/参考信息），任务说明提及的「激活本地地址池分配[基于APN/SMF+APN/SMF/位置]」等本地地址池激活文档**未在文档树中定位**。本文件 PD-UDG 仅覆盖「外部网元地址分配」场景。 |
| ADD ADDRPOOLGRP（UNC 远端地址池组） | ⚠️手册未在本簇定位 | ADD DHCPBINDPOOLGRP.POOLGRPNAME 引用 ADD ADDRPOOLGRP 生成，但该手册未在 DHCP 文档树范围内定位（属簇B UNC 地址池组体系，需在簇B 复核）。 |

### 9.3 与簇B 样板的关键差异 / 补充（★重点核对项）

| 差异项 | 簇B 样板（UDG 地址分配） | 本簇（簇C DHCP/PD） | 影响 |
|--------|---------|----------------|------|
| **DHCP 服务器体系** | 簇B 无（簇B 为本地/SMF/RADIUS 地址分配） | ★新增 4 对象（DHCPSERVERGRP/DHCPSERVER/DHCPBINDPOOLGRP/AGENTIP）+ 1 请求信元对象（DHCPPARAREQ），共 5 个 DHCP 专属命令 24 参数 | DHCP 外置服务器地址分配场景完整建模 |
| **PD 无专属命令** | 簇B ADD SECTION.V6PREFIXLENGTH 49~64（普通 IPv6 地址段） | ★PD-UDG 复用簇B ADD SECTION，关键在 V6PREFIXLENGTH 取 49~63（<64）触发 PD（非新命令，是参数取值语义）；PD-UNC 复用簇B SET APNADDRESSATTR.IPV6ALLOCTYPE=LOCAL 触发 | PD 通过参数触发，无 PD 专属命令建模 |
| **License 链** | 簇B 未涉及 PD/DHCP License | ★IPv6 License 链尾：PD-UDG=LKV3G5P6PD01，PD-UNC=LKV3W9V6PD11；DHCPv4=LKV3W9DHCP12，DHCPv6=LKV3W9V6AA11 | IPv6 License 链完整（承载上下文→双栈→PD） |
| **DHCP/DHCPv6 命令清单相同** | — | ★WSFD-104413 与 WSFD-104005 参考信息命令清单**完全相同**，区别仅在 IPVERSION（V4/V6）与 License。建模上 ADD DHCPSERVERGRP/DHCPSERVER/AGENTIP 通过 IPVERSION 参数区分 V4/V6 场景 | 2 特性共用 5 命令，避免重复建模 |
| **IPv6 路由（PD-UDG）** | 簇B 为 IPv4 OSPF（ADD OSPF/AREA/NETWORK/IMPORTROUTE） | ★PD-UDG 为 IPv6 OSPFv3（ADD OSPFV3/AREA/INTERFACE/IMPORTROUTE），与簇E IPv4 OSPF 并列，登记为引用簇E | PD 下行 IPv6 路由完整 |
| **PD 互斥特性** | — | ★GWFD-020406 概述明确 PD 与 L2TP VPN / 用户面地址自动检测 / NAT / 入不转板 / 通用DNN漫游分流 互斥（手机后路由用户限制） | PD 部署约束明确 |

### 9.4 抽取统计

| 维度 | 数量 |
|------|------|
| 簇C 专属配置类命令（手册定位成功） | 5（ADD DHCPSERVERGRP/DHCPSERVER/DHCPBINDPOOLGRP/AGENTIP + SET DHCPPARAREQ） |
| 簇C 专属配置类命令参数总行数 | 24 |
| 跨簇引用命令（参数见簇A/B/E） | 11（ADD ADDRPOOL/SET APNADDRESSATTR/SET IPALLOCRULE/ADD APN/MOD APN/ADD VPNINST + ADD POOL/SECTION/POOLGROUP/POOLBINDGROUP/POOLGRPMAP + ADD OSPFV3/AREA/INTERFACE/IMPORTROUTE，去重后约 11 类） |
| ⚠️手册未定位/文档缺口 | 5（DHCP 激活文档 / DHCPv6 激活文档 / SET LICENSESWITCH 参数 / PD-UDG 本地地址池激活文档 / ADD ADDRPOOLGRP） |
| ConfigObject（本簇新对象） | 5（DHCPSERVERGRP/DHCPSERVER/DHCPBINDPOOLGRP/AGENTIP/DHCPPARAREQ） |
| CommandRule | 5（CR-CD-01~05） |
| ConfigObject 关系边 | 7（contains 1 + refers_to 2 + links 1 + depends_on 3） |
| operates_on 边 | 5（核心）+ 7（跨簇引用） |
| 激活子场景脚本 | 6（DHCPv4 服务器组 / 代理 IP / 请求信元 / ⚠️DHCP 完整 draft / PD-UDG 外部网元 / PD-UNC 本地） |

---

> 本文件为簇C（DHCP/PD）4 个特性命令层抽取。
> **★关键贡献**：①补齐 DHCP 外置服务器地址分配体系（5 命令 24 参数，簇B 未覆盖）；②明确 PD 无专属命令、通过参数触发（V6PREFIXLENGTH<64 / IPV6ALLOCTYPE=LOCAL）；③标注 DHCP/DHCPv6 文档缺口（无激活文档，§8.4 为 draft 重建）；④完整 IPv6 License 链（承载上下文→双栈→PD）；⑤建立 5 条特性级 CommandRule（主备 IP/VPN 一致/绑定基数/请求信元/PD 触发条件）。
> **⚠️待复核**：DHCP/DHCPv6 激活文档缺失，§8.4 脚本需补充产品文档后复核；PD-UDG 本地地址池激活文档未定位；ADD ADDRPOOLGRP 需在簇B 复核。
