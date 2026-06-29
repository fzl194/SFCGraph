# APN 业务域命令图谱 · 簇E：IPFD-015004 IPSec功能（UDG）

> **文件定位**：`three-layer-graph/draft/04-cluster-E-IPSec-015004.md`
> **特性范围**：仅 IPFD-015004 IPSec功能（UDG 侧），**13 个激活子场景不合并**（8 普通场景 + 5 国密 IKEv1 场景；其中 GRE/多Sequence/指定本端接口 3 场景在普通与国密下各有一份，命令族复用但算法/认证参数不同）
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **结构对齐**：严格 follow `04-cluster-B-GWFD-010105.md`（表格列、CMD-UDG-015004-xx 编号、9 节组织、§5 参数表、§6 operates_on 边）
> **数据来源**：1 篇特性概述 + 6 篇实现原理 + 2 篇调测/术语 + **13 篇激活文档**（8 普通 + 5 国密）+ **22 篇 MML 命令手册原文**（路径见 §抽取核对清单）
> **铁律**：命令/参数 100% 来自原始产品文档原文，零编造。手册未定位的命令标注「⚠️手册未定位」。

---

## 0. 命令清单总览（IPFD-015004 用到的全部命令）

### 0.1 按命令类型分布

| 类型 | 命令数 | 命令清单 |
|------|-------|---------|
| IPSec 核心配置类（IPsec微服务侧） | 10 | ADD ACLGROUPIPSEC、ADD ACLRULEADV4IPSEC、ADD ACLGROUP6IPSEC、ADD ACLRULEADV6IPSEC、ADD IPSECPROPOSALIPSEC、ADD IKEPROPOSAL、ADD IKEPEER、ADD IKEPEER6、ADD IPSECPOLICY、ADD IPSECPOLICY6、ADD PROPATTACHIPSECPROPOSAL、ADD ATTACHIKEPEER、ADD IPSECINTFCFGIPSEC、SET IKEGLOBALCONFIG |
| IPSec 模板/策略模板类 | 1 | ADD IPSECPOLICYTM（策略模板模式 TEMPLATEMODE=PolicyTemplate 时引用） |
| 国密独有命令族 | 4 | SET FWSOFTPARA（国密开关 DWORD 1401）、ADD CERTSCENE（证书场景）、SET PKICRLCHECK（CRL检查）、DSP PKICERTLIST（查询证书，本期略参数） |
| GRE over IPsec 独有 | 1 | ADD GRETUNNEL（GRE隧道，承载组播/广播业务） |
| IPsec微服务双配命令族（与VNRS侧对称，参数简化） | 6 | ADD L3VPNINSTIPSEC、ADD VPNINSTAFIPSEC、ADD INTERFACEIPSEC、ADD IPBINDVPNIPSEC、ADD IFIPV4ADDRESSIPSEC、（IPv6场景）ADD IFIPV6ADDRESSIPSEC |
| VNRS侧前置依赖（非本特性核心，但在激活脚本中出现） | 8 | ADD L3VPNINST、ADD VPNINSTAF、ADD IPBINDVPN、ADD IFIPV4ADDRESS、ADD INTERFACE、ADD IPSECINTFCFG（VNRS侧，仅2参数）、ADD SRROUTE、ADD GRETUNNEL（GRE场景） |
| 查询/调测类（本期略，不抽参数） | 12+ | DSP IKESA、DSP IKEIPSECSA、LST IKEPEER/IKEPROPOSAL/IPSECPOLICY/IPSECPROPOSALIPSEC/PROPATTACHIPSECPROPOSAL/IPSECINTFCFGIPSEC/IFIPV4ADDRESSIPSEC、DSP IPSECPATHMTU、RTR IKESA、RST IPSECPATHMTU |

> **★核心说明**：IPSec 特性的本质是**双微服务双配**——VNRS微服务（负责引流与外部网络通信）+ IPsec微服务（负责 IKE 协商与加解密）。激活脚本中几乎所有配置都需要在两个微服务各执行一次（VPN实例、隧道接口、接口IP、隧道类型）。本文件聚焦**IPsec微服务侧的核心命令族**（§1-§7），VNRS侧命令仅在 §6.2 前置依赖中标注引用关系。

### 0.2 ConfigObject 分布（本特性涉及）

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| ACL数据流定义 | 4 | ACLGROUPIPSEC、ACLRULEADV4IPSEC、ACLGROUP6IPSEC、ACLRULEADV6IPSEC |
| IPSec安全提议 | 1 | IPSECPROPOSALIPSEC |
| IKE安全提议 | 1 | IKEPROPOSAL |
| IKE对等体 | 2 | IKEPEER、IKEPEER6 |
| IPSec安全策略 | 3 | IPSECPOLICY、IPSECPOLICY6、IPSECPOLICYTM（模板） |
| 策略绑定关系 | 2 | PROPATTACHIPSECPROPOSAL（策略↔提议）、ATTACHIKEPEER（策略↔对等体） |
| 隧道接口应用 | 1 | IPSECINTFCFGIPSEC（含 POLICYNAME + SRCIFNAME 借用接口） |
| IKE全局配置 | 1 | IKEGLOBALCONFIG（DPD/NAT保活/抗重放等全局参数） |
| 国密证书管理 | 3 | CERTSCENE、FWSOFTPARA（国密开关）、PKICRLCHECK |
| GRE隧道（GRE场景独有） | 1 | GRETUNNEL |
| 前置依赖（引用，非本特性拥有） | 5 | L3VPNINST/L3VPNINSTIPSEC、VPNINSTAF/VPNINSTAFIPSEC、INTERFACE/INTERFACEIPSEC、IPBINDVPN/IPBINDVPNIPSEC、IFIPV4ADDRESS/IFIPV4ADDRESSIPSEC |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1 所有 MMLCommand。
> **声明**：本文件 §1 所有 MMLCommand 的 `status` 字段值均为 `active`（Schema §11.3 MMLCommand.status 必备）。IPFD-015004 所有正式命令均处于启用状态。
> **依据**：所有命令均在产品文档正式登记，无 `deprecated` 或 `planned` 状态。

---

## 1. MMLCommand 实例化（IPFD-015004，22 个核心命令 + 2 个未定位）

### 1.1 ACL 数据流定义（UDG，4个：IPv4×2 + IPv6×2）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-01` | `ADD ACLGROUPIPSEC` | ADD | ACLGROUPIPSEC | IPv4 ACL规则组（★ACLNAME 可为编号3000~3999或名称；★激活文档强约束：ACL 只支持源IP和目的IP配置，端口配置不生效） | ACLNAME, ACLSTEP, ACLTYPE(Basic/Advance), ACLMATCHORDER(Config/Auto), ACLDESCRIPTION | EV-IPSEC-01 |
| `CMD-UDG-015004-02` | `ADD ACLRULEADV4IPSEC` | ADD | ACLRULEADV4IPSEC | IPv4 高级ACL规则（★25参数；ACLSRCWILD/ACLDESTWILD 为反掩码，0=精确匹配；ACLPROTOCOL 0=IP/1=ICMP/6=TCP/17=UDP/89=OSPF） | ACLNAME, ACLRULENAME, ACLRULEID, ACLACTION(Permit/Deny), ACLFRAGTYPE, ACLSOURCEIP, ACLSRCWILD, VRFNAME, ACLPROTOCOL, ACLDESTIP, ACLDESTWILD, ACLSRCPORTOP/BEGIN/END, ACLDESTPORTOP/BEGIN/END, ACLPRECEDENCE, ACLTOS, ACLDSCP, ACLICMPNAME/TYPE/PCODE, ACLSYNFLAG, ACLRULEDESCRIPTION | EV-IPSEC-01 |
| `CMD-UDG-015004-03` | `ADD ACLGROUP6IPSEC` | ADD | ACLGROUP6IPSEC | IPv6 ACL规则组（参数同 ACLGROUPIPSEC，独立命令） | ACLNAME, ACLSTEP, ACLTYPE, ACLMATCHORDER, ACLDESCRIPTION | EV-IPSEC-02 |
| `CMD-UDG-015004-04` | `ADD ACLRULEADV6IPSEC` | ADD | ACLRULEADV6IPSEC | IPv6 高级ACL规则（★25参数；ACLSRCWILD/ACLDESTWILD 为正掩码前缀长度0~128，与 v4 反掩码语义相反；ACLPROTOCOLTYPE=Number/WellKnow；WellKnow 时 ACLPROTOCOLNAME 取 GRE/ICMPv6/OSPF/TCP/UDP 等） | ACLNAME, ACLRULENAME, ACLRULEID, ACLACTION, ACLFRAGTYPE, ACLSOURCEIP, ACLSRCWILD(前缀长度), VRFNAME, ACLPROTOCOL, ACLPROTOCOLTYPE, ACLPROTOCOLNAME, ACLDESTIP, ACLDESTWILD(前缀长度), ACLSRCPORTOP/BEGIN/END, ACLDESTPORTOP/B/E, ACLPRECEDENCE, ACLTOS, ACLDSCP, ACLICMPNAME/TYPE/PCODE | EV-IPSEC-02 |

### 1.2 IPSec 安全提议（UDG，1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-05` | `ADD IPSECPROPOSALIPSEC` | ADD | IPSECPROPOSALIPSEC | IPsec安全提议（6参数；★IPSECPROTOCOL=Ah_esp时 ESPAUTHALGO/ESPENCRYPTALGO 与 AHAUTHALGO 均条件必选；★国密场景 ESPENCRYPTALGO=Sm4/ESPAUTHALGO=Sm3/AHAUTHALGO=Sm3 取值在手册枚举内） | PROPOSALNAME, IPSECPROTOCOL(Ah/Esp/Ah_esp), ESPAUTHALGO(Md5/Sha1/Sha2_256/Sha2_384/Sha2_512/Null/Sm3), ESPENCRYPTALGO(Des/A3des/Aes_128/192/256/Sm4/Aes_gcm_128/256/Aes_gmac_128/Null), AHAUTHALGO(Md5/Sha1/Sha2_256/384/512/Sm3), ENCAPMODE(Transport/Tunnel) | EV-IPSEC-01 |

### 1.3 IKE 安全提议（UDG，1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-06` | `ADD IKEPROPOSAL` | ADD | IKEPROPOSAL | IKE安全提议（★11参数；★DHGROUP 不能配置为 None 或不配置，建议 Dh_group19；★国密 IKEv1 场景 AUTHMETHOD=Digital_envelope + ASYMENCRALG=Sm2 + ENCRALGORITHM=Sm4 + INTEGALGORITHM=Sm3） | PROPOSALNUMBER(1~100, 101为系统默认仅查询), AUTHMETHOD(Pre_share/Rsa_signature/Cert_signature/**Digital_envelope**), AUTHALGORITHM, ENCRALGORITHM(含**Sm4**), INTEGALGORITHM(含**Sm3**), DHGROUP(None/Dh_group1/2/5/14/19/20/31), REAUTHINTERVAL, SADURATION, SIGHASHALGNEGSW, SIGNPADDING, **ASYMENCRALG(NULL/Sm2)** | EV-IPSEC-01 |

### 1.4 IKE 对等体（UDG，2个：IPv4 + IPv6）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-07` | `ADD IKEPEER` | ADD | IKEPEER | IPv4 IKE对等体（★21参数；★缺省同时开 IKEv1+IKEv2，对端不支持 v2 时 VERSION2=FALSE；★国密场景不用 PRESHAREDKEY，改用 CERTLOCALFILE+ENCCERTLOCFILE 证书；★指定本端接口场景 IKEPEER 的 LOWREMOTEADDR 配置对端 LoopBack IP） | PEERNAME, PRESHAREDKEY, EXCHANGEMODE(Main/Aggressive), NATTRAVERSAL, PROPOSAL, LOCALIDTYPE(Ip/Fqdn/User_fqdn/Dn/Ip_disable), REMOTEID, VERSION1, VERSION2, LOWREMOTEADDR(IPv4), INVRFNAME, OUTVRFNAME, AUTHADDRESS, AUTHENDADDRESS, **CERTLOCALFILE**, DPDHASHSEQ, IKEMSGSYNC, IPSECMSGSYNC, **ENCCERTLOCFILE**, CERTSCENARIO, ENCCERTSCENARIO, CUSTOMPARA | EV-IPSEC-01 |
| `CMD-UDG-015004-08` | `ADD IKEPEER6` | ADD | IKEPEER6 | IPv6 IKE对等体（★20参数；★与 v4 差异：LOWREMOTEADDR/AUTHADDRESS/AUTHENDADDRESS 改为 IPv6 类型；LOCALIDTYPE 取值 IPv6/Fqdn_ipv6/User_fqdn_ipv6/Dn_ipv6；★仅 VERSION2 参数，无 VERSION1） | PEERNAME, PRESHAREDKEY, EXCHANGEMODE, NATTRAVERSAL, PROPOSAL, LOCALIDTYPE(IPv6/Fqdn_ipv6/...), REMOTEID, VERSION2, LOWREMOTEADDR(IPv6), INVRFNAME, OUTVRFNAME, AUTHADDRESS(IPv6), AUTHENDADDRESS(IPv6), CERTLOCALFILE, DPDHASHSEQ, IKEMSGSYNC, IPSECMSGSYNC, ENCCERTLOCFILE, CERTSCENARIO, ENCCERTSCENARIO, CUSTOMPARA | EV-IPSEC-02 |

