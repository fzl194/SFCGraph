# APN 业务域三层图谱 · 第4层：命令图谱

> **文件定位**：`three-layer-graph/04-command-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **作用**：实例化 142 MMLCommand（UDG 63 + UNC 79）+ 65 ConfigObject + 18 CommandRule + ConfigObject 间关系边
> **数据来源**：`feature-knowledge/cross-feature-analysis.md` 附录B（MML命令交叉参考）+ 附录C（配置对象复用矩阵）+ 附录D（典型端到端流程）+ 各 feature-knowledge §配置对象/§约束
> **★Schema合规要点**：`CommandRule governs MMLCommand`（反向），非 `has_rule`；POOL(UDG) vs ADDRPOOL(UNC) 分离建模；APNL2TPATTR(U,10+参数) vs APNL2TPCTRL(C,2参数) 分离；ConfigObject 关系直接作为边（§11.7）

---

## 0. 命令图谱总览

### 0.1 MMLCommand 按产品分布

| 产品 | 命令数 | 说明 |
|------|-------|------|
| UDG | 63 | 用户面执行命令：地址池体系(POOL/SECTION) + 静态冗余(GRE/REDUNDRDTIP) + L2TP(U面LAC) + IPSec(VNRS+IPsec双配) + MPLS(推导) + 地址分配规则 + 接入控制(APNQOSATTR) + OSPF/OSPFv3 + 运维查询 + 策略刷新生效(REFRESHSRV) |
| UNC | 79 | 控制面策略命令：地址池体系(ADDRPOOL) + UPF选择(11件套) + Radius三件套 + 二次鉴权(UPF Radius) + AKA鉴权(2/3/4/5G) + ARD接入限制(2/3/4G) + NGMM移动性 + 别名APN(双视角) + DHCP + L2TP(C面决策) + 对等网元DNS + 会话管理维护 + 策略刷新生效(REFRESHSRV) |
| **合计** | **142** | 含跨产品共用双计数（POOL vs ADDRPOOL / L2TPN4KEY vs L2TPKEY / ADD APN / SET LICENSESWITCH / REDUNDUSER / SET REFRESHSRV） |

### 0.2 ConfigObject 按功能域分布

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| 地址分配域（U+C 双侧） | 20 | POOL/ADDRPOOL, SECTION, POOLGROUP/ADDRPOOLGRP, POOLBINDGROUP/POOLBINDGRP, POOLGRPMAP, APN, APNADDRESSATTR, IPALLOCRULE, APNIPALLOCRULE, CPNODEID, IPALLOCBYSMFGLBSW, IPALLOCBYLOCGLBSW, LACGROUP/TACGROUP, ADRLOCWHITELST, CONFLICTIP, UPNODE, PNFPROFILE, UPFBINDGRP, STATICADDRPARA, BLACKLIST |
| 隧道类（GRE/IPSec/MPLS/L2TP） | 22 | GRETUNNEL, IPSECPROPOSALIPSEC, IKEPROPOSAL, IKEPEER, IPSECPOLICY, IPSECINTFCFGIPSEC, ACLGROUPIPSEC/ACLRULEADV4IPSEC, VPNINSTANCE/BGPVPNV4PEER(★推导), APNL2TPATTR(U), APNL2TPCTRL(C), L2TPGROUP/L2TPLNSINFO, L2TPCLIENTIP/L2TPRDSCLIENT, PPPCFG/APNPPPACCESS, GLOBALL2TP, L2TPN4KEY(U)/L2TPKEY(C), REDUNDRDTIP, REDUNDUSER, APNREDUNDUPSW, SRROUTE/SRROUTE6, Tunnel/LoopBack接口 |
| 鉴权/Radius/接入控制/网元选择 | 28 | APNAUTHATTR, RDSSVRGRP, RDSSVR/APNRDSSVRGRP, APNRDSCLIENTIP, APNRDSACCTCTRL, APNRADIUSATTR, UPLIST4RDS, CPGTPUADDR, RDSUPFCTRL, UPFRDSSVR, UPFRDSCLIENTIP, NETWORKINSTVPNMAP, FHBYPASS, GBAUTHCIPH/IUAUTHCIPH/S1USRSECPARA/NGUSRSECPARA(AKA系列), GBARD/IUARD/S1ARD(2/3/4G ARD), NGMMSUBDATA, NGMMPROCTRL, APNALIAS, ALIASAPN, APNREPORTATTR, PNFDNN/PNFNS/PNFDNAI/PNFUPFINFO, UPAREA/UPAREABINDN2TAI, UPBINDS11/UPBINDGNGP, UPSELECTPRI/UPSELECTFLAG/APNUPSELPLY/UPLOADBALANCE, AREADNS/DNSN/SGSNDNS, APNQOSATTR, APNACTNUM |
| 底座/会话管理/用户数据 | 6 | PDPAPN, SMSUBDATA, SDBTMR, DSP POOLUSAGE/SESSIONINFO(运维), AMDATA |
| **合计** | **~65**（去重） | — |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1（142 个 MMLCommand）所有对象。
> **声明**：本文件 §1 所有 142 个 MMLCommand 的 `status` 字段值均为 `active`（Schema §11.3 MMLCommand.status 必备）。APN 业务域所有正式命令均处于启用状态。
> **★MPLS 推导命令说明**：CMD-UDG-062/063/064（GWFD-020411 MPLS VPN 推导命令，见 §1.11）虽 `status=active`（已在命令图谱登记），但 `command_summary` 列已用 "★推导" 前缀明确标注其源自 MPLS L3VPN 标准实践推导（9 篇文档无 MML 脚本），需命令字典补全验证；参见 CR-APN-18。
> **依据**：APN 业务域所有命令均处于正式启用状态，无 `deprecated` 或 `planned` 状态。
> **例外**：无。

---

## 1. MMLCommand 实例化

### 1.1 基础对象与 License 门控（UDG，2个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-001` | `SET LICENSESWITCH` | SET | LICENSESWITCH | License 开关，APN 业务域所有需 License 特性的前置门控（IPv6三件套/L2TP/基于位置/MPLS） | LICITEM, SWITCH(ENABLE/DISABLE) | EV-FK-18, EV-FK-26, EV-FK-30, EV-FK-21 |
| `CMD-UDG-002` | `SET SOFTPARAOFBIT` | SET | SOFTPARAOFBIT | 软参位控制（如 BIT391 地址分配真值表标准/华为私有切换；Byte671 bit7 L2TP 关闭快速流表） | BITID, BITVALUE | EV-FK-06, EV-FK-21 |

### 1.2 VPN 实例与接口体系（UDG，6个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-003` | `ADD VPNINST` | ADD | VPNINST | VPN 实例（IPv4 地址分配/隧道承载基础） | VPNINSTNAME | EV-FK-06, EV-FK-17, EV-FK-28, EV-FK-21, EV-FK-18, EV-FK-29 |
| `CMD-UDG-004` | `ADD L3VPNINST` | ADD | L3VPNINST | L3VPN 实例（VRF） | VRFNAME | EV-FK-06, EV-FK-17, EV-FK-28, EV-FK-26, EV-FK-30, EV-FK-30 |
| `CMD-UDG-005` | `ADD VPNINSTAF` | ADD | VPNINSTAF | VPN 地址族（★IPv6/双栈必须 AFTYPE=ipv6uni） | VRFNAME, AFTYPE(ipv4uni/ipv6uni) | EV-FK-28, EV-FK-26, EV-FK-30, EV-FK-30 |
| `CMD-UDG-006` | `ADD INTERFACE` | ADD | INTERFACE | 物理/逻辑接口（Tunnel/LoopBack） | IFNAME | EV-FK-20, EV-FK-28, EV-FK-29, EV-FK-30 |
| `CMD-UDG-007` | `ADD IPBINDVPN` | ADD | IPBINDVPN | 接口绑定 VPN | IFNAME, VPNINSTNAME | EV-FK-20, EV-FK-28, EV-FK-30 |
| `CMD-UDG-008` | `ADD LOGICINF` | ADD | LOGICINF | Giif 逻辑接口（L2TP 源端绑定） | IFNAME | EV-FK-21 |

### 1.3 地址池体系（UDG 侧 POOL，8个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-009` | `ADD APN` | ADD | APN | APN/DNN 实例（★跨域共用挂载点；HASVPN/HASVPNIPV6 双栈标识） | APN, HASVPN, VPNINSTANCE, HASVPNIPV6, VPNINSTANCEIPV6 | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-37, EV-FK-21, EV-FK-18, EV-FK-26 |
| `CMD-UDG-010` | `MOD APN` | MOD | APN | APN 修改 | APN, ... | EV-FK-37 |
| `CMD-UDG-011` | `LST APN` | LST | APN | APN 查询 | APN | EV-FK-37 |
| `CMD-UDG-012` | `RMV APN` | RMV/DEL | APN | APN 删除 | APN | EV-FK-37 |
| `CMD-UDG-013` | `SET APNADDRESSATTR` | SET | APNADDRESSATTR | ★APN 地址分配属性（SUPPORTIPV4/V6/IGNOREV4/V6POOLID/HOSTROUTEIP） | APN, SUPPORTIPV4, SUPPORTIPV6, IGNOREV4, V6POOLID, HOSTROUTEIP | EV-FK-06, EV-FK-17, EV-FK-18, EV-FK-26, EV-FK-30 |
| `CMD-UDG-014` | `ADD POOL` | ADD | POOL | ★UDG 地址池（POOLTYPE=LOCAL，与 UNC ADDRPOOL 分离建模） | POOLNAME, POOLTYPE(LOCAL/EXTERNAL), IPVERSION(IPV4/IPV6), HASVPN, VPNINSTANCE | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26, EV-FK-30 |
| `CMD-UDG-015` | `ADD SECTION` | ADD | SECTION | 地址段（V4STARTIP/V6PREFIXSTART，★V6PREFIXLENGTH<64=PD模式） | POOLNAME, SECTIONNUM, IPVERSION, V4STARTIP, V4ENDIP, V6PREFIXSTART, V6PREFIXEND, V6PREFIXLENGTH | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26, EV-FK-30 |
| `CMD-UDG-016` | `ADD POOLGROUP` | ADD | POOLGROUP | 地址池组（IPV4ALLOCPRIALG/IPV6ALLOCPRIALG 优先级算法） | POOLGRPNAME, IPV4ALLOCPRIALG, IPV6ALLOCPRIALG | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26, EV-FK-30 |

### 1.4 地址分配规则与绑定（UDG，8个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-017` | `ADD POOLBINDGROUP` | ADD | POOLBINDGROUP | 地址池绑定到池组（PRIORITY 控制优先级，★UDG 命名 GROUP） | POOLGROUPNAME, POOLNAME, PRIORITY | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26, EV-FK-30 |
| `CMD-UDG-018` | `ADD POOLGRPMAP` | ADD | POOLGRPMAP | 池组映射（APN/SMF/LOCATION 任意组合） | MAPPINGNAME, APN, POOLGROUPNAME | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26, EV-FK-30 |
| `CMD-UDG-019` | `SET IPALLOCRULE` | SET | IPALLOCRULE | 全局三级地址分配规则（FIRSTRULE/SECONDRULE/THIRDRULE） | FIRSTRULESW, FIRSTRULE(APN/SMF/LOCATION), SECONDRULESW, SECONDRULE, THIRDRULESW, THIRDRULE | EV-FK-06, EV-FK-18, EV-FK-30 |
| `CMD-UDG-020` | `SET APNIPALLOCRULE` | SET | APNIPALLOCRULE | APN 级地址分配规则（覆盖全局） | APN, FIRSTRULE, ... | EV-FK-06, EV-FK-18 |
| `CMD-UDG-021` | `ADD CPNODEID` | ADD | CPNODEID | SMF 的 NodeID（基于 SMF 分配场景） | NODEID | EV-FK-06, EV-FK-30 |
| `CMD-UDG-022` | `SET IPALLOCBYSMFGLBSW` | SET | IPALLOCBYSMFGLBSW | 基于 SMF 分配全局开关 | SWITCH | EV-FK-06, EV-FK-30 |
| `CMD-UDG-023` | `SET IPALLOCBYSMFSW` | SET | IPALLOCBYSMFSW | 指定 SMF 分配开关 | SMFID, SWITCH | EV-FK-06 |
| `CMD-UDG-024-1` | `ADD CONFLICTIP` | ADD | CONFLICTIP | 冲突地址标识（IPv4/IPv6 分命令） | CONFLICTIP | EV-FK-06, EV-FK-30 |
| `CMD-UDG-024-2` | `ADD CONFLICTIPV6` | ADD | CONFLICTIPV6 | 冲突地址标识（IPv4/IPv6 分命令） | CONFLICTIP | EV-FK-06, EV-FK-30 |

### 1.5 基于位置地址分配（UDG，6个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-025` | `ADD LACGROUP` | ADD | LACGROUP | LAC 位置区组（2/3G） | LACGROUPNAME | EV-FK-18, EV-FK-30 |
| `CMD-UDG-026` | `ADD LACID` | ADD | LACID | LAC 位置区 ID | LACGROUPNAME, LAC | EV-FK-18, EV-FK-30 |
| `CMD-UDG-027` | `ADD TACGROUP` | ADD | TACGROUP | TAC 位置区组（4/5G） | TACGROUPNAME | EV-FK-18 |
| `CMD-UDG-028-1` | `ADD S1TACID` | ADD | S1TACID | 4G(S1)/5G(N2) TAC ID | TACGROUPNAME, TAC | EV-FK-18 |
| `CMD-UDG-028-2` | `ADD N2TACID` | ADD | N2TACID | 4G(S1)/5G(N2) TAC ID | TACGROUPNAME, TAC | EV-FK-18 |
| `CMD-UDG-029` | `SET IPALLOCBYLOCGLBSW` | SET | IPALLOCBYLOCGLBSW | ★基于位置分配全局开关（IPv4/IPv6 分别） | IPV4SWITCH, IPV6SWITCH | EV-FK-18 |
| `CMD-UDG-030` | `ADD ADRLOCWHITELST` | ADD | ADRLOCWHITELST | 位置区地址分配白名单（MSISDN） | MSISDN | EV-FK-18, EV-FK-30 |
| `CMD-UDG-031` | `SET IPALLOCBYLOCSW` | SET | IPALLOCBYLOCSW | 指定位置区开关（覆盖全局） | LOCATIONID, SWITCH | EV-FK-18 |

