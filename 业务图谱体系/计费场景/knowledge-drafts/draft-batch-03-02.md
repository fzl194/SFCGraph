# Batch 03-02: N40接口融合计费原理 知识草稿

## 来源文件（27篇）

路径前缀: 网络部署/业务专题/5G Core 计费解决方案/计费解决方案概述/计费原理/N40接口融合计费/

### 融合计费概述 (1篇)
- 融合计费概述_42995681.md

### 融合计费可靠性 (3篇)
- 融合计费可靠性_50085257.md
- 融合计费可靠性/融合计费可靠性（未部署NCG）_01_10008.md
- 融合计费可靠性/融合计费可靠性（部署NCG）_31702099.md

### 标准计费流程-未部署NCG (11篇)
- 融合计费原理/标准计费流程（未部署NCG场景）_56728529.md
- 计费会话创建流程_76308085.md
- 计费会话更新流程_76428001.md
- 计费会话释放流程_16976658.md
- 计费会话通知流程_57206245.md
- 相关参考/PCC规则及计费策略_90776686.md
- 相关参考/多UPF配额管理_90776687.md
- 相关参考/计费事件触发条件_01_10007.md
- 相关参考/计费用量搜集_62477215.md
- MEC计费流程_01_10005.md
- 互操作计费流程_01_10006.md

### 标准计费流程-部署NCG (3篇)
- 融合计费原理/标准计费流程（部署NCG场景）/计费流程_43650335.md
- 话单及处理流程/CHF-CDR话单_43364675.md
- 话单及处理流程/话单处理流程_52552752.md

### 相关术语 (9篇)
- 相关术语/CC_92032690.md, Charging ID_91327364.md, QCT_91532421.md, QHT_91532399.md, RG_91327370.md, SID_91532397.md, URR_84060175.md, 话单_91327368.md, 容器_91327366.md

---

## 一、融合计费架构

### K42: 融合计费涉及的网元及功能
> 来源: 融合计费概述_42995681

**原理知识**

| 网元 | 融合计费中的角色 |
|------|----------------|
| SMF | Nchf服务使用者；选择CHF；处理计费参数；通过N4向UPF下发配额；通过N7与PCF交互；监控在线配额 |
| CHF | Nchf服务提供者；在线：批价/扣费/配额下发；离线：参数下发；处理用量上报生成CHF-CDR；提供重授权触发条件 |
| PCF | 通过N7接口进行计费策略控制；可下发CHF地址 |
| UPF | 接收PDR/URR规则或预定义规则；根据规则上报计费信息 |
| UDM | 通过CC计费特性传递签约数据到SMF |
| NRF | NF注册/发现；SMF通过NRF发现CHF |

### K43: 华为三种融合计费方案
> 来源: 融合计费概述_42995681

**方案设计知识**

| 方案 | 描述 | 可靠性特点 |
|------|------|-----------|
| 方案一 | CCS部署在计费域，无NCG | 网络侧无话单，可靠性低 |
| 方案二 | NCG(网络侧) + CCS(计费域) | NCG转发到CCS；NCG保存全量话单；CHF异常时NCG代应答 |
| 方案三 | NCG(网络侧) + OCS(计费域) | 离线由NCG完成，在线由OCS完成；OCS改造量减少40% |

---

## 二、融合计费关键术语

### K44: CC (Charging Characteristics / 计费属性)
> 来源: CC_92032690

**原理知识**

CC是16位字符串，映射到行为索引表，定义：
- 默认计费方法（在线/离线/融合）
- CHF地址
- 每PDU会话的TimeLimit/VolLimit
- 变更条件限制
- 资费时间

**CC优先级（从高到低）：**
1. UserProfile（PCF下发）
2. DNN配置
3. 全局配置
4. 默认值

**CC来源：** 首先来自DNN订阅数据(UDM)。DNN无CC则回退到SMF本地配置。

**三种用户类型：** 本地用户(归属PLMN)、漫游用户、拜访用户