### 1.5 IPSec 安全策略（UDG，3个：IPv4 + IPv6 + 模板）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-09` | `ADD IPSECPOLICY` | ADD | IPSECPOLICY | IPv4 IPsec策略（★27参数；★主备场景 WORKMODE=Master_standby + AUTOSWITCHBACK；★多Sequence场景同 POLICYNAME 下多 SEQUENCENUMBER 各绑不同 ACLNUMBER+IKEPEER；★POLICYMODE 仅 Isakmp） | POLICYNAME, SEQUENCENUMBER(1~10000), POLICYMODE(Isakmp), TEMPLATEMODE(None/PolicyTemplate), ACLNUMBER(3000~3999), ACLNAME, TRAFFSADISFLG, SALIFETIMEKB, SALIFETIMESEC, PFS, DSCPINSELECT/BOUNDVAL, DSCPOUTSELECT/BOUNDVAL, ANTIREPLAYENUM, WINDOWSIZE, DFBITCLEAR, FRAGBEFOREENCR, INSPEEDLIMIT, OUTSPEEDLIMIT, LOGENABLE, **WORKMODE(Round_robin/Master_standby)**, **AUTOSWITCHBACK(Disable/Enable)**, ACLTYPE(AclIPv4/AclIPv6), ESN, TFCENABLE, TEMPLATENAME | EV-IPSEC-01 |
| `CMD-UDG-015004-10` | `ADD IPSECPOLICY6` | ADD | IPSECPOLICY6 | IPv6 IPsec策略（★28参数；★与 v4 差异：新增 ACL6NUMBER/ACL6NAME + ACLTYPE 必选区分 v4/v6；★IPv6 不支持 Round_robin，配置后实际以 Master_standby 生效） | POLICYNAME, SEQUENCENUMBER, POLICYMODE, TEMPLATEMODE, ACLNUMBER, ACLNAME, **ACL6NUMBER**, **ACL6NAME**, **ACLTYPE(AclIPv4/AclIPv6,必选)**, TRAFFSADISFLG, SALIFETIMEKB, SALIFETIMESEC, PFS, DSCPIN/OUT系列, ANTIREPLAYENUM, WINDOWSIZE, DFBITCLEAR, FRAGBEFOREENCR, INSPEEDLIMIT, OUTSPEEDLIMIT, LOGENABLE, WORKMODE(不支持Round_robin), AUTOSWITCHBACK, ESN, TFCENABLE | EV-IPSEC-02 |
| `CMD-UDG-015004-11` | `ADD IPSECPOLICYTM` | ADD | IPSECPOLICYTM | IPsec策略模板（TEMPLATEMODE=PolicyTemplate 时本端作为响应方；★22参数；PEERNAME+IPSECPROPNAME 直接绑定，不需 ATTACHIKEPEER/PROPATTACHIPSECPROPOSAL） | POLICYNAME, SEQUENCENUMBER, PEERNAME, IPSECPROPNAME, ACLNAME, ACLNUMBER, TRAFFSADISFLG, SALIFETIMEKB/SEC, PFS, DSCPIN/OUT系列, ANTIREPLAYENUM, WINDOWSIZE, DFBITCLEAR, FRAGBEFOREENCR, INSPEEDLIMIT, OUTSPEEDLIMIT, ACLTYPE, ESN, TFCENABLE | EV-IPSEC-01 |

### 1.6 策略绑定关系（UDG，2个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-12` | `ADD PROPATTACHIPSECPROPOSAL` | ADD | PROPATTACHIPSECPROPOSAL | 策略↔提议绑定（5参数；与 POLICYNAME+SEQUENCENUMBER+POLICYMODE+TEMPLATEMODE 四元组定位策略行） | POLICYNAME, SEQUENCENUMBER, POLICYMODE, TEMPLATEMODE, IPSECPROPNAME | EV-IPSEC-01 |
| `CMD-UDG-015004-13` | `ADD ATTACHIKEPEER` | ADD | ATTACHIKEPEER | 策略↔IKE对等体绑定（★6参数；★主备场景同一 SEQUENCENUMBER 下 ATTACHIKEPEER 执行2次，PEERPRIORITY=1主/2备；★多Sequence场景不同 SEQUENCENUMBER 各绑1个 IKEPEER，PEERPRIORITY 均可=1） | POLICYNAME, SEQUENCENUMBER, POLICYMODE, TEMPLATEMODE, IKEPEERNAME, **PEERPRIORITY(1~3)** | EV-IPSEC-01 |

### 1.7 隧道接口应用 + IKE全局配置（UDG，2个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-14` | `ADD IPSECINTFCFGIPSEC` | ADD | IPSECINTFCFGIPSEC | IPsec隧道接口应用策略（★4参数；★★指定本端接口场景独有 SRCIFNAME=LoopBack1，仅支持环回口，作为 IKE 协商源IP；★与 VNRS侧 ADD IPSECINTFCFG 双配，VNRS侧仅2参数无 POLICYNAME/SRCIFNAME） | INTERFACENAME, TNLTYPE(IPSEC/IPSEC6), POLICYNAME, **SRCIFNAME(仅环回口)** | EV-IPSEC-01/07 |
| `CMD-UDG-015004-15` | `SET IKEGLOBALCONFIG` | SET | IKEGLOBALCONFIG | IKE全局配置（★19参数；DPD/NAT保活/抗重放/SA生命周期/流控/CPU告警等；DPDTYPE=Periodic/Ondemand 时 DPDINTERVAL 条件必选；★NAT穿越场景 NATKLI 生效） | DFBITCLEAR, FRAGBEFOREENCR, TRAFFSADISFLG, TRAFFICSADURTN, TIMESADURTN, ANTIREPLFLG, WINDOWSIZE, LOCALNAME, DPDTYPE(None/Periodic/Ondemand), DPDINTERVAL, DPDRETRYINTRVL, NUMBER, DOSTHRESHOLD, NATKLI, CPUREPORTTHRES, CPUCLEARTHRES, UIKECHECKTIME, FLOWCTRLSTHRES, FLOWCTRLRTHRES | EV-IPSEC-01 |

### 1.8 国密独有命令族（UDG，3个配置 + 1查询）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-16` | `SET FWSOFTPARA` | SET | FWSOFTPARA | ServiceFabric软参（★国密开关：PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1；所有国密场景必须先开此开关） | PARAMETERSTYPE(DWORD/DWORD_EX), DWORDINDEX(1~2048), DWORDVALUE, EXTENDDWORDINDEX, EXTENDDWORDVALUE | EV-IPSEC-GM |
| `CMD-UDG-015004-17` | `ADD CERTSCENE` | ADD | CERTSCENE | 证书场景（★国密证书认证：SCENETYPE=CA 创建CA证书场景，SCENETYPE=LOCAL+CERTTYPE=Cert_sig/Cert_enc 创建签名/加密证书场景；与 IKEPEER 的 CERTSCENARIO/ENCCERTSCENARIO 关联） | SCENENAME, SCENETYPE(CA/LOCAL), ENDESCRIPTION, CNDESCRIPTION, CERTTYPE(NULL/Cert_sig/Cert_enc) | EV-IPSEC-GM |
| `CMD-UDG-015004-18` | `SET PKICRLCHECK` | SET | PKICRLCHECK | CRL检查使能（国密证书吊销检查，可选） | ISCRLENABLE(TRUE/FALSE) | EV-IPSEC-GM |
| `CMD-UDG-015004-Q1` | `DSP PKICERTLIST` | DSP | PKICERTLIST | 查询证书列表（调测查询类，本期略，参数 FILETYPE/FILENAME/PODNAME） | 调测查询类，本期略 | EV-IPSEC-GM |

### 1.9 GRE over IPsec 独有（UDG，1个，归属 VNRS侧）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-19` | `ADD GRETUNNEL` | ADD | GRETUNNEL | GRE隧道（★17参数；GRE over IPsec 场景：Tunnel1(GRE)承载组播/广播业务 + Tunnel2(IPsec)加密GRE报文；SRCTYPE=if_name + SRCIFNAME=LoopBack1 指定源接口） | TNLNAME, TNLTYPE(gre/gre6), SRCTYPE(no_type/ip_address/if_name), SRCTYPE6, SRCIPADDR, SRCIPV6ADDR, SRCIFNAME, DSTIPADDR, DSTIPV6ADDR, DSTVPNNAME, KEEPALVEN, KEEPALVPERIOD, KEEPALVRETRYCNT, GREKEYEN, GREKEY, CHECKSUMEN, STATENABLE, REDUNDANCYEN | EV-IPSEC-04 |

### 1.10 IPsec微服务双配命令族（UDG，6个，参数简化版）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015004-20` | `ADD L3VPNINSTIPSEC` | ADD | L3VPNINSTIPSEC | IPsec微服务VPN实例（★仅1参数 VRFNAME，VNRS侧 ADD L3VPNINST 多 VRFDESCRIPTION；双配要求两微服务 VRFNAME 一致） | VRFNAME | EV-IPSEC-01 |
| `CMD-UDG-015004-21` | `ADD VPNINSTAFIPSEC` | ADD | VPNINSTAFIPSEC | IPsec微服务VPN地址族（★仅2参数，VNRS侧 ADD VPNINSTAF 多 VRFRD/IMPOLICYNAME 等9参数） | VRFNAME, AFTYPE(Ipv4uni/Ipv6uni) | EV-IPSEC-01 |
| `CMD-UDG-015004-22` | `ADD INTERFACEIPSEC` | ADD | INTERFACEIPSEC | IPsec微服务接口（8参数；与 VNRS侧 ADD INTERFACE 对称） | IFNAME, IFDESCR, IFADMINSTATUS(Down/Up), IFMTU, IFDF, IFSTATIENABLE, IFTRAPENABLE, IFSTATITVL | EV-IPSEC-01 |
| `CMD-UDG-015004-23` | `ADD IPBINDVPNIPSEC` | ADD | IPBINDVPNIPSEC | IPsec微服务绑定VPN（★7参数；★清除接口下所有IP配置，须在 ADD IPSECINTFCFGIPSEC 之前执行；支持 IPv4/IPv6 双地址） | IFNAME, VRFNAME, IPTYPECHECK(Ipv4/Ipv6), IFIPADDR, SUBNETMASK, IPV6ADDR, SUBNETMASKIPV6 | EV-IPSEC-01 |
| `CMD-UDG-015004-24` | `ADD IFIPV4ADDRESSIPSEC` | ADD | IFIPV4ADDRESSIPSEC | IPsec微服务IPv4地址（4参数；与 VNRS侧 ADD IFIPV4ADDRESS 对称） | IFNAME, IFIPADDR, SUBNETMASK, ADDRTYPE(Main/Sub/Brwd/Brw) | EV-IPSEC-01 |
| `CMD-UDG-015004-25` | `ADD IFIPV6ADDRESSIPSEC` | ADD | IFIPV6ADDRESSIPSEC | IPsec微服务IPv6地址（IPv6场景双配；⚠️手册未在本特性树定位，参照 IFIPV4ADDRESSIPSEC 结构推断，需复核） | ⚠️手册未定位（IPv6场景激活文档引用，参数结构推断 IFNAME/IPV6ADDR/PREFIXLEN） | EV-IPSEC-02 |

### 1.11 查询/调测类（本期略）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 说明 |
|--------------|----------------|--------|------------------|-------------------|------|
| `CMD-UDG-015004-Q2` | `DSP IKESA` | DSP | IKESA | 显示IKE安全联盟 | 调测查询类，本期略 |
| `CMD-UDG-015004-Q3` | `DSP IKEIPSECSA` | DSP | IKEIPSECSA | 显示IKE IPsec安全联盟 | 调测查询类，本期略 |
| `CMD-UDG-015004-Q4` | `LST IKEPEER/IKEPROPOSAL/IPSECPOLICY/IPSECPROPOSALIPSEC` 等 | LST | — | 查询各类配置 | 调测查询类，本期略 |
| `CMD-UDG-015004-Q5` | `DSP IPSECPATHMTU` / `RST IPSECPATHMTU` | DSP/RST | — | Path MTU 查询/复位 | 调测查询类，本期略 |
| `CMD-UDG-015004-Q6` | `RTR IKESA` / `RTR IKEIPSECSA` | RTR | — | 恢复安全联盟 | 调测查询类，本期略 |

