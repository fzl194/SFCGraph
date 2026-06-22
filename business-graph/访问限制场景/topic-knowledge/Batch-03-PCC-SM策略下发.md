# Batch-03: PCC-SM策略下发（UNC侧）——重定向动作下发链路
> 批次 03 | 主题 SM策略生成/下发/执行 + 重定向动作 + 预定义规则组机制 | 来源 UNC WSFD-109101(10) + SM策略解决方案(8) | 文件数 18 | 核心度 ★★★★★

## 1. 概述（本批次文档覆盖的板块）

本批次是UNC（SMF/AMF）侧的PCC-SM策略完整视图，**重点揭示重定向动作如何从PCF决策经SMF翻译到UPF执行**：

| 板块 | 来源文件 | 核心内容 |
|------|----------|----------|
| PCC 5G特性概述 | `WSFD-109101 PCC基本功能特性概述（适用于5G）_71770359.md` | 适用NF=AMF/SMF；PCF发现选择；动态PCC vs 本地PCC；DNN粒度混合 |
| PCC 5G核心概念 | `实现原理/相关概念_71770360.md` | AM/UE/SM策略；**PCR Trigger（5 AMF + 24 SMF触发器）**；规则优先级 |
| PCC 5G参考信息 | `WSFD-109101 PCC基本功能（5G）参考信息_72466541.md` | UNC侧20+ MML命令；软参；测量指标 |
| PCC 5G激活 | `激活PCC基本功能_72467890.md` | AMF/SMF两侧PCC激活流程；PCF选择策略；UserProfile+DNAI下发 |
| SM策略整体介绍 | `整体介绍_86483627.md` | **SM策略三内容：QoS+计费+短信或重定向** |
| SM策略原理概述 | `原理概述_15464534.md` | 策略生成→下发→执行三阶段；PCF决策垄断 |
| 规则相关概念 | `规则相关概念_17152898.md` | PCF下发 vs SMF本地；**静态规则=预定义+本地** |
| 动态规则 | `动态规则_86483635.md` | UPCF策略架构（触发器+条件组+动作组）；**动作含重定向** |
| 预定义/本地规则 | `预定义规则_预定义规则组_本地规则_86483636.md` | UPF识别业务；6条预定义规则完整示例；**PCC vs BWM策略类型差异** |
| 业务识别与分流 | `业务识别与分流_86483639.md` | PF/PFS包过滤器；4G一级映射 vs 5G两级映射 |
| QoS Flow建改删 | `QoS Flow建立_修改_删除_86483638.md` | 默认/专有QoS Flow；5QI判断新建/修改/删除 |
| **重定向** | `重定向_86483631.md` | **重定向两大触发场景**（配额耗尽+特定区域） |
| 短信/邮件通知 | `短信_邮件通知_86483632.md` | UPCF通过SMSC/Email/SOAP通知；可并用重定向 |

**对访问限制场景的核心价值**：明确揭示了**SM策略的"短信或重定向"内容**是访问限制REDIRECT动作的策略载体，并给出了重定向的两大触发场景（配额耗尽、特定区域）。

## 2. 核心知识点

### KP-01: PCC 5G架构与网元分工（UNC侧） — ★★★★★

> SourcePath: `特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能特性概述（适用于5G）_71770359.md`

**适用NF**：AMF、SMF（本特性）、UPF、PCF、UCF、UE

**网元功能分工**：

| 网元 | 功能 | 访问限制相关性 |
|------|------|----------------|
| **PCF** | UE/AM/SM策略决策与控制（最高决策权） | 重定向/URL过滤策略决策 |
| **AMF** | 从PCF接收UE/AM策略→传递UE/(R)AN；上报订阅事件；无PCF时本地配置AM策略 | **SAR服务区限制=接入控制** |
| **SMF** | 从PCF接收SM策略→执行；生成PDR下发给UPF；上报订阅事件；无PCF时本地配置SM策略 | **重定向策略翻译为PDR给UPF** |
| **UPF** | 执行数据包检测；**执行门控、重定向等用户面策略执行** | **★重定向/URL过滤执行点** |
| UCF | 存储用户信息和业务签约信息 | 签约数据源 |
| UE | 执行UE策略 | 路由选择 |

