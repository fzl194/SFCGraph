# APN 业务域命令图谱 · 簇F：网元选择 + 接入控制

> **文件定位**：`three-layer-graph/draft/04-cluster-F-网元接入控制.md`
> **特性范围**：4 个网元选择/接入控制特性
>   - WSFD-107010 UPF选择（UNC/SMF）— **文档缺口（仅1篇特性概述，无激活/参考信息）**
>   - WSFD-010202 基于位置区域的对等网元选择（UNC/SGSN/MME）— AREDNS 族 DNS 域名简化
>   - WSFD-106003 用户接入控制功能（UNC/AMF + SGSN/MME 两套）— NGMMSUBDATA/GBARD/IUARD/S1ARD/NGMMPROCTRL
>   - GWFD-010151 接入控制（UDG/SGW-U+PGW-U+UPF）— APNQOSATTR U 面带宽流控（CAR/Shaping）
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **结构对齐**：严格 follow `04-cluster-B-GWFD-010105.md` 样板（表格列、CMD-<NF>-<featureid>-nn 编号、9 节结构）
> **数据来源**：4 特性文档（WSFD-107010 仅概述）+ 30 篇 MML 命令手册原文（路径见 §9 抽取核对清单）
> **铁律**：命令/参数 100% 来自原始产品文档原文，零编造。手册未定位的命令标注「⚠️手册未定位」。
> **UPF选择文档缺口**：WSFD-107010 仅 1 篇特性概述（`WSFD-107010 UPF选择_10789013.md`），**无激活文档、无参考信息**。本文件命令/参数来源为「特性概述原文 + 概述中嵌入式引用的 MML 手册路径」——概述 §原理概述 表1「UPF选择原则」已将每条选择原则与具体命令逐一对应并附手册路径，等价于参考信息命令清单；激活脚本缺位，§8 使用实例由概述表2 UPF 属性示例 + 手册使用实例组合而成，已标注「概述推导」。

---

## 0. 命令清单总览（簇F 4 特性用到的全部命令）

### 0.1 按特性分布

| 特性 | 配置类命令数 | 查询类命令数 | 命令清单（配置类核心） |
|------|------------|------------|---------------------|
| **WSFD-107010 UPF选择**（UNC，⚠️文档缺口） | 14 | 0（无 LST，全 SET/ADD） | ADD PNFPROFILE、ADD PNFDNN、ADD PNFNS、ADD PNFDNAI、ADD PNFUPFINFO、ADD PNFSMFSERAREA、ADD PNFTAI、ADD PNFTAIRANGE、ADD UPNODE、ADD UPAREA、ADD UPAREABINDN2TAI、ADD LOCBINDAREA、ADD UPBINDS11、ADD UPBINDGNGP；策略类 SET UPSELECTPRI、SET UPSELECTFLAG、SET APNUPSELPLY、SET UPLOADBALANCE |
| **WSFD-010202 对等网元选择**（UNC/SGSN/MME） | 3 ADD（+ MOD/RMV 配套） | LST 配套 | ADD AREADNS、ADD IPV4DNSH、ADD DNSN（MOD/RMV/LST 同族归 §1 不重复抽参数） |
| **WSFD-106003 用户接入控制（AMF）**（UNC/AMF） | 2 | LST NGMMSUBDATA/NGMMPROCTRL | ADD NGMMSUBDATA、SET NGMMPROCTRL |
| **WSFD-106003 用户接入控制（SGSN/MME）**（UNC/SGSN/MME） | 3 ADD（+ MOD/RMV 配套） | LST 配套 | ADD GBARD、ADD IUARD、ADD S1ARD（MOD/RMV/LST 同族不重复抽参数） |
| **GWFD-010151 接入控制**（UDG/SGW-U+PGW-U+UPF） | 2 核心（ADD APN 引用簇A、SET APNQOSATTR 核心） | LST APNQOSATTR | SET APNQOSATTR（ADD APN 归簇A，本文件 §6 仅标注引用） |

> **策略类命令归类**：SET UPSELECTPRI / SET UPSELECTFLAG / SET APNUPSELPLY / SET UPLOADBALANCE 在概述「UPF 选择原则」表1 中作为「配置命令」明确列出（负载/优先级/合一/位置区/S11 等优选条件开关），属于 WSFD-107010 核心策略命令，本文件抽参数。

### 0.2 ConfigObject 分布（本簇涉及）

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| **UPF 选择·NF 概述与属性**（WSFD-107010） | 9 | PNFPROFILE、PNFDNN、PNFNS、PNFDNAI、PNFUPFINFO、UPNODE、PNFSMFSERAREA、PNFTAI、PNFTAIRANGE |
| **UPF 选择·位置/接口绑定**（WSFD-107010） | 5 | UPAREA、UPAREABINDN2TAI、LOCBINDAREA、UPBINDS11、UPBINDGNGP |
| **UPF 选择·策略开关**（WSFD-107010） | 4 | UPSELECTPRI、UPSELECTFLAG、APNUPSELPLY、UPLOADBALANCE |
| **对等网元选择·DNS 简化**（WSFD-010202） | 3 | AREADNS、IPV4DNSH、DNSN |
| **用户接入控制·AMF**（WSFD-106003） | 2 | NGMMSUBDATA、NGMMPROCTRL |
| **用户接入控制·SGSN/MME ARD 族**（WSFD-106003） | 3 | GBARD、IUARD、S1ARD |
| **接入控制·U 面带宽流控**（GWFD-010151） | 1 | APNQOSATTR |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1 所有 MMLCommand。
> **声明**：本文件 §1 所有 MMLCommand 的 `status` 字段值均为 `active`（Schema §11.3 MMLCommand.status 必备）。簇F 所有正式命令均处于启用状态。
> **依据**：所有命令均在产品文档正式登记，无 `deprecated` 或 `planned` 状态。

---

## 1. MMLCommand 实例化（按特性分组，共 25 个核心配置命令）

### 1.1 WSFD-107010 UPF选择 — NF 概述与属性族（UNC/SMF，⚠️文档缺口，9个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-107010-01` | `ADD PNFPROFILE` | ADD | PNFPROFILE | ★对端NF实例概述信息（UPF 选择核心；NF类型含 NfUPF；PRIORITY/CAPACITY/LOAD/LOCALITY/FQDN/IP 地址；★高危：UPF 类型时 PRIORITY 仅在 UPSELECTFLAG.PRIORITYFLAG=ENABLE 时生效） | NFINSTANCEID, NFTYPE, NFSTATUS, FQDN, INTERPLMNFQDN, IPADDRESSTYPE, IPV4ADDRESS1~4, IPV6ADDRESS1~4, PORT, CAPACITY, PRIORITY, LOAD, LOCALITY, NFDESCNAME, SCHEME | EV-FK-107010（概述） |
| `CMD-UNC-107010-02` | `ADD PNFDNN` | ADD | PNFDNN | 对端NF的DNN信息（必选条件·用户DNN；★PRISWITCH/CAPSWITCH=INHERIT/SPECIFIC 优先级权重切换；PNFNSINDEX 关联切片索引） | INDEX, NFINSTANCEID, DNN, PNFNSINDEX, PDUSESSIONTYPE, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY, ISLOCKED | EV-FK-107010 |
| `CMD-UNC-107010-03` | `ADD PNFNS` | ADD | PNFNS | 对端NF的切片信息（必选条件·用户切片；SST+SD；★INDEX 与 ADD PNFDNN.PNFNSINDEX 关联） | INDEX, NFINSTANCEID, SST, SD, NSDESCRIPTION | EV-FK-107010 |
| `CMD-UNC-107010-04` | `ADD PNFDNAI` | ADD | PNFDNAI | 对端NF的DNAI信息（必选条件·DNAI；★PNFDNNINDEX 关联 DNN；PRISWITCH/CAPSWITCH 优先级权重） | INDEX, NFINSTANCEID, DNAI, PNFDNNINDEX, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY, ISLOCKED | EV-FK-107010 |
| `CMD-UNC-107010-05` | `ADD PNFUPFINFO` | ADD | PNFUPFINFO | 对端UPF信息（必选条件·UPF 是否支持与EPS互通；IWKEPSIND；★此参数当前版本不使用） | NFINSTANCEID, IWKEPSIND, PDUSESSIONTYPE | EV-FK-107010 |
| `CMD-UNC-107010-06` | `ADD PNFSMFSERAREA` | ADD | PNFSMFSERAREA | 对端NF的SMF服务区域（必选条件·用户位置区；SMFSERVINGAREA；★SMFSERVINGAREA="*" 支持所有区域；PRISWITCH/CAPSWITCH） | NFINSTANCEID, SMFSERVINGAREA, PNFNSINDEX, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY | EV-FK-107010 |
| `CMD-UNC-107010-07` | `ADD PNFTAI` | ADD | PNFTAI | 对端NF的TAI信息（必选条件·用户位置区 TAI；★TAI="*" 支持所有 TAI；PRISWITCH/CAPSWITCH） | NFINSTANCEID, TAI, PNFNSINDEX, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY, BINDNWDAFINFOID | EV-FK-107010 |
| `CMD-UNC-107010-08` | `ADD PNFTAIRANGE` | ADD | PNFTAIRANGE | 对端NF的TAI范围（必选条件·用户位置区 TAI 范围；★QUERYTYPE=START_END/PATTERN；MCC/MNC 必填；PRISWITCH/CAPSWITCH） | INDEX, NFINSTANCEID, MCC, MNC, QUERYTYPE, RANGESTART, RANGEEND, PATTERN, PNFNSINDEX, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY, BINDNWDAFINFOID | EV-FK-107010 |
| `CMD-UNC-107010-09` | `ADD UPNODE` | ADD | UPNODE | ★UPF节点特征（必选条件·UPF位置特征+分流能力；★28 参数；LOCATION=Local/Central/CentralOnly 决定主辅锚点能力；高危：SUPULCLBPONLY=ENABLE 或 LOCATION=LOCAL 不能作 I-UPF） | NFINSTANCENAME, LOCATION, UPFUNCTION, LOCK, APSAMIGFUNC, ADDRALLOCMODE, SHAREDUPFSW, VPNNAME, SUPULCLBPONLY, SUPATSSS, IPV6NDPLCY, IOSWITCH, NFDESCNAME, CAMPUSSW, ULCLFWDTNLSW, PDUESTWITHOUTN9, NGLANSW, PSACOMBINEULCL, MBSSW, SUPINTELLISRV, PATHMIGSW, TOPATHMIGSW, PATHMIGTIMER, UEIPNATFUNC, PROXYUPFS8USW, QOSANASW, TOHPSASW, SILENTSIGMIGSW, PATHMIGEXT | EV-FK-107010 |