### 1.6 下行路由发布（OSPF/OSPFv3，UDG，8个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-032` | `ADD OSPF` | ADD | OSPF | IPv4 OSPF 进程 | PROCID, ROUTERID, VRFNAME | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26 |
| `CMD-UDG-033` | `ADD OSPFAREA` | ADD | OSPFAREA | OSPF 区域 | PROCID, AREAID | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26 |
| `CMD-UDG-034` | `ADD OSPFNETWORK` | ADD | OSPFNETWORK | OSPF 网段 | PROCID, AREAID, NETWORK | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26 |
| `CMD-UDG-035` | `ADD OSPFIMPORTROUTE` | ADD | OSPFIMPORTROUTE | ★引入 WLR 路由（PROTOCOL=wlr） | PROCID, PROTOCOL(wlr) | EV-FK-06, EV-FK-17, EV-FK-20, EV-FK-18, EV-FK-26 |
| `CMD-UDG-036` | `ADD OSPFV3` | ADD | OSPFV3 | IPv6 OSPFv3 进程（IPv6 承载链必需） | PROCID, ROUTERID | EV-FK-28, EV-FK-26, EV-FK-30 |
| `CMD-UDG-037` | `ADD OSPFV3AREA` | ADD | OSPFV3AREA | OSPFv3 区域 | PROCID, AREAID | EV-FK-28, EV-FK-26, EV-FK-30 |
| `CMD-UDG-038` | `ADD OSPFV3IMPORTROUTE` | ADD | OSPFV3IMPORTROUTE | ★引入 WLR 到 OSPFv3 | PROCID, PROTOCOL(wlr) | EV-FK-28, EV-FK-26, EV-FK-30 |
| `CMD-UDG-039-1` | `ADD ROUTEPOLICY` | ADD | ROUTEPOLICY | 路由策略 | POLICYNAME, NODEID | EV-FK-28, EV-FK-26, EV-FK-30 |
| `CMD-UDG-039-2` | `ADD ROUTEPOLICYNODE` | ADD | ROUTEPOLICYNODE | 路由策略 | POLICYNAME, NODEID | EV-FK-28, EV-FK-26, EV-FK-30 |
| `CMD-UDG-039-3` | `ADD MATCHROUTETYPE` | ADD | MATCHROUTETYPE | 路由策略 | POLICYNAME, NODEID | EV-FK-28, EV-FK-26, EV-FK-30 |

### 1.7 接口 IP 与静态路由（UDG，4个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-040` | `ADD IFIPV4ADDRESS` | ADD | IFIPV4ADDRESS | 接口 IPv4 地址 | IFNAME, IFIPADDR, SUBNETMASK | EV-FK-20, EV-FK-28, EV-FK-29, EV-FK-30 |
| `CMD-UDG-041` | `ADD IFIPV6ADDRESS` | ADD | IFIPV6ADDRESS | 接口 IPv6 地址 | IFNAME, IFIPV6ADDR, PREFIXLENGTH | EV-FK-28 |
| `CMD-UDG-042` | `SET IFIPV6ENABLE` | SET | IFIPV6ENABLE | IPv6 接口使能 | IFNAME, SWITCH | EV-FK-28 |
| `CMD-UDG-043-1` | `ADD SRROUTE` | ADD | SRROUTE | 静态路由（IPv4/IPv6 分命令，引导流量进 Tunnel） | AFTYPE, PREFIX, MASKLENGTH, IFNAME | EV-FK-20, EV-FK-29, EV-FK-30 |
| `CMD-UDG-043-2` | `ADD SRROUTE6` | ADD | SRROUTE6 | 静态路由（IPv4/IPv6 分命令，引导流量进 Tunnel） | AFTYPE, PREFIX, MASKLENGTH, IFNAME | EV-FK-20, EV-FK-29, EV-FK-30 |

### 1.8 GRE 隧道（UDG，3个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-044` | `ADD GRETUNNEL` | ADD | GRETUNNEL | ★GRE 隧道（TNLTYPE=gre，IPFD-015002 核心；GWFD-010107 主备 UDG 间冗余用） | TNLNAME, TNLTYPE(gre), SRCTYPE, SRCIFNAME, DSTIPADDR | EV-FK-29, EV-FK-20 |
| `CMD-UDG-045` | `MOD GRETUNNEL` | MOD | GRETUNNEL | GRE 隧道修改（Checksum/Key/Keepalive 可选特性） | TNLNAME, TNLTYPE, CHECKSUMEN, GREKEYEN, GREKEY, KEEPALVEN, KEEPALVPERIOD, KEEPALVRETRYCNT | EV-FK-29 |
| `CMD-UDG-046` | `RMV GRETUNNEL` | RMV/DEL | GRETUNNEL | GRE 隧道删除 | TNLNAME, TNLTYPE | EV-FK-29 |

### 1.9 IPSec 隧道（UDG，9个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-047` | `ADD ACLGROUPIPSEC` | ADD | ACLGROUPIPSEC | IPSec ACL 组（保护数据流容器） | ACLGROUPNAME | EV-FK-30 |
| `CMD-UDG-048` | `ADD ACLRULEADV4IPSEC` | ADD | ACLRULEADV4IPSEC | IPSec ACL 规则（★仅源/目的 IP，不支持端口） | ACLGROUPNAME, SRCIP, DSTIP | EV-FK-30 |
| `CMD-UDG-049` | `ADD IPSECPROPOSALIPSEC` | ADD | IPSECPROPOSALIPSEC | IPSec 安全提议（封装+协议+算法） | PROPOSALNAME, ENCAPSULATIONMODE(TUNNEL/TRANSPORT), SECURITYPROTOCOL(AH/ESP) | EV-FK-30 |
| `CMD-UDG-050` | `ADD IKEPROPOSAL` | ADD | IKEPROPOSAL | IKE 提议（★DH 组不能为 None） | PROPOSALNAME, AUTHMETHOD(PSK), DHGROUP | EV-FK-30 |
| `CMD-UDG-051` | `ADD IKEPEER` | ADD | IKEPEER | IKE 对等体（★DH 组不能为 None；默认 IKEv2） | PEERNAME, PRESHAREDKEY, EXCHANGEMODE(MAIN), REMOTEADDR, NATTRAVERSAL, VERSION1 | EV-FK-30 |
| `CMD-UDG-052` | `ADD IPSECPOLICY` | ADD | IPSECPOLICY | IPSec 安全策略（聚合 ACL+Proposal+IKE Peer） | POLICYNAME, SEQ, MODE(ISAKMP), ACLGROUPNAME | EV-FK-30 |
| `CMD-UDG-053` | `ADD PROPATTACHIPSECPROPOSAL` | ADD | PROPATTACHIPSECPROPOSAL | 策略绑定 Proposal | POLICYNAME, SEQ, PROPOSALNAME | EV-FK-30 |
| `CMD-UDG-054` | `ADD ATTACHIKEPEER` | ADD | ATTACHIKEPEER | 策略绑定 IKE Peer（PRIORITY） | POLICYNAME, SEQ, PEERNAME, PRIORITY | EV-FK-30 |
| `CMD-UDG-055` | `ADD IPSECINTFCFGIPSEC` | ADD | IPSECINTFCFGIPSEC | 应用策略到 Tunnel 接口 | IFNAME, TNLTYPE(IPSEC), POLICYNAME | EV-FK-30 |
| `CMD-UDG-056` | `SET IKEGLOBALCONFIG` | SET | IKEGLOBALCONFIG | IKE 全局配置（DPD + NAT 保活） | DPDTYPE, DPDINTERVAL, NATKLI | EV-FK-30 |

### 1.10 IPSec 微服务镜像（UDG，5个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-057` | `ADD L3VPNINSTIPSEC` | ADD | L3VPNINSTIPSEC | IPsec 微服务 L3VPN 实例镜像 | VRFNAME | EV-FK-30 |
| `CMD-UDG-058` | `ADD VPNINSTAFIPSEC` | ADD | VPNINSTAFIPSEC | IPsec 微服务 VPN 地址族镜像 | VRFNAME, AFTYPE | EV-FK-30 |
| `CMD-UDG-059` | `ADD INTERFACEIPSEC` | ADD | INTERFACEIPSEC | IPsec 微服务接口镜像 | IFNAME | EV-FK-30 |
| `CMD-UDG-060` | `ADD IPBINDVPNIPSEC` | ADD | IPBINDVPNIPSEC | IPsec 微服务接口绑定 VPN 镜像 | IFNAME, VPNINSTNAME | EV-FK-30 |
| `CMD-UDG-061` | `ADD IFIPV4ADDRESSIPSEC` | ADD | IFIPV4ADDRESSIPSEC | IPsec 微服务接口 IPv4 地址镜像 | IFNAME, IFIPADDR, SUBNETMASK | EV-FK-30 |

### 1.11 MPLS VPN（UDG，3个，★推导）

> **文档缺口标注**：GWFD-020411 共 9 篇文档无 MML 脚本，以下命令基于 MPLS L3VPN 标准实践**推导**，需命令字典补全。

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-062` | `ADD VPNINSTANCE` | ADD | VPNINSTANCE | ★推导：MPLS VPN 实例（VRF+RD） | VPNINSTANCE, RD | EV-FK-32（推导） |
| `CMD-UDG-063` | `ADD BGPVPNV4ROUTETARGET` | ADD | BGPVPNV4ROUTETARGET | ★推导：VPN Target（MP-BGP 路由目标） | VPNINSTANCE, ROUTETARGET | EV-FK-32（推导） |
| `CMD-UDG-064` | `ADD BGPVPNV4PEER` | ADD | BGPVPNV4PEER | ★推导：MP-BGP 对等体 | VPNINSTANCE, PEERIP | EV-FK-32（推导） |

### 1.12 L2TP VPN（UDG U 面 LAC 执行，10个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-065` | `SET APNL2TPATTR` | SET | APNL2TPATTR | ★UDG L2TP APN 属性（U 面核心，10+ 参数；与 UNC APNL2TPCTRL 分离） | APN, L2TPSWITCH, SUPPORTIPV6, ...（10+ 参数） | EV-FK-21 |
| `CMD-UDG-066` | `LST APNL2TPATTR` | LST | APNL2TPATTR | L2TP APN 属性查询 | APN | EV-FK-21 |
| `CMD-UDG-067` | `ADD L2TPGROUP` | ADD | L2TPGROUP | L2TP 组（本地配置方式，LNS 容器） | L2TPGROUPID, DOMAINNAME, LNSIP | EV-FK-21 |
| `CMD-UDG-068` | `ADD L2TPLNSINFO` | ADD | L2TPLNSINFO | L2TP LNS 信息 | L2TPGROUPID, LNSINFO | EV-FK-21 |
| `CMD-UDG-069` | `ADD L2TPCLIENTIP` | ADD | L2TPCLIENTIP | L2TP 源端 Giif 绑定（本地配置方式） | L2TPGROUPID, INTFNAME | EV-FK-21 |
| `CMD-UDG-070` | `ADD L2TPRDSCLIENT` | ADD | L2TPRDSCLIENT | L2TP Radius LNS（AAA 下发方式，替代本地配置） | APN, INTFNAME, RDSLNSMODE | EV-FK-21 |
| `CMD-UDG-071` | `SET GLOBALL2TP` | SET | GLOBALL2TP | L2TP 缺省属性 | ... | EV-FK-21 |
| `CMD-UDG-072` | `SET PPPCFG` | SET | PPPCFG | PPP 协商参数 | ... | EV-FK-21 |
| `CMD-UDG-073` | `SET APNPPPACCESS` | SET | APNPPPACCESS | APN PPP 鉴权 | APN, ... | EV-FK-21 |
| `CMD-UDG-074` | `SET L2TPN4KEY` | SET | L2TPN4KEY | ★N4 接口 L2TP 加密密钥（U 侧；与 UNC L2TPKEY 须相同） | KEY | EV-FK-21 |

### 1.13 静态地址用户路由冗余（UDG，5个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-075` | `ADD REDUNDRDTIP` | ADD | REDUNDRDTIP | ★虚拟 IP（重定向业务流到 GRE Tunnel） | REDUNDRDTIP | EV-FK-20 |
| `CMD-UDG-076` | `SET REDUNDUSER` | SET | REDUNDUSER | 全局冗余开关（★与 ADD POOL REDUNDFUNC 双使能；U+C 共用） | SWITCH | EV-FK-20 |
| `CMD-UDG-077` | `SET APNREDUNDUPSW` | SET | APNREDUNDUPSW | APN 上行报文隧道转发开关（仅备用 UDG） | APN, SWITCH | EV-FK-20 |
| `CMD-UDG-078` | `ADD OSPFINTERFACE` | ADD | OSPFINTERFACE | OSPF 接口（主备 UDG 路由互通） | PROCID, IFNAME | EV-FK-20 |
| `CMD-UDG-079-1` | `MOD OSPFIMPORTROUTE` | MOD | OSPFIMPORTROUTE | 修改路由引入 COST/MED 优先级 | PROCID, COST, MED | EV-FK-20 |
| `CMD-UDG-079-2` | `MOD IMPORTROUTE` | MOD | IMPORTROUTE | 修改路由引入 COST/MED 优先级 | PROCID, COST, MED | EV-FK-20 |

### 1.14 接入控制（UDG U 面带宽流控，3个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-080` | `SET APNQOSATTR` | SET | APNQOSATTR | ★APN QoS 属性（接入控制 U 面核心；CARSHAPESWUL/DL + CARSHAPEUL/DL，上下行独立 CAR/SHAPE） | APN, CARSHAPESWUL, CARSHAPEUL(CAR/SHAPE), CARSHAPESWDL, CARSHAPEDL(CAR/SHAPE) | EV-FK-37 |
| `CMD-UDG-081` | `LST APNQOSATTR` | LST | APNQOSATTR | APN QoS 属性查询 | APN | EV-FK-37 |
| `CMD-UDG-082` | `ADD POOL` (REDUNDFUNC) | ADD | POOL | 静态冗余场景 POOL REDUNDFUNC 标识（复用 CMD-UDG-014，参数差异） | POOLNAME, REDUNDFUNC | EV-FK-20 |

### 1.15 地址自动检测与运维查询（UDG，5个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-083` | `STR PDNROUTETST` | STR | PDNROUTETST | 地址自动检测启动（无 ADD 配置，纯运维） | APN | EV-FK-19 |
| `CMD-UDG-084` | `STP PDNROUTETST` | STP | PDNROUTETST | 地址自动检测停止 | APN | EV-FK-19 |
| `CMD-UDG-085` | `DSP PDNTSTRESULT` | DSP | PDNTSTRESULT | 地址自动检测结果查询 | APN | EV-FK-19 |
| `CMD-UDG-086` | `DSP POOLUSAGE` | DSP | POOLUSAGE | 地址池使用率查询（会话管理运维） | POOLNAME | EV-FK-01, EV-FK-06 |
| `CMD-UDG-087` | `DSP SESSIONINFO` | DSP | SESSIONINFO | 会话信息查询（纯描述性底座运维） | SESSIONID | EV-FK-01, EV-FK-06 |

### 1.15a UDG 策略刷新生效（1个，★运维动作命令）

> **说明**：SET REFRESHSRV 是 UDG 侧配置链统一终点的运维动作命令（非 ADD 配置类），使地址分配/隧道/L2TP/带宽流控等策略变更下发生效。无对应 ConfigObject（动作命令，不产生配置实体）。★与 UNC 侧 CMD-UNC-087 同命令名（U+C 通用刷新命令），按产品侧分离建模以保持 command_id 编号体系（CMD-UDG / CMD-UNC）一致。

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-088` | `SET REFRESHSRV` | SET | REFRESHSRV | ★UDG 侧策略刷新生效（地址分配/隧道/L2TP/带宽流控变更后必须；配置链统一终点；Task 级 `must_be_last=true`） | （无业务参数，触发下发动作） | EV-FK-06, EV-FK-11, EV-FK-37, EV-CA-01 |

### 1.16 UNC 基础与 License（1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-001` | `SET LICENSESWITCH` | SET | LICENSESWITCH | License 开关，UNC 侧所有需 License 特性的前置门控（IPv6/ARD/UPF选择/二次鉴权/别名APN/MPLS） | LICENSECODE, SWITCH | EV-FK-19, EV-FK-27, EV-FK-31, EV-FK-36, EV-FK-05, EV-FK-34, EV-FK-27, EV-FK-33 |

