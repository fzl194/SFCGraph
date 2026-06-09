# Batch-10 重点业务保障：新增保障业务配置、部署总览与数据分析订阅流程

---

## 1. 概述

本知识文档融合提炼自"5G Core 重点业务保障解决方案"业务专题下的10个产品文档，覆盖三大主题块：

1. **新增保障业务配置与调测**：当运营商在初始业务配置后需要新增保障应用（如云游戏）或子应用（如TikTok）时，UDG侧和UPCF侧分别需要做哪些增量配置，以及如何调测验证。
2. **部署总览对比**：典型场景（华为全套PCF/SMF）与异厂商PCF场景在网元部署、接口对接、业务配置流程上的关键差异。
3. **信令流程**：包括RAT（Radio Access Technology）切换场景下带宽保障的连续性处理，以及数据分析订阅的完整生命周期三阶段——订阅（Subscribe）、更新订阅（Update Subscribe）、去订阅（Unsubscribe）。

这些内容共同构成了"重点业务保障"从部署落地到运行期信令交互的完整知识链条，是理解带宽控制如何在端到端网元间协同执行的关键基础。

---

## 2. 核心知识点

### 2.1 新增保障业务：UDG侧配置要素

当运营商新增保障业务时，UDG侧只需要配置**新增应用的上报策略**和**应用对应的协议质差检测策略**。存在两种典型场景：

- **场景一（已有应用中增加子应用）**：例如在直播类业务类型中新增TikTok子应用。
- **场景二（新增一个全新应用）**：例如新增一个云游戏应用，该应用下配置一个游戏子应用。

两种场景的配置操作一致，核心是三步：
1. `ADD POLICYCONDITION`：配置质差检测策略参数（速率基线、大流阈值、多KPI判断逻辑）。
2. `ADD SSUPROTCOLGROUP`：配置基于协议的质差检测策略，将策略绑定到具体协议组。
3. `ADD APPPOLICYCTRL`：配置基于应用的质差上报策略，将应用与检测协议组关联。

**关键参数说明**：
- `POLICYCNDNAME`：策略参数名，本端规划，需绑定到具体协议。
- `UPLINKAVGRATE` / `DNLINKAVGRATE`：上行/下行平均速率基线（千比特/秒），取值样例260。
- `UPFLOWTHRD`：上行大流阈值（千比特/秒），取值样例15。
- `MULTIKPIJUDGE`：多KPI判断逻辑，取值`SOME_COND_NOT_MATCHED`。
- `QOEDETECTCOND`：业务流量特征检测条件，可取`UP_BIGFLOW_CHECK`（仅大流检测）或`ALL_CHECK`（全量检测）。
- `PROTOCOLNAME`：协议名称，如`tiktok_live`、`miguplay_media`。

**版本注意事项**：UDG 20.13.2.10之前的版本，`ADD POLICYCONDITION`命令中速率基线、大流阈值类参数单位为**千字节/秒**（而非千比特/秒），配置时需注意版本差异。

### 2.2 新增保障业务：UPCF侧配置要素

UPCF侧需要为新增的应用标识下发**QoS加速策略**。核心配置流程为五步：

1. **配置5G动作组**：包括TrafficControlData（流量控制）、Arp（分配保留优先级）、QoSData（QoS数据）、DynamicPccRuleIMS（动态PCC规则）、CmdN23EventSubscription（N23事件订阅）。
2. **配置规则**：将条件组与5G动作组关联，规则类型为`5G Smf Pcc Rule for IMS`。
3. **配置策略**：策略类型为`N7 Policy`，触发器为`AFSessionAuthorization`。
4. **配置业务**：业务类型为`VALUE_ADDED_SERVICE`，激活方式为`AF`，QoS模式为`替换`。
5. **配置应用业务映射**：将应用标识（如`appgroup2`）映射到对应业务。

**QoS加速核心参数**：
- `5qi=4`：建立应用媒体流专有QoS Flow。
- `priorityLevel=1`：向SMF下发的QoS优先级，数字越小优先级越高。
- `preemptCap=NOT_PREEMPT` / `preemptVuln=NOT_PREEMPTABLE`：不可抢占、不可被抢占。
- `maxbrUl/maxbrDl`：最大上下行带宽，取值来自AF会话对象属性`AfSession.MediaMaxBandwidthUL/DL`。
- `gbrUl/gbrDl`：保证上下行带宽，取值来自`AfSession.MediaMirBandwidthUL/DL`。

