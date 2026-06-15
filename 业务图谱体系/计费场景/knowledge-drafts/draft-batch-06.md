# Knowledge Draft - Batch 06: UNC初始配置与网络运维计费知识

> 来源: UNC 20.15.2 产品文档 - 初始配置 + 网络运维
> 提取日期: 2026-06-04
> 知识编号: K270 ~ K310

---

## 一、SMF公共配置与计费体系概述

### K270 - UNC计费功能四大分类
- 来源: 配置PCC策略和计费_31442453.md
- UNC SMF/PGW-C/GGSN支持四类计费相关功能:
  1. **预定义/本地PCC策略**: 根据用户签约属性、使用量、网络位置、业务类型等进行策略控制
  2. **内容计费**: 区分用户数据流中的业务类型，配以不同资费标准
  3. **融合计费(N40)**: UNC与CHF通过Nchf接口进行实时计费和后计费
  4. **离线+在线计费(Ga/Gy)**: UNC与CG通过Ga接口实现离线计费，与OCS通过Gy接口实现在线计费

### K271 - 计费系统对接总体架构（NF部署组合与接口模式）
- 来源: 配置到计费系统和策略控制网元的对接（Ga_Gy_N40_Gx_N7）_19247690.md
- 随5G网络演进，协议定义的策略控制功能由PCF完成（替代EPC的PCRF），5G计费由CHF完成，网络侧取消传统CG网元
- 不同NF部署组合对应的接口模式:

| NF部署 | 计费接口 | 策略接口 | 说明 |
|--------|---------|---------|------|
| SMF | GaGy | - | 通过Ga对接CG，Gy对接OCS（未完成融合改造） |
| SMF | Nchf | - | 通过N40对接CHF（完成融合改造） |
| SMF | - | Npcf | 仅5G SA，通过PCF做策略控制 |
| GGSN/PGW-C | GaGy | Gx或Npcf | 未完成融合改造，通过PCRF或PCF做策略 |
| GGSN/PGW-C | Nchf | Npcf | 完成融合改造 |
| GGSN/PGW-C/SMF | Nchf+GaGy | Npcf+Gx | 部分用户N40+部分用户Ga/Gy |
| SGW-C | GaGy | - | SGW-C目前仅使用GaGy接口模式 |

---

## 二、计费接口选择模式

### K272 - 计费接口选择三级优先级
- 来源: 配置计费和策略模式_67342025.md
- 计费接口选择有三级优先级（从高到低）:
  1. **基于用户漫游属性** (ADD ROAMCHGMODE) - 最高优先级
  2. **基于APN/DNN** (ADD APNCHGMODE) - 中等优先级
  3. **全局配置** (SET CHGMODE) - 最低优先级（兜底）
- 策略接口选择有两级优先级: 基于APN/DNN > 全局配置

### K273 - SET CHGMODE按终端和接入类型选择计费接口
- 来源: 配置计费和策略模式_67342025.md
- SET CHGMODE命令通过TMACCTYPE（终端和接入类型）参数区分不同场景:
  - **UE5G_RAT5G**: 5G终端接入5G网络（SMF场景，典型用NchfMode）
  - **UE5G_RAT4G**: 5G终端接入4G网络（PGW-C场景，可选NchfMode或GaGyMode）
  - **UENON5G_RAT4G**: 非5G终端接入4G网络（PGW-C场景，典型用GaGyMode）
  - **RAT2G/RAT3G**: 2G/3G接入（GGSN场景，典型用GaGyMode）
  - **RATNBIOT**: NB-IoT终端接入
  - **RATLTEM**: LTE-M终端接入
  - **NON_3GPP**: 非3GPP网络接入
- FORCED参数指定计费接口: NchfMode（融合计费）或GaGyMode（传统离线+在线）

### K274 - 5GS互操作指示(BY5GSIWKI)对计费接口的影响
- 来源: 配置计费和策略模式_67342025.md
- BY5GSIWKI参数控制是否根据对端携带的"5GS Interworking Indication"参数选择计费接口:
  - BY5GSIWKI=True时: 对端携带"5GS Interworking Indication"为1则选Nchf，为0或未携带则选GaGy
  - BY5GSIWKI=False时: 不根据互操作指示判断，直接使用FORCED指定的计费接口
- 典型用法: ADD APNCHGMODE中按APN级别配置，5G终端4G接入时根据互操作指示灵活选择

### K275 - V-SMF和I-SMF的计费模式
- 来源: 配置计费和策略模式_67342025.md
- SET CHGMODE中与SMF角色相关的参数:
  - **FORVSMFONLY**: UNC作为V-SMF时的计费模式，典型配置NchfMode
  - **ISMFCHGSW**: I-SMF是否支持计费，典型配置DISABLE（I-SMF不进行计费）