### 1.17 UNC 地址池体系（UNC 侧 ADDRPOOL，7个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-002` | `ADD ADDRPOOL` | ADD | ADDRPOOL | ★UNC 地址池（★POOLTYPE 无 LOCAL，仅 UDM 静态签约；与 UDG POOL 分离建模） | ADDRPOOLNAME, POOLTYPE(UDM), IPVERSION | EV-FK-12, EV-FK-13, EV-FK-25, EV-FK-32, EV-FK-33, EV-FK-27, EV-FK-31 |
| `CMD-UNC-003` | `MOD ADDRPOOL` | MOD | ADDRPOOL | UNC 地址池修改 | ADDRPOOLNAME, ... | EV-FK-12 |
| `CMD-UNC-004` | `RMV ADDRPOOL` | RMV/DEL | ADDRPOOL | UNC 地址池删除 | ADDRPOOLNAME | EV-FK-12 |
| `CMD-UNC-005-1` | `ADD ADDRPOOLGRP` | ADD | ADDRPOOLGRP | UNC 地址池组（对应 UDG POOLGROUP） | ADDRPOOLGRPNAME | EV-FK-12, EV-FK-13, EV-FK-25, EV-FK-32, EV-FK-33 |
| `CMD-UNC-005-2` | `ADD ADDRUPGROUP` | ADD | ADDRUPGROUP | UNC 地址池组（对应 UDG POOLGROUP） | ADDRPOOLGRPNAME | EV-FK-12, EV-FK-13, EV-FK-25, EV-FK-32, EV-FK-33 |
| `CMD-UNC-006` | `ADD SECTION` | ADD | SECTION | 地址段（UNC 侧，与 UDG 同命令） | POOLNAME, SECTIONNUM, IPVERSION, V4STARTIP | EV-FK-12, EV-FK-13, EV-FK-25, EV-FK-32, EV-FK-33, EV-FK-31 |
| `CMD-UNC-007` | `ADD POOLBINDGRP` | ADD | POOLBINDGRP | UNC 地址池绑定（★UNC 命名 GRP，非 GROUP） | ADDRPOOLGRPNAME, ADDRPOOLNAME | EV-FK-12, EV-FK-13, EV-FK-25, EV-FK-32, EV-FK-33 |
| `CMD-UNC-008` | `ADD POOLBINDAPN` | ADD | POOLBINDAPN | UNC APN 绑定地址池（UNC 独有） | APN, ADDRPOOLNAME | EV-FK-12, EV-FK-13, EV-FK-25, EV-FK-32, EV-FK-33 |
| `CMD-UNC-009` | `ADD POOLGRPMAP` | ADD | POOLGRPMAP | UNC 池组映射（与 UDG 同命令） | MAPPINGNAME, APN, ADDRPOOLGRPNAME | EV-FK-12, EV-FK-13, EV-FK-25, EV-FK-32, EV-FK-33 |

### 1.18 UNC UPF 节点与绑定（地址分配共用，4个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-010` | `ADD UPNODE` | ADD | UPNODE | ★UPF 节点（共用对象：WSFD-107010 用位置特征+分流能力；WSFD-010502 用 ADDRALLOCMODE=INHERIT） | NFINSTANCENAME, ADDRALLOCMODE(INHERIT), 位置特征, 分流能力 | EV-FK-12, EV-FK-13, EV-FK-25, EV-FK-34 |
| `CMD-UNC-011` | `ADD PNFPROFILE` | ADD | PNFPROFILE | UPF NF 实例属性（WEIGHT/PRIORITY；★网元选择+地址分配共用） | NFINSTANCENAME, NFTYPE(UPF), WEIGHT, PRIORITY | EV-FK-12, EV-FK-13, EV-FK-34, EV-FK-25 |
| `CMD-UNC-012` | `ADD UPFBINDGRP` | ADD | UPFBINDGRP | UPF 绑定组（PRIORITY 控制优先级，UNC 独有） | UPGROUPNAME, NFINSTANCENAME, PRIORITY | EV-FK-12, EV-FK-13, EV-FK-25 |
| `CMD-UNC-013` | `SET STATICADDRPARA` | SET | STATICADDRPARA | 静态 IP 段绑定 UPF（★与 SMF 主锚点 UPF 选择冲突时 SMF 优先） | STATICIPSEG, NFINSTANCENAME | EV-FK-12 |

### 1.19 UNC 地址分配规则（4个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-014` | `SET APNADDRESSATTR` | SET | APNADDRESSATTR | UNC APN 地址分配属性（与 UDG 同命令名） | APN, SUPPORTIPV4, SUPPORTIPV6 | EV-FK-13, EV-FK-32, EV-FK-33, EV-FK-31 |
| `CMD-UNC-015` | `LST APNADDRESSATTR` | LST | APNADDRESSATTR | UNC APN 地址属性查询 | APN | EV-FK-13, EV-FK-32, EV-FK-33 |
| `CMD-UNC-016-1` | `SET IPALLOCRULE` | SET | IPALLOCRULE | UNC 地址分配规则（控制面侧，★同名 UDG 命令） | FIRSTRULE, ... | EV-FK-13 |
| `CMD-UNC-016-2` | `SET APNIPALLOCRULE` | SET | APNIPALLOCRULE | UNC 地址分配规则（控制面侧，★同名 UDG 命令） | FIRSTRULE, ... | EV-FK-13 |
| `CMD-UNC-016-3` | `SET ADDRESSATTR` | SET | ADDRESSATTR | UNC 地址分配规则（控制面侧，★同名 UDG 命令） | FIRSTRULE, ... | EV-FK-13 |
| `CMD-UNC-016-4` | `SET SOFTPARA` | SET | SOFTPARA | UNC 地址分配规则（控制面侧，★同名 UDG 命令） | FIRSTRULE, ... | EV-FK-13 |
| `CMD-UNC-017` | `SET IPALLOCBYLOCGLBSW` | SET | IPALLOCBYLOCGLBSW | UNC 基于位置分配全局开关（与 UDG 同命令名） | IPV4SWITCH, IPV6SWITCH | EV-FK-13 |
| `CMD-UNC-018-1` | `ADD BLACKLIST` | ADD | BLACKLIST | 静态地址黑名单 | MSISDN, IPSEG | EV-FK-12 |
| `CMD-UNC-018-2` | `LST BLACKLIST` | LST | BLACKLIST | 静态地址黑名单 | MSISDN, IPSEG | EV-FK-12 |

### 1.20 UNC UPF 选择 11 件套（WSFD-107010，11个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-019` | `ADD PNFDNN` | ADD | PNFDNN | UPF 支持的 DNN（第一轮筛选必选） | NFINSTANCENAME, DNN | EV-FK-34 |
| `CMD-UNC-020` | `ADD PNFNS` | ADD | PNFNS | UPF 支持的切片（SST+SD；★4G 接入 PNFNSINDEX=0） | NFINSTANCENAME, SST, SD, PNFNSINDEX | EV-FK-34 |
| `CMD-UNC-021` | `ADD PNFDNAI` | ADD | PNFDNAI | UPF 支持的 DNAI | NFINSTANCENAME, DNAI | EV-FK-34 |
| `CMD-UNC-022` | `ADD PNFUPFINFO` | ADD | PNFUPFINFO | UPF 信息（EPS 互通等） | NFINSTANCENAME, EPSFUPPORTED | EV-FK-34 |
| `CMD-UNC-023-1` | `ADD UPAREA` | ADD | UPAREA | UPF 位置区绑定 | NFINSTANCENAME, AREAID | EV-FK-34 |
| `CMD-UNC-023-2` | `ADD UPAREABINDN2TAI` | ADD | UPAREABINDN2TAI | UPF 位置区绑定 | NFINSTANCENAME, AREAID | EV-FK-34 |
| `CMD-UNC-023-3` | `ADD LOCBINDAREA` | ADD | LOCBINDAREA | UPF 位置区绑定 | NFINSTANCENAME, AREAID | EV-FK-34 |
| `CMD-UNC-024-1` | `ADD PNFSMFSERAREA` | ADD | PNFSMFSERAREA | UPF SMF 服务区/TAI 范围 | NFINSTANCENAME, TAI | EV-FK-34 |
| `CMD-UNC-024-2` | `ADD PNFTAIRANGE` | ADD | PNFTAIRANGE | UPF SMF 服务区/TAI 范围 | NFINSTANCENAME, TAI | EV-FK-34 |
| `CMD-UNC-024-3` | `ADD PNFTAI` | ADD | PNFTAI | UPF SMF 服务区/TAI 范围 | NFINSTANCENAME, TAI | EV-FK-34 |
| `CMD-UNC-025` | `ADD UPBINDS11` | ADD | UPBINDS11 | SGW-U 与 S11 接口绑定（4G 互操作） | NFINSTANCENAME, S11IF | EV-FK-34 |
| `CMD-UNC-026` | `ADD UPBINDGNGP` | ADD | UPBINDGNGP | GGSN/PGW-U 与 Gn/Gp 接口绑定 | NFINSTANCENAME, GNGPIF | EV-FK-34 |
| `CMD-UNC-027` | `SET UPSELECTPRI` | SET | UPSELECTPRI | UPF 选择策略次序（第二轮优选） | FIRSTPRIORITY, SECONDPRIORITY | EV-FK-34 |
| `CMD-UNC-028` | `SET UPSELECTFLAG` | SET | UPSELECTFLAG | UPF 选择开关（PRIORITYFLAG/AMBRUPFFLAG/N3UPFAPNFLAG/ULISGWFLAG） | PRIORITYFLAG, ... | EV-FK-34 |
| `CMD-UNC-029` | `SET APNUPSELPLY` | SET | APNUPSELPLY | APN 级 UPF 选择策略 | APN, COMBINEPRISTG | EV-FK-34 |
| `CMD-UNC-030` | `SET UPLOADBALANCE` | SET | UPLOADBALANCE | UPF 负载均衡（第三轮权重） | SWITCH | EV-FK-34 |

### 1.21 UNC 鉴权功能 AKA（WSFD-010301，6个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-031` | `ADD GBAUTHCIPH` | ADD | GBAUTHCIPH | 2G 鉴权加密参数（+MOD/RMV/LST） | IMSI, KI, OPC | EV-FK-26 |
| `CMD-UNC-032` | `ADD IUAUTHCIPH` | ADD | IUAUTHCIPH | 3G 鉴权加密参数（+MOD/RMV/LST） | IMSI, KI, OPC | EV-FK-26 |
| `CMD-UNC-033` | `ADD S1USRSECPARA` | ADD | S1USRSECPARA | 4G AKA 鉴权加密参数（+MOD/RMV/LST） | IMSI, KI, OPC | EV-FK-26 |
| `CMD-UNC-034` | `ADD NGUSRSECPARA` | ADD | NGUSRSECPARA | 5G AKA 鉴权加密参数（+MOD/RMV/LST） | SUPI, KI, OPC | EV-FK-26 |
| `CMD-UNC-035` | `MOD AMDATA` | MOD | AMDATA | AM 数据修改 | IMSI, ... | EV-FK-26 |
| `CMD-UNC-036` | `DSP COMMMTX` | DSP | COMMMTX | 通信上下文查询 | IMSI | EV-FK-26 |

### 1.22 UNC Radius 三件套（WSFD-011305/011306/011307，10个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-037` | `SET APNAUTHATTR` | SET | APNAUTHATTR | ★APN 鉴权属性（ACCESSMODE 4 取值，鉴权接入核心） | APN, ACCESSMODE(TRANS_NON_AUTH/TRANS_AUTH/NON_TRANS/LOC_AUTH), COMMONUSERNAME, COMMONUSERPASS | EV-FK-24 |
| `CMD-UNC-038` | `LST APNAUTHATTR` | LST | APNAUTHATTR | APN 鉴权属性查询 | APN | EV-FK-24 |
| `CMD-UNC-039` | `ADD RDSSVRGRP` | ADD | RDSSVRGRP | ★Radius 服务器组（三件套共享对象） | RDSSVRGRPNAME | EV-FK-25, EV-FK-28 |
| `CMD-UNC-040` | `ADD RDSSVR` | ADD | RDSSVR | Radius 服务器（鉴权/计费） | RDSSVRGRPNAME, SERVERTYPE(AUTHENTICATION/ACCOUNTING), PRIFLAG(PRIMARY/BACKUP/CARBON_COPY), PRIORITY | EV-FK-25, EV-FK-28 |
| `CMD-UNC-041` | `ADD APNRDSSVRGRP` | ADD | APNRDSSVRGRP | APN↔Radius 服务器组绑定 | APN, RDSSVRGRPNAME, PRIFLAG | EV-FK-25, EV-FK-28 |
| `CMD-UNC-042` | `ADD APNRDSCLIENTIP` | ADD | APNRDSCLIENTIP | APN Radius Client IP（鉴权/计费 Giif） | APN, INTFNAME, CLIENTTYPE(AUTHENTICATION/ACCOUNTING) | EV-FK-25 |
| `CMD-UNC-043` | `SET APNRDSACCTCTRL` | SET | APNRDSACCTCTRL | Radius 计费控制（SRVTRIGGER/SUPPORTACCTRSP） | APN, SRVTRIGGER, SUPPORTACCTRSP | EV-FK-25 |
| `CMD-UNC-044` | `SET APNRADIUSATTR` | SET | APNRADIUSATTR | Radius 域名增加/剥离 | APN, ... | EV-FK-25 |
| `CMD-UNC-045` | `SET RDSRSPADDRCHK` | SET | RDSRSPADDRCHK | Radius 响应端口检查 | ... | EV-FK-25 |
| `CMD-UNC-046` | `SET FHBYPASS` | SET | FHBYPASS | ★故障场景一键放通（优先级最高） | APN, SWITCH | EV-FK-25 |

### 1.23 UNC 二次鉴权（WSFD-108007，6个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-047` | `ADD UPLIST4RDS` | ADD | UPLIST4RDS | PGW-U/UPF List（按主锚点 UPF 发送 AAA；三件套+二次鉴权共用） | UPLISTNAME, UPINSTANCEID | EV-FK-25, EV-FK-28, EV-FK-27 |
| `CMD-UNC-048` | `ADD CPGTPUADDR` | ADD | CPGTPUADDR | GTP-U 地址（SMF 下发分装 GTPU 报文 IP） | IPVERSION, IPV4ADDR | EV-FK-27 |
| `CMD-UNC-049` | `ADD RDSUPFCTRL` | ADD | RDSUPFCTRL | Radius UPF 控制（PREFERENCE/LOCKED） | UPLISTNAME, UPINSTANCEID, PREFERENCE, LOCKED | EV-FK-27 |
| `CMD-UNC-050` | `ADD UPFRDSSVR` | ADD | UPFRDSSVR | ★UPF Radius 服务器（DN-AAA，★必须先于 UPFRDSCLIENTIP） | SERVERTYPE, IPVERSION, SERVERIPV4, UPLISTNAME | EV-FK-27 |
| `CMD-UNC-051` | `ADD UPFRDSCLIENTIP` | ADD | UPFRDSCLIENTIP | ★UPF Radius 客户端 IP（★必须最后执行，执行后 SMF 立即触发建链） | CLIENTYPE, IPVERSION, UPLISTNAME, VPNINSTANCE, CLIENTIPV4 | EV-FK-27 |
| `CMD-UNC-052` | `ADD NETWORKINSTVPNMAP` | ADD | NETWORKINSTVPNMAP | UPF VPN 配置（★必须先于 UPFRDSSVR/CLIENTIP） | VPNINSTANCE | EV-FK-27 |