**N23事件订阅约束**：
- 只允许`5G Smf Pcc Rule`、`Non-PCC规则`下关联`CmdN23EventSubscription`动作。
- 同一个规则下只能关联一个`CmdN23EventSubscription`动作。
- 一个`CmdN23EventSubscription`动作仅支持配置一个event事件。
- 系统所有`CmdN23EventSubscription`动作`QOS_ANALYSIS`事件关联的`appIds`最大个数为40，所有`CmdN23EventSubscription`动作配置的`appIds`总共不能超过255个。

**对已有规则的修改**：当新增应用（如`appgroup2`）时，需要基于初始业务配置中的规则`N23_Rule02`和`N23_Rule03`，对已有规则进行修改，增加`appIds=appgroup2`属性，而非创建全新规则。

### 2.3 新增保障业务的调测要点

调测流程与初始业务配置一致，区别在于消息流程中新增了保障业务的订阅流程。调测关注点：
- 验证UDG侧质差检测策略是否生效（协议组绑定、速率基线匹配）。
- 验证UPCF侧QoS加速策略是否正确下发（5G动作组、规则匹配、应用映射）。
- 验证端到端N23订阅流程是否正常建立（PCF -> NWDAF -> SMF -> UPF）。

### 2.4 License申请：管控项与控制原则

重点业务保障解决方案涉及的License跨越多个网元，共30+个控制项：

**必选License（核心依赖）**：

| 网元 | License控制项 | 用途 |
|------|--------------|------|
| PCF (UPCF) | `LRM0PCFN23107` N23接口策略控制 | PCF与NWDAF的N23接口通信 |
| PCF (UPCF) | `LRM0PCFN5D104` N5接口数据业务策略控制 | PCF与AF的N5接口（异厂商PCF场景无需） |
| NWDAF (UDC) | `LKV8SPDUSN01` 重点业务订阅会话数 | 订阅管理功能 |
| NWDAF (UDC) | `LKV8GPDUSN01` 5G保障会话数 | 重点业务保障管理 |
| NWDAF (UDC) | `LKV8GSNUDC01` 4G保障会话数 | 4G用户保障 |
| SMF (UNC) | `LKV2USBL01` UPF选择 | 基于预定义规则选择智能UPF |
| SMF (UNC) | `LKV3W9SPCC11` PCC基本功能 | 规则判定与策略下发 |
| SMF (UNC) | `LKV2PYCTRL1` 基于实时位置策略控制 | 实时位置上报触发保障 |
| UPF (UDG) | `LKV3G5ANAR01` 重点用户质差监测和保障 | 质差判断及上报 |
| UPF (UDG) | `LKV3G5IBIC01` 智能板订阅和采集 | 智能板基础功能 |
| UPF (UDG) | `LKV3G5TDIR01` TCP/UDP传输分析上报 | 传输层分析 |
| UPF (UDG) | `LKV3G5IARG01` 智能分析记录生成 | 分析记录生成 |
| UPF (UDG) | `LKV3G5FSFR01` 业务全样分析上报 | 全样分析 |
| UPF (UDG) | `LKV3G5SARS01` 业务分析上报订阅 | 订阅功能 |
| UPF (UDG) | `LKV3G5RSLR01` 用户实时位置分析上报 | 位置分析 |
| UDN (CloudUDN) | `LKVAICLP01` 无线小区负载智能预测 | 负载预测 |
| UDN (CloudUDN) | `LKVCELLC01` 无线小区日志信息采集 | 负载预测依赖 |

**可选License**：
- `LKV8CNSUDC01` 跨NWDAF服务区域订阅会话数（仅中国区，跨省漫游能力）。
- `LKV8NFIRAPD01` NF间接路由及代理发现（受限提供）。
- `LKV8EIEEUDC01` 体验信息能力开放。
- `LKV8IBRIUDC01` 智能码率识别（聚类算法，直播档位识别）。
- `LKVAICODE01` 智能码率识别可视。
- `LKV3G5EXPR01` 体验信息采集。

