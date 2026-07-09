# Batch-02: CS-5基础数据/MTU + CS-3网管对接
> 批次02 | 对接面CS-5基础就绪 + CS-3网管对接 | 文件数6 | 核心度★★★★
> 子场景：UPF网元对接（UDG扮演 UPF / PGW-U / SGW-U 融合角色，对接 N4/N3/N9/N6）
> 文档前缀：`output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/`

## 1. 概述

本批次覆盖 **CS-5基础就绪**剩余板块（基础数据配置 + MTU调整）与 **CS-3网管对接**完整闭环。CS-5基础数据是所有对接面（控制面/用户面/网管/路由）的**系统级前置**：网元身份、时间、安全授权、全局QoS参数、链路MTU必须先就位，业务面才能稳定承载；CS-3网管对接是开局**对接调测起点**，完成此步后运营商才能通过 U2020/MAE 对所有网元集中管理与下发MML。

| 板块 | 解决的问题 | 来源文档 |
|------|------------|----------|
| NTP时间同步 | 双路时间源（OMC + FusionStage）可靠性，依赖NPFD-010014 | 配置NTP时间同步_53637513.md |
| 网元基本信息 | 修改网元名称/浮动IP，与网管侧保持一致 | 修改网元基本信息_50422559.md |
| 高危命令二次授权 | 安全合规：13类UDG默认二次授权命令清单 + 自定义流程 | 配置高危命令二次授权_48016554.md |
| 公共参数 | 全局DSCP/UDP校验和/QoS CAR/IPv6分片/时区/防欺诈/转发参数等11项 | 公共参数配置_97905321.md |
| MTU调整 | Fabric平面/Tunnel接口/外联口三层MTU修改与自动部署模板同步 | 修改MTU值_75096774.md |
| 网管对接 | 北向用户密码/SNMP共享密钥/网管适配层/创建网元14项关键参数 | 配置网元和网管对接_34981624.md |

文档关系：6个文档相互独立、可并行执行，但存在隐性顺序约束——`修改网元基本信息`（MOD ME/SET OMIP）若改浮动IP会**中断网管与VNFM连接**，因此必须在 `配置网元和网管对接` 之前完成；`公共参数配置` 的 SET SIGDSCP/SET QOSCAR 等需在业务开通前定稿；`高危命令二次授权` 中 SET OMIP 本身就是默认二次授权命令，与 `修改网元基本信息` 形成自洽闭环。

---

## 2. 核心知识点

### KP-01: NTP双路时间同步（OMC + FusionStage）
- **内容**：网元支持**同时从OMC和FusionStage两路**同步时间信息。当一路故障后，另一路仍可正常运行，保证时间同步可靠性。
  - OMC路：详细配置参见特性文档 `NPFD-010014 支持NTP功能/激活支持NTP功能`
  - FusionStage路：可从外部NTP Server同步，也可通过FusionSphere提供的NTP服务同步
- **来源**：配置NTP时间同步_53637513.md
- **核心度**：★★★
- **关联特性**：**NPFD-010014 支持NTP功能**（明确引用），属 **NPFD-010000 操作维护功能** 父特性
- **关联命令**：无（本文档为入口说明，具体MML在 `激活支持NTP功能_40755235.md`）
- **关联配置对象**：NTP时间源
- **对接面**：CS-5（基础就绪，全局时间基准）

### KP-02: 修改网元基本信息（MOD ME + SET OMIP）
- **内容**：软件安装阶段已完成网元名称和浮动IP配置；生产预安装或现网使用时如需修改，使用以下两条MML。

| MML命令 | 关键参数 | 取值样例 | 用途 |
|---------|----------|----------|------|
| **MOD ME** | MEID / MENAME | 0 / "APP" | 修改网元名称 |
| **SET OMIP** | OMIPTYPE / OMSETTYPE / OMFIPADDR / OMNETMASK / OMIPV4GATEWAY | IPV4 / SET_IP / 10.145.27.173 / 255.255.255.0 / 10.145.27.1 | 修改浮动IP（已配物理IP场景） |
| **SET OMIP** | 同上 + OMHOST1IPV4 / OMHOST2IPV4 | + 10.145.27.174 / 10.145.27.175 | 修改浮动IP+物理IP（未配或IP不符场景） |

- **配置实例（保留原始MML）**：
  ```
  MOD ME: MEID=0, MENAME="APP";
  SET OMIP: OMIPTYPE=IPV4, OMSETTYPE=SET_IP, OMFIPADDR="10.145.27.173", OMNETMASK="255.255.255.0", OMIPV4GATEWAY="10.145.27.1";
  SET OMIP: OMIPTYPE=IPV4, OMSETTYPE=SET_IP, OMFIPADDR="10.145.27.173", OMNETMASK="255.255.255.0", OMIPV4GATEWAY="10.145.27.1", OMHOST1IPV4="10.145.27.174", OMHOST2IPV4="10.145.27.175";
  ```
