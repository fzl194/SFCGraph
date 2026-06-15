## 第九章：Gx/PCC策略与计费

### K136: PCC规则类别与一致性要求 [配置]
> 来源: K63, K159

| 规则类别 | PCF | SMF | UPF |
|---------|-----|-----|-----|
| 动态规则 | 定义名称+内容，下发 | 传递 | 执行 |
| 预定义规则 | 定义名称（与SMF匹配） | 匹配名称，传递 | 匹配本地配置，执行 |
| 预定义规则组 | 名称与SMF UserProfile匹配 | 定义UserProfile包含多条规则 | 匹配UserProfile，按优先级执行 |
| 本地规则 | 无关联 | 定义UserProfile | 匹配并执行 |

优先级：PCF全局优先级。相同优先级时动态>预定义。

一致性要求（SMF与UPF必须匹配）：UserProfile name、Rule name、URR ID。

---

### K137: Charging-Rule-Definition AVP结构 [协议]
> 来源: K224

Charging-Rule-Definition（AVP 1003, Grouped类型）定义PCRF发送给PCEF的PCC规则：

| 子信元 | 类型 | 计费相关 |
|--------|------|----------|
| Charging-Rule-Name | 必选 | 规则唯一标识 |
| Service-Identifier | 可选 | 服务标识(SID) |
| Rating-Group | 可选 | 费率组(RG) |
| Flow-Information | 可选 | 业务流信息 |
| Reporting-Level | 可选 | 上报级别 |
| Online | 可选 | 在线计费使能 |
| Offline | 可选 | 离线计费使能 |
| Metering-Method | 可选 | 计量方式 |
| Monitoring-Key | 可选 | 配额监控键 |
| Precedence | 可选 | 优先级 |

规则：如果可选AVP被删除但之前已提供，之前的信息保留有效。Flow-Information/Flows AVP如果重新提供则替换所有之前的值。

---

### K138: Charging-Rule-Install与Charging-Rule-Remove [协议]
> 来源: K225

**Charging-Rule-Install**（AVP 1001, Grouped）：
- 功能：激活、安装或修改PCC规则（PCRF→PCEF）
- 安装新规则或修改已安装规则：使用Charging-Rule-Definition
- 激活预定义规则：使用Charging-Rule-Name或Charging-Rule-Base-Name
- GPRS场景：包含Bearer-Identifier
- 可含Rule-Activation-Time/Rule-Deactivation-Time控制生效时间

**Charging-Rule-Remove**（AVP 1002, Grouped）：
- 功能：去激活或删除PCC规则（PCRF→PCEF）
- 使用Charging-Rule-Name删除特定PCC规则
- 使用Charging-Rule-Base-Name去激活预定义规则组

---

### K139: Online AVP与Offline AVP [协议]
> 来源: K158, K226

**Online AVP**（AVP 1009, 枚举型）：
- DISABLE_ONLINE (0)：PCC规则在线计费接口禁用
- ENABLE_ONLINE (1)：PCC规则在线计费接口使能
- 在initial CCR中：指示PCEF预配置的在线计费方式是否可用
- 在initial CCA中：指示默认在线计费方式，PCRF下发的优先级高于PCEF预配置

**Offline AVP**（AVP 1008, 枚举型）：
- DISABLE_OFFLINE (0)：PCC规则离线计费接口禁用
- ENABLE_OFFLINE (1)：PCC规则离线计费接口使能
- 规则同Online AVP

**互斥规则**：offline和online不能同时为true，但可同时为false（不计费）。两者都不存在或都为false时，使用PDU会话的默认计费方法。PCF下发的优先级高于SMF本地配置。

---

### K140: Metering-Method AVP [协议]
> 来源: K227

Metering-Method AVP（AVP 1007, 枚举型）定义离线计费的计量参数：

| 取值 | 含义 |
|------|------|
| DURATION (0) | 测量持续时间 |
| VOLUME (1) | 测量流量 |
| DURATION_VOLUME (2) | 同时测量持续时间和流量 |

- PCEF在decentralized unit determination中将该AVP用于在线计费
- 删除后之前提供的信息保持有效；之前未提供则使用PCEF预配置的默认计量方法