### K276 - 基于PCF实例标识决策计费/策略接口(ADD PCCCHGMODEBYPCFID)
- 来源: 配置计费和策略模式_67342025.md
- 当需要基于PCF实例标识调整用户最终使用的计费/策略接口时使用ADD PCCCHGMODEBYPCFID:
  - 以SET CHGMODE或ADD APNCHGMODE为初选结果
  - 在此基础上决策: 是否由N40回落GaGy，或由GaGy升级为N40
  - 策略接口类型: N7（5G PCF）或Gx（4G PCRF）
  - 计费接口类型: INHERIT（继承初选结果）或指定N40/GaGy

### K277 - SET POLICYMODE策略接口选择
- 来源: 配置计费和策略模式_67342025.md
- 策略接口选择命令SET POLICYMODE:
  - FORCED=Npcf: 使用5G PCF（N7服务化接口）
  - FORCED=Gx: 使用4G PCRF（Diameter接口）
  - PCFRESELBYPCFID: 是否基于PCF实例标识决策策略接口类型
- 典型配置: 5G终端4G接入和非5G终端4G接入用Npcf，2G/3G/NB-IoT/LTE-M/非3GPP用Gx

---

## 三、CG对接配置（Ga接口 - 离线计费）

### K278 - CG对接配置流程与关键命令
- 来源: 配置到CG的数据（GGSN_PGW-C_SMF）_67429269.md
- 适用场景: 运营商未完成融合计费接口改造，通过CG实现离线计费
- 接口: Ga接口（GTP'协议）
- 配置流程:
  1. 创建L3VPN实例（ADD L3VPNINST + ADD VPNINSTAF + MOD VPNINSTAF配置RD）
  2. 创建VPN实例（ADD VPNINST）
  3. 配置Ga集中点模式（SET CONCENPOINT: GACONCENMODE）
     - SINGLE_CONNECT: 默认模式
     - MULTI_PORT: 对端CG需要较多Ga链路时使用
  4. 配置Ga逻辑接口（ADD LOGICIP + ADD LOGICINF，IP+VPN必须一致）
  5. 配置CG信息（ADD CG: IPVERSION, IPV4ADDR, PORT, CDRTYPE, PRIORITY）
     - PRIORITY: CG优先级，数值越小优先级越高
  6. 配置GTP'消息控制（SET CDRTRANSFER）

### K279 - SET CDRTRANSFER话单发送参数
- 来源: 配置到CG的数据（GGSN_PGW-C_SMF）_67429269.md
- SET CDRTRANSFER关键参数:
  - **CGSELECTIONMODE**: CG负荷分担算法（如MSG_BASED_LB）
  - **RETRANSTIMES**: Echo和Data Record Transfer Request重传次数（默认3）
  - **RETRANSINTERVAL**: Data Record Transfer Request重传间隔秒数（默认2）
  - **NARESTRANSINTVL**: Node Alive消息重传间隔秒数（默认20）
  - **GTPPMAXPAYLOAD**: GTP'消息最大可携带话单字节数（有效范围1200~7180，建议小于网络MTU）
- 注意: GTP'消息重发次数和间隔通常使用默认值；GTPPMAXPAYLOAD过小会频繁发送，过大会导致分片

---

## 四、CHF对接配置（N40接口 - 融合计费）

### K280 - CHF对接配置流程与关键命令
- 来源: 配置到CHF的数据（GGSN_PGW-C_SMF）_20495042.md
- 适用场景: 运营商完成融合计费接口改造，通过N40接口与CHF/NCG对接
- 接口: N40服务化接口（HTTP/2协议）
- 配置建议:
  - SBI业务IP地址不能和其他接口业务IP共用
  - 端口号未明确时使用HTTP知名端口8080
  - 一个NF类型配一个HTTP本端端点组
- 配置流程:
  1. 增加N40接口IP（ADD LOGICIP）
  2. 配置HTTP本端端点组（ADD HTTPLEGRP）
  3. 配置HTTP本端端点（ADD HTTPLE: LETYPE=SERVER/CLIENT）
  4. 配置N40接入点（ADD SBIAPLE: PEERNFTYPE=Nchf, PEERSERVICE=Nchf_ConvCharg）
  5. 配置HTTP属性（SET HTTPCONF: 超时/最大消息体/JSON叶子节点数）
  6. 配置CHF实例（ADD TNFINS + ADD TNFINSIP）
  7. 配置CHF组（ADD TNFGRP + ADD TNFBINDGRP）
  8. 配置CHF选择策略

