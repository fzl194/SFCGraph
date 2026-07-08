---
id: UDG@20.15.2@MMLCommand@ADD SQOSCAR
type: MMLCommand
name: ADD SQOSCAR（增加流行为CAR配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SQOSCAR
command_category: 配置类
effect_mode: ''
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流行为CAR
status: active
---

# ADD SQOSCAR（增加流行为CAR配置）

## 功能

该命令用来增加流行为CAR配置。

该命令配置的重标记报文服务等级和颜色对简单流分类映射有效QoS调度只使用服务等级不关心颜色。

## 注意事项

- 该命令最大记录数为65535。
- 需要使用ADD MQCBEHAVIOR命令先配置流行为。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 流行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流行为名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| CIR | 承诺信息速率（kbps） | 可选必选说明：必选参数<br>参数含义：该参数用于指定承诺的信息速率。 流量参数表示正常情况下允许发送的信息速率。即向漏桶发送令牌的速率，单位为kbit/s。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PIR | 峰值速率（kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定峰值速率。 流量参数表示峰值流量速率，单位为kbit/s。该参数值应大于或等于CIR。不配置时为单筒模式。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：0 |
| CBS | 承诺突发尺寸（bytes） | 可选必选说明：可选参数<br>参数含义：该参数用于指定承诺突发尺寸，在双速三色标记（RFC2968）方式下，流量控制通过令牌桶C、P实现。此参数用于描述令牌桶C的容量，即在按CIR转发数据时允许转发的最大突发IP包尺寸。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：该参数必须大于0，建议大于或等于可能转发的最大IP包长度。如果不设置该参数，CBS的取值通过CIR*187计算得出。 |
| PBS | 超出突发尺寸（bytes） | 可选必选说明：可选参数<br>参数含义：该参数用于指定超出突发尺寸，在双速三色标记（RFC2698）方式下，流量控制通过令牌桶C、P实现。此参数用于描述令牌桶P的容量，即在按PIR转发数据时允许转发的最大突发IP包尺寸。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：0<br>配置原则：该参数必须大于0，建议大于或等于可能转发的最大IP包长度。缺省情况下，PBS的取值通过PIR*187计算得出。 |
| GREENACTION | 绿色报文的动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定绿色报文的动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- pass：报文通过。<br>- discard：报文丢弃。<br>- remark：报文重标记服务等级和颜色。<br>- null：无效的动作类型。<br>默认值：pass |
| GREENSERVICECLASS | 绿色报文的服务等级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GREENACTION”配置为“remark”时为必选参数。<br>参数含义：该参数用于指定绿色报文的服务等级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- be：尽力而为。<br>- af1：确保转发等级1。<br>- af2：确保转发等级2。<br>- af3：确保转发等级3。<br>- af4：确保转发等级4。<br>- ef：加速转发。<br>- cs6：类选择码6。<br>- cs7：类选择码7。<br>- null：无效的服务等级。<br>默认值：无 |
| GREENSERVICECOLOR | 绿色报文的重标记颜色 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GREENACTION”配置为“remark”时为必选参数。<br>参数含义：该参数用于指定绿色报文的重标记颜色。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- green：报文颜色，绿色报文的丢弃优先级最低。<br>- yellow：报文颜色，黄色报文的丢弃优先级介于绿色红色之间。<br>- red：报文颜色，红色报文的丢弃优先级最高。<br>- null：无效的颜色类型。<br>默认值：无 |
| YELLOWACTION | 黄色报文的动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定黄色报文的动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- pass：报文通过。<br>- discard：报文丢弃。<br>- remark：报文重标记服务等级和颜色。<br>- null：无效的动作类型。<br>默认值：pass |
| YELLOWSERVICECLASS | 黄色报文的服务等级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“YELLOWACTION”配置为“remark”时为必选参数。<br>参数含义：该参数用于指定黄色报文的服务等级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- be：尽力而为。<br>- af1：确保转发等级1。<br>- af2：确保转发等级2。<br>- af3：确保转发等级3。<br>- af4：确保转发等级4。<br>- ef：加速转发。<br>- cs6：类选择码6。<br>- cs7：类选择码7。<br>- null：无效的服务等级。<br>默认值：无 |
| YELLOWSERVICECOLOR | 黄色报文的重标记颜色 | 可选必选说明：条件必选参数<br>前提条件：该参数在“YELLOWACTION”配置为“remark”时为必选参数。<br>参数含义：该参数用于指定黄色报文的重标记颜色。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- green：报文颜色，绿色报文的丢弃优先级最低。<br>- yellow：报文颜色，黄色报文的丢弃优先级介于绿色红色之间。<br>- red：报文颜色，红色报文的丢弃优先级最高。<br>- null：无效的颜色类型。<br>默认值：无 |
| REDACTION | 红色报文的动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定红色报文的动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- pass：报文通过。<br>- discard：报文丢弃。<br>- remark：报文重标记服务等级和颜色。<br>- null：无效的动作类型。<br>默认值：discard |
| REDSERVICECLASS | 红色报文的服务等级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REDACTION”配置为“remark”时为必选参数。<br>参数含义：该参数用于指定红色报文的服务等级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- be：尽力而为。<br>- af1：确保转发等级1。<br>- af2：确保转发等级2。<br>- af3：确保转发等级3。<br>- af4：确保转发等级4。<br>- ef：加速转发。<br>- cs6：类选择码6。<br>- cs7：类选择码7。<br>- null：无效的服务等级。<br>默认值：无 |
| REDSERVICECOLOR | 红色报文的重标记颜色 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REDACTION”配置为“remark”时为必选参数。<br>参数含义：该参数用于指定红色报文的重标记颜色。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- green：报文颜色，绿色报文的丢弃优先级最低。<br>- yellow：报文颜色，黄色报文的丢弃优先级介于绿色红色之间。<br>- red：报文颜色，红色报文的丢弃优先级最高。<br>- null：无效的颜色类型。<br>默认值：无 |
| COLORAWARE | 色敏模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定色敏模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- blind：色盲。<br>- keen：色敏。<br>默认值：blind |

## 操作的配置对象

- [流行为CAR配置（SQOSCAR）](configobject/UDG/20.15.2/SQOSCAR.md)

## 使用实例

增加流行为的CAR配置：

```
ADD SQOSCAR:BEHAVIORNAME="b1",CIR=10,PIR=20,CBS=30,PBS=40,GREENACTION=remark,GREENSERVICECLASS=af1,GREENSERVICECOLOR=green,YELLOWACTION=remark,YELLOWSERVICECLASS=be,YELLOWSERVICECOLOR=green,REDACTION=remark,REDSERVICECLASS=af1,REDSERVICECOLOR=green;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加流行为CAR配置（ADD-SQOSCAR）_50280710.md`