- **强约束（3条级联影响）**：
  1. 网元名称、浮动IP必须与**网管侧配置的名称和IP属性一致**，本端修改后需在网管侧同步修改
  2. 修改浮动IP后 **OM Portal 将退出**，需用新IP重新登录
  3. 修改浮动IP后 **网管与网元的连接将中断**，需在网管上重新对接网元；**VNFM与网元的连接也将中断**，需在VNFM上修改对应网元的IP地址
- **物理IP约束**：物理IP必须与浮动IP**在同一网段**
- **前置查询**：执行 `LST OMIP` 查询系统是否已配置物理IP，决定走"仅改浮动IP"分支还是"改浮动IP+物理IP"分支
- **来源**：修改网元基本信息_50422559.md
- **核心度**：★★★★★（影响CS-3网管对接链路）
- **关联特性**：无（基础运维操作）
- **关联命令**：MOD ME、SET OMIP、LST OMIP、LST ME（查询MEID）
- **关联配置对象**：网元（ME）、OM网络（OMIP）
- **对接面**：CS-5（基础就绪）+ 间接关联 CS-3（修改后必须重新对接网管）

### KP-03: 高危命令二次授权机制与13类UDG默认清单
- **内容**：系统提供高危命令二次授权能力——操作员执行被二次授权的高危命令时，必须经**二次授权用户**的授权确认。系统默认关闭，建议开局/日常维护开启。
- **配置流程（3步MML + 1步验证）**：
  ```
  SET SECAUTH: STATUS=ON;                       // 1.开启二次授权总开关
  ADD USRSECAUTH: USRNAME="User01";             // 2.增加二次授权用户（须已在OM Portal"安全>用户管理"创建）
  ADD SECAUTHMEM: MEID=0, COMMAND="LST ME";     // 3.（可选）增加自定义二次授权命令
  ```
- **权限要求**：
  - 普通域：admin用户登录 OM Portal
  - 扩展域：系统管理员权限用户登录 OM Portal；无权限者需在 "安全 > 用户管理 > 角色" 添加系统管理员权限
- **验证方法**：执行已加入二次授权列表的命令（如 LST ME）→ MML界面弹出二次授权提示 → 输入步骤2配置的二次授权用户名/密码 → 返回执行结果
- **UDG默认二次授权命令清单（13类，不可删除）**：

| 类别 | MML命令 | 风险说明 |
|------|---------|----------|
| OM网络/通信 | **MOD VIRTUALIP** | 修改浮动IP，可能导致通信中断 |
| OM网络/通信 | **SET OMIP** | 修改系统OM网络配置，可能导致通信中断 |
| 存储故障 | **SET BYPASSSWITCH** | 设置存储故障节点BYPASS，可能导致系统无法自动进入Bypass |
| 节点复位 | **RST NODEBATCH** | 批量复位节点，模块数据丢失、业务受影响、文件损坏 |
| OM网络/通信 | **MOD NETWORK** | 修改OM网络网卡VLANID，可能导致通信中断 |
| OM网络/通信 | **MOD OMNWCONF** | 配置OM网络故障探测参数，仅Administrators可执行，可能导致通信中断 |
| 热补丁 | **RMV HPATCH** | 删除热补丁，操作不当影响系统运行 |
| Pod重建 | **RST MESYS** | Pod重建，复位期间部分服务不可用 |
| 容器引擎 | **SET CNTTMPDIR** | 设置容器引擎临时目录，会复位容器引擎，可能导致业务受损 |
| OM开关 | **SET OMSWITCH** | 设置OM功能开关，可能导致通信中断 |
| 双向认证 | **SET CLTVFYSWITCH** | 修改双向认证开关，可能导致通信中断 |
| 资源规格 | **ADD/MOD/RMV SPECCFGITEM** | 资源规格调整范围配置不当→业务资源不足/进程复位/虚机复位 |
| IPsec（仅升级路径） | **RMV ACLGROUP6IPSEC / RMV ACLGROUP4IPSEC / RMV ACLRULEADV4IPSEC5G / RMV ACLRULEADV6IPSEC / RMV PROPATTACHIPSECPROPOSAL5G / ADD/MOD/RMV IKEPROPOSAL5G / RMV IPSECINTFCFGIPSEC5G / ADD/MOD/RMV IPSECPOLICY4 / ADD/MOD/RMV IPSECPOLICY6 / ADD/MOD/RMV IPSECPROPOSALIPSEC5G / ADD/MOD/RMV IPBINDVPNIPSEC5G / RMV L3VPNINSTIPSEC5G / RMV VPNINSTAFIPSEC5G** | 仅从20.6.2/20.7.1升级到20.8.2及后续版本时需二次授权；20.8.2及后续新建部署或新建后升级**不需要** |

