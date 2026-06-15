# Batch 04: SM策略 + ULCL分流 + FUP 知识草稿

## 来源文件清单

| # | 文件组 | 篇数 | 重点 |
|---|--------|------|------|
| 1 | SM策略整体介绍+计费参数 | 3 | PCF下发计费参数全集 |
| 2 | SM策略E2E原理 | 4 | 动态/预定义规则与计费 |
| 3 | 业务拆解方法 | 2 | 配额状态拆解 |
| 4 | 本地/动态/预定义PCC配置 | 9 | 配置命令与逻辑 |
| 5 | 资费差异化控制(动态) | 5 | 用户等级→费率映射 |
| 6 | 多业务场景策略控制 | 8 | 配额+时间约束组合 |
| 7 | 业务重定向方案 | 10 | 配额耗尽→重定向充值 |
| 8 | 位置区域带宽控制 | 7 | USAGERPTMODE=QOS |
| 9 | ULCL分流计费 | 3 | 多锚点独立配额 |
| 10 | FUP会话级+业务级 | 9 | MonitoringKey+累计流量 |

---

## 一、PCF计费参数与规则类型

### K157: PCF下发的计费参数全集（ChargingData）
> 来源: 计费参数_86483630

**原理知识**

PCF通过ChargingData动作组下发计费参数：

| 参数 | 含义 | 必选 |
|------|------|------|
| chgId | 计费控制策略数据标识 | 必选(1次) |
| meteringMethod | 离线计量方式：DURATION/VOLUME/DURATION_VOLUME/EVENT | 可选 |
| offline | 是否离线计费 | 可选 |
| online | 是否在线计费 | 可选 |
| ratingGroup | 费率组(RG) | 可选 |
| reportingLevel | 上报级别：SER_ID_LEVEL/RAT_GR_LEVEL/SPON_CON_LEVEL | 可选 |
| serviceId | 服务标识(SID) | 可选 |
| sponsorId | 赞助商标识 | 可选 |
| sdfHandl | 在线等待信用响应时是否允许通过 | 可选(仅在线) |

### K158: offline/online互斥规则
> 来源: 计费参数_86483630

**隐性规则**

- offline和online**不能同时为true**，但可同时为false（不计费）
- 优先级：PCF下发 > SMF本地配置
- 两者都不存在或都为false时，使用PDU会话的**默认计费方法**
- sdfHandl仅用于在线计费场景
- meteringMethod为离线专用参数

### K159: 三种规则类型与计费信息携带方式
> 来源: 预定义规则_预定义规则组_本地规则_86483636

**原理知识**

| 维度 | 动态规则 | 预定义规则 | 本地规则 |
|------|----------|------------|----------|
| 流条件 | PCF配置 | UPF配置 | UPF配置 |
| 流动作 | PCF配置 | UPF配置 | UPF配置 |
| 规则名一致性 | 不需要 | PCF/SMF/UPF三侧一致 | SMF/UPF两侧一致 |
| 业务识别 | 不识别（非定向流） | UPF识别（三四层+七层） | UPF识别 |
| 计费控制 | PCF通过ChargingData下发 | UPF本地配置计费动作 | UPF本地配置 |
| 适用场景 | 非定向流、达量限速 | 定向流（需识别特定业务） | PCF故障降级方案 |

### K160: 5G动态规则必配动作组
> 来源: 业务配置逻辑_64569729

**配置知识**

5G DynamicPccRule完整配置需7种动作类型：
1. FlowDescription（流描述）
2. FlowInformation（流信息）
3. TrafficControlData（flowStatus=enabled，配流描述时必须配）
4. Arp（优先级参数）
5. QoSData（带宽参数：5qi, maxbrUl, maxbrDl）
6. UsageMornitoringData（配额监控键值，业务关联配额时必须通过5G动作组下发）
7. DynamicPccRule（汇总动作）

4G/5G差异：条件组Object选择4G选"IPSession"，5G选"SmfSession"；策略类型4G为"Gx Policy"，5G为"N7 Policy"。

---

## 二、配额状态驱动策略变更

### K161: 配额类型与触发器
> 来源: 动态规则_86483635

**原理知识**

配额类型（PCF用于策略计算）：
- **流量配额**：UPCF统计的用户业务流量
- **在线时长配额**：UPCF统计的在线会话时长
- **时长配额**：SMF上报的时长

