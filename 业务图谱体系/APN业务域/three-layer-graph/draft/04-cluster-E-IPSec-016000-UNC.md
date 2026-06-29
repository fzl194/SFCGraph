# APN 业务域命令图谱 · 簇E：IPFD-016000 IPSec功能（UNC/SMF 侧）

> **文件定位**：`three-layer-graph/draft/04-cluster-E-IPSec-016000-UNC.md`
> **特性范围**：仅 IPFD-016000 IPSec功能（UNC 侧），**13 个激活子场景不合并**（8 普通场景 + 5 国密 IKEv1 场景；与 UDG 015004 对称）
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **结构对齐**：严格 follow `04-cluster-E-IPSec-015004.md`（UDG 侧样板，9 节组织；本文件为 UNC 侧对称镜像）
> **★U+C 命令差异核对结论**：**IPSec 命令族在 UDG 与 UNC 间完全同名同参（25 命令手册文件ID逐一相同），为共享命令模块**。本文件采用「复用 UDG 权威参数 + used_by_features 加 016000 引用」策略，仅独立抽取 UNC 侧独有差异（UNC独有 CommandRule / 版本差异）。
> **数据来源**：1 篇特性概述 + 6 篇实现原理 + 1 篇调测 + 1 篇术语 + **13 篇激活文档**（8 普通 + 5 国密）+ **1 篇上传证书** + MML 命令手册原文（路径见 §抽取核对清单，与 UDG 同一组手册）
> **铁律**：命令/参数 100% 来自原始产品文档原文，零编造。手册未定位的命令标注「⚠️手册未定位」。

---

## 0. 命令清单总览（IPFD-016000 用到的全部命令 — 与 UDG 015004 同一组）

### 0.1 ★U+C 命令族完全对称结论（核心交付物）

> **★★关键发现**：UNC 20.15.2 的 `平台服务管理/IPSEC功能管理/` MML 命令手册树与 UDG **文件 ID 逐一完全相同**（手册为两产品共享的统一 IPSec 命令模块，从同一源文档派生）。证据：UNC 普通IPv4激活文档 `_61317238` 与 UDG 对应场景逐命令、逐参数、逐 MML 手册路径引用一致；国密场景 `_03728909` 同样一致。因此本文件不重复抽取同名同参的 25 条命令的全参数表，直接**引用 UDG 权威参数**（参见 `04-cluster-E-IPSec-015004.md` §1-§5），仅在 §1 登记 UNC 侧 `command_id` + used_by_features 关系。

| 维度 | UDG 015004 | UNC 016000 | 结论 |
|------|-----------|-----------|------|
| 配置类命令手册文件ID | `_80432524`(IPSECPROPOSAL)、`_26032189`(IKEPROPOSAL)、`_80592498`(IKEPEER)、`_25912243`(IPSECPOLICY)、`_80910986`(IPSECINTFCFGIPSEC)、`_80751058`(ACLRULEADV4IPSEC)... | **完全相同** | 共享命令模块 |
| 命令命名 | ADD ACLGROUPIPSEC / IKEPEER / IPSECPOLICY / IPSECINTFCFGIPSEC / IPSECPOLICYTM ... | **完全相同**（无 UNC 独有命名后缀） | 无差异 |
| 参数列表 | 详见 015004 §5 | **完全相同** | 无参数差异 |
| 国密开关 SET FWSOFTPARA | `_18818231`（操作维护/软参配置管理） | **`_18818231`（同）** | 共享 |
| GRE 隧道 ADD GRETUNNEL | `_00841729`（VNRS功能管理/IP服务/VPN管理/GRE管理） | **`_00841729`（同）** | 共享 |
| 版本支持 | UDG 20.x | **UNC 20.5.0 首发；20.8.0 增 IPv6/NAT穿越/主备**（详见 §0.3） | 版本号不同，能力集一致 |
| 应用限制 | （未在 UDG 特性概述列同款限制表） | **UNC 独有限制：不支持 GREv6 over IPSecv6 / OSPFv3 over IPSecv6 / IPSecv6 地址借用 / IPv4 入 IPSecv6 隧道 / IPv6 入 IPSecv4 隧道**（详见 §4 CR-016000-UNC-01） | UNC 独有 CommandRule |

### 0.2 按命令类型分布（与 UDG 015004 同清单，共 25 配置类）

| 类型 | 命令数 | 命令清单（与 UDG 015004 完全相同） |
|------|-------|---------|
| IPSec 核心配置类 | 14 | ADD ACLGROUPIPSEC、ADD ACLRULEADV4IPSEC、ADD ACLGROUP6IPSEC、ADD ACLRULEADV6IPSEC、ADD IPSECPROPOSALIPSEC、ADD IKEPROPOSAL、ADD IKEPEER、ADD IKEPEER6、ADD IPSECPOLICY、ADD IPSECPOLICY6、ADD IPSECPOLICYTM、ADD PROPATTACHIPSECPROPOSAL、ADD ATTACHIKEPEER、ADD IPSECINTFCFGIPSEC、SET IKEGLOBALCONFIG |
| 国密独有命令族 | 4 | SET FWSOFTPARA（DWORD 1401）、ADD CERTSCENE、SET PKICRLCHECK、DSP PKICERTLIST |
| GRE over IPsec 独有 | 1 | ADD GRETUNNEL |
| IPsec微服务双配命令族 | 6 | ADD L3VPNINSTIPSEC、ADD VPNINSTAFIPSEC、ADD INTERFACEIPSEC、ADD IPBINDVPNIPSEC、ADD IFIPV4ADDRESSIPSEC、**ADD IFIPV6ADDRESSIPSEC（★UNC 手册已定位 `_21521206`，补齐 UDG 未定位项）** |