### 1.24 UNC 接入控制 ARD/NGMM（WSFD-106003，5个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-053` | `ADD GBARD` | ADD | GBARD | 2G 接入限制（签约 ARD/APN/卡类型，+MOD/RMV/LST） | IMSI, APNNI, CARDTYPE(SIM/USIM), ARD, CTRLTYPE(ALLOW/DENY), CAUSE | EV-FK-36 |
| `CMD-UNC-054` | `ADD IUARD` | ADD | IUARD | 3G 接入限制（+MOD/RMV/LST） | IMSI, APNNI, CARDTYPE, ARD, CTRLTYPE | EV-FK-36 |
| `CMD-UNC-055` | `ADD S1ARD` | ADD | S1ARD | 4G 接入限制（+MOD/RMV/LST） | IMSI, APNNI, CARDTYPE, ARD, CTRLTYPE | EV-FK-36 |
| `CMD-UNC-056` | `ADD NGMMSUBDATA` | ADD | NGMMSUBDATA | ★5GC 接入限制（AMF 侧移动性限制，子特性 A） | USER_RANGE, IMSIPRE, RATRESTRICT, CORERESTRICT | EV-FK-36 |
| `CMD-UNC-057` | `SET NGMMPROCTRL` | SET | NGMMPROCTRL | NGMM 处理控制 | ... | EV-FK-36 |

### 1.25 UNC 别名 APN 双视角（WSFD-106203，6个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-058` | `ADD APNALIAS` | ADD | APNALIAS | ★GGSN/PGW-C/SMF 侧：别名 APN→真实 APN（资源归一；5G 先按 SST+SD 查再 ALL_USER） | SUBRANGE(ALL_USER), ALIASAPN, CONVERTAPN, SST, SD | EV-FK-05 |
| `CMD-UNC-059-1` | `MOD APNALIAS` | MOD | APNALIAS | APNALIAS 管理（+MOD/RMV/LST） | ALIASAPN | EV-FK-05 |
| `CMD-UNC-059-2` | `RMV APNALIAS` | RMV | APNALIAS | APNALIAS 管理（+MOD/RMV/LST） | ALIASAPN | EV-FK-05 |
| `CMD-UNC-059-3` | `LST APNALIAS` | LST | APNALIAS | APNALIAS 管理（+MOD/RMV/LST） | ALIASAPN | EV-FK-05 |
| `CMD-UNC-060` | `ADD ALIASAPN` | ADD | ALIASAPN | ★SGSN/MME 侧：协商 APN→别名 APN（DNS 屏蔽；双条件 IMSI 号段 AND 协商 APN） | IMSI_PREFIX, OLDAPN, NEWAPN | EV-FK-05 |
| `CMD-UNC-061-1` | `MOD ALIASAPN` | MOD | ALIASAPN | ALIASAPN 管理（+MOD/RMV/LST） | IMSI_PREFIX, OLDAPN | EV-FK-05 |
| `CMD-UNC-061-2` | `RMV ALIASAPN` | RMV | ALIASAPN | ALIASAPN 管理（+MOD/RMV/LST） | IMSI_PREFIX, OLDAPN | EV-FK-05 |
| `CMD-UNC-061-3` | `LST ALIASAPN` | LST | ALIASAPN | ALIASAPN 管理（+MOD/RMV/LST） | IMSI_PREFIX, OLDAPN | EV-FK-05 |
| `CMD-UNC-062` | `SET APNREPORTATTR` | SET | APNREPORTATTR | APN 报告属性 | APN, ... | EV-FK-05 |
| `CMD-UNC-063` | `SET DEACTIVERATE` | SET | DEACTIVERATE | 去活速率 | APN, RATE | EV-FK-05 |

### 1.26 UNC L2TP 决策（WSFD-104410，4个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-064` | `SET APNL2TPCTRL` | SET | APNL2TPCTRL | ★UNC L2TP APN 控制（C 面专用，★仅 2 参数 APN/L2TPSWITCH；与 UDG APNL2TPATTR 10+ 参数不对称） | APN, L2TPSWITCH(ENABLE/DISABLE) | EV-FK-14 |
| `CMD-UNC-065` | `LST APNL2TPCTRL` | LST | APNL2TPCTRL | L2TP APN 控制查询 | APN | EV-FK-14 |
| `CMD-UNC-066` | `SET L2TPKEY` | SET | L2TPKEY | ★N4 接口 L2TP 加密密钥（C 侧；与 UDG L2TPN4KEY 须相同） | KEY | EV-FK-14 |
| `CMD-UNC-067-1` | `SET PFCPPVTEXT` | SET | PFCPPVTEXT | PFCP 私有扩展 + UP 控制面管理（下发 LNS 参数经 N4） | ... | EV-FK-14 |
| `CMD-UNC-067-2` | `ADD UPCMPT` | ADD | UPCMPT | PFCP 私有扩展 + UP 控制面管理（下发 LNS 参数经 N4） | ... | EV-FK-14 |

### 1.27 UNC 会话管理/多 PDN（WSFD-010501/010503，6个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-068-1` | `ADD PDPAPN` | ADD | PDPAPN | 2/3G PDP APN 维护（会话管理 C 面） | APN | EV-FK-02 |
| `CMD-UNC-068-2` | `MOD PDPAPN` | MOD | PDPAPN | 2/3G PDP APN 维护（会话管理 C 面） | APN | EV-FK-02 |
| `CMD-UNC-068-3` | `RMV PDPAPN` | RMV | PDPAPN | 2/3G PDP APN 维护（会话管理 C 面） | APN | EV-FK-02 |
| `CMD-UNC-068-4` | `LST PDPAPN` | LST | PDPAPN | 2/3G PDP APN 维护（会话管理 C 面） | APN | EV-FK-02 |
| `CMD-UNC-069-1` | `SET GBSM` | SET | GBSM | 2/3G 会话管理维护 | ... | EV-FK-02 |
| `CMD-UNC-069-2` | `SET IUSM` | SET | IUSM | 2/3G 会话管理维护 | ... | EV-FK-02 |
| `CMD-UNC-069-3` | `SET SMPDUCTRL` | SET | SMPDUCTRL | 2/3G 会话管理维护 | ... | EV-FK-02 |
| `CMD-UNC-069-4` | `SET SDCFG` | SET | SDCFG | 2/3G 会话管理维护 | ... | EV-FK-02 |
| `CMD-UNC-069-5` | `SET SMFUNC` | SET | SMFUNC | 2/3G 会话管理维护 | ... | EV-FK-02 |
| `CMD-UNC-069-6` | `SET CHGCHAR` | SET | CHGCHAR | 2/3G 会话管理维护 | ... | EV-FK-02 |
| `CMD-UNC-070` | `ADD APNACTNUM` | ADD | APNACTNUM | ★单 APN 并发限制（PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM + PDNCONNREJCAUSE） | APN, PDNNUM, IPV4ADDRNUM, IPV6ADDRNUM, PDNCONNREJCAUSE | EV-FK-03 |
| `CMD-UNC-071-1` | `MOD APNACTNUM` | MOD | APNACTNUM | 单 APN 并发限制管理 | APN | EV-FK-03 |
| `CMD-UNC-071-2` | `RMV APNACTNUM` | RMV | APNACTNUM | 单 APN 并发限制管理 | APN | EV-FK-03 |
| `CMD-UNC-071-3` | `LST APNACTNUM` | LST | APNACTNUM | 单 APN 并发限制管理 | APN | EV-FK-03 |

### 1.28 UNC 用户数据管理（WSFD-010400，2个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-072` | `SET SDBTMR` | SET | SDBTMR | 签约数据库定时器 | ... | EV-FK-04 |
| `CMD-UNC-073` | `SET SYS` | SET | SYS | 系统配置（SUBSTORAG 存储分拆） | SUBSTORAG | EV-FK-04 |

### 1.29 UNC IPv6 承载 SM 子表（WSFD-104001/104002/104004，3个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-074-1` | `ADD SMSUBDATA` | ADD | SMSUBDATA | SM 子表数据（UNC IPv6 承载） | IMSI, ... | EV-FK-19, EV-FK-27, EV-FK-31 |
| `CMD-UNC-074-2` | `MOD SMSUBDATA` | MOD | SMSUBDATA | SM 子表数据（UNC IPv6 承载） | IMSI, ... | EV-FK-19, EV-FK-27, EV-FK-31 |
| `CMD-UNC-074-3` | `RMV SMSUBDATA` | RMV | SMSUBDATA | SM 子表数据（UNC IPv6 承载） | IMSI, ... | EV-FK-19, EV-FK-27, EV-FK-31 |
| `CMD-UNC-075` | `SET SMFUNC` | SET | SMFUNC | SM 功能（IPv6 承载） | ... | EV-FK-19, EV-FK-27, EV-FK-31 |
| `CMD-UNC-076` | `MOD GTPCCMPT` | MOD | GTPCCMPT | GTP-C 控制（IPv6 承载） | ... | EV-FK-19, EV-FK-27, EV-FK-31 |

### 1.30 UNC DHCP（WSFD-104413/104005，5个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-077` | `ADD DHCPBINDPOOLGRP` | ADD | DHCPBINDPOOLGRP | DHCP 池组绑定 | POOLGRPNAME | EV-FK-22, EV-FK-23 |
| `CMD-UNC-078-1` | `ADD DHCPSERVER` | ADD | DHCPSERVER | DHCP 服务器 + 服务器组 | SERVERNAME, GROUPNAME | EV-FK-22, EV-FK-23 |
| `CMD-UNC-078-2` | `ADD DHCPSERVERGRP` | ADD | DHCPSERVERGRP | DHCP 服务器 + 服务器组 | SERVERNAME, GROUPNAME | EV-FK-22, EV-FK-23 |
| `CMD-UNC-079` | `ADD AGENTIP` | ADD | AGENTIP | DHCP Agent IP | AGENTIP | EV-FK-22, EV-FK-23 |
| `CMD-UNC-080` | `SET DHCPPARAREQ` | SET | DHCPPARAREQ | DHCP 参数请求 | ... | EV-FK-22, EV-FK-23 |

### 1.31 UNC 对等网元选择（WSFD-010202，4个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-081` | `ADD AREADNS` | ADD | AREADNS | ★位置区域 DNS 域名定制（LAC/RAC/TAC + ZONESW；+MOD/RMV/LST） | AREAID, LAC, RAC, TAC, ZONESW | EV-FK-35 |
| `CMD-UNC-082-1` | `ADD DNSN` | ADD | DNSN | DNS 配置（SGSN/MME） | DNSNAME | EV-FK-35 |
| `CMD-UNC-082-2` | `ADD IPV4DNSH` | ADD | IPV4DNSH | DNS 配置（SGSN/MME） | DNSNAME | EV-FK-35 |
| `CMD-UNC-082-3` | `ADD SGSNDNS` | ADD | SGSNDNS | DNS 配置（SGSN/MME） | DNSNAME | EV-FK-35 |
| `CMD-UNC-083` | `SET MSCSELPLCY` | SET | MSCSELPLCY | MSC 选择策略（SRVCC 基于 RAI/LAI FQDN） | ... | EV-FK-35 |

### 1.32 UNC 静态路由冗余（WSFD-107021，1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-084` | `SET REDUNDUSER` | SET | REDUNDUSER | ★静态路由冗余全局开关（UNC 侧；★与 UDG 同命令，U+C 共用对象） | SWITCH | EV-FK-25 |

### 1.33 UNC VPN 与逻辑接口（共用，2个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-085` | `ADD VPNINST` | ADD | VPNINST | UNC VPN 实例（Radius 鉴权/二次鉴权用 AAA VPN） | VPNINSTNAME | EV-FK-25, EV-FK-28, EV-FK-27 |
| `CMD-UNC-086-1` | `ADD LOGICIP` | ADD | LOGICIP | UNC Gi 逻辑接口（giif1/0/0 鉴权 AAA / giif1/0/1 计费 AAA） | IFNAME, LOGICIP | EV-FK-25, EV-FK-28, EV-FK-27 |
| `CMD-UNC-086-2` | `ADD LOGICINF` | ADD | LOGICINF | UNC Gi 逻辑接口（giif1/0/0 鉴权 AAA / giif1/0/1 计费 AAA） | IFNAME, LOGICIP | EV-FK-25, EV-FK-28, EV-FK-27 |

### 1.33a UNC 策略刷新生效（1个，★运维动作命令）