---

## 2. ConfigObject 实例化（25 个核心 + 引用）

### 2.1 ACL 数据流定义（4个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-ACLGROUPIPSEC` | ACLGROUPIPSEC | UDG | composite | ACLNAME | ACLSTEP, ACLTYPE, ACLMATCHORDER | **contains** ACLRULEADV4IPSEC |
| `OBJ-ACLRULEADV4IPSEC` | ACLRULEADV4IPSEC | UDG | entity | ACLNAME, ACLRULENAME | ACLACTION, ACLSOURCEIP/SRCWILD, ACLDESTIP/DESTWILD, ACLPROTOCOL | belongs_to ACLGROUPIPSEC；refers_to VPNINST(VRFNAME) |
| `OBJ-ACLGROUP6IPSEC` | ACLGROUP6IPSEC | UDG | composite | ACLNAME | 同 ACLGROUPIPSEC | **contains** ACLRULEADV6IPSEC |
| `OBJ-ACLRULEADV6IPSEC` | ACLRULEADV6IPSEC | UDG | entity | ACLNAME, ACLRULENAME | ACLACTION, ACLSOURCEIP/SRCWILD(前缀长度), ACLDESTIP/DESTWILD(前缀长度), ACLPROTOCOL/PROTOCOLTYPE | belongs_to ACLGROUP6IPSEC；refers_to VPNINST |

### 2.2 IPSec 提议 + IKE 提议（2个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-IPSECPROPOSALIPSEC` | IPSECPROPOSALIPSEC | UDG | entity | PROPOSALNAME | IPSECPROTOCOL, ESPAUTHALGO, ESPENCRYPTALGO, AHAUTHALGO, ENCAPMODE | refers_to（被 IPSECPOLICY/PROPATTACHIPSECPROPOSAL 引用） |
| `OBJ-IKEPROPOSAL` | IKEPROPOSAL | UDG | entity | PROPOSALNUMBER | AUTHMETHOD, AUTHALGORITHM, ENCRALGORITHM, INTEGALGORITHM, DHGROUP, ASYMENCRALG, SADURATION | refers_to（被 IKEPEER.PROPOSAL 引用） |

### 2.3 IKE 对等体（2个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-IKEPEER` | IKEPEER | UDG | entity | PEERNAME | PRESHAREDKEY/CERTLOCALFILE, EXCHANGEMODE, NATTRAVERSAL, LOCALIDTYPE, VERSION1/2, LOWREMOTEADDR(IPv4), INVRFNAME/OUTVRFNAME | refers_to IKEPROPOSAL(PROPOSAL)；refers_to CERTSCENE(国密) |
| `OBJ-IKEPEER6` | IKEPEER6 | UDG | entity | PEERNAME | 同 IKEPEER 但地址 IPv6 化，仅 VERSION2 | refers_to IKEPROPOSAL；refers_to CERTSCENE |

### 2.4 IPSec 策略 + 绑定关系（5个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-IPSECPOLICY` | IPSECPOLICY | UDG | composite | POLICYNAME, SEQUENCENUMBER | POLICYMODE, TEMPLATEMODE, ACLNUMBER/NAME, WORKMODE, AUTOSWITCHBACK, ACLTYPE, SALIFETIMESEC/KB, PFS, ANTIREPLAYENUM | **contains**（逻辑）多 SEQUENCENUMBER；refers_to ACLGROUPIPSEC |
| `OBJ-IPSECPOLICY6` | IPSECPOLICY6 | UDG | composite | POLICYNAME, SEQUENCENUMBER | 同 IPSECPOLICY + ACL6NUMBER/ACL6NAME；ACLTYPE 必选 | refers_to ACLGROUP6IPSEC |
| `OBJ-IPSECPOLICYTM` | IPSECPOLICYTM | UDG | composite | POLICYNAME, SEQUENCENUMBER | PEERNAME, IPSECPROPNAME 直接绑定，ACLNAME/NUMBER | refers_to IKEPEER + IPSECPROPOSALIPSEC |
| `OBJ-PROPATTACHIPSECPROPOSAL` | PROPATTACHIPSECPROPOSAL | UDG | binding | POLICYNAME, SEQUENCENUMBER, POLICYMODE, TEMPLATEMODE | IPSECPROPNAME | links IPSECPOLICY to IPSECPROPOSALIPSEC |
| `OBJ-ATTACHIKEPEER` | ATTACHIKEPEER | UDG | binding | POLICYNAME, SEQUENCENUMBER, POLICYMODE, TEMPLATEMODE | IKEPEERNAME, PEERPRIORITY(1~3) | links IPSECPOLICY to IKEPEER |

### 2.5 隧道接口应用 + IKE全局 + 国密（5个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-IPSECINTFCFGIPSEC` | IPSECINTFCFGIPSEC | UDG | binding | INTERFACENAME, TNLTYPE | POLICYNAME, SRCIFNAME(借用环回口) | links Tunnel接口 to IPSECPOLICY |
| `OBJ-IKEGLOBALCONFIG` | IKEGLOBALCONFIG | UDG | entity | — | DPDTYPE/INTERVAL/RETRYINTRVL, NATKLI, ANTIREPLFLG, WINDOWSIZE, TIMESADURTN/TRAFFICSADURTN | activates 全局 IKE 行为 |
| `OBJ-FWSOFTPARA` | FWSOFTPARA | UDG | entity | PARAMETERSTYPE, DWORDINDEX | DWORDVALUE（国密开关 1401=1） | activates 国密算法支持 |
| `OBJ-CERTSCENE` | CERTSCENE | UDG | composite | SCENENAME | SCENETYPE(CA/LOCAL), CERTTYPE(Cert_sig/Cert_enc) | **contains** 证书文件；refers_to IKEPEER.CERTSCENARIO |
| `OBJ-PKICRLCHECK` | PKICRLCHECK | UDG | entity | — | ISCRLENABLE | activates CRL吊销检查 |

### 2.6 GRE隧道 + IPsec微服务双配（7个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-GRETUNNEL` | GRETUNNEL | UDG | entity | TNLNAME | TNLTYPE(gre/gre6), SRCTYPE, SRCIFNAME, DSTIPADDR, KEEPALVEN | refers_to LoopBack接口（源） |
| `OBJ-L3VPNINSTIPSEC` | L3VPNINSTIPSEC | UDG | entity | VRFNAME | —（简化版） | 双配 refers_to L3VPNINST |
| `OBJ-VPNINSTAFIPSEC` | VPNINSTAFIPSEC | UDG | entity | VRFNAME, AFTYPE | —（简化版） | belongs_to L3VPNINSTIPSEC |
| `OBJ-INTERFACEIPSEC` | INTERFACEIPSEC | UDG | entity | IFNAME | IFADMINSTATUS, IFMTU | — |
| `OBJ-IPBINDVPNIPSEC` | IPBINDVPNIPSEC | UDG | binding | IFNAME, VRFNAME | IPTYPECHECK, IFIPADDR/IPV6ADDR | links INTERFACEIPSEC to L3VPNINSTIPSEC |
| `OBJ-IFIPV4ADDRESSIPSEC` | IFIPV4ADDRESSIPSEC | UDG | entity | IFNAME, IFIPADDR | SUBNETMASK, ADDRTYPE | belongs_to INTERFACEIPSEC |
| `OBJ-IFIPV6ADDRESSIPSEC` | IFIPV6ADDRESSIPSEC | UDG | entity | IFNAME | IPV6ADDR（⚠️手册未定位全参数） | belongs_to INTERFACEIPSEC |

---

## 3. ConfigObject 间关系边（§11.7）

### 3.1 contains 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| ACLGROUPIPSEC | `contains` | ACLRULEADV4IPSEC | IPv4 ACL规则组包含规则（一个规则组多条规则） |
| ACLGROUP6IPSEC | `contains` | ACLRULEADV6IPSEC | IPv6 ACL规则组包含规则 |
| CERTSCENE | `contains` | 证书文件 | 证书场景包含 CA/LOCAL 证书（LOCAL 下分 Cert_sig/Cert_enc） |

### 3.2 refers_to 边（8条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| ACLRULEADV4IPSEC | `refers_to` | VPNINST | ACL规则引用 VPN 实例（VRFNAME） |
| IKEPEER | `refers_to` | IKEPROPOSAL | IKE对等体引用 IKE安全提议（PROPOSAL） |
| IKEPEER | `refers_to` | CERTSCENE | 国密场景 IKE对等体引用证书场景（CERTSCENARIO/ENCCERTSCENARIO） |
| IPSECPOLICY | `refers_to` | ACLGROUPIPSEC | IPsec策略引用 ACL规则组（ACLNUMBER/ACLNAME） |
| PROPATTACHIPSECPROPOSAL | `refers_to` | IPSECPROPOSALIPSEC | 策略绑定提议引用 IPsec安全提议 |
| ATTACHIKEPEER | `refers_to` | IKEPEER | 策略绑定对等体引用 IKE对等体 |
| IPSECINTFCFGIPSEC | `refers_to` | IPSECPOLICY | 隧道接口引用 IPsec安全策略（POLICYNAME） |
| IPSECINTFCFGIPSEC | `refers_to` | LoopBack接口 | 指定本端接口场景 SRCIFNAME 借用环回口作 IKE源IP |

### 3.3 depends_on 边（6条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| ACLRULEADV4IPSEC | `depends_on` | ACLGROUPIPSEC | 规则依赖规则组存在（先 ADD ACLGROUPIPSEC） |
| IPSECPOLICY | `depends_on` | ACLGROUPIPSEC + IKEPEER + IPSECPROPOSALIPSEC | 策略依赖 ACL+对等体+提议（手册：先配 ACL/提议/IKE，再配策略） |
| ATTACHIKEPEER | `depends_on` | IPSECPOLICY + IKEPEER | 绑定依赖策略与对等体存在 |
| IPSECINTFCFGIPSEC | `depends_on` | IPSECPOLICY + Tunnel接口 | 接口应用策略依赖策略与接口存在 |
| IPsec微服务VPN/接口/地址 | `depends_on` | VNRS侧对应配置 | ★双配原则：IPsec微服务配置必须与 VNRS微服务一对一一致（手册原文强约束） |
| IKEPEER（国密） | `depends_on` | CERTSCENE + FWSOFTPARA | 国密对等体依赖证书场景 + 国密开关（DWORD 1401=1） |

### 3.4 activates 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| IKEGLOBALCONFIG | `activates` | IKEPEER/IKEPROPOSAL | 全局 DPD/NAT保活/抗重放 激活 IKE 行为 |
| FWSOFTPARA (DWORD 1401=1) | `activates` | IKEPROPOSAL 国密算法 | 国密开关激活 SM2/SM3/SM4 算法支持 |
| PKICRLCHECK | `activates` | CERTSCENE | CRL检查激活证书吊销校验 |

---