**License控制项**：
- AMF：`82209964 LKV2PCCBF01 PCC基本功能-UAM`
- SMF：`82207979 LKV3W9SPCC11 PCC基本功能`

**特性规格**：
- 支持配置UserProfile个数（整机）：**5000个**
- 单个QoS Flow支持安装规则个数（动态+预定义）：**50个**

### KP-02: 动态PCC vs 本地PCC（DNN粒度混合） — ★★★★

> SourcePath: 同上 §原理概述

**动态PCC**：SMF通过PCF获取SM策略。PCF向AMF/SMF下发UE/AM/SM策略+PCR Trigger。

**本地PCC**：SMF直接使用本地配置策略，不与PCF交互。以**DNN粒度**配置。

**★混合部署能力★**：可在**一个UNC上实现基于DNN混合使用动态PCC和本地PCC**。例如配置DNN1用本地PCC、DNN2用动态PCC。

**PCF发现和选择**：
- AMF方式：切换时从老AMF获取；本地运营商策略；NRF NF发现
- SMF方式：PDU会话建立时从AMF获取；本地运营商策略；NRF NF发现
- 选择因素：本地运营商策略、DNN、S-NSSAI、SUPI范围
- **PCF主备容灾**：支持failover一次；超时根据 `SET PCCFAILACTION` 决定回落本地PCC或会话失败

### KP-03: 三类策略获取流程 — ★★★★

> SourcePath: 同上 §UE/AM/SM策略获取

| 策略 | 获取时机 | 关键动作 |
|------|----------|----------|
| **UE策略** | 用户注册时 | AMF向PCF发起UE策略关联，获取UE策略→发送给UE |
| **AM策略** | 用户注册时 | AMF向PCF发起AM策略关联，获取AM策略+AMF PCR Trigger；根据是否含**SAR和RFSP**保存并下发(R)AN/UE |
| **SM策略** | PDU会话建立时 | SMF向PCF发起SM策略关联，获取SM策略+SMF PCR Trigger；**生成PDR下发给UPF**，指示执行转发/QoS/时长流量上报等 |

**关键能力**：SMF支持将**预定义规则/预定义规则组/本地规则**下发给：
- 主锚点UPF + 辅锚点UPF
- 仅主锚点UPF
- 仅辅锚点UPF
- 指定的辅锚点UPF（DNAI粒度）

### KP-04: PCR Trigger（AMF 5 + SMF 24类） — ★★★★★（访问限制触发条件清单）

> SourcePath: `实现原理/相关概念_71770360.md` §PCR Trigger

**AMF PCR Trigger**（适用AM/UE策略）：

| 事件 | 描述 | 上报条件 | 访问限制相关性 |
|------|------|----------|----------------|
| **LOC_CH** | UE跟踪区TA改变 | PCF下发 | 位置类接入控制 |
| **PRA_CH** | 用户进入/离开PRA | PCF下发 | **★基于区域的重定向** |
| **SERV_AREA_CH** | 签约SAR改变 | AMF默认上报 | **★服务区限制变更** |
| RFSP_CH | RFSP索引改变 | AMF默认上报 | 无线资源管理 |
| ALLOWED_NSSAI_CH | 允许NSSAI改变 | PCF下发 | 切片接入控制 |

**SMF PCR Trigger**（适用SM策略，节选访问限制相关）：

