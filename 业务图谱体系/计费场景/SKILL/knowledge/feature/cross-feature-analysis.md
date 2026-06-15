# 计费场景跨特性分析文档

> 基于 14 个特性知识文档的综合分析。每条结论标注来源特性。

---

## 一、特性分类体系

### 1.1 按产品线分类

| 分类 | 特性ID | 特性名称 | License | 首次发布 |
|------|--------|----------|---------|----------|
| **UDG/UPF（用户面）** | GWFD-110101 | SA-Basic（业务感知基本功能） | LKV3G5SABS01 | 20.0.0 |
| | GWFD-020351 | PCC基本功能 | LKV3G5PCCB01 | 20.0.0 |
| | GWFD-020301 | 内容计费基本功能 | LKV3G5BCBC01 | 20.0.0 |
| | GWFD-020302 | 基于业务时长的计费 | LKV3G5TBCS01 | 20.0.0 |
| | GWFD-020303 | 基于业务流量的计费 | LKV3G5VBCS01 | 20.0.0 |
| | GWFD-020306 | 支持事件计费 | LKV3G5EBCS01 | 20.5.0 |
| | GWFD-010171 | 离线计费 | 无需License | 20.0.0 |
| | GWFD-020300 | 在线计费 | LKV3G5OLCH01 | 20.0.0 |
| | GWFD-010173 | 融合计费 | 无需License（依赖内容计费License） | 20.0.0 |
| **UNC/SMF（控制面）** | WSFD-109101 | PCC基本功能 | LKV3W9SPCC11 | 20.0.0 |
| | WSFD-109002 | 内容计费基本功能 | LKV3W9BCC12 | 20.0.0/20.3.0 |
| | WSFD-011201 | 支持离线计费 | 无需License | 20.3.0 |
| | WSFD-011202 | 支持热计费 | SGSN需LKV2HBILL02 | 20.3.0 |
| | WSFD-011206 | 支持融合计费 | 无需额外License | 20.0.0 |

> 来源：各特性知识文档"概述"章节的License、版本信息。

### 1.2 按功能层分类

| 功能层 | 特性 | 说明 |
|--------|------|------|
| **基础能力层** | GWFD-110101 SA-Basic | 业务识别基础，所有内容计费的前置依赖 |
| | GWFD-020351 / WSFD-109101 PCC基本功能 | 策略控制基础，连接PCF/PCRF与计费执行 |
| **计量方式层** | GWFD-020301 / WSFD-109002 内容计费 | 计费三件套（URR→URRGROUP→PCCPOLICYGRP）的基础模式 |
| | GWFD-020302 时长计费 | 内容计费增强，METERINGTYPE=DURATION |
| | GWFD-020303 流量计费 | 内容计费增强，METERINGTYPE=VOLUME |
| | GWFD-020306 事件计费 | 内容计费增强，METERINGTYPE=EVENT |
| **计费模式层** | GWFD-010171 / WSFD-011201 离线计费 | 非实时，Ga/GTP'接口，无需配额管理 |
| | GWFD-020300 在线计费 | 实时，Gy/Diameter接口，配额管理 |
| | GWFD-010173 / WSFD-011206 融合计费 | 5G统一架构，Nchf/N40/HTTP2，同时支持在线+离线RG |
| | WSFD-011202 热计费 | 离线计费增强，CC=0x0100，加速话单产生 |

> 来源：GWFD-020301 定义内容计费三件套；GWFD-020302/020303/020306 各自定义计量方式为内容计费增强形式；GWFD-010173 定义融合计费为5G统一架构。

### 1.3 按是否需要License分类

| License要求 | UDG/UPF 侧 | UNC/SMF 侧 |
|-------------|-----------|-----------|
| **无需License** | GWFD-010171 离线计费、GWFD-010173 融合计费 | WSFD-011201 离线计费、WSFD-011206 融合计费 |
| **需要License** | 其余 7 个特性均需License | WSFD-109101 PCC、WSFD-109002 内容计费、WSFD-011202 热计费（仅SGSN） |

> 来源：各特性"License要求"章节。GWFD-010171 明确"无需License许可"；GWFD-010173 明确"无需获得License许可"但"需确认内容计费基本功能对应的License开关已打开"。WSFD-011202 仅 SGSN 需要 LKV2HBILL02，GGSN/SGW-C/PGW-C 无需License。