### K45: RG (Rating Group / 计费费率组)
> 来源: RG_91327370

**原理知识**

- 共享相同计费类型/费率的一组服务
- SMF以RG粒度向CHF请求配额
- CHF以RG粒度授予配额和计费参数
- SMF维护RG→URR ID映射
- **所有RG都有URR ID，但并非所有URR ID都有RG**（非计费用途的URR无RG）

PCF可在PDU会话生命周期内更改：RG、SID、Sponsor ID、Application Service Provider ID、Policy and Reporting priority

### K46: SID (Service Identifier / 业务识别标识)
> 来源: SID_91532397

**原理知识**

- 代表一个业务数据流，是RG的子集
- 必须与绑定的RG一起使用
- 一个RG可包含多个SID
- 计费模型（流量/时长/事件）由RG+SID共同决定

### K47: URR (Usage Reporting Rule / 使用量上报规则)
> 来源: URR_84060175

**原理知识**

SMF通过N4(PFCP)向UPF下发的规则，指示UPF测量和报告网络资源使用情况。
- 测量维度：流量(Volume)、时长(Duration)、事件(Event)
- 上报触发：阈值到达、周期性、应请求上报

**URR关键参数：**
- URR ID, Measurement Method, Reporting Triggers
- Volume Quota, Time Quota, Volume Threshold, Time Threshold
- Linked URR ID（关联上报）, Measurement Information（ISTM等）

### K48: QCT (Quota Consumption Time / 配额空耗时间)
> 来源: QCT_91532421

**原理知识**

设置阈值（秒），确定数据包间空闲期是否算应计费时间。

**时长计费四种模式：**
1. **连续时长计费(CTP)**: QCT=0，从首包到尾包所有时间都计费
2. **QCT时长计费**: QCT>0，空闲≤QCT=应计费；空闲>QCT=仅QCT持续时间应计费
3. **CTP (Continuous-Time-Period)**
4. **DTP (Discrete-Time-Period)**

**QCT机制：** 空闲时启动QCT计时器。QCT到期前有数据包到达→重置；QCT到期→超出部分不计费。

在线计费连续模式：从SMF创建配额开始，无论有无流量，直到用户去活。
离线计费连续模式：从UPF接收第一个业务数据包开始。

### K49: QHT (Quota Holding Time / 配额空闲时间)
> 来源: QHT_91532399

**原理知识**

用户无数据包时UPF启动计时器（秒）。QHT到期→SMF向CHF报告计费信息。
- **在线计费**：QHT到期=SMF不请求配额，配额仅在下一次业务活动时请求
- **离线计费**：QHT到期=触发关闭当前业务容器
- QHT=0：禁用
- 适用于流量和时长计费

### K50: Container (容器 / Used Unit Container)
> 来源: 容器_91327366

**原理知识**

CDR中的容器，记录计费条件更改信息。一个CDR可包含多个容器。

**两种报告类别：**
- **即时上报**：立即关闭计数器，SMF立即发送Charging Data Request，打开新计数器
- **延迟上报**：关闭计数器存储数据，在下一条Charging Data Request中发送，打开新计数器

**PDU容器信息字段：** Time of First/Last Usage, QoS Information, User Location, UE Time Zone, RAT Type, Serving NF ID, Charging Rule Base Name, 3GPP PS Data Off Status 等

---

## 三、计费会话生命周期

### K51: CHF选择优先级（6级）
> 来源: 计费会话创建流程_76308085

**配置知识**

| 优先级 | 方式 | 配置命令 |
|--------|------|---------|
| 1 | 基于IMSI拨测选择 | `ADD SELCHFGBYIMSI` |
| 2 | 基于IMSI号段选择（多CHF组负载均衡） | - |
| 3 | PCF下发的chargingInfo | - |
| 4 | UDM签约CC→本地配置的CHF（DNN/APN级CC优先于会话级CC） | - |
| 5 | NRF发现CHF（仅支持优先级/权重，不支持主备） | - |
| 6 | 本地配置CC选择CHF | `ADD SELECTCHFGBYCC` |

