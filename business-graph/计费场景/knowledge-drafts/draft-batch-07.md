# Batch 07: 5G Core知识问答 — PDR/PDI/FAR/QER/URR映射 + URR与RG关系 + CC决策 + ULCL计费 + 流量监管

## 来源文件清单

| # | 文件名（简） | 文件名（完整后缀） | 重点 |
|---|-------------|-------------------|------|
| 1 | PDR、PDI、FAR_QER_URR与本地规则的映射关系 | _55239517 | 核心映射关系、App ID关联本地分流规则 |
| 2 | PDR是什么？都有哪些类型？ | _05259983 | PDR信息构成、动态PDR与预定义PDR |
| 3 | PDR是怎么进行匹配的？ | _05259984 | PDR匹配方式、动态rule vs ADC rule vs 预定义PDR |
| 4 | URR与RG的关系 | _45662434 | SMF维护RG-URR映射、非计费URR无RG |
| 5 | 流量监管、流量拥塞是什么？ | _02921978 | CAR双令牌桶、CIR/PIR/CBS/PBS、拥塞管理与避免 |
| 6 | 本地配置CC和签约CC决策 | _03213871 | CC四级优先级、HOMESGSN/ROAMSGSN/VISITSGSN控制 |
| 7 | 本地分流业务怎么计费？ | _05147613 | UL CL不计费、主辅锚点独立计费 |

> 注：UNC文档根路径下未找到独立的计费相关术语文件（仅存在IPSec、过载控制、设备标识的相关术语文件），故本批次不含术语来源。

---

## 一、PDR信息构成与类型

### K250: PDR核心定义与信息构成
> 来源: PDR是什么？都有哪些类型？_05259983

**原理知识**

PDR（Packet Detection Rule，流检测规则）是SMF在PFCP会话建立过程中下发给UPF的，用于指示UPF识别流及流处理动作的属性集合。

PDR的信息构成包含以下关键参数：

| 参数 | 说明 |
|------|------|
| PDI（Packet Detection Information） | 流匹配信息，包含报文方向（source interface: 0=上行, 1=下行）和filter（SDF Filter / Application ID）。入口数据流量的对应字段与PDI中所有匹配条件全部匹配则命中 |
| FAR ID | 指示转发动作FAR ID（转发动作包含转发、缓存、重传、丢弃等） |
| QER ID | 指示流控类动作的QER ID（流控类动作如CAR） |
| URR ID | 指示统计上报类动作的URR ID（统计上报类动作包含配额、阈值、时长、流量、上报原因等） |
| Precedence | PDR优先级 |
| Activate Predefined Rules | 预定义规则名称 |

### K251: PDR两大类型 — 动态PDR与预定义PDR
> 来源: PDR是什么？都有哪些类型？_05259983

**原理知识**

PDR分为动态PDR和预定义PDR两种类型：

| 类型 | 组成 | 特点 |
|------|------|------|
| 动态PDR | PDI + FAR + QER + URR + Precedence | 所有匹配条件和动作由SMF动态下发 |
| 预定义PDR | PDI + FAR + QER + URR + Precedence + Activate Predefined Rules | 携带预定义规则名，UPF匹配本地配置 |

预定义PDR的关键特性：
- 一条预定义PDR可携带多个Activate Predefined Rules
- Activate Predefined Rules可以是UPF/PGW-U本地配置的userprofile名称，或者是本地配置的rule名称

### K252: PDI/FAR/QER/URR各自定义
> 来源: PDR、PDI、FAR_QER_URR与本地规则的映射关系_55239517

**原理知识**

| 组件 | 全称 | 定义 |
|------|------|------|
| PDI | Packet Detection Information（流匹配信息） | PDR的组成部分，包含识别流的各种属性（Source interface、Local F-TEID、App ID等） |
| FAR | Forwarding Action Rule（转发动作规则） | PDR的组成部分，指示对流做转发、缓存、重传、丢弃等处理 |
| QER | QoS Enforcement Rule（流控动作规则） | PDR的组成部分，指示对流做带宽控制（Gate、GBR、MBR、报文速率控制等） |
| URR | Usage Reporting Rule（计费动作规则） | PDR的组成部分，指示对流的计费信息（配额、阈值、时长、流量、上报原因等） |

