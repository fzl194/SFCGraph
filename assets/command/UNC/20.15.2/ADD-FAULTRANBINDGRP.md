---
id: UNC@20.15.2@MMLCommand@ADD FAULTRANBINDGRP
type: MMLCommand
name: ADD FAULTRANBINDGRP（增加N3接口故障RAN与RAN组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: FAULTRANBINDGRP
command_category: 配置类
applicable_nf:
- SGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP故障管理
- N3接口故障RAN组绑定管理
status: active
---

# ADD FAULTRANBINDGRP（增加N3接口故障RAN与RAN组的绑定关系）

## 功能

**适用NF：SGW-C、SMF**

该命令用于添加N3接口故障RAN与故障RAN组的绑定关系，当N3接口出现故障，SMF在为通过和故障RAN组绑定的RAN接入的用户选择UPF时，会自动过滤掉与该RAN组绑定的UPF组内的UPF。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 一个RAN组最多可以绑定1024个实例。
- 如果要配置IPv4v6类型双栈地址，需要在同一条记录中同时配置NODEIPV4和NODEIPV6。
- 不同基站的基站IP地址不允许重复。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMN | PLMN | 可选必选说明：必选参数<br>参数含义：该参数用于标识接入网设备的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| RANNODETYPE | RAN基站类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAN基站类型。<br>数据来源：全网规划<br>取值范围：<br>- “MACROENB（Macro eNodeB）”：Macro eNodeB<br>- “SHORTENB（Short Macro eNodeB）”：Short Macro eNodeB<br>- “LONGENB（Long Macro eNodeB）”：Long Macro eNodeB<br>- “GNB（Global gNodeB）”：Global gNodeB<br>默认值：无<br>配置原则：无 |
| RANNODEID | RAN基站标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAN基站标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。如果将RANNODETYPE设置为MACROENB，则该参数的值范围为0到1048575；如果将RANNODETYPE设置为SHORTENB，则该参数的取值范围为0到262143；如果将RANNODETYPE设置为LONGENB，则该参数的取值范围为0到2097151；如果将RANNODETYPE设置为GNB，则该参数的值范围为0到4294967295。<br>默认值：无<br>配置原则：无 |
| NODEIDLEN | RAN基站标识长度(比特) | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAN基站的标识长度(比特)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是18~32。当RANNODETYPE选择MACROENB时，本参数应当输入值为20；当RANNODETYPE选择SHORTENB时，本参数应当输入值为18；当RANNODETYPE选择LONGENB时，本参数应当输入值为21；当RANNODETYPE选择GNB时，本参数的输入范围应当是22到32。<br>默认值：无<br>配置原则：无 |
| RANGRPNAME | RAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD FAULTRANGRP命令配置生成。 |
| NODEIPV4 | 基站IPv4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基站IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| NODEIPV6 | 基站IPv6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基站IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [N3接口故障RAN与RAN组的绑定关系（FAULTRANBINDGRP）](configobject/UNC/20.15.2/FAULTRANBINDGRP.md)

## 使用实例

新增N3接口故障RAN与RAN组绑定：

```
ADD FAULTRANBINDGRP: PLMN="12303", RANNODETYPE=GNB, RANNODEID=327697, NODEIDLEN=24, RANGRPNAME="group1", NODEIPV4="192.168.1.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加N3接口故障RAN与RAN组的绑定关系（ADD-FAULTRANBINDGRP）_39777019.md`