### K281 - CHF选择策略四种方式
- 来源: 配置到CHF的数据（GGSN_PGW-C_SMF）_20495042.md
- CHF选择策略（优先级从高到低）:
  1. **基于计费属性选择** (ADD SELECTCHFGBYCC): 按Charge Characteristic值和掩码匹配，指定主备CHF组
  2. **基于IMSI号段选择** (ADD SELCHFGBIMSISEG): 按号段范围匹配，指定主备CHF组
  3. **基于NRF选择**: 不需要专有配置
  4. **基于本地NRF配置**: 支持SUPI（ADD PNFSUPI）和GPSI（ADD PNFGPSI）维度
  5. **全局默认CHF组** (SET GLBDFTCHFGROUP): 兜底配置，建议必须配置
- CHF组结构: 主CHF组(PRIMARYCHFGRP) + 备CHF组(SECONDARYCHFGRP)

---

## 五、OCS对接配置（Gy接口 - 在线计费）

### K282 - OCS对接配置流程与关键命令
- 来源: 配置到OCS的数据(GGSN_PGW-C_SMF)_67309461.md
- 适用场景: 运营商未完成融合计费接口改造，通过Gy接口与OCS对接实现在线计费
- 接口: Gy接口（Diameter协议）
- 配置流程:
  1. 创建VPN实例（ADD VPNINST）+ L3VPN实例
  2. 配置Gy集中点模式（SET CONCENPOINT: GYCONCENMODE=LOCALPORT）
  3. 配置Gy逻辑接口（ADD LOGICIP + ADD LOGICINF）
  4. 配置本端设备标识（ADD DIAMLOCINFO: HOSTNAME, REALMNAME, PRODUCTNAME）
  5. 配置OCS信息（ADD OCS: OCSHOSTNAME, REALMNAME, VPNINSTANCE）
     - OCS Server绑定的VPN必须和Gy逻辑接口绑定的VPN一致
  6. 配置Diameter链路（ADD DIAMCONNGRP: APPLICATION=GY）+ 对端地址（ADD DIAMPEERADDR）+ 链路（ADD DIAMCONNECTION）
  7. 配置OCS组和绑定（ADD OCSGROUP + ADD OCSBINDING）
  8. 配置主从OCS组（MOD DCCTEMPLATE: PRIOCSGRPNAME, SECOCSGRPNAME）
  9. 可选: CEA消息Origin-Host检查（SET CEAORIGHOSTCHK）

### K283 - Diameter链路配置要点
- 来源: 配置到OCS的数据(GGSN_PGW-C_SMF)_67309461.md, 配置到PCRF的数据（GGSN_PGW-C）_29355781.md
- Diameter链路配置三件套:
  1. **ADD DIAMCONNGRP**: 链路组，指定APPLICATION(GY/GX)、本端主机名、对端主机名、链路选择模式(MASTER_SLAVE/SESSION_ID/ROUND_ROBIN)
  2. **ADD DIAMPEERADDR**: 对端地址信息
  3. **ADD DIAMCONNECTION**: 链路实例，绑定逻辑接口和链路组
- Gx应用和Gy应用的本端主机名可以相同，但要求REALMNAME和PRODUCTNAME也必须相同
- 集中点模式为LOCALPORT时，必须在DIAMCONNECTION中配置本端端口号（非0有效值）

---

## 六、PCF/PCRF对接配置

### K284 - PCF对接配置（N7/Npcf服务化接口）
- 来源: 配置到PCF的数据（GGSN_PGW-C_SMF）_66127221.md
- 适用场景: 网络中部署PCF，UNC通过Npcf接口对接实现策略控制
- N7接口是服务化接口，传输层使用HTTP/2
- 配置流程:
  1. SBI接口本端信息配置（参考配置SBI接口步骤）
  2. 可选: 本地配置PCF（无NRF或PCF未注册NRF时）:
     - ADD PNFPROFILE: 增加PCF实例概述信息
     - ADD PNFSERVICE: 增加PCF服务信息（SERVICENAME=NpcfSmplcCtrl）
     - ADD PNFPLMN: PCF的PLMN信息
     - ADD PNFSUPI/PNFGPSI: PCF支持的SUPI/GPSI号段
     - ADD PNFNS: PCF支持的切片信息
     - ADD PNFPCFINFO: PCF的Rx接口Diameter信息
     - ADD PNFDNN: PCF支持的DNN
  3. 使能PCC功能（SET PCCFUNC: HOMEPCCSWITCH/ROAMPCCSWITCH/VISITPCCSWITCH=ENABLE）
  4. 可选: 基于DNN配置PCC开关和PCF选择方式（SET APNPCCFUNC: PCFSELECTMODE）
  5. 可选: 按ServingScope选择PCF（ADD PCFSSCOPE + ADD USRTAIRANGE + ADD PCFSSCOPEBIND）
  6. 可选: 按优选区域选择PCF（ADD NFPROFILE: LOCALITY）