### K52: 计费会话创建流程
> 来源: 计费会话创建流程_76308085

**协议知识**

1. UE发起PDU会话建立请求
2. SMF→PCF: Npcf_SMPolicyControl_Create（获取PCC规则和计费策略）
3. PCF→CHF: Nchf_SpendingLimitControl_Subscribe（若用户关联Sy配额）
4. CHF→PCF: 返回用户配额信息
5. PCF→SMF: 下发PCC规则+计费策略
6. SMF→UPF: PFCP会话建立请求（创建PDR/FAR，指示地址分配）
7. UPF→SMF: 返回分配的IP地址
8. SMF选择CHF
9. SMF→CHF: Nchf_ConvergedCharging_ChargingDataCreate请求
10. CHF: 检查余额→预留配额→开启CDR
11. CHF→SMF: 授权配额+触发条件
12. SMF→UPF: PFCP会话修改请求（创建PDR/FAR/URR+关联关系）
13. UPF→SMF: 响应
14. PDU会话建立成功

### K53: N40创建请求/响应关键信元
> 来源: 计费会话创建流程_76308085

**协议知识**

**请求关键信元：**
- `nfConsumerIdentification`: SMF标识(IPv4/IPv6/名称/PLMN)
- `multipleUnitUsage`: UPFID, ratingGroup, requestedUnit
- `pDUSessionChargingInformation`: chargingId, chargingCharacteristics, startTime
- `notifyUri`: 接收CHF notify的SMF地址

**响应关键信元：**
- `grantedUnit`: totalVolume(字节), time(秒)
- `triggers`: triggerType + triggerCategory
- `timeQuotaThreshold`, `volumeQuotaThreshold`

**创建URR关键信元：**
- URR ID, Measurement Method, Reporting Triggers
- Volume Quota, Time Quota, Volume Threshold, Time Threshold
- Linked URR ID, Measurement Information

### K54: 在线 vs 离线计费的信元差异（隐性规则）
> 来源: 计费会话创建流程_76308085

**隐性规则**

| 信元 | 在线计费 | 离线计费 |
|------|---------|---------|
| requestedUnit (N40请求) | 携带 | **不携带** |
| grantedUnit (N40响应) | 携带 | **不携带** |
| timeQuotaThreshold/volumeQuotaThreshold | 携带 | **不携带** |
| QUOTA_THRESHOLD/QUOTA_EXHAUSTED trigger | 携带 | **不携带** |
| Volume/Time/Event Quota (N4 URR) | 携带 | **不携带** |

这是区分在线/离线计费的核心信元差异。

### K55: 计费会话更新的四种触发场景
> 来源: 计费会话更新流程_76428001

**方案设计知识**

| 场景 | 触发条件 | 关键流程 |
|------|---------|---------|
| UPF触发 | 配额耗尽/阈值到达、配额空闲时间门限、访问无配额新业务 | UPF Usage Report → SMF → CHF → 新配额 → UPF |
| SMF触发 | 在线配额有效时长超期 | SMF查询UPF用量 → CHF → 新配额 → UPF |
| 外部事件触发 | 服务节点变更、PRA区域变更、QoS改变、用户位置更新、终端时区改变、PLMN变更 | UE→SMF→UPF查询→CHF→新配额→UPF |
| CHF触发 | 重授权（如用户充值成功） | CHF Notify → SMF查询UPF→CHF→新配额→UPF |

**UPF定时器机制：** 触发上报后启动定时器 = `T3RESPONSE * N3REQUEST + 4s`（`SET UPPFCPPATH`配置）；超时未收到配额更新则UPF阻塞业务。

### K56: N40更新请求的trigger规则（隐性）
> 来源: 计费会话更新流程_76428001

**隐性规则**