- **关键交叉点**：`SET OMIP`（KP-02）与 `MOD VIRTUALIP` **本身即默认二次授权命令**——执行"修改网元基本信息"前必须先完成二次授权配置或获得授权用户配合
- **来源**：配置高危命令二次授权_48016554.md
- **核心度**：★★★★（开局安全合规必配）
- **关联特性**：无（系统级安全功能）
- **关联命令**：SET SECAUTH、ADD USRSECAUTH、ADD SECAUTHMEM、LST ME（验证）
- **关联配置对象**：二次授权用户、二次授权命令列表
- **对接面**：CS-5（基础就绪，安全合规）

### KP-04: 公共参数11项配置（全局业务面基准）
- **内容**：本页面涉及的公共参数均有默认值，根据网设LLD规划值调整。共11项配置，覆盖协议DSCP、UDP校验和、用户五元组上限、QoS CAR、IPv6分片、TEID分配、时区、防欺诈、转发参数、头增强全局参数、告警开关。

| 序号 | MML命令 | 用途 | 系统初始值 | 配置实例 |
|------|---------|------|-----------|----------|
| 1 | **SET SIGDSCP** | N4接口PFCP协议信令报文DSCP（填充ToS字段） | 46 | `SET SIGDSCP:PROTOCOL=PFCP,DSCPV=46;` |
| 2 | **SET UDPCHECKSUM** | UDG发送UDP报文是否携带CheckSum（**IPv6报文必须ENABLE**） | DISABLE | `SET UDPCHECKSUM:UDPTYPE=PFCP,SWITCH=ENABLE;` |
| 3 | **SET SRVCOMMONPARA** | 每用户最大五元组个数 | 600 | `SET SRVCOMMONPARA: FDMAXNUM=1000;` |
| 4 | **SET QOSCAR** | QoS CAR（按用户类型×RAT类型使能） | NULL（不使能） | 见下方完整实例（HOME/ROAMING/VISITING三类） |
| 5 | **SET IPV6FRAGPLCY** | IPv6报文分片策略（INNERIPV4/INNERIPV6） | OUTERFRAG / TOOBIG_PKTDROP | `SET IPV6FRAGPLCY: INNERIPV4FRAGPLCY=OUTERFRAG, INNERIPV6FRAGPLCY=OUTERFRAG;` |
| 6 | **SET CPTEIDUALLOC** | 用户面支持分配F-TEID（CP分配TEID-U可能重复，**必须DISABLE由UP分配**） | DISABLE | `SET CPTEIDUALLOC: SWITCH=DISABLE;` |
| 7 | **SET TZ** | 时区（东八区、不执行夏令时为例） | — | `SET TZ: TZONE=E0800, DST=NO;` |
| 8 | **SET ANTIFRAUD** | 防欺诈（FUI/HTTP/URL重定向） | — | `SET ANTIFRAUD:ISNULLRECEN=DISABLE, ISTEXTEN=DISABLE, ISHEURISTICEN=DISABLE, FUIAFSWITCH=DISABLE, HTTPAFSWITCH=ENABLE, URLREDAFSWITCH=DISABLE;` |
| 9 | **SET FWDPARA** | 转发参数（**高危命令**，报文重组超时） | RSTime=3 | `SET FWDPARA:RSTime=6, IPV6RSTime=6, FWDSWITCH=ON;` |
| 10 | **SET HEADENGLBPARA** | 头增强全局参数（盐类型等） | HEADENSALTTYPE=RANDNUM | `SET HEADENGLBPARA:RC4KEYMD5EN=DISABLE, MSISDNMINLEN=0, RSANODEAGETIME=10, RSAEXPIREDALM=ENABLE, RSACERTEXPALMDAYS=30, HEADENSALTTYPE=TIMESTAMP;` |
| 11 | **SET MSFAULTALARM** | 告警开关（抑制使能+抑制时长） | TRUE / 300 | `SET MSFAULTALARM: SUPPRESSENABLE=TRUE, SUPPRESSTIME=300;` |