### K285 - PCF选择方式(PCFSELECTMODE)
- 来源: 配置到PCF的数据（GGSN_PGW-C_SMF）_66127221.md
- SET APNPCCFUNC的PCFSELECTMODE支持组合选择:
  - DNN: 按数据网络名称
  - SUPI: 按用户永久标识
  - GPSI: 按通用公共订阅标识
  - S-NSSAIs: 按网络切片
  - PLMN: 按PLMN标识
  - NFLOC: 按优选区域（需ADD NFPROFILE配置LOCALITY）
  - SERVINGSCOPE: 按服务区（需ADD PCFSSCOPE+ADD USRTAIRANGE+ADD PCFSSCOPEBIND）
- 可复选组合，如 DNN&SERVINGSCOPE&NFLOC

### K286 - PCRF对接配置（Gx/Diameter接口）
- 来源: 配置到PCRF的数据（GGSN_PGW-C）_29355781.md
- 适用场景: GGSN/PGW-C通过Gx接口与PCRF对接（4G策略控制）
- 仅适用于GGSN、PGW-C
- 配置要点:
  1. VPN实例 + Gx集中点模式 + Gx逻辑接口
  2. 本端设备标识（ADD DIAMLOCINFO）
  3. PCRF信息（ADD PCRF: HOSTNAME, REALMNAME, VPNINSTANCE, SUPFEANEGOSW, FEATURELIST）
  4. Diameter链路（ADD DIAMCONNGRP: APPLICATION=GX + ADD DIAMPEERADDR + ADD DIAMCONNECTION）
  5. PCRF组（ADD PCRFGROUP + ADD PCRFBINDGRP + SET MASTERPCRF）
  6. 号段绑定（ADD IMSIMSISDNSEG + ADD GLBPCRFGROUP）+ 全局缺省PCRF组（SET DFTGLBPCRFGRP）
  7. APN绑定PCRF组（ADD APN + ADD PCRFGRPBNDAPN）

### K287 - CU Full Mesh组网下多本端主机名的Gx配置
- 来源: 配置到PCRF的数据（GGSN_PGW-C）_29355781.md
- 当同一PGW-C下多个PGW-U用户IP存在重叠，且PCRF要求UE IP + GxLocalHost唯一确定用户时:
  1. 配置多个本端主机名（多个ADD DIAMLOCINFO）
  2. 每个本端主机名对每个PCRF配一个Diameter链路组（4个链路组 = 2本端 x 2 PCRF）
  3. 配置Diameter本端主机组（ADD LOCALHOSTGRP + ADD LOCALHOSTBIND）
  4. 配置Gx UPF组（ADD GXUPFGROUP + ADD UPFBINDGXUPFGRP）
  5. 绑定UPF组与本端主机组（ADD UPFGLOCGBNDGRP + ADD UPFGBINDLOCG）
  6. PCC模板配置（ADD PCCTEMPLATE: LOCSLCTMODE=UPFGRP）
  7. APN绑定PCC模板（SET APNPCCFUNC: PCCTEMPLATE）

---

## 七、SMF典型配置实例

### K288 - SMF典型配置完整流程（不含计费）
- 来源: SMF典型配置实例_24779297.md
- 典型SMF+GW-C配置场景: 5G网络、IPv4单栈用户、OSPF动态路由
- 配置步骤（关键顺序）:
  1. 关闭自动配置开关（SET AUTOCONFIG:SWITCHFLAG=FALSE）
  2. 全局激活BFD（SET BFD:BFDENABLE=TRUE）
  3. 配置IP路由数据（SBI外联口、MME、GW、UPF各配VPN+OSPF）
  4. 打开自动配置开关（SET AUTOCONFIG:SWITCHFLAG=TRUE）
  5. 配置运营商基础数据（ADD NGMNO + ADD NGHPLMN + ADD NGSRVPLMN + ADD PLMNNS）
  6. 配置SMF实例信息（ADD NFUUID + ADD NFPROFILE + ADD SMFINFO + ADD NFSERVICE）
  7. 配置SMF服务化接口（ADD LOGICIP + ADD HTTPLEGRP + ADD HTTPLE + ADD SBIAPLE）
  8. 配置NRF数据（ADD NRF + ADD NRFADDR + ADD NRFPARA）
  9. 激活NF注册（SET LICENSESWITCH + ACT NFONLINE）
  10. 配置N4接口（ADD LOGICIP + ADD CPNODE + ADD CPPOINT + ADD PNFPROFILE + ADD UPNODE + ADD UPAREA）
  11. 配置S11/S5/S8-C接口（ADD LOGICIP + ADD GTPCLEGRP + ADD GTPCLEGRPMEM + ADD GTPCINTF）
  12. 配置会话管理（SET UEDNSBINDAPN）
  13. 配置4/5G互操作（SET SMFFUNC:EBID=Support + SET LICENSESWITCH）