---

## 二、UPF/UDG 与 SMF/UNC 对应关系

### 2.1 特性级对应关系

| 功能域 | UDG/UPF 侧特性 | UNC/SMF 侧特性 | 对应关系 |
|--------|----------------|----------------|----------|
| 业务感知 | GWFD-110101 SA-Basic | （无独立特性，由PCC承载） | UDG负责报文解析和规则匹配；UNC通过N4下发动态规则 |
| PCC | GWFD-020351 PCC基本功能 | WSFD-109101 PCC基本功能 | **配对使用**：UNC接收PCF/PCRF策略→N4下发→UDG执行 |
| 内容计费 | GWFD-020301 内容计费基本功能 | WSFD-109002 内容计费基本功能 | **配对使用**：UDG配置FILTER/L7FILTER/FLOWFILTER+三件套；UNC配置USAGERPTMODE、PCCPOLICYGRP |
| 时长计费 | GWFD-020302 时长计费 | （无独立特性，由WSFD-109003承载） | UDG侧OFFMETERINGTYPE=DURATION；UNC侧通过内容计费或独立License |
| 流量计费 | GWFD-020303 流量计费 | （无独立特性，由WSFD-109004承载） | UDG侧OFFMETERINGTYPE=VOLUME；UNC侧通过内容计费或独立License |
| 事件计费 | GWFD-020306 事件计费 | （无独立特性） | 仅UDG侧定义，OFFMETERINGTYPE=EVENT |
| 离线计费 | GWFD-010171 离线计费 | WSFD-011201 支持离线计费 | **配对使用**：UDG收集计费信息→UNC生成话单→CG |
| 在线计费 | GWFD-020300 在线计费 | （通过Gy接口由UNC实现） | UDG上报使用量→UNC与OCS交互配额 |
| 融合计费 | GWFD-010173 融合计费 | WSFD-011206 支持融合计费 | **配对使用**：UNC与CHF交互Nchf→N4下发→UDG执行 |
| 热计费 | （无独立特性） | WSFD-011202 支持热计费 | 仅UNC侧定义，CC=0x0100控制话单优先级 |

> 来源：WSFD-109101 明确"本特性与UDG侧的GWFD-020351 PCC基本功能配合"；WSFD-109002 明确"UDG侧重用户面（业务识别与流量统计）"；GWFD-020301/WSFD-109002 各自描述C面/U面分工。

### 2.2 CU面分工原则

| 职责 | 控制面（UNC/SMF） | 用户面（UDG/UPF） |
|------|-------------------|-------------------|
| 策略接收 | 接收PCF/PCRF下发的动态规则 | 不直接对接PCF/PCRF |
| 规则管理 | 管理PCC规则、URR规则生命周期 | 接收并执行N4下发的规则 |
| 业务识别 | 不做报文解析 | 通过SA-Basic做3/4/7层解析和协议识别 |
| 流量统计 | 不统计流量/时长/事件 | 统计上下行字节、时长、事件次数 |
| 配额交互 | 与OCS/CHF交互配额 | 不直接对接OCS/CHF |
| 话单生成 | UNC生成原始话单，通过Ga/Nchf发送 | 不生成话单 |
| 计费属性 | 配置CC（Charging Characteristics）和CCT模板 | 通过N4接收计费属性 |

> 来源：GWFD-110101 描述UDG"对报文进行识别和解析，根据解析结果匹配规则"；WSFD-109101 描述UNC"接收并执行动态策略规则"；GWFD-020301 描述"UDG负责统计不同业务的上下行流量访问量，并上报给控制面（UNC/SMF）"。

### 2.3 UNC侧特有配置对象

WSFD-109002 明确指出以下配置对象**仅存在于UNC侧**，UDG侧不配置：

| UNC特有对象 | 功能 | 对应命令 |
|-------------|------|----------|
| USRPROFGROUP | UserProfile模板组 | ADD USRPROFGROUP |
| UPBINDUPG | UserProfile绑定到UPG | ADD UPBINDUPG |
| APN | APN配置 | ADD APN |
| APNUSRPROFG | APN绑定UserProfile模板组 | ADD APNUSRPROFG |
| CCT（Converged Charging Template） | 融合计费模板 | ADD CCT |

