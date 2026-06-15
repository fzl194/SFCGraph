# Batch-29: UNC E2E方案 - 位置区域带宽差异化与多业务场景策略控制

## 1. 概述

本批文档来自"5G PCC之SM策略解决方案"的典型业务场景E2E方案设计（UNC侧），涵盖两个独立的E2E方案：

**方案一：基于位置区域的带宽差异化控制方案（预定义）**（3个文档）

该方案解决用户在不同位置区域接入时带宽差异化控制的问题。需求场景为：用户在国内接入时享受100Mbit/s高带宽，在国外（漫游区）接入时带宽被限制为1Mbit/s。方案采用预定义规则方式实现，PCF根据用户MCC/MNC位置变化下发不同的预定义规则名，SMF/UPF侧需配置对应的预定义规则内容。文档覆盖了需求描述、整体方案设计（PCF/SMF/UPF三侧设计）和UPF侧MML配置实操。

**方案二：基于多业务场景的策略控制（动态）**（7个文档，重点）

该方案解决运营商将多个业务（基本FUP业务+假期业务）组合为套餐，根据时间、配额状态等条件动态下发策略的问题。方案采用动态规则方式实现，PCF侧负责全部业务配置，SMF/UPF侧无需配置。文档覆盖了整体拆解逻辑、PCF侧业务设计、业务1（Service_FUP）配置、业务2（Service_Holiday）配置、套餐配置（互斥组+套餐+开户签约）和两种调测方法（信令调测法+快速调测法）。

这两个方案共同体现了带宽控制在PCC策略体系中的核心定位：位置区域方案是"按位置条件差异化带宽"，多业务方案是"按多业务组合实现策略控制（带宽+计费+消息通知+业务互斥）"。

---

## 2. 核心知识点

### 2.1 位置区域带宽差异化方案 -- 预定义规则三侧设计

**需求拆解**：将原始需求转换为"条件-动作"映射表。国内接入 -> 上下行100Mbit/s；国外漫游区接入 -> 上下行1Mbit/s。两个条件之和等于全部位置状态，场景完备。

**业务拆解五步法**：抽取 -> 合并 -> 排查 -> 规则类型判断 -> 选择触发器。
- **抽取**：按照"在XX条件下，实现XX控制"的逻辑抽取条件（国内/国外接入）和动作（控制上下行带宽）。
- **合并**：相同条件或相同动作的逻辑语句合并。此场景无可合并项。
- **排查**：确认条件完备性，"国内+国外=全部位置状态"。
- **规则类型判断**：选用预定义规则（Predefined Rule），因为需求明确要求通过预定义方式实现。
- **触发器选择**：配置 `IPCAN_EST`（用户上线触发策略计算）+ `PLMN_CH`（用户MCC/MNC位置变化触发策略更新）。

**PCF侧配置顺序**：PLMN -> 漫游区（RoamingRegion） -> 条件组 -> 5G动作组 -> 规则 -> 策略 -> 业务。PCF定义两个预定义规则 Predefined1（条件：RoamingRegion=Region_Local，动作：下发Predefined1）和 Predefined2（条件：RoamingRegion!=Region_Local，动作：下发Predefined2）。

**SMF侧设计**：SMF侧仅需配置预定义规则的QoS参数（5QI、ARP、上下行带宽），配置链路为 URR -> QOSPROP -> PCCPOLICYGRP -> RULE。

**UPF侧设计**：UPF侧需配置完整的流识别+QoS执行链路，配置链路为 FILTER -> FLOWFILTER -> FLTBINDFLOWF -> URR -> QOSPROP -> PCCPOLICYGRP -> RULE。

### 2.2 多业务场景策略控制 -- 整体拆解逻辑

**两个单业务的需求拆解**：

| 场景 | 配额状态 | 上下行带宽 | 消息通知 | 时间限制 |
|------|----------|-----------|---------|---------|
| 基本FUP业务 | 未耗尽 | 10 Mbps | 否 | 全时段 |
| 基本FUP业务 | 耗尽 | 1 Mbps | 是 | 全时段 |
| 假期业务 | 未耗尽 | 100 Mbps | 否 | 仅周末 |
| 假期业务 | 耗尽 | 终止业务 | 是 | 仅周末 |