- 注: 该典型实例未包含计费配置部分，计费配置需参考上述CG/CHF/OCS对接文档

---

## 八、计费告警处理

### K289 - ALM-82000 计费中心长时间未取话单（NCG告警）
- 来源: ALM-82000 计费中心长时间未取话单_51174179.md
- **告警级别**: 紧急告警（可自动清除）
- **触发条件**: NCG用PULL模式提供给计费中心第二份最终话单时:
  - 未配置备份或分发任务
  - 监控路径不存在
  - 超过时间阈值后计费中心未取走话单
- **影响**: 计费延迟 -> 话单在磁盘堆积 -> NCG磁盘空间不足 -> NCG停止接收话单 -> 话单产生网元话单池堆积 -> 限呼或话单丢失
- **停止接收话单阈值**: 磁盘剩余空间400MB
- **恢复条件**: 配置分发/备份任务、删除监控任务、或话单被取走删除

### K290 - ALM-100417 UPF中转RADIUS计费服务器无响应
- 来源: ALM-100417 UPF中转RADIUS计费服务器无响应_16408521.md
- **适用NF**: GGSN、PGW-C、SMF
- **告警级别**: 重要告警（可自动清除）
- **触发机制**: SMF通过UPF中转向RADIUS计费服务器发送计费请求，按RDSSVRGRP配置重发后仍无响应，异常次数达软参DWORD1040 BIT14-16门限，再等待BYTE41+BYTE42总时长后仍无响应
- **恢复机制**: 通信恢复或链路中断达BYTE201设定的告警恢复时长（默认60分钟）
- **影响**: 如果是唯一计费服务器，计费用户将无法计费、接入
- **可能原因**: SMF与UPF间RADIUS中转会话异常、UPF与RADIUS间传输中断、RADIUS服务器故障
- **相关命令**: MOD RDSSVRGRP可设置ACCTRETRANSMIT（重发次数）和ACCTTIMEOUT（重发间隔秒）

### K291 - ALM-100530 融合计费用户放通不计费
- 来源: ALM-100530 融合计费用户放通不计费_49169057.md
- **适用NF**: GGSN、PGW-C、SMF
- **告警级别**: 次要告警（可自动清除）
- **触发条件**（三点同时满足）:
  1. 告警开关开启（SET CNVRGDCHGPARA: CONTINUEALARM=ENABLE）
  2. 话单缓存功能关闭（SET N40MSGSTG: STGSWITCH=DISABLE）
  3. 单进程级，5min内会话放通且话单缓存未开启次数>=100
- **恢复条件**（满足任一）: 告警开关关闭、话单缓存开启、或5min内放通次数<=5
- **影响**: 用户业务过流不计费，有损失计费风险
- **根因**: 话单缓存未开启 + CHF故障导致会话放通
- **处理步骤**: 检查LST N40MSGSTG缓存开关 -> 确认是否允许放通不计费 -> 分析话统指标（无可用CHF/CHF无响应/结果码错误/信元错误）

### K292 - ALM-100630 在线计费定时器过载流控
- 来源: ALM-100630 在线计费定时器过载流控_18833222.md
- **适用NF**: GGSN、PGW-C、SMF
- **告警级别**: 重要（可自动清除）
- **触发机制**: 在线计费定时器被流控达到5分钟
- **恢复机制**: 定时器不再被流控达到10秒
- **定时器类型及影响**:
  - **VT Timer Congestion**: 业务级VT延迟上报OCS，可能OCS处理异常
  - **NPT Timer Congestion**: NPT定时器延迟生效，用户阻包时间延长
  - **User VT Timer Congestion**: 用户级VT延迟上报OCS
  - **Tx Timer Congestion**: 对端OCS不回响应时UNC异常处理不及时
- **可能原因**: VT/NPT时长较短、突发大量CCR消息且OCS不回响应
- **处理**: 等待10分钟看是否自动恢复，否则联系技术支持