- **QoS CAR 完整配置实例（HOME/ROAMING/VISITING三类用户×10种RAT）**：
  ```
  // 配置本地用户的上下行CAR功能（-1=使能，-0=不使能）
  SET QOSCAR: USERTYPE=HOME, ULRAT=eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&lte_m-1&nr-1&unknown-1&utran-1&wlan-1, DLRAT=eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&nr-1&unknown-1&utran-1&wlan-1;
  // 配置漫游用户的上下行CAR功能
  SET QOSCAR: USERTYPE=ROAMING, ULRAT=eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&lte_m-1&nr-1&unknown-1&utran-1&wlan-1, DLRAT=eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&nr-1&unknown-1&utran-1&wlan-1;
  // 配置拜访用户的上下行CAR功能
  SET QOSCAR: USERTYPE=VISITING, ULRAT=eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&lte_m-1&nr-1&unknown-1&utran-1&wlan-1, DLRAT=eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&nr-1&unknown-1&utran-1&wlan-1;
  ```
- **关键约束**：
  - 序号2 UDP CheckSum：**IPv6报文必须设为ENABLE**
  - 序号5 IPv6分片：当UPF封装后报文长度>MTU时，`TOOBIG_PKTDROP`会丢弃并回Too big报文；需业务稳定时改为 `OUTERFRAG` 由UPF做外层IPv6分片（与KP-05 MTU强相关）
  - 序号6 CPTEIDUALLOC：不同CP分配给同一UP的TEID-U可能重复，**必须DISABLE**由用户面分配TEID-U
  - 序号9 SET FWDPARA：**高危命令**，重组超时过小→分片不完整；过大→降低设备性能；操作不当导致业务故障，须联系华为技术支持
- **前置条件**：具备管理员权限的操作人员已登录华为操作维护系统（U2020/MAE客户端 或 OM Portal）
- **文档约束**：参数值依据**网设LLD**；LLD未描述的参数默认用系统初始值，为防误改建议按本页面重新配置
- **来源**：公共参数配置_97905321.md
- **核心度**：★★★★★（业务面全局基准）
- **关联特性**：无（系统级公共参数）
- **关联命令**：SET SIGDSCP / SET UDPCHECKSUM / SET SRVCOMMONPARA / SET QOSCAR / SET IPV6FRAGPLCY / SET CPTEIDUALLOC / SET TZ / SET ANTIFRAUD / SET FWDPARA / SET HEADENGLBPARA / SET MSFAULTALARM
- **关联配置对象**：全局业务参数集（DSCP/CheckSum/五元组/CAR/分片/TEID/时区/防欺诈/转发/头增强/告警）
- **对接面**：CS-5（基础就绪，业务面全局）

### KP-05: MTU三层修改（Fabric / Tunnel / 外联口）+ 自动部署模板同步
- **内容**：修改MTU值为**高危操作**——MTU修改可能导致整网分片增多、协议邻居无法建立。涉及3个层面MTU修改，外加自动部署模板同步。

**MTU层级强约束**：
> **网卡MTU ≥ Fabric的MTU > 主接口的MTU ≥ 子接口的MTU**
> 建议子接口MTU与主接口配置一致
> 外联口MTU必须与直连下一跳网关（DCGW/路由器）一致，默认1500

| 层面 | MML命令 | 关键参数 | 取值样例 |
|------|---------|----------|----------|
| Fabric平面 | **SET FABRICMTU** | MTUVALUE | 1800 |
| Tunnel接口（IPv4） | **MOD INTERFACE** | IFNAME / IFMTU | "Tunnel6" / 1500 |
| Tunnel接口（IPv6） | **SET IFIPV6ENABLE** | IFNAME / ENABLEFLAG / MTU | "Tunnel6" / TRUE / 1500 |
| 外联口主接口 Ethernet（IPv4） | **MOD INTERFACE** | IFNAME / IFMTU | "Ethernet64/0/4" / 1500 |
| 外联口主接口 Ethernet（IPv6） | **SET IFIPV6ENABLE** | IFNAME / ENABLEFLAG / MTU | "Ethernet64/0/4" / TRUE / 1500 |
| 外联口子接口 Ethernet（IPv4） | **MOD INTERFACE** | IFNAME / IFMTU | "Ethernet64/0/4.1" / 1500 |
| 外联口主接口 Eth-trunk（IPv4） | **MOD INTERFACE** | IFNAME / IFMTU | "Eth-trunk1" / 1500 |
| 自动部署模板 | **MOD AUTOSCALINGSERVICE** | SERVICENAME / MTU | "ServName_test1" / 1500 |