### 1.2 WSFD-107010 UPF选择 — 位置/接口绑定族（UNC/SMF+SGW-C+PGW-C，5个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-107010-10` | `ADD UPAREA` | ADD | UPAREA | UPF服务区（必选条件·用户位置区；AREATYPE=S1TAI/N2TAI/LAI 三类型） | AREANAME, AREATYPE | EV-FK-107010 |
| `CMD-UNC-107010-11` | `ADD UPAREABINDN2TAI` | ADD | UPAREABINDN2TAI | UPF服务区名称绑定的5G TAI范围（SMF；★各服务区 5G TAI 范围不允许交集；起止 PLMN 必须一致） | AREANAME, N2BEGINTAI, N2ENDTAI | EV-FK-107010 |
| `CMD-UNC-107010-12` | `ADD LOCBINDAREA` | ADD | LOCBINDAREA | UPF位置与优先服务区绑定（优选条件·位置区优先级；★SET UPSELECTFLAG.LOCALITYFLAG=ENABLE 时生效；LOCALITY 关联 PNFPROFILE.LOCALITY） | LOCALITY, AREANAME | EV-FK-107010 |
| `CMD-UNC-107010-13` | `ADD UPBINDS11` | ADD | UPBINDS11 | SGW-U 与 S11 接口绑定（优选条件·S11口；SGW-C；★ULI 为空时基于 S11 选 SGW-U；PRIORITY 0~255） | NFINSTANCENAME, S11IPTYPE, S11IPV4, S11IPV6, PRIORITY | EV-FK-107010 |
| `CMD-UNC-107010-14` | `ADD UPBINDGNGP` | ADD | UPBINDGNGP | GGSN/PGW-U 与 Gn/Gp 或 S5/S8 接口绑定（GGSN/PGW-C；★PRIORITY 0~255） | NFINSTANCENAME, GNGPIPTYPE, GNGPIPV4, GNGPIPV6, PRIORITY | EV-FK-107010 |

### 1.3 WSFD-107010 UPF选择 — 策略开关族（UNC/SMF+SGW-C+PGW-C+GGSN，4个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-107010-15` | `SET UPSELECTPRI` | SET | UPSELECTPRI | ★UPF选择策略次序（优选条件排序；FIRSTPRIORITY/SECONDPRIORITY/THIRDPRIORITY 取 Combined/LocS11Priority/Load；★三者不可相同；初始值 Combined/LocS11Priority/Load） | FIRSTPRIORITY, SECONDPRIORITY, THIRDPRIORITY | EV-FK-107010 |
| `CMD-UNC-107010-16` | `SET UPSELECTFLAG` | SET | UPSELECTFLAG | ★UPF选择条件开关（15 参数；含 N3UPFAPNFLAG/ULISGWFLAG/AMBRUPFFLAG/PRIORITYFLAG/LOCALITYFLAG/PSAPOSPRIFLAG/LOADFLTFLAG/OVERLOADFLTFLAG/OVERLOADALWFLAG/LOCKAPNFLAG/ACCLOCKAPNFLAG/LEASEUPFFLAG/NGLANUPFSELSW/ROAMTYPEFLAG/UPFBLOCKFLAG；★高危：PRIORITYFLAG=ENABLE 后 PNF 系列优先级/容量才生效） | N3UPFAPNFLAG, ULISGWFLAG, AMBRUPFFLAG, UPFBLOCKFLAG, ROAMTYPEFLAG, NGLANUPFSELSW, LEASEUPFFLAG, LOCALITYFLAG, PSAPOSPRIFLAG, OVERLOADFLTFLAG, PRIORITYFLAG, OVERLOADALWFLAG, LOADFLTFLAG, LOCKAPNFLAG, ACCLOCKAPNFLAG | EV-FK-107010 |
| `CMD-UNC-107010-17` | `SET APNUPSELPLY` | SET | APNUPSELPLY | ★APN粒度UP选择策略（覆盖全局；含 PSAPOSPRIFLAG/ULISGWFLAG/SHAREDPRIFLAG/PRIORITYFLAG=INHERIT/DISABLE/ENABLE；COMBINEPRISTG/COMBINEDSELSTG/LOCS11SELSTG 优选策略；★ADD APN 时自动建初始记录） | APN, PSAPOSPRIFLAG, ULISGWFLAG, SHAREDPRIFLAG, PRIORITYFLAG, COMBINEPRISTG, COMBINEDSELSTG, LOCS11SELSTG | EV-FK-107010 |
| `CMD-UNC-107010-18` | `SET UPLOADBALANCE` | SET | UPLOADBALANCE | UP负载均衡（负载条件；LOADCTRLFLG/OVERLOADCTRLFLG 处理 UPF 上报 LCI/OCI；LIGHTLOAD/HEAVYLOAD 0~100 门限；★轻负载优先于重负载） | LOADCTRLFLG, LIGHTLOAD, HEAVYLOAD, OVERLOADCTRLFLG | EV-FK-107010 |

### 1.4 WSFD-010202 对等网元选择 — DNS 简化族（UNC/SGSN/MME，3 ADD）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-010202-01` | `ADD AREADNS` | ADD | AREADNS | ★位置区域DNS域名（核心；★DNTYPE 14 种：SGW/SGSN/MME/GGSN-PGW/MSC × RAI/TAI/LAI/UUT；LAC/LACRANGE/RAC/RACRANGE/TAC/TACRANGE 条件可选；ZONESW=YES 时 ZONENAME 必填，ZONELOC 定制域名位置） | DNTYPE, LAC, LACRANGE, RAC, RACRANGE, TAC, TACRANGE, UUT, ZONESW, ZONENAME, ZONELOC | EV-FK-010202 |
| `CMD-UNC-010202-02` | `ADD IPV4DNSH` | ADD | IPV4DNSH | IPV4 DNS Hostfile 记录（A 解析；HSINDEX+HOSTNAME+ADDRSECTION 必填；IPV4ADDR1~8 + PRIORITY1~8 + WEIGHT1~8 三元组；一个主机名最多 64 IP） | HSINDEX, HOSTNAME, ADDRSECTION, IPV4ADDR1~8, PRIORITY1~8, WEIGHT1~8 | EV-FK-010202 |
| `CMD-UNC-010202-03` | `ADD DNSN` | ADD | DNSN | DNS NAPTR 记录（FQDN→网元接口映射；★ENTITY 8 类型 + INTYPE 13 类型有配置约束；智能网关选择 topon/topoff 拓扑优选；S5PROTOCOL/S8PROTOCOL/UEUSGTYPEPLCY/DCNR/SMF） | FQDN, HSINDEX, ENTITY, INTYPE, S5PROTOCOL, S8PROTOCOL, UEUSGTYPEPLCY, UEUSGTYPEGPID, DCNR, SMF, PRIORITY, WEIGHT, DESC | EV-FK-010202 |

### 1.5 WSFD-106003 用户接入控制（AMF）（UNC/AMF，2个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-106003-01` | `ADD NGMMSUBDATA` | ADD | NGMMSUBDATA | ★AMF本地用户移动性管理参数（★AMF本地优先于签约；SUBRANGE 5 类 ALL_USER/HOME_USER/FOREIGN_USER/IMSI_PREFIX/IMSI，匹配优先级 IMSI>IMSI_PREFIX>FOREIGN/HOME>ALL；含 RATRESTRICT/CORERESTRICT/RFSPINDEX/NIM/DRX/UEAMBRULK/DLK 等 17 参数） | SUBRANGE, IMSIPRE, IMSI, RATRESTRICT, CORERESTRICT, RFSPINDEX, NIM, DRX, RFSPPRI, UEAMBRULK, UEAMBRDLK, EXRATRESTRICT, PRIMRATRESTRICT, SECRATRESTRICT, MPSMCSPRI, MPS, MCS | EV-FK-106003 |
| `CMD-UNC-106003-02` | `SET NGMMPROCTRL` | SET | NGMMPROCTRL | ★5G MM流程控制参数（拒绝原因值下发；★PROT 14 流程类型；60+ 拒绝原因值参数；取值 0=不使用特殊原因值；高危：原因值不合理导致用户无法驻留） | PROT, AUSFDISCNOFOUND/AUSFDISCFC/AUSFDISCOTHER（AUSF_DISCOVERY），AIRUSERNOTFOUND/AIRAUTHREJECTED 等 11（AIR），AUTHRESCHKFAIL/AUTHMACFAIL/AUTHSYNCHFAIL（AUTHENTICATION），UDMREG*/UDMGETSUB*/UDMSUB* 系列（UDM），ACCRST/ROAMRST/AREARST/SARST/NSNOTAVL（OTHER_PROC），CAGREJ（CAG），UDMREGALWAYS/UDMDISCALWAYS（强制开关）等 | EV-FK-106003 |

### 1.6 WSFD-106003 用户接入控制（SGSN/MME）— ARD 族（UNC/SGSN+MME，3 ADD）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-106003-03` | `ADD GBARD` | ADD | GBARD | ★Gb模式接入限制参数（SGSN；GERAN；★按 IMSI 号段分类 + 卡类型/签约ARD/APNNI 区分；CARDTYPE 仅 GERAN/UTRAN 有；CTRLTYPE=ALLOW/REJECT；3 种控制方式：签约ARD/签约APN/卡类型） | SUBRANGE, IMSIPRE, BEGIMSI, ENDIMSI, APNNI, CARDTYPE, ARD, CTRLTYPE, CAUSE, SDCAUSE | EV-FK-106003 |
| `CMD-UNC-106003-04` | `ADD IUARD` | ADD | IUARD | ★Iu模式接入限制参数（SGSN；UTRAN；同 GBARD 结构 + CSI 属性；卡类型控制） | SUBRANGE, IMSIPRE, BEGIMSI, ENDIMSI, APNNI, CARDTYPE, ARD, CTRLTYPE, CAUSE, SDCAUSE | EV-FK-106003 |
| `CMD-UNC-106003-05` | `ADD S1ARD` | ADD | S1ARD | ★S1模式接入限制参数（MME；E-UTRAN；★无 CARDTYPE，仅签约ARD/签约APN 两种控制方式；CAUSE 取 EPS_SERVICE_NOT_ALLOWED 等系列） | SUBRANGE, IMSIPRE, BEGIMSI, ENDIMSI, APNNI, ARD, CTRLTYPE, CAUSE, SDCAUSE | EV-FK-106003 |