### K293 - ALM-81020 RADIUS计费服务器无响应
- 来源: ALM-81020 RADIUS计费服务器无响应_13767441.md
- **适用NF**: GGSN、PGW-C、SMF
- **告警级别**: 重要告警（可自动清除）
- **触发机制**: UNC向RADIUS计费服务器发送请求，按配置重发后仍无响应，异常次数达软参门限，等待BYTE41+BYTE42总时长后仍无响应
- **恢复**: 收到RADIUS应答或无业务达Byte201配置时间
- **影响**: UNC无法将计费信息发送到RADIUS，但仍可用CG计费。新接入用户默认去活APN上下文
- **配置修改**: SET APNRDSACCTCTRL命令可将DEACTIVE改为CONTINUE（未收到响应时不去活用户上下文）
- **可能原因**: 未配置本端IP、节点故障、服务器配置错误(IP/端口/密钥/VPN)、传输中断、网络拥塞

### K294 - ALM-100682/100683 SMSF计费网元设备故障/业务状态异常
- 来源: ALM-100682 计费网元设备故障_92941240.md, ALM-100683 计费网元业务状态异常_29460633.md
- **适用NF**: SMSF
- **告警级别**: 重要告警（可自动清除）
- SMSF/VLR对接的NCG网元出现故障告警时，SMSF将告警上报网管
- 100682: NCG设备故障，可能导致业务受阻
- 100683: NCG业务状态异常，可能影响业务
- **处理步骤**: 记录NCG告警流水号/名称/ID -> 找到NCG对应告警 -> 查看NCG告警帮助处理

---

## 九、信令跟踪与故障定位

### K295 - EMS-SIGNALING 5G计费问题处理
- 来源: EMS-SIGNALING问题处理（适用于5G计费）_01898104.md
- 5G计费问题定位流程:
  1. 建立用户跟踪，查看是否上报**EMS_CtfErrorRpt**消息
  2. 打开EMS_CtfErrorRpt消息，解析关键字段:
     - **ChargingID**: 计费编号
     - **AnonymizeSupi**: 匿名化用户永久标识
     - **PduSessionId**: PDU会话编号
     - **RptErrorInfo**: 错误原因描述
     - **Details**: 定位详细信息
     - **Suggestion**: 错误处理建议
  3. 根据原因和建议处理，重新拨测验证

### K296 - EMS-SIGNALING 5G策略问题处理
- 来源: EMS-SIGNALING问题处理（适用于5G策略）_48458079.md
- 5G策略问题定位流程:
  1. 建立用户跟踪，查看是否上报**EMS_SmpolicyErr**消息
  2. 打开EMS_SmpolicyErr消息，解析关键字段:
     - **AnonymizedSupi**: 匿名化用户永久标识
     - **PdusessionId**: PDU会话编号
     - **Rattype**: 无线接入类型
     - **PcfInstanceId**: PCF实例标识
     - **EmsErrInfo**: 错误原因描述
     - **Suggestion**: 错误处理建议
  3. 根据原因和建议处理，重新拨测验证

---

## 十、配置命令速查与关联关系

### K297 - 计费接口配置命令全景图
- 来源: 综合（配置到CG/CHF/OCS/PCF/PCRF数据 + 配置计费和策略模式）
- **离线计费(Ga)**: ADD L3VPNINST -> ADD VPNINST -> SET CONCENPOINT(GACONCENMODE) -> ADD LOGICIP -> ADD LOGICINF -> ADD CG -> SET CDRTRANSFER
- **融合计费(N40)**: ADD LOGICIP -> ADD HTTPLEGRP -> ADD HTTPLE -> ADD SBIAPLE -> SET HTTPCONF -> ADD TNFINS -> ADD TNFINSIP -> ADD TNFGRP -> ADD TNFBINDGRP -> CHF选择策略
- **在线计费(Gy)**: ADD VPNINST -> SET CONCENPOINT(GYCONCENMODE) -> ADD LOGICIP -> ADD LOGICINF -> ADD DIAMLOCINFO -> ADD OCS -> ADD DIAMCONNGRP -> ADD DIAMPEERADDR -> ADD DIAMCONNECTION -> ADD OCSGROUP -> ADD OCSBINDING -> MOD DCCTEMPLATE
- **5G策略(N7)**: SBI接口 -> ADD PNFPROFILE -> ADD PNFSERVICE -> SET PCCFUNC -> SET APNPCCFUNC
- **4G策略(Gx)**: ADD VPNINST -> SET CONCENPOINT(GXCONCENMODE) -> ADD LOGICIP -> ADD LOGICINF -> ADD DIAMLOCINFO -> ADD PCRF -> ADD DIAMCONNGRP -> ADD DIAMPEERADDR -> ADD DIAMCONNECTION -> ADD PCRFGROUP -> SET MASTERPCRF -> SET DFTGLBPCRFGRP
- **计费模式**: SET CHGMODE -> ADD APNCHGMODE -> ADD ROAMCHGMODE
- **策略模式**: SET POLICYMODE -> ADD APNPOLICYMODE -> ADD PCCCHGMODEBYPCFID