> **说明**：SET REFRESHSRV 是 UNC 侧配置链统一终点的运维动作命令（非 ADD 配置类），使 Radius 鉴权级联链 / UPF 选择三轮筛选 / ARD 接入控制等 C 面策略变更下发生效。无对应 ConfigObject（动作命令，不产生配置实体）。★与 UDG 侧 CMD-UDG-088 同命令名（U+C 通用刷新命令），按产品侧分离建模。

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-087` | `SET REFRESHSRV` | SET | REFRESHSRV | ★UNC 侧策略刷新生效（Radius/UPF 选择/ARD 接入控制变更后必须；C 面配置链统一终点；Task 级 `must_be_last=true`） | （无业务参数，触发下发动作） | EV-FK-24, EV-FK-25, EV-FK-34, EV-FK-36, EV-CA-01 |

> **说明**：ADD APN 在 UDG 已实例化（CMD-UDG-009），UNC 侧复用同命令族（不再独立编号），支撑别名 APN 等场景前置依赖。

---

## 2. ConfigObject 实例化（~65 个）

### 2.1 地址分配域 UDG 侧（13个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-POOL-U` | POOL | UDG | entity | POOLNAME | POOLTYPE(LOCAL/EXTERNAL), IPVERSION, HASVPN, VPNINSTANCE, REDUNDFUNC | belongs_to POOLGROUP |
| `OBJ-SECTION` | SECTION | 共用 | entity | POOLNAME, SECTIONNUM | IPVERSION, V4STARTIP/V4ENDIP, V6PREFIXSTART/END, V6PREFIXLENGTH | belongs_to POOL/ADDRPOOL |
| `OBJ-POOLGROUP` | POOLGROUP | UDG | composite | POOLGRPNAME | IPV4ALLOCPRIALG, IPV6ALLOCPRIALG | **contains** POOL（via POOLBINDGROUP） |
| `OBJ-POOLBINDGROUP` | POOLBINDGROUP | UDG | binding | POOLGROUPNAME, POOLNAME | PRIORITY | links POOL to POOLGROUP |
| `OBJ-POOLGRPMAP-U` | POOLGRPMAP | UDG | binding | MAPPINGNAME | APN, POOLGROUPNAME | links APN+POOLGROUP |
| `OBJ-APN-U` | APN | UDG | entity | APN | HASVPN, VPNINSTANCE, HASVPNIPV6, VPNINSTANCEIPV6 | refers_to VPNINST |
| `OBJ-APNADDRESSATTR-U` | APNADDRESSATTR | UDG | entity | APN | SUPPORTIPV4, SUPPORTIPV6, IGNOREV4, V6POOLID, HOSTROUTEIP | belongs_to APN |
| `OBJ-IPALLOCRULE-U` | IPALLOCRULE | UDG | entity | — | FIRSTRULE, SECONDRULE, THIRDRULE | — |
| `OBJ-APNIPALLOCRULE` | APNIPALLOCRULE | UDG | entity | APN | FIRSTRULE（覆盖全局） | belongs_to APN |
| `OBJ-CPNODEID` | CPNODEID | UDG | entity | NODEID | — | refers_to POOLGRPMAP（SMF 分配子方式） |
| `OBJ-IPALLOCBYSMFGLBSW` | IPALLOCBYSMFGLBSW | UDG | entity | — | SWITCH | activates OBJ-IPALLOCRULE（SMF 分配子方式） |
| `OBJ-LACGROUP` / `OBJ-TACGROUP` | LACGROUP/TACGROUP | UDG | composite | GROUPNAME | LAC/TAC ID 集合 | **contains** LACID/TACID |
| `OBJ-IPALLOCBYLOCGLBSW-U` | IPALLOCBYLOCGLBSW | UDG | entity | — | IPV4SWITCH, IPV6SWITCH | activates OBJ-IPALLOCRULE（位置子方式） |
| `OBJ-ADRLOCWHITELST` | ADRLOCWHITELST | UDG | entity | MSISDN | — | refers_to LACGROUP/TACGROUP |
| `OBJ-CONFLICTIP` | CONFLICTIP/CONFLICTIPV6 | UDG | entity | CONFLICTIP | — | — |

### 2.2 地址分配域 UNC 侧（9个，★与 UDG 分离建模）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-ADDRPOOL` | ADDRPOOL | UNC | entity | ADDRPOOLNAME | POOLTYPE(UDM 静态), IPVERSION | belongs_to ADDRPOOLGRP |
| `OBJ-ADDRPOOLGRP` | ADDRPOOLGRP | UNC | composite | ADDRPOOLGRPNAME | — | **contains** ADDRPOOL（via POOLBINDGRP） |
| `OBJ-POOLBINDGRP` | POOLBINDGRP | UNC | binding | ADDRPOOLGRPNAME, ADDRPOOLNAME | PRIORITY | links ADDRPOOL to ADDRPOOLGRP |
| `OBJ-POOLGRPMAP-C` | POOLGRPMAP | UNC | binding | MAPPINGNAME | APN, ADDRPOOLGRPNAME | links APN+ADDRPOOLGRP |
| `OBJ-APNADDRESSATTR-C` | APNADDRESSATTR | UNC | entity | APN | SUPPORTIPV4, SUPPORTIPV6 | belongs_to APN（UNC 侧复用 ADD APN） |
| `OBJ-IPALLOCRULE-C` | IPALLOCRULE | UNC | entity | — | FIRSTRULE | — |
| `OBJ-UPNODE` | UPNODE | UNC | entity | NFINSTANCENAME | ADDRALLOCMODE(INHERIT), 位置特征, 分流能力 | ★refers_to PNFPROFILE（共用对象） |
| `OBJ-PNFPROFILE` | PNFPROFILE | UNC | entity | NFINSTANCENAME | NFTYPE(UPF), WEIGHT, PRIORITY | refers_to UPFBINDGRP |
| `OBJ-UPFBINDGRP` | UPFBINDGRP | UNC | binding | UPGROUPNAME, NFINSTANCENAME | PRIORITY | links PNFPROFILE to ADDRPOOLGRP |
| `OBJ-STATICADDRPARA` | STATICADDRPARA | UNC | entity | STATICIPSEG, NFINSTANCENAME | — | conflicts_with SMF 主锚点 UPF 选择（FR-SMF主锚点优先） |
| `OBJ-BLACKLIST` | BLACKLIST | UNC | entity | MSISDN, IPSEG | — | — |

### 2.3 隧道类 GRE（3个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-GRETUNNEL` | GRETUNNEL | GRE/静态冗余 | entity | TNLNAME, TNLTYPE(gre) | SRCTYPE, SRCIFNAME, DSTIPADDR, CHECKSUMEN, GREKEYEN, GREKEY, KEEPALVEN | refers_to LoopBack/Tunnel 接口 |
| `OBJ-LOOPBACK` | LoopBack 接口 | GRE/IPSec | entity | IFNAME | IFIPADDR | — |
| `OBJ-TUNNELIF` | Tunnel 接口 | GRE/IPSec | entity | IFNAME | TNLTYPE | refers_to GRETUNNEL/IPSECPOLICY |

### 2.4 隧道类 IPSec（9个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-ACLGROUPIPSEC` | ACLGROUPIPSEC | IPSec | composite | ACLGROUPNAME | — | **contains** ACLRULEADV4IPSEC |
| `OBJ-ACLRULEADV4IPSEC` | ACLRULEADV4IPSEC | IPSec | entity | ACLGROUPNAME, RULEID | SRCIP, DSTIP（★仅源/目的 IP） | belongs_to ACLGROUPIPSEC |
| `OBJ-IPSECPROPOSALIPSEC` | IPSECPROPOSALIPSEC | IPSec | entity | PROPOSALNAME | ENCAPSULATIONMODE(TUNNEL/TRANSPORT), SECURITYPROTOCOL(AH/ESP) | — |
| `OBJ-IKEPROPOSAL` | IKEPROPOSAL | IPSec | entity | PROPOSALNAME | AUTHMETHOD(PSK), DHGROUP（★不能 None） | — |
| `OBJ-IKEPEER` | IKEPEER | IPSec | entity | PEERNAME | PRESHAREDKEY, EXCHANGEMODE, REMOTEADDR, NATTRAVERSAL, VERSION1 | — |
| `OBJ-IPSECPOLICY` | IPSECPOLICY | IPSec | composite | POLICYNAME, SEQ | MODE(ISAKMP) | **contains** ACLGROUPIPSEC, IPSECPROPOSALIPSEC, IKEPEER |
| `OBJ-PROPATTACHIPSECPROPOSAL` | PROPATTACHIPSECPROPOSAL | IPSec | binding | POLICYNAME, SEQ, PROPOSALNAME | — | links IPSECPOLICY to IPSECPROPOSALIPSEC |
| `OBJ-ATTACHIKEPEER` | ATTACHIKEPEER | IPSec | binding | POLICYNAME, SEQ, PEERNAME | PRIORITY | links IPSECPOLICY to IKEPEER |
| `OBJ-IPSECINTFCFGIPSEC` | IPSECINTFCFGIPSEC | IPSec | binding | IFNAME, TNLTYPE(IPSEC) | POLICYNAME | links Tunnel 接口 to IPSECPOLICY |

### 2.5 隧道类 MPLS（3个，★推导）

> **文档缺口标注**：GWFD-020411 共 9 篇无 MML 脚本，以下对象基于 MPLS L3VPN 标准实践**推导**。

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-VPNINSTANCE` | VPNINSTANCE | MPLS | entity | VPNINSTANCE | RD | ★推导 |
| `OBJ-BGPVPNV4ROUTETARGET` | BGPVPNV4ROUTETARGET | MPLS | entity | VPNINSTANCE, ROUTETARGET | — | belongs_to VPNINSTANCE（★推导） |
| `OBJ-BGPVPNV4PEER` | BGPVPNV4PEER | MPLS | entity | VPNINSTANCE, PEERIP | — | belongs_to VPNINSTANCE（★推导） |

### 2.6 隧道类 L2TP（8个，U+C 分离）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-APNL2TPATTR` | APNL2TPATTR | **UDG** | entity | APN | L2TPSWITCH, SUPPORTIPV6, ...（★10+ 参数） | belongs_to APN（U 面 LAC 执行） |
| `OBJ-APNL2TPCTRL` | APNL2TPCTRL | **UNC** | entity | APN | L2TPSWITCH（★仅 2 参数） | belongs_to APN（C 面决策） |
| `OBJ-L2TPGROUP` | L2TPGROUP | UDG | composite | L2TPGROUPID | DOMAINNAME, LNSIP | **contains** L2TPLNSINFO, L2TPCLIENTIP |
| `OBJ-L2TPLNSINFO` | L2TPLNSINFO | UDG | entity | L2TPGROUPID | LNSINFO | belongs_to L2TPGROUP |
| `OBJ-L2TPCLIENTIP` | L2TPCLIENTIP | UDG | binding | L2TPGROUPID, INTFNAME | — | links L2TPGROUP to LOGICINF |
| `OBJ-L2TPRDSCLIENT` | L2TPRDSCLIENT | UDG | binding | APN, INTFNAME | RDSLNSMODE | refers_to LOGICINF（AAA 下发方式，互斥 L2TPGROUP） |
| `OBJ-GLOBALL2TP` | GLOBALL2TP | UDG | entity | — | L2TP 缺省属性 | — |
| `OBJ-PPPCFG` | PPPCFG | UDG | entity | — | PPP 协商参数 | — |
| `OBJ-L2TPN4KEY` | L2TPN4KEY | **UDG** | entity | — | KEY（N4 加密） | refers_to OBJ-L2TPKEY（★U+C 密钥须相同） |
| `OBJ-L2TPKEY` | L2TPKEY | **UNC** | entity | — | KEY（N4 加密） | refers_to OBJ-L2TPN4KEY（★U+C 密钥须相同） |

### 2.7 鉴权 AKA 系列（4个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-GBAUTHCIPH` | GBAUTHCIPH | AKA 2G | entity | IMSI | KI, OPC | — |
| `OBJ-IUAUTHCIPH` | IUAUTHCIPH | AKA 3G | entity | IMSI | KI, OPC | — |
| `OBJ-S1USRSECPARA` | S1USRSECPARA | AKA 4G | entity | IMSI | KI, OPC | — |
| `OBJ-NGUSRSECPARA` | NGUSRSECPARA | AKA 5G | entity | SUPI | KI, OPC | — |

### 2.8 鉴权 Radius 系列（9个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-APNAUTHATTR` | APNAUTHATTR | Radius 接入 | entity | APN | ACCESSMODE(4取值), COMMONUSERNAME/PASS | belongs_to APN |
| `OBJ-RDSSVRGRP` | RDSSVRGRP | Radius 三件套 | composite | RDSSVRGRPNAME | — | **contains** RDSSVR（★三件套共享：011306/011305/011307） |
| `OBJ-RDSSVR` | RDSSVR | Radius 三件套 | entity | RDSSVRGRPNAME, SERVERTYPE | PRIFLAG(PRIMARY/BACKUP/CARBON_COPY), PRIORITY | belongs_to RDSSVRGRP |
| `OBJ-APNRDSSVRGRP` | APNRDSSVRGRP | Radius 三件套 | binding | APN, RDSSVRGRPNAME | PRIFLAG | links APN to RDSSVRGRP |
| `OBJ-APNRDSCLIENTIP` | APNRDSCLIENTIP | Radius 功能 | binding | APN, INTFNAME, CLIENTTYPE | — | links APN to LOGICINF |
| `OBJ-APNRDSACCTCTRL` | APNRDSACCTCTRL | Radius 功能 | entity | APN | SRVTRIGGER, SUPPORTACCTRSP | — |
| `OBJ-APNRADIUSATTR` | APNRADIUSATTR | Radius 功能 | entity | APN | 域名增加/剥离 | — |
| `OBJ-UPLIST4RDS` | UPLIST4RDS | 三件套+二次鉴权 | composite | UPLISTNAME | UPINSTANCEID | **contains** UPFRDSSVR, UPFRDSCLIENTIP |
| `OBJ-FHBYPASS` | FHBYPASS | Radius 功能 | entity | APN | SWITCH（★故障一键放通，优先级最高） | — |

### 2.9 二次鉴权 UPF Radius 系列（5个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-CPGTPUADDR` | CPGTPUADDR | 二次鉴权 | entity | IPVERSION | IPV4ADDR | — |
| `OBJ-RDSUPFCTRL` | RDSUPFCTRL | 二次鉴权 | entity | UPLISTNAME, UPINSTANCEID | PREFERENCE, LOCKED | refers_to UPLIST4RDS |
| `OBJ-UPFRDSSVR` | UPFRDSSVR | 二次鉴权 | entity | SERVERTYPE, IPVERSION | SERVERIPV4, UPLISTNAME | belongs_to UPLIST4RDS（★必须先于 UPFRDSCLIENTIP） |
| `OBJ-UPFRDSCLIENTIP` | UPFRDSCLIENTIP | 二次鉴权 | binding | CLIENTYPE, UPLISTNAME | VPNINSTANCE, CLIENTIPV4 | belongs_to UPLIST4RDS（★必须最后执行） |
| `OBJ-NETWORKINSTVPNMAP` | NETWORKINSTVPNMAP | 二次鉴权前置 | binding | VPNINSTANCE | — | refers_to UPF VPN（★必须先于 UPFRDSSVR/CLIENTIP） |

### 2.10 接入控制 ARD/NGMM（5个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-GBARD` | GBARD | ARD 2G | entity | IMSI, APNNI | CARDTYPE, ARD, CTRLTYPE, CAUSE | — |
| `OBJ-IUARD` | IUARD | ARD 3G | entity | IMSI, APNNI | CARDTYPE, ARD, CTRLTYPE | — |
| `OBJ-S1ARD` | S1ARD | ARD 4G | entity | IMSI, APNNI | CARDTYPE, ARD, CTRLTYPE | — |
| `OBJ-NGMMSUBDATA` | NGMMSUBDATA | NGMM 子特性 A | entity | USER_RANGE, IMSIPRE | RATRESTRICT, CORERESTRICT | — |
| `OBJ-NGMMPROCTRL` | NGMMPROCTRL | NGMM | entity | — | — | — |
| `OBJ-APNQOSATTR` | APNQOSATTR | 接入控制 U | entity | APN | CARSHAPESWUL/DL, CARSHAPEUL/DL(CAR/SHAPE) | belongs_to APN（★U 面带宽流控，与 C 面 ARD 分离） |

### 2.11 别名 APN 双视角（3个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-APNALIAS` | APNALIAS | 别名 GGSN/PGW-C/SMF | entity | SUBRANGE, ALIASAPN | CONVERTAPN, SST, SD | refers_to APN（转换后 APN 必须已 ADD APN） |
| `OBJ-ALIASAPN` | ALIASAPN | 别名 SGSN/MME | entity | IMSI_PREFIX, OLDAPN | NEWAPN | — |
| `OBJ-APNREPORTATTR` | APNREPORTATTR | 别名 APN | entity | APN | — | belongs_to APN |