> 来源：WSFD-109002 明确"SMF侧不配置FILTER/L7FILTER/FLOWFILTER（仅UDG配置）"。WSFD-011206 定义CCT模板。WSFD-011201 定义APN相关配置。

---

## 三、计费方式差异分析

### 3.1 三种计费方式对比

| 维度 | 离线计费 | 在线计费 | 融合计费 |
|------|----------|----------|----------|
| **实时性** | 非实时 | 实时 | 同时支持实时和非实时 |
| **接口** | Ga（UNC→CG） | Gy（PGW-C→OCS） | Nchf/N40（SMF→CHF） |
| **协议** | GTP' | Diameter | HTTP/2 |
| **对端NF** | CG→BS | OCS | CHF |
| **配额管理** | 不需要申请配额 | 需要向OCS申请配额 | 在线RG申请配额，离线RG不申请 |
| **话单生成** | UNC生成→CG预处理→BS结算 | OCS实时跟踪 | CHF生成话单 |
| **用户类型** | 后付费用户 | 预付费用户 | 两者兼顾 |
| **UDG License** | 无需License | LKV3G5OLCH01 | 无需License（依赖内容计费License） |
| **适用网络** | 2G/3G/4G/5G | 2G/3G/4G | 5G（Nchf为5G引入） |
| **URR参数** | USAGERPTMODE=OFFLINE | USAGERPTMODE=ONLINE | URR中同时包含在线和离线RG |
| **超时阻塞** | 无 | T3RESPONSE*N3REQUEST+4秒 | 同在线机制 |

> 来源：GWFD-010171 离线计费定义"非实时"、"Ga接口"、"不需要申请配额"；GWFD-020300 在线计费定义"实时"、"Gy接口"、"配额管理"、超时阻塞公式；GWFD-010173 融合计费定义"Nchf/N40"、"HTTP/2"、"同时支持在线RG和离线RG"；WSFD-011206 三种计费机制对比表。

### 3.2 融合计费的关键差异：RGAPPLIED 规则

融合计费中，RGAPPLIED 参数决定URRGROUP中在线和离线RG的配置规则，这是融合计费区别于单独在线/离线计费的核心配置：

| RGAPPLIED | 含义 | URRGROUP配置规则 |
|-----------|------|-----------------|
| DEFAULT | 默认模式 | URRGROUP中**只能有一种模式**的URR（要么全在线，要么全离线） |
| ONLINERGONLY | 仅在线RG | URRGROUP中**必须同时包含**在线和离线RG |
| OFFLINERGONLY | 仅离线RG | URRGROUP中**必须同时包含**在线和离线RG |

> 来源：GWFD-010173 详细描述RGAPPLIED规则："DEFAULT→only one mode in URRGROUP; ONLINERGONLY/OFFLINERGONLY→must have both"。

### 3.3 UNC侧离线计费的CC优先级

WSFD-011201 定义了UNC侧离线计费特有的计费属性（CC，Charging Characteristics）优先级机制，UDG侧无此概念：

```
UserProfile > APN > CC > Global
```

即：UserProfile绑定的CC > APN绑定的CC > 独立CC配置 > 全局默认配置。

> 来源：WSFD-011201 "CC优先级"章节。

### 3.4 UNC侧融合计费的CHF选择机制

WSFD-011206 定义了7级CHF选择优先级，这是UNC侧融合计费特有的：

1. PCF下发的CHF地址
2. NRF发现的CHF
3. DNN配置的CHF
4. UDM下发的CHF地址
5. S-NSSAI配置的CHF
6. 用户Profile配置的CHF
7. 全局默认CHF

> 来源：WSFD-011206 "CHF选择"章节。

---

## 四、计量方式差异分析

### 4.1 三种计量方式核心参数对比