| 事件 | 描述 | 上报条件 | 访问限制相关性 |
|------|------|----------|----------------|
| PLMN_CH | PLMN变更 | PCF下发 | 漫游重定向 |
| AC_TY_CH | 3GPP/非3GPP接入类型变化 | PCF下发 | 接入类型策略 |
| **UE_IP_CH** | UE IP分配/释放 | SMF默认上报 | IP类访问限制 |
| **UE_MAC_CH** | UE MAC地址变化 | PCF下发 | MAC类访问限制 |
| **US_RE** | 资源/监控关键资源达门限 | PCF下发 | **★配额耗尽触发重定向** |
| APP_STA | 应用程序流量开始 | PCF下发 | 应用类访问限制 |
| APP_STO | 应用程序流量结束 | PCF下发 | 应用类访问限制 |
| **NO_CREDIT** | 信用失效（配额申请失败） | PCF下发 | **★配额耗尽触发重定向** |
| **PRA_CH** | UE所处位置PRA变化 | PCF下发 | **★基于区域的重定向** |
| **SAREA_CH** | 服务区域（跟踪区）变化 | PCF下发 | 位置类策略 |
| **SCELL_CH** | 服务小区变化 | PCF下发 | 小区级策略 |
| **USER_LOCATION_CH** | SAREA/SCELL/二者组合 | PCF下发 | 综合位置策略 |
| RAT_TY_CH | 无线接入类型变化（4G/5G切换） | PCF下发 | 互操作策略 |
| DEF_QOS_CH | 默认QoS变更 | SMF默认上报 | QoS类策略 |
| SE_AMBR_CH | Session-AMBR变更 | SMF默认上报 | 带宽类策略 |

**关键发现**：**US_RE、NO_CREDIT、PRA_CH、SAREA_CH、USER_LOCATION_CH** 这几类触发器是访问限制（特别是重定向）的主要触发条件。

### KP-05: SM策略三内容（QoS+计费+短信或重定向） — ★★★★★（访问限制策略载体权威定义）

> SourcePath: `业务专题/5G PCC之SM策略解决方案/整体介绍_86483627.md`

**SM策略三方面内容**：

| 内容 | 作用 | 访问限制相关性 |
|------|------|----------------|
| **QoS** | 对UE访问DN网络的带宽、无线侧调度优先级等控制 | 带宽域（非访问限制） |
| **计费参数** | 对不同应用类型/套餐余量/位置区域的资费控制 | 计费域（非访问限制） |
| **★短信或重定向★** | 对不同套餐余量/位置区域变更/漫游状态等进行**短信通知用户或将用户访问网页重定向到运营商首页充值**等控制 | **★★★★★ 访问限制REDIRECT策略载体** |

**关键定位**：SM策略的"短信或重定向"内容是**访问限制场景中重定向动作的策略层定义点**。这回答了"重定向策略在哪里定义"——在SM策略的第三类内容中。

### KP-06: SM策略生成-下发-执行三阶段 — ★★★★

> SourcePath: `业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/原理概述_15464534.md`

| 阶段 | 步骤 | 网元 | 说明 |
|------|------|------|------|
| **策略生成** | 1a/1b | UDM→SMF→PCF | 用户上线从UDM获取签约Session-AMBR/ARP/5QI；PCF根据切片/位置信息**决策**生成策略；**完全由PCF决策，无协商** |
| **策略下发** | 2a/2b/2c | SMF→UPF/RAN/UE | SMF将QoS策略分别下发UPF、RAN（经AMF透传）、UE |
| **策略执行** | 3 | UPF/RAN/UE | 将业务流基于QoS策略映射到QoS Flow/DRB |

**PCF决策垄断**：策略生成**完全由PCF决策**，不存在与UDM、SMF协商。PCF能根据用户位置、等级、时间段、配额状态、节假日等灵活定制。

**本地策略回退**：网络未开启PCC或PCF异常导致N7不可达时，SMF本地也能配置策略，但**精细化程度低于PCF策略**。

### KP-07: UPCF策略架构（触发器+条件组+动作组） — ★★★★★（重定向动作定义点）

> SourcePath: `业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略生成原理/动态规则_86483635.md`

**UPCF侧SM策略关键参数**：

| 参数 | 解释 |
|------|------|
| 策略 | 若干触发器+规则的组合；任一触发器事件发生→下发规则 |
| 配额 | 流量配额/在线时长配额/时长配额（用于引导消费行为） |
| 漫游区 | 多PLMN集合，统一策略控制 |
| 规则 | 条件组+动作组+业务流+费率+消息通知 |
| **触发器** | IPCAN_EST（会话建立必配）/US_RE/SAREA_CH/PRA_CH/SCELL_CH/PLMN_CH/APP_STA/APP_STP等 |
| **条件组** | 用户签约信息+位置信息+上线时间+会话信息等 |
| **★动作组★** | 带宽控制+计费控制+**消息通知**+**重定向**等 |