**业务1（Service_FUP）拆解**：条件为配额状态（未耗尽/耗尽），动作为带宽控制+消息通知。触发器为 `IPCAN_EST` + `US_RE`。规则类型为动态规则（DynamicPccRule）。

**业务2（Service_Holiday）拆解**：条件为配额状态 + 时间段（周末），动作为带宽控制/终止业务+消息通知。触发器为 `IPCAN_EST` + `US_RE` + `TimeRangeChange`。规则类型为动态规则。

**多业务逻辑关系判断**：业务1与业务2为"激活+替换"互斥关系。优先级：Service_Holiday（优先级1） > Service_FUP（优先级2）。周末时段且假期配额未耗尽时，假期业务激活并替换基本业务；假期配额耗尽或非周末时段时，基本业务激活。

**套餐逻辑**：Flow_Package套餐包含Service_FUP和Service_Holiday两个业务，通过互斥组Mutex_FUP_Holiday（类型=激活，互斥操作=替换）管理业务间的切换。

### 2.3 多业务方案 -- PCF侧业务设计

**Service_FUP业务**：包含1个策略（Policy_FUP）和10GB配额（Quota_10GB，监控键值=100）。
- Policy_FUP触发器：IPCAN_EST + US_RE
- Rule_FUP_Normal：条件=配额未耗尽，动作=DynamicPccRule（maxbrUL/DL=10 Mbps）
- Rule_FUP_Exhaust：条件=配额耗尽，动作=DynamicPccRule（maxbrUL/DL=1 Mbps），挂载消息通知Notification_FUP

**Service_Holiday业务**：包含1个策略（Policy_Holiday）和20GB配额（Quota_20GB，监控键值=101）。
- Policy_Holiday触发器：IPCAN_EST + US_RE + TimeRangeChange
- Rule_Holiday_Normal：条件=配额未耗尽 AND 周末时段，动作=DynamicPccRule（maxbrUL/DL=100 Mbps）
- Rule_Holiday_Exhaust：条件=配额耗尽 AND 周末时段，动作=Non-PCC（终止业务），挂载消息通知Notification_Holiday

**5G动作组配置要点**：采用"仅使用DynamicPccRule类型动作建立缺省QoS Flow"方式。5qi和arp取值为Object Attribute引用SmfSession.SubsDefQos5qi/SubsDefQosPriorityLevel等，即PCF直接取用户上线请求的5QI/ARP进行配置下发，无需在PCF侧硬编码。

### 2.4 多业务方案 -- 配置层次与依赖关系

**业务1配置层次**（完整9步配置链）：
1. 配额（Quota_10GB：流量型，10,485,760 KB=10GB，会话级，监控键值100，每月1日01:00复位）
2. 短信/邮件模板（Notification_Template_FUP）
3. 消息通知（Notification_FUP：发送抑制=天，唯一键=Quota.QuotaStatus）
4. 条件组（CG_FUP_Normal：QuotaStatus=Normal；CG_FUP_Exhaust：QuotaStatus=Exhaust）
5. 5G动作组（FlowDescription -> FlowInformation -> TrafficControlData -> Arp -> QoSData_Normal/Exhaust -> UsageMonitoringData -> DynamicPccRule_Normal/Exhaust）
6. 规则（Rule_FUP_Normal -> 条件组CG_FUP_Normal -> 动作组AG_FUP_Normal；Rule_FUP_Exhaust -> 条件组CG_FUP_Exhaust -> 动作组AG_FUP_Exhaust + 消息通知Notification_FUP）
7. 策略（Policy_FUP：触发器IPCAN_EST+US_RE，包含两条规则）
8. 业务（Service_FUP：VALUE_ADDED_SERVICE，优先级2，QoS模式=替换）
9. 套餐/互斥组/开户签约（在套餐配置中统一完成）