### 2.5 典型场景 vs 异厂商PCF场景部署总览

两种场景在网元部署和配置流程上存在显著差异：

| 维度 | 典型场景 | 异厂商PCF场景 |
|------|---------|-------------|
| **NWDAF (UDC)** | 新建，逻辑分省 | 新建或升级到配套版本 |
| **UPF** | 新建/智能改造（仅ARM平台UPF支持），需具备智能板 | 新建或升级，需具备智能板 |
| **PCF** | 升级到配套版本（使用现网PCF） | **新建一对智能PCF**（独立于现网异厂商PCF） |
| **SMF** | 升级到配套版本 | 新建或升级到配套版本 |
| **NRF** | 升级到配套版本 | 无特别说明 |
| **第三方设备** | 无 | 可选，支持SFTP/FTP协议 |
| **N5接口** | 必选（PCF依赖N5和N23） | **无需配置N5**（智能PCF不与AF直连） |
| **N7接口** | 无特别说明 | 必选（智能PCF与SMF之间新增N7） |
| **接口配置总览** | 必选 | 无此章节（分别在各网元配置） |
| **全局数据规划** | 典型场景全局业务数据规划 | 异厂商场景全局业务数据规划 |
| **UNC侧初始配置** | 实时位置上报 | AMF/MME选择SMF + 基于预定义规则选择智能UPF + 选择智能PCF |
| **UDG侧接口** | UDG新增服务化接口 | 配置Nupf接口数据（必须先完成SSU和SBIM服务安装） |
| **CloudUDN** | 必选 | 可选（局点部署UDN时配置） |
| **端到端调测** | 调测初始业务配置 | 调测应用GBR保障功能 |

**关键差异解读**：
- 典型场景使用现网华为PCF升级，PCF同时处理N5（与AF）和N23（与NWDAF）接口。
- 异厂商PCF场景需要新建独立的智能PCF，智能PCF只处理N23（与NWDAF）和N7（与SMF），不直接与AF通信，因此无需N5接口。
- 异厂商场景中，SMF需要额外配置AMF/MME选择SMF规则、基于预定义规则选择智能UPF、以及选择智能PCF，这些在典型场景中由PCF统一处理。

### 2.6 RAT切换场景的业务流程（4G/5G互操作）

RAT（Radio Access Technology）切换场景由**PCF感知用户网络制式变化**，判断是否支持保障，并通知NWDAF进行订阅变更。

**不支持4G保障的场景**（`SET NWDAFCTRL` "是否支持4G场景下质差保障及体验上报"为"不使能"）：
- NWDAF不支持2G和3G用户的保障。
- 4G是否支持由`SET NWDAFCTRL`命令控制。

**支持保障切换到不支持保障**（如5G切换到2G/3G/4G）：
1. PCF感知网络类型变化，向NWDAF发起N23订阅更新，`status=SUSPEND`（暂停订阅）。
2. NWDAF收到暂停指示，如果存在N5保障，向PCF发起保障取消流程。
3. NWDAF保留本地N23会话，向SMF发起事件去订阅。暂停期间仍正常处理PCF的周期性更新和取消订阅。
4. 当用户切换回支持保障的网络时，PCF向NWDAF发起`status=NORMAL`（恢复订阅）。
5. NWDAF向SMF重新发起事件订阅，SMF向UPF转发。

**支持4G保障的场景**（`SET NWDAFCTRL`为"使能"）：
- 4G/5G切换时，UPF的QOS_ANA/QOS_EXP事件不变，正常上报制式和小区信息给NWDAF。
- NWDAF按用户位置变更场景处理：判断新小区是否满足保障条件，满足则触发/继续保障，不满足则不触发/停止保障。
- SMF+PGW-C在互操作中通知PCF和UPF制式变更及小区变更，互操作结束后发起实时位置订阅。

**首次接入特殊处理**：用户首次从不支持保障的网络接入时，PCF不向NWDAF下发N23订阅，但向SMF下发RAT变化Trigger。后续切换到支持保障的网络时，SMF通知PCF，PCF发现无N23订阅，根据初始TA发现NWDAF并下发订阅。