### 1.7 GWFD-010151 接入控制（UDG）（U面带宽流控，2个核心）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-010151-01` | `SET APNQOSATTR` | SET | APNQOSATTR | ★APN级QoS带宽控制（UDG U面；★CARSHAPESWUL/DL=INHERIT/ENABLE/DISABLE 三态开关 + CARSHAPEUL/DL=CAR/SHAPE 二选；★与 C 面接入权限机制不同：C 面 = UNC 侧接入控制，U 面 = UDG 侧带宽流控，非 C-U 对称；初始值 INHERIT/NULL） | APN, CARSHAPESWUL, CARSHAPEUL, CARSHAPESWDL, CARSHAPEDL | EV-FK-010151 |
| `CMD-UDG-010151-02` | `ADD APN`（簇A引用） | ADD | APN | APN 实例（前置依赖；归簇A 04-cluster-A，本文件不重复抽参数，仅 §6 标注 operates_on） | 见簇A | EV-FK-010151 |

---

## 2. ConfigObject 实例化（共 24 个）

### 2.1 WSFD-107010 UPF选择 — NF 概述与属性族（9个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-PNFPROFILE` | PNFPROFILE | 共用 | entity | NFINSTANCEID | NFTYPE(含NfUPF), NFSTATUS, FQDN, IPADDRESSTYPE, IPV4/V6ADDRESS1~4, PORT, CAPACITY, PRIORITY, LOAD, LOCALITY | **被 PNFDNN/PNFNS/PNFDNAI/PNFUPFINFO/PNFSMFSERAREA/PNFTAI/PNFTAIRANGE/UPNODE/UPBINDS11/UPBINDGNGP refers_to** |
| `OBJ-PNFDNN` | PNFDNN | 共用 | entity | INDEX, NFINSTANCEID | DNN, PNFNSINDEX, PDUSESSIONTYPE, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY, ISLOCKED | refers_to PNFPROFILE（NFINSTANCEID 关联）；refers_to PNFNS（PNFNSINDEX 关联） |
| `OBJ-PNFNS` | PNFNS | 共用 | entity | INDEX, NFINSTANCEID | SST, SD, NSDESCRIPTION | refers_to PNFPROFILE；被 PNFDNN/PNFDNAI/PNFSMFSERAREA/PNFTAI/PNFTAIRANGE PNFNSINDEX 反向引用 |
| `OBJ-PNFDNAI` | PNFDNAI | 共用 | entity | INDEX, NFINSTANCEID | DNAI, PNFDNNINDEX, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY, ISLOCKED | refers_to PNFPROFILE；refers_to PNFDNN（PNFDNNINDEX） |
| `OBJ-PNFUPFINFO` | PNFUPFINFO | UNC | entity | NFINSTANCEID | IWKEPSIND, PDUSESSIONTYPE | refers_to PNFPROFILE |
| `OBJ-PNFSMFSERAREA` | PNFSMFSERAREA | 共用 | entity | NFINSTANCEID, SMFSERVINGAREA | PNFNSINDEX, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY | refers_to PNFPROFILE；被 LOCBINDAREA.AREANAME 反向引用（SMFSERVINGAREA=AREANAME） |
| `OBJ-PNFTAI` | PNFTAI | 共用 | entity | NFINSTANCEID, TAI | PNFNSINDEX, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY, BINDNWDAFINFOID | refers_to PNFPROFILE |
| `OBJ-PNFTAIRANGE` | PNFTAIRANGE | 共用 | entity | INDEX, NFINSTANCEID | MCC, MNC, QUERYTYPE, RANGESTART/RANGEEND/PATTERN, PNFNSINDEX, PRISWITCH, PRIORITY, CAPSWITCH, CAPACITY, BINDNWDAFINFOID | refers_to PNFPROFILE |
| `OBJ-UPNODE` | UPNODE | UNC | entity | NFINSTANCENAME | LOCATION(Local/Central/CentralOnly), UPFUNCTION, LOCK, APSAMIGFUNC, ADDRALLOCMODE, SHAREDUPFSW, VPNNAME, SUPULCLBPONLY, SUPATSSS, IPV6NDPLCY, IOSWITCH, NFDESCNAME, CAMPUSSW, ULCLFWDTNLSW, PDUESTWITHOUTN9, NGLANSW, PSACOMBINEULCL, MBSSW, SUPINTELLISRV, PATHMIGSW, TOPATHMIGSW, PATHMIGTIMER, UEIPNATFUNC, PROXYUPFS8USW, QOSANASW, TOHPSASW, SILENTSIGMIGSW, PATHMIGEXT | refers_to PNFPROFILE（NFINSTANCENAME = NFINSTANCEID）；refers_to CPPOINT（VPNNAME） |

### 2.2 WSFD-107010 UPF选择 — 位置/接口绑定族（5个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-UPAREA` | UPAREA | UNC | entity | AREANAME | AREATYPE(S1TAI/N2TAI/LAI) | 被 UPAREABINDN2TAI/LOCBINDAREA.AREANAME refers_to；被 PNFSMFSERAREA.SMFSERVINGAREA 关联 |
| `OBJ-UPAREABINDN2TAI` | UPAREABINDN2TAI | UNC(SMF) | binding | AREANAME | N2BEGINTAI, N2ENDTAI | refers_to UPAREA（AREANAME） |
| `OBJ-LOCBINDAREA` | LOCBINDAREA | UNC | binding | LOCALITY, AREANAME | — | refers_to PNFPROFILE（LOCALITY）；refers_to PNFSMFSERAREA/UPAREA（AREANAME） |
| `OBJ-UPBINDS11` | UPBINDS11 | UNC(SGW-C) | binding | NFINSTANCENAME, S11IPTYPE | S11IPV4, S11IPV6, PRIORITY | refers_to PNFPROFILE（NFINSTANCENAME）；refers_to GTPCLEGRPMEM（S11 口地址） |
| `OBJ-UPBINDGNGP` | UPBINDGNGP | UNC(GGSN/PGW-C) | binding | NFINSTANCENAME, GNGPIPTYPE | GNGPIPV4, GNGPIPV6, PRIORITY | refers_to PNFPROFILE（NFINSTANCENAME） |

### 2.3 WSFD-107010 UPF选择 — 策略开关族（4个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-UPSELECTPRI` | UPSELECTPRI | UNC | entity | — | FIRSTPRIORITY, SECONDPRIORITY, THIRDPRIORITY（Combined/LocS11Priority/Load） | governs UPF 选择流程 |
| `OBJ-UPSELECTFLAG` | UPSELECTFLAG | UNC | entity | — | 15 开关（N3UPFAPNFLAG/ULISGWFLAG/AMBRUPFFLAG/PRIORITYFLAG/LOCALITYFLAG/PSAPOSPRIFLAG/LOADFLTFLAG 等） | activates PNF 系列优先级（PRIORITYFLAG=ENABLE 时 PRIORITY/CAPACITY 生效） |
| `OBJ-APNUPSELPLY` | APNUPSELPLY | UNC | entity | APN | PSAPOSPRIFLAG, ULISGWFLAG, SHAREDPRIFLAG, PRIORITYFLAG, COMBINEPRISTG, COMBINEDSELSTG, LOCS11SELSTG | belongs_to APN（覆盖全局 UPSELECTFLAG） |
| `OBJ-UPLOADBALANCE` | UPLOADBALANCE | UNC | entity | — | LOADCTRLFLG, LIGHTLOAD, HEAVYLOAD, OVERLOADCTRLFLG | governs UPF 负载均衡（处理 UPF 上报 LCI/OCI） |

### 2.4 WSFD-010202 对等网元选择 — DNS 简化族（3个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-AREADNS` | AREADNS | UNC(SGSN/MME) | entity | DNTYPE, LAC/RAC/TAC（条件） | LACRANGE, RACRANGE, TACRANGE, UUT, ZONESW, ZONENAME, ZONELOC | 简化 IPV4DNSH/DNSN 配置（位置区域→域名映射） |
| `OBJ-IPV4DNSH` | IPV4DNSH | UNC(SGSN/MME) | entity | HSINDEX, HOSTNAME, ADDRSECTION | IPV4ADDR1~8, PRIORITY1~8, WEIGHT1~8 | 被 DNSN.HSINDEX refers_to |
| `OBJ-DNSN` | DNSN | UNC(SGSN/MME) | entity | FQDN, HSINDEX, ENTITY, INTYPE | S5PROTOCOL, S8PROTOCOL, UEUSGTYPEPLCY, UEUSGTYPEGPID, DCNR, SMF, PRIORITY, WEIGHT, DESC | refers_to IPV4DNSH（HSINDEX） |

### 2.5 WSFD-106003 用户接入控制（AMF）（2个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-NGMMSUBDATA` | NGMMSUBDATA | UNC(AMF) | entity | SUBRANGE, IMSIPRE/IMSI | RATRESTRICT, CORERESTRICT, RFSPINDEX, NIM, DRX, RFSPPRI, UEAMBRULK/DLK, EXRATRESTRICT, PRIMRATRESTRICT, SECRATRESTRICT | —（AMF 本地配置，优先于签约） |
| `OBJ-NGMMPROCTRL` | NGMMPROCTRL | UNC(AMF) | entity | PROT | 60+ 拒绝原因值参数（AUSF/AIR/AUTH/UDM/OTHER_PROC/CAG/SMC/PCF 系列） | governs AMF MM 流程拒绝原因值下发 |

### 2.6 WSFD-106003 用户接入控制（SGSN/MME）— ARD 族（3个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-GBARD` | GBARD | UNC(SGSN) | entity | SUBRANGE, IMSIPRE/BEGIMSI+ENDIMSI | APNNI, CARDTYPE, ARD, CTRLTYPE, CAUSE, SDCAUSE | —（GERAN 接入限制） |
| `OBJ-IUARD` | IUARD | UNC(SGSN) | entity | SUBRANGE, IMSIPRE/BEGIMSI+ENDIMSI | APNNI, CARDTYPE, ARD, CTRLTYPE, CAUSE, SDCAUSE | —（UTRAN 接入限制） |
| `OBJ-S1ARD` | S1ARD | UNC(MME) | entity | SUBRANGE, IMSIPRE/BEGIMSI+ENDIMSI | APNNI, ARD, CTRLTYPE, CAUSE, SDCAUSE | —（E-UTRAN 接入限制；★无 CARDTYPE） |