### K298 - VPN实例隔离原则
- 来源: 综合（CG/CHF/OCS/PCRF配置文档）
- 各计费/策略接口使用独立VPN实例:
  - Ga接口: vpn_ga（L3VPN）
  - Gy接口: vpn_gy（L3VPN）
  - Gx接口: vpn_gxif
  - N40接口: VRF_CHF（通过SBI统一VPN或独立VPN）
- 运营商通常提供专网连接作为计费网络，Ga/Gy/Gx接口可与其他接口接入不同的Router设备

### K299 - Diameter集中点模式(SET CONCENPOINT)
- 来源: 综合（OCS/PCRF配置文档）
- SET CONCENPOINT命令控制各接口的Diameter集中点模式:
  - **GACONCENMODE**: Ga接口集中点（SINGLE_CONNECT/MULTI_PORT）
  - **GYCONCENMODE**: Gy接口集中点（默认LOCALPORT）
  - **GXCONCENMODE**: Gx接口集中点（典型LOCALPORT）
- LOCALPORT模式下可手动指定本端端口号（ADD DIAMCONNECTION的LOCALPORT参数必须为非0有效值）
- 非LOCALPORT模式下端口号由系统自动分配

### K300 - 主从/主备配置模式总结
- 来源: 综合
- 不同计费网元的主从配置模式:

| 网元 | 组配置 | 绑定 | 主备设置 | 默认/兜底 |
|------|--------|------|----------|-----------|
| CG | ADD CG(PRIORITY) | - | PRIORITY数值越小越高 | - |
| CHF | ADD TNFGRP | ADD TNFBINDGRP | SELECTCHFGBYCC/SELCHFGBIMSISEG | SET GLBDFTCHFGROUP |
| OCS | ADD OCSGROUP | ADD OCSBINDING | MOD DCCTEMPLATE(PRIOCSGRPNAME/SECOCSGRPNAME) | 全局DCC模板 |
| PCRF | ADD PCRFGROUP | ADD PCRFBINDGRP | SET MASTERPCRF | SET DFTGLBPCRFGRP |
| PCF | 本地: ADD TNFGRP | ADD TNFBINDGRP | NRF发现或本地配置 | - |

---

## 十一、告警速查表

### K301 - 计费相关告警速查
- 来源: 综合（6篇告警文档）

| 告警ID | 名称 | 级别 | 适用NF | 核心含义 |
|--------|------|------|--------|----------|
| 82000 | 计费中心长时间未取话单 | 紧急 | NCG | PULL模式下计费中心未取话单 |
| 100417 | UPF中转RADIUS计费服务器无响应 | 重要 | SMF/GW-C/GGSN | SMF通过UPF中转RADIUS链路断 |
| 100530 | 融合计费用户放通不计费 | 次要 | SMF/GW-C/GGSN | CHF故障+缓存关闭导致放通不计费 |
| 100630 | 在线计费定时器过载流控 | 重要 | SMF/GW-C/GGSN | 在线计费定时器拥塞（VT/NPT/Tx） |
| 81020 | RADIUS计费服务器无响应 | 重要 | SMF/GW-C/GGSN | UNC直连RADIUS计费服务器链路断 |
| 100682 | 计费网元设备故障 | 重要 | SMSF | NCG设备故障 |
| 100683 | 计费网元业务状态异常 | 重要 | SMSF | NCG业务异常 |

### K302 - ALM-100530处理要点：融合计费放通不计费
- 来源: ALM-100530 融合计费用户放通不计费_49169057.md
- **核心关联命令**:
  - SET CNVRGDCHGPARA: CONTINUEALARM=ENABLE（告警开关）
  - SET N40MSGSTG: STGSWITCH=ENABLE（开启话单缓存可避免放通不计费）
- **话统分析维度**（定位根因）:
  - 无可用CHF导致的放通次数
  - CHF无响应导致的放通次数
  - CHF返回的结果码导致的放通次数
  - CHF响应消息信元错误导致的放通次数
- **建议**: 现网应开启话单缓存功能(SET N40MSGSTG: STGSWITCH=ENABLE)以避免CHF故障时用户放通不计费

---

## 十二、运维排障要点

### K303 - 5G计费故障定位方法论
- 来源: 综合（告警文档 + 信令跟踪文档）
- 计费故障定位四步法:
  1. **告警分析**: 查看是否有计费相关告警（K301速查表）
  2. **信令跟踪**: 建立用户跟踪，查看EMS_CtfErrorRpt消息，解析ChargingID/RptErrorInfo/Suggestion
  3. **配置核查**: 检查计费模式(SET CHGMODE)、接口配置、网元对接参数
  4. **话统分析**: 分析放通次数、无响应次数等话统指标