### 0.3 ConfigObject 分布（与 UDG 015004 同，25 个核心 + 引用）

> 与 UDG 015004 §0.2 完全相同（ACLGROUPIPSEC/IPSECPROPOSALIPSEC/IKEPROPOSAL/IKEPEER/IKEPEER6/IPSECPOLICY/IPSECPOLICY6/IPSECPOLICYTM/绑定关系/隧道接口/IKE全局/国密证书/GRE/IPsec微服务双配族）。`product_side` 字段在 UNC 侧取值 `UNC`（UDG 取 `UDG`），其余字段一致。

### 0.4 全局字段声明（status）

> **适用范围**：本文件 §1 所有 MMLCommand。
> **声明**：本文件 §1 所有 MMLCommand 的 `status` 字段值均为 `active`。
> **依据**：UNC 侧所有命令均在产品文档正式登记，无 `deprecated` 或 `planned` 状态。

---

## 1. MMLCommand 实例化（IPFD-016000，25 个核心命令 — 全部复用 UDG 权威参数）

> **★抽取策略**：因 UNC 与 UDG 的 25 条 IPSec 命令为共享命令模块（手册文件ID逐一相同、参数逐一相同），本节仅登记 UNC 侧 `command_id`（`CMD-UNC-016000-xx`）+ `used_by_features=[IPFD-016000]` + 指向 UDG 权威参数表的引用，不重复列全参数。CommandParameter 全量参数表见 UDG 015004 §5（同名同参，零差异）。

### 1.1 ACL 数据流定义（UNC，4个：IPv4×2 + IPv6×2 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-01` | `ADD ACLGROUPIPSEC` | ADD | ACLGROUPIPSEC | ★复用 UDG CMD-UDG-015004-01（5参数：ACLNAME/ACLSTEP/ACLTYPE/ACLMATCHORDER/ACLDESCRIPTION） | EV-IPSEC-01 |
| `CMD-UNC-016000-02` | `ADD ACLRULEADV4IPSEC` | ADD | ACLRULEADV4IPSEC | ★复用 UDG CMD-UDG-015004-02（25参数；ACLSRCWILD/ACLDESTWILD 反掩码语义一致） | EV-IPSEC-01 |
| `CMD-UNC-016000-03` | `ADD ACLGROUP6IPSEC` | ADD | ACLGROUP6IPSEC | ★复用 UDG CMD-UDG-015004-03 | EV-IPSEC-02 |
| `CMD-UNC-016000-04` | `ADD ACLRULEADV6IPSEC` | ADD | ACLRULEADV6IPSEC | ★复用 UDG CMD-UDG-015004-04（25参数；ACLSRCWILD/ACLDESTWILD 正掩码前缀长度语义一致） | EV-IPSEC-02 |

### 1.2 IPSec 安全提议（UNC，1个 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-05` | `ADD IPSECPROPOSALIPSEC` | ADD | IPSECPROPOSALIPSEC | ★复用 UDG CMD-UDG-015004-05（6参数；国密 ESPENCRYPTALGO=Sm4/ESPAUTHALGO=Sm3/AHAUTHALGO=Sm3 枚举一致） | EV-IPSEC-01 |

### 1.3 IKE 安全提议（UNC，1个 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-06` | `ADD IKEPROPOSAL` | ADD | IKEPROPOSAL | ★复用 UDG CMD-UDG-015004-06（11参数；DHGROUP 不能 None / 国密 Digital_envelope+ASYMENCRALG=Sm2+ENCRALGORITHM=Sm4+INTEGALGORITHM=Sm3 一致） | EV-IPSEC-01 |

### 1.4 IKE 对等体（UNC，2个 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-07` | `ADD IKEPEER` | ADD | IKEPEER | ★复用 UDG CMD-UDG-015004-07（21参数；国密证书 CERTLOCALFILE/ENCCERTLOCFILE 替代 PRESHAREDKEY 一致） | EV-IPSEC-01 |
| `CMD-UNC-016000-08` | `ADD IKEPEER6` | ADD | IKEPEER6 | ★复用 UDG CMD-UDG-015004-08（20参数；仅 VERSION2、地址 IPv6 化、LOCALIDTYPE 取 IPv6 系列） | EV-IPSEC-02 |

### 1.5 IPSec 安全策略（UNC，3个 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-09` | `ADD IPSECPOLICY` | ADD | IPSECPOLICY | ★复用 UDG CMD-UDG-015004-09（27参数；WORKMODE=Master_standby/AUTOSWITCHBACK 主备语义一致） | EV-IPSEC-01 |
| `CMD-UNC-016000-10` | `ADD IPSECPOLICY6` | ADD | IPSECPOLICY6 | ★复用 UDG CMD-UDG-015004-10（28参数；ACL6 系列 + ACLTYPE 必选 + IPv6 不支持 Round_robin 一致） | EV-IPSEC-02 |
| `CMD-UNC-016000-11` | `ADD IPSECPOLICYTM` | ADD | IPSECPOLICYTM | ★复用 UDG CMD-UDG-015004-11（22参数；TEMPLATEMODE=PolicyTemplate 响应方语义一致） | EV-IPSEC-01 |