**关键触发器**：
- IPCAN_EST：PDU会话建立（必须配置）
- US_RE：使用量状态上报（配额变化触发策略更新）
- SAREA_CH/PRA_CH/SCELL_CH/PLMN_CH：位置变更
- APP_STA/APP_STP：应用类型变更
- TimeRangeChange：时间范围变更

### K162: 多业务拆解6步法
> 来源: 多业务拆解方法_70951751

**方案设计知识**

多业务拆解方法：**抽取 → 合并 → 排查 → 规则类型判断 → 触发器选择 → 业务关系判断**

关键步骤：
- 合并：条件相同的动作合并或动作相同的条件合并
- 排查：确认条件完备（如"配额未耗尽"+"配额耗尽"=全部状态）
- 触发器选择：IPCAN_EST + US_RE（配额变化）+ 可选TimeRangeChange
- 业务互斥：通过互斥组定义多业务间关系（订购互斥/激活互斥）

### K163: 基于用户等级的资费差异化控制
> 来源: 整体方案设计_93907864

**方案设计知识**

用户等级→费率/带宽映射：
| 用户等级 | RatingGroup | 上下行带宽 |
|----------|-------------|------------|
| Gold | RG=1 | 100 Mbps |
| Silver | RG=2 | 50 Mbps |
| Normal | RG=3 | 10 Mbps |

PCF配置：3个规则(Rule_Gold/Silver/Normal)，每个规则动作组包含ChargingData(设置ratingGroup) + QoSData(设置带宽)。用户等级变更由业务发放系统通过订阅通知推送。

### K164: 多业务场景配额+时间约束组合
> 来源: 整体拆解逻辑_71227537

**方案设计知识**

场景1（基础流量包）：配额未耗尽→10Mbps；配额耗尽→1Mbps+通知。触发器：IPCAN_EST + US_RE

场景2（周末流量包）：配额未耗尽→100Mbps（仅周末）；配额耗尽→终止业务+通知。触发器：IPCAN_EST + US_RE + **TimeRangeChange**

业务互斥：场景2优先级高于场景1，使用"激活+替换"互斥模式。

---

## 三、重定向方案（配额耗尽场景）

### K165: 配额耗尽重定向完整控制链
> 来源: 整体方案设计_08571784

**方案设计知识**

配额耗尽后完整控制：**限速(1Kbit/s) + 发送提醒通知 + 重定向到充值页面**

**动态规则方案（仅PCF配置）**：
- Rule_Normal：条件=配额未耗尽，动作=QoSData(100Mbit/s)
- Rule_Exhaust：条件=配额耗尽，动作=QoSData(1Kbit/s) + RedirectInformation

**预定义规则方案（PCF+SMF+UPF三方配置）**：
- PCF侧：下发规则名Rule_Normal和up_Exhaust
- SMF侧：识别预定义规则名，配置URR/URRGROUP/PCCPOLICYGRP/RULE
- UPF侧：配置流过滤器+QoS+重定向URL(ADD REDIRECT)+PCCPOLICYGRP+RULE

**隐性规则**：SMF配预定义规则级则UPF配规则级；SMF配规则组级则UPF须配规则组级。配额耗尽场景需用**预定义规则组**。

### K166: FUP达量限速配置实例
> 来源: 业务配置逻辑_64569729

**方案设计知识**

需求：2000MB配额，<100%时10Mbit/s，>=100%时512Kbit/s。

5G配置方案：
- AG_Basic：SessionRuleAction（缺省QoS Flow）
- AG_Basic_Dyn：DynamicPccRule（rule01, maxbr=10000Kbit/s, umId=2001）
- predefinedPccRule01：pccRuleId=Pre_Quota_exhaust（配额耗尽时激活预定义规则）
- 策略：Policy_usage，trigger=US_RE OR IPCAN_EST
- 配额：quota01, MonitorKey=2001, Value=2048000, Slice=100%

---

## 四、ULCL分流计费

### K167: ULCL多锚点独立配额管理
> 来源: 分流场景下的计费_97585673

**方案设计知识**