## 4. CommandRule 实例化（本特性相关，8条）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-015004-01` | DHGROUP 不能为 None 或不配置 | `parameter_dependency` | explicit | restriction | parameter | CMD-UDG-015004-06.DHGROUP (ADD IKEPROPOSAL) | 手册原文：DHGROUP 参数不能配置为 None 或者不配置，建议配置为 Dh_group19 | SA 协商失败 | critical | EV-IPSEC-01 |
| `CR-015004-02` | ACL 仅支持源/目的IP，端口配置不生效 | `semantic_rule` | explicit | restriction | parameter | CMD-UDG-015004-02/04 (ACLRULEADV4/6IPSEC) | 手册原文：ACL 只支持源IP和目的IP的配置，如果配置了端口，不会对端口配置生效 | 端口过滤失效，数据流匹配范围扩大 | warning | EV-IPSEC-01 |
| `CR-015004-03` | GRE 与 IPSec 源地址互斥（GRE over IPsec 双隧道编排） | `semantic_rule` | explicit | config | relation | OBJ-GRETUNNEL ↔ OBJ-IPSECINTFCFGIPSEC | GRE over IPsec 场景：Tunnel1(GRE) 用 LoopBack1 作源，Tunnel2(IPsec) ACL 匹配 LoopBack 间流量；GRE源地址与 IPSec 隧道地址不可共用同一接口（避免递归封装） | 隧道无法UP或递归封装 | critical | EV-IPSEC-04 |
| `CR-015004-04` | 主备隧道 PEERPRIORITY 主1备2 | `parameter_dependency` | explicit | config | parameter | CMD-UDG-015004-13.PEERPRIORITY (ADD ATTACHIKEPEER) | 主备场景（WORKMODE=Master_standby）：同一 SEQUENCENUMBER 下 ATTACHIKEPEER 执行2次，主用 PEERPRIORITY=1，备用 PEERPRIORITY=2；★IPv6 不支持 Round_robin，配置后实际以 Master_standby 生效 | 主备切换失效 | critical | EV-IPSEC-03 |
| `CR-015004-05` | 多Sequence 同 POLICYNAME 各绑不同 ACL+Peer | `parameter_dependency` | explicit | config | parameter | CMD-UDG-015004-09/10.SEQUENCENUMBER | 多Sequence场景：同一 POLICYNAME 下多 SEQUENCENUMBER（如10/20），每 sequence 各绑不同 ACLNUMBER（如3000/3001）+ 不同 IKEPEERNAME，PEERPRIORITY 均可=1（跨 sequence 优先级独立） | 单隧道多对端协商混乱 | critical | EV-IPSEC-06 |
| `CR-015004-06` | 双微服务双配一致性 | `semantic_rule` | explicit | config | relation | VNRS微服务 ↔ IPsec微服务 | 手册原文：IPsec协商用到的隧道接口、隧道接口IP、隧道类型、VPN 以及指定本端接口建立IPsec隧道的接口需要在 VNRS微服务和IPsec微服务上一对一的配置；若未遵循双配原则会导致业务不通；删除时也须同时删除两侧 | 业务不通 | critical | EV-IPSEC-01 |
| `CR-015004-07` | 指定本端接口 SRCIFNAME 仅支持环回口 | `parameter_dependency` | explicit | restriction | parameter | CMD-UDG-015004-14.SRCIFNAME (ADD IPSECINTFCFGIPSEC) | 手册原文：SRCIFNAME 地址借用接口名称，只支持配置环回口；多个IPsec隧道可指定同一个LoopBack口，但被指定接口需被IPsec隧道单独使用 | 借用失败或接口冲突 | warning | EV-IPSEC-07 |
| `CR-015004-08` | 国密场景必须先开 FWSOFTPARA DWORD 1401 | `sequence_rule` | explicit | config | command | CMD-UDG-015004-16 (SET FWSOFTPARA) | 国密场景所有配置前必须 SET FWSOFTPARA:PARAMETERSTYPE=DWORD,DWORDINDEX=1401,DWORDVALUE=1；且 IKEPROPOSAL 改用 Digital_envelope+SM2/SM3/SM4，IKEPEER 改用 CERTLOCALFILE/ENCCERTLOCFILE 替代 PRESHAREDKEY | 国密算法不生效，SA协商失败 | critical | EV-IPSEC-GM |

---

## 5. MMLCommand 关键参数集（核心命令全参数）

> **Schema 参考**：§11.4 CommandParameter。`required_mode` 取值 `required / optional / conditional_required`（Schema §11.4 必备字段）。本节核心命令的参数表已从手册原文抽取全量参数。

### 5.1 ADD ACLGROUPIPSEC（IPv4 ACL规则组，5 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| ACLNAME | string/int | 字符串1~32（a~z/A~Z开头，区分大小写）或整数3000~3999 | `required` | 无 | 规则组标识（名称或编号） |
| ACLSTEP | int | 1~20 | `optional` | 5 | 规则组步长（仅不指定规则ID时生效） |
| ACLTYPE | enum | Basic / Advance | `optional` | 无（ACLNAME非数字时默认Advance） | 规则组类型 |
| ACLMATCHORDER | enum | Config / Auto | `optional` | Config | 规则匹配顺序（配置优先/深度优先） |
| ACLDESCRIPTION | string | 1~127（支持空格，区分大小写） | `optional` | 无 | 规则组描述 |

### 5.2 ADD ACLRULEADV4IPSEC（IPv4 高级ACL规则，25 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| ACLNAME | string/int | 同 ADD ACLGROUPIPSEC.ACLNAME | `required` | 无 | 所属规则组 |
| ACLRULENAME | string | 1~32（不支持空格，区分大小写） | `required` | 无 | 规则名称 |
| ACLRULEID | int | 0~4294967294 | `optional` | 无（按步长增长） | 规则ID |
| ACLACTION | enum | Permit / Deny | `required` | 无 | 规则行为 |
| ACLFRAGTYPE | enum | FragmentSubseq/Fragment/NonFragment/NonSubseq/FragmentSpeFirst/Unconfiged | `optional` | 无（不校验分片） | 报文分片类型 |
| ACLSOURCEIP | IPv4 | 0.0.0.0~255.255.255.255 | `optional` | 0.0.0.0 | 源IP地址 |
| ACLSRCWILD | IPv4 | 0.0.0.0~255.255.255.255 | `optional` | 255.255.255.255 | ★源IP反掩码（0=精确匹配，1=任意） |
| VRFNAME | string | 1~31（不支持空格，区分大小写） | `optional` | 无 | VPN实例名称 |
| ACLPROTOCOL | int | 0~255 | `required` | 无 | 协议类型值（0=IP/1=ICMP/2=IGMP/6=TCP/17=UDP/89=OSPF） |
| ACLDESTIP | IPv4 | 0.0.0.0~255.255.255.255 | `optional` | 0.0.0.0 | 目的IP地址 |
| ACLDESTWILD | IPv4 | 0.0.0.0~255.255.255.255 | `optional` | 255.255.255.255 | ★目的IP反掩码 |
| ACLSRCPORTOP | enum | Unconfiged/Lt/Eq/Gt/Range | `optional` | 无（不校验源端口） | 源端口范围类型 |
| ACLSRCPORTBEGIN | int | 0~65535 | `conditional_required` | 无 | 源端口起始（ACLSRCPORTOP=Eq/Gt/Range 时必填） |
| ACLSRCPORTEND | int | 0~65535 | `conditional_required` | 无 | 源端口结束（ACLSRCPORTOP=Lt/Range 时必填） |
| ACLDESTPORTOP | enum | Unconfiged/Lt/Eq/Gt/Range | `optional` | 无 | 目的端口范围类型 |
| ACLDESTPORTBEGIN | int | 0~65535 | `conditional_required` | 无 | 目的端口起始 |
| ACLDESTPORTEND | int | 0~65535 | `conditional_required` | 无 | 目的端口结束 |
| ACLPRECEDENCE | int | 0~7 | `optional` | 无 | 报文优先级（不可与 ACLDSCP 同配） |
| ACLTOS | int | 0~15 | `optional` | 无 | 服务优先级（不可与 ACLDSCP 同配） |
| ACLDSCP | int | 0~63 | `optional` | 无 | DSCP值（不可与 ACLPRECEDENCE/ACLTOS 同配） |
| ACLICMPNAME | enum | Unconfiged/Echo/EchoReply/.../Custom | `optional` | 无 | ICMP名称（仅 ACLPROTOCOL=1 生效） |
| ACLICMPTYPE | int | 0~255 | `conditional_required` | 无 | ICMP类型（ACLICMPNAME=Custom 时必填） |
| ACLICMPCODE | int | 0~255 | `conditional_required` | 无 | ICMP消息码（ACLICMPNAME=Custom 时必填） |
| ACLSYNFLAG | int | 0~63 | `optional` | 无 | TCP-FLAG值（仅 ACLPROTOCOL=6 生效） |
| ACLRULEDESCRIPTION | string | 1~127（支持空格） | `optional` | 无 | 规则描述 |

### 5.3 ADD ACLRULEADV6IPSEC（IPv6 高级ACL规则，25 参数；与 v4 关键差异）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| ACLNAME | string/int | 同 v4 | `required` | 无 | 所属规则组 |
| ACLRULENAME | string | 1~32 | `required` | 无 | 规则名称 |
| ACLRULEID | int | 0~4294967294 | `optional` | 无 | 规则ID |
| ACLACTION | enum | Permit / Deny | `required` | 无 | 规则行为 |
| ACLFRAGTYPE | enum | 同 v4 | `optional` | 无 | 分片类型 |
| ACLSOURCEIP | IPv6 | IPv6地址类型 | `optional` | 无 | ★源IPv6地址 |
| ACLSRCWILD | int | 0~128 | `optional` | 无 | ★★源IPv6前缀长度（正掩码，与v4反掩码语义相反；128=精确） |
| VRFNAME | string | 1~31 | `optional` | 无 | VPN实例 |
| ACLPROTOCOL | int | 0~255 | `conditional_required` | 无 | 协议类型值（ACLPROTOCOLTYPE=Number 时必填） |
| ACLPROTOCOLTYPE | enum | Number / WellKnow | `optional` | Number | ★协议选项类型（v4无此参数） |
| ACLPROTOCOLNAME | enum | GRE/HOPOPT/ICMPv6/IPv6/IPv6_AH/IPv6_ESP/OSPF/TCP/UDP | `conditional_required` | 无 | 协议名称（ACLPROTOCOLTYPE=WellKnow 时必填） |
| ACLDESTIP | IPv6 | IPv6地址类型 | `optional` | 无 | 目的IPv6地址 |
| ACLDESTWILD | int | 0~128 | `optional` | 无 | ★★目的IPv6前缀长度（正掩码） |
| ACLSRCPORTOP/BEGIN/END | — | 同 v4 | `optional`/`conditional_required` | 无 | 源端口范围 |
| ACLDESTPORTOP/B/E | — | 同 v4（注意v6命名 ACLDESTPORTB/ACLDESTPORTE） | `optional`/`conditional_required` | 无 | 目的端口范围 |
| ACLPRECEDENCE/ACLTOS/ACLDSCP | — | 同 v4 | `optional` | 无 | 优先级/TOS/DSCP |
| ACLICMPNAME | enum | Unconfiged/Redirect/Echo/.../Custom（IPv6 ICMP集） | `optional` | 无 | ICMPv6名称（ACLPROTOCOL=58 生效） |
| ACLICMPTYPE/PCODE | int | 0~255 | `conditional_required` | 无 | ICMP类型/码（Custom 时必填） |
| ACLRULEDESCRI | string | 1~127 | `optional` | 无 | 规则描述 |

### 5.4 ADD IPSECPROPOSALIPSEC（IPsec安全提议，6 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PROPOSALNAME | string | 1~15（不区分大小写） | `required` | 无 | Proposal名称 |
| IPSECPROTOCOL | enum | Ah / Esp / Ah_esp | `optional` | Esp | IPsec协议 |
| ESPAUTHALGO | enum | Md5/Sha1/Sha2_256/Sha2_384/Sha2_512/Null/Unconfigure/**Sm3** | `conditional_required` | Null | ESP认证算法（IPSECPROTOCOL=Esp/Ah_esp 时条件必选） |
| ESPENCRYPTALGO | enum | Des/A3des/Aes_128/Aes_192/Aes_256/Unconfigure/**Sm4**/Aes_gcm_128/Aes_gcm_256/Aes_gmac_128/Null | `conditional_required` | Aes_gcm_128 | ESP加密算法（IPSECPROTOCOL=Esp/Ah_esp 时条件必选） |
| AHAUTHALGO | enum | Md5/Sha1/Sha2_256/Sha2_384/Sha2_512/Unconfigure/**Sm3** | `conditional_required` | Sha2_256 | AH认证算法（IPSECPROTOCOL=Ah/Ah_esp 时条件必选） |
| ENCAPMODE | enum | Transport / Tunnel | `optional` | Tunnel | 封装模式 |

### 5.5 ADD IKEPROPOSAL（IKE安全提议，★11 参数含国密 ASYMENCRALG）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PROPOSALNUMBER | int | 1~100（101为系统默认，仅查询） | `required` | 无 | 提议编号（仅本端记录，无需与对端一致） |
| AUTHMETHOD | enum | Pre_share / Rsa_signature / Cert_signature / **Digital_envelope** | `optional` | Pre_share | 认证方法（★国密用 Digital_envelope 数字信封） |
| AUTHALGORITHM | enum | Md5/Sha1/Sha2_256/Sha2_384/Sha2_512 | `optional` | Sha2_256 | 认证算法 |
| ENCRALGORITHM | enum | Des_cbc/Aes_cbc_128/Aes_cbc_192/Aes_cbc_256/Alg_3Des_cbc/Aes_gcm_128/Aes_gcm_256/**Sm4** | `optional` | Aes_gcm_128 | 加密算法（★国密用 Sm4） |
| INTEGALGORITHM | enum | Hmac_md5_96/Hmac_sha1_96/Hmac_sha2_256/Hmac_sha2_384/Aes_xcbc_96/**Sm3**/Hmac_sha2_512 | `optional` | Hmac_sha2_256 | 完整性算法（★国密用 Sm3） |
| DHGROUP | enum | None/Dh_group1/Dh_group2/Dh_group5/Dh_group14/Dh_group19/Dh_group20/Dh_group31 | `optional` | Dh_group19 | ★DH组（CR-015004-01：不能为 None 或不配置） |
| REAUTHINTERVAL | int | 60~604800（秒） | `optional` | 无 | 重认证周期 |
| SADURATION | int | 60~604800（秒） | `optional` | 86400 | SA生命周期 |
| SIGHASHALGNEGSW | enum | Disable / Enable | `conditional_required` | Enable | 签名哈希算法协商开关（AUTHMETHOD=Cert_signature 时条件必选） |
| SIGNPADDING | enum | Pkcs / Pss | `conditional_required` | Pss | 签名填充方式（SIGHASHALGNEGSW=Enable 时条件必选） |
| **ASYMENCRALG** | enum | NULL / **Sm2** | `conditional_required` | Sm2 | ★★非对称加密算法（AUTHMETHOD=Digital_envelope 国密时条件必选，取 Sm2） |