### 2.7 数据分析订阅生命周期：三阶段

#### 2.7.1 订阅（Subscribe）

**触发条件**（满足任一）：
- 用户签约重点业务保障套餐。
- PCF发现当前NWDAF故障后向Pool内其他可用NWDAF下发订阅。
- 因异常情况NWDAF删除本地订阅，PCF更新订阅收到404后重新下发。

**PCF下发订阅的必要条件**（同时满足）：
- 用户签约了重点业务保障套餐。
- 用户激活在智能UPF上。

**信令流程**（7步）：
1. PCF通过NRF/SCP寻址NWDAF，携带初始TAI和eventId（QOS_ANALYSIS）。
2. PCF发送`Nnwdaf_EventsSubscription_Subscribe_Request`（N23接口POST），携带信元：PCF ID、notificationURI、smfId、supis、pduSeId、appIds、ipDomain、ueIpv4/ueIpv6、event。
3. NWDAF回复`Nnwdaf_EventsSubscription_Subscribe_Response`（201 Created），返回subscriptionId。
   - 若当前已有QOS_ANALYSIS订阅，NWDAF先取消旧订阅再处理新订阅。
4. NWDAF通过NRF寻址SMF，发送`Nsmf_EventExposure_Subscribe_Request`（Nsmf接口POST），携带：notifId、notifUri、appIds、event(QOS_ANA)、nupfeeUri、pduSeid、supi。
5. SMF将订阅参数转化为N4接口消息，通过`PFCP_Session_Modification_Request`发送给UPF，携带Create SRR信元（SRR ID、QoS Analysis Information含Appid、Direct Reporting Information含Event Notification URL和Notification Correlation ID）。
6. UPF安装SRR成功后回复`PFCP_Session_Modification_Response`，启动业务质量监控。
   - SRR安装失败不影响其他业务，UPF仍返回成功响应但携带失败的SRR ID。
7. SMF向NWDAF返回`Nsmf_EventExposure_Subscribe_Response`（201 Created），创建订阅URI。

#### 2.7.2 更新订阅（Update Subscribe）

**触发条件**：
- PCF周期性发起（重置N23老化定时器）。
- 用户套餐变更导致appIds变更。
- RAT切换（status在NORMAL和SUSPEND之间切换）。

**信令流程**（6步）：
1. PCF发送`Nnwdaf_EventsSubscription_Subscribe_Request`（N23接口PUT），携带更新后的信元。
2. NWDAF重置N23老化定时器（通过`SET QOSGUARTIMER`命令设置），回复响应。
   - 若NWDAF返回404（订阅不存在），PCF改为重新下发订阅。
3. 若appId已删除且已触发保障，NWDAF向PCF发送删除/更新请求撤销该appId保障。
4. 若appIds改变，NWDAF通知SMF更新订阅（Nsmf PUT操作）；appIds未变则不通知SMF。
5. SMF通过`PFCP_Session_Modification_Request`通知UPF更新订阅。
6. SMF收到UPF响应后向NWDAF回复。
   - 若NWDAF未收到SMF响应或收到失败响应，发起取消订阅并通知PCF释放专载。

#### 2.7.3 去订阅（Unsubscribe）

**触发条件**：
- 用户会话释放。
- 套餐取消。
- 更新订阅失败后的补偿操作。

**信令流程**（6步）：
1. PCF发送`Nnwdaf_EventsSubscription_Unsubscribe_Request`（N23接口DELETE）。
2. NWDAF返回成功。
3. 若已建立专载，NWDAF通过`Npcf_PolicyAuthorization_Delete_Request`通知PCF释放专载。
   - 未收到PCF响应或失败响应当做删除成功处理。
4. NWDAF发送`Nsmf_EventExposure_Unsubscribe_Request`（Nsmf接口DELETE）向SMF去订阅。
5. SMF通过`PFCP_Session_Modification_Request`通知UPF取消数据采集和上报。
6. UPF取消订阅并回复，SMF向NWDAF回复`Nsmf_EventExposure_Unsubscribe_Response`。
   - NWDAF未收到响应或收到失败响应，当做UPF侧订阅已取消。