这四个组件通过PDR聚合：PDI负责匹配，FAR/QER/URR分别负责转发/流控/计费动作。

---

## 二、PDR匹配机制

### K253: PDR在数据流转发过程中的匹配位置
> 来源: PDR是怎么进行匹配的？_05259984

**流程知识**

PDR匹配发生在数据流转发过程中，流程如下：

1. **PDR下发**: SMF向UPF下发一组PDR（通过PFCP Session Establishment Request消息），至少包含：
   - 一个access类型PDR（用于上行数据流规则匹配）
   - 一个core类型PDR（用于下行数据流规则匹配）
2. **报文到达**: 用户数据报文发送至UPF
3. **会话匹配**: UPF对用户报文进行PDR匹配，查找用户所属PDU Session
4. **PDR命中**: UPF根据PDR优先级、报文关键信息（域名、IP等）进行PDR匹配，命中PDR
5. **动作执行**: UPF根据PDR中的相关信息或本地配置的相关规则信息，执行数据流的相关动作并转发

### K254: PDR匹配优先级规则
> 来源: PDR是怎么进行匹配的？_05259984

**原理知识**

PDR匹配的核心规则：

- PDR按优先级（Precedence）匹配，多个PDR时取优先级最高的PDR
- 当动态PDR与预定义PDR优先级相同时，**动态PDR优先级高于预定义PDR**

### K255: 动态PDR的两种匹配方式 — 动态rule vs ADC rule
> 来源: PDR是怎么进行匹配的？_05259984

**原理知识**

动态PDR有两种匹配方式：

| 方式 | SDF filter | Application ID | 匹配逻辑 | 动作执行 |
|------|-----------|----------------|----------|----------|
| 动态rule | 携带转发匹配条件 | 不携带 | 按SDF filter匹配报文 | 按PDR中对应动作执行流转发 |
| ADC rule | "Permit out ip from any to assigned" | 携带 | 根据Application ID匹配本地配置的Flowfilter/Flowfilter Group | 按本地的Flowfilter/Flowfilter Group配置执行流动作 |

关键区别：动态rule直接用SDF filter匹配报文字段；ADC rule通过Application ID间接匹配本地配置的Flowfilter/Flowfilter Group。

### K256: 预定义PDR匹配方式
> 来源: PDR是怎么进行匹配的？_05259984

**原理知识**

预定义PDR匹配机制：

- UPF根据Activate Predefined Rules值匹配本地配置的**userprofile**或本地配置的**rule**
- 命中该PDR后，UPF按照userprofile或rule进行带宽、计费等策略控制

### K257: PDR与本地规则的映射关系（分流场景）
> 来源: PDR、PDI、FAR_QER_URR与本地规则的映射关系_55239517

**原理知识**

在分流特性中，PDR通过Application ID与本地配置的分流规则建立映射关系：

- **映射方式**: PDR中的Application-ID值对应本地分流规则的flowfilter或flowfiltergroup名称
- **执行顺序**: 数据报文先匹配flowfilter/flowfiltergroup，根据Application-ID检索到分流PDR，然后按照PDR中的FAR（转发规则）、QER（QoS规则）执行策略动作
- 即：**报文 → flowfilter/flowfiltergroup匹配 → App ID → 检索PDR → 执行FAR/QER/URR动作**

---

## 三、URR与RG的关系

### K258: SMF维护RG与URR ID的映射关系
> 来源: URR与RG的关系_45662434

**原理知识**

Nchf接口、N4接口与RG/URR的关系：