**★动作组明确枚举（访问限制核心）★**：
> 动作是规则中配置的操作，包括带宽控制、计费控制、**消息通知**和**重定向**等。
> - 控制上网速率：上下行带宽、是否建业务访问专有通路（专有QoS Flow）等
> - 控制短信发送
> - 控制邮件发送
> - **重定向：套餐耗尽后，禁止上网，重定向到运营商充值首页**

**策略计算逻辑**："在XX**触发**下，**if 满足XX条件 then 执行XX动作**"

**关键发现**：**重定向和消息通知是UPCF动作组的官方枚举项**——访问限制REDIRECT动作在PCF策略层的标准定义。

### KP-08: 动态规则vs静态规则使用场景 — ★★★★

> SourcePath: `业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略生成原理/规则相关概念_17152898.md`

**PCC策略来源两种**：
- **PCF下发**（动态PCC）：PCF定义，SMF执行；可下发动态规则/预定义规则/预定义规则组
- **SMF本地策略**（本地PCC）：SMF/UPF本地配置；PCF下发优先级高于本地

**规则定义对比表**（PCF/SMF/UPF分工）：

| 规则类别 | PCF | SMF | UPF |
|----------|-----|-----|-----|
| 动态规则 | 定义规则名+内容，下发完整规则 | 透传规则内容给UPF/RAN/UE | 按接收规则处理 |
| 预定义规则（1条） | 定义与SMF/UPF一致的规则名，只下发名称 | 定义规则名，透传名称给UPF | **定义规则名+具体内容**，按名称匹配本地规则 |
| 预定义规则组（1组） | 定义与SMF/UPF UserProfile同名的名称 | 定义UserProfile名+多规则绑定 | **定义规则内容**，按UserProfile匹配，按UserProfile内优先级处理 |
| 本地规则 | 与PCF无关 | 定义UserProfile名，下发名称 | **定义规则内容**，按UserProfile匹配 |

**优先级规则**：
- 全局规划，值越小优先级越高
- 同优先级时：**动态规则 > 预定义规则**
- rule优先级=SMF侧定义的全局优先级，与UserProfile内优先级无关

### KP-09: 静态规则=预定义+本地（PCF无七层识别能力） — ★★★★★

> SourcePath: `业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略生成原理/预定义规则_预定义规则组_本地规则_86483636.md`

**核心约束（重申）**：
> 在PCC功能开关正常开启的组网中，QoS策略只能由PCF生成，由于**PCF不具备业务识别能力**，而UPF具备该能力，因此对于需要对特定业务类型如带宽抢占较强的视频业务进行限速控制等，此时**业务的识别操作只能在UPF上进行**。UPF识别业务的配置过程即为静态规则的配置。

**UPF支持的流条件**：
- 三四层特征：IP、Port、三四层协议
- **七层特征：URL、HOST、七层协议**
- 组合：三四层any+特定七层 / 特定三四层+特定七层 / 特定三四层 / 三四层any+七层any

**UPF支持的流动作**：计费、带宽管理、**头增强**、QoS等；单动作或组合动作。

**PCC策略类型 vs BWM策略类型（关键差异）**：
- **PCC策略类型**：定义整个QoS Flow级的整体QoS控制（如所有业务带宽合计≤100Mbps）
- **BWM策略类型**：定义QoS Flow中的带宽管理分类策略（如100Mbps内FTP≤20Mbps、HTTPS≤50Mbps、其他≤30Mbps）

**本地规则使用场景**：
- 现网部署PCF时，SMF/UPF本地都会配置本地规则，**用于异常情况下保证业务连续性**
- 现网未部署PCF或SMF未开启PCC开关
- SMF-PCF链路故障
- PCF签约异常/下发策略异常且SMF配置回滚本地PCC

**本地规则限制**：SMF不支持实时更新，新增绑定规则需用户下次上线才生效。

### KP-10: 预定义规则6规则完整示例（配置逻辑） — ★★★★

> SourcePath: 同上 §示例分析

**业务套餐**（20G通用+30G A视频专项）的6条预定义规则规划：