**业务2配置层次**（与业务1类似，关键差异）：
- 配额：Quota_20GB（20,971,520 KB=20GB，监控键值101）
- 条件组增加时间条件：System.DateTime = 相对时间段（周末周六周日，00:00-24:00）
- Rule_Holiday_Exhaust类型为Non-PCC（终止业务），无5G动作组
- 触发器增加TimeRangeChange
- 业务优先级=1（高于Service_FUP的优先级2）

**套餐配置**（3步）：
1. 互斥组（Mutex_FUP_Holiday：类型=激活，互斥操作=替换）
2. 套餐（Flow_Package：包含Service_FUP + Service_Holiday）
3. 开户签约（ADD PSUB增加用户 + ADD PSRVPKG签约套餐Flow_Package）

### 2.5 多业务方案 -- 8种业务场景与策略下发矩阵

由于两个业务各有"配额未耗尽/耗尽"两种状态，叠加"工作日/周末"两种时间，组合出8种完整场景：

| 场景 | 时间 | FUP配额 | Holiday配额 | PCF下发规则 |
|------|------|---------|-------------|------------|
| 1 | 工作日 | 未耗尽 | 未耗尽 | AG_FUP_Normal（10 Mbps） |
| 2 | 工作日 | 未耗尽 | 耗尽 | AG_FUP_Normal（10 Mbps） |
| 3 | 工作日 | 耗尽 | 未耗尽 | AG_FUP_Exhaust（1 Mbps）+ Notification_FUP |
| 4 | 工作日 | 耗尽 | 耗尽 | AG_FUP_Exhaust（1 Mbps）+ Notification_FUP |
| 5 | 周末 | 未耗尽 | 未耗尽 | AG_Holiday_Normal（100 Mbps） |
| 6 | 周末 | 未耗尽 | 耗尽 | AG_FUP_Normal（10 Mbps）+ Notification_Holiday |
| 7 | 周末 | 耗尽 | 未耗尽 | AG_Holiday_Normal（100 Mbps） |
| 8 | 周末 | 耗尽 | 耗尽 | AG_FUP_Exhaust（1 Mbps）+ Notification_Holiday + Notification_FUP |

**核心逻辑**：周末且假期配额未耗尽时，假期业务（100 Mbps）优先激活替换基本业务；假期配额耗尽后，假期业务终止，基本业务激活（10 Mbps或1 Mbps取决于基本配额状态）。

### 2.6 动态规则 vs 预定义规则的方案选择

两个方案形成了鲜明对比：

| 维度 | 位置区域方案（预定义） | 多业务方案（动态） |
|------|---------------------|-------------------|
| 规则类型 | 预定义规则 | 动态规则 |
| PCF配置 | 条件组+动作组(预定义规则名) | 条件组+5G动作组(完整QoS/流信息) |
| SMF配置 | 需配置（URR/QOSPROP/PCCPOLICYGRP/RULE） | 无需配置 |
| UPF配置 | 需配置（FILTER/FLOWFILTER/URR/QOSPROP等） | 无需配置 |
| 策略下发 | PCF下发规则名，SMF/UPF本地匹配 | PCF直接下发完整策略码流 |
| 适用场景 | 固定带宽值，条件简单 | 灵活策略组合，需配额/时间等复杂条件 |

### 2.7 UPCF业务配置对象层级体系

从两个方案中提炼出UPCF统一的业务配置对象层级：

```
配额(Quota) ─────────────────────────────────────┐
通知模板(SMS/Email Template) ────────┐           |
消息通知(Notification) <─────────────┘           |
条件组(ConditionGroup) <─── 条件引用配额/时间对象  |
5G动作组(5GActionGroup) <── 动作组间互相引用       | 全部被引用
规则(Rule) <─── 引用条件组+5G动作组+消息通知       |
策略(Policy) <── 引用规则+触发器                   |
业务(Service) <── 引用策略+配额                   |
互斥组(MutexGroup) <── 引用多个业务              |
套餐(Package) <── 引用多个业务                    |
开户签约 ──> ADD PSUB + ADD PSRVPKG(套餐) <───────┘
```