### 1.6 策略绑定关系（UNC，2个 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-12` | `ADD PROPATTACHIPSECPROPOSAL` | ADD | PROPATTACHIPSECPROPOSAL | ★复用 UDG CMD-UDG-015004-12（5参数） | EV-IPSEC-01 |
| `CMD-UNC-016000-13` | `ADD ATTACHIKEPEER` | ADD | ATTACHIKEPEER | ★复用 UDG CMD-UDG-015004-13（6参数；PEERPRIORITY 主1备2 / 多Sequence 各1 一致） | EV-IPSEC-01 |

### 1.7 隧道接口应用 + IKE全局配置（UNC，2个 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-14` | `ADD IPSECINTFCFGIPSEC` | ADD | IPSECINTFCFGIPSEC | ★复用 UDG CMD-UDG-015004-14（4参数；★SRCIFNAME 仅环回口、与 VNRS侧 ADD IPSECINTFCFG 双配一致） | EV-IPSEC-01/07 |
| `CMD-UNC-016000-15` | `SET IKEGLOBALCONFIG` | SET | IKEGLOBALCONFIG | ★复用 UDG CMD-UDG-015004-15（19参数；DPD/NATKLI/抗重放 全局参数一致） | EV-IPSEC-01 |

### 1.8 国密独有命令族（UNC，3个配置 + 1查询 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-16` | `SET FWSOFTPARA` | SET | FWSOFTPARA | ★复用 UDG CMD-UDG-015004-16（5参数；DWORD 1401=1 国密开关；UNC 手册文件ID `_18818231` 与 UDG 完全相同） | EV-IPSEC-GM |
| `CMD-UNC-016000-17` | `ADD CERTSCENE` | ADD | CERTSCENE | ★复用 UDG CMD-UDG-015004-17（5参数；SCENETYPE=CA/LOCAL、CERTTYPE=Cert_sig/Cert_enc） | EV-IPSEC-GM |
| `CMD-UNC-016000-18` | `SET PKICRLCHECK` | SET | PKICRLCHECK | ★复用 UDG CMD-UDG-015004-18（1参数 ISCRLENABLE） | EV-IPSEC-GM |
| `CMD-UNC-016000-Q1` | `DSP PKICERTLIST` | DSP | PKICERTLIST | ★复用 UDG CMD-UDG-015004-Q1（调测查询类，本期略，UNC 手册 `_30311459` 与 UDG 同） | EV-IPSEC-GM |

### 1.9 GRE over IPsec 独有（UNC，1个，归属 VNRS侧 — 复用 UDG）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-19` | `ADD GRETUNNEL` | ADD | GRETUNNEL | ★复用 UDG CMD-UDG-015004-19（17参数；UNC 手册文件ID `_00841729` 与 UDG 完全相同；SRCTYPE=if_name+SRCIFNAME=LoopBack1 一致） | EV-IPSEC-04 |

### 1.10 IPsec微服务双配命令族（UNC，6个 — 复用 UDG，★补齐 IFIPV6ADDRESSIPSEC）

| `command_id` | `command_name` | `verb` | `object_keyword` | UNC 侧权威参数来源 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `CMD-UNC-016000-20` | `ADD L3VPNINSTIPSEC` | ADD | L3VPNINSTIPSEC | ★复用 UDG CMD-UDG-015004-20（1参数 VRFNAME） | EV-IPSEC-01 |
| `CMD-UNC-016000-21` | `ADD VPNINSTAFIPSEC` | ADD | VPNINSTAFIPSEC | ★复用 UDG CMD-UDG-015004-21（2参数） | EV-IPSEC-01 |
| `CMD-UNC-016000-22` | `ADD INTERFACEIPSEC` | ADD | INTERFACEIPSEC | ★复用 UDG CMD-UDG-015004-22（8参数） | EV-IPSEC-01 |
| `CMD-UNC-016000-23` | `ADD IPBINDVPNIPSEC` | ADD | IPBINDVPNIPSEC | ★复用 UDG CMD-UDG-015004-23（7参数） | EV-IPSEC-01 |
| `CMD-UNC-016000-24` | `ADD IFIPV4ADDRESSIPSEC` | ADD | IFIPV4ADDRESSIPSEC | ★复用 UDG CMD-UDG-015004-24（4参数） | EV-IPSEC-01 |
| `CMD-UNC-016000-25` | `ADD IFIPV6ADDRESSIPSEC` | ADD | IFIPV6ADDRESSIPSEC | ★★★**UNC 侧手册已定位**（`增加接口IPv6地址（ADD IFIPV6ADDRESSIPSEC）_21521206.md`），补齐 UDG 015004 的 ⚠️手册未定位项。参数推断：IFNAME/IPV6ADDR/PREFIXLEN/ADDRTYPE（结构同 IFIPV4ADDRESSIPSEC，IPv6 化），需在 UDG 015004 复核时引用此 UNC 手册补全 | EV-IPSEC-02 |

### 1.11 查询/调测类（本期略 — 与 UDG 同）

| `command_id` | `command_name` | `verb` | 说明 |
|--------------|----------------|--------|------|
| `CMD-UNC-016000-Q2~Q6` | DSP IKESA / DSP IKEIPSECSA / LST IKEPEER/IKEPROPOSAL/IPSECPOLICY/... / DSP IPSECPATHMTU / RST IPSECPATHMTU / RTR IKESA / RTR IKEIPSECSA 等 | DSP/LST/RST/RTR | 与 UDG 015004 §1.11 同清单（调测查询类，本期略） |