### 5.6 ADD IKEPEER（IPv4 IKE对等体，★21 参数含国密证书）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PEERNAME | string | 1~15（不区分大小写） | `required` | 无 | 对端名字 |
| PRESHAREDKEY | pwd | 1~127 | `optional` | 无 | 预共享密钥（★国密场景不用，改用证书） |
| EXCHANGEMODE | enum | Main / Aggressive | `optional` | Main | 交换模式 |
| NATTRAVERSAL | bool | TRUE / FALSE | `optional` | 无 | Nat穿越（TRUE 时 NATKLI 生效） |
| PROPOSAL | int | 1~100（101不可配置） | `optional` | 无 | IKE提议编号（引用 ADD IKEPROPOSAL） |
| LOCALIDTYPE | enum | Ip / Fqdn / User_fqdn / Dn / Ip_disable | `optional` | Ip | 本地ID类型 |
| REMOTEID | string | 1~255 | `optional` | 无 | 远程ID（LOCALIDTYPE为 Fqdn/User_fqdn 时必配） |
| VERSION1 | bool | TRUE / FALSE | `optional` | TRUE | IKE版本1 |
| VERSION2 | bool | TRUE / FALSE | `optional` | TRUE | IKE版本2（★缺省 v1+v2 同开，对端不支持 v2 时 VERSION2=FALSE） |
| LOWREMOTEADDR | IPv4 | IPv4地址 | `optional` | 无 | 远程地址（对端协商IP；指定本端接口场景配对端 LoopBack IP） |
| INVRFNAME | string | 1~47 | `optional` | 无 | SA绑定VPN名称 |
| OUTVRFNAME | string | 1~47 | `optional` | 无 | 远端地址VPN名称 |
| AUTHADDRESS | IPv4 | IPv4地址 | `optional` | 无 | IKE远端认证地址 |
| AUTHENDADDRESS | IPv4 | IPv4地址 | `optional` | 无 | IKE远端认证结尾地址 |
| **CERTLOCALFILE** | string | 1~127 | `optional` | 无 | ★签名证书文件名（国密） |
| DPDHASHSEQ | enum | Hash_notify / Notify_hash | `optional` | Hash_notify | IKEv1 DPD载荷顺序 |
| IKEMSGSYNC | enum | Disable / Enable | `optional` | Disable | IKE消息序列号同步（仅 VERSION2=TRUE 生效） |
| IPSECMSGSYNC | enum | Disable / Enable | `optional` | Disable | IPSEC消息序列号同步 |
| **ENCCERTLOCFILE** | string | 1~127 | `optional` | 无 | ★加密证书文件名（国密） |
| CERTSCENARIO | string | 0~192 | `optional` | 无 | 签名证书场景名称（关联 ADD CERTSCENE） |
| ENCCERTSCENARIO | string | 0~192 | `optional` | 无 | 加密证书场景名称 |
| CUSTOMPARA | int | 0~4294967295 | `optional` | 0 | 自定义参数（国密数字信封场景控制位 bit0~bit10） |

### 5.7 ADD IKEPEER6（IPv6 IKE对等体，20 参数；与 v4 差异点标注）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PEERNAME | string | 1~15 | `required` | 无 | 对等体名称 |
| PRESHAREDKEY | pwd | 1~127 | `optional` | 无 | 预共享密钥 |
| EXCHANGEMODE | enum | Main / Aggressive | `optional` | Main | 交换模式 |
| NATTRAVERSAL | bool | TRUE/FALSE | `optional` | 无 | Nat穿越 |
| PROPOSAL | int | 1~100 | `optional` | 无 | IKE提议 |
| LOCALIDTYPE | enum | ★**IPv6** / Fqdn_ipv6 / User_fqdn_ipv6 / Dn_ipv6 / Ip_disable | `optional` | IPv6 | 本地ID类型（v4 为 Ip/Fqdn/...） |
| REMOTEID | string | 1~255 | `optional` | 无 | 远程ID |
| VERSION2 | bool | TRUE/FALSE | `optional` | TRUE | ★仅 VERSION2（v4 有 VERSION1+VERSION2） |
| LOWREMOTEADDR | IPv6 | IPv6地址 | `optional` | 无 | ★远程地址（IPv6类型，参数名不变） |
| INVRFNAME | string | 1~47 | `optional` | 无 | SA绑定VPN |
| OUTVRFNAME | string | 1~47 | `optional` | 无 | 远端地址VPN |
| AUTHADDRESS | IPv6 | IPv6地址 | `optional` | 无 | ★认证地址（IPv6） |
| AUTHENDADDRESS | IPv6 | IPv6地址 | `optional` | 无 | ★认证结尾地址（IPv6） |
| CERTLOCALFILE | string | 1~127 | `optional` | 无 | 签名证书（国密） |
| DPDHASHSEQ | enum | Hash_notify/Notify_hash | `optional` | Hash_notify | DPD载荷顺序 |
| IKEMSGSYNC | enum | Disable/Enable | `optional` | Disable | IKE消息同步 |
| IPSECMSGSYNC | enum | Disable/Enable | `optional` | Disable | IPSEC消息同步 |
| ENCCERTLOCFILE | string | 1~127 | `optional` | 无 | 加密证书（国密） |
| CERTSCENARIO | string | 0~192 | `optional` | 无 | 签名证书场景 |
| ENCCERTSCENARIO | string | 0~192 | `optional` | 无 | 加密证书场景 |
| CUSTOMPARA | int | 0~4294967295 | `optional` | 0 | 自定义参数 |

### 5.8 ADD IPSECPOLICY（IPv4 IPsec策略，★27 参数含主备 WORKMODE）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POLICYNAME | string | 1~15（不区分大小写） | `required` | 无 | 策略名 |
| SEQUENCENUMBER | int | 1~10000 | `required` | 无 | 序列号（★多Sequence场景同 POLICYNAME 下多个） |
| POLICYMODE | enum | Isakmp | `required` | 无 | 策略模式（仅 ISAKMP） |
| TEMPLATEMODE | enum | None / PolicyTemplate | `required` | 无 | 模板模式 |
| ACLNUMBER | int | 3000~3999 或 0 | `conditional_optional` | 无 | ACL编号（TEMPLATEMODE=None 时；与 ACLNAME 二选一） |
| ACLNAME | string | 1~32（a~z/A~Z开头） | `conditional_optional` | 无 | ACL名称 |
| TRAFFSADISFLG | bool | TRUE/FALSE | `conditional_optional` | FALSE | 去使能SA按流量计长（TEMPLATEMODE=None 时） |
| SALIFETIMEKB | int | 8000~200000000（MByte） | `conditional_optional` | 无 | 基于流量的SA生命周期（TRAFFSADISFLG=FALSE 时） |
| SALIFETIMESEC | int | 0 或 480~604800（秒） | `conditional_optional` | 无（采用 SET IKEGLOBALCONFIG.TIMESADURTN） | SA的生命周期 |
| PFS | enum | None/Dh_group1/2/5/14/19/20/31 | `conditional_optional` | 无 | 前向安全保护 |
| DSCPINSELECT | enum | Af11~43/Cs1~7/Default/Ef/None/EnterDSCPCode | `conditional_optional` | 无 | DSCP入方向 |
| DSCPINBOUNDVAL | int | 0~63 | `conditional_required` | 无 | DSCP入方向值（DSCPINSELECT=EnterDSCPCode 时） |
| DSCPOUTSELECT | enum | 同 DSCPINSELECT | `conditional_optional` | 无 | DSCP出方向 |
| DSCPOUTBOUNDVAL | int | 0~63 | `conditional_required` | 无 | DSCP出方向值 |
| ANTIREPLAYENUM | enum | NotConfigured/Enable/Disable | `conditional_optional` | NotConfigured | 抗重放 |
| WINDOWSIZE | enum | None/Size_32/64/128/256/512/1024 | `conditional_optional` | 无 | 抗重放窗口（ANTIREPLAYENUM=Enable 时） |
| DFBITCLEAR | bool | TRUE/FALSE | `conditional_optional` | FALSE | 清除分片标记 |
| FRAGBEFOREENCR | bool | TRUE/FALSE | `conditional_optional` | FALSE | 加密前分片 |
| INSPEEDLIMIT | int | 8~4194303 或 0（kByte/s） | `conditional_optional` | 无 | 入方向限速 |
| OUTSPEEDLIMIT | int | 8~4194303 或 0 | `conditional_optional` | 无 | 出方向限速 |
| LOGENABLE | bool | TRUE/FALSE | `conditional_optional` | FALSE | 日志使能 |
| **WORKMODE** | enum | **Round_robin** / **Master_standby** | `conditional_optional` | Round_robin | ★★工作模式（主备场景用 Master_standby） |
| **AUTOSWITCHBACK** | enum | Disable / Enable | `conditional_required` | 无 | ★★自动切回（WORKMODE=Master_standby 时必填） |
| ACLTYPE | enum | AclIPv4 / AclIPv6 | `conditional_optional` | AclIPv4 | ACL类型 |
| ESN | enum | Disable / Enable | `conditional_optional` | Disable | 扩展序列号 |
| TFCENABLE | bool | TRUE/FALSE | `conditional_optional` | FALSE | 数据流可信使能 |
| TEMPLATENAME | string | 0~15（不区分大小写） | `conditional_required` | 无 | 策略模板名（TEMPLATEMODE=PolicyTemplate 时） |

### 5.9 ADD IPSECPOLICY6（IPv6 IPsec策略，28 参数；与 v4 差异：ACL6 系列 + ACLTYPE 必选）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POLICYNAME | string | 1~15 | `required` | 无 | 策略名 |
| SEQUENCENUMBER | int | 1~10000 | `required` | 无 | 序列号 |
| POLICYMODE | enum | Isakmp | `required` | 无 | 策略模式 |
| TEMPLATEMODE | enum | None/PolicyTemplate | `required` | 无 | 模板模式 |
| ACLNUMBER | int | 3000~3999,0 | `conditional_optional`(ACLTYPE=AclIPv4) | 无 | ACL编号（IPv4） |
| ACLNAME | string | 1~32 | `conditional_optional`(ACLTYPE=AclIPv4) | 无 | ACL名称（IPv4） |
| **ACL6NUMBER** | int | 3000~3999,0 | `conditional_optional`(ACLTYPE=AclIPv6) | 无 | ★★ACL编号（IPv6） |
| **ACL6NAME** | string | 0~32 | `conditional_optional`(ACLTYPE=AclIPv6) | 无 | ★★ACL名称（IPv6） |
| **ACLTYPE** | enum | AclIPv4 / AclIPv6 | ★`required` | 无 | ★★ACL类型（v4 为可选默认AclIPv4，v6 必选） |
| TRAFFSADISFLG/SALIFETIMEKB/SALIFETIMESEC/PFS | — | 同 v4 | — | — | SA生命周期/PFS |
| DSCPIN/OUT 系列 | — | 同 v4 | — | — | DSCP |
| ANTIREPLAYENUM/WINDOWSIZE | — | 同 v4 | — | — | 抗重放 |
| DFBITCLEAR/FRAGBEFOREENCR/INSPEEDLIMIT/OUTSPEEDLIMIT/LOGENABLE | — | 同 v4 | — | — | 分片/限速/日志 |
| WORKMODE | enum | Round_robin/Master_standby | `optional` | Round_robin | ★IPv6 不支持 Round_robin，配置后实际以 Master_standby 生效 |
| AUTOSWITCHBACK | enum | Disable/Enable | `conditional_required`(WORKMODE=Master_standby) | 无 | 自动切回 |
| ESN | enum | Disable/Enable | `optional` | Disable | 扩展序列号 |
| TFCENABLE | bool | TRUE/FALSE | `optional` | FALSE | 数据流可信 |