---

### K141: Reporting-Level AVP [协议]
> 来源: K228

Reporting-Level AVP（AVP 1011, 枚举型）定义PCEF上报配额的等级：

| 取值 | 含义 | 条件 |
|------|------|------|
| SERVICE_IDENTIFIER_LEVEL (0) | 基于SID+RG联合等级 | CRD中提供Service-Identifier和Rating-Group |
| RATING_GROUP_LEVEL (1) | 基于费率组等级 | CRD中提供Rating-Group |

未携带但之前已提供，则之前的值保持有效。未携带且之前未提供，使用PCEF预配置的默认上报等级。

---

### K142: Rating-Group AVP [协议]
> 来源: K229

Rating-Group AVP（AVP 432, Unsigned32类型）：
- 包含费率组的标识
- 同一费率类型的所有业务属于同一费率组
- 请求相关的特定费率组被联合的Service-Context-Id和Rating-Group AVPs唯一标识
- 参考：RFC 4006 8.29章节

---

### K143: Event-Trigger AVP关键计费触发器 [协议]
> 来源: K233

Event-Trigger AVP（AVP 1006, 枚举型）与计费相关的关键触发器：

| 取值 | 名称 | 计费关联 |
|------|------|----------|
| 0 | SGSN_CHANGE | SGSN变更触发PCC规则更新 |
| 2 | RAT_CHANGE | RAT变更触发PCC规则更新 |
| 4 | PLMN_CHANGE | PLMN变更触发PCC规则更新 |
| 13 | USER_LOCATION_CHANGE | 用户位置变更（CGI/SAI/RAI/TAI/ECGI） |
| 14 | NO_EVENT_TRIGGERS | PCRF不需要事件触发通知 |
| 17 | REVALIDATION_TIMEOUT | 重新验证超时触发 |
| 25 | UE_TIME_ZONE_CHANGE | UE时区变更 |
| 26/27 | TAI_CHANGE | TAI变更 |
| 27/28 | ECGI_CHANGE | ECGI变更 |
| 28/29 | CHARGING_CORRELATION_EXCHANGE | 上报接入网计费标识 |
| 26/33 | USAGE_REPORT | 配额监控上报 |
| 39 | APPLICATION_START | 应用流量检测开始 |
| 40 | APPLICATION_STOP | 应用流量检测结束 |
| 45 | ACCESS_NETWORK_INFO_REPORT | 接入网络信息上报 |
| 101 | TETHERING_REPORT | Tethering检测上报 |
| 1003 | CELL_CONGESTION_CHANGE | 小区状态变更（华为私有） |

USAGE_REPORT触发器与Usage Monitoring（FUP）直接关联：PCRF下发Monitoring-Key+Granted-Service-Unit，PCEF上报Used-Service-Unit。

---

### K144: PCF下发的计费参数全集（ChargingData） [原理]
> 来源: K157

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

---

### K145: 5G动态规则必配动作组 [配置]
> 来源: K160

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

### K146: 三种规则类型对比（动态/预定义/本地） [原理]
> 来源: K16, K159

| 维度 | 动态规则 | 预定义规则 | 本地规则 |
|------|----------|------------|----------|
| 规划位置 | PCF | UPF+SMF+PCF | UPF+SMF |
| 策略决策者 | PCF | PCF | SMF |
| 流条件 | PCF配置 | UPF配置 | UPF配置 |
| 流动作 | PCF配置 | UPF配置 | UPF配置 |
| 规则名一致性 | 不需要 | PCF/SMF/UPF三侧一致 | SMF/UPF两侧一致 |
| 业务识别 | 不识别（非定向流） | UPF识别（三四层+七层） | UPF识别 |
| 计费控制 | PCF通过ChargingData下发 | UPF本地配置计费动作 | UPF本地配置 |
| 七层支持 | **不支持** | **支持** | **支持** |
| 适用场景 | 非定向流、达量限速 | 定向流（需识别特定业务） | PCF故障降级方案 |

使用场景：
- 有PCF → 动态规则+预定义规则
- 无PCF或PCF故障 → 本地规则
- 需要七层匹配 → 必须用预定义规则或本地规则

---