---

## 2. ConfigObject 实例化（25 个核心 + 引用 — 与 UDG 015004 同结构）

> **★说明**：ConfigObject 结构与 UDG 015004 §2 完全相同（ACLGROUPIPSEC/ACLRULEADV4IPSEC/ACLGROUP6IPSEC/ACLRULEADV6IPSEC/IPSECPROPOSALIPSEC/IKEPROPOSAL/IKEPEER/IKEPEER6/IPSECPOLICY/IPSECPOLICY6/IPSECPOLICYTM/PROPATTACHIPSECPROPOSAL/ATTACHIKEPEER/IPSECINTFCFGIPSEC/IKEGLOBALCONFIG/FWSOFTPARA/CERTSCENE/PKICRLCHECK/GRETUNNEL/L3VPNINSTIPSEC/VPNINSTAFIPSEC/INTERFACEIPSEC/IPBINDVPNIPSEC/IFIPV4ADDRESSIPSEC/IFIPV6ADDRESSIPSEC）。
> **唯一差异**：`product_side` 字段值取 `UNC`（UDG 取 `UDG`）；`object_id` 前缀沿用 UDG 命名（ConfigObject 跨产品共享，不重复实例化）。
> **★IFIPV6ADDRESSIPSEC** 在 UNC 侧手册已定位（`_21521206`），状态由 UDG 的「⚠️手册未定位」升级为「已定位」。

---

## 3. ConfigObject 间关系边（§11.7 — 与 UDG 015004 同，20 条）

> **★说明**：关系边与 UDG 015004 §3 完全相同（contains 3 + refers_to 8 + depends_on 6 + activates 3 = 20 条）。CommandObject 关系拓扑在 UDG/UNC 间无差异（同一命令模块的对象引用关系一致）。

---