配置顺序严格自底向上：被引用对象必须先于引用对象创建。

---

## 3. 配置调测要点

### 3.1 位置区域方案 -- UPF侧MML配置（7步）

UPF（UDG）侧预定义规则配置流程，需配置两套完全平行的规则链（Predefined1=100M，Predefined2=1M）：

```mml
// 步骤1-2：配置过滤器+流过滤器（两套）
ADD FILTER: FILTERNAME="f_fup_service_100M", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FILTER: FILTERNAME="f_fup_service_1M", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER: FLOWFILTERNAME="flowfliter_service_100M";
ADD FLTBINDFLOWF: FLOWFILTERNAME="flowfliter_service_100M", FILTERNAME="f_fup_service_100M";
ADD FLOWFILTER: FLOWFILTERNAME="flowfliter_service_1M";
ADD FLTBINDFLOWF: FLOWFILTERNAME="flowfliter_service_1M", FILTERNAME="f_fup_service_1M";

// 步骤3：配置QoS URR（与SMF侧URRID保持一致）
ADD URR: URRNAME="urr_QoS2", URRID=2, USAGERPTMODE=QOS;
ADD URR: URRNAME="urr_QoS3", URRID=3, USAGERPTMODE=QOS;

// 步骤4：配置QoS属性（100M = 100000 kbps，1M = 1000 kbps）
ADD QOSPROP: QOSPROPNAME="qosprop_5qi5_arp2_100", MBRUPLKVALUE=100000, MBRDNLKVALUE=100000, QOSURRNAME="urr_QoS2", DECOUPLINGSW=DISABLE, KEYFLOWDETECTSW=DISABLE;
ADD QOSPROP: QOSPROPNAME="qosprop_5qi5_arp2_1", MBRUPLKVALUE=1000, MBRDNLKVALUE=1000, QOSURRNAME="urr_QoS3", DECOUPLINGSW=DISABLE, KEYFLOWDETECTSW=DISABLE;

// 步骤5：配置PCC策略组
ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccfuppolicy_100M", ..., QOSPROPNAME="qosprop_5qi5_arp2_100";
ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccfuppolicy_1M", ..., QOSPROPNAME="qosprop_5qi5_arp2_1";

// 步骤6：配置预定义规则（名称须与PCF侧一致）
ADD RULE: RULENAME="Predefined1", POLICYTYPE=PCC, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="flowfliter_service_100M", PRIORITY=10, POLICYNAME="pccfuppolicy_100M";
ADD RULE: RULENAME="Predefined2", POLICYTYPE=PCC, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="flowfliter_service_1M", PRIORITY=50, POLICYNAME="pccfuppolicy_1M";

// 步骤7：刷新生效
SET REFRESHSRV: REFRESHTYPE=ALL;
```

**关键约束**：
- UPF侧URRID必须与SMF侧URRID保持严格一致
- 预定义规则名称、数量必须与PCF侧定义完全一致
- PRIORITY值越小优先级越高（Predefined1=10高于Predefined2=50）
- SET REFRESHSRV必须最后执行

### 3.2 多业务方案 -- UPCF Web UI配置要点

**业务1（Service_FUP）核心配置参数**：
- 配额Quota_10GB：流量型，10,485,760 KB，会话级，监控键值=100，分片100%，每月1日01:00复位清零
- 动态规则AG_FUP_Normal：5qi取SmfSession.SubsDefQos5qi，arp取SmfSession.SubsDefQos*，maxbrUL/DL=10 Mbps
- 动态规则AG_FUP_Exhaust：同上但maxbrUL/DL=1 Mbps
- 触发器：IPCAN_EST + US_RE

**业务2（Service_Holiday）核心配置参数**：
- 配额Quota_20GB：流量型，20,971,520 KB，会话级，监控键值=101
- 时间条件：相对时间段，周=周六+周日，00:00-24:00
- 动态规则AG_Holiday_Normal：maxbrUL/DL=100 Mbps
- Rule_Holiday_Exhaust：类型=Non-PCC（终止业务），无5G动作组
- 触发器：IPCAN_EST + US_RE + TimeRangeChange