### 2.7 GWFD-010151 接入控制（UDG）（1个核心）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-APNQOSATTR` | APNQOSATTR | UDG | entity | APN | CARSHAPESWUL(INHERIT/ENABLE/DISABLE), CARSHAPEUL(CAR/SHAPE), CARSHAPESWDL, CARSHAPEDL | belongs_to APN；refers_to QOSSHAPE/QOSCAR（INHERIT 时继承全局） |

---

## 3. ConfigObject 间关系边（§11.7）

### 3.1 refers_to 边（核心，14条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| PNFDNN/PNFNS/PNFDNAI/PNFUPFINFO/PNFSMFSERAREA/PNFTAI/PNFTAIRANGE/UPNODE/UPBINDS11/UPBINDGNGP | `refers_to` | PNFPROFILE | PNF 系列命令的 NFINSTANCEID/NFINSTANCENAME 关联 PNFPROFILE.NFINSTANCEID（手册原文：取值一致时关联关系生效） |
| PNFDNN/PNFDNAI/PNFSMFSERAREA/PNFTAI/PNFTAIRANGE | `refers_to` | PNFNS | PNFNSINDEX 关联 PNFNS.INDEX（手册原文：INDEX 一致时 NFINSTANCEID 必须一致） |
| PNFDNAI | `refers_to` | PNFDNN | PNFDNNINDEX 关联 PNFDNN.INDEX |
| UPAREABINDN2TAI/LOCBINDAREA | `refers_to` | UPAREA | AREANAME 关联 UPAREA.AREANAME |
| LOCBINDAREA | `refers_to` | PNFPROFILE | LOCALITY 关联 PNFPROFILE.LOCALITY（手册：大小写不敏感） |
| LOCBINDAREA | `refers_to` | PNFSMFSERAREA | AREANAME 关联 SMFSERVINGAREA（手册：取值应一致） |
| UPBINDS11 | `refers_to` | GTPCLEGRPMEM | S11IPV4/S11IPV6 关联 GTPCLEGRPMEM 描述信息为 S11 接口的地址 |
| DNSN | `refers_to` | IPV4DNSH | HSINDEX 关联 IPV4DNSH.HSINDEX（手册：必须先由 ADD IPV4DNSH 定义） |
| APNQOSATTR | `refers_to` | QOSSHAPE/QOSCAR | INHERIT 时继承 SET QOSSHAPE/SET QOSCAR 全局配置（手册：SET QOSSHAPE 优先级高于 SET QOSCAR） |

### 3.2 belongs_to 边（2条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| APNUPSELPLY | `belongs_to` | APN | APN 粒度 UP 选择策略归属 APN（手册：ADD APN 时自动建初始记录） |
| APNQOSATTR | `belongs_to` | APN | APN 级 QoS 带宽控制归属 APN |

### 3.3 depends_on 边（核心约束，5条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| PNFDNN | `depends_on` | PNFPROFILE | ADD PNFDNN 前必须 ADD PNFPROFILE（NFINSTANCEID 关联） |
| PNFDNAI | `depends_on` | PNFDNN | ADD PNFDNAI 的 PNFDNNINDEX 必须引用已存在的 ADD PNFDNN |
| LOCBINDAREA | `depends_on` | UPAREA + PNFSMFSERAREA | LOCBINDAREA.AREANAME 必须在 UPAREA 中事先配置，且与 PNFSMFSERAREA.SMFSERVINGAREA 一致 |
| UPAREABINDN2TAI | `depends_on` | UPAREA | ADD UPAREABINDN2TAI 前必须 ADD UPAREA（AREANAME 对应 AREATYPE=N2TAI） |
| IPV4DNSH | `depends_on`（被引用） | DNSN | ADD DNSN 前必须 ADD IPV4DNSH（HSINDEX 引用） |

### 3.4 activates / governs 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| UPSELECTFLAG.PRIORITYFLAG | `activates` | PNF 系列 PRIORITY/CAPACITY | ★手册原文：UPSELECTFLAG.PRIORITYFLAG=ENABLE 后，PNFPROFILE/PNFDNN/PNFTAI/PNFTAIRANGE/PNFSMFSERAREA/PNFDNAI 的 PRIORITY（优先级）和特定 CAPACITY（容量）才生效 |
| UPSELECTFLAG.LOCALITYFLAG | `activates` | LOCBINDAREA | ★手册原文：SET UPSELECTFLAG.LOCALITYFLAG=ENABLE 时 LOCBINDAREA 生效 |
| NGMMSUBDATA | `governs`（优先级） | UE 签约数据 | ★手册原文：AMF 本地配置的接入和移动性签约数据优先级高于用户签约 |

---

## 4. CommandRule 实例化（本簇相关，9条）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-107010-01` | UPF 选择三轮筛选次序 | `process_rule` | explicit | config | command | SET UPSELECTPRI / SET UPSELECTFLAG | ★手册原文：UPF 选择分三轮——第一轮必选条件（DNN/切片/DNAI/位置特征/接口能力/EPS互通/位置区/S11/GnGp-S5S8 间无优先级，全不满足则选择失败）→ 第二轮优选条件（合一UPF/位置区或S11/优先级，由 SET UPSELECTPRI 排序）→ 第三轮负载+权重（多 UPF 满足时按权重选择）。三轮顺序固定不可调换 | 跳过必选条件直接优选导致选择结果非预期 | critical | EV-FK-107010 |
| `CR-107010-02` | PNF 系列 PRIORITY/CAPACITY 依赖 PRIORITYFLAG 开关 | `parameter_dependency` | explicit | config | parameter | PNFPROFILE/PNFDNN/PNFDNAI/PNFSMFSERAREA/PNFTAI/PNFTAIRANGE 的 PRIORITY/CAPACITY | ★手册原文：基于 PNFPROFILE/PNFDNN/PNFTAI/PNFTAIRANGE/PNFSMFSERAREA/PNFDNAI 的 UPF 优先级和特定容量，需要在 UPSELECTFLAG.PRIORITYFLAG=ENABLE（或 APNUPSELPLY.PRIORITYFLAG=ENABLE）后才生效；CAPSWITCH=SPECIFIC 时 CAPACITY 生效前提也是 PRIORITYFLAG=ENABLE | 优先级/容量配置不生效，UPF 选择忽略配置 | critical | EV-FK-107010 |
| `CR-107010-03` | SET UPSELECTPRI 三级优先级不可相同 | `semantic_rule` | explicit | config | parameter | SET UPSELECTPRI.FIRSTPRIORITY/SECONDPRIORITY/THIRDPRIORITY | ★手册原文：第一优先级、第二优先级与第三优先级不能存在相同值；取值 Combined/LocS11Priority/Load | 配置失败或选择逻辑混乱 | warning | EV-FK-107010 |
| `CR-107010-04` | ADD UPNODE 高危：SUPULCLBPONLY/LOCATION 影响 I-UPF 选择 | `runtime_check_rule` | explicit | restriction | parameter | ADD UPNODE.SUPULCLBPONLY / LOCATION | ★手册原文：SUPULCLBPONLY=ENABLE 或 LOCATION=LOCAL 时该 UPF 不能作为 I-UPF；非 UL CL 场景下须确保某位置区存在 LOCATION≠LOCAL 且 SUPULCLBPONLY=DISABLE 的 UPF，否则 UPF 选择失败 | UPF 选择失败（4G↔5G 注册/切换失败） | critical | EV-FK-107010 |
| `CR-010202-01` | ADD AREADNS DNTYPE 决定条件可选参数 | `parameter_dependency` | explicit | config | command | CMD-UNC-010202-01 (ADD AREADNS) | ★手册原文：DNTYPE 决定 LAC/LACRANGE/RAC/RACRANGE/TAC/TACRANGE/UUT 哪些为条件必选/可选；如 SGSN_RAI→LAC+RAC+RACRANGE，MME_TAI→TAC+TACRANGE，MSC_LAI→LAC+LACRANGE，*_UUT→+UUT；LACRANGE/TACRANGE/RACRANGE 必须 ≥ 起始值且不与原有重叠；同时匹配 *_RAI 与 *_LAI 时以 RAI 为准 | DNTYPE 与位置参数不匹配导致命令失败或域名简化失效 | warning | EV-FK-010202 |
| `CR-010202-02` | ADD AREADNS ZONESW=YES 时 ZONENAME 必填 | `parameter_dependency` | explicit | config | parameter | ADD AREADNS.ZONESW / ZONENAME | ★手册原文：ZONESW=YES 时将 RAI/LAI/TAI 集合映射到 ZONENAME（区域名称）定制 DNS 域名，ZONENAME 条件必选；ZONELOC=APNNI_ZONE_APNOI（默认）/ZONE_APNNI_APNOI 决定 ZONENAME 在域名中位置 | ZONESW=YES 缺 ZONENAME 导致命令失败 | warning | EV-FK-010202 |
| `CR-106003-01` | AMF 本地配置优先于签约（NGMMSUBDATA） | `semantic_rule` | explicit | config | relation | OBJ-NGMMSUBDATA ↔ UE 签约数据 | ★手册原文：AMF 本地配置的接入和移动性签约数据优先级高于用户签约；多条记录用户群重叠时 AMF 以号段最长匹配为准；匹配优先级 IMSI > IMSI_PREFIX > FOREIGN/HOME_USER > ALL_USER；签约或本地配置为空表示不限制 | 本地配置覆盖签约，误配导致用户误拒/误放 | critical | EV-FK-106003 |
| `CR-106003-02` | GBARD/IUARD 卡类型控制仅 GERAN/UTRAN 适用（子特性B依赖鉴权） | `scope_rule` | explicit | restriction | command | CMD-UNC-106003-03/04 (ADD GBARD/IUARD).CARDTYPE | ★手册原文：CARDTYPE（SIM/USIM）仅 GBARD（GERAN）/IUARD（UTRAN）有，S1ARD（E-UTRAN）无 CARDTYPE；卡类型控制子特性仅适用于 GERAN/UTRAN 接入用户；且用户不鉴权时卡类型限制判断不生效（依赖 WSFD-010301 鉴权特性） | S1ARD 误配 CARDTYPE 失败；不鉴权用户卡类型控制无效 | warning | EV-FK-106003 |
| `CR-010151-01` | SET APNQOSATTR CARSHAPE 依赖 CARSHAPESW 开关 | `parameter_dependency` | explicit | config | parameter | CMD-UDG-010151-01 (SET APNQOSATTR).CARSHAPEUL/DL | ★手册原文：CARSHAPEUL 在 CARSHAPESWUL=ENABLE 时必选（CAR/SHAPE 二选一），CARSHAPEDL 在 CARSHAPESWDL=ENABLE 时必选；CARSHAPESW=INHERIT 时继承 SET QOSSHAPE/QOSCAR 全局（QOSSHAPE 优先）；CAR=超出丢弃，SHAPE=令牌桶缓存整形；U 面带宽流控与 C 面接入权限机制不同（非 C-U 对称） | CARSHAPESW=ENABLE 缺 CARSHAPE 导致命令失败 | warning | EV-FK-010151 |