- 请求消息triggerType只能携带**一个**（当前触发的那个，多个同时满足时取优先级最高的）
- 响应消息triggerType携带**全集**（所有满足条件的）

### K57: 计费会话释放流程
> 来源: 计费会话释放流程_16976658

**协议知识**

1. UE发起PDU会话释放请求
2. SMF→UPF: PFCP会话删除请求（请求上报计费信息）
3. UPF→SMF: 返回计费统计信息
4. SMF→CHF: Nchf_ConvergedCharging_ChargingDataRelease请求
5. CHF: 扣费+关闭CHF-CDR
6. CHF→SMF: HTTP 204 No Content
7. PDU会话释放成功

**N40释放请求关键信元：**
- `multipleUnitUsage`: 最终用量上报
- `triggers`: triggerType=FINAL, triggerCategory=IMMEDIATE_REPORT
- `pDUSessionChargingInformation`: stopTime, sessionStopIndicator=true

### K58: 异常去活的triggerType填写规则（隐性）
> 来源: 计费会话释放流程_16976658

**隐性规则**

| 去活场景 | triggerType值 |
|----------|--------------|
| 正常去活 | FINAL |
| 异常去活（有`ADD N40DIAGTRIGGER`） | 按RELEASETRIGGER参数配置 |
| 异常去活（无N40DIAGTRIGGER，`SET CNVRGDCHGPARA` SPTABNTRIGGER=ENABLE） | AbnormalRelease |
| 异常去活（无N40DIAGTRIGGER，SPTABNTRIGGER=DISABLE） | FINAL |

**优先级：** `ADD N40DIAGTRIGGER` > `SET CNVRGDCHGPARA` SPTABNTRIGGER

### K59: 计费会话通知流程（CHF发起）
> 来源: 计费会话通知流程_57206245

**协议知识**

**CHF发起重授权（仅在线计费）：**
1. CHF发送ChargingDataNotify Request（notificationType=REAUTHORIZATION）
2. SMF确认
3. SMF查询UPF用量
4. SMF→CHF: ChargingDataUpdate Request（重新申请配额）
5. CHF下发新计费参数

**CHF发起去激活（所有计费类型）：**
1. CHF发送ChargingDataNotify Request（notificationType=ABORT_CHARGING）
2. SMF确认
3. SMF→UPF: PFCP会话删除（丢弃数据包，释放资源）
4. SMF→CHF: ChargingDataRelease Request（最终用量上报）
5. SMF发起PDU会话释放

---

## 四、计费事件触发条件

### K60: 计费触发条件分类体系
> 来源: 计费事件触发条件_01_10007

**原理知识**

**两个级别：**
- Session级：应用于整个PDU会话
- RG级：应用于PDU会话内的特定RG

**冲突解决：** Session级和RG级冲突时，**Session级优先**。

**关键触发器：**

| 触发器 | 级别 | 缺省模式 | CHF可变更 |
|--------|------|---------|----------|
| Start of PDU Session | Session | Immediate | N/A |
| QoS change | Session/RG | Deferred | 是 |
| User Location change | Session/RG | Deferred | 是 |
| UE time zone change | Session/RG | Immediate | 是 |
| PLMN change | Session/RG | Immediate | 是 |
| RAT type change | Session/RG | Immediate | 是 |
| UPF add/remove | Session/RG | Immediate | 是 |
| PDU session time/volume/event limit | Session | Immediate | 仅使能 |
| RG time/volume/event limit | RG | Deferred | 是 |
| Quota time/volume/unit threshold | RG | Immediate | 仅使能 |
| Quota time/volume/unit exhausted | RG | Immediate | 仅使能 |
| Quota validity time expiry | RG | Immediate | 仅使能 |
| QHT expiry | RG | Immediate | 仅使能 |
| End of PDU Session | Session | Immediate | N/A |

**配置优先级：** CHF下发 > SMF本地(`ADD PDUTRIGGER`/`ADD RGTRIGGER`)

---