**套餐与互斥组配置**：
- 互斥组Mutex_FUP_Holiday：类型=激活，互斥操作=替换
- 套餐Flow_Package：包含Service_FUP + Service_Holiday
- 注意：新增互斥组仅对后续签约生效，对已签约业务不生效

**开户签约MML**：
```mml
ADD PSUB: USRIDENTIFIER="46000120010****", USRMSISDN="861390010****", USRSTATE=Normal, ...;
ADD PSRVPKG: USRIDENTIFIER="46000120010****", SRVNAME="Flow_Package", ...;
```

### 3.3 多业务方案 -- E2E调测两种方法

**信令调测法**（深度验证）：
1. 在PCF/SMF/UPF三侧建立消息跟踪任务
2. 检查用户签约（LST PSRVPKG查询套餐名=Flow_Package）
3. 检查初始配额（LST PQUOTA查询配额名称和初始值是否一致）
4. 按场景（场景1/5/8）触发用户上线，逐层验证：
   - PCF侧：Npcf_SMPolicyControl_Create/Update消息中的pccRules/qosDecs/umDecs是否正确
   - SMF侧：PFCP Session Establishment Request消息是否正确转发策略
   - UPF侧：PFCP Session Report Request消息中配额消耗上报是否正确
5. 验证配额耗尽后策略更新：PCF切换规则（如AG_FUP_Normal -> AG_FUP_Exhaust），发送消息通知

**快速调测法**（效率验证）：
1. 检查系统时间（DSP TIME确认与本地时间一致）
2. 检查用户签约和配额状态
3. SMF侧：DSP PCCSESSINFO查询动态规则安装是否正确
4. SMF侧：DSP SESSIONQOSINFO查询协商QoS参数（5QI/ARP/MFBR）是否一致
5. UPF侧：DSP SESSIONINFO查询QER的MBR是否与PCF下发一致（关键：Service QER的Uplink/Downlink MBR）
6. 终端测速验证实际带宽体验

**调测关键检查点**：
- UPF侧QER ID中Service类型的QER反映业务级带宽限制（10000kbps=10Mbps / 100000kbps=100Mbps）
- APN Session类型的QER反映会话级AMBR限制（2000000kbps=2Gbps）
- URR ID中Dynamic标记表示动态规则下发，Predefined标记表示预定义规则
- volth=1（Volume Threshold开关打开）表示流量上报已启用

---

## 4. 与带宽控制的关系

### 4.1 位置区域方案 -- 纯带宽控制场景

位置区域带宽差异化方案是带宽控制最直接的典型应用：以**位置区域**为条件，以**上下行MBR**为动作，通过预定义规则在UPF侧执行速率限制。方案中不涉及计费、消息通知、时间条件等复杂逻辑，是最纯粹的"按条件差异化带宽"模型。

### 4.2 多业务方案 -- 带宽控制与多种策略的组合

多业务场景策略控制体现了带宽控制在复杂业务场景中的组合应用：

**带宽控制的多层次体现**：
- Service_FUP：配额未耗尽=10 Mbps，配额耗尽=1 Mbps（典型的FUP带宽限制）
- Service_Holiday：配额未耗尽=100 Mbps（高带宽假期提速）
- 两业务间通过"激活+替换"互斥实现带宽策略切换

**带宽控制与其他策略类型的组合**：
- **带宽 + 配额管理**：10GB/20GB流量配额驱动带宽策略切换
- **带宽 + 时间条件**：周末时段触发假期高带宽策略
- **带宽 + 消息通知**：配额耗尽时发短信通知用户带宽变化
- **带宽 + 业务互斥**：高优先级业务替换低优先级业务的带宽策略