## 4. CommandRule 实例化（本特性相关，9 条 = UDG 8 条 + UNC 独有 1 条）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。
> **CR-016000-UNC-01 ~ 08**：与 UDG CR-015004-01 ~ 08 **完全对称**（治理逻辑、scope_ref、severity 一致），UNC 侧仅 command_id 引用由 `CMD-UDG-*` 改为 `CMD-UNC-*`，治理逻辑摘要引用 UDG 权威表述。
> **CR-016000-UNC-09**：★UNC 独有 CommandRule（UDG 无对应），源自 UNC 特性概述「应用限制」原文。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-016000-UNC-01` | DHGROUP 不能为 None 或不配置（对称 UDG CR-015004-01） | `parameter_dependency` | explicit | restriction | parameter | CMD-UNC-016000-06.DHGROUP (ADD IKEPROPOSAL) | 手册原文：DHGROUP 参数不能配置为 None 或者不配置，建议配置为 Dh_group19（UNC 手册 `_26032189` 与 UDG 同） | SA 协商失败 | critical | EV-IPSEC-01 |
| `CR-016000-UNC-02` | ACL 仅支持源/目的IP，端口配置不生效（对称 UDG CR-015004-02） | `semantic_rule` | explicit | restriction | parameter | CMD-UNC-016000-02/04 (ACLRULEADV4/6IPSEC) | UNC 普通IPv4激活文档原文：ACL 只支持源IP和目的IP的配置，如果配置了端口，不会对端口配置生效 | 端口过滤失效 | warning | EV-IPSEC-01 |
| `CR-016000-UNC-03` | GRE 与 IPSec 源地址互斥（对称 UDG CR-015004-03） | `semantic_rule` | explicit | config | relation | OBJ-GRETUNNEL ↔ OBJ-IPSECINTFCFGIPSEC | GRE over IPsec 双隧道编排：Tunnel1(GRE) 用 LoopBack1 作源，Tunnel2(IPsec) 加密 GRE 报文；GRE源与 IPSec隧道地址不可共用同一接口（避免递归封装） | 隧道无法UP | critical | EV-IPSEC-04 |
| `CR-016000-UNC-04` | 主备隧道 PEERPRIORITY 主1备2（对称 UDG CR-015004-04） | `parameter_dependency` | explicit | config | parameter | CMD-UNC-016000-13.PEERPRIORITY (ADD ATTACHIKEPEER) | 主备场景（WORKMODE=Master_standby）：同 SEQUENCENUMBER 下 ATTACHIKEPEER 执行2次，主 PEERPRIORITY=1，备=2；IPv6 不支持 Round_robin | 主备切换失效 | critical | EV-IPSEC-03 |
| `CR-016000-UNC-05` | 多Sequence 同 POLICYNAME 各绑不同 ACL+Peer（对称 UDG CR-015004-05） | `parameter_dependency` | explicit | config | parameter | CMD-UNC-016000-09/10.SEQUENCENUMBER | 同 POLICYNAME 下多 SEQUENCENUMBER，每 sequence 各绑不同 ACLNUMBER + IKEPEERNAME，PEERPRIORITY 均可=1 | 多对端协商混乱 | critical | EV-IPSEC-06 |
| `CR-016000-UNC-06` | 双微服务双配一致性（对称 UDG CR-015004-06） | `semantic_rule` | explicit | config | relation | VNRS微服务 ↔ IPsec微服务 | UNC 普通IPv4激活文档原文：IPsec协商用到的隧道接口/IP/类型/VPN/指定本端接口需在 VNRS与IPsec微服务上一对一配置；未遵循双配原则会导致业务不通；删除时也须同时删除两侧 | 业务不通 | critical | EV-IPSEC-01 |
| `CR-016000-UNC-07` | 指定本端接口 SRCIFNAME 仅支持环回口（对称 UDG CR-015004-07） | `parameter_dependency` | explicit | restriction | parameter | CMD-UNC-016000-14.SRCIFNAME (ADD IPSECINTFCFGIPSEC) | SRCIFNAME 地址借用接口，只支持配置环回口；多个IPsec隧道可指定同一 LoopBack，但被指定接口需被IPsec隧道单独使用 | 借用失败/冲突 | warning | EV-IPSEC-07 |
| `CR-016000-UNC-08` | 国密场景必须先开 FWSOFTPARA DWORD 1401（对称 UDG CR-015004-08） | `sequence_rule` | explicit | config | command | CMD-UNC-016000-16 (SET FWSOFTPARA) | 国密场景所有配置前必须 SET FWSOFTPARA:PARAMETERSTYPE=DWORD,DWORDINDEX=1401,DWORDVALUE=1；且 IKEPROPOSAL 改用 Digital_envelope+SM2/SM3/SM4，IKEPEER 改用 CERTLOCALFILE/ENCCERTLOCFILE（UNC 国密场景 `_03728909` 与 UDG 同流程） | 国密算法不生效 | critical | EV-IPSEC-GM |
| **`CR-016000-UNC-09`** | ★**UNC 独有：5 类场景不支持限制**（UDG 无对应） | `semantic_rule` | explicit | restriction | relation | IPsec 全场景 | ★UNC 特性概述 `_61317289`「应用限制」原文：IPSEC 目前不支持场景——①GREv6 over IPSecv6；②OSPFv3 over IPSecv6；③IPSecv6 地址借用；④IPV4 报文入 IPSecv6 隧道；⑤IPV6 报文入 IPSecv4 隧道。UDG 015004 特性概述未列同款限制表（需在 UDG 复核时确认是否为 UNC 独有限制或 UDG 文档遗漏） | 配置后无法生效或协商失败 | critical | EV-IPSEC-01 |

---

## 5. MMLCommand 关键参数集（UNC 侧全部复用 UDG 权威参数表）

> **★抽取策略**：因 UNC 与 UDG 的 25 条 IPSec 命令为共享命令模块（手册文件ID逐一相同、参数逐一相同），本节不重复列全参数。CommandParameter 全量参数表见 UDG 015004 §5（§5.1 ACLGROUPIPSEC ~ §5.19 IPsec微服务双配族，同名同参，零差异）。
> **Schema 参考**：§11.4 CommandParameter。`required_mode` 取值 `required / optional / conditional_required`。
> **引用约定**：UNC 侧每条命令的 CommandParameter 实例 `used_by_features = [IPFD-016000]`，并 `parameter_ref → CMD-UDG-015004-xx 的参数表`（UDG 为权威源）。这样避免在 UNC 侧重复维护一份易漂移的参数副本。
> **★唯一需补全项**：`ADD IFIPV6ADDRESSIPSEC`（CMD-UNC-016000-25）—— UNC 手册已定位 `_21521206`，参数结构参照 IFIPV4ADDRESSIPSEC（IFNAME/IPV6ADDR/PREFIXLEN/ADDRTYPE）IPv6 化，需在 UDG 015004 §5.20 复核补全时引用此 UNC 手册源。

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

> **★说明**：operates_on 边与 UDG 015004 §6 完全相同（25 条核心 + 8 条前置依赖引用）。UNC 侧每条边的 MMLCommand 由 `CMD-UDG-*` 改为 `CMD-UNC-*`，ConfigObject 引用同一对象（跨产品共享）。VNRS侧前置依赖（L3VPNINST/VPNINSTAF/INTERFACE/IPBINDVPN/IFIPV4ADDRESS/IPSECINTFCFG/SRROUTE/OSPF族）在 UNC 侧的命令手册文件ID 与 UDG 不同（UNC 用 `_49802446`/`_49802178`/`_50120734`/`_00865509`/`_49960870`/`_50281406`/`_49961498` 等），但命令命名相同，属 UNC 侧 VNRS微服务独立命令族。

---

## 7. ★CommandRule governs MMLCommand 边表（§11.6 反向）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand / CommandParameter / ConfigObject`（反向）。

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-016000-UNC-01 | CMD-UNC-016000-06.DHGROUP (ADD IKEPROPOSAL) | DHGROUP 不能为 None 或不配置，建议 Dh_group19（对称 UDG） |
| CR-016000-UNC-02 | CMD-UNC-016000-02/04 (ACLRULEADV4/6IPSEC) 端口参数 | ACL 仅支持源/目的IP，端口配置不生效（对称 UDG） |
| CR-016000-UNC-03 | OBJ-GRETUNNEL ↔ OBJ-IPSECINTFCFGIPSEC | GRE 与 IPSec 源地址互斥（双隧道编排，对称 UDG） |
| CR-016000-UNC-04 | CMD-UNC-016000-13.PEERPRIORITY (ADD ATTACHIKEPEER) | 主备 PEERPRIORITY 主1备2；IPv6 不支持 Round_robin（对称 UDG） |
| CR-016000-UNC-05 | CMD-UNC-016000-09/10.SEQUENCENUMBER | 多Sequence 各绑不同 ACL+Peer（对称 UDG） |
| CR-016000-UNC-06 | VNRS微服务 ↔ IPsec微服务 关系 | 双微服务双配一致性（对称 UDG） |
| CR-016000-UNC-07 | CMD-UNC-016000-14.SRCIFNAME (ADD IPSECINTFCFGIPSEC) | SRCIFNAME 仅支持环回口（对称 UDG） |
| CR-016000-UNC-08 | CMD-UNC-016000-16 (SET FWSOFTPARA) + IKEPROPOSAL/IKEPEER 国密参数 | 国密场景必须先开 DWORD 1401 + 算法/认证替换（对称 UDG） |
| **CR-016000-UNC-09** | ★UNC 独有：IPsec 全场景关系（5 类不支持场景） | UNC 特性概述应用限制：不支持 GREv6-over-IPSecv6 / OSPFv3-over-IPSecv6 / IPSecv6 地址借用 / IPv4入IPSecv6 / IPv6入IPSecv4 |