| 套餐 | 规则 | PCF | SMF | UPF（流匹配） | 策略类型 | 优先级 |
|------|------|-----|-----|---------------|----------|--------|
| 1 | Prerule01 | 下发UmData监控A视频用量 | UmData→MK URR传UPF | URL:www.example.com+HTTP | PCC | 高 |
| 2 | Prerule02 | 每天凌晨下发 | BWM | URL:www.example.com+HTTP | BWM(100Mbps) | 高 |
| 2' | Prerule03 | 超2000M删除Prerule02下发Prerule03 | BWM | URL:www.example.com+HTTP | BWM(25Mbps) | 高 |
| 3 | Prerule04 | 下发UmData监控通用用量 | UmData→MK URR传UPF | 三四层any+七层any | PCC | 较高 |
| 4 | Prerule05 | 通用<20G下发 | BWM | 三四层any+七层any | BWM(50Mbps) | 较高 |
| 4' | Prerule06 | 通用>20G删除Prerule05下发Prerule06 | BWM | 三四层any+七层any | BWM(1Mbps) | 较高 |

**三网元参数一致性约束**：
- 同一预定义规则：**PCF/SMF/UPF规则名称必须一致**
- 同一预定义规则：**SMF/UPF的URR ID必须一致**

**规则安装流程**：
1. 用户开机→PDU会话创建请求
2. SMF选择PCF，建立SM策略偶联，获取SM策略
3. PCF决策生成规则，下发预定义规则名+Triggers
4. SMF选择UPF，发起会话建立请求（携带预定义规则名+Triggers）
5. UPF安装规则，返回响应；UPF对报文做业务识别，匹配Filter/L7filter，按动作处理

**规则更新流程**（流量累计达阈值）：
- PCF更新规则（删除Prerule02，安装Prerule03）
- SMF/UPF删除旧规则，安装新规则
- 后续报文按新规则处理

### KP-11: 重定向两大触发场景 — ★★★★★（访问限制REDIRECT触发条件权威定义）

> SourcePath: `业务专题/5G PCC之SM策略解决方案/SM策略关键内容/重定向_86483631.md`

**重定向定义**：SM策略中的关键参数类型，当用户触发重定向规则，将用户当前访问状态**重定向到某个服务页的URL地址**。

**★用户侧触发重定向的两大原因★**：

| 触发场景 | 描述 | 典型用例 |
|----------|------|----------|
| **基于配额/资费消耗** | 流量配额或资费耗尽时，及时提醒用户充值 | **重定向到运营商充值首页** |
| **进入特定位置区域** | 出国、热点接入区域等，引导签约优惠套餐 | **重定向到套餐订购页面或免费接入网络验证页面** |

**关键发现**：重定向的两大触发场景完全对应访问限制的业务目标——配额耗尽重定向（业务5）和区域引导重定向（如Captive Portal）。

### KP-12: 短信/邮件通知（可与重定向并用） — ★★★

> SourcePath: `业务专题/5G PCC之SM策略解决方案/SM策略关键内容/短信_邮件通知_86483632.md`

**通知机制**：UPCF通过SMSC、Email服务器、SOAP服务器给终端用户发送通知，提醒业务状态。**特殊地，UPCF也支持通过重定向方式提醒业务状态**。

**特性**：
- 支持短信通知与邮件通知独立发送，速度互不影响
- 支持配置通知发送时间段（避免休息时间打扰）
- 支持控制通知发送速度（避免对端无法处理）
- 支持按IMSI号段配置不同通知内容

### KP-13: 业务识别与分流（4G vs 5G映射机制） — ★★★

> SourcePath: `业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略下发与执行原理/业务识别与分流_86483639.md`

| 对比项 | 4G | 5G |
|--------|-----|-----|
| 映射机制 | 一级映射：数据包→EPS Bearer | **两级映射：数据包→QoS Flow→Radio Bearer** |
| 特征 | 对称性（上下行处理一致） | **不对称性**（上下行处理不一致） |
| UL执行网元 | UE | UE |
| DL执行网元 | P-GW | **UPF、RAN** |
| UL关联工具 | UL TFT | **QoS Rule（N:1 QoS Flow）+空口映射规则** |
| DL关联工具 | DL TFT | **PDR（N:1 QoS Flow）+空口映射规则** |