- **配置实例（保留原始MML）**：
  ```
  // 1. Fabric平面 MTU（NP卡加速场景不支持MML修改）
  SET FABRICMTU: MTUVALUE=1800;

  // 2. Tunnel接口 MTU
  // IPv4
  MOD INTERFACE:IFNAME="Tunnel6",IFMTU=1500;
  // IPv6
  SET IFIPV6ENABLE:IFNAME="Tunnel6",ENABLEFLAG=TRUE,MTU=1500;

  // 3. Ethernet外联口主接口 MTU
  // IPv4
  MOD INTERFACE:IFNAME="Ethernet64/0/4",IFMTU=1500;
  // IPv6
  SET IFIPV6ENABLE:IFNAME="Ethernet64/0/4",ENABLEFLAG=TRUE,MTU=1500;

  // 4. Ethernet外联口子接口 MTU（可选，主接口下存在子接口时）
  MOD INTERFACE:IFNAME="Ethernet64/0/4.1",IFMTU=1500;
  SET IFIPV6ENABLE:IFNAME="Ethernet64/0/4.1",ENABLEFLAG=TRUE,MTU=1500;

  // 5. Eth-trunk外联口主接口 MTU（注意：不需要修改成员接口MTU，加入Eth-trunk前修改会导致添加成员失败）
  MOD INTERFACE:IFNAME="Eth-trunk1",IFMTU=1500;
  SET IFIPV6ENABLE:IFNAME="Eth-trunk1",ENABLEFLAG=TRUE,MTU=1500;
  ```
- **自动部署模板同步（4步，避免后续告警ALM-232398849 接口自动化配置失败）**：
  ```
  LST AUTOCONFIG:;                                   // a.查询自动配置开关
  SET AUTOCONFIG:SWITCHFLAG=FALSE;                   // b.关闭自动配置开关（须先DSP OPSASSISTSTATE确认autoscaling_autoconfig.py为Ready或无此脚本）
  MOD AUTOSCALINGSERVICE: SERVICENAME="ServName_test1", MTU=1500;   // c.修改模板MTU
  SET AUTOCONFIG: SWITCHFLAG=TRUE;                   // d.重新开启自动配置开关
  ```
- **验证方法（5步）**：
  1. `LST FABRICMTU:;` 查询Fabric平面MTU
  2. `LST INTERFACE:IFNAME="Ethernet64/0/4";` / `LST IFIPV6ENABLE:IFNAME="Ethernet64/0/4";` 查询接口MTU
  3. `DSP IFSTATUS:IFNAME="Ethernet64/0/4";` 查询接口状态（UP/Down）
  4. `LST AUTOSCALINGSERVICE:;` 查询自动配置模板MTU
  5. 发送不大于MTU值的报文确认无分片；异常时 `EXP MML` 导出配置 + 收集对端设备配置联系华为技术支持
- **Eth-trunk特殊约束**：不需要修改成员接口MTU；成员接口加入Eth-trunk前修改MTU会导致添加成员失败
- **来源**：修改MTU值_75096774.md
- **核心度**：★★★★（影响CS-2用户面/CS-4路由对接的链路层）
- **关联特性**：**IPFD-010001 接口管理**（明确引用，"IP基本特性/IPFD-010000 接口与链路/IPFD-010001 接口管理/IPFD-010001 接口管理特性概述"）
- **关联命令**：SET FABRICMTU / MOD INTERFACE / SET IFIPV6ENABLE / MOD AUTOSCALINGSERVICE / LST FABRICMTU / LST INTERFACE / LST IFIPV6ENABLE / DSP IFSTATUS / LST AUTOSCALINGSERVICE / LST AUTOCONFIG / SET AUTOCONFIG / DSP OPSASSISTSTATE / EXP MML
- **关联配置对象**：Fabric平面、Tunnel接口、Ethernet外联口、Eth-trunk外联口、自动部署模板（AUTOSCALINGSERVICE）
- **对接面**：CS-5（基础就绪，链路层）+ CS-4（路由对接前置）

### KP-06: CS-3网管对接完整流程（5步闭包）
- **内容**：UDG对接网管（U2020/MAE）后，运营商可通过网管对所有网元集中管理和维护。完整对接流程为5步：

| 步骤 | 操作 | 关键说明 |
|------|------|----------|
| 1 | 修改北向对接用户密码 | **初次对接必须重置密码**，否则对接失败；密码修改参见"修改对接网管的北向对接用户密码_74094640.md" |
| 2 | 修改SNMP用户共享密钥 | **初次对接必须重置共享认证密钥和共享加密密钥，且两者不能相同**，否则对接失败；通过 OM Portal "系统 > SNMP管理 > 重置共享密钥" 修改 |
| 3 | 安装网管适配层 | 从华为技术支持网站下载网元版本配套的网管适配层软件 → 在网管侧安装 |
| 4 | 创建UDG网元（14项关键参数，见下方表2） | 参见 MAE/U2020 产品文档"创建单个物理网元"章节 |
| 5 | 检查VNF已添加到所属EMS | **仅VNF LCM独立部署形态时**需要在 VNF LCM "VNFM-EMS管理" 检查；未添加则需为VNF增加所属EMS |