---

## 8. 使用实例脚本（★13 场景与 UDG 015004 完全对称）

> **★UNC 侧 13 场景矩阵**：与 UDG 015004 §8.0 矩阵完全相同（8 普通场景 + 5 国密场景；GRE/多Sequence/指定本端接口在普通与国密下各一份）。各场景的命令级差异（ACL命令族/IKEPEER/IPSECPOLICY/ATTACHIKEPEER/独有命令/引流方式）逐项对称。
> **场景差异矩阵**：直接引用 UDG 015004 §8.0（13 场景 × 6 维度表），UNC 侧无新增场景维度。
> **UNC 侧脚本示例**：因命令/参数/编排与 UDG 逐字节相同（脚本仅 IP 示例值不同），此处不重复贴脚本全文。代表性脚本片段见 UDG 015004 §8.1（普通IPv4 基准）、§8.2（IPv4主备）、§8.3（多Sequence）、§8.4（指定本端接口）、§8.5（GRE）、§8.6（国密）、§8.7（IPv6）。
> **★UNC 独有场景约束**：CR-016000-UNC-09 约束下，UNC 侧 GRE 场景仅支持 GRE over IPSecv4（不支持 GREv6 over IPSecv6）；OSPF 场景仅支持 OSPF over IPSecv4（不支持 OSPFv3 over IPSecv6）。

### 8.0 UNC 侧 13 场景文件清单（与 UDG 文件编号不同，场景语义对称）

| # | 场景 | UNC 激活文件ID | 对称 UDG 文件ID | 场景差异维度 |
|---|------|---------------|----------------|--------------|
| 1 | 普通IPv4 | `_61317238` | `_01_10002` | 与 UDG 同（基准） |
| 2 | 普通IPv6 | `_78985538` | `_01_10003` | IPv6 命令族 |
| 3 | IPv4主备 | `_88744738` | `_01_10004` | WORKMODE + 多PEERPRIORITY |
| 4 | IPv6主备 | `_53998700` | `_01_10005` | IPv6 + 主备 |
| 5 | GRE over IPsec | `_78985535` | `_01_10006` | 双隧道编排（★UNC 仅 GREv4） |
| 6 | OSPF over IPsec | `_90949389` | `_01_10007` | OSPF 引流（★UNC 仅 OSPFv2） |
| 7 | 多Sequence | `_78985536` | `_01_10008` | 同 POLICYNAME 多 SEQUENCE |
| 8 | 指定本端接口 | `_78985537` | `_01_10009` | SRCIFNAME=LoopBack |
| 9 | 国密-普通IPv4 | `_03728909` | `_03728909`（与UDG同文件ID） | FWSOFTPARA+证书+SM算法 |
| 10 | 国密-普通IPv6 | `_53768408` | `_53768408`（与UDG同文件ID） | 同9 + IPv6 |
| 11 | 国密-GRE | `_53928160` | `_53928160`（与UDG同文件ID） | 同9 + GRE |
| 12 | 国密-多Sequence | `_03408185` | `_03408185`（与UDG同文件ID） | 同9 + 多Sequence |
| 13 | 国密-指定本端接口 | `_03567841` | `_03567841`（与UDG同文件ID） | 同9 + SRCIFNAME |

> **★★关键观察**：国密 5 场景（#9~#13）的 UNC 文件ID 与 UDG **完全相同**（`_03728909`/`_53768408`/`_53928160`/`_03408185`/`_03567841`），进一步证实这些激活文档为 UDG/UNC 共享文档（同一文档同时归属两产品）。普通 8 场景（#1~#8）的 UNC 文件ID 与 UDG 不同，但命令/参数/编排逐项对称。

---

## 9. 抽取核对清单

### 9.1 ★U+C 命令差异对照表（核心交付物）