### 2.12 UPF 选择 11 件套（11个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-PNFDNN` | PNFDNN | UPF 选择 | entity | NFINSTANCENAME, DNN | — | belongs_to PNFPROFILE |
| `OBJ-PNFNS` | PNFNS | UPF 选择 | entity | NFINSTANCENAME, SST, SD | PNFNSINDEX（★4G=0） | belongs_to PNFPROFILE |
| `OBJ-PNFDNAI` | PNFDNAI | UPF 选择 | entity | NFINSTANCENAME, DNAI | — | belongs_to PNFPROFILE |
| `OBJ-PNFUPFINFO` | PNFUPFINFO | UPF 选择 | entity | NFINSTANCENAME | EPSFUPPORTED | belongs_to PNFPROFILE |
| `OBJ-UPAREA` | UPAREA/UPAREABINDN2TAI/LOCBINDAREA | UPF 选择 | entity | NFINSTANCENAME, AREAID | — | belongs_to PNFPROFILE |
| `OBJ-PNFSMFSERAREA` | PNFSMFSERAREA/PNFTAIRANGE/PNFTAI | UPF 选择 | entity | NFINSTANCENAME, TAI | — | belongs_to PNFPROFILE |
| `OBJ-UPBINDS11` | UPBINDS11 | UPF 选择 4G | binding | NFINSTANCENAME, S11IF | — | links PNFPROFILE to S11 |
| `OBJ-UPBINDGNGP` | UPBINDGNGP | UPF 选择 Gn/Gp | binding | NFINSTANCENAME, GNGPIF | — | links PNFPROFILE to GnGp |
| `OBJ-UPSELECTPRI` | UPSELECTPRI | UPF 选择第二轮 | entity | — | FIRSTPRIORITY, SECONDPRIORITY | — |
| `OBJ-UPSELECTFLAG` | UPSELECTFLAG | UPF 选择第二轮 | entity | — | PRIORITYFLAG, AMBRUPFFLAG, N3UPFAPNFLAG, ULISGWFLAG | — |
| `OBJ-APNUPSELPLY` | APNUPSELPLY | UPF 选择 | entity | APN | COMBINEPRISTG | belongs_to APN |
| `OBJ-UPLOADBALANCE` | UPLOADBALANCE | UPF 选择第三轮 | entity | — | SWITCH | — |

### 2.13 底座/会话管理/用户数据/其他（7个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------|---------------|----------|----------|---------------|
| `OBJ-APNACTNUM` | APNACTNUM | 多 PDN | entity | APN | PDNNUM, IPV4ADDRNUM, IPV6ADDRNUM, PDNCONNREJCAUSE | belongs_to APN |
| `OBJ-PDPAPN` | PDPAPN | 会话管理 2/3G | entity | APN | — | — |
| `OBJ-SMSUBDATA` | SMSUBDATA | IPv6 承载 | entity | IMSI | — | — |
| `OBJ-SDBTMR` | SDBTMR | 用户数据 | entity | — | 定时器 | — |
| `OBJ-AREADNS` | AREADNS | 对等网元 | entity | AREAID | LAC, RAC, TAC, ZONESW | — |
| `OBJ-REDUNDRDTIP` | REDUNDRDTIP | 静态冗余 | entity | REDUNDRDTIP | — | refers_to GRETUNNEL |
| `OBJ-REDUNDUSER` | REDUNDUSER | 静态冗余 | entity | — | SWITCH（★U+C 共用对象） | activates OBJ-POOL REDUNDFUNC |

---

## 3. ConfigObject 间关系边（§11.7 contains / refers_to / depends_on / conflicts_with / composed_by / activates）

> **Schema 参考**：§11.7 `ConfigObject contains / refers_to / depends_on / conflicts_with / composed_by / activates ConfigObject` 直接作为边，不建实体。

### 3.1 contains 边（组合/包含关系，22条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| POOLGROUP | `contains` | POOL | UDG 地址池组包含地址池（via POOLBINDGROUP） |
| ADDRPOOLGRP | `contains` | ADDRPOOL | UNC 地址池组包含地址池（via POOLBINDGRP） |
| POOL / ADDRPOOL | `contains` | SECTION | 地址池包含地址段（V4STARTIP/V6PREFIXSTART，V6PREFIXLENGTH<64=PD） |
| POOLGRPMAP | `contains` | POOLGROUP / ADDRPOOLGRP | 池组映射关联池组（APN/SMF/LOCATION 任意组合） |
| LACGROUP | `contains` | LACID | LAC 位置区组包含 LAC ID（2/3G） |
| TACGROUP | `contains` | TACID | TAC 位置区组包含 TAC ID（4/5G） |
| ACLGROUPIPSEC | `contains` | ACLRULEADV4IPSEC | IPSec ACL 组包含规则（★仅源/目的 IP） |
| IPSECPOLICY | `contains` | ACLGROUPIPSEC | IPSec 策略聚合 ACL |
| IPSECPOLICY | `contains` | IPSECPROPOSALIPSEC | IPSec 策略绑定 Proposal（via PROPATTACHIPSECPROPOSAL） |
| IPSECPOLICY | `contains` | IKEPEER | IPSec 策略绑定 IKE Peer（via ATTACHIKEPEER） |
| L2TPGROUP | `contains` | L2TPLNSINFO | L2TP 组包含 LNS 信息 |
| L2TPGROUP | `contains` | L2TPCLIENTIP | L2TP 组包含源端 Giif 绑定（本地配置方式） |
| RDSSVRGRP | `contains` | RDSSVR | Radius 服务器组包含服务器（★三件套共享对象） |
| UPLIST4RDS | `contains` | UPFRDSSVR | UP List 包含 UPF Radius 服务器（二次鉴权） |
| UPLIST4RDS | `contains` | UPFRDSCLIENTIP | UP List 包含 UPF Radius 客户端 IP |
| VPNINSTANCE | `contains` | BGPVPNV4ROUTETARGET | ★推导：MPLS VPN 实例包含 Route Target |
| VPNINSTANCE | `contains` | BGPVPNV4PEER | ★推导：MPLS VPN 实例包含 MP-BGP 对等体 |
| PNFPROFILE | `contains` | PNFDNN/PNFNS/PNFDNAI/PNFUPFINFO | UPF NF 实例包含支持的 DNN/切片/DNAI/EPS 信息（第一轮筛选） |
| PNFPROFILE | `contains` | UPAREA/PNFSMFSERAREA/PNFTAI | UPF NF 实例包含位置区信息 |
| APN | `contains` | APNADDRESSATTR / APNAUTHATTR / APNL2TPATTR / APNL2TPCTRL / APNQOSATTR / APNACTNUM | APN 是跨域共用挂载点（地址/鉴权/L2TP/接入控制/多 PDN 均挂 APN） |

### 3.2 refers_to 边（引用关系，16条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| POOL | `refers_to` | VPNINST | UDG 地址池引用 VPN 实例（HASVPN=ENABLE） |
| APN | `refers_to` | VPNINST / L3VPNINST | APN 引用 VPN（IPv4 + IPv6 双实例） |
| GRETUNNEL | `refers_to` | LoopBack 接口 | GRE 隧道源接口（推荐 LoopBack） |
| IPSECINTFCFGIPSEC | `refers_to` | IPSECPOLICY | Tunnel 接口引用 IPSec 策略 |
| APNRDSSVRGRP | `refers_to` | RDSSVRGRP | APN 绑定引用 Radius 服务器组 |
| APNRDSCLIENTIP | `refers_to` | LOGICINF | APN Radius Client IP 引用 Giif |
| RDSUPFCTRL | `refers_to` | UPLIST4RDS | Radius UPF 控制引用 UP List |
| UPFRDSSVR | `refers_to` | UPLIST4RDS | UPF Radius 服务器引用 UP List |
| NETWORKINSTVPNMAP | `refers_to` | UPFRDSSVR / UPFRDSCLIENTIP | UPF VPN 配置引用 UPF Radius（★前置依赖） |
| UPNODE | `refers_to` | PNFPROFILE | UPF 节点引用 NF 实例属性（★共用对象） |
| UPFBINDGRP | `refers_to` | PNFPROFILE | UPF 绑定组引用 NF 实例 |
| APNALIAS | `refers_to` | APN | 别名 APN 引用真实 APN（转换后 APN 必须已 ADD APN） |
| REDUNDRDTIP | `refers_to` | GRETUNNEL | 虚拟 IP 引用 GRE Tunnel（重定向业务流） |
| ADRLOCWHITELST | `refers_to` | LACGROUP / TACGROUP | 白名单引用位置区组 |
| CPNODEID | `refers_to` | POOLGRPMAP | SMF NodeID 引用池组映射（基于 SMF 分配子方式） |
| L2TPCLIENTIP / L2TPRDSCLIENT | `refers_to` | LOGICINF | L2TP 源端绑定 Giif |

### 3.3 depends_on 边（依赖关系，9条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| UPFRDSCLIENTIP | `depends_on` | UPFRDSSVR | ★二次鉴权强顺序：UPF Radius 服务器必须先于客户端 IP |
| UPFRDSSVR / UPFRDSCLIENTIP | `depends_on` | NETWORKINSTVPNMAP | UPF VPN 配置必须先于 Radius 服务器/客户端 |
| ADDRPOOLGRP | `depends_on` | ADDRPOOL | UNC 地址池组依赖地址池存在 |
| POOLGROUP | `depends_on` | POOL | UDG 地址池组依赖地址池存在 |
| IPSECPOLICY | `depends_on` | IPSECPROPOSALIPSEC / IKEPEER / ACLGROUPIPSEC | IPSec 策略依赖提议+对等体+ACL |
| IPSECINTFCFGIPSEC | `depends_on` | IPSECPOLICY | 应用策略到 Tunnel 依赖策略已存在 |
| OBJ-APNL2TPATTR | `depends_on` | OBJ-L2TPN4KEY | L2TP 加密两端密钥须相同（U+C 跨产品依赖） |
| OBJ-APNL2TPCTRL | `depends_on` | OBJ-L2TPKEY | L2TP 加密两端密钥须相同 |
| OBJ-PNFPROFILE 子对象 | `depends_on` | OBJ-PNFPROFILE | PNFDNN/PNFNS/PNFDNAI/PNFUPFINFO 依赖 PNFPROFILE 主对象 |

### 3.4 conflicts_with 边（互斥关系，3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| OBJ-L2TPGROUP | `conflicts_with` | OBJ-L2TPRDSCLIENT | L2TP 本地配置方式与 AAA 下发方式互斥 |
| OBJ-STATICADDRPARA | `conflicts_with` | SMF 主锚点 UPF 选择 | 静态 IP 段绑定 UPF 与 SMF 主锚点 UPF 选择冲突时，**SMF 选择优先**（FR-SMF主锚点优先） |
| OBJ-GRETUNNEL 源地址 | `conflicts_with` | OBJ-IPSECINTFCFGIPSEC 源地址 | GRE 隧道源地址不能与 IPSec 隧道源地址相同（FR-GRE-IPSEC-SRC-EXCL） |

### 3.5 activates 边（激活/使能关系，4条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| OBJ-IPALLOCBYSMFGLBSW | `activates` | OBJ-IPALLOCRULE | 基于 SMF 分配全局开关激活三级规则（SMF 分配子方式） |
| OBJ-IPALLOCBYLOCGLBSW | `activates` | OBJ-IPALLOCRULE | 基于位置分配全局开关激活三级规则（位置子方式） |
| OBJ-REDUNDUSER | `activates` | OBJ-POOL (REDUNDFUNC) | 全局冗余开关与 POOL REDUNDFUNC 双使能（静态路由冗余） |
| OBJ-FHBYPASS | `activates` | OBJ-RDSSVRGRP（故障放通） | 故障场景一键放通优先级最高（绕过 Radius） |

### 3.6 composed_by 边（由...组合，1条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| OBJ-IPSECPOLICY | `composed_by` | OBJ-IPSECPROPOSALIPSEC + OBJ-IKEPEER + OBJ-ACLGROUPIPSEC | IPSec 策略由提议+对等体+ACL 组合而成 |

---