- **3类必获取帐号（开局前准备）**：

| 帐号类型 | 用途 | 密码修改策略 | 参考文档 |
|----------|------|--------------|----------|
| 网管用户 | 登录网管系统 | — | 网管产品文档《系统默认帐号》 |
| 北向对接用户 | 对接北向网管系统 | **初次对接必须重置密码**，否则对接失败 | 《UDG应用用户默认帐号》 |
| SNMP用户 | 对接北向网管SNMP协议 | **初次对接必须重置共享认证密钥和共享加密密钥，且两者不能相同**，否则对接失败 | 《UDG应用用户默认帐号》 |

- **创建UDG网元14项关键参数（表2，对接核心）**：

| 参数名 | 取值样例 | 来源/说明 |
|--------|----------|-----------|
| **名称** | UDG | UDG网元名称（与KP-02 MOD ME一致） |
| **IP地址** | IPv4: 10.85.164.135 / IPv6: fc00:0db8:0:0:0:0:0:2 | **UDG外网浮动IP**（即KP-02 SET OMIP配置的OMFIPADDR） |
| **网元连接类型** | **TLS连接** | UDG与网管建链类型 |
| **OSS认证模式** | 证书认证 / 匿名认证 | UDG与网管对接认证模式 |
| **用于登录网元的账号** | **emscomm** | UDG与网管对接账号；**必须输入密码**（单击"..."输入emscomm密码和确认密码），否则网管用初始密码连接→密码错误→断链→业务功能受影响 |
| **协议版本** | **SNMPV3（推荐）** | UDG与网管对接SNMP协议版本 |
| **安全用户名** | v3User | 已创建的SNMP用户名（《UDG应用用户默认帐号》查询）；**对接多个网管时使用不同SNMP账号** |
| **端口** | 8000 | UDG与网管SNMP对接端口号（《UDG通信矩阵》查询） |
| **授权协议** | **SHA512（推荐）** | 支持SHA/SHA256/SHA384/SHA512，须与对端协商一致；**SHA为不安全协议，使用会告警"ALM-136750 SNMP协议存在弱算法"** |
| **授权密码** | — | 以帐号表为准 |
| **确认密码** | — | 与授权密码一致 |
| **加密协议** | **AES256（推荐）** | 支持AES128/AES192/AES256，须与对端协商一致 |
| **加密协议密码** | — | 以帐号表为准 |
| **确认密码** | — | 与加密协议密码一致 |

- **证书自动更新为LiteCA的5项前置条件（采用MAE自动更新时）**：
  1. 关联初始证书的证书场景在网管MAE上显示为"OM"类型，且网元对接设备为**华为域内设备**（非第三方厂商设备）
  2. 网元对接网管MAE前，`SET NEWCERTSWITCH` 命令中 **CERTSWITCH=ON**（证书开关打开）
  3. 网管MAE已创建默认CA证书且网元首次接入自动更新证书功能已开启（详见 MAE 产品文档"创建本地默认CA"）
  4. 网元对接MAE网管系统，**网管系统版本V100R024C10及后续版本**
  5. LiteCA只支持从网管MAE生成；自动更新期间OM Portal提示"请求错误，系统内部错误"为正常现象，等待完成后刷新即可
- **LiteCA不支持自动更新的4类证书场景**：对接syslog服务器用户设备证书、对接syslog拓展服务器1/2/3用户设备证书、运维接入设备证书
- **验证方法（7步）**：登录 U2020/MAE → 维护 > MML命令 → 选择UDG → 输入 `LST ME` → 设置参数 → 执行命令 → **预期结果：命令执行成功**（异常：收集系统日志联系华为技术支持）
- **前置条件**：网管服务器运行正常 / 网管与UDG网络正常 / 已获取UDG外网浮动IP
- **VNF LCM部署形态对步骤的影响（决策点DP-02）**：
  - **独立部署 + 已装网管适配层 + 实例化时选了EMS名称** → **不需要**配置网元和网管对接（步骤4可跳过）
  - **独立部署 + 未装网管适配层 + 实例化时选了EMS名称** → 网管已创建网络拓扑，仅执行步骤3安装网管适配层，**不需要**执行步骤4
  - 其他形态 → 完整执行5步