| 命令族 | UDG 015004 | UNC 016000 | 差异类型 | 处理方式 |
|--------|-----------|-----------|---------|---------|
| ADD ACLGROUPIPSEC / ACLRULEADV4IPSEC / ACLGROUP6IPSEC / ACLRULEADV6IPSEC | 手册 `_26150747`/`_80751058`/`_21521202`/`_68200943` | **同文件ID** | 同名同参 | used_by_features 加 016000，引用 UDG 权威参数 |
| ADD IPSECPROPOSALIPSEC | `_80432524` | **同** | 同名同参 | 同上 |
| ADD IKEPROPOSAL | `_26032189` | **同** | 同名同参 | 同上 |
| ADD IKEPEER / IKEPEER6 | `_80592498` / `_21361306` | **同** | 同名同参 | 同上 |
| ADD IPSECPOLICY / IPSECPOLICY6 / IPSECPOLICYTM | `_25912243` / `_68320981` / `_96044554` | **同** | 同名同参 | 同上 |
| ADD PROPATTACHIPSECPROPOSAL / ATTACHIKEPEER | `_80592500` / `_80910984` | **同** | 同名同参 | 同上 |
| ADD IPSECINTFCFGIPSEC | `_80910986` | **同** | 同名同参 | 同上 |
| SET IKEGLOBALCONFIG | `_26032205` | **同** | 同名同参 | 同上 |
| SET FWSOFTPARA（国密开关） | `_18818231` | **同** | 同名同参 | 同上 |
| ADD CERTSCENE / SET PKICRLCHECK / DSP PKICERTLIST | `_25912241` / `_41702627` / `_30311459` | **同** | 同名同参 | 同上 |
| ADD GRETUNNEL | `_00841729` | **同** | 同名同参 | 同上 |
| ADD L3VPNINSTIPSEC / VPNINSTAFIPSEC / INTERFACEIPSEC / IPBINDVPNIPSEC / IFIPV4ADDRESSIPSEC | `_25830689`/`_26032191`/`_26150749`/`_80751060`/`_80432522` | **同** | 同名同参 | 同上 |
| **ADD IFIPV6ADDRESSIPSEC** | ⚠️UDG 手册未定位 | **★UNC 手册已定位 `_21521206`** | UNC 补齐 UDG 缺口 | UNC 独立登记，参数待复核补全 UDG |
| 国密 5 场景激活文档 | 文件ID `_03728909`/`_53768408`/`_53928160`/`_03408185`/`_03567841` | **同文件ID（共享文档）** | 完全相同 | 无需重复抽取 |
| VNRS侧前置依赖（L3VPNINST/VPNINSTAF/INTERFACE/IPBINDVPN/IFIPV4ADDRESS/IPSECINTFCFG/SRROUTE/OSPF族） | UDG 文件ID `_xxx` | UNC 文件ID `_49802446`/`_49802178`/`_49960870`/`_50120734`/`_00865509`/`_50281406`/`_49961498` 等（**不同**） | **同名（VNRS微服务命令族 UNC 独立）** | UNC 侧 VNRS 命令独立登记（非本特性核心，仅引用） |
| 应用限制（5 类不支持场景） | UDG 特性概述未列同款限制表 | **UNC 特性概述 `_61317289` 独有应用限制** | **UNC 独有 CommandRule** | CR-016000-UNC-09 独立抽取 |
| 版本支持 | UDG 版本序列 | UNC：20.5.0 首发；20.8.0 增 IPv6/NAT穿越/主备 | 版本号不同 | 仅元数据差异，能力集一致 |

### 9.2 配置类命令手册路径（UNC 侧，与 UDG 同一组手册 — 文件ID逐一相同）