## 4. CommandRule 实例化（18条）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-APN-01` | POOL(UDG) vs ADDRPOOL(UNC) 前缀不对称 | `object_reference_rule` | explicit | config | object | OBJ-POOL-U / OBJ-ADDRPOOL | UDG 用 ADD POOL（POOLTYPE=LOCAL），UNC 用 ADD ADDRPOOL（POOLTYPE=UDM 静态）；两侧命令前缀不对称，ConfigObject 必须分离建模，避免规则匹配混淆 | 命令误用导致地址池无法识别或分配失败 | critical | EV-FK-06, EV-FK-12 |
| `CR-APN-02` | APNL2TPATTR(U,10+参数) vs APNL2TPCTRL(C,2参数) 不对称 | `parameter_dependency` | explicit | config | parameter | CMD-UDG-065 / CMD-UNC-064 | UDG SET APNL2TPATTR 有 10+ 参数（L2TPSWITCH/SUPPORTIPV6/...）；UNC SET APNL2TPCTRL 仅 2 参数（APN/L2TPSWITCH）；C 决策 U 执行模式典型不对称 | 参数集不匹配导致 L2TP 隧道建链失败 | critical | EV-FK-21, EV-FK-14 |
| `CR-APN-03` | L2TPN4KEY(U) 与 L2TPKEY(C) 必须相同 | `semantic_rule` | explicit | config | object | OBJ-L2TPN4KEY / OBJ-L2TPKEY | N4 接口 L2TP 加密：UDG SET L2TPN4KEY 与 UNC SET L2TPKEY 的 KEY 值必须相同，否则 N4 隧道加密协商失败 | 加密协商失败导致 L2TP 隧道无法建立 | critical | EV-FK-21, EV-FK-14 |
| `CR-APN-04` | POOLTYPE 取值跨产品差异 | `semantic_rule` | explicit | restriction | parameter | ADD POOL.POOLTYPE / ADD ADDRPOOL.POOLTYPE | UDG POOLTYPE=LOCAL（本地池，用户面分配）/EXTERNAL（外部池）；UNC POOLTYPE 仅 UDM（静态签约用）；跨产品同名参数取值集不同 | POOLTYPE 误用导致地址分配逻辑错误 | warning | EV-FK-06, EV-FK-12 |
| `CR-APN-05` | V6PREFIXLENGTH<64 切换 PD 模式 | `parameter_dependency` | explicit | config | parameter | ADD SECTION.V6PREFIXLENGTH | V6PREFIXLENGTH=64 为普通 IPv6 单栈地址分配；V6PREFIXLENGTH<64 切换为 IPv6 Prefix Delegation 模式（GWFD-020406）；前缀长度 64 是 PD 分水岭 | PD 模式误判导致前缀代理失败 | critical | EV-FK-30, EV-FK-26 |
| `CR-APN-06` | VPNINSTAF AFTYPE=ipv6uni IPv6 必需 | `precondition_rule` | explicit | config | parameter | ADD VPNINSTAF.AFTYPE | IPv4 地址分配仅需 IPv4 VPN（无 VPNINSTAF 或 AFTYPE=ipv4uni）；IPv6/双栈必须额外 ADD VPNINSTAF AFTYPE=ipv6uni 激活 IPv6 地址族 | IPv6 地址族未激活导致 IPv6 地址无法分配 | critical | EV-FK-28, EV-FK-26, EV-FK-30 |
| `CR-APN-07` | APN VPN 与地址池 VPN 必须一致 | `semantic_rule` | explicit | config | relation | OBJ-APN-U ↔ OBJ-POOL-U | ADD APN 的 VPNINSTANCE 必须与 ADD POOL 的 VPNINSTANCE 一致；双栈场景 APN 的 HASVPN/HASVPNIPV6 双绑定对应双 VPN 实例 | VPN 不一致导致地址分配后路由不通 | critical | EV-FK-06 |
| `CR-APN-08` | UPFRDSSVR 必须先于 UPFRDSCLIENTIP | `precondition_rule` | explicit | config | command | CMD-UNC-050 / CMD-UNC-051 | 二次鉴权强顺序：ADD UPFRDSSVR（DN-AAA 服务器）必须先于 ADD UPFRDSCLIENTIP；CLIENTIP 执行后 SMF 立即触发建链，若服务器未就绪则建链失败 | Radius 建链失败 | critical | EV-FK-27 |
| `CR-APN-09` | NETWORKINSTVPNMAP 必须先于 UPFRDSSVR/CLIENTIP | `precondition_rule` | explicit | config | command | CMD-UNC-052 | UPF 侧 VPN 配置必须先于 UPF Radius 服务器/客户端 IP，否则 Radius 报文无法路由 | Radius 报文路由失败 | critical | EV-FK-27 |
| `CR-APN-10` | IPSec IKE DH 组不能为 None | `runtime_check_rule` | explicit | restriction | parameter | ADD IKEPROPOSAL.DHGROUP / ADD IKEPEER | IPSec IKE 提议的 DHGROUP 不能为 None；否则 IKE 协商无法完成密钥交换 | IKE 协商失败导致 IPSec 隧道无法建立 | critical | EV-FK-30 |
| `CR-APN-11` | IPSec ACL 仅支持源/目的 IP | `parameter_mutex` | explicit | restriction | parameter | ADD ACLRULEADV4IPSEC | IPSec ACL 规则仅支持源/目的 IP，不支持端口；NAT 穿越仅 ESP 隧道模式；默认 IKEv2（IKEv1 需 MOD IKEPEER VERSION1=FALSE 关闭） | 规则不匹配导致保护数据流识别失败 | warning | EV-FK-30 |
| `CR-APN-12` | GRE 源地址不能与 IPSec 源地址相同 | `parameter_mutex` | explicit | restriction | object | OBJ-GRETUNNEL ↔ OBJ-IPSECINTFCFGIPSEC | GRE 隧道源地址不能与 IPSec 隧道源地址相同（FR-GRE-IPSEC-SRC-EXCL）；GRE over IPSec 场景需先建 GRE 再叠加 IPSec | 源地址冲突导致隧道建链失败 | critical | EV-FK-29, EV-FK-30 |
| `CR-APN-13` | L2TP 与地址自动检测/基于位置互斥 | `parameter_mutex` | explicit | restriction | object | OBJ-APNL2TPATTR ↔ OBJ-CONFLICTIP | L2TP VPN（GWFD-020412）与用户面地址自动检测（GWFD-010108）不可同时应用；与基于位置地址分配（GWFD-020421）互斥（地址分配主体不同：LNS 远程 vs 位置本地池） | 互斥特性同时启用导致地址分配逻辑冲突 | warning | EV-FK-21, EV-FK-19, EV-FK-18 |
| `CR-APN-14` | L2TP 本地配置与 AAA 下发互斥 | `parameter_mutex` | explicit | restriction | object | OBJ-L2TPGROUP ↔ OBJ-L2TPRDSCLIENT | L2TP 本地配置方式（ADD L2TPGROUP+L2TPCLIENTIP）与 AAA 下发方式（ADD L2TPRDSCLIENT）互斥；不支持 PPP 用户/DHCP 延迟分配/IPv6 PD/NAT | 两种方式同时配置导致 L2TP 行为不确定 | warning | EV-FK-21 |
| `CR-APN-15` | APNACTNUM 并发限制触发拒绝 | `runtime_check_rule` | explicit | ops | parameter | ADD APNACTNUM.PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM | 单 APN 并发超过 PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM 阈值时，触发 PDNCONNREJCAUSE 拒绝；防止单 APN 资源耗尽 | 并发超限导致用户被拒（业务影响） | info | EV-FK-03 |
| `CR-APN-16` | STATICADDRPARA 与 SMF 主锚点 UPF 冲突时 SMF 优先 | `semantic_rule` | explicit | config | relation | OBJ-STATICADDRPARA ↔ OBJ-PNFPROFILE | 静态 IP 段绑定 UPF（SET STATICADDRPARA）与 SMF 主锚点 UPF 选择冲突时，SMF 选择优先（FR-SMF主锚点优先） | 静态绑定被忽略（行为符合预期，需文档化） | info | EV-FK-12, EV-FK-34 |
| `CR-APN-17` | APNALIAS 转换后 APN 必须已 ADD APN | `precondition_rule` | explicit | config | command | CMD-UNC-058 | GGSN/PGW-C/SMF 侧 ADD APNALIAS 的 CONVERTAPN 必须在 ADD APN 中已存在；5G 先按切片 SST+SD 查，未中再按 ALL_USER | 转换后 APN 不存在导致会话建立失败 | critical | EV-FK-05 |
| `CR-APN-18` | MPLS VPN 命令为推导（文档缺口） | `syntax_rule` | implicit | restriction | command | CMD-UDG-062 / CMD-UDG-063 / CMD-UDG-064 | GWFD-020411 共 9 篇文档无 MML 脚本，VPNINSTANCE/BGPVPNV4ROUTETARGET/BGPVPNV4PEER 基于 MPLS L3VPN 标准实践推导，需命令字典补全 | 推导命令参数待验证 | info | EV-FK-32（推导） |

---

## 5. MMLCommand 关键参数集（核心命令）

> **Schema 参考**：§11.4 CommandParameter。`required_mode` 取值 `required / optional / conditional_required`（Schema §11.4 必备字段）。本节 9 个核心命令的参数表已补齐 `required_mode` 列。

### 5.1 ADD POOL（UDG 地址池核心命令）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| POOLNAME | string | — | `required` | 地址池名 |
| POOLTYPE | enum | LOCAL / EXTERNAL | `required` | ★CR-APN-01/04：UDG 用 LOCAL（本地池）；EXTERNAL 为外部池 |
| IPVERSION | enum | IPV4 / IPV6 | `required` | 地址版本 |
| HASVPN | enum | ENABLE / DISABLE | `optional` | 是否绑定 VPN |
| VPNINSTANCE | string | — | `conditional_required` | 引用 VPNINST（CR-APN-07：与 APN VPN 一致；HASVPN=ENABLE 时必填） |
| REDUNDFUNC | enum | — | `conditional_required` | 冗余功能标识（静态路由冗余场景，与 REDUNDUSER 双使能；仅静态冗余特性启用时必填） |

### 5.2 ADD ADDRPOOL（UNC 地址池核心命令，★与 ADD POOL 分离）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| ADDRPOOLNAME | string | — | `required` | UNC 地址池名（★命名前缀 ADDR，与 UDG POOL 分离） |
| POOLTYPE | enum | UDM | `required` | ★CR-APN-04：UNC 仅 UDM（静态签约用），无 LOCAL |
| IPVERSION | enum | IPV4 / IPV6 | `required` | 地址版本 |

### 5.3 SET APNADDRESSATTR（APN 地址分配属性，U+C 共用命令名）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| APN | string | — | `required` | APN/DNN 名 |
| SUPPORTIPV4 | enum | ENABLE / DISABLE | `required` | 支持 IPv4 |
| SUPPORTIPV6 | enum | ENABLE / DISABLE | `required` | 支持 IPv6（双栈 ENABLE+ENABLE） |
| IGNOREV4 | enum | ENABLE / DISABLE | `optional` | 忽略 IPv4（IPv6 单栈场景） |
| V6POOLID | int | — | `conditional_required` | IPv6 池 ID（PD 场景 V6PREFIXLENGTH<64 时必填） |
| HOSTROUTEIP | string | — | `optional` | 主机路由 IP |

### 5.4 SET APNL2TPATTR（UDG L2TP U 面核心，★10+ 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| APN | string | — | `required` | APN 名 |
| L2TPSWITCH | enum | ENABLE / DISABLE | `required` | L2TP 开关 |
| SUPPORTIPV6 | enum | ENABLE / DISABLE | `optional` | 支持 IPv6 |
| ... | ... | ... | ... | ★CR-APN-02：共 10+ 参数（与 UNC APNL2TPCTRL 仅 2 参数不对称） |

### 5.5 SET APNL2TPCTRL（UNC L2TP C 面决策，★仅 2 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| APN | string | — | `required` | APN 名 |
| L2TPSWITCH | enum | ENABLE / DISABLE | `required` | ★CR-APN-02：仅 2 参数（与 UDG APNL2TPATTR 10+ 参数不对称） |

### 5.6 SET APNAUTHATTR（Radius 鉴权接入核心，ACCESSMODE 4 取值）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| APN | string | — | `required` | APN 名 |
| ACCESSMODE | enum | TRANS_NON_AUTH / TRANS_AUTH / NON_TRANS / LOC_AUTH | `required` | ★透明不鉴权/透明鉴权/非透明接入/本地鉴权；仅 TRANS_AUTH/NON_TRANS 强依赖 Radius 功能 |
| COMMONUSERNAME | string | — | `conditional_required` | 公共用户名（TRANS_AUTH 用；ACCESSMODE=TRANS_AUTH 时必填） |
| COMMONUSERPASS | string | — | `conditional_required` | 公共密码（TRANS_AUTH 用；ACCESSMODE=TRANS_AUTH 时必填） |

### 5.7 ADD IPSECPOLICY（IPSec 安全策略聚合命令）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| POLICYNAME | string | — | `required` | 策略名 |
| SEQ | int | — | `required` | 策略序号 |
| MODE | enum | ISAKMP | `required` | 模式（ISAKMP 表示经 IKE 协商） |
| ACLGROUPNAME | string | — | `conditional_required` | 引用 ACLGROUPIPSEC（CR-APN-11：仅源/目的 IP；ISAKMP 模式下必填以定义保护数据流） |

### 5.8 ADD GRETUNNEL（GRE 隧道核心命令）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| TNLNAME | string | — | `required` | 隧道名 |
| TNLTYPE | enum | gre | `required` | 隧道类型 |
| SRCTYPE | enum | if_name / ... | `required` | 源类型（推荐 LoopBack 接口） |
| SRCIFNAME | string | — | `conditional_required` | 源接口名（LoopBack1；SRCTYPE=if_name 时必填） |
| DSTIPADDR | string | — | `required` | 目的 IP（CR-APN-12：不能与 IPSec 源地址相同） |

### 5.9 ADD APNACTNUM（单 APN 并发限制核心命令）

| 参数 | 类型 | 取值范围 | `required_mode` | 说明 |
|------|------|---------|-----------------|------|
| APN | string | — | `required` | APN 名 |
| PDNNUM | int | — | `optional` | PDN 并发数阈值 |
| IPV4ADDRNUM | int | — | `optional` | IPv4 地址数阈值 |
| IPV6ADDRNUM | int | — | `optional` | IPv6 地址数阈值 |
| PDNCONNREJCAUSE | int | — | `conditional_required` | 超限拒绝原因值（CR-APN-15；配置了任一并发阈值后必填以定义拒绝行为） |

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

> **Schema 参考**：§11.7 `MMLCommand operates_on ConfigObject`。仅列核心命令，全量见各小节。

### 6.1 UDG 侧地址分配（16条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UDG-001) | LICENSESWITCH | License 开关 |
| ADD APN (CMD-UDG-009) | APN | APN/DNN 实例（跨域共用挂载点） |
| SET APNADDRESSATTR (CMD-UDG-013) | APNADDRESSATTR | APN 地址分配属性 |
| ADD POOL (CMD-UDG-014) | POOL | ★UDG 地址池（POOLTYPE=LOCAL） |
| ADD SECTION (CMD-UDG-015) | SECTION | 地址段 |
| ADD POOLGROUP (CMD-UDG-016) | POOLGROUP | 地址池组 |
| ADD POOLBINDGROUP (CMD-UDG-017) | POOLBINDGROUP | 地址池绑定（UDG 命名 GROUP） |
| ADD POOLGRPMAP (CMD-UDG-018) | POOLGRPMAP | 池组映射 |
| SET IPALLOCRULE (CMD-UDG-019) | IPALLOCRULE | 全局三级地址分配规则 |
| SET APNIPALLOCRULE (CMD-UDG-020) | APNIPALLOCRULE | APN 级地址分配规则 |
| ADD CPNODEID (CMD-UDG-021) | CPNODEID | SMF 的 NodeID |
| SET IPALLOCBYSMFGLBSW (CMD-UDG-022) | IPALLOCBYSMFGLBSW | 基于 SMF 分配全局开关 |
| ADD LACGROUP (CMD-UDG-025) | LACGROUP | LAC 位置区组 |
| SET IPALLOCBYLOCGLBSW (CMD-UDG-029) | IPALLOCBYLOCGLBSW | 基于位置分配全局开关 |
| ADD ADRLOCWHITELST (CMD-UDG-030) | ADRLOCWHITELST | 位置区白名单 |
| ADD CONFLICTIP (CMD-UDG-024) | CONFLICTIP | 冲突地址标识 |

### 6.2 UDG 侧 VPN/接口/路由（10条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD VPNINST (CMD-UDG-003) | VPNINST | VPN 实例 |
| ADD L3VPNINST (CMD-UDG-004) | L3VPNINST | L3VPN 实例 |
| ADD VPNINSTAF (CMD-UDG-005) | VPNINSTAF | VPN 地址族（IPv6 需 AFTYPE=ipv6uni） |
| ADD INTERFACE (CMD-UDG-006) | INTERFACE | 物理/逻辑接口 |
| ADD IPBINDVPN (CMD-UDG-007) | IPBINDVPN | 接口绑定 VPN |
| ADD LOGICINF (CMD-UDG-008) | LOGICINF | Giif 逻辑接口 |
| ADD IFIPV4ADDRESS (CMD-UDG-040) | IFIPV4ADDRESS | 接口 IPv4 地址 |
| ADD SRROUTE (CMD-UDG-043) | SRROUTE | 静态路由 |
| ADD OSPF (CMD-UDG-032) | OSPF | IPv4 OSPF 进程 |
| ADD OSPFIMPORTROUTE (CMD-UDG-035) | OSPFIMPORTROUTE | 引入 WLR 路由 |