- **来源**：配置网元和网管对接_34981624.md
- **核心度**：★★★★★（CS-3对接面核心闭包）
- **关联特性**：**NPFD-010000 操作维护功能**（OM Portal 北向/SNMP/证书属操作维护范畴）
- **关联命令**：SET NEWCERTSWITCH（证书开关，LiteCA前置）、LST ME（验证）
- **关联配置对象**：北向对接用户、SNMP用户、网管适配层、网元（网管侧创建）、EMS
- **对接面**：**CS-3（网管对接）**

---

## 3. 关键发现

### 发现1：KP-02 与 KP-06 的强耦合 — 修改浮动IP必触发CS-3重对接
`修改网元基本信息`（SET OMIP）修改浮动IP后，**网管与网元连接中断，需重新对接网管**；同时VNFM连接也中断。这意味着 CS-5 的网元身份变更会**强制回流到 CS-3** 重做对接流程（KP-06 步骤1~5），且 SET OMIP 本身是默认二次授权命令（KP-03），需先完成二次授权配置。三者形成：**二次授权配置（KP-03）→ 修改网元信息（KP-02）→ 重对接网管（KP-06）** 的串行链。

### 发现2：KP-04 IPv6分片策略 与 KP-05 MTU 的业务稳定性联动
公共参数 `SET IPV6FRAGPLCY: INNERIPV6FRAGPLCY=TOOBIG_PKTDROP`（初始值）在 UPF 封装后报文 > MTU 时丢弃报文并回 Too big；如果 MTU（KP-05）规划偏小或对接链路MTU不一致，会触发丢包。**业务稳定场景需将 INNERIPV6FRAGPLCY 改为 OUTERFRAG**，由 UPF 做外层IPv6分片。两参数必须协同规划。

### 发现3：KP-03 高危命令清单覆盖了 KP-02/KP-04/KP-05 的关键MML
UDG 默认二次授权命令清单中：
- `SET OMIP`（KP-02 修改网元基本信息）
- `SET CNTTMPDIR`（容器引擎，公共参数相关）
- IPsec 系列命令（仅升级路径触发）
这意味着任何自动化开局脚本执行基础数据配置时，**必须先开启二次授权（SET SECAUTH:STATUS=ON）并配置二次授权用户**，否则高危MML会因弹窗阻塞而卡住。

### 发现4：CS-3网管对接的"密码三元组"约束
KP-06 的3类帐号（网管用户 / 北向对接用户 / SNMP用户）中，**后两类有严格的初次对接密码约束**：
- 北向对接用户：**必须重置密码**
- SNMP用户：**必须重置共享认证密钥和共享加密密钥，且两者不能相同**
任何一项不满足，对接直接失败。这是开局最常见的对接失败原因，需在第1层业务图谱中作为**前置检查项**强调。

### 发现5：MTU 的 Eth-trunk 特殊约束（易踩坑）
Eth-trunk 接口组网时**不需要修改成员接口MTU**；若成员接口在加入 Eth-trunk **前**修改了MTU，会导致**添加成员接口失败**。这是 KP-05 中最隐蔽的约束，需在自动部署/扩容场景下重点提示。

### 发现6：自动部署模板MTU同步避免告警 ALM-232398849
仅修改接口MTU而不同步 `MOD AUTOSCALINGSERVICE` 模板，会触发告警 **ALM-232398849 接口自动化配置失败**，且后续扩容新接口仍需逐个修改。完整MTU修改必须包含模板同步4步（LST AUTOCONFIG → SET AUTOCONFIG:FALSE → MOD AUTOSCALINGSERVICE → SET AUTOCONFIG:TRUE）。

---

## 4. 对接面与决策点归纳（★供第1层业务图谱）

### CS-3网管对接方案要素（CS-3 闭包）
| 要素 | 内容 | 来源KP |
|------|------|--------|
| 前置帐号准备 | 网管用户 + 北向对接用户（必须重置密码）+ SNMP用户（必须重置共享认证/加密密钥且不相同） | KP-06 |
| 北向对接用户密码 | 初次对接必须重置，参见 _74094640.md | KP-06 |
| SNMP共享密钥 | OM Portal "系统 > SNMP管理 > 重置共享密钥" | KP-06 |
| 网管适配层安装 | 华为支持网站下载版本配套软件 → 网管侧安装 | KP-06 |
| 创建网元14项关键参数 | 名称 / IP（外网浮动IP）/ TLS连接 / OSS认证（证书/匿名）/ emscomm账号+密码 / SNMPV3 / v3User / 端口8000 / SHA512+AES256（推荐） | KP-06 |
| 证书场景 | LiteCA自动更新5前置条件；4类证书场景不支持自动更新 | KP-06 |
| EMS归属检查 | VNF LCM 独立部署时在 "VNFM-EMS管理" 检查 | KP-06 |
| 验证 | U2020/MAE 执行 LST ME 成功 | KP-06 |
| TLS连接 | 网元连接类型默认 TLS | KP-06 |