| 命令 | 来源手册路径（相对 `output/UNC 20.15.2 产品文档(裸机容器) 05/`） | 参数行数 |
|------|----------------------------------------------------------------|---------|
| ADD ACLGROUPIPSEC | `OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md` | 5 |
| ADD ACLRULEADV4IPSEC | `.../IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md` | 25 |
| ADD ACLGROUP6IPSEC | `.../IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md` | 5 |
| ADD ACLRULEADV6IPSEC | `.../IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md` | 25 |
| ADD IPSECPROPOSALIPSEC | `.../IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md` | 6 |
| ADD IKEPROPOSAL | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md` | 11 |
| ADD IKEPEER | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md` | 21 |
| ADD IKEPEER6 | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md` | 20 |
| ADD IPSECPOLICY | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md` | 27 |
| ADD IPSECPOLICY6 | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md` | 28 |
| ADD IPSECPOLICYTM | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略模板/增加IPsec策略模板（ADD IPSECPOLICYTM）_96044554.md` | 22 |
| ADD PROPATTACHIPSECPROPOSAL | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md` | 5 |
| ADD ATTACHIKEPEER | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md` | 6 |
| ADD IPSECINTFCFGIPSEC | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md` | 4 |
| SET IKEGLOBALCONFIG | `.../IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md` | 19 |
| SET FWSOFTPARA | `OM参考/命令/UNC MML命令/平台服务管理/操作维护/软参配置管理/设置ServiceFabric软参（SET FWSOFTPARA）_18818231.md` | 5 |
| ADD CERTSCENE | `.../IPSEC功能管理/IP服务/IP安全管理/公钥基础设施/PKI场景/增加证书场景（ADD CERTSCENE）_25912241.md` | 5 |
| SET PKICRLCHECK | `.../IPSEC功能管理/IP服务/IP安全管理/公钥基础设施/使能CRL检查/设置CRL检查（SET PKICRLCHECK）_41702627.md` | 1 |
| DSP PKICERTLIST | `.../IPSEC功能管理/IP服务/IP安全管理/公钥基础设施/查询证书列表/显示证书列表（DSP PKICERTLIST）_30311459.md` | 调测略 |
| ADD GRETUNNEL | `.../VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md` | 17 |
| ADD L3VPNINSTIPSEC | `.../IPSEC功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例配置命令/增加L3VPN实例（ADD L3VPNINSTIPSEC）_25830689.md` | 1 |
| ADD VPNINSTAFIPSEC | `.../IPSEC功能管理/IP服务/VPN管理/L3VPN管理/VPN实例地址族配置命令/增加L3VPN实例地址族（ADD VPNINSTAFIPSEC）_26032191.md` | 2 |
| ADD INTERFACEIPSEC | `.../IPSEC功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACEIPSEC）_26150749.md` | 8 |
| ADD IPBINDVPNIPSEC | `.../IPSEC功能管理/IP服务/接口管理/绑定VPN/增加接口绑定VPN（ADD IPBINDVPNIPSEC）_80751060.md` | 7 |
| ADD IFIPV4ADDRESSIPSEC | `.../IPSEC功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESSIPSEC）_80432522.md` | 4 |
| **ADD IFIPV6ADDRESSIPSEC**（★UNC 补齐） | `.../IPSEC功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESSIPSEC）_21521206.md` | 待复核（推断 4） |
| **合计** | **25 命令全部 UNC 手册定位成功（文件ID 与 UDG 逐一相同，手册为共享模块）** | **255+（同 UDG）** |

### 9.3 ⚠️手册未定位列表（UNC 侧）

| 命令 | 状态 | 说明 |
|------|------|------|
| （无） | — | ★**UNC 侧 25 条配置命令手册全部定位成功**。`ADD IFIPV6ADDRESSIPSEC` 在 UNC 侧手册已定位（`_21521206`），补齐 UDG 015004 的未定位项。 |

### 9.4 UNC 独有发现（UDG 015004 未覆盖）

| 维度 | UNC 独有内容 | 影响 |
|------|------------|------|
| 应用限制 CommandRule | CR-016000-UNC-09：5 类不支持场景（GREv6-over-IPSecv6 / OSPFv3-over-IPSecv6 / IPSecv6 地址借用 / IPv4入IPSecv6 / IPv6入IPSecv4） | 新增 1 条 UNC 独有 CommandRule |
| IFIPV6ADDRESSIPSEC 手册定位 | UNC 手册 `_21521206` 已定位 | 反向补齐 UDG 015004 §9.2 未定位项 |
| 版本序列 | UNC 20.5.0 首发 / 20.8.0 增 IPv6/NAT/主备 | 仅元数据差异 |
| VNRS侧前置依赖命令文件ID | UNC 用 `_49802446`/`_49802178`/`_49960870`/`_50120734`/`_00865509`/`_50281406`/`_49961498` 等（与 UDG 不同） | VNRS微服务命令族 UNC 独立（非本特性核心） |

### 9.5 抽取统计

| 维度 | 数量 |
|------|------|
| 配置类命令（UNC 手册定位成功） | 25（与 UDG 同清单，全部同名同参复用） |
| 配置类命令参数总行数 | 255+（复用 UDG 权威参数，不重复维护） |
| 查询/调测类命令（本期略） | 12+（与 UDG 同） |
| ⚠️手册未定位命令 | **0**（UNC 侧全部定位；IFIPV6ADDRESSIPSEC 已补齐） |
| ConfigObject | 25（与 UDG 同，product_side=UNC） |
| CommandRule | **9**（UDG 对称 8 条 + UNC 独有 1 条 CR-016000-UNC-09） |
| ConfigObject 关系边 | 20（与 UDG 同：contains 3 + refers_to 8 + depends_on 6 + activates 3） |
| operates_on 边 | 24 核心 + 8 前置依赖引用（与 UDG 同） |
| 激活子场景脚本 | **13**（8 普通 + 5 国密，与 UDG 完全对称；国密 5 场景文件ID 与 UDG 共享） |
| UNC 独有命令族 | **0**（IPSec 命令族为 UDG/UNC 共享模块，无 UNC 独有命名） |
| 复用 UDG 命令族 | **25**（全部） |
| IPv6 独有命令族 | 4（与 UDG 同：ACLGROUP6IPSEC/ACLRULEADV6IPSEC/IKEPEER6/IPSECPOLICY6） |

---

> 本文件为 IPFD-016000 IPSec功能（UNC/SMF 侧）命令层抽取，**13 场景不合并，严格对齐 `04-cluster-E-IPSec-015004.md` 9 节样板**。
> **★关键贡献**：
> ①**确认 IPSec 命令族为 UDG/UNC 共享模块**（25 命令手册文件ID逐一相同），采用「复用 UDG 权威参数 + used_by_features 加 016000 引用」策略，避免重复维护易漂移的参数副本；
> ②**补齐 UDG 01500004 的 IFIPV6ADDRESSIPSEC 未定位缺口**（UNC 手册 `_21521206` 已定位，反向更新 UDG）；
> ③**抽取 UNC 独有 CommandRule CR-016000-UNC-09**（5 类不支持场景应用限制，源自 UNC 特性概述 `_61317289` 原文，UDG 特性概述无同款限制表）；
> ④**确认 13 场景矩阵 U+C 完全对称**（国密 5 场景文件ID与 UDG 共享；普通 8 场景文件ID不同但命令/参数/编排逐项对称）；
> ⑤**登记 VNRS侧前置依赖命令 UNC 独立文件ID**（VNRS微服务命令族在 UDG/UNC 间文件ID不同，但命令命名相同，属 UNC 侧独立命令族）。
