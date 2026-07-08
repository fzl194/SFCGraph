---
id: UDG@20.15.2@MMLCommand@MOD PIMSITE
type: MMLCommand
name: MOD PIMSITE（修改PIM全局配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: PIMSITE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM全局参数
status: active
---

# MOD PIMSITE（修改PIM全局配置）

## 功能

该命令用于修改全局PIM相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| ASSERTHOLDTIME | Assert保持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示所有PIM接口保持Assert状态的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为7～65535，单位是秒。<br>默认值：无 |
| JPHOLDTIME | JP加入剪枝维持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示JP加入剪枝维持时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无 |
| HELLOLANDELAY | 接口的Lan-delay（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于表示接口的Lan-delay，Lan-delay表示LAN内传输消息的延迟时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32767，单位是毫秒。<br>默认值：无 |
| HELLOHOLDTIME | PIM邻居维持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示PIM邻居维持时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无 |
| DRPRIORITY | DR优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DR优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SOURCELIFETIME | （S，G）表项生存时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示（S，G）表项的生存时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～65535，单位是秒。<br>默认值：无 |
| SSMPLYNAME | SSM策略号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SSM策略号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| HELLOINTERVAL | Hello报文发送间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示Hello报文发送间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～18000，单位是秒。<br>默认值：无 |
| JPTIMERINTERVAL | JP报文发送间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示JP报文发送间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～18000，单位是秒。<br>默认值：无 |
| HELLOOVERRIDE | 配置Hello消息中携带的否决Prune剪枝的时间间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于表示配置Hello消息中携带的否决Prune剪枝的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是毫秒。<br>默认值：无 |
| BIDIRENABLE | 使能双向PIM | 可选必选说明：可选参数<br>参数含义：该参数用于表示使能双向PIM的标志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PIMSITE]] · PIM全局配置（PIMSITE）

## 使用实例

PIM全局修改Assert保持时间为65535秒，JP加入剪枝维持时间为1秒，接口的Lan-delay为1毫秒，PIM邻居维持时间为65531秒，DR优先级为1秒，表项生存时间为65535秒，SSM策略号为2000，Hello报文发送间隔为1秒，JP报文发送间隔为18000秒，Hello消息中携带的否决Prune剪枝的时间间隔为2500毫秒：

```
MOD PIMSITE: VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,ASSERTHOLDTIME=65535,JPHOLDTIME=1,HELLOLANDELAY=1,HELLOHOLDTIME=65531,DRPRIORITY=1,SOURCELIFETIME=65535,SSMPLYNAME="2000",HELLOINTERVAL=1,JPTIMERINTERVAL=18000,HELLOOVERRIDE=2500;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-PIMSITE.md`
