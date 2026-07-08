---
id: UNC@20.15.2@MMLCommand@SET S1OVERLOAD
type: MMLCommand
name: SET S1OVERLOAD（设置S1过载控制信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: S1OVERLOAD
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1接口过载控制
status: active
---

# SET S1OVERLOAD（设置S1过载控制信息）

## 功能

**适用网元：MME**

此命令用于设置S1过载控制信息，参见 3GPP TS 36.413协议。

当MME过载时可以通过本命令配置各过载级别的控制策略，向eNodeB发送Overload Start消息，通知eNodeB拒绝UE新建连接，从而减少对网络的信令冲击。当MME从过载状态恢复到正常状态后向eNodeB发送Overload Stop消息，通知eNodeB允许UE接入，继续为UE提供服务。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。
- 过载级别有4个级别。
- 在设置过载策略时，LV1级过载策略不高于LV2级过载策略、LV3级过载策略和LV4级过载策略，LV2级过载策略不高于LV3级过载策略、LV4级过载策略，LV3级过载策略不高于LV4级过载策略。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ON(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LV1 | 一级过载控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一级过载控制策略。<br>数据来源：整网规划<br>取值范围：<br>- “NO_CONTROL(No control)”<br>- “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”<br>- “REJECT_ALL_SIGNALLING(Reject all Signalling)”<br>- “PERMIT_EMERGENCY_ONLY(Permit Emergency only)”<br>- “PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”<br>- “REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”<br>系统初始设置值：<br>“NO_CONTROL(No control)”<br>配置原则：<br>- 建议的控制策略优先级从低到高为：“REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”<“REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”<“REJECT_ALL_SIGNALLING(Reject all Signalling)”<“PERMIT_EMERGENCY_ONLY(Permit Emergency only)”或“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”，逐级增大控制程度；其中“PERMIT_EMERGENCY_ONLY(Permit Emergency only)”和“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”不区分优先级。<br>- 使用场景按照协议定义使用，具体参考3GPP.36.413。<br>说明：- “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”：拒绝RRC建立原因值为“mo-data”和“delayTolerantAccess”的业务消息。<br>- “REJECT_ALL_SIGNALLING(Reject all Signalling)”：拒绝RRC建立原因值为“mo-data”、“mo-signalling”和“delayTolerantAccess”的业务消息。<br>- “PERMIT_EMERGENCY_ONLY(Permit Emergency only)”：仅允许接入RRC建立原因值为“emergency”和“mt-Access”的业务消息。<br>- “PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”：仅允许接入RRC建立原因值为“highPriorityAccess”和“mt-Access”的业务消息。<br>- “REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”：仅拒绝RRC建立原因值为“delayTolerantAccess”的业务消息。<br>- 特性正式启用时，参数“一级过载控制策略 ”、“二级过载控制策略 ”、“三级过载控制策略 ”、“四级过载控制策略 ”中只要有一个不设置为“NO_CONTROL(No control)”，此特性才生效。 |
| LV2 | 二级过载控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定二级过载控制策略。<br>数据来源：整网规划<br>取值范围：<br>- “NO_CONTROL(No control)”<br>- “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”<br>- “REJECT_ALL_SIGNALLING(Reject all Signalling)”<br>- “PERMIT_EMERGENCY_ONLY(Permit Emergency only)”<br>- “PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”<br>- “REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”<br>系统初始设置值：<br>“NO_CONTROL(No control)”<br>配置原则：<br>- 建议的控制策略优先级从低到高为：“REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”<“REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”<“REJECT_ALL_SIGNALLING(Reject all Signalling)”<“PERMIT_EMERGENCY_ONLY(Permit Emergency only)”或“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”，逐级增大控制程度；其中“PERMIT_EMERGENCY_ONLY(Permit Emergency only)”和“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”不区分优先级。<br>- 使用场景按照协议定义使用，具体参考3GPP.36.413。<br>说明：- “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”：拒绝RRC建立原因值为“mo-data”和“delayTolerantAccess”的业务消息。<br>- “REJECT_ALL_SIGNALLING(Reject all Signalling)”：拒绝RRC建立原因值为“mo-data”、“mo-signalling”和“delayTolerantAccess”的业务消息。<br>- “PERMIT_EMERGENCY_ONLY(Permit Emergency only)”：仅允许接入RRC建立原因值为“emergency”和“mt-Access”的业务消息。<br>- “PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”：仅允许接入RRC建立原因值为“highPriorityAccess”和“mt-Access”的业务消息。<br>- “REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”：仅拒绝RRC建立原因值为“delayTolerantAccess”的业务消息。<br>- 特性正式启用时，参数“一级过载控制策略 ”、“二级过载控制策略 ”、“三级过载控制策略 ”、“四级过载控制策略 ”中只要有一个不设置为“NO_CONTROL(No control)”，此特性才生效。 |
| LV3 | 三级过载控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定三级过载控制策略。<br>数据来源：整网规划<br>取值范围：<br>- “NO_CONTROL(No control)”<br>- “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”<br>- “REJECT_ALL_SIGNALLING(Reject all Signalling)”<br>- “PERMIT_EMERGENCY_ONLY(Permit Emergency only)”<br>- “PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”<br>- “REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”<br>系统初始设置值：<br>“NO_CONTROL(No control)”<br>配置原则：<br>- 建议的控制策略优先级从低到高为：“REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”<“REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”<“REJECT_ALL_SIGNALLING(Reject all Signalling)”<“PERMIT_EMERGENCY_ONLY(Permit Emergency only)”或“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”，逐级增大控制程度；其中“PERMIT_EMERGENCY_ONLY(Permit Emergency only)”和“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”不区分优先级。<br>- 使用场景按照协议定义使用，具体参考3GPP.36.413。<br>说明：- “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”：拒绝RRC建立原因值为“mo-data”和“delayTolerantAccess”的业务消息。<br>- “REJECT_ALL_SIGNALLING(Reject all Signalling)”：拒绝RRC建立原因值为“mo-data”、“mo-signalling”和“delayTolerantAccess”的业务消息。<br>- “PERMIT_EMERGENCY_ONLY(Permit Emergency only)”：仅允许接入RRC建立原因值为“emergency”和“mt-Access”的业务消息。<br>- “PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”：仅允许接入RRC建立原因值为“highPriorityAccess”和“mt-Access”的业务消息。<br>- “REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”：仅拒绝RRC建立原因值为“delayTolerantAccess”的业务消息。<br>- 特性正式启用时，参数“一级过载控制策略 ”、“二级过载控制策略 ”、“三级过载控制策略 ”、“四级过载控制策略 ”中只要有一个不设置为“NO_CONTROL(No control)”，此特性才生效。 |
| LV4 | 四级过载控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定四级过载控制策略。<br>数据来源：整网规划<br>取值范围：<br>- “NO_CONTROL(No control)”<br>- “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”<br>- “REJECT_ALL_SIGNALLING(Reject all Signalling)”<br>- “PERMIT_EMERGENCY_ONLY(Permit Emergency only)”<br>- “PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”<br>- “REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”<br>系统初始设置值：<br>“NO_CONTROL(No control)”<br>配置原则：<br>- 建议的控制策略优先级从低到高为：“REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”<“REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”<“REJECT_ALL_SIGNALLING(Reject all Signalling)”<“PERMIT_EMERGENCY_ONLY(Permit Emergency only)”或“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”，逐级增大控制程度；其中“PERMIT_EMERGENCY_ONLY(Permit Emergency only)”和“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”不区分优先级。<br>- 使用场景按照协议定义使用，具体参考3GPP.36.413。<br>说明：- “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”：拒绝RRC建立原因值为“mo-data”和“delayTolerantAccess”的业务消息。<br>- “REJECT_ALL_SIGNALLING(Reject all Signalling)”：拒绝RRC建立原因值为“mo-data”、“mo-signalling”和“delayTolerantAccess”的业务消息。<br>- “PERMIT_EMERGENCY_ONLY(Permit Emergency only)”：仅允许接入RRC建立原因值为“emergency”和“mt-Access”的业务消息。<br>- “PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”：仅允许接入RRC建立原因值为“highPriorityAccess”和“mt-Access”的业务消息。<br>- “REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”：仅拒绝RRC建立原因值为“delayTolerantAccess”的业务消息。<br>- 特性正式启用时，参数“一级过载控制策略 ”、“二级过载控制策略 ”、“三级过载控制策略 ”、“四级过载控制策略 ”中只要有一个不设置为“NO_CONTROL(No control)”，此特性才生效。 |
| DLYTM | 等待时长（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定等待时长，向eNodeB发送过载消息的平滑定时器，即每隔固定时间向固定数量的eNodeB发送过载消息。<br>数据来源：整网规划<br>取值范围：0秒～60秒<br>系统初始设置值：30秒 |
| REJRATEIND | 拒绝比例指示 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME在Overload Start消息中是否携带"Traffic Load Reduction Indication"信元。"Traffic Load Reduction Indication"信元表示MME指示eNodeB限制指定过载控制策略下用户接入的流控百分比。如果该参数配置为<br>“YES(是)”<br>，那么首次过载时，携带拒绝比例为50%；如果连续3个5s周期过载级别不变，携带拒绝比例为99%。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：<br>“NO(否)”<br>配置原则：在系统连接的所有eNodeB都支持"Traffic Load Reduction Indication"信元时，可配置为<br>“YES(是)”<br>。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1OVERLOAD]] · S1接口过载控制（S1OVERLOAD）

## 使用实例

当MME过载时可以通过本命令配置各过载级别的控制策略，向eNodeB发送Overload Start消息，通知eNodeB拒绝UE新建连接，从而减少对网络的信令冲击。设置一级过载控制策略为NO_CONTROL(No control)，二级过载控制策略为REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)，三级过载控制策略为REJECT_ALL_SIGNALLING(Reject all Signalling)，四级过载控制策略为PERMIT_EMERGENCY_ONLY(Permit Emergency only)，等待时长为30秒，拒绝比例指示为YES(是)：

SET S1OVERLOAD: LV1=NO_CONTROL, LV2=REJECT_ALL_NON_EMERGENCY, LV3=REJECT_ALL_SIGNALLING, LV4=PERMIT_EMERGENCY_ONLY, DLYTM=30, REJRATEIND=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-S1OVERLOAD.md`