| 维度 | 流量计费 | 时长计费 | 事件计费 |
|------|----------|----------|----------|
| **URR参数** | OFFMETERINGTYPE=VOLUME | OFFMETERINGTYPE=DURATION | OFFMETERINGTYPE=EVENT |
| **统计对象** | 上下行字节数 | 业务持续时间（秒） | 业务触发次数 |
| **配额单位** | 字节（CC-Total-Octets） | 秒（CC-Total-Time） | 次数（serviceSpecificUnits） |
| **离线话单字段** | datavolumeFBCUplink/Downlink | timeOfFirstUsage/timeOfLastUsage/duration | serviceSpecificUnits |
| **在线AVP** | CC-Total-Octets, CC-Input-Octets, CC-Output-Octets | CC-Total-Time | serviceSpecificUnits |
| **融合上报字段** | totalVolume/uplinkVolume/downlinkVolume | totalTime | serviceSpecificUnits |
| **在线计费模式** | SCUR | SCUR | **仅SCUR** |
| **依赖SA特性** | 依赖 | 依赖 | 依赖 |

> 来源：GWFD-020303 流量计费定义VOLUME参数和字段；GWFD-020302 时长计费定义DURATION参数；GWFD-020306 事件计费定义EVENT参数并明确"仅SCUR"。

### 4.2 时长计费的两种模式

GWFD-020302 定义了时长计费的两种具体实现方式：

| 模式 | 说明 | 配额下发 | 适用场景 |
|------|------|----------|----------|
| QCT（Quota Charging Time） | 按配额时长计费 | OCS/CHF下发Time Quota | 标准时长计费 |
| CTP（Charging Time Period） | 按计费时段计费 | 本地配置周期阈值 | 自定义周期场景 |

关键差异：
- 在线计费：QCT优先级为"OCS下发 > 本地配置"，当OCS下发Time Quota时使用QCT模式。
- 离线计费：仅使用本地配置的时间阈值。
- 融合计费：CHF下发配额时使用QCT模式。

> 来源：GWFD-020302 "时长计费的两种方式"章节。

### 4.3 事件计费的特殊性

GWFD-020306 定义了事件计费相比流量/时长计费的独特差异：

| 维度 | 说明 |
|------|------|
| 计费点 | 三个独立计费点：REQUEST（请求）、RESPONSE（响应）、FINISH（结束） |
| 在线模式 | 仅支持SCUR，不支持ECUR（20.9.0版本后支持ECUR事件计费） |
| HTTP限制 | HTTP协议中connect报文不触发事件计费（仅建立安全隧道） |
| 下载特殊 | HTTP断点续传/多线程下载/多源下载，每个请求算独立事件 |
| 业务类型 | HTTP业务（依赖SA-Web Browsing）、WAP业务（依赖SA-Mobile）、MMS业务（依赖SA-Mobile） |

> 来源：GWFD-020306 "事件计费与流量/时长计费的核心差异"和"事件计费支持的业务类型"章节。

### 4.4 OFFMETERINGTYPE 组合支持

GWFD-010171 定义了离线计费中OFFMETERINGTYPE的组合支持能力：

| OFFMETERINGTYPE | 含义 |
|-----------------|------|
| VOLUME | 仅流量 |
| TIME | 仅时长 |
| EVENT | 仅事件 |
| FREE | 免费（不计费） |
| EVENT_VOLUME_TIME | 事件+流量+时长（组合统计） |
| EVENT_VOLUME | 事件+流量 |
| EVENT_TIME | 事件+时长 |
| VOLUME_TIME | 流量+时长 |

> 来源：GWFD-010171 "URR"章节中OFFMETERINGTYPE参数说明。

---

## 五、特性依赖关系图

### 5.1 UDG/UPF 侧依赖链

```
GWFD-110101 SA-Basic（业务识别基础）
    │
    ├──→ GWFD-020351 PCC基本功能（策略控制基础）
    │       │
    │       └──→ GWFD-020300 在线计费（需PCC支撑配额控制）
    │
    └──→ GWFD-020301 内容计费基本功能（计费三件套基础）
            │
            ├──→ GWFD-020302 基于业务时长的计费
            │
            ├──→ GWFD-020303 基于业务流量的计费
            │
            └──→ GWFD-020306 支持事件计费

GWFD-010171 离线计费（独立，无前置依赖）
    │
    └──→ GWFD-010173 融合计费（需内容计费License）

GWFD-020300 在线计费
    │
    └──→ GWFD-010173 融合计费（共享超时阻塞机制）
```