---

## 5. MMLCommand 关键参数集（核心命令全参数）

> **Schema 参考**：§11.4 CommandParameter。`required_mode` 取值 `required / optional / conditional_required`。本节抽取簇F 核心命令的全量参数（UPF 选择 18 + 对等网元 3 + AMF 接入控制 2 + ARD 族 3 + APNQOSATTR 1 = 27 命令）。ADD NGMMSUBDATA/SET NGMMPROCTRL/ADD UPNODE 参数众多，本节给出关键参数表；全量参数见 §9 抽取核对清单的来源手册。

### 5.1 ADD PNFPROFILE（UPF选择核心，16 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| NFINSTANCEID | string | 1~36（uuid 或 ≤18 非纯数字/十六进制），不区分大小写 | `required` | 无 | NF 实例标识（建议 UUID 格式）；★被 PNF 系列命令关联 |
| NFTYPE | enum | 28 类型（NfInvalid/NfNRF/NfUDM/NfAMF/NfSMF/NfAUSF/NfNEF/NfPCF/NfSMSF/NfNSSF/NfUDR/NfLMF/NfGMLC/Nf5G_EIR/NfSEPP/**NfUPF**/NfN3IWF/NfAF/NfUDSF/NfBSF/NfCHF/NfCUSTOM_OCS/NfSCP/NfPCSCF/NfMBSMF/NfUDN/NfNWDAF） | `required` | 无 | NF 类型；★UPF 选择用 NfUPF |
| NFSTATUS | enum | Invalid/Registered/Suspend/DeRegistered/UnDiscoverable | `optional` | Registered | NF 状态；非 Registered 时 NF 选择不会被选中 |
| FQDN | string | 0~255，不区分大小写 | `conditional_required` | 无 | 域名；★NFTYPE=NfUPF 时条件必选；不允许空格 |
| INTERPLMNFQDN | string | 0~255 | `optional` | 无 | PLMN 间域名（跨 PLMN NF 发现） |
| IPADDRESSTYPE | enum | IPTypeV4/IPTypeV6/IPTypeV4V6 | `optional` | 无 | IP 地址类型；★NFTYPE=NfUPF 时不支持 IPV4V6 双栈，IPV4/IPV6 只能加一个 |
| IPV4ADDRESS1~4 | IPv4 | IPv4 类型（A/B/C 类及 0.0.0.0） | `conditional_required` | 无 | IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时 1 必填，2~4 可选 |
| IPV6ADDRESS1~4 | IPv6 | 全球单播（禁环回/链路本地/组播） | `conditional_required` | 无 | IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时 1 必填，2~4 可选 |
| PORT | int | 0~65535 | `optional` | 无 | 端口号；不配 IP 则不应配本参数 |
| CAPACITY | int | 0~65535 | `optional` | 100 | 相对权重（容量）；值越大容量越大；0 时通常不被选中 |
| PRIORITY | int | 0~65535 | `optional` | 无 | 优先级；★值越小优先级越高；NfUPF 时仅 PRIORITYFLAG=ENABLE 生效 |
| LOAD | int | 0~100 | `optional` | 无 | 负载；值越大负载越大 |
| LOCALITY | string | 0~150（建议字母/数字/-/_） | `optional` | 无 | 位置信息；★中国区建议点分格式「大区.数据中心.资源池」；被 LOCBINDAREA 关联 |
| NFDESCNAME | string | 0~255 | `optional` | 无 | NF 描述名称（唯一值）；★被 UPNODE.NFDESCNAME 关联 |
| SCHEME | enum | HTTP/HTTPS | `conditional_required` | HTTPS | NFTYPE=NfSEPP/NfSCP 时条件可选；本端对端须一致 |

### 5.2 ADD PNFDNN（9 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| INDEX | int | 0~4294967295 | `required` | 无 | DNN 索引（不可重复，建议从 0 起） |
| NFINSTANCEID | string | 0~38 | `required` | 无 | NF 实例标识；★与 PNFPROFILE 一致时关联生效 |
| DNN | string | 0~66，不区分大小写 | `required` | 无 | 数据网络名 |
| PNFNSINDEX | int | 0~4294967295 | `optional` | 0 | 对端NF切片索引；0=不属于切片；UPF/SMF 不建议 0 |
| PDUSESSIONTYPE | 位域 | IPV4-X&IPV6-X&IPV4V6-X&UNSTRUCTURED-X&ETHERNET-X | `optional` | 全 1（支持所有） | PDU 会话类型；全 0=支持所有 |
| PRISWITCH | enum | INHERIT/SPECIFIC | `optional` | INHERIT | 优先级功能开关；SPECIFIC 时 PRIORITY 生效 |
| PRIORITY | int | 0~65535 | `conditional_required` | 无 | PRISWITCH=SPECIFIC 时必填；值越小优先级越高 |
| CAPSWITCH | enum | INHERIT/SPECIFIC | `optional` | INHERIT | 容量功能开关；★SPECIFIC 时 CAPACITY 生效前提 PRIORITYFLAG=ENABLE |
| CAPACITY | int | 0~65535 | `conditional_required` | 无 | CAPSWITCH=SPECIFIC 时必填；相对权重 |
| ISLOCKED | enum | TRUE/FALSE | `optional` | 无 | TRUE=锁定，不参与服务发现 |

### 5.3 ADD AREADNS（对等网元选择核心，11 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| DNTYPE | enum | 14 类型（SGW_RAI/SGW_TAI/SGSN_RAI/MME_TAI/GGSN-PGW_RAI/PGW_TAI/MSC_RAI/MSC_LAI/GGSN-PGW_LAI/SGW_LAI/SGSN_LAI/MME_TAI_UUT/SGW_TAI_UUT/MMEGI_TAI_UUT） | `required` | 无 | ★域名类型；决定后续位置参数条件必选 |
| LAC | hex | 0x0000~0xFFFF | `conditional_required` | 无 | DNTYPE 含 _RAI/_LAI 时条件必选；位置区域码 |
| LACRANGE | hex | 0x0000~0xFFFF | `conditional_optional` | 无 | DNTYPE 含 _LAI 时显示；★必须 ≥ LAC 且不与原有重叠 |
| RAC | hex | 0x00~0xFF | `conditional_required` | 无 | DNTYPE 含 _RAI 时条件必选；路由区域码 |
| RACRANGE | hex | 0x00~0xFF | `conditional_optional` | 无 | DNTYPE 含 _RAI 时显示；★必须 ≥ RAC 且同一 LAC 下不重叠 |
| TAC | hex | 0x0000~0xFFFF | `conditional_required` | 无 | DNTYPE 含 _TAI 时条件必选；跟踪区域码 |
| TACRANGE | hex | 0x0000~0xFFFF | `conditional_optional` | 无 | DNTYPE 含 _TAI 时显示；★必须 ≥ TAC 且不重叠 |
| UUT | int | 0~255 | `conditional_required` | 无 | DNTYPE 含 _UUT 时条件必选；UE USAGE TYPE |
| ZONESW | enum | NO/YES | `conditional_optional` | NO | 定制区域标识；YES=映射到 ZONENAME |
| ZONENAME | string | 1~32（字母/数字/-/.） | `conditional_required` | 无 | ZONESW=YES 时条件必选；区域名称 |
| ZONELOC | enum | APNNI_ZONE_APNOI/ZONE_APNNI_APNOI | `conditional_optional` | APNNI_ZONE_APNOI | ZONESW=YES 时显示；ZONENAME 在域名中位置 |

### 5.4 ADD IPV4DNSH（7 类参数组）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| HSINDEX | int | 1~1024 | `required` | 无 | 主机名索引 |
| HOSTNAME | string | 1~255（字母/数字/-/.） | `required` | 无 | 主机名；不能以 . 开始/结束；SGW 格式 `<APNNI>.MNC<MNC>.MCC<MCC>.GPRS` |
| ADDRSECTION | enum | SECTION1~SECTION8 | `required` | 无 | 地址区间号；8 区间×8 地址=64 IP |
| IPV4ADDR1~8 | IPv4 | 1.0.0.0~255.255.255.254（A/B/C 类，禁组播/环回） | `optional` | 无 | IPv4 地址 1~8 |
| PRIORITY1~8 | int | 0~255 | `optional` | 127 | 优先级；越小越高 |
| WEIGHT1~8 | int | 1~255 | `optional` | 127 | 权重；越大选中概率越高 |

### 5.5 ADD DNSN（13 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| FQDN | string | 1~255（字母/数字/-/.） | `required` | 无 | FQDN；构建格式见手册（TAC-LB/HB.TAC/MMEC.MMEGI/APN） |
| HSINDEX | int | 1~2048 | `required` | 无 | 主机名索引；★必须先由 ADD IPV4DNSH/IPV6DNSH 定义 |
| ENTITY | enum | SGSN/GGSN/MME/SGW/PGW/MSC/IWS/AMF | `required` | 无 | 网元类型 |
| INTYPE | enum | Gn/Gp/S3/S4/S5/S8/S10/S11/S16/Sv/S102/Sdup/N26 | `required` | 无 | 接口类型；★与 ENTITY 有约束（如 MSC→Sv，IWS→S102） |
| S5PROTOCOL | enum | GTP/PMIP/GTP_PMIP | `optional` | GTP | ENTITY=SGW/PGW 时有效 |
| S8PROTOCOL | enum | GTP/PMIP/GTP_PMIP | `optional` | GTP | ENTITY=SGW/PGW 时有效 |
| UEUSGTYPEPLCY | enum | NO/YES | `optional` | NO | UE USAGE TYPE 策略；DECOR 时 YES |
| UEUSGTYPEGPID | int | 0~1023 | `conditional_required` | 无 | UEUSGTYPEPLCY=YES 时生效 |
| DCNR | enum | NO/YES | `optional` | NO | 支持DCNR；YES 时不支持 SGSN/MSC/IWS |
| SMF | enum | NO/YES | `optional` | NO | 融合PGW-C/SMF；★仅 ENTITY=PGW 时可 YES |
| PRIORITY | int | 0~65535 | `optional` | 0 | 优先级；越小越高 |
| WEIGHT | int | 0~65535 | `optional` | 100 | 权重；越大选中概率越高 |
| DESC | string | 0~32 | `optional` | 无 | 描述 |

