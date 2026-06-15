## 第十一章：Usage Monitoring与FUP

### K162: Usage-Monitoring-Information AVP结构 [协议]
> 来源: K230

Usage-Monitoring-Information AVP（AVP 1067, Grouped类型）包含配额监控信息：

| 子信元 | 功能 |
|--------|------|
| Monitoring-Key | 监控键值，标识一个配额监控实例 |
| Granted-Service-Unit | CHF/PCRF授权的服务单元（配额） |
| Used-Service-Unit | PCEF/SMF已使用的服务单元 |
| Usage-Monitoring-Level | 监控级别（Session级/PCC规则级） |
| Usage-Monitoring-Report | 上报指示 |
| Usage-Monitoring-Support | 监控支持指示 |

---

### K163: Usage-Monitoring-Level AVP [协议]
> 来源: K231

Usage-Monitoring-Level AVP（AVP 1068, 枚举型）：

| 取值 | 含义 |
|------|------|
| SESSION_LEVEL (0) | 配额监控实例应用于整个IP-CAN会话（会话级FUP） |
| PCC_RULE_LEVEL (1) | 配额监控实例应用于一个或多个PCC规则（业务级FUP） |

默认值：未提供时指示PCC_RULE_LEVEL (1)。

---

### K164: Usage-Monitoring-Report AVP [协议]
> 来源: K232

Usage-Monitoring-Report AVP（AVP 1069, 枚举型）：
- USAGE_MONITORING_REPORT_REQUIRED (0)：PCRF指示PCEF应该上报累积流量
- 用于PCRF在RAR/CCA中请求PCEF上报特定监控键值的累积流量（无论门限是否到达）

---

### K165: 会话级FUP vs 业务级FUP对比 [原理]
> 来源: K169

| 维度 | 会话级FUP | 业务级FUP |
|------|-----------|-----------|
| 监控范围 | 用户所有业务 | 特定业务(三四层/七层) |
| N7信元位置 | sessRules.refUmData | PccRule.refUmData |
| URR绑定 | 关联到**所有PDR** | 绑定到**指定业务流PDR** |
| MONITORINGKEY | 动态规则时由PCF下发 | ADD URR中必选配置 |
| UNC/UDG配置量 | 仅需License开关 | 需完整三件套+两套策略 |
| License(UNC) | LKV3W9PCBT12 | LKV2FUPSAT01 |
| License(UDG) | LKV3G5PCBT01 | LKV3G5FPBS01 |

---

### K166: FUP配额驱动策略切换机制 [方案设计]
> 来源: K170

FUP核心机制：配额状态驱动策略切换：

1. **初始**：PCF下发流量阈值 + 规则（高优先级，低费率/免费）
2. **阈值耗尽**：UPF检测VOLTH触发，上报Usage Report → SMF转发PCF
3. **PCF决策**：
   - 配额未耗尽 → 下发新阈值，维持当前规则
   - 配额耗尽 → **不下发新阈值**(refUmData=NULL)，更新QoS(限速/重定向)，切换到低优先级规则(高费率)

**隐性规则**：FUPSESSIONEXC=ENABLE的业务流量**不参与会话级FUP累计**，避免双重计量。

---

### K167: 业务级FUP三件套扩展模型 [配置]
> 来源: K171

业务级FUP是标准三件套的**扩展版本**，需配配额耗尽前/后**两套策略**：

**三组URR：**
1. urr_mk：URRID=1000, USAGERPTMODE=MONITORINGKEY, MONITORINGKEY="2001"（累计流量监控）
2. urr_basic：URRID=2000, USAGERPTMODE=ONLINE, RG=10（配额耗尽前，免费）
3. urr_exhaust：URRID=3000, USAGERPTMODE=ONLINE, RG=20（配额耗尽后，1元/M）

**两套PCCPOLICYGRP：**
- cg_basic：绑定urrg_basic(urr_mk + urr_basic)，FUPSESSIONEXC=ENABLE
- cg_exhaust：绑定urrg_exhaust(urr_mk + urr_exhaust)，FUPSESSIONEXC=ENABLE

**两条RULE：** rule_test1(绑定cg_basic, PRIORITY=30) + rule_test2(绑定cg_exhaust, PRIORITY=40)

---

### K168: FUP URR ID与UMID映射机制 [原理]
> 来源: K172

SMF建立URR ID与UMID之间的映射：
- 预定义规则：通过ADD URR命令配置URR ID和MONITORINGKEY
- 动态规则：SMF直接将PCF下发的UMID转换为URR ID

映射流转路径：UPF检测VOLTH触发 → Usage Report(含URR ID, Volume Measurement) → SMF通过URR ID→UMID映射 → Npcf_SMPolicyControl_Update(accuUsageReports含refUmId, volUsage) → PCF决策