### 6.3 UDG 侧隧道（17条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD GRETUNNEL (CMD-UDG-044) | GRETUNNEL | GRE 隧道 |
| ADD ACLGROUPIPSEC (CMD-UDG-047) | ACLGROUPIPSEC | IPSec ACL 组 |
| ADD ACLRULEADV4IPSEC (CMD-UDG-048) | ACLRULEADV4IPSEC | IPSec ACL 规则 |
| ADD IPSECPROPOSALIPSEC (CMD-UDG-049) | IPSECPROPOSALIPSEC | IPSec 安全提议 |
| ADD IKEPROPOSAL (CMD-UDG-050) | IKEPROPOSAL | IKE 提议 |
| ADD IKEPEER (CMD-UDG-051) | IKEPEER | IKE 对等体 |
| ADD IPSECPOLICY (CMD-UDG-052) | IPSECPOLICY | IPSec 安全策略 |
| ADD IPSECINTFCFGIPSEC (CMD-UDG-055) | IPSECINTFCFGIPSEC | 应用策略到 Tunnel |
| ADD VPNINSTANCE (CMD-UDG-062) | VPNINSTANCE | ★推导：MPLS VPN 实例 |
| ADD BGPVPNV4PEER (CMD-UDG-064) | BGPVPNV4PEER | ★推导：MP-BGP 对等体 |
| SET APNL2TPATTR (CMD-UDG-065) | APNL2TPATTR | ★UDG L2TP APN 属性（10+ 参数） |
| ADD L2TPGROUP (CMD-UDG-067) | L2TPGROUP | L2TP 组（本地配置方式） |
| ADD L2TPRDSCLIENT (CMD-UDG-070) | L2TPRDSCLIENT | L2TP Radius LNS（AAA 下发方式） |
| SET L2TPN4KEY (CMD-UDG-074) | L2TPN4KEY | U 侧 N4 加密密钥 |
| ADD REDUNDRDTIP (CMD-UDG-075) | REDUNDRDTIP | 虚拟 IP（静态冗余） |
| SET REDUNDUSER (CMD-UDG-076) | REDUNDUSER | 全局冗余开关 |
| SET APNQOSATTR (CMD-UDG-080) | APNQOSATTR | 接入控制 U 面 QoS 属性 |

### 6.4 UNC 侧地址分配（12条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD ADDRPOOL (CMD-UNC-002) | ADDRPOOL | ★UNC 地址池（POOLTYPE=UDM） |
| ADD ADDRPOOLGRP (CMD-UNC-005) | ADDRPOOLGRP | UNC 地址池组 |
| ADD POOLBINDGRP (CMD-UNC-007) | POOLBINDGRP | UNC 地址池绑定（命名 GRP） |
| ADD POOLBINDAPN (CMD-UNC-008) | POOLBINDAPN | UNC APN 绑定地址池 |
| ADD POOLGRPMAP (CMD-UNC-009) | POOLGRPMAP | UNC 池组映射 |
| ADD UPNODE (CMD-UNC-010) | UPNODE | UPF 节点（共用对象） |
| ADD PNFPROFILE (CMD-UNC-011) | PNFPROFILE | UPF NF 实例属性 |
| ADD UPFBINDGRP (CMD-UNC-012) | UPFBINDGRP | UPF 绑定组 |
| SET STATICADDRPARA (CMD-UNC-013) | STATICADDRPARA | 静态 IP 段绑定 UPF |
| SET APNADDRESSATTR (CMD-UNC-014) | APNADDRESSATTR | UNC APN 地址属性 |
| SET IPALLOCBYLOCGLBSW (CMD-UNC-017) | IPALLOCBYLOCGLBSW | UNC 基于位置开关 |
| ADD BLACKLIST (CMD-UNC-018) | BLACKLIST | 静态地址黑名单 |

### 6.5 UNC 侧 UPF 选择（12条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD PNFDNN (CMD-UNC-019) | PNFDNN | UPF 支持的 DNN |
| ADD PNFNS (CMD-UNC-020) | PNFNS | UPF 支持的切片（4G PNFNSINDEX=0） |
| ADD PNFDNAI (CMD-UNC-021) | PNFDNAI | UPF 支持的 DNAI |
| ADD PNFUPFINFO (CMD-UNC-022) | PNFUPFINFO | UPF 信息（EPS 互通） |
| ADD UPAREA (CMD-UNC-023) | UPAREA | UPF 位置区绑定 |
| ADD PNFTAI (CMD-UNC-024) | PNFTAI | UPF TAI 范围 |
| ADD UPBINDS11 (CMD-UNC-025) | UPBINDS11 | SGW-U S11 绑定 |
| ADD UPBINDGNGP (CMD-UNC-026) | UPBINDGNGP | Gn/Gp 绑定 |
| SET UPSELECTPRI (CMD-UNC-027) | UPSELECTPRI | UPF 选择策略次序 |
| SET UPSELECTFLAG (CMD-UNC-028) | UPSELECTFLAG | UPF 选择开关 |
| SET APNUPSELPLY (CMD-UNC-029) | APNUPSELPLY | APN 级 UPF 选择策略 |
| SET UPLOADBALANCE (CMD-UNC-030) | UPLOADBALANCE | UPF 负载均衡 |

### 6.6 UNC 侧鉴权/Radius/二次鉴权（18条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD GBAUTHCIPH (CMD-UNC-031) | GBAUTHCIPH | 2G AKA 鉴权 |
| ADD IUAUTHCIPH (CMD-UNC-032) | IUAUTHCIPH | 3G AKA 鉴权 |
| ADD S1USRSECPARA (CMD-UNC-033) | S1USRSECPARA | 4G AKA 鉴权 |
| ADD NGUSRSECPARA (CMD-UNC-034) | NGUSRSECPARA | 5G AKA 鉴权 |
| SET APNAUTHATTR (CMD-UNC-037) | APNAUTHATTR | APN 鉴权属性（ACCESSMODE 4 取值） |
| ADD RDSSVRGRP (CMD-UNC-039) | RDSSVRGRP | ★Radius 服务器组（三件套共享） |
| ADD RDSSVR (CMD-UNC-040) | RDSSVR | Radius 服务器 |
| ADD APNRDSSVRGRP (CMD-UNC-041) | APNRDSSVRGRP | APN↔Radius 服务器组绑定 |
| ADD APNRDSCLIENTIP (CMD-UNC-042) | APNRDSCLIENTIP | APN Radius Client IP |
| SET FHBYPASS (CMD-UNC-046) | FHBYPASS | 故障一键放通 |
| ADD UPLIST4RDS (CMD-UNC-047) | UPLIST4RDS | PGW-U/UPF List |
| ADD CPGTPUADDR (CMD-UNC-048) | CPGTPUADDR | GTP-U 地址 |
| ADD RDSUPFCTRL (CMD-UNC-049) | RDSUPFCTRL | Radius UPF 控制 |
| ADD UPFRDSSVR (CMD-UNC-050) | UPFRDSSVR | ★UPF Radius 服务器（必须先于 CLIENTIP） |
| ADD UPFRDSCLIENTIP (CMD-UNC-051) | UPFRDSCLIENTIP | ★UPF Radius 客户端 IP（必须最后） |
| ADD NETWORKINSTVPNMAP (CMD-UNC-052) | NETWORKINSTVPNMAP | UPF VPN 配置（必须前置） |

### 6.7 UNC 侧接入控制/别名/会话/DNS（17条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD GBARD (CMD-UNC-053) | GBARD | 2G 接入限制 |
| ADD IUARD (CMD-UNC-054) | IUARD | 3G 接入限制 |
| ADD S1ARD (CMD-UNC-055) | S1ARD | 4G 接入限制 |
| ADD NGMMSUBDATA (CMD-UNC-056) | NGMMSUBDATA | 5GC 移动性限制 |
| ADD APNALIAS (CMD-UNC-058) | APNALIAS | 别名 APN→真实 APN |
| ADD ALIASAPN (CMD-UNC-060) | ALIASAPN | 协商 APN→别名 APN |
| SET APNL2TPCTRL (CMD-UNC-064) | APNL2TPCTRL | ★UNC L2TP 控制（仅 2 参数） |
| SET L2TPKEY (CMD-UNC-066) | L2TPKEY | C 侧 N4 加密密钥 |
| ADD PDPAPN (CMD-UNC-068) | PDPAPN | 2/3G PDP APN |
| ADD APNACTNUM (CMD-UNC-070) | APNACTNUM | 单 APN 并发限制 |
| ADD SMSUBDATA (CMD-UNC-074) | SMSUBDATA | SM 子表数据 |
| ADD AREADNS (CMD-UNC-081) | AREADNS | 位置区域 DNS 定制 |
| ADD DHCPSERVER (CMD-UNC-078) | DHCPSERVER | DHCP 服务器 |
| SET REDUNDUSER (CMD-UNC-084) | REDUNDUSER | UNC 静态冗余开关（U+C 共用） |
| ADD VPNINST (CMD-UNC-085) | VPNINST | UNC VPN 实例 |
| ADD LOGICINF (CMD-UNC-086) | LOGICINF | UNC Gi 逻辑接口 |
| SET SDBTMR (CMD-UNC-072) | SDBTMR | 签约数据库定时器 |

---

## 7. ★CommandRule governs MMLCommand 边表（§11.6 反向）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand / CommandParameter / ConfigObject`（反向：规则治理命令，非命令 has_rule）。

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-APN-01 | CMD-UDG-014 (ADD POOL) + CMD-UNC-002 (ADD ADDRPOOL) | 前缀不对称，POOL vs ADDRPOOL 分离建模 |
| CR-APN-02 | CMD-UDG-065 (SET APNL2TPATTR) + CMD-UNC-064 (SET APNL2TPCTRL) | U 10+ 参数 vs C 2 参数不对称 |
| CR-APN-03 | CMD-UDG-074 (SET L2TPN4KEY) + CMD-UNC-066 (SET L2TPKEY) | U+C 密钥必须相同 |
| CR-APN-04 | CMD-UDG-014.POOLTYPE + CMD-UNC-002.POOLTYPE | POOLTYPE 跨产品取值差异（LOCAL vs UDM） |
| CR-APN-05 | CMD-UDG-015.V6PREFIXLENGTH (ADD SECTION) | <64 切换 PD 模式 |
| CR-APN-06 | CMD-UDG-005.AFTYPE (ADD VPNINSTAF) | IPv6 需 AFTYPE=ipv6uni |
| CR-APN-07 | OBJ-APN-U ↔ OBJ-POOL-U 关系 | VPN 必须一致 |
| CR-APN-08 | CMD-UNC-050 (UPFRDSSVR) precedes CMD-UNC-051 (UPFRDSCLIENTIP) | 强顺序：服务器先于客户端 |
| CR-APN-09 | CMD-UNC-052 (NETWORKINSTVPNMAP) precedes CMD-UNC-050/051 | VPN 配置必须前置 |
| CR-APN-10 | CMD-UDG-050.DHGROUP (IKEPROPOSAL) + CMD-UDG-051 (IKEPEER) | DH 组不能 None |
| CR-APN-11 | CMD-UDG-048 (ACLRULEADV4IPSEC) | ACL 仅源/目的 IP |
| CR-APN-12 | OBJ-GRETUNNEL ↔ OBJ-IPSECINTFCFGIPSEC | GRE 源地址 ≠ IPSec 源地址 |
| CR-APN-13 | OBJ-APNL2TPATTR ↔ GWFD-010108/020421 | L2TP 与地址自动检测/基于位置互斥 |
| CR-APN-14 | OBJ-L2TPGROUP ↔ OBJ-L2TPRDSCLIENT | 本地配置 vs AAA 下发互斥 |
| CR-APN-15 | CMD-UNC-070 (ADD APNACTNUM) 阈值参数 | 并发超限触发拒绝 |
| CR-APN-16 | OBJ-STATICADDRPARA ↔ OBJ-PNFPROFILE | SMF 主锚点优先 |
| CR-APN-17 | CMD-UNC-058 (ADD APNALIAS).CONVERTAPN | 转换后 APN 必须已存在 |
| CR-APN-18 | CMD-UDG-062/063/064 (MPLS 推导命令) | 文档缺口，推导待验证 |

---

## 8. 与带宽控制/计费场景命令图谱的差异

| 维度 | 计费场景 | 带宽控制场景 | APN 业务域（本文件） |
|------|---------|------------|---------------------|
| MMLCommand 数量 | 87（UDG 41 + UNC 46） | 55（UDG 30 + UNC 25） | **142**（UDG 63 + UNC 79） |
| ConfigObject 数量 | 55 | 29 | **~65** |
| CommandRule 数量 | 14 | 5 | **18** |
| 独有命令族 | URR 三件套、在线计费 DIAMCONNGRP/DCCTEMPLATE、融合计费 18 步链、CG 接口 | BWM 三级体系（BWMSERVICE/CONTROLLER/USERGROUP/RULE）、Shaping、智能 Shaping、FUP(URR 复用)、ADC | **地址池体系（POOL/ADDRPOOL U+C 分离）+ 4 隧道（GRE/IPSec/MPLS/L2TP U+C 不对称）+ Radius 三件套 + UPF 选择 11 件套 + AKA 4 代 + ARD 3 代 + 别名 APN 双视角 + DHCP + 地址自动检测运维** |
| 共享命令 | SET LICENSESWITCH、ADD RULE、ADD USERPROFILE 等 PCC 规则体系 | 同左 + URR/URRGROUP 共享 | SET LICENSESWITCH、ADD APN（跨域共用挂载点）、SET APNADDRESSATTR（U+C 共用命令名）、SET REDUNDUSER（U+C 共用对象）、ADD SECTION（U+C 同命令） |
| POLICYTYPE 枚举差异 | CHARGING（独有） | BWM（独有）、PCC/QOS/ADC | APN 域无 POLICYTYPE 概念（ADD RULE/USERPROFILE 不在本域核心命令） |
| 核心不对称 | — | — | ★POOL(UDG) vs ADDRPOOL(UNC)、APNL2TPATTR(U,10+) vs APNL2TPCTRL(C,2)、L2TPN4KEY(U) vs L2TPKEY(C) |
| 文档缺口 | — | — | ★MPLS VPN 9 篇无 MML 脚本（CMD-UDG-062/063/064 推导） |

---

## 9. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| MMLCommand | **142** | CMD-UDG-001~088（含运维+REFRESHSRV）+ CMD-UNC-001~087（U+C 复用 ADD APN 不独立编号；含 REFRESHSRV） |
| ConfigObject | **~65**（去重） | OBJ-POOL-U ~ OBJ-REDUNDUSER（含 ★推导 3 个 MPLS） |
| CommandRule | **18** | CR-APN-01 ~ CR-APN-18 |
| ConfigObject contains/refers_to/depends_on/conflicts_with/activates/composed_by 边 | **55** | contains 22 + refers_to 16 + depends_on 9 + conflicts_with 3 + activates 4 + composed_by 1 |
| operates_on 边 | **102** | UDG 侧 43 + UNC 侧 59（REFRESHSRV 动作命令无 ConfigObject） |
| ★CommandRule governs 边 | **18** | CR-APN-01 ~ CR-APN-18 各治理若干命令/参数/对象 |
| **命令层对象总计** | **~282** | — |

---

> 本文件为 APN 业务域三层图谱第 4 层。第 5 层跨层映射、第 6 层证据索引见同目录其他文件。
> **★Stage 5 审查重点**：①CommandRule governs 方向（反向）；②POOL vs ADDRPOOL 分离建模；③APNL2TPATTR vs APNL2TPCTRL 分离；④ConfigObject 关系作为边（非节点）；⑤MPLS 命令推导标注；⑥source_evidence_ids 指向 EV-FK-xx。