依赖规则总结：
1. **SA-Basic 是所有内容计费特性的根基**：内容计费首先需要识别业务类型，而SA-Basic提供3/4/7层解析能力。来源：GWFD-020301、GWFD-020302、GWFD-020303 均声明依赖 GWFD-110101。
2. **内容计费是时长/流量/事件计费的前置**：三种计量方式是内容计费的增强形式。来源：GWFD-020302 明确"时长计费是内容计费的增强形式，使用前必须先开启内容计费功能"。
3. **离线计费独立于内容计费**：离线计费无需内容计费License或SA-Basic。来源：GWFD-010171 "无需License许可"。
4. **融合计费依赖内容计费License**：融合计费本身无License，但需要内容计费License。来源：GWFD-010173 "需确认内容计费基本功能对应的License开关（LKV3G5BC01）已打开"。

### 5.2 UNC/SMF 侧依赖链

```
WSFD-109101 PCC基本功能（UNC侧策略控制基础）
    │
    └──→ WSFD-109002 内容计费基本功能（需PCC支撑规则下发）

WSFD-011201 支持离线计费（独立基础特性）
    │
    ├──→ WSFD-011202 支持热计费（离线计费增强，CC=0x0100）
    │
    └──→ WSFD-011206 支持融合计费（可选依赖内容计费/流量计费/时长计费License）

WSFD-109002 内容计费基本功能
    │
    └──→ WSFD-011206 支持融合计费（基于业务粒度融合计费时需开启）
```

> 来源：WSFD-011202 明确"依赖 WSFD-011201 支持离线计费"；WSFD-011206 列出依赖特性表包含WSFD-109002、WSFD-109003、WSFD-109004；WSFD-109101 前置条件要求"UDG侧已完成GWFD-020351 PCC基本功能配置"。

### 5.3 跨产品线依赖（CU协同）

```
[PCF/PCRF]
    │
    ├── N7/N15（5G）──→ WSFD-109101 PCC（UNC侧）
    │                    │
    │                    └── N4 ──→ GWFD-020351 PCC（UDG侧）
    │
    └── Gx（2/3/4G）──→ WSFD-109101 PCC（UNC侧）
                          │
                          └── N4 ──→ GWFD-020351 PCC（UDG侧）

[SMF/PGW-C ← N4 → UPF/PGW-U] 的协同要求：
    - 11+个参数必须保持一致
    - CP/UP一致性检查：30分钟扫描周期，不一致触发ALM-81054告警
```

> 来源：GWFD-020301 "SMF/UPF一致性要求"章节列出11+参数；GWFD-110101 定义ALM-81054告警用于CP/UP配置不一致检测。

---

## 六、配置对象全景

### 6.1 UDG/UPF 侧配置对象层级

```
UserProfile（用户档案）
    │
    ├── RULE（计费规则）
    │       │
    │       ├── FLOWFILTER（流过滤器）
    │       │       │
    │       │       ├── FILTER（5元组过滤）
    │       │       └── L7FILTER（7层过滤/URL过滤）
    │       │
    │       └── PCCPOLICYGRP（PCC策略组）
    │               │
    │               ├── URR（使用量上报规则）
    │               │       ├── OFFMETERINGTYPE / ONLMETERINGTYPE（计量方式）
    │               │       ├── USAGERPTMODE（OFFLINE/ONLINE）
    │               │       ├── RG（费率组）/ SID（业务标识）
    │               │       ├── VOLUMETHRESHOLD / TIMETHRESHOLD / EVENTTHRESHOLD
    │               │       └── RGAPPLIED（融合计费模式）
    │               │
    │               └── URRGROUP（URR组）
    │                       ├── UPURRNAME1/2/3（URR成员）
    │                       └── DFTURRGRPNAME（默认URR组）
    │
    └── SPECURRGRPLIST（特殊URR组列表，防欺诈）
```

> 来源：GWFD-020301 定义"计费三件套"（URR→URRGROUP→PCCPOLICYGRP）；GWFD-020351 定义UPF配置对象层级（UserProfile→RULE→FLOWFILTER→FILTER/PCCPOLICYGRP）；GWFD-020300 定义USAGERPTMODE；GWFD-010173 定义RGAPPLIED。

### 6.2 UNC/SMF 侧配置对象层级