---

## 附录：跨协议映射关系摘要

### Gx → Nchf → N4 参数映射链

| Gx AVP | Nchf N40信元 | N4 PFCP信元 |
|--------|-------------|-------------|
| Online=ENABLE_ONLINE | quotaManagementIndicator=ONLINE_CHARGING | Create URR含Volume/Time/Event Quota |
| Online=DISABLE_ONLINE | quotaManagementIndicator=OFFLINE_CHARGING | Create URR不含配额信元 |
| Metering-Method=DURATION | grantedUnit.time | Time Quota |
| Metering-Method=VOLUME | grantedUnit.totalVolume | Volume Quota |
| Metering-Method=DURATION_VOLUME | grantedUnit.time+totalVolume | Time Quota+Volume Quota |
| Rating-Group | multipleUnitUsage.ratingGroup | (SMF映射到URR ID) |
| Reporting-Level=SERVICE_IDENTIFIER_LEVEL | UsedUnitContainer.serviceId+ratingGroup | (N4无对应，SMF层处理) |
| Reporting-Level=RATING_GROUP_LEVEL | UsedUnitContainer.ratingGroup | (N4无对应，SMF层处理) |
| Monitoring-Key | (5G: UsageMonitoringData动作组) | (5G: 独立UM URR) |
| Usage-Monitoring-Level=SESSION_LEVEL | (5G: 会话级UM) | (5G: 会话级UM URR) |
| Usage-Monitoring-Level=PCC_RULE_LEVEL | (5G: 业务级UM) | (5G: 业务级UM URR) |

### Trigger映射链

| Gx Event-Trigger | Nchf Trigger Type | N4 Reporting Trigger |
|-------------------|-------------------|---------------------|
| USAGE_REPORT | (Usage Monitoring机制) | (配额阈值/耗尽触发) |
| USER_LOCATION_CHANGE | USER_LOCATION_CHANGE | (SMF层Query URR) |
| REVALIDATION_TIMEOUT | VALIDITY_TIME | (SMF本地定时器) |
| (配额相关) | QUOTA_THRESHOLD | VOLTH / TIMTH |
| (配额相关) | QUOTA_EXHAUSTED | VOLQU / TIMQU |
| (配额保持) | - | QUHTI |

---

## 知识统计

| 章节 | 知识条目 | 数量 |
|------|----------|------|
| 第七章：Nchf融合计费服务 | K101-K121 | 21 |
| 第八章：PFCP/N4接口与URR | K122-K135 | 14 |
| 第九章：Gx/PCC策略与计费 | K136-K146 | 11 |
| 第十章：规则匹配与业务识别 | K147-K161 | 15 |
| 第十一章：Usage Monitoring与FUP | K162-K168 | 7 |
| **合计** | K101-K168 | **68** |

### 按类型统计

| 类型 | 数量 | 编号 |
|------|------|------|
| [协议] | 30 | K101, K103, K104, K107, K109, K110, K114-K119, K123-K125, K127-K130, K132-K135, K137, K138, K140-K143, K152, K162-K164 |
| [原理] | 17 | K112, K122, K144, K146-K150, K155-K157, K159-K161, K165, K168 |
| [隐性规则] | 4 | K105, K108, K111, K151 |
| [方案设计] | 10 | K106, K113, K120-K121, K153, K154, K158, K166 |
| [配置] | 7 | K102, K123, K136, K145, K151, K167 |

### 融合去重记录

| 新编号 | 融合来源 | 说明 |
|--------|----------|------|
| K101 | K04 + K190 | 四种服务操作合并 |
| K102 | K08 + K51 + K191 | CHF选择优先级保留6级版本 |
| K103 | K53 + K192 | Create Request信元合并 |
| K104 | K53 + K193 | Create Response信元合并 |
| K105 | K54 + K194 | 在线/离线信元差异合并 |
| K106 | K55 + K197 | Update触发场景合并 |
| K108 | K56 + K200 | Trigger全集与优先级合并 |
| K109 | K57 + K201 | Release流程合并 |
| K110 | K59 + K202 | Notify通知合并 |
| K112 | K195 + K258 | RG与URR ID映射合并 |
| K123 | K209 + K210 + K211 | URR生命周期三阶段合并 |
| K131 | K49 + K205 + K220 | QHT三来源合并 |
| K136 | K63 + K159 | PCC规则类别合并 |
| K139 | K158 + K226 | Online/Offline AVP合并 |
| K146 | K16 + K159 | 三种规则类型对比合并 |
| K149 | K17 + K254 | 规则匹配原则合并 |

---