### CS-5基础就绪要素（CS-5 闭包）
| 要素 | 内容 | 来源KP |
|------|------|--------|
| NTP时间同步 | OMC + FusionStage 双路；NPFD-010014 | KP-01 |
| 网元基本信息 | MOD ME 改名 + SET OMIP 改浮动IP/物理IP | KP-02 |
| 高危命令二次授权 | SET SECAUTH + ADD USRSECAUTH + ADD SECAUTHMEM；13类UDG默认清单 | KP-03 |
| 公共参数 — 协议层 | SET SIGDSCP（PFCP DSCP=46）/ SET UDPCHECKSUM（IPv6必须ENABLE） | KP-04 |
| 公共参数 — 用户面 | SET SRVCOMMONPARA（五元组600→1000）/ SET CPTEIDUALLOC（DISABLE由UP分配） | KP-04 |
| 公共参数 — QoS | SET QOSCAR（HOME/ROAMING/VISITING × 10 RAT） | KP-04 |
| 公共参数 — 分片 | SET IPV6FRAGPLCY（初始TOOBIG_PKTDROP→OUTERFRAG） | KP-04 |
| 公共参数 — 系统 | SET TZ（时区）/ SET ANTIFRAUD（防欺诈）/ SET FWDPARA（**高危**）/ SET HEADENGLBPARA / SET MSFAULTALARM | KP-04 |
| MTU调整 | SET FABRICMTU / MOD INTERFACE / SET IFIPV6ENABLE + 自动部署模板 MOD AUTOSCALINGSERVICE；层级约束 网卡≥Fabric>主接口≥子接口 | KP-05 |

### 决策点 DP（供业务图谱 constrained_by / variant_dimensions）

**DP-01: 网管对接认证模式 × 协议版本 × 加密协议（三方阵）**
- OSS认证模式：证书认证 vs 匿名认证
- 协议版本：SNMPV3（推荐） vs 其他
- 授权协议：SHA512（推荐） vs SHA256/SHA384 vs SHA（不安全，告警ALM-136750）
- 加密协议：AES256（推荐） vs AES192/AES128
- 影响：创建网元参数填写、密钥协商、弱算法告警风险

**DP-02: VNF LCM 部署形态 × 网管适配层安装时序（决定CS-3步骤数）**
- 独立部署 + 已装适配层 + 实例化选EMS → **跳过**配置网管对接
- 独立部署 + 未装适配层 + 实例化选EMS → **仅执行**安装适配层（步骤3）
- 合设部署 / 未选EMS → 完整执行5步
- 影响：CS-3流程裁剪、是否需要VNFM-EMS管理检查

**DP-03: 证书更新路径（LiteCA自动 vs 手动）**
- 自动路径前置：MAE + V100R024C10+ + SET NEWCERTSWITCH=ON + OM类型证书 + 华为域内设备 + MAE已创建默认CA
- 不支持自动的4类场景：syslog服务器/拓展1/拓展2/拓展3 用户设备证书 + 运维接入设备证书 → 必须手动
- 影响：是否需要在网元侧执行 SET NEWCERTSWITCH、证书获取流程

**DP-04: IPv6分片策略 × MTU规划（业务稳定性）**
- INNERIPV6FRAGPLCY=TOOBIG_PKTDROP（初始）+ MTU偏小 → 丢包+Too big
- INNERIPV6FRAGPLCY=OUTERFRAG + MTU对齐 → UPF外层分片，业务稳定
- 影响：丢包风险、与KP-05 MTU规划强相关

**DP-05: 外联口组网类型（Ethernet vs Eth-trunk）× 子接口（影响MTU修改路径）**
- Ethernet组网：主接口 + 可选子接口 MTU 修改
- Eth-trunk组网：仅主接口 MTU 修改，**不改成员接口**（加入前改MTU会失败）
- 影响：MTU修改MML分支选择、扩容脚本

**DP-06: 自动部署模式 × 自动配置开关（MTU模板同步）**
- 自动配置开关=是 → 完整4步同步模板（LST/SET FALSE/MOD/SET TRUE）
- 自动配置开关=否 → 仅执行 MOD AUTOSCALINGSERVICE
- 影响：是否触发告警ALM-232398849、扩容新接口是否需逐个改MTU

**DP-07: 浮动IP是否变更（触发CS-3回流）**
- 变更 → OM Portal退出 + 网管连接中断 + VNFM连接中断 → 必须重对接网管（CS-3回流）+ VNFM修改IP
- 不变 → 仅改网元名称（MOD ME），无需重对接
- 影响：是否触发CS-3完整流程重跑