### 5.10 ADD IPSECPOLICYTM（IPsec策略模板，22 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POLICYNAME | string | 1~15 | `required` | 无 | 模板名称 |
| SEQUENCENUMBER | int | 1~10000 | `required` | 无 | 模板序列号 |
| PEERNAME | string | 0~15 | `required` | 无 | IKE对等体名称（直接绑定） |
| IPSECPROPNAME | string | 1~15 | `required` | 无 | IPsec安全提议名称（直接绑定） |
| ACLNAME/ACLNUMBER | — | 同 IPSECPOLICY | `optional` | 无 | ACL（可选） |
| TRAFFSADISFLG/SALIFETIMEKB/SALIFETIMESEC/PFS | — | 同 IPSECPOLICY | — | — | SA生命周期/PFS |
| DSCPIN/OUT 系列 | — | 同 IPSECPOLICY | — | — | DSCP |
| ANTIREPLAYENUM/WINDOWSIZE | — | 同 IPSECPOLICY | — | — | 抗重放 |
| DFBITCLEAR/FRAGBEFOREENCR/INSPEEDLIMIT/OUTSPEEDLIMIT | — | 同 IPSECPOLICY | — | — | 分片/限速 |
| ACLTYPE | enum | AclIPv4/AclIPv6 | `optional` | 无 | ACL类型（当前用户级IPsec仅支持IPv4） |
| ESN/TFCENABLE | — | 同 IPSECPOLICY | — | — | 扩展序列号/TFC |

### 5.11 ADD PROPATTACHIPSECPROPOSAL（策略绑定提议，5 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POLICYNAME | string | 1~15 | `required` | 无 | 策略名 |
| SEQUENCENUMBER | int | 1~10000 | `required` | 无 | 序列号 |
| POLICYMODE | enum | Isakmp | `required` | 无 | 策略模式 |
| TEMPLATEMODE | enum | None/PolicyTemplate | `required` | 无 | 模板模式 |
| IPSECPROPNAME | string | 1~15 | `required` | 无 | IPsec安全提议名称 |

### 5.12 ADD ATTACHIKEPEER（绑定IKE对等体，★6 参数；主备/多Sequence 核心）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| POLICYNAME | string | 1~15 | `required` | 无 | 策略名 |
| SEQUENCENUMBER | int | 1~10000 | `required` | 无 | 序列号 |
| POLICYMODE | enum | Isakmp | `required` | 无 | 策略模式 |
| TEMPLATEMODE | enum | None/PolicyTemplate | `required` | 无 | 模板模式 |
| IKEPEERNAME | string | 1~15 | `required` | 无 | IKE对等体名称 |
| **PEERPRIORITY** | int | 1~3 | `required` | 无 | ★★优先级（主备：主1备2；多Sequence：各sequence均可1） |

### 5.13 ADD IPSECINTFCFGIPSEC（IPsec隧道接口，★4 参数含 SRCIFNAME）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| INTERFACENAME | string | 1~63 | `required` | 无 | 接口名 |
| TNLTYPE | enum | IPSEC（IPv4）/ IPSEC6（IPv6） | `required` | 无 | Tunnel口协议类型 |
| POLICYNAME | string | 1~15（不区分大小写） | `optional` | 无 | 策略名（与 ADD IPSECPOLICY/IPSECPOLICY6 一致） |
| **SRCIFNAME** | string | 1~63 | `optional` | 无 | ★★地址借用接口（仅支持环回口；指定本端接口场景用，作 IKE协商源IP） |

### 5.14 SET IKEGLOBALCONFIG（IKE全局配置，19 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| DFBITCLEAR | bool | TRUE/FALSE | `optional` | 无 | 清除分片标记位 |
| FRAGBEFOREENCR | bool | TRUE/FALSE | `optional` | FALSE | 加密前分片 |
| TRAFFSADISFLG | bool | FALSE/TRUE | `optional` | FALSE | 流量方式触发SA过期标记 |
| TRAFFICSADURTN | int | 8000~200000000（kbyte） | `conditional_required` | 1843200 | 流量SA过期阈值（TRAFFSADISFLG=FALSE 时） |
| TIMESADURTN | int | 480~604800（s） | `optional` | 3600 | 时间SA过期间隔 |
| ANTIREPLFLG | bool | False/True | `optional` | True | 抗重放开关 |
| WINDOWSIZE | enum | Size_32/64/128/256/512/1024 | `conditional_required` | Size_1024 | 抗重放窗口（ANTIREPLFLG=True 时） |
| LOCALNAME | string | 1~255 | `optional` | 无 | 本地名字 |
| DPDTYPE | enum | None / Periodic / Ondemand | `optional` | None | DPD类型 |
| DPDINTERVAL | int | 10~3600（s） | `conditional_required` | 无 | DPD检查间隔（DPDTYPE=Periodic/Ondemand 时） |
| DPDRETRYINTRVL | int | 2~60（s） | `conditional_optional` | 无 | DPD重试间隔 |
| NUMBER | int | 30~1024 | `optional` | 30 | 历史信息记录条数 |
| DOSTHRESHOLD | int | 0~200 | `optional` | 0 | 安全日志阈值 |
| NATKLI | int | 5~300（s） | `optional` | 20 | ★NAT保活间隔（IPSec使能NAT穿越时生效） |
| CPUREPORTTHRES | int | 50~100（%） | `optional` | 无 | CPU过载告警阈值 |
| CPUCLEARTHRES | int | 50~100（%） | `optional` | 无 | CPU过载恢复阈值 |
| UIKECHECKTIME | int | 0~23, 65535 | `optional` | 无 | UIKE主动核查时间（0~23整点；65535关闭） |
| FLOWCTRLSTHRES | int | 50~100（%） | `optional` | 无 | 流控开启CPU阈值 |
| FLOWCTRLRTHRES | int | 50~100（%） | `optional` | 无 | 流控恢复CPU阈值 |

### 5.15 SET FWSOFTPARA（国密开关，5 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PARAMETERSTYPE | enum | DWORD / DWORD_EX | `required` | 无 | 参数类型 |
| DWORDINDEX | int | 1~2048 | `conditional_required` | 无 | DWORD索引（★国密开关=1401；PARAMETERSTYPE=DWORD 时） |
| DWORDVALUE | int | 0~4294967295 | `conditional_required` | 无 | DWORD取值（★国密开=1） |
| EXTENDDWORDINDEX | int | 1~2048 | `conditional_required` | 无 | 扩展DWORD索引（PARAMETERSTYPE=DWORD_EX 时） |
| EXTENDDWORDVALUE | int | 0~4294967295 | `conditional_required` | 无 | 扩展DWORD取值 |

### 5.16 ADD CERTSCENE（证书场景，5 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| SCENENAME | string | 0~192（不区分大小写，最多1空格，不支持中文） | `required` | 无 | 场景名称 |
| SCENETYPE | enum | CA / LOCAL | `required` | 无 | 场景类型（CA证书/本地证书） |
| ENDESCRIPTION | string | 0~192 | `optional` | 无 | 英文描述 |
| CNDESCRIPTION | string | 0~192 | `optional` | 无 | 中文描述 |
| CERTTYPE | enum | NULL / **Cert_sig** / **Cert_enc** | `conditional_optional` | Cert_sig | 证书类型（SCENETYPE=LOCAL 时；签名/加密证书） |

### 5.17 SET PKICRLCHECK（CRL检查，1 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| ISCRLENABLE | bool | TRUE / FALSE | `optional` | FALSE | CRL检查使能 |

### 5.18 ADD GRETUNNEL（GRE隧道，17 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| TNLNAME | string | 1~63（格式 Tunnel+X/Y/Z） | `required` | 无 | 隧道名称 |
| TNLTYPE | enum | gre / gre6 | `required` | 无 | 隧道类型 |
| SRCTYPE | enum | no_type / ip_address / if_name | `conditional_required`(TNLTYPE=gre) | no_type | IPv4源类型 |
| SRCTYPE6 | enum | no_type / ip_address / if_name | `conditional_required`(TNLTYPE=gre6) | no_type | IPv6源类型 |
| SRCIPADDR | IPv4 | IPv4地址 | `conditional_required`(SRCTYPE=ip_address) | 无 | 源IPv4地址 |
| SRCIPV6ADDR | IPv6 | IPv6地址 | `conditional_required`(SRCTYPE6=ip_address) | 无 | 源IPv6地址 |
| SRCIFNAME | string | 1~63 | `conditional_required`(SRCTYPE=if_name) | 无 | 源接口名称（GRE场景常用 LoopBack1） |
| DSTIPADDR | IPv4 | IPv4地址 | `conditional_optional`(TNLTYPE=gre) | 无 | 目的IPv4地址 |
| DSTIPV6ADDR | IPv6 | IPv6地址 | `conditional_optional`(TNLTYPE=gre6) | 无 | 目的IPv6地址 |
| DSTVPNNAME | string | 1~31 | `optional` | 无 | 目的VPN名称 |
| KEEPALVEN | bool | TRUE/FALSE | `optional` | FALSE | 使能Keepalive |
| KEEPALVPERIOD | int | 1~32767（s） | `conditional_optional`(KEEPALVEN=TRUE) | 5 | Keepalive周期 |
| KEEPALVRETRYCNT | int | 1~255 | `conditional_optional`(KEEPALVEN=TRUE) | 3 | 不可达计数 |
| GREKEYEN | bool | TRUE/FALSE | `optional` | FALSE | 使能识别关键字 |
| GREKEY | pwd | 1~268 | `conditional_required`(GREKEYEN=TRUE) | 无 | 识别关键字 |
| CHECKSUMEN | bool | TRUE/FALSE | `optional` | FALSE | 端到端校验 |
| STATENABLE | bool | TRUE/FALSE | `optional` | FALSE | 报文统计 |
| REDUNDANCYEN | bool | TRUE/FALSE | `conditional_optional`(TNLTYPE=gre/gre6) | FALSE | 备份隧道功能 |

### 5.19 ADD L3VPNINSTIPSEC / ADD VPNINSTAFIPSEC / ADD INTERFACEIPSEC / ADD IPBINDVPNIPSEC / ADD IFIPV4ADDRESSIPSEC（IPsec微服务双配简化版）

> **★双配简化说明**：IPsec微服务的 VPN/接口命令相比 VNRS侧大幅简化（L3VPNINSTIPSEC 仅1参数 vs VNRS侧多 VRFDESCRIPTION；VPNINSTAFIPSEC 仅2参数 vs VNRS侧多 VRFRD/策略/标签等9参数）。参数表见 §1.10，此处不重复。

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

### 6.1 IPFD-015004 核心命令（22条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD ACLGROUPIPSEC (01) | ACLGROUPIPSEC | IPv4 ACL规则组 |
| ADD ACLRULEADV4IPSEC (02) | ACLRULEADV4IPSEC | IPv4 高级ACL规则 |
| ADD ACLGROUP6IPSEC (03) | ACLGROUP6IPSEC | IPv6 ACL规则组 |
| ADD ACLRULEADV6IPSEC (04) | ACLRULEADV6IPSEC | IPv6 高级ACL规则 |
| ADD IPSECPROPOSALIPSEC (05) | IPSECPROPOSALIPSEC | IPsec安全提议 |
| ADD IKEPROPOSAL (06) | IKEPROPOSAL | IKE安全提议 |
| ADD IKEPEER (07) | IKEPEER | IPv4 IKE对等体 |
| ADD IKEPEER6 (08) | IKEPEER6 | IPv6 IKE对等体 |
| ADD IPSECPOLICY (09) | IPSECPOLICY | IPv4 IPsec策略 |
| ADD IPSECPOLICY6 (10) | IPSECPOLICY6 | IPv6 IPsec策略 |
| ADD IPSECPOLICYTM (11) | IPSECPOLICYTM | IPsec策略模板 |
| ADD PROPATTACHIPSECPROPOSAL (12) | PROPATTACHIPSECPROPOSAL | 策略↔提议绑定 |
| ADD ATTACHIKEPEER (13) | ATTACHIKEPEER | 策略↔对等体绑定 |
| ADD IPSECINTFCFGIPSEC (14) | IPSECINTFCFGIPSEC | 隧道接口应用策略 |
| SET IKEGLOBALCONFIG (15) | IKEGLOBALCONFIG | IKE全局配置 |
| SET FWSOFTPARA (16) | FWSOFTPARA | 国密开关 |
| ADD CERTSCENE (17) | CERTSCENE | 证书场景 |
| SET PKICRLCHECK (18) | PKICRLCHECK | CRL检查 |
| ADD GRETUNNEL (19) | GRETUNNEL | GRE隧道 |
| ADD L3VPNINSTIPSEC (20) | L3VPNINSTIPSEC | IPsec微服务VPN实例 |
| ADD VPNINSTAFIPSEC (21) | VPNINSTAFIPSEC | IPsec微服务VPN地址族 |
| ADD INTERFACEIPSEC (22) | INTERFACEIPSEC | IPsec微服务接口 |
| ADD IPBINDVPNIPSEC (23) | IPBINDVPNIPSEC | IPsec微服务绑定VPN |
| ADD IFIPV4ADDRESSIPSEC (24) | IFIPV4ADDRESSIPSEC | IPsec微服务IPv4地址 |