### 5.6 ADD NGMMSUBDATA（AMF 接入控制核心，17 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| SUBRANGE | enum | ALL_USER/HOME_USER/FOREIGN_USER/IMSI_PREFIX/IMSI | `required` | 无 | ★用户范围；匹配优先级 IMSI>IMSI_PREFIX>FOREIGN/HOME>ALL |
| IMSIPRE | string | 5~15 数字 | `conditional_required` | 无 | SUBRANGE=IMSI_PREFIX 时必填 |
| IMSI | string | 14~15 数字 | `conditional_required` | 无 | SUBRANGE=IMSI 时必填（全匹配） |
| RATRESTRICT | 位域 | EUTRA-X/NR-X/NR_REDCAP-X | `optional` | 全灰化（未生效） | 限制 RAT 类型；NR_RedCap 是 NR 子类型 |
| CORERESTRICT | 位域 | EPC-X/FIFTHGC-X | `optional` | 全灰化 | 限制核心网类型 |
| RFSPINDEX | int | 0~256 | `optional` | 0 | RFSP 索引；0=用签约值 |
| NIM | enum | MODE_A/MODE_B/MODE_C/MODE_D | `optional` | MODE_C | 3GPP 接入网络切片包含模式 |
| DRX | int | 0/32/64/128/256 | `optional` | 0 | 寻呼 DRX；0=无效 |
| RFSPPRI | enum | CFG_FIRST/SUB_FIRST | `optional` | CFG_FIRST | RFSP 数据优先级 |
| UEAMBRULK | int(kbps) | 0~4000000000 | `optional` | 无 | 上行 UE AMBR；0=不生效；否则取配置与签约最小值 |
| UEAMBRDLK | int(kbps) | 0~4000000000 | `optional` | 无 | 下行 UE AMBR；同上 |
| EXRATRESTRICT | enum | NOT_SUPPORT/CFG_ONLY | `optional` | 无 | 扩展RAT数据来源（仅测试） |
| PRIMRATRESTRICT | enum | E-UTRA/NR/NR_UNLICENSED/NR_LEO/NR_MEO/NR_GEO/NR_OTHERSAT | `conditional_optional` | 无 | EXRATRESTRICT=CFG_ONLY 时可选；主接入限制 |
| SECRATRESTRICT | enum | E-UTRA/NR/E-UTRA_UNLICENSED/NR_UNLICENSED | `conditional_optional` | 无 | EXRATRESTRICT=CFG_ONLY 时可选；辅助接入限制 |
| MPSMCSPRI | enum | CFG_FIRST/SUB_FIRST | `conditional_optional` | CFG_FIRST | SUBRANGE=IMSI 时可选；MPS/MCS 优先级（依赖 UEOVERLDCTRL.MPSMCSSWITCH=ON） |
| MPS | enum | NOT_SUPPORT/SUPPORT/NULL | `conditional_optional` | NULL | SUBRANGE=IMSI 时可选；本地 MPS |
| MCS | enum | NOT_SUPPORT/SUPPORT/NULL | `conditional_optional` | NULL | SUBRANGE=IMSI 时可选；本地 MCS |

### 5.7 ADD GBARD / IUARD（SGSN ARD 族，10 参数，结构相同）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| SUBRANGE | enum | ALL_USER/SPECIAL_IMSIPRE/SPECIAL_IMSI_RANGE | `required` | 无 | ★用户范围；IMSIPRE 与 IMSI_RANGE 互斥不可混用；匹配优先 IMSIPRE/IMSI_RANGE > ALL_USER |
| IMSIPRE | string | 1~15 数字 | `conditional_required` | 无 | SUBRANGE=SPECIAL_IMSIPRE 时生效；最长匹配 |
| BEGIMSI | string | 1~15 数字 | `conditional_required` | 无 | SUBRANGE=SPECIAL_IMSI_RANGE 时生效；起始 IMSI |
| ENDIMSI | string | 1~15 数字 | `conditional_required` | 无 | SUBRANGE=SPECIAL_IMSI_RANGE 时生效；终止 IMSI；★号段不可交叉/包含/重合 |
| APNNI | string | 1~62（字母/数字/-） | `optional` | * | APN 网络标识；*=所有 |
| CARDTYPE | 位域 | SIM-X&USIM-X | `optional` | 无 | ★卡类型；GBARD/IUARD 有，S1ARD 无；不鉴权时不生效 |
| ARD | enum | NO/YES | `optional` | NO | 启用签约 ARD；不建议与 APNNI 同时用 |
| CTRLTYPE | enum | ALLOW/REJECT | `required` | 无 | 控制类型；★仅用 ARD 时建议 ALLOW 防 APNNI 默认值影响 |
| CAUSE | enum | CUSTOMER_DEFINED/GPRS_SERVICE_NOT_ALLOWED/GPRS_NONGPRS_SRV_NOT_ALLOWED/PLMN_NOT_ALLOWED/LA_NOT_ALLOWED/ROAMING_NOT_ALLOWED_IN_LA/GPRS_SRV_NOT_ALLOWED_IN_PLMN/NO_SUITABLE_CELLS_IN_LA（GBARD/IUARD）；EPS 系列（S1ARD） | `optional` | NO_SUITABLE_CELLS_IN_LA / NO_SUITABLE_CELLS_IN_TA | 原因值 |
| SDCAUSE | int | 1~254 | `conditional_required` | 无 | CAUSE=CUSTOMER_DEFINED 时生效 |

> **S1ARD 差异**：无 CARDTYPE 参数（E-UTRAN 不支持卡类型控制）；CAUSE 取 EPS_SERVICE_NOT_ALLOWED/EPS_NONEPS_SRV_NOT_ALLOWED/PLMN_NOT_ALLOWED/TA_NOT_ALLOWED/ROAMING_NOT_ALLOWED_IN_TA/EPS_SRV_NOT_ALLOWED_IN_PLMN/NO_SUITABLE_CELLS_IN_TA 系列（参考 3GPP TS 24.301）。

### 5.8 SET APNQOSATTR（UDG U面带宽流控核心，5 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| APN | string | 1~63（-/数字/字母/.，不以 . 开头，无连续 ..） | `required` | 无 | APN 名称；引用 ADD APN 生成 |
| CARSHAPESWUL | enum | INHERIT/ENABLE/DISABLE | `optional` | 无（初始 INHERIT） | 上行 QoS 开关；INHERIT=继承 SET QOSSHAPE/QOSCAR（QOSSHAPE 优先） |
| CARSHAPEUL | enum | CAR/SHAPE | `conditional_required` | 无（初始 NULL） | ★CARSHAPESWUL=ENABLE 时必选；CAR=超出丢弃，SHAPE=令牌桶整形 |
| CARSHAPESWDL | enum | INHERIT/ENABLE/DISABLE | `optional` | 无（初始 INHERIT） | 下行 QoS 开关 |
| CARSHAPEDL | enum | CAR/SHAPE | `conditional_required` | 无（初始 NULL） | ★CARSHAPESWDL=ENABLE 时必选 |

### 5.9 SET UPSELECTFLAG（UPF选择 15 开关，节选核心 6 个，全量见手册）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| PRIORITYFLAG | enum | DISABLE/ENABLE | `optional` | 无（初始 DISABLE） | ★基于优先级优选UPF开关；ENABLE 后 PNF 系列 PRIORITY/CAPACITY 生效 |
| LOCALITYFLAG | enum | DISABLE/ENABLE | `optional` | 无（初始 DISABLE） | 位置区UPF优选开关；ENABLE 后 LOCBINDAREA 生效 |
| N3UPFAPNFLAG | enum | DISABLE/ENABLE | `optional` | 无（初始 DISABLE） | I-UPF 选择的 APN 开关；ENABLE 时未配 PNFDNN 的 UPF 不被选 |
| ULISGWFLAG | enum | DISABLE/ENABLE | `optional` | 无（初始 DISABLE） | 基于 ULI For SGW 选 SGW-U；ENABLE 时 ULI 空优先用 ULI For SGW |
| AMBRUPFFLAG | enum | DISABLE/ENABLE | `optional` | 无（初始 DISABLE） | AMBR 聚合 UPF 选择；同用户同 DNN 会话优选相同主锚点 |
| LOADFLTFLAG | enum | DISABLE/ENABLE | `optional` | 无（初始 ENABLE） | 基于负载优选 UPF |

> 其余 9 开关：UPFBLOCKFLAG(初始 ENABLE)/ROAMTYPEFLAG/NGLANUPFSELSW(初始 LOCALABILITY)/LEASEUPFFLAG(初始 ENABLE)/PSAPOSPRIFLAG/OVERLOADFLTFLAG/OVERLOADALWFLAG/LOCKAPNFLAG/ACCLOCKAPNFLAG，全量见 §9 手册。

### 5.10 SET UPSELECTPRI / SET APNUPSELPLY / SET UPLOADBALANCE（节选关键参数）

| 命令 | 关键参数 | 取值 | 默认/初始 |
|------|---------|------|----------|
| SET UPSELECTPRI | FIRSTPRIORITY/SECONDPRIORITY/THIRDPRIORITY | Combined/LocS11Priority/Load（三者不可相同） | Combined/LocS11Priority/Load |
| SET APNUPSELPLY | COMBINEPRISTG | COMBINEFIRST/PRIORITYFIRST | COMBINEFIRST |
| SET APNUPSELPLY | COMBINEDSELSTG | TAIPRI/APNPRI | TAIPRI |
| SET APNUPSELPLY | LOCS11SELSTG | PRIORITYFIRST/LOCS11FIRST | PRIORITYFIRST |
| SET UPLOADBALANCE | LOADCTRLFLG | DISABLE/ENABLE | DISABLE |
| SET UPLOADBALANCE | LIGHTLOAD/HEAVYLOAD | 0~100（LIGHT<HEAVY） | 45/75 |
| SET UPLOADBALANCE | OVERLOADCTRLFLG | DISABLE/ENABLE | DISABLE |

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