**5G关键机制**：一个PDU会话共用一个NG-U隧道；通过QFI区分QoS Flow（类似公交车线路标识）。

### KP-14: PCC激活流程（AMF+SMF两侧） — ★★★★

> SourcePath: `激活PCC基本功能_72467890.md`

**AMF侧PCC激活步骤**：
1. 打开License开关（`SET LICENSESWITCH`）
2. 配置AMF选择PCF策略（`ADD PCFSELPLCY`）
3. 配置应用网络侧AM/UE策略的用户群（`ADD AMUEPLCYCTRL`，ISAMASSOC=YES/ISUEASSOC=YES）
4. （可选）修改用户群应用本地AM/UE策略（`MOD AMUEPLCYCTRL`，设为NO）
5. （可选）设置实时通知PCF删除AM/UE偶联（`SET AMFPLCYFUNC`）
6. 配置本地RFSP索引（`ADD NGMMSUBDATA`，未签约RFSP ID时）
7. 配置AMF支持PCF通过Location信元通信（`SET AMFPEERSELFUNC`）

**SMF侧PCC激活步骤**：
1. 打开License开关
2. 使能SMF全局PCC功能（`SET PCCFUNC`：HOMEPCCSWITCH/ROAMPCCSWITCH/VISITPCCSWITCH=ENABLE）
3. （可选）配置N7接收信元处理（`SET N7RCVATTRCTRL`）
4. 配置PCC模板（`ADD PCCTEMPLATE`）
5. 配置APN PCC功能（`SET APNPCCFUNC`：APN粒度ENABLE/DISABLE/INHERIT）
6. 配置PCF业务服务区（`ADD PCFSSCOPE`/`ADD USRTAIRANGE`/`ADD PCFSSCOPEBIND`）
7. 配置PCC策略组（`ADD PCCPOLICYGRP`）
8. 配置规则（`ADD RULE`，含RULERANGE=ALL/CENTRAL/LOCAL）
9. 配置UserProfile（`ADD USERPROFILE`，含PROFILERANGE=ALL/CENTRAL/LOCAL）
10. 配置规则绑定（`ADD RULEBINDING`）
11. 配置用户模板组（`ADD USRPROFGROUP`/`ADD UPBINDUPG`/`ADD APNUSRPROFG`）

**关键参数**：
- `SET APNPCCFUNC` 的 HOMEPCCSWITCH/ROAMPCCSWITCH/VISITPCCSWITCH：ENABLE=动态PCC，DISABLE=本地PCC，INHERIT=继承SET PCCFUNC
- `ADD RULE` 的 RULERANGE：**ALL（主+辅锚点）/CENTRAL（仅主锚点）/LOCAL（仅辅锚点）**
- `ADD PCCTEMPLATE` 的 N7FAILOVERSW：PCF主备容灾开关

### KP-15: UNC侧PCC核心MML命令清单 — ★★★★★

> SourcePath: `WSFD-109101 PCC基本功能（5G）参考信息_72466541.md` + 激活PCC基本功能