| 接口 | 方向 | RG/URR角色 |
|------|------|-----------|
| Nchf（SMF↔CHF） | SMF→CHF申请配额 | 按RG粒度申请配额，按RG或RG+SID粒度上报配额 |
| Nchf（CHF→SMF） | CHF→SMF下发配额 | 按RG粒度下发配额 |
| N4（SMF→UPF） | SMF→UPF下发URR | URR包含计费事件和计费参数，UPF按URR向SMF上报配额用量 |

关键映射规则：
- **所有RG都有对应的URR ID**
- 但URR并不都用于计费，**非计费的URR ID没有对应的RG**
- SMF负责维护RG与URR ID之间的映射关系

---

## 四、CC（计费属性）决策逻辑

### K259: CC四级优先级机制
> 来源: 在本地配置计费属性CC和签约CC下发的场景下，UNC是如何决策的？_03213871

**配置知识**

UNC支持基于UserProfile、APN/DNN、全局配置用户的计费属性CC（Charging Characteristics）。CC的优先级从高到低：

| 优先级 | 来源 | 说明 |
|--------|------|------|
| 1（最高） | UserProfile下的配置 | 用户级配置 |
| 2 | APN/DNN下的配置 | 接入点级配置 |
| 3 | 全局配置 | 全局默认 |
| 4（最低） | normal（普通计费） | 兜底默认 |

如果高级别参数没有配置，则依次向下使用低一级别的参数取值。

### K260: 本地CC与签约CC的选择控制
> 来源: 在本地配置计费属性CC和签约CC下发的场景下，UNC是如何决策的？_03213871

**配置知识**

本地CC与签约CC的选择受两类命令控制，核心参数为HOMESGSN、ROAMSGSN、VISITSGSN（分别控制本地、漫游、拜访用户）：

| 场景 | 控制命令 | ENABLE含义 | DISABLE含义 |
|------|----------|-----------|------------|
| 基于UserProfile/APN/DNN配置CC | ADD CHARGECHAR | 使用签约下发的CC | 使用本地配置的CC |
| 基于全局配置CC | SET GLBCHARGECHAR | 使用签约下发的CC | 使用本地基于全局配置的CC |

决策逻辑：先按K259的四级优先级确定本地CC，再根据HOMESGSN/ROAMSGSN/VISITSGSN的ENABLE/DISABLE决定是否用签约CC覆盖本地CC。

### K261: 各网络制式下签约CC的来源网元
> 来源: 在本地配置计费属性CC和签约CC下发的场景下，UNC是如何决策的？_03213871

**原理知识**

| 网络制式 | UNC角色 | 签约CC来源 |
|----------|---------|-----------|
| 5G | SMF | UDM下发 |
| 4G（SP合设） | SGW-C + PGW-C | 左侧MME携带（MME从HSS获取） |
| 4G（SP分离，UNC=SGW-C） | SGW-C | 左侧MME携带（MME从HSS获取） |
| 4G（SP分离，UNC=PGW-C） | PGW-C | 左侧SGW-C携带（SGW-C通过MME得到） |
| 2/3G | GGSN | 左侧SGSN携带（SGSN从HLR获取） |

规律：4G网络中签约CC统一由左侧MME/SGW-C携带；5G由UDM下发；2/3G由SGSN携带。

---

## 五、本地分流（ULCL）计费规则

### K262: ULCL分流场景的计费架构
> 来源: 本地分流业务怎么计费？_05147613

**原理知识**

本地分流业务中的计费架构：

- **UL CL UPF不计费**: UL CL UPF仅负责将流量分发给主锚点UPF和辅锚点UPF，自身不做计费
- **主锚点和辅锚点独立计费**: 业务流量分别在主锚点UPF和辅锚点UPF上独立计费
- **计费策略下发时机**: 在N4会话建立或更新时，由SMF通过普通PDR中携带的URR定义
- **计费规则来源**: 计费规则及计费动作可以在UPF本地配置，也可以由SMF动态下发

核心原则：UL CL只分流、不计费；计费在锚点UPF按各自的URR独立执行。

---

## 六、流量监管与流量拥塞

