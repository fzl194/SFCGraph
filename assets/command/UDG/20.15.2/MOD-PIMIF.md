---
id: UDG@20.15.2@MMLCommand@MOD PIMIF
type: MMLCommand
name: MOD PIMIF（修改PIM接口配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: PIMIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM接口配置
status: active
---

# MOD PIMIF（修改PIM接口配置）

## 功能

该命令用于修改接口下PIM相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| SETPIMMODE | 设置PIM模式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示设置接口PIM模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NOSET：不设置PIM模式。<br>- SET：设置PIM模式。<br>默认值：无 |
| PIMSMENABLE | 接口使能PIM标志 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SETPIMMODE”配置为“SET”时为必选参数。<br>参数含义：该参数用于表示接口PIM使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DRPRIORITY | DR优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DR优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| HELLOINTERVAL | Hello报文发送间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示Hello报文发送间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～18000，单位是秒。<br>默认值：无 |
| HELLOHOLDTIME | PIM邻居维持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示PIM邻居维持时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无 |
| HELLOOVERRIDE | Hello消息中否决Prune剪枝的时间间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于表示配置Hello消息中携带的否决Prune剪枝的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是毫秒。<br>默认值：无 |
| HELLOLANDELAY | 接口的Lan-delay（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于表示接口的Lan-delay，Lan-delay表示LAN内传输消息的延迟时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32767，单位是毫秒。<br>默认值：无 |
| JPTIMERINTERVAL | JP报文发送间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示JP报文发送间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～18000，单位是秒。<br>默认值：无 |
| JPHOLDTIME | JP加入剪枝维持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示JP加入剪枝维持时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无 |
| ASSERTHOLDTIME | Assert状态的保持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示PIM接口Assert状态的保持时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为7～65535，单位是秒。<br>默认值：无 |
| SILENTENABLE | 是否使能PIM Silent | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否使能PIM Silent。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| PIMMODE | PIM模式 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SETPIMMODE”配置为“SET”时为必选参数。<br>参数含义：该参数用于表示接口PIM模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPARSE：稀疏模式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PIMIF]] · PIM接口配置（PIMIF）

## 使用实例

PIM接口修改Hello周期为10秒：

```
MOD PIMIF:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,IFNAME="Ethernet64/0/3",HELLOINTERVAL=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-PIMIF.md`