ULCL计费架构：
- 主锚点PSA0(Internet) + 辅锚点PSA1(本地DN) + UL CL UPF(分流器，通常与PSA1合设)
- SMF将计费规则通过N4接口分别下发到PSA0和PSA1
- CHF对每个锚点UPF**独立进行配额管理**，每个UPF**独享配额**
- SMF按UPF向CHF申请配额，消息中Multiple Unit Usage携带UPF ID
- **UL CL UPF不计费**：UL CL UPF没有计费规则

### K168: ULCL系统约束
> 来源: 系统影响与约束_97556113

**隐性规则**

- UL CL仅针对5G用户，2/3/4G不支持
- 国漫V-SMF场景下不支持UL CL
- 当前版本仅支持UL CL UPF和辅锚点UPF**合一部署**
- **UL CL方案只支持融合计费**

---

## 五、FUP（Fair Usage Policy）

### K169: 会话级FUP vs 业务级FUP对比
> 来源: 综合FUP文档

**原理知识**

| 维度 | 会话级FUP | 业务级FUP |
|------|-----------|-----------|
| 监控范围 | 用户所有业务 | 特定业务(三四层/七层) |
| N7信元位置 | sessRules.refUmData | PccRule.refUmData |
| URR绑定 | 关联到**所有PDR** | 绑定到**指定业务流PDR** |
| MONITORINGKEY | 动态规则时由PCF下发 | ADD URR中必选配置 |
| UNC/UDG配置量 | 仅需License开关 | 需完整三件套+两套策略 |
| License(UNC) | LKV3W9PCBT12 | LKV2FUPSAT01 |
| License(UDG) | LKV3G5PCBT01 | LKV3G5FPBS01 |

### K170: FUP配额驱动策略切换机制
> 来源: 综合会话级和业务级原理

**方案设计知识**

FUP核心机制：配额状态驱动策略切换：
1. **初始**：PCF下发流量阈值 + 规则(高优先级，低费率/免费)
2. **阈值耗尽**：UPF检测VOLTH触发，上报Usage Report → SMF转发PCF
3. **PCF决策**：
   - 配额未耗尽 → 下发新阈值，维持当前规则
   - 配额耗尽 → **不下发新阈值**(refUmData=NULL)，更新QoS(限速/重定向)，切换到低优先级规则(高费率)

**隐性规则**：FUPSESSIONEXC=ENABLE的业务流量**不参与会话级FUP累计**，避免双重计量。

### K171: 业务级FUP三件套扩展模型
> 来源: 配置业务级累计流量策略控制_70607729

**配置知识**

业务级FUP是标准三件套的**扩展版本**，需配配额耗尽前/后**两套策略**：

**三组URR**：
1. urr_mk：URRID=1000, USAGERPTMODE=MONITORINGKEY, MONITORINGKEY="2001"（累计流量监控）
2. urr_basic：URRID=2000, USAGERPTMODE=ONLINE, RG=10（配额耗尽前，免费）
3. urr_exhaust：URRID=3000, USAGERPTMODE=ONLINE, RG=20（配额耗尽后，1元/M）

**两套PCCPOLICYGRP**：
- cg_basic：绑定urrg_basic(urr_mk + urr_basic)，FUPSESSIONEXC=ENABLE
- cg_exhaust：绑定urrg_exhaust(urr_mk + urr_exhaust)，FUPSESSIONEXC=ENABLE

**两条RULE**：rule_test1(绑定cg_basic, PRIORITY=30) + rule_test2(绑定cg_exhaust, PRIORITY=40)

### K172: FUP URR ID与UMID映射机制
> 来源: 基于N7接口策略控制_23928080

**原理知识**

SMF建立URR ID与UMID之间的映射：
- 预定义规则：通过ADD URR命令配置URR ID和MONITORINGKEY
- 动态规则：SMF直接将PCF下发的UMID转换为URR ID

UPF检测VOLTH触发 → Usage Report(含URR ID, Volume Measurement) → SMF通过URR ID→UMID映射 → Npcf_SMPolicyControl_Update(accuUsageReports含refUmId, volUsage) → PCF决策

---

## 知识统计

| 类别 | 数量 |
|------|------|
| 原理知识 | 6 (K157, K159, K161, K169, K172) |
| 方案设计知识 | 6 (K162-K166, K167, K170) |
| 配置知识 | 2 (K160, K171) |
| 隐性规则 | 3 (K158, K165, K168) |
| **合计** | **16条 (K157-K172)** |