### K263: CAR流量监管 — 双令牌桶机制
> 来源: 流量监管、流量拥塞是什么？_02921978

**原理知识**

流量监管功能通过CAR（Committed Access Rate，承诺访问速率）限制报文流量。CAR使用双令牌桶模型：

**报文处理流程**:
1. 报文首先进入令牌桶P（峰值桶），速率PIR，溢出报文标记为**red**
2. 通过令牌桶P的报文进入令牌桶C（承诺桶），速率CIR，溢出报文标记为**yellow**
3. 通过令牌桶C的报文标记为**green**

**UDG染色处理**:
- red：直接丢弃
- yellow：拥塞时首先丢弃，不拥塞时高优先级可通过
- green：丢弃优先级最低

### K264: CAR双令牌桶四个参数
> 来源: 流量监管、流量拥塞是什么？_02921978

**原理知识**

| 参数 | 全称 | 含义 |
|------|------|------|
| CIR | Committed Information Rate（承诺信息速率） | 向令牌桶C投放令牌的速率，即允许转发报文的平均速率 |
| CBS | Committed Burst Size（承诺突发尺寸） | 令牌桶C的容量，即允许通过的最大报文长度 |
| PIR | Peak Information Rate（峰值信息速率） | 向令牌桶P投放令牌的速率，即峰值允许转发报文的平均速率 |
| PBS | Peak Burst Size（峰值突发尺寸） | 令牌桶P的容量，即峰值允许通过的最大报文长度 |

关系：CIR < PIR，CBS和PBS分别对应两个令牌桶的容量。

### K265: 拥塞管理与拥塞避免
> 来源: 流量监管、流量拥塞是什么？_02921978

**原理知识**

| 机制 | 说明 |
|------|------|
| 拥塞管理 | 当报文到达速度超过接口发送速度时，将报文分类送入不同队列，队列调度对不同优先级报文分别处理，优先级高的报文优先处理 |
| 拥塞避免（Congestion Avoidance） | 监视网络资源（队列/内存缓冲区）使用情况，在拥塞加剧趋势时主动丢弃报文，通过调整流量解除网络过载 |

拥塞管理是被动应对（排队+调度），拥塞避免是主动预防（提前丢弃）。

---

## 统计表

| 段 | 知识条目 | 数量 | 来源篇数 |
|----|----------|------|----------|
| 一、PDR信息构成与类型 | K250-K252 | 3 | 2 |
| 二、PDR匹配机制 | K253-K257 | 5 | 3 |
| 三、URR与RG的关系 | K258 | 1 | 1 |
| 四、CC决策逻辑 | K259-K261 | 3 | 1 |
| 五、本地分流（ULCL）计费 | K262 | 1 | 1 |
| 六、流量监管与拥塞 | K263-K265 | 3 | 1 |
| **合计** | K250-K265 | **16** | **7**（去重后7篇） |

---

## 核心概念关系图

```
SMF通过PFCP下发
  └─ PDR（流检测规则）
       ├─ PDI（流匹配信息）
       │    ├─ Source Interface（上行/下行）
       │    └─ Filter（SDF Filter / Application ID）
       │         └─ Application ID → 映射本地Flowfilter/FlowfilterGroup
       ├─ FAR（转发动作）
       ├─ QER（流控动作 / CAR）
       │    └─ CIR/CBS/PIR/PBS 双令牌桶
       ├─ URR（计费动作）
       │    ├─ SMF维护 URR ID ↔ RG 映射
       │    └─ 非计费URR无RG
       └─ Precedence（优先级）

CC决策链：
  UserProfile > APN/DNN > 全局 > normal
  └─ ADD CHARGECHAR / SET GLBCHARGECHAR 的 HOMESGSN/ROAMSGSN/VISITSGSN
       决定是否用签约CC覆盖本地CC

ULCL计费：
  UL CL UPF（不计费，仅分流）→ 主锚点UPF（独立计费）+ 辅锚点UPF（独立计费）
```