---

## 3. 配置调测要点

### 3.1 UDG侧MML命令序列（新增保障业务）

```
// 步骤1：配置质差检测策略
ADD POLICYCONDITION: POLICYCNDNAME="policytestname1",
    UPLINKAVGRATE=260, DNLINKAVGRATE=260,
    UPFLOWTHRD=15, MULTIKPIJUDGE=SOME_COND_NOT_MATCHED;

// 步骤2：配置协议组并绑定质差策略
ADD SSUPROTCOLGROUP: DEFPRTGRPNAME="live_video2",
    PROTOCOLNAME="tiktok_live",
    POLICYCNDNAME="policytestname1",
    QOEDETECTCOND=UP_BIGFLOW_CHECK;

// 步骤3：配置应用质差上报策略
ADD APPPOLICYCTRL: APPIDNAME="appgroup1",
    SUBAPPIDNAME="add_app1",
    DEFPRTGRPNAME="live_video2";
```

### 3.2 UPCF侧MML命令序列（新增保障业务）

```
// 创建5G动作组
ADD NGACTION:ACTIONNAME="TCData_AG02",TYPE="TrafficControlData";
ADD NGACTION:ACTIONNAME="Arp_AG02",TYPE="Arp";
ADD NGACTION:ACTIONNAME="QoSData_AG02",TYPE="QoSData";
ADD NGACTION:ACTIONNAME="DynamicPccRule_AG02",TYPE="DynamicPccRuleIMS";

// 配置动作组属性
ADD NGACTIONATTR:ACTIONNAME="TCData_AG02",ATTRNAME="tcId",TYPE=Value,VALUE="N5_tcId2";
ADD NGACTIONATTR:ACTIONNAME="TCData_AG02",ATTRNAME="flowStatus",TYPE=Object Attribute,VALUE="AfSession.FlowStatus";
ADD NGACTIONATTR:ACTIONNAME="Arp_AG02",ATTRNAME="priorityLevel",TYPE=Value,VALUE="1";
ADD NGACTIONATTR:ACTIONNAME="Arp_AG02",ATTRNAME="preemptCap",TYPE=Value,VALUE="NOT_PREEMPT";
ADD NGACTIONATTR:ACTIONNAME="Arp_AG02",ATTRNAME="preemptVuln",TYPE=Value,VALUE="NOT_PREEMPTABLE";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG02",ATTRNAME="qosId",TYPE=Value,VALUE="N5_Qos02";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG02",ATTRNAME="5qi",TYPE=Value,VALUE="4";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG02",ATTRNAME="arp",TYPE=Reference ActionGroup,VALUE="Arp_AG02";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG02",ATTRNAME="gbrDl",TYPE=Object Attribute,VALUE="AfSession.MediaMirBandwidthDL";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG02",ATTRNAME="gbrUl",TYPE=Object Attribute,VALUE="AfSession.MediaMirBandwidthUL";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG02",ATTRNAME="maxbrDl",TYPE=Object Attribute,VALUE="AfSession.MediaMaxBandwidthDL";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG02",ATTRNAME="maxbrUl",TYPE=Object Attribute,VALUE="AfSession.MediaMaxBandwidthUL";
ADD NGACTIONATTR:ACTIONNAME="DynamicPccRule_AG02",ATTRNAME="refTcData",TYPE=Reference ActionGroup,VALUE="TCData_AG02";
ADD NGACTIONATTR:ACTIONNAME="DynamicPccRule_AG02",ATTRNAME="refQosData",TYPE=Reference ActionGroup,VALUE="QoSData_AG02";
ADD NGACTIONATTR:ACTIONNAME="DynamicPccRule_AG02",ATTRNAME="pccRuleId",TYPE=Value,VALUE="N5_Pcc02";

// 修改已有N23订阅动作，增加新appId
ADD NGACTIONATTR:ACTIONNAME="CmdN23Event_AG01",ATTRNAME="appIds",TYPE=Value,VALUE="appgroup2";
ADD NGACTIONATTR:ACTIONNAME="CmdN23Event_AG02",ATTRNAME="appIds",TYPE=Value,VALUE="appgroup2";

// 配置规则
ADD RULE:RULENAME="AFQos_Rule02",OPERATION=Change Rule,
    TYPE=Smf Pcc Rule for IMS 5G,PRECEDENCE=0,
    CHARGINGINDICATOR=DISABLE,EDR=OFF,RELATION=AND;
ADD RULECONDITIONGROUP:RULENAME="AFQos_Rule02",CONDITIONGROUPNAME="AfSessionMediaType_CG01";
ADD RULENGACTION:RULENAME="AFQos_Rule02",ACTIONNAME="DynamicPccRule_AG02";

// 配置策略
ADD POLICY:POLICYNAME="AFQos_Policy02",TYPE=N7 Policy;
ADD POLICYRULE:POLICYNAME="AFQos_Policy02",RULENAME="AFQos_Rule02";
ADD POLICYTRIGGER:POLICYNAME="AFQos_Policy02",TRIGGERNAME="AFSessionAuthorization";

// 配置业务
ADD SERVICE:SERVICENAME="AFQos_Service02",SERVICETYPE=VALUE_ADDED_SERVICE,
    ACTIVATEDBY=AF,PRECEDENCE=0,QOSMODE=Replace,
    SUBSCRIPTIONFORCED=No,...;
ADD SERVICEPOLICY:SERVICENAME="AFQos_Service02",POLICYNAME="AFQos_Policy02";

// 配置应用业务映射
ADD APPLICATIONSERVICEMAPPING:APPID="appgroup2",SERVICENAME="AFQos_Service02";
```