### K304 - 5G策略故障定位方法论
- 来源: EMS-SIGNALING问题处理（适用于5G策略）_48458079.md
- 策略故障定位步骤:
  1. 建立用户跟踪，查看EMS_SmpolicyErr消息
  2. 解析PcfInstanceId/EmsErrInfo/Suggestion字段
  3. 确认PCF实例是否正常、策略接口模式是否正确
  4. 处理后重新拨测验证

### K305 - 计费配置变更风险点
- 来源: 综合
- 计费配置变更的高风险操作:
  1. **SET CHGMODE修改计费模式**: 直接影响所有用户的计费接口选择，变更期间可能导致话单丢失
  2. **SET N40MSGSTG关闭话单缓存**: CHF故障时用户将放通不计费
  3. **OCS/CHF组主备切换**: 变更期间可能短暂影响在线计费
  4. **Diameter链路删除重建**: 影响在线计费和策略控制会话
  5. **CG PRIORITY调整**: 影响离线话单发送路径

### K306 - 2/3/4/5G共存网络计费配置策略
- 来源: 配置计费和策略模式_67342025.md
- 典型2/3/4/5G共存网络计费配置:
  - 5G终端+5G接入(SMF): NchfMode（融合计费）
  - 5G终端+4G接入(PGW-C): 可根据5GS互操作指示选Nchf或GaGy
  - 非5G终端+4G接入(PGW-C): GaGyMode
  - 2G/3G接入(GGSN): GaGyMode
  - NB-IoT/LTE-M: GaGyMode或NchfMode（按运营商规划）
- 策略接口配置:
  - 5G相关接入: Npcf（PCF）
  - 2G/3G/NB-IoT/LTE-M: Gx（PCRF）或Npcf

### K307 - 离线计费CG优先级与话单发送机制
- 来源: 配置到CG的数据（GGSN_PGW-C_SMF）_67429269.md
- ADD CG命令的PRIORITY参数:
  - 数值越小优先级越高，优先使用高优先级CG
  - 典型配置: 主CG PRIORITY=0，备CG PRIORITY=1
- CG负荷分担算法(CGSELECTIONMODE):
  - MSG_BASED_LB: 基于消息的负载均衡
- GTP'消息控制:
  - 重传机制: 先重传RETRANSTIMES次，每次间隔RETRANSINTERVAL秒
  - Node Alive: 保活机制，重传间隔NARESTRANSINTVL秒
  - 话单打包: GTPPMAXPAYLOAD控制单个消息最大字节数，小话单可合并发送

### K308 - 融合计费N40接口HTTP配置要点
- 来源: 配置到CHF的数据（GGSN_PGW-C_SMF）_20495042.md
- HTTP/2协议栈: SBI统一使用HTTP/2，所有SBI接口在同一总线上传输
- SET HTTPCONF关键参数:
  - SERVERRCVBDTMT: 服务端接收HTTP请求消息体超时（秒）
  - SERVERSNDRSPTMT: 服务端回复HTTP响应超时（秒）
  - MAXBODYSIZE: 最大消息体大小（MBytes）
  - MAXJSONLEAFNUM: JSON数据最多叶子节点个数
- 超大报文场景需合理设置这些参数，避免报文不完整导致业务异常

### K309 - ADD HTTPLE本端端点的SERVER/CLIENT角色
- 来源: 配置到CHF的数据（GGSN_PGW-C_SMF）_20495042.md
- ADD HTTPLE中LETYPE参数:
  - **SERVER**: SMF作为HTTP服务端（接收CHF的请求），需要配置PORT
  - **CLIENT**: SMF作为HTTP客户端（向CHF发请求），不需要PORT
- 典型配置: 同一个HTTPLEGRP下配一个SERVER端点+一个CLIENT端点，使用不同IP

### K310 - ADD SBIAPLE服务化接口接入点配置
- 来源: 配置到CHF的数据（GGSN_PGW-C_SMF）_20495042.md
- ADD SBIAPLE关键参数:
  - **NFTYPE**: 本端NF类型（NFTypeSMF）
  - **PEERNFTYPE**: 对端NF类型（Nchf表示计费、Npcf表示策略）
  - **PEERSERVICE**: 对端服务名称
    - Nchf_ConvCharg: CHF融合计费服务
    - NpcfSmplcCtrl: PCF会话管理策略控制
- 通过PEERNFTYPE和PEERSERVICE区分不同SBI接口的目的NF