```
APN
    │
    ├── APNCHARGECTRL（APN计费控制）
    │       ├── ONLINESW / OFFLINESW（在线/离线开关）
    │       ├── PGWOFCTEMPLATE / SGWOFCTEMPLATE / GGSNOFCTEMPLATE（离线计费模板）
    │       └── CCNAME（计费属性名）
    │
    └── APNUSRPROFG（APN绑定UserProfile模板组）

USRPROFGROUP（UserProfile模板组）

UPBINDUPG（UserProfile绑定到UPG）

CHARGECHAR（计费属性）
    ├── HOME / ROAM / VISIT（本地/漫游/拜访用户CC值）
    └── HOMESGSN / ROAMSGSN / VISITSGSN（是否使用Serving Node CC）

CHARGECTRL（计费控制）
    ├── HOMEOFFLINE / VISITOFFLINE（离线计费开关）
    └── HOMEONLINE / VISITONLINE（在线计费开关）

OFCTemplate（离线计费模板）
    ├── GCDRVERSION（CDR版本）
    ├── VOLUMETHRESHOLD / TIMETHRESHOLD（阈值）
    └── CONDITIONCHANGE / SERVINGNODECHNG（触发条件）

CCT（Converged Charging Template，融合计费模板）
    ├── QHT（Quota Holding Time）
    ├── VQT（Volume Quota Time）
    ├── TQT（Time Quota Time）
    ├── VT（Volume Threshold）
    └── 其他触发器和阈值参数

PCCPOLICYGRP（PCC策略组，UNC侧）
    └── URR / URRGROUP（与UDG侧对应）

CHF配置
    ├── CHF选择优先级（7级）
    ├── N40 API版本控制
    └── ADD QUOTAEXHAUSTACT（配额耗尽动作）

CG配置
    ├── 最多32个CG
    ├── 负载均衡
    └── WAL保护
```

> 来源：WSFD-011201 定义CHARGECHAR、CHARGECTRL、OFCTemplate、CG配置；WSFD-011206 定义CCT模板、CHF配置、QUOTAEXHAUSTACT；WSFD-109002 定义USRPROFGROUP、UPBINDUPG、APNUSRPROFG；WSFD-011202 定义ADD CHARGECHAR的HOME/ROAM/VISIT参数。

### 6.3 跨面一致性要求的配置对象

GWFD-020301 定义了SMF与UPF之间必须保持一致的11+个参数：

| 参数 | SMF（UNC） | UPF（UDG） | 一致性要求 |
|------|-----------|-----------|-----------|
| URR名称 | N4会话管理 | ADD URR | 必须一致 |
| URRGROUP名称 | N4会话管理 | ADD URRGROUP | 必须一致 |
| PCCPOLICYGRP名称 | N4会话管理 | ADD PCCPOLICYGRP | 必须一致 |
| RG（Rating Group） | PCC规则 | URR.RG | 必须一致 |
| SID（Service Identifier） | PCC规则 | URR.SID | 必须一致 |
| OFFMETERINGTYPE | PCC规则 | URR.OFFMETERINGTYPE | 必须一致 |
| ONLMETERINGTYPE | PCC规则 | URR.ONLMETERINGTYPE | 必须一致 |
| USAGERPTMODE | PCC规则 | URR.USAGERPTMODE | 必须一致 |
| VOLUMETHRESHOLD | PCC规则 | URR.VOLUMETHRESHOLD | 必须一致 |
| TIMETHRESHOLD | PCC规则 | URR.TIMETHRESHOLD | 必须一致 |
| METERINGMETHOD | PCC规则 | URR.METERINGMETHOD | 必须一致 |

> 来源：GWFD-020301 "SMF/UPF一致性要求"章节。

### 6.4 SET REFRESHSRV 规则

GWFD-020351 和 GWFD-020301 均强调：**在UDG侧修改FILTER、L7FILTER、FLOWFILTER等配置后，必须执行 SET REFRESHSRV 命令**，使配置生效。PROTBINDFLOWF 参数要求在修改后等待60秒再执行。

> 来源：GWFD-020351 "SET REFRESHSRV"相关说明；GWFD-020301 配置步骤中多次出现REFRESHSRV。

---

## 七、共性知识提取