### 6.1 簇F 核心命令（25条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD PNFPROFILE (CMD-UNC-107010-01) | PNFPROFILE | UPF 选择核心（NF 概述，被 PNF 系列关联） |
| ADD PNFDNN (CMD-UNC-107010-02) | PNFDNN | 对端 DNN 信息 |
| ADD PNFNS (CMD-UNC-107010-03) | PNFNS | 对端切片信息 |
| ADD PNFDNAI (CMD-UNC-107010-04) | PNFDNAI | 对端 DNAI 信息 |
| ADD PNFUPFINFO (CMD-UNC-107010-05) | PNFUPFINFO | 对端 UPF 信息（EPS 互通） |
| ADD PNFSMFSERAREA (CMD-UNC-107010-06) | PNFSMFSERAREA | 对端 SMF 服务区域 |
| ADD PNFTAI (CMD-UNC-107010-07) | PNFTAI | 对端 TAI 信息 |
| ADD PNFTAIRANGE (CMD-UNC-107010-08) | PNFTAIRANGE | 对端 TAI 范围 |
| ADD UPNODE (CMD-UNC-107010-09) | UPNODE | UPF 节点特征 |
| ADD UPAREA (CMD-UNC-107010-10) | UPAREA | UPF 服务区 |
| ADD UPAREABINDN2TAI (CMD-UNC-107010-11) | UPAREABINDN2TAI | UPF 服务区绑定 5G TAI 范围 |
| ADD LOCBINDAREA (CMD-UNC-107010-12) | LOCBINDAREA | UPF 位置绑定优先服务区 |
| ADD UPBINDS11 (CMD-UNC-107010-13) | UPBINDS11 | SGW-U 绑定 S11 |
| ADD UPBINDGNGP (CMD-UNC-107010-14) | UPBINDGNGP | GGSN/PGW-U 绑定 GnGp/S5S8 |
| SET UPSELECTPRI (CMD-UNC-107010-15) | UPSELECTPRI | UPF 选择策略次序 |
| SET UPSELECTFLAG (CMD-UNC-107010-16) | UPSELECTFLAG | UPF 选择条件开关（15 开关） |
| SET APNUPSELPLY (CMD-UNC-107010-17) | APNUPSELPLY | APN 粒度 UP 选择策略 |
| SET UPLOADBALANCE (CMD-UNC-107010-18) | UPLOADBALANCE | UP 负载均衡 |
| ADD AREADNS (CMD-UNC-010202-01) | AREADNS | 位置区域 DNS 域名 |
| ADD IPV4DNSH (CMD-UNC-010202-02) | IPV4DNSH | IPv4 DNS Hostfile |
| ADD DNSN (CMD-UNC-010202-03) | DNSN | DNS NAPTR |
| ADD NGMMSUBDATA (CMD-UNC-106003-01) | NGMMSUBDATA | AMF 本地用户移动性管理参数 |
| SET NGMMPROCTRL (CMD-UNC-106003-02) | NGMMPROCTRL | 5G MM 流程控制参数 |
| ADD GBARD/IUARD/S1ARD (CMD-UNC-106003-03/04/05) | GBARD/IUARD/S1ARD | Gb/Iu/S1 模式接入限制 |
| SET APNQOSATTR (CMD-UDG-010151-01) | APNQOSATTR | APN 级 QoS 带宽控制（U 面） |

### 6.2 前置依赖命令（引用，非本簇拥有）

| MMLCommand | operates_on -> ConfigObject | 归属簇 | 说明 |
|------------|---------------------------|--------|------|
| ADD APN | APN | 簇A | APN 实例（GWFD-010151/WSFD-107010 SET APNUPSELPLY 引用） |
| SET QOSSHAPE / SET QOSCAR | QOSSHAPE/QOSCAR | UDG 全局 QoS | APNQOSATTR INHERIT 时继承 |
| ADD GTPCLEGRPMEM | GTPCLEGRPMEM | UNC 接口管理 | UPBINDS11 的 S11 口地址来源 |
| ADD CPPOINT | CPPOINT | UNC | UPNODE.VPNNAME 来源 |
| SET LICENSESWITCH | LICENSESWITCH | 平台服务 | WSFD-106003 SGSN/MME 激活开关（LKV2ARD02） |

---

## 7. CommandRule governs MMLCommand 边表（§11.6 反向）

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-107010-01 | SET UPSELECTPRI / SET UPSELECTFLAG（流程） | UPF 选择三轮筛选次序（必选→优选→负载权重） |
| CR-107010-02 | PNF 系列 PRIORITY/CAPACITY 参数 | 依赖 PRIORITYFLAG=ENABLE 才生效 |
| CR-107010-03 | SET UPSELECTPRI 三级优先级 | 不可相同 |
| CR-107010-04 | ADD UPNODE.SUPULCLBPONLY/LOCATION | 高危：影响 I-UPF 选择 |
| CR-010202-01 | ADD AREADNS（DNTYPE 与位置参数） | DNTYPE 决定条件可选参数 |
| CR-010202-02 | ADD AREADNS.ZONESW/ZONENAME | ZONESW=YES 时 ZONENAME 必填 |
| CR-106003-01 | OBJ-NGMMSUBDATA ↔ 签约 | AMF 本地优先于签约 |
| CR-106003-02 | ADD GBARD/IUARD.CARDTYPE | 卡类型控制仅 GERAN/UTRAN，依赖鉴权 |
| CR-010151-01 | SET APNQOSATTR.CARSHAPE | 依赖 CARSHAPESW=ENABLE；U面与C面机制不同 |

---

## 8. 使用实例脚本（保留手册/概述原文）

### 8.1 WSFD-107010 UPF选择（⚠️文档缺口·概述推导）

> **说明**：WSFD-107010 无激活文档。本实例由概述表2「SMF 下的 UPF 属性」+ 各手册使用实例组合，标注「概述推导」。

```
// [概述推导] 配置 UPF1（dnn1/dnn2/dnn3, SST=1/SD=010101, 合一UPF, 位置区0x0000-0x0009, 权重6）
ADD PNFPROFILE: NFINSTANCEID="UPF1_Instance", NFTYPE=NfUPF, NFSTATUS=Registered, FQDN="upf1.example.com", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="10.0.0.1", LOCALITY="DC1.BJ.Pool1", CAPACITY=6;
ADD PNFDNN: INDEX=1, NFINSTANCEID="UPF1_Instance", DNN="dnn1", PNFNSINDEX=1;
ADD PNFNS: INDEX=1, NFINSTANCEID="UPF1_Instance", SST=1, SD="010101";
ADD UPNODE: NFINSTANCENAME="UPF1_Instance", LOCATION=Central, UPFUNCTION=UlClAndBp, CAPACITY=6;

// [概述推导] 配置基于位置区优选 UPF（SET UPSELECTFLAG.LOCALITYFLAG=ENABLE + ADD LOCBINDAREA）
SET UPSELECTFLAG: LOCALITYFLAG=ENABLE;
ADD LOCBINDAREA: LOCALITY="DC1.BJ.Pool1", AREANAME="area01";

// [手册使用实例] 设置 UPF 选择策略次序（合一优先 → 位置区/S11 → 负载）
SET UPSELECTPRI: FIRSTPRIORITY=Combined, SECONDPRIORITY=LocS11Priority, THIRDPRIORITY=Load;

// [手册使用实例] 开启优先级优选（使 PNF 系列 PRIORITY 生效）
SET UPSELECTFLAG: PRIORITYFLAG=ENABLE;

// [手册使用实例] 开启 UPF 负载均衡（处理 UPF 上报 LCI/OCI）
SET UPLOADBALANCE: LOADCTRLFLG=ENABLE, LIGHTLOAD=45, HEAVYLOAD=75;
```

### 8.2 WSFD-010202 对等网元选择（来源：激活文档任务1/2/3）

```
// 任务1：选择SGSN（基于RAI→ZONE）
ADD IPV4DNSH: HSINDEX=1, HOSTNAME="ZONE.MNC123.MCC123.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="10.2.3.10";
ADD AREADNS: DNTYPE=SGSN_RAI, LAC="0x0001", RAC="0x01", RACRANGE="0x05", ZONESW=YES, ZONENAME="ZONE";

// 任务2：选择MME（基于TAI，无ZONESW）
ADD IPV4DNSH: HSINDEX=2, HOSTNAME="TOPON.MME-S10.MMEC02.MMEGI8001.MME.EPC.MNC000.MCC123.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="10.2.3.11";
ADD DNSN: FQDN="TAC-LB01.TAC-HB00.TAC.EPC.MNC123.MCC123.3GPPNETWORK.ORG", HSINDEX=2, ENTITY=MME, INTYPE=S10;
ADD AREADNS: DNTYPE=MME_TAI, TAC="0x0001", TACRANGE="0x0005";

// 任务3：选择MSC（基于LAI→ZONE）
ADD IPV4DNSH: HSINDEX=3, HOSTNAME="NODES.EPC.ENVID68.MNC003.MCC123.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="10.2.3.12";
ADD DNSN: FQDN="ZONE.EPC.MNC003.MCC123.3GPPNETWORK.ORG", HSINDEX=3, ENTITY=MSC, INTYPE=Sv;
ADD AREADNS: DNTYPE=MSC_LAI, LAC="0x0001", LACRANGE="0x0005", ZONESW=YES, ZONENAME="ZONE";
```

### 8.3 WSFD-106003 用户接入控制（AMF，来源：激活文档场景一/二）

```
// 场景一：所有用户拒绝接入5GC（CORERESTRICT=FIFTHGC-1）
ADD NGMMSUBDATA: SUBRANGE=ALL_USER, CORERESTRICT=FIFTHGC-1;
SET NGMMPROCTRL: PROT=OTHER_PROC, ACCRST=0;

// 场景二：IMSI前缀限制NR接入（RATRESTRICT=NR-1）
ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="123431234567890", RATRESTRICT=NR-1;
SET NGMMPROCTRL: PROT=OTHER_PROC, ACCRST=0;
```