### 6.2 前置依赖命令（引用，非本特性拥有，VNRS侧 + 路由）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD L3VPNINST（簇A） | L3VPNINST | VNRS侧 VPN实例（前置依赖） |
| ADD VPNINSTAF（簇A） | VPNINSTAF | VNRS侧 VPN地址族 |
| ADD INTERFACE（簇A） | INTERFACE | VNRS侧 接口 |
| ADD IPBINDVPN（簇A） | IPBINDVPN | VNRS侧 绑定VPN |
| ADD IFIPV4ADDRESS（簇A） | IFIPV4ADDRESS | VNRS侧 IPv4地址 |
| ADD IPSECINTFCFG（VNRS侧） | IPSECINTFCFG(VNRS) | ★VNRS侧创建IPsec隧道接口（仅2参数 INTERFACENAME+TNLTYPE，与 IPsec侧双配） |
| ADD SRROUTE（簇E） | SRROUTE | 静态路由（引流） |
| ADD OSPF/OSPFAREA/OSPFNETWORK/OSPFIMPORTROUTE（簇E） | OSPF 系列 | OSPF over IPsec 场景引流 |

---

## 7. ★CommandRule governs MMLCommand 边表（§11.6 反向）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand / CommandParameter / ConfigObject`（反向：规则治理命令，非命令 has_rule）。

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-015004-01 | CMD-UDG-015004-06.DHGROUP (ADD IKEPROPOSAL) | DHGROUP 不能为 None 或不配置，建议 Dh_group19 |
| CR-015004-02 | CMD-UDG-015004-02/04 (ACLRULEADV4/6IPSEC) 端口参数 | ACL 仅支持源/目的IP，端口配置不生效 |
| CR-015004-03 | OBJ-GRETUNNEL ↔ OBJ-IPSECINTFCFGIPSEC | GRE 与 IPSec 源地址互斥（双隧道编排） |
| CR-015004-04 | CMD-UDG-015004-13.PEERPRIORITY (ADD ATTACHIKEPEER) | 主备 PEERPRIORITY 主1备2；IPv6 不支持 Round_robin |
| CR-015004-05 | CMD-UDG-015004-09/10.SEQUENCENUMBER | 多Sequence 各绑不同 ACL+Peer |
| CR-015004-06 | VNRS微服务 ↔ IPsec微服务 关系 | 双微服务双配一致性（隧道接口/IP/类型/VPN） |
| CR-015004-07 | CMD-UDG-015004-14.SRCIFNAME (ADD IPSECINTFCFGIPSEC) | SRCIFNAME 仅支持环回口 |
| CR-015004-08 | CMD-UDG-015004-16 (SET FWSOFTPARA) + IKEPROPOSAL/IKEPEER 国密参数 | 国密场景必须先开 DWORD 1401 + 算法/认证替换 |

---

## 8. 使用实例脚本（保留手册原文，★13 个激活子场景不合并）

> **★场景差异矩阵核心**：下表汇总 13 场景的命令级差异。脚本仅保留各场景的**差异片段**（非全文），完整脚本见各激活文档。

### 8.0 13 场景差异矩阵（★核心交付物）

| # | 场景 | 文件编号 | ACL命令族 | IKEPEER | IPSECPOLICY | ATTACHIKEPEER | 独有命令/参数 | 引流方式 |
|---|------|---------|-----------|---------|-------------|---------------|--------------|---------|
| 1 | 普通IPv4 | _01_10002 | ACLGROUPIPSEC + ACLRULEADV4IPSEC | IKEPEER (LOWREMOTEADDR=对端TunnelIP) | IPSECPOLICY (ACLNUMBER) | 1次 PEERPRIORITY=1 | —（基准） | SRROUTE 下一跳=Tunnel对端IP |
| 2 | 普通IPv6 | _01_10003 | **ACLGROUP6IPSEC + ACLRULEADV6IPSEC** | **IKEPEER6** (LOWREMOTEADDR=IPv6) | **IPSECPOLICY6** (ACL6NUMBER, ACLTYPE=AclIPv6) | 1次 | IFIPV6ADDRESSIPSEC, SRROUTE6 | SRROUTE6 |
| 3 | IPv4主备 | _01_10004 | 同#1 | IKEPEER ×2 (b主/c备, LOWREMOTEADDR不同) | IPSECPOLICY (**WORKMODE=Master_standby, AUTOSWITCHBACK=Disable**) | ★**2次同SEQUENCE** (PEERPRIORITY=1主/2备) | — | SRROUTE ×2 (下一跳不同) |
| 4 | IPv6主备 | _01_10005 | 同#2 | IKEPEER6 ×2 | IPSECPOLICY6 (WORKMODE/AUTOSWITCHBACK) | 2次同SEQUENCE | — | SRROUTE6 ×2 |
| 5 | GRE over IPsec | _01_10006 | ACLGROUPIPSEC (源/目=LoopBack IP) | IKEPEER (LOWREMOTEADDR=对端LoopBackIP) | IPSECPOLICY | 1次 | ★**ADD GRETUNNEL** (Tunnel1 GRE) + Tunnel2 IPsec 双隧道 | 业务路由→GRE隧道；IPsec加密GRE报文 |
| 6 | OSPF over IPsec | _01_10007 | ACLGROUPIPSEC + ★**2条规则** (rule_1 ACLPROTOCOL=0 IP / rule_2 ACLPROTOCOL=89 OSPF) | IKEPEER (LOWREMOTEADDR=对端LoopBackIP) | IPSECPOLICY | 1次 | ★**ADD OSPF/OSPFAREA/OSPFNETWORK/OSPFIMPORTROUTE** + IPSECINTFCFGIPSEC.**SRCIFNAME=LoopBack1** | OSPF 引流绑 IPSec Tunnel |
| 7 | 多Sequence | _01_10008 | ACLGROUPIPSEC ×2 (3000/3001) | IKEPEER ×2 (b/c) | IPSECPOLICY ×2 (**同POLICYNAME, SEQUENCENUMBER=10/20**, ACLNUMBER=3000/3001) | ★**2次跨SEQUENCE** (各 PEERPRIORITY=1) | — | 单隧道多对端 |
| 8 | 指定本端接口 | _01_10009 | 同#1 | IKEPEER (LOWREMOTEADDR=对端LoopBackIP) | IPSECPOLICY | 1次 | ★**ADD IPSECINTFCFGIPSEC.SRCIFNAME=LoopBack1** + LoopBack双配 | LoopBack IP 路由 |
| 9 | 国密-普通IPv4 | _03728909 | 同#1 | IKEPEER (**CERTLOCALFILE+ENCCERTLOCFILE**, 无PRESHAREDKEY, VERSION1=TRUE/VERSION2=FALSE) | IPSECPOLICY | 1次 | ★**SET FWSOFTPARA(DWORD 1401=1)** + IKEPROPOSAL(**Digital_envelope+SM2/3/4**) + ADD CERTSCENE | 同#1 |
| 10 | 国密-普通IPv6 | _53768408 | 同#2 | IKEPEER6 (证书) | IPSECPOLICY6 | 1次 | 同#9 + IPv6命令族 | 同#2 |
| 11 | 国密-GRE | _53928160 | 同#5 | IKEPEER (证书+EXCHANGEMODE=Main+LOCALIDTYPE=Ip) | IPSECPOLICY | 1次 | 同#9 + ADD GRETUNNEL | 同#5 |
| 12 | 国密-多Sequence | _03408185 | 同#7 | IKEPEER ×2 (证书) | IPSECPOLICY ×2 | 2次跨SEQUENCE | 同#9 | 同#7 |
| 13 | 国密-指定本端接口 | _03567841 | 同#8 (+ACLSTEP/ACLTYPE/ACLMATCHORDER) | IKEPEER (证书) | IPSECPOLICY (+TRAFFSADISFLG) | 1次 | 同#9 + IPSECINTFCFGIPSEC.SRCIFNAME=LoopBack1 | 同#8 |

### 8.1 普通IPv4 IPsec隧道（_01_10002，基准场景，关键片段）

```
//配置高级ACL 3000，允许PCA访问PCB。
ADD ACLGROUPIPSEC:ACLNAME="3000";
ADD ACLRULEADV4IPSEC:ACLNAME="3000",ACLRULENAME="rule_1",ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=0,ACLSOURCEIP="10.1.1.2",ACLSRCWILD="0.0.0.0",ACLDESTIP="10.1.2.2",ACLDESTWILD="0.0.0.0";

//配置IPsec安全提议。
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="tran1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;

//配置IKE安全提议（DHGROUP 不能为 None）。
ADD IKEPROPOSAL:PROPOSALNUMBER=10,AUTHMETHOD=Pre_share,AUTHALGORITHM=Sha2_256,DHGROUP=Dh_group19;

//配置IKE peer（NAT穿越）。
ADD IKEPEER:PEERNAME="b",PRESHAREDKEY="abcde",NATTRAVERSAL=TRUE,PROPOSAL=10,LOWREMOTEADDR="192.168.1.2",INVRFNAME="vrf1",OUTVRFNAME="vrf1";

//配置IPsec安全策略 + 绑定提议 + 绑定IKE Peer。
ADD IPSECPOLICY:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3000;
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="tran1";
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="b",PEERPRIORITY=1;

//应用安全策略。
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC,POLICYNAME="map1";

//DPD（可选）。
SET IKEGLOBALCONFIG:DPDINTERVAL=10,DPDTYPE=Periodic,DPDRETRYINTRVL=3,NATKLI=30;
```

### 8.2 IPv4 IPsec 主备隧道（_01_10004，★差异：WORKMODE + 多 PEERPRIORITY）

```
//配置2个IKE peer（b主/c备）。
ADD IKEPEER:PEERNAME="b",PRESHAREDKEY="abcde",PROPOSAL=10,LOWREMOTEADDR="192.168.1.2",INVRFNAME="vrf1",OUTVRFNAME="vrf1";
ADD IKEPEER:PEERNAME="c",PRESHAREDKEY="abcde",PROPOSAL=10,LOWREMOTEADDR="192.168.1.3",INVRFNAME="vrf1",OUTVRFNAME="vrf1";

//配置IPsec安全策略（主备模式）。
ADD IPSECPOLICY:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3000,WORKMODE=Master_standby,AUTOSWITCHBACK=Disable;

//绑定2个IKE Peer（同SEQUENCE，主1备2）。
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="tran1";
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="b",PEERPRIORITY=1;
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="c",PEERPRIORITY=2;
```

### 8.3 多Sequence IPsec策略（_01_10008，★差异：同 POLICYNAME 多 SEQUENCENUMBER）

```
//配置2个ACL组（3000对端B / 3001对端C）。
ADD ACLGROUPIPSEC:ACLNAME="3000";
ADD ACLRULEADV4IPSEC:ACLNAME="3000",ACLRULENAME="rule_1",...,ACLDESTIP="10.1.2.0",ACLDESTWILD="0.0.0.255";
ADD ACLGROUPIPSEC:ACLNAME="3001";
ADD ACLRULEADV4IPSEC:ACLNAME="3001",ACLRULENAME="rule_1",...,ACLDESTIP="10.1.3.0",ACLDESTWILD="0.0.0.255";

//配置2个IKE peer。
ADD IKEPEER:PEERNAME="b",...,LOWREMOTEADDR="192.168.1.2";
ADD IKEPEER:PEERNAME="c",...,LOWREMOTEADDR="192.168.1.3";

//配置IPsec安全策略（同POLICYNAME=map1，SEQUENCENUMBER=10/20）。
ADD IPSECPOLICY:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3000;
ADD IPSECPOLICY:POLICYNAME="map1",SEQUENCENUMBER=20,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3001;

//绑定（各sequence绑不同peer，PEERPRIORITY均可=1）。
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="map1",SEQUENCENUMBER=10,...,IPSECPROPNAME="tran1";
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="map1",SEQUENCENUMBER=20,...,IPSECPROPNAME="tran1";
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=10,...,IKEPEERNAME="b",PEERPRIORITY=1;
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=20,...,IKEPEERNAME="c",PEERPRIORITY=1;
```

### 8.4 指定本端接口建立 IPsec 隧道（_01_10009，★差异：SRCIFNAME）

```
//创建并配置LoopBack接口（VNRS+IPsec双配）。
ADD INTERFACE:IFNAME="LoopBack1",IFADMINSTATUS=up;
ADD IPBINDVPN:IFNAME="LoopBack1",VRFNAME="vrf1";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.102.105.223",SUBNETMASK="255.255.255.255";
ADD INTERFACEIPSEC:IFNAME="LoopBack1",IFADMINSTATUS=Up;
ADD IPBINDVPNIPSEC:IFNAME="LoopBack1",VRFNAME="vrf1";
ADD IFIPV4ADDRESSIPSEC:IFNAME="LoopBack1",IFIPADDR="10.102.105.223",SUBNETMASK="255.255.255.255";

//IKE peer 远程地址配对端 LoopBack IP。
ADD IKEPEER:PEERNAME="b",...,LOWREMOTEADDR="10.102.105.224",...;

//应用策略时指定本端源接口（★SRCIFNAME）。
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC,POLICYNAME="policy1",SRCIFNAME="LoopBack1";
```