### 3.3 关键检查点

| 检查项 | 验证方法 | 预期结果 |
|--------|---------|---------|
| UDG质差检测生效 | 查看协议组绑定和策略参数 | 协议组正确绑定POLICYCNDNAME |
| UPCF动作组完整性 | 检查动作组属性引用链 | QoSData引用Arp，DynamicPccRule引用QoSData和TCData |
| N23订阅建立 | 查看N23接口话务统计 | 订阅创建请求次数与成功次数匹配 |
| N23老化定时器 | 检查`SET QOSGUARTIMER`配置 | 定时器值大于PCF周期性更新间隔 |
| RAT切换行为 | 查看`SET NWDAFCTRL`配置 | 确认4G保障是否使能 |
| SRR安装状态 | 查看PFCP响应 | 无Failed Rule ID或Offending IE |
| License加载 | 检查各网元License状态 | 必选License全部加载 |

### 3.4 关键错误码速查

| 错误码 | 接口 | 含义 | 处理建议 |
|--------|------|------|---------|
| 400 | N23/Nsmf | 信元异常（缺失/错误） | 检查PCF/NWDAF携带的信元完整性 |
| 404 | N23/Nsmf | 订阅任务不存在 | PCF需重新下发订阅而非更新 |
| 500 | N23 | License不支持 | 检查NWDAF的License是否加载 |
| 500 | Nsmf | SMF配置未开启/超最大值/UPF不支持 | 检查SMF配置和UPF能力 |
| 504 | N23/Nsmf | 内部服务不可用/超时 | 检查网元状态和连通性 |

---

## 4. 与带宽控制的关系

本批文档描述的"重点业务保障"是带宽控制在应用层面的**端到端落地机制**：

1. **UDG侧质差检测是带宽问题的发现层**：通过`ADD POLICYCONDITION`配置速率基线和大流阈值，UPF实时监控业务流量质量，当检测到质差（速率低于基线）时触发上报，驱动后续保障动作。

2. **UPCF侧QoS加速策略是带宽控制的执行层**：通过5G动作组下发`5qi=4`（保证比特率QoS Flow）、`maxbrUl/maxbrDl`（最大带宽）、`gbrUl/gbrDl`（保证带宽），直接控制用户面的带宽分配。AF通过N5接口携带`MediaMaxBandwidth`和`MediaMirBandwidth`参数，将应用层的带宽需求映射为网络层的QoS参数。

3. **数据分析订阅三阶段是带宽保障的控制信令**：订阅建立触发UPF开始监控，更新订阅维持监控连续性（含RAT切换时的暂停/恢复），去订阅终止监控。整个生命周期确保带宽保障仅在需要的时段和用户上生效。