| 命令 | 用途 | 访问限制相关性 |
|------|------|----------------|
| **SET PCCFUNC** | 设置SMF全局PCC功能 | ★★★★★ 动态/本地PCC切换 |
| **ADD PCCTEMPLATE** | 增加PCC模板 | ★★★★ PCC模板配置 |
| **SET APNPCCFUNC** | 设置APN PCC功能 | ★★★★ DNN粒度动态/本地PCC |
| **SET PCCFAILACTION** | 设置PCC故障处理 | ★★★ PCF故障回退本地PCC |
| **ADD PCFSELPLCY** | 增加PCF选择策略 | ★★ AMF选PCF |
| **ADD AMUEPLCYCTRL** | 增加AM/UE策略控制参数 | ★★★ AM/UE策略应用 |
| **ADD NGMMSUBDATA** | 增加用户移动性管理参数 | ★★ RFSP配置 |
| **ADD PCFSSCOPE** | 增加PCF业务服务区 | ★★ PCF选择 |
| **ADD USRTAIRANGE** | 增加用户TAI区域 | ★★ 位置类PCF选择 |
| **ADD PCFSSCOPEBIND** | 增加PCF业务服务区绑定 | ★★ PCF选择 |
| **ADD PCCPOLICYGRP** | 增加PCC策略组（UNC侧） | ★★★★★ PCC动作载体 |
| **ADD RULE** | 增加规则（UNC侧） | ★★★★★ 规则定义 |
| **ADD USERPROFILE** | 增加用户模板（UNC侧） | ★★★★ 规则组容器 |
| **ADD USRPROFGROUP** | 增加用户模板组 | ★★★ UserProfile组 |
| **ADD RULEBINDING** | 增加规则-用户模板绑定 | ★★★★ 规则激活 |
| **ADD UPBINDUPG** | 增加用户模板-模板组绑定 | ★★★ 模板组组装 |
| **ADD APNUSRPROFG** | 增加APN-用户模板组绑定 | ★★★ DNN级规则 |
| **ADD RULEBINDDNAI** | 增加预定义规则-DNAI绑定 | ★★★ 辅锚点UPF下发 |
| **ADD USRPROBINDDNAI** | 增加用户模板-DNAI绑定 | ★★★ 辅锚点UPF下发 |
| **SET AMFPLCYFUNC** | 设置AMF策略功能 | ★★ AM/UE偶联管理 |
| **SET N7RCVATTRCTRL** | 设置N7接收信元处理 | ★★ N7接口控制 |
| **SET N7SNDATTRCTRL** | 设置N7发送信元处理 | ★★ N7接口控制 |
| **SET AMFPEERSELFUNC** | 设置AMF对端选择功能 | ★★ PCF Location通信 |

## 3. 关键发现（跨文档归纳的隐性规则/约束）

### 发现-1: SM策略"短信或重定向"是访问限制REDIRECT的策略层定义点
SM策略三方面内容明确为"QoS+计费参数+**短信或重定向**"。重定向作为SM策略的独立内容类型，是访问限制REDIRECT动作的策略层载体。**图谱落位**：业务层（BD）的"重定向业务规则"应关联SM策略的"短信或重定向"内容对象。

### 发现-2: 重定向两大触发场景覆盖访问限制全部REDIRECT用例
重定向的两大触发场景：**基于配额/资费消耗**（重定向充值页）+ **进入特定位置区域**（重定向套餐订购/验证页）。这两类场景完全覆盖了访问限制场景的重定向族特性（HTTP智能重定向、用户Portal、DNS纠错等）。**图谱落位**：重定向族特性的业务触发条件应映射到这两类场景。

### 发现-3: PCF决策垄断（无协商）决定访问限制策略必须PCF侧完整定义
SM策略生成"完全由PCF决策，不存在与UDM、SMF协商的过程"。PCF能根据用户位置/等级/时间段/配额状态/节假日等灵活定制。这意味着访问限制的策略逻辑（如"套餐耗尽→重定向"）必须在PCF侧完整定义。**图谱落位**：访问限制策略决策点是PCF，非SMF/UDM。

### 发现-4: UPCF动作组官方枚举含"重定向"和"消息通知"
UPCF侧动作组明确包括"带宽控制、计费控制、**消息通知**和**重定向**"。特别是"重定向：套餐耗尽后，禁止上网，重定向到运营商充值首页"——这是PCF策略层对访问限制REDIRECT动作的官方定义。**图谱落位**：第4层动作对象应包含"重定向动作"和"消息通知动作"两类。

### 发现-5: US_RE/NO_CREDIT/PRA_CH是访问限制重定向的主触发器
SMF PCR Trigger中，**US_RE（资源达门限）、NO_CREDIT（信用失效）、PRA_CH（PRA变化）、SAREA_CH/SCELL_CH/USER_LOCATION_CH（位置变化）** 是触发访问限制（特别是重定向）的主要条件。**图谱落位**：业务层触发条件节点应关联这些PCR Trigger。

### 发现-6: 动态PCC与本地PCC可DNN粒度混合部署
一个UNC上可基于DNN混合使用动态PCC和本地PCC（DNN1本地、DNN2动态）。这意味着访问限制策略可以按DNN差异化部署——某些DNN走PCF动态决策，某些DNN走SMF本地静态规则。**图谱落位**：业务层部署决策点应支持DNN粒度策略类型选择。

