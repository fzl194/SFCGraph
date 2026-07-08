---
id: UNC@20.15.2@MMLCommand@SET CDRTRIGGER
type: MMLCommand
name: SET CDRTRIGGER（配置离线计费话单产生开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CDRTRIGGER
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费基础参数
- 离线计费模板
status: active
---

# SET CDRTRIGGER（配置离线计费话单产生开关）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来配置离线计费话单产生开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 只有ADD OFCTemplate后才能配置该命令。
- 优先级的默认值255表示该开关采用默认优先级。默认优先级由高到低顺序为计费条件改变、Serving Node更新、MS时区更新、CDR RAT更新、Serving Node PLMN标识更新，用户配置优先级的开关比使用默认优先级的开关优先级高，未配置优先级的开关保持默认优先级顺序。
- 用户配置的更新优先级值越小，优先级越高。
- 用户配置的优先级不能相同。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CDRTRIGRATCHNG | CDRTRIGRATPRIOR | CDRTRIGSNCHNG | CDRTRIGSNPRIOR | CDRTRIGTIMEZONE | CDRTRIGMAXCHNG | CDRTRIMAXCHGPRI | CDRTRIGTZPRIOR | CDRTRIGPLMNCHNG | CDRTRIGPLMNPRIO | CDRTRIGMOEXC | CDRTRIGMOEXCPRI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | ENABLE | 255 | ENABLE | 255 | ENABLE | ENABLE | 255 | 255 | ENABLE | 255 | ENABLE | 255 |

- 该命令设定后的数据，需要通过LST OFCTEMPLATE命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTEMPLATENAME | 离线计费模板名 | 可选必选说明：必选参数<br>参数含义：配置离线模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD OFCTEMPLATE命令配置生成。 |
| CDRTRIGRATCHNG | CDR RAT更新 | 可选必选说明：可选参数<br>参数含义：这是个开关参数，表示发生RAT更新时是否产生话单。该Trigger开始支持的话单版本为r6v660gcdr。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CDRTRIGRATPRIOR | RAT更新优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRTRIGRATCHNG”配置为“ENABLE”时为可选参数。<br>参数含义：RAT更新优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| CDRTRIGSNCHNG | Serving Node更新 | 可选必选说明：可选参数<br>参数含义：这是个开关参数，表示发生SGSN/SGW更新时是否触发产生话单。该Trigger开始支持的话单版本为r98cmccv130。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CDRTRIGSNPRIOR | Serving Node更新优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRTRIGSNCHNG”配置为“ENABLE”时为可选参数。<br>参数含义：Serving Node更新优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| CDRTRIGTIMEZONE | MS时区更新 | 可选必选说明：可选参数<br>参数含义：这是个开关参数，表示发MS time zone更新时是否触发产生话单。该Trigger开始支持的话单版本为r6v660gcdr。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CDRTRIGMAXCHNG | 计费条件改变 | 可选必选说明：可选参数<br>参数含义：这是个开关参数，表示计费条件改变次数达到配置的最大次数时是否触发产生话单。计费条件指的是触发产生容器的条件，包括QoS、ULI、RAI改变。该Trigger开始支持的话单版本为r98cmccv130。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- 如果配置为ENABLE，根据SET OFCTHRESHOLD的CONDITIONCHANGE参数配置的计费条件改变次数产生话单。<br>- 如果配置为DISABLE，则计费条件改变10次后产生话单。 |
| CDRTRIMAXCHGPRI | 计费条件改变优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRTRIGMAXCHNG”配置为“ENABLE”时为可选参数。<br>参数含义：计费条件改变优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| CDRTRIGTZPRIOR | MS时区优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRTRIGTIMEZONE”配置为“ENABLE”时为可选参数。<br>参数含义：MS时区更新优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| CDRTRIGPLMNCHNG | Serving Node PLMN标识更新 | 可选必选说明：可选参数<br>参数含义：这是个开关参数，表示SGSN/SGW PLMN标识改变时是否触发产生话单。该Trigger开始支持的话单版本为r99v3a0。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CDRTRIGPLMNPRIO | Serving Node PLMN标识优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRTRIGPLMNCHNG”配置为“ENABLE”时为可选参数。<br>参数含义：Serving Node PLMN标识更新优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| CDRTRIGMOEXC | CDR MO Exception Data Counter更新 | 可选必选说明：可选参数<br>参数含义：该参数用于指示发生MO Exception Data Counter更新时是否产生话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CDRTRIGMOEXCPRI | MO Exception Data Counter更新优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRTRIGMOEXC”配置为“ENABLE”时为可选参数。<br>参数含义：MO Exception Data Counter更新优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [离线计费话单产生开关（CDRTRIGGER）](configobject/UNC/20.15.2/CDRTRIGGER.md)

## 使用实例

设置名称为“ofc_test”的离线模板的话单产生开关，CDRTrigSNChng为“ENABLE”，CDRTrigRATPrior为22，CDRTrigMaxChng为“ENABLE”，CDRTriMaxChgPri为18，其他参数都设为默认值：

```
SET CDRTRIGGER:OFCTEMPLATENAME="ofc_test",CDRTRIGRATCHNG=ENABLE,CDRTRIGRATPRIOR=22,CDRTRIGMAXCHNG=ENABLE,CDRTRIMAXCHGPRI=18;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/配置离线计费话单产生开关（SET-CDRTRIGGER）_09896911.md`