### 8.4 WSFD-106003 用户接入控制（SGSN/MME，来源：激活文档脚本二/三/六）

```
// 打开 License 开关
SET LICENSESWITCH: LICITEM="LKV2ARD02", SWITCH=ENABLE;

// 脚本二：IMSI前缀拒绝SIM卡用户接入UTRAN（IUARD + CARDTYPE）
ADD IUARD: SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="12303001", APNNI="*", CARDTYPE=SIM-1, ARD=NO, CTRLTYPE=REJECT, CAUSE=GPRS_SERVICE_NOT_ALLOWED;

// 脚本三：IMSI前缀只允许SIM卡用户接入GERAN（GBARD + CARDTYPE）
ADD GBARD: SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="12303001", APNNI="*", CARDTYPE=SIM-1, ARD=NO, CTRLTYPE=ALLOW;

// 脚本六：IMSI前缀根据签约ARD允许接入E-UTRAN（S1ARD，无CARDTYPE）
ADD S1ARD: SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="12303001", APNNI="*", ARD=YES, CTRLTYPE=ALLOW;
```

### 8.5 GWFD-010151 接入控制（U面带宽流控，来源：激活文档）

```
// 增加APN实例（簇A）
ADD APN:APN="apn";

// 配置上下行CAR带宽控制（丢弃超出报文）
SET APNQOSATTR:APN="apn",CARSHAPESWUL=ENABLE,CARSHAPEUL=CAR,CARSHAPESWDL=ENABLE,CARSHAPEDL=CAR;
```

---

## 9. 抽取核对清单

### 9.1 配置类命令参数行数与来源手册路径

| 特性 | 命令 | 参数行数 | 来源手册路径（相对 `output/UNC 20.15.2 产品文档(裸机容器) 05/` 或 `output/UDG_Product_Documentation_CH_20.15.2/`） |
|------|------|---------|----------------------------------------------------------------|
| **WSFD-107010** | ADD PNFPROFILE | 16 | `OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md` |
| | ADD PNFDNN | 9 | `.../对端DNN信息管理/增加对端NF的DNN信息（ADD PNFDNN）_09654342.md` |
| | ADD PNFNS | 5 | `.../对端NF实例切片信息管理/增加对端NF的切片信息（ADD PNFNS）_09652622.md` |
| | ADD PNFDNAI | 9 | `.../对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md` |
| | ADD PNFUPFINFO | 3 | `.../对端NF UPF信息管理/增加对端UPF信息（ADD PNFUPFINFO）_09653643.md` |
| | ADD PNFSMFSERAREA | 7 | `.../对端SMF服务区管理/增加对端NF的SMF服务区域信息（ADD PNFSMFSERAREA）_09653019.md` |
| | ADD PNFTAI | 8 | `.../对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md` |
| | ADD PNFTAIRANGE | 13 | `.../对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md` |
| | ADD UPNODE | 28 | `.../PFCP接口管理/UP管理/UP节点管理/增加UPF节点（ADD UPNODE）_09652571.md` |
| | ADD UPAREA | 2 | `.../UP跟踪区管理/UP区域管理/增加UPF服务区（ADD UPAREA）_09652457.md` |
| | ADD UPAREABINDN2TAI | 3 | `.../TAI绑定UP区域/增加UPF服务区名称绑定的5G TAI范围（ADD UPAREABINDN2TAI）_09653098.md` |
| | ADD LOCBINDAREA | 2 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UPF选择管理/位置区域绑定本地优选名称/增加UPF位置信息与该UPF优先支持的服务区的绑定关系（ADD LOCBINDAREA）_09653286.md` |
| | ADD UPBINDS11 | 5 | `.../UPF选择管理/UPF绑定S11接口/增加SGW-U与SGW-C侧S11接口的绑定关系（ADD UPBINDS11）_09653045.md` |
| | ADD UPBINDGNGP | 5 | `.../UPF选择管理/UPF绑定GnGp或S5S8接口/增加GGSN与Gn_Gp接口或PGW-U与S5_S8接口的绑定关系（ADD UPBINDGNGP）_78029307.md` |
| | SET UPSELECTPRI | 3 | `.../UPF选择管理/UPF选择策略次序/设置UPF选择策略次序（SET UPSELECTPRI）_09652604.md` |
| | SET UPSELECTFLAG | 15 | `.../UPF选择管理/UPF选择条件开关/设置UPF选择条件开关（SET UPSELECTFLAG）_09652250.md` |
| | SET APNUPSELPLY | 8 | `.../UPF选择管理/APN粒度的UPF选择策略/设置APN粒度的UP选择策略（SET APNUPSELPLY）_96243087.md` |
| | SET UPLOADBALANCE | 4 | `.../UPF选择管理/UPF负载均衡/设置UP负载均衡功能（SET UPLOADBALANCE）_97782146.md` |
| **WSFD-010202** | ADD AREADNS | 11 | `OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/位置域名管理/增加位置区域DNS域名(ADD AREADNS)_72345559.md` |
| | ADD IPV4DNSH | 7（类） | `.../DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md` |
| | ADD DNSN | 13 | `.../DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md` |
| **WSFD-106003(AMF)** | ADD NGMMSUBDATA | 17 | `OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md` |
| | SET NGMMPROCTRL | 60+（PROT 14 流程 + 各流程拒绝原因值） | `.../移动性管理/MM流程管理/5G移动性管理流程控制参数/设置5G移动性管理流程控制参数（SET NGMMPROCTRL）_09652386.md` |
| **WSFD-106003(SGSN/MME)** | ADD GBARD | 10 | `OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/接入限制管理/Gb模式接入限制参数/增加Gb模式接入限制参数(ADD GBARD)_26305284.md` |
| | ADD IUARD | 10 | `.../Iu模式接入限制参数/增加Iu模式接入限制参数(ADD IUARD)_72345073.md` |
| | ADD S1ARD | 9（无CARDTYPE） | `.../S1模式接入限制参数/增加S1模式接入限制参数(ADD S1ARD)_26145478.md` |
| **GWFD-010151** | SET APNQOSATTR | 5 | `UDG.../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/流量管理/APN的QoS属性配置/设置ApnQosAttr配置（SET APNQOSATTR）_82837665.md` |
| **合计** | **27 命令** | **~270 参数行** | **27 命令全部手册定位成功** |

### 9.2 ⚠️手册未定位列表

| 命令 | 状态 | 原因 |
|------|------|------|
| —（无） | — | **簇F 全部 27 核心命令手册均定位成功，无手册未定位项** |

> **说明**：簇F 4 特性的全部核心配置命令（WSFD-107010 的 18 个 + WSFD-010202 的 3 个 + WSFD-106003 的 5 个 + GWFD-010151 的 1 个）MML 手册均已定位并抽取参数。MOD/RMV/LST 同族命令（AREADNS/IPV4DNSH/DNSN/GBARD/IUARD/S1ARD/APN/APNQOSATTR 的 MOD/RMV/LST）参数与 ADD 同构，本文件不重复抽取，按样板 §0.1 归类处理。

### 9.3 ★UPF选择文档缺口标注（WSFD-107010）

| 维度 | 状态 | 说明 |
|------|------|------|
| 特性概述文档 | ✅ 有（1篇） | `WSFD-107010 UPF选择_10789013.md`（含适用NF=SMF、定义、原理概述表1「UPF选择原则」+ 表2 UPF属性示例） |
| 激活文档 | ⚠️ **缺** | 无独立激活文档（同目录仅 1 篇概述） |
| 参考信息文档 | ⚠️ **缺** | 无独立参考信息文档（命令清单缺位） |
| **命令清单来源** | ✅ **概述表1 嵌入式引用** | ★概述 §原理概述 表1「UPF选择原则」每行对应一条「配置命令」并附 MML 手册相对路径（共 18 命令），等价于参考信息命令清单，本文件据此抽取 |
| **激活脚本来源** | ⚠️ **概述推导** | §8.1 由概述表2 UPF 属性示例 + 各手册使用实例组合，每行标注「[概述推导]」或「[手册使用实例]」 |
| 文档完整性结论 | ⚠️ **部分完整** | 命令/参数 100% 来自手册原文（零编造），但缺激活文档导致端到端配置脚本为概述推导，需后续补充激活文档复核 |

### 9.4 抽取统计

| 维度 | 数量 |
|------|------|
| 配置类命令（手册定位成功） | 27 |
| 配置类命令参数总行数 | ~270 |
| 查询类命令（MOD/RMV/LST 同族，本期略） | 14（AREADNS/IPV4DNSH/DNSN 各 MOD/RMV/LST=9 + GBARD/IUARD/S1ARD 各 MOD/RMV/LST=9 - 重复 -4 = 14） |
| ⚠️手册未定位命令 | 0 |
| ⚠️文档缺口特性 | 1（WSFD-107010，仅概述，无激活/参考信息） |
| ConfigObject | 24 |
| CommandRule | 9 |
| ConfigObject 关系边 | 24（refers_to 14 + belongs_to 2 + depends_on 5 + activates/governs 3） |
| operates_on 边 | 25（核心）+ 5（前置依赖引用） |
| 激活子场景脚本 | 5（UPF选择概述推导 / 对等网元3任务 / AMF接入控制 / SGSN-MME接入控制 / UDG带宽流控） |

---

> 本文件为簇F（网元选择+接入控制，4 特性）命令层抽取，严格对齐 `04-cluster-B-GWFD-010105.md` 样板 9 节结构。
> **★关键贡献**：①WSFD-107010 文档缺口完整标注（仅概述，命令清单来自概述表1嵌入式手册引用，激活脚本概述推导）；②WSFD-010202 AREADNS 14 种 DNTYPE 完整抽取（含 ZONESW/ZONENAME/ZONELOC 域名定制）；③WSFD-106003 AMF/SGSN-MME 两套接入控制完整建模（NGMMSUBDATA 本地优先于签约 + ARD 族卡类型控制仅 GERAN/UTRAN + S1ARD 无 CARDTYPE）；④GWFD-010151 U 面带宽流控（CARSHAPESW 三态 + CARSHAPE 二选）与 C 面接入权限机制差异标注（非 C-U 对称）；⑤建立 9 条特性级 CommandRule（含 UPF 三轮筛选次序、PNF 优先级依赖 PRIORITYFLAG、AMF 本地优先签约等关键约束）。