### 7.1 计费三件套（URR → URRGROUP → PCCPOLICYGRP）

这是所有内容计费（含流量、时长、事件计费）的核心配置模式，跨UDG和UNC两侧通用：

```
第一步：ADD URR（定义使用量上报规则）
    - 指定计量方式：OFFMETERINGTYPE/ONLMETERINGTYPE
    - 指定费率：RG/SID
    - 指定阈值：VOLUMETHRESHOLD/TIMETHRESHOLD/EVENTTHRESHOLD
    - 指定上报模式：USAGERPTMODE（OFFLINE/ONLINE）

第二步：ADD URRGROUP（将URR组织为组）
    - UPURRNAME1/2/3 指定组成员（仅编号，无优先级语义）
    - DFTURRGRPNAME 指定默认URR组（隐式兜底）
    - 融合计费中 RGAPPLIED 控制组内在线/离线RG配置

第三步：ADD PCCPOLICYGRP（将URRGROUP绑定到策略组）
    - 绑定到RULE，实现业务匹配 → 计费执行的完整链路
```

> 来源：GWFD-020301 定义三件套为内容计费核心配置模式；GWFD-020302/020303/020306 均复用该模式，仅改变METERINGTYPE参数。

### 7.2 License 依赖树

```
LKV3G5SABS01（SA-Basic）── 基础依赖
    │
    ├── LKV3G5BCBC01（内容计费）── 依赖SA-Basic
    │       │
    │       ├── LKV3G5TBCS01（时长计费）── 依赖内容计费
    │       ├── LKV3G5VBCS01（流量计费）── 依赖内容计费
    │       └── LKV3G5EBCS01（事件计费）── 依赖内容计费
    │
    └── LKV3G5PCCB01（PCC基本功能）── 依赖SA-Basic（前置条件"完成业务感知配置"）

LKV3G5OLCH01（在线计费）── 独立
LKV2HBILL02（热计费，仅SGSN）── 依赖离线计费

UNC侧：
LKV3W9SPCC11（PCC基本功能）── 独立
LKV3W9BCC12（内容计费）── 独立
```

> 来源：各特性License章节。GWFD-020302 明确"使用前必须先开启内容计费功能"且"必须先开启SA特性"；GWFD-020303 明确"依赖链：SA-Basic → 内容计费基本功能 → 基于业务流量的计费"。

### 7.3 在线/融合计费共享的超时阻塞机制

在线计费和融合计费共享相同的超时阻塞公式：

```
超时时间 = T3RESPONSE × N3REQUEST + 4（秒）
```

当OCS/CHF未在超时时间内响应配额请求时，PGW-U/UPF将阻塞用户业务。

> 来源：GWFD-020300 定义超时阻塞公式；GWFD-010173 明确融合计费使用相同的超时阻塞机制。

### 7.4 遵循标准的分层结构

| 层级 | 标准编号 | 适用范围 |
|------|----------|----------|
| 系统架构 | 3GPP 23.501 | 5G系统架构（Stage 2） |
| 流程定义 | 3GPP 23.502 | 5G系统流程（Stage 2） |
| PCC框架 | 3GPP 23.503 | 5G策略和计费控制框架 |
| CP/UP接口 | 3GPP 29.244 | 控制面与用户面接口（Stage 3） |
| 计费架构 | 3GPP 32.240 | 计费架构和原则 |
| 5G计费 | 3GPP 32.255 | 5G数据连接域计费（Stage 2） |
| Diameter计费 | 3GPP 32.299 | Diameter计费应用 |
| PS域计费 | 3GPP 32.015 | PS域呼叫和事件数据 |

> 来源：各特性"遵循标准"章节。GWFD-020301/020302/020303 引用23.502和29.244；GWFD-010173 融合计费引用23.501/23.502/23.503；WSFD-011201 离线计费引用32.240/32.299；WSFD-011202 热计费引用32.015。

### 7.5 Default Quota 机制

在线计费中，当OCS不可达或配额下发失败时，UPF可使用默认配额继续允许用户业务：

- 配置命令：SET UPDEFAULTQUOTA
- 适用场景：OCS故障时的容灾
- 仅在线计费使用，离线计费无此机制

> 来源：GWFD-020300 "Default Quota"章节。