**套餐组合的价值**：Flow_Package套餐将基本FUP业务和假期业务打包，用户只需订购一个套餐即可享受工作日10Mbps/周末100Mbps的差异化带宽体验，配额耗尽后自动降速到1Mbps，充分展示了带宽控制在套餐化运营中的灵活性。

### 4.3 预定义规则与动态规则的带宽控制差异

预定义方案中带宽由SMF/UPF本地配置的QOSPROP.MBRUPLKVALUE/MBRDNLKVALUE决定，PCF仅下发规则名。动态方案中带宽由PCF的5G动作组QoSData.maxbrUl/maxbrDl决定，通过N7接口码流直接下发完整QoS参数。两者在带宽控制的灵活性、配置复杂度和适用场景上有本质区别。

---

## 5. 关键术语

| 术语 | 简释 |
|------|------|
| PLMN | Public Land Mobile Network，公共陆地移动网络，由MCC（国家码）+MNC（网络码）组成 |
| RoamingRegion | 漫游区，UPCF中定义的位置区域对象，用于判断用户是否在本地/漫游区接入 |
| PLMN_CH | PLMN Change触发器，当用户MCC/MNC变化时触发PCF重新计算策略 |
| IPCAN_EST | IP-CAN Session Establishment触发器，用户N7接口上线时触发策略计算 |
| US_RE | Usage Report触发器，UPF上报使用量时触发PCF重新计算策略 |
| TimeRangeChange | 时间段变化触发器，时间条件（如工作日/周末）切换时触发策略更新 |
| QuotaStatus | 配额状态，取值Normal（未耗尽）或Exhaust（耗尽），驱动规则匹配 |
| DynamicPccRule | 动态PCC规则，PCF通过N7接口码流完整下发规则内容（含QoS/流描述/使用量监控） |
| Non-PCC | 非PCC规则，用于终止业务执行，不产生PCC策略下发 |
| 激活+替换 | 互斥组操作类型，高优先级业务激活时替换（去激活）已激活的低优先级业务 |
| MFBR | Maximum Flow Bit Rate，最大流比特率，即上下行最大带宽 |
| QER | QoS Enforcement Rule，UPF侧QoS执行规则，Service类型QER承载业务级MBR |
| URR | Usage Reporting Rule，使用量上报规则，UPF侧用于流量监控和配额统计 |
| 5G动作组 | UPCF中5G策略动作的集合，包含FlowDescription/FlowInformation/TrafficControlData/QoSData/UsageMonitoringData/DynamicPccRule等类型 |
| 条件组 | ConditionGroup，一个或多个条件的逻辑组合（AND/OR），用于规则匹配判断 |
| 配额分片 | Quota Slice，配额的一部分分配给当前会话，UPF基于分片阈值上报使用量 |

---

## 6. 知识来源

| 序号 | 文件名 | 来源路径前缀 |
|------|--------|-------------|
| 1 | UPF侧业务配置_22160708.md | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于位置区域的带宽差异化控制方案（预定义）/E2E业务配置/` |
| 2 | 整体方案设计_08571777.md | `.../基于位置区域的带宽差异化控制方案（预定义）/` |
| 3 | 需求描述_08571743.md | `.../基于位置区域的带宽差异化控制方案（预定义）/` |
| 4 | 信令调测方法_24058838.md | `.../基于多业务场景的策略控制（动态）/E2E业务调测/` |
| 5 | 快速调测方法_23899010.md | `.../基于多业务场景的策略控制（动态）/E2E业务调测/` |
| 6 | 业务1配置_23899008.md | `.../基于多业务场景的策略控制（动态）/E2E业务配置/` |
| 7 | 业务2配置_71231363.md | `.../基于多业务场景的策略控制（动态）/E2E业务配置/` |
| 8 | 套餐配置_24671552.md | `.../基于多业务场景的策略控制（动态）/E2E业务配置/` |
| 9 | PCF侧业务设计_24667722.md | `.../基于多业务场景的策略控制（动态）/整体方案设计/` |
| 10 | 整体拆解逻辑_71227537.md | `.../基于多业务场景的策略控制（动态）/整体方案设计/` |