4. **RAT切换涉及跨制式带宽保障连续性**：当用户从5G切换到4G时，如果4G保障使能，NWDAF继续分析并判断新小区是否满足保障条件；如果4G保障不使能，PCF发送`status=SUSPEND`暂停订阅，NWDAF取消SMF侧订阅但保留N23会话，等待用户切回5G后恢复。这种机制确保跨制式切换时带宽保障不会因网络类型变化而异常中断或残留。

5. **License控制直接决定带宽保障能力上限**：`5G保障会话数`、`4G保障会话数`、`重点业务订阅会话数`等License项以会话数为计量单位，直接限制了系统能同时保障的带宽控制实例数量。

---

## 5. 关键术语

| 术语 | 全称/含义 |
|------|----------|
| **RAT** | Radio Access Technology，无线接入技术（如5G NR、4G EUTRA、2G GERA） |
| **NWDAF** | Network Data Analytics Function，网络数据分析功能（UDC产品为其FE） |
| **UDC** | 统一数据分析中心，NWDAF-FE的产品形态 |
| **UDN** | 统一数据分析节点，NWDAF-BE的产品形态（CloudUDN） |
| **UPCF** | 统一策略控制功能，PCF的产品形态 |
| **N23接口** | PCF与NWDAF之间的接口，用于数据分析订阅 |
| **N5接口** | AF与PCF之间的接口，用于应用会话授权和带宽请求 |
| **N7接口** | SMF与PCF之间的接口，用于会话策略控制 |
| **Nsmf接口** | NWDAF与SMF之间的接口，用于事件订阅转发 |
| **Nupf接口** | UPF与NWDAF之间的服务化接口，用于直接事件上报 |
| **QOS_ANALYSIS** | N23接口上的事件类型名称（PCF向NWDAF订阅时使用） |
| **QOS_ANA** | Nsmf接口上的事件类型名称（NWDAF向SMF订阅时使用），与QOS_ANALYSIS为同一事件 |
| **SRR** | Session Reporting Rule，会话上报规则（N4接口私有信元） |
| **SUSPEND/NORMAL** | N23订阅状态：暂停/正常，用于RAT切换时的订阅控制 |
| **AFSessionAuthorization** | AF会话授权触发器，当AF请求业务高带宽时触发UPCF策略 |
| **5qi=4** | 5G QoS标识符4，对应Non-GBR QoS Flow（延迟敏感型，如视频流媒体） |
| **License控制项** | 产品功能授权项，通过License文件控制功能开关和容量规格 |
| **智能PCF** | 异厂商PCF场景中新建的独立华为PCF，专门用于重点业务保障 |
| **智能UPF** | 具备智能板的UPF，支持业务质量分析和质差检测 |
| **VVIP** | 智能板上的业务测量组件，处理上报NWDAF的流消息和用户消息 |

---

## 6. 知识来源

| 序号 | 文件名 | 主题 |
|------|--------|------|
| 1 | `UDG侧配置_17506332.md` | 新增保障业务UDG侧配置（质差检测+上报策略） |
| 2 | `UPCF侧配置_36370353.md` | 新增保障业务UPCF侧配置（QoS加速策略+应用映射） |
| 3 | `调测新增保障业务配置_80595846.md` | 新增保障业务调测（引用初始配置调测流程） |
| 4 | `申请License_76978890.md` | License控制项清单（30+项，跨5网元） |
| 5 | `典型场景部署总览_24818349.md` | 典型场景部署总览（华为全套网元） |
| 6 | `异厂商PCF场景部署总览_72646164.md` | 异厂商PCF场景部署总览（新建智能PCF） |
| 7 | `RAT切换场景的业务流程_83026385.md` | RAT切换流程（4G/5G互操作带宽保障连续性） |
| 8 | `典型场景数据分析去订阅_24818321.md` | 数据分析去订阅流程（DELETE操作） |
| 9 | `典型场景数据分析更新订阅_76978878.md` | 数据分析更新订阅流程（PUT操作） |
| 10 | `典型场景数据分析订阅_24938205.md` | 数据分析订阅流程（POST操作） |