### 发现-7: PCF主备容灾+failover决定访问限制策略连续性
SMF支持PCF主备容灾，对同一消息执行一次failover。若新PCF也超时，根据 `SET PCCFAILACTION` 决定回落本地PCC或会话失败。这意味着访问限制策略在PCF故障时有**本地PCC兜底机制**保证连续性。**图谱落位**：可靠性决策点——PCF故障回退本地PCC。

### 发现-8: SMF支持主辅锚点UPF差异化规则下发
SMF支持将规则下发给：主+辅锚点UPF / 仅主锚点 / 仅辅锚点 / 指定辅锚点（DNAI粒度）。访问限制规则可按UPF角色差异化部署——这意味着不同UPF可执行不同访问限制策略。**图谱落位**：第4层规则对象应有"规则生效范围（RULERANGE）"属性：ALL/CENTRAL/LOCAL。

### 发现-9: 本地规则作为访问限制异常兜底（保证业务连续性）
原文明确："现网部署了PCF时，一般使用动态规则和预定义规则，但**SMF/UPF本地都会配置本地规则，用于异常情况下保证用户业务体验的连续性**"。这意味着本地规则是访问限制的**容灾兜底方案**。**图谱落位**：本地规则对象的用途属性应为"异常兜底/业务连续性保障"。

### 发现-10: PCC策略类型 vs BWM策略类型的关键差异
PCC策略类型定义**QoS Flow整体QoS**（如总带宽≤100Mbps）；BWM策略类型定义**QoS Flow内带宽分类**（如100Mbps内FTP≤20Mbps）。访问限制的REDIRECT/DISCARD动作主要绑定**PCC策略类型**；带宽控制的限速动作绑定**BWM策略类型**。**图谱落位**：策略类型对象应区分PCC/BWM，动作映射应体现此差异。

### 发现-11: UserProfile规格限制（整机5000，单QoS Flow 50规则）
UserProfile整机5000个，单个QoS Flow支持安装50个规则（动态+预定义合计）。这是访问限制规则部署的容量约束。**图谱落位**：第4层ConfigObject容量规格节点。

---

**涉及的配置对象（UNC侧，供第4层图谱引用）**：
- **PCCTEMPLATE**（PCC模板，动态/本地PCC选择）
- **PCCPOLICYGRP**（PCC策略组，UNC侧动作载体）
- **RULE**（规则，含RULERANGE=ALL/CENTRAL/LOCAL）
- **USERPROFILE**（用户模板，含PROFILERANGE=ALL/CENTRAL/LOCAL）
- **USRPROFGROUP**（用户模板组）
- **RULEBINDING / UPBINDUPG / APNUSRPROFG**（三级绑定关系）
- **RULEBINDDNAI / USRPROBINDDNAI**（DNAI绑定，辅锚点下发）
- **PCFSELPLCY / PCFSSCOPE / USRTAIRANGE / PCFSSCOPEBIND**（PCF发现选择）
- **AMUEPLCYCTRL / NGMMSUBDATA**（AM/UE策略控制+RFSP）

**涉及的MML命令（UNC侧）**：
SET PCCFUNC, ADD PCCTEMPLATE, SET APNPCCFUNC, SET PCCFAILACTION, ADD PCFSELPLCY, ADD AMUEPLCYCTRL, ADD NGMMSUBDATA, ADD PCFSSCOPE, ADD USRTAIRANGE, ADD PCFSSCOPEBIND, ADD PCCPOLICYGRP, ADD RULE, ADD USERPROFILE, ADD USRPROFGROUP, ADD RULEBINDING, ADD UPBINDUPG, ADD APNUSRPROFG, ADD RULEBINDDNAI, ADD USRPROBINDDNAI, SET AMFPLCYFUNC, SET N7RCVATTRCTRL, SET N7SNDATTRCTRL, SET AMFPEERSELFUNC, SET LICENSESWITCH

**涉及的信令接口**：N7（PCF↔SMF/AMF）、N15（AMF↔PCF，AM策略）、N4（SMF↔UPF，PFCP）、N14（AMF↔AMF，切换时PCR Trigger传递）