### 7.6 CP/UP 配置一致性检查

- 检查机制：SMF每30分钟扫描一次UPF配置
- 告警：配置不一致时触发 ALM-81054
- 影响范围：所有需要C面/U面协同的计费特性

> 来源：GWFD-110101 定义ALM-81054告警；GWFD-020301 描述一致性检查机制。

### 7.7 跨面配置的完整流程

典型内容计费配置涉及C面和U面的协同步骤：

```
UDG侧（用户面）：
1. ADD URR          ── 定义使用量上报规则
2. ADD URRGROUP     ── 组织URR为组
3. ADD PCCPOLICYGRP ── 绑定URRGROUP到策略组
4. ADD FILTER/L7FILTER/FLOWFILTER ── 定义流量过滤规则
5. ADD RULE         ── 绑定过滤器和策略组
6. SET REFRESHSRV   ── 刷新配置生效（必须）

UNC侧（控制面）：
1. ADD USRPROFGROUP ── 定义UserProfile模板组
2. ADD UPBINDUPG   ── 绑定UserProfile到UPG
3. ADD APN         ── 定义APN
4. ADD APNUSRPROFG ── 绑定APN到UserProfile模板组
5. SET CHARGECTRL  ── 设置计费控制
6. ADD OFCTemplate/CCT ── 设置计费模板
```

> 来源：GWFD-020301 "配置规则"章节定义14步配置流程；WSFD-109002 定义UNC侧配置步骤。

### 7.8 融合计费的CCT模板触发器

WSFD-011206 定义的CCT（Converged Charging Template）是UNC侧融合计费特有的配置对象，包含以下关键触发器：

| 触发器 | 全称 | 说明 |
|--------|------|------|
| QHT | Quota Holding Time | 配额持有时间 |
| VQT | Volume Quota Time | 流量配额时间 |
| TQT | Time Quota Time | 时长配额时间 |
| VT | Volume Threshold | 流量阈值 |
| TIMTH | Time Threshold | 时长阈值 |
| PERIO | Periodic | 周期性触发 |
| QUHTI | Quota Holding Time Indication | 配额持有时间指示 |
| START | Session Start | 会话开始 |
| STOPT | Session Stop | 会话结束 |

> 来源：WSFD-011206 "CCT模板"章节。

### 7.9 Credit Pooling 机制

GWFD-020300 提到在线计费在20.15.2版本引入了Credit Pooling功能，允许多个RG共享同一配额池。该机制可以减少配额请求次数，提升OCS性能。

> 来源：GWFD-020300 版本历史中提到的Credit Pooling功能。

---

## 附录：特性索引

| 特性ID | 特性名称 | 产品线 | License | 首次版本 |
|--------|----------|--------|---------|----------|
| GWFD-110101 | SA-Basic | UDG | LKV3G5SABS01 | 20.0.0 |
| GWFD-020351 | PCC基本功能 | UDG | LKV3G5PCCB01 | 20.0.0 |
| GWFD-020301 | 内容计费基本功能 | UDG | LKV3G5BCBC01 | 20.0.0 |
| GWFD-020302 | 基于业务时长的计费 | UDG | LKV3G5TBCS01 | 20.0.0 |
| GWFD-020303 | 基于业务流量的计费 | UDG | LKV3G5VBCS01 | 20.0.0 |
| GWFD-020306 | 支持事件计费 | UDG | LKV3G5EBCS01 | 20.5.0 |
| GWFD-010171 | 离线计费 | UDG | 无需License | 20.0.0 |
| GWFD-020300 | 在线计费 | UDG | LKV3G5OLCH01 | 20.0.0 |
| GWFD-010173 | 融合计费 | UDG | 无需License | 20.0.0 |
| WSFD-109101 | PCC基本功能 | UNC | LKV3W9SPCC11 | 20.0.0 |
| WSFD-109002 | 内容计费基本功能 | UNC | LKV3W9BCC12 | 20.0.0 |
| WSFD-011201 | 支持离线计费 | UNC | 无需License | 20.3.0 |
| WSFD-011202 | 支持热计费 | UNC | SGSN需LKV2HBILL02 | 20.3.0 |
| WSFD-011206 | 支持融合计费 | UNC | 无需额外License | 20.0.0 |