## 五、融合计费可靠性

### K61: 未部署NCG的CHF主备切换（3种场景+1回切）
> 来源: 融合计费可靠性（未部署NCG）_01_10008

**方案设计知识**

| 场景 | 触发条件 | 处理 |
|------|---------|------|
| 场景一 | SMF感知主CHF异常（TXTIMER超时） | 向备CHF重发 |
| 场景二 | SMF超时未收到响应（FHACTION=CONTINUE或RETRY_AND_TERM） | 向备CHF重发 |
| 场景三 | 收到异常响应码（SCACT=FAILOVER） | 向备CHF重发 |
| P4回切 | 主CHF恢复后 | AUTOFAILBACK回切 |

**约束：** 未部署华为NCG时，**不支持计费消息缓存**（ChargingDataRef分配冲突）。

### K62: 部署NCG时的故障处理
> 来源: 融合计费可靠性（部署NCG）_31702099

**方案设计知识**

**OCS/CHF故障处理：**
1. SMF→NCG→OCS/CHF1（超时/异常）
2. NCG→OCS/CHF2（超时/异常）
3. NCG代OCS/CHF应答：给SMF成功响应+携带本地配置配额；生成异常话单

**计费消息缓存（4个必要配置）：**
1. `SET FAILHANDLING`: FHACTION=CONTINUE
2. `ADD PDUSCACT`: SCACT=FAILOVER或CONTINUE
3. `SET N40MSGSTG`: STGSWITCH（开启缓存）
4. `SET CNVRGDCHGPARA`: CHGDATAREFGEN=SMF

**ChargingDataRef生成规则：**
- CHGDATAREFGEN=SMF: SMF分配，忽略CHF下发的
- CHGDATAREFGEN=SMF + CHGDATAREFUSE=CHF: 优先用CHF的

**缓存回放流程：**
1. NCG恢复后，超过最小重放间隔（`SET N40MSGSTG`的REPLAYINTERVAL）
2. 发送ChargingDataFailureUpdate + ChargingDataFailureafterUpdate
3. 响应码2XX=成功释放；429=继续存储待重试

---

## 六、PCC规则与计费策略

### K63: PCC规则类别与一致性要求
> 来源: PCC规则及计费策略_90776686

**配置知识**

| 规则类别 | PCF | SMF | UPF |
|---------|-----|-----|-----|
| 动态规则 | 定义名称+内容，下发 | 传递 | 执行 |
| 预定义规则 | 定义名称（与SMF匹配） | 匹配名称，传递 | 匹配本地配置，执行 |
| 预定义规则组 | 名称与SMF UserProfile匹配 | 定义UserProfile包含多条规则 | 匹配UserProfile，按优先级执行 |
| 本地规则 | 无关联 | 定义UserProfile | 匹配并执行 |

**优先级：** PCF全局优先级。相同时动态>预定义。

**一致性要求（SMF↔UPF必须匹配）：** UserProfile name, Rule name, URR ID

### K64: 多UPF配额管理
> 来源: 多UPF配额管理_90776687

**方案设计知识**

**华为融合计费只支持CHF管理方式：** 每个UPF独立配额。
- SMF在每个UPF基础上请求配额（`Multiple Unit Usage`携带`UPF ID`）
- 哪个UPF请求配额，配额就授予哪个UPF
- I-UPF和UL CL UPF不下发配额
- 只有主锚点(PSA1)和辅助锚点(PSA2)需要配额管理

### K65: MEC计费流程
> 来源: MEC计费流程_01_10005

**方案设计知识**

架构：UL CL + PSA1(主锚点) + PSA2(辅锚点)
- UL CL UPF没有计费规则，不进行计费
- PSA1和PSA2各自独立申请配额
- SMF按UPF独立请求CHF（携带UPF ID）
- 本地DN通过PSA2，互联网通过PSA1

### K66: 互操作计费流程
> 来源: 互操作计费流程_01_10006

**方案设计知识**