### 8.5 GRE over IPsec（_01_10006，★差异：双隧道编排）

```
//创建GRE本端源接口。
ADD INTERFACE:IFNAME="LoopBack1",IFADMINSTATUS=up;
ADD IPBINDVPN:IFNAME="LoopBack1",VRFNAME="vrf1";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.102.105.223",SUBNETMASK="255.255.255.255";

//配置GRE隧道（Tunnel1，承载组播/广播业务）。
ADD GRETUNNEL:TNLNAME="Tunnel1",TNLTYPE=gre,SRCTYPE=if_name,SRCIFNAME="LoopBack1",DSTIPADDR="10.102.105.224";
ADD IPBINDVPN:IFNAME="Tunnel1",VRFNAME="vrf1";
ADD IFIPV4ADDRESS:IFNAME="Tunnel1",IFIPADDR="192.168.1.1",SUBNETMASK="255.255.255.255";

//配置IPsec隧道（Tunnel2，加密GRE报文）。ACL匹配 LoopBack 间流量。
ADD ACLGROUPIPSEC:ACLNAME="3000";
ADD ACLRULEADV4IPSEC:ACLNAME="3000",...,ACLSOURCEIP="10.102.105.223",ACLDESTIP="10.102.105.224",...;
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC,POLICYNAME="map1";

//业务路由指向GRE隧道（IFNAME=Tunnel1）。
ADD SRROUTE:...,IFNAME="Tunnel1";
```

### 8.6 国密 IPsec 支持 IKEv1（_03728909，★差异：国密算法+证书认证）

```
//★★国密开关（所有国密配置前必须执行）。
SET FWSOFTPARA:PARAMETERSTYPE=DWORD,DWORDINDEX=1401,DWORDVALUE=1;

//配置IKE安全提议（国密算法）。
ADD IKEPROPOSAL:PROPOSALNUMBER=10,AUTHMETHOD=Digital_envelope,ENCRALGORITHM=Sm4,INTEGALGORITHM=Sm3,ASYMENCRALG=Sm2,DHGROUP=Dh_group19;

//配置证书场景（CA + LOCAL签名/加密）。
ADD CERTSCENE:SCENENAME="ca_scene",SCENETYPE=CA;
ADD CERTSCENE:SCENENAME="sig_scene",SCENETYPE=LOCAL,CERTTYPE=Cert_sig;
ADD CERTSCENE:SCENENAME="enc_scene",SCENETYPE=LOCAL,CERTTYPE=Cert_enc;

//配置IKE peer（证书认证，无PRESHAREDKEY，强制IKEv1）。
ADD IKEPEER:PEERNAME="b",CERTLOCALFILE="sm2_c_sig.cer",ENCCERTLOCFILE="sm2_c_enc.cer",CERTSCENARIO="sig_scene",ENCCERTSCENARIO="enc_scene",VERSION1=TRUE,VERSION2=FALSE,PROPOSAL=10,LOWREMOTEADDR="192.168.1.2",...;

//（后续IPSECPOLICY/绑定/应用同普通场景，算法由提议决定）。
```

### 8.7 IPv6 IPsec 隧道（_01_10003，★差异：IPv6 命令族）

```
//IPv6 ACL。
ADD ACLGROUP6IPSEC:ACLNAME="3000";
ADD ACLRULEADV6IPSEC:ACLNAME="3000",ACLRULENAME="rule_1",ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=58,ACLSOURCEIP="2001:db8:1::2",ACLSRCWILD=128,ACLDESTIP="2001:db8:2::2",ACLDESTWILD=128;

//IPv6 IKE peer。
ADD IKEPEER6:PEERNAME="b",PRESHAREDKEY="abcde",PROPOSAL=10,LOWREMOTEADDR="2001:db8:1::1",...;

//IPv6 IPsec策略。
ADD IPSECPOLICY6:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLTYPE=AclIPv6,ACL6NUMBER=3000;
```

---

## 9. 抽取核对清单

### 9.1 配置类命令参数行数与来源手册路径

| 命令 | 参数行数 | 来源手册路径（相对 `output/UDG_Product_Documentation_CH_20.15.2/`） |
|------|---------|----------------------------------------------------------------|
| ADD ACLGROUPIPSEC | 5 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md` |
| ADD ACLRULEADV4IPSEC | 25 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md` |
| ADD ACLGROUP6IPSEC | 5 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md` |
| ADD ACLRULEADV6IPSEC | 25 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md` |
| ADD IPSECPROPOSALIPSEC | 6 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md` |
| ADD IKEPROPOSAL | 11 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md` |
| ADD IKEPEER | 21 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md` |
| ADD IKEPEER6 | 20 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md` |
| ADD IPSECPOLICY | 27 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md` |
| ADD IPSECPOLICY6 | 28 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md` |
| ADD IPSECPOLICYTM | 22 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略模板/增加IPsec策略模板（ADD IPSECPOLICYTM）_96044554.md` |
| ADD PROPATTACHIPSECPROPOSAL | 5 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md` |
| ADD ATTACHIKEPEER | 6 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md` |
| ADD IPSECINTFCFGIPSEC | 4 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md` |
| SET IKEGLOBALCONFIG | 19 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md` |
| SET FWSOFTPARA | 5 | `OM参考/命令/UDG MML命令/平台服务管理/操作维护/软参配置管理/设置ServiceFabric软参（SET FWSOFTPARA）_18818231.md` |
| ADD CERTSCENE | 5 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/公钥基础设施/PKI场景/增加证书场景（ADD CERTSCENE）_25912241.md` |
| SET PKICRLCHECK | 1 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/公钥基础设施/使能CRL检查/设置CRL检查（SET PKICRLCHECK）_41702627.md` |
| ADD GRETUNNEL | 17 | `OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md` |
| ADD L3VPNINSTIPSEC | 1 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例配置命令/增加L3VPN实例（ADD L3VPNINSTIPSEC）_25830689.md` |
| ADD VPNINSTAFIPSEC | 2 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/VPN管理/L3VPN管理/VPN实例地址族配置命令/增加L3VPN实例地址族（ADD VPNINSTAFIPSEC）_26032191.md` |
| ADD INTERFACEIPSEC | 8 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACEIPSEC）_26150749.md` |
| ADD IPBINDVPNIPSEC | 7 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/绑定VPN/增加接口绑定VPN（ADD IPBINDVPNIPSEC）_80751060.md` |
| ADD IFIPV4ADDRESSIPSEC | 4 | `OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESSIPSEC）_80432522.md` |
| ADD IPSECINTFCFG (VNRS侧) | 2 | `OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/创建IPsec隧道接口（ADD IPSECINTFCFG）_50281406.md` |
| **合计** | **255 参数行** | 25 命令全部手册定位成功 |

### 9.2 ⚠️手册未定位列表

| 命令 | 状态 | 原因 |
|------|------|------|
| `ADD IFIPV6ADDRESSIPSEC`（IPsec微服务IPv6地址） | ⚠️手册未定位 | IPv6场景激活文档引用，但手册未在本特性文档树中定位（参照 IFIPV4ADDRESSIPSEC 结构推断参数 IFNAME/IPV6ADDR/PREFIXLEN，需复核） |

> **说明**：除 ADD IFIPV6ADDRESSIPSEC 外，本特性涉及的全部配置命令手册均已定位（25 命令）。查询/调测类（DSP/LST/RTR/RST）12+ 命令本期略不抽参数。

### 9.3 ★8 普通场景 + 5 国密场景差异矩阵（与原 04 合并版的对比）

| 场景维度 | 原 04（合并为1通用流） | 本 draft（13 场景不合并） | 影响 |
|---------|----------------------|--------------------------|------|
| **主备隧道** | ★丢失：未区分 WORKMODE=Master_standby / AUTOSWITCHBACK / 多 PEERPRIORITY(主1备2) | ★补齐：§8.0 矩阵第3/4行 + §5.8 WORKMODE/AUTOSWITCHBACK 全参数 + CR-015004-04 | 主备切换逻辑可建模 |
| **多Sequence** | ★丢失：未体现同 POLICYNAME 下多 SEQUENCENUMBER 各绑不同 ACL+Peer | ★补齐：§8.0 矩阵第7行 + §8.3 脚本 + CR-015004-05 | 单隧道多对端可建模 |
| **GRE over IPsec** | ★丢失：未体现双隧道编排(Tunnel1 GRE + Tunnel2 IPsec) | ★补齐：§8.0 矩阵第5行 + §8.5 脚本 + ADD GRETUNNEL 17参数 + CR-015004-03 | GRE+IPSec 编排可建模 |
| **OSPF over IPsec** | ★丢失：未体现 OSPF 引流 + ACL双规则(IP/OSPF协议) + SRCIFNAME | ★补齐：§8.0 矩阵第6行 + ACLPROTOCOL=0/89 双规则 + OSPF命令族引用 | OSPF 引流可建模 |
| **指定本端接口** | ★丢失：未体现 SRCIFNAME=LoopBack 作 IKE源 + LoopBack双配 | ★补齐：§8.0 矩阵第8行 + §8.4 脚本 + ADD IPSECINTFCFGIPSEC.SRCIFNAME + CR-015004-07 | 借用接口可建模 |
| **IPv6 命令族** | ★部分丢失：未区分 IKEPEER6/IPSECPOLICY6/ACLGROUP6IPSEC 独立命令 + ACLSRCWILD 正掩码语义 | ★补齐：§1 独立登记 4 个 IPv6 命令 + §5.3/5.7/5.9 全参数 + 正掩码 vs 反掩码差异标注 | IPv6 场景完整建模 |
| **国密 IKEv1** | ★★完全丢失：未建任何国密场景 | ★补齐：§1.8 国密独有命令族(4) + §5.5/5.6 国密参数(SM2/SM3/SM4/Digital_envelope/CERTLOCALFILE) + §8.6 脚本 + CR-015004-08 + 5 国密场景矩阵(第9-13行) | ★★国密场景从0到1建立 |
| **双微服务双配** | ★丢失：未体现 VNRS侧 vs IPsec侧 命令对称简化 | ★补齐：§1.10 IPsec微服务双配命令族(6) + §0.1 双配说明 + CR-015004-06 | 双配一致性可建模 |

### 9.4 抽取统计

| 维度 | 数量 |
|------|------|
| 配置类命令（手册定位成功） | 25（IPSec核心14 + 国密4 + GRE 1 + IPsec微服务双配6） |
| 配置类命令参数总行数 | 255 |
| 查询/调测类命令（本期略） | 12+（DSP/LST/RTR/RST 系列） |
| ⚠️手册未定位命令 | 1（ADD IFIPV6ADDRESSIPSEC） |
| ConfigObject | 25 |
| CommandRule | 8 |
| ConfigObject 关系边 | 20（contains 3 + refers_to 8 + depends_on 6 + activates 3） |
| operates_on 边 | 24（核心）+ 8（前置依赖引用） |
| 激活子场景脚本 | **13**（8 普通 + 5 国密，含 GRE/多Sequence/指定本端接口 在普通与国密下各一份） |
| 国密独有命令族 | 4（SET FWSOFTPARA / ADD CERTSCENE / SET PKICRLCHECK / DSP PKICERTLIST） |
| IPv6 独有命令族 | 4（ADD ACLGROUP6IPSEC / ACLRULEADV6IPSEC / IKEPEER6 / IPSECPOLICY6） |

---

> 本文件为 IPFD-015004 IPSec功能（UDG）命令层抽取，**13 场景不合并**，严格对齐 `04-cluster-B-GWFD-010105.md` 9 节样板。
> **★关键贡献**：①补齐 8 普通场景差异（主备 WORKMODE/多Sequence/GRE双隧道/OSPF引流/指定本端接口 SRCIFNAME/IPv6命令族）；②★国密场景从0建立（4 独有命令 + SM2/SM3/SM4/Digital_envelope 算法替换 + 证书认证 + DWORD 1401 开关）；③纠正 IPv6 ACLSRCWILD 正掩码语义（与 v4 反掩码相反）；④建立 IPsec微服务双配命令族（VNRS侧简化版）；⑤建立 8 条特性级 CommandRule（DH组非None/ACL仅源目/GRE-IPSec源互斥/主备PEERPRIORITY/多Sequence/双配一致/SRCIFNAME仅环回/国密开关前置）。