- PGW-C与SMF必须共部署，使用相同融合计费机制
- 切换发生时RAT type change trigger激活
- PGW-C/SMF关闭所有使用计数器→向CHF发送Update→CHF更新CDR→开始新计数器和时间戳

---

## 七、NCG部署场景的计费流程

### K67: NCG场景的在线/融合计费流程
> 来源: 计费流程_43650335

**方案设计知识**

1. SMF→NCG: ChargingDataRequest[Initial]
2. NCG根据CC确定在线/融合→OCS/CHF: 转发
3. OCS/CHF→NCG: 配额响应
4. NCG生成CDR→SMF: 转发响应
5. 触发器→SMF→NCG→OCS/CHF: ChargingDataRequest[Update]
6. OCS/CHF→NCG: 更新响应
7. NCG关闭当前CDR，打开新CDR→SMF: 转发

**NCG过滤控制命令：**
- `ADD CCPCCACT` FWDOCSENABLE: 控制每个CC的OCS转发
- `ADD CCPDNNACT` FWDOCSENABLE: 控制每个DNN+CC的OCS转发
- `ADD CCPRGACT` FWDOCSENABLE: 控制每个RG的OCS转发

### K68: CHF-CDR话单关键字段
> 来源: CHF-CDR话单_43364675

**协议知识**

| 字段 | TAG | 描述 |
|------|-----|------|
| recordType | 0x80 | CDR类型 |
| Recording NF ID | 0x81 | CHF名称 |
| Subscriber Identifier | 0xa2 | SUPI |
| NF Consumer Information | 0xa3 | SMF信息 |
| Triggers | 0xa4 | 触发器列表 |
| List of Multiple Unit Information | 0xa5 | 使用报告（含RG/SID/配额/流量/时长） |

---

## 八、关键配置命令索引

### K69: 融合计费关键配置命令汇总
> 来源: 多个文件

**配置知识**

| 命令 | 用途 | 关键参数 |
|------|------|---------|
| `ADD SELECTCHFGBYCC` | 基于CC选择CHF组 | 主CHF组、备CHF组 |
| `ADD SELCHFGBYIMSI` | 基于IMSI选择CHF | - |
| `SET FAILHANDLING` | 故障处理 | TXTIMER、FHACTION、AUTOFAILBACK |
| `ADD PDUSCACT` | 异常响应码处理 | SCACT(FAILOVER/CONTINUE) |
| `SET N40MSGSTG` | 计费缓存 | STGSWITCH、REPLAYINTERVAL |
| `SET CNVRGDCHGPARA` | 融合计费参数 | TIMEROUNDMODE、BADRSPACT、OFLRGTIMECALC、RPTBASEDONGU、MERGERGVTSW、CHGDATAREFGEN、SPTABNTRIGGER |
| `SET CTXSTARTRATING` | 初始配额申请 | - |
| `SET CHFINIT` | N40创建触发时机 | CHFINIT |
| `ADD CCT` | RG级配额有效时长 | - |
| `SET UPPFCPPATH` | UPF PFCP定时器 | T3RESPONSE、N3REQUEST |
| `SET STGTRIGGER` | 会话级trigger | - |
| `ADD N40DIAGTRIGGER` | 异常去活trigger | RELEASETRIGGER |
| `SET CDRSTORAGECTRL` | 缓存超期时间 | - |
| `ADD PDUTRIGGER` | Session级本地触发器 | - |
| `ADD RGTRIGGER` | RG级本地触发器 | - |

---

## 知识统计

| 类别 | 数量 |
|------|------|
| 原理知识 | 10 (K42-K50, K60) |
| 协议知识 | 5 (K52, K53, K57, K59, K68) |
| 方案设计知识 | 7 (K43, K55, K61-K62, K64-K67) |
| 配置知识 | 4 (K51, K63, K69, K58) |
| 隐性规则 | 3 (K54, K56, K58) |
| **合计** | **28条** |
