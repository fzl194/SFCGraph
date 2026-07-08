---
id: UDG@20.15.2@MMLCommand@ADD OSPFV3FILTERPOLICY
type: MMLCommand
name: ADD OSPFV3FILTERPOLICY（创建OSPFv3过滤策略配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: OSPFV3FILTERPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8016
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3过滤策略配置
status: active
---

# ADD OSPFV3FILTERPOLICY（创建OSPFv3过滤策略配置）

## 功能

该命令用于创建OSPFv3过滤策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8016。
- 只有在执行ADD OSPFV3配置了OSPFv3进程后才能使用此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。请使用LST OSPFV3命令查看可用的OSPFv3进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：0<br>配置原则：目前只支持默认拓扑0。 |
| FILTERTYPE | 过滤方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤方向是import还是export。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- import：引入方向的过滤。<br>- export：发布方向的过滤。<br>默认值：无<br>配置原则：<br>- import表示对接收到的区域内，区域间和自治系统外部的路由进行过滤。<br>- export表示对通过引入路由（OSPFv3）命令引入的路由信息向外发布时进行过滤。该命令需要配置在ASBR上。 |
| TYPE | 过滤规则类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl_name：ACL名称。<br>- ip_prefix：IPv6前缀过滤策略名称。<br>- route_policy：路由策略名。<br>- acl_num：ACL号。<br>默认值：无 |
| ACLNAMEORNUM | ACL名称或ACL号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“acl_name” 或 “acl_num”时为必选参数。<br>参数含义：该参数用于指定ACL规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 当过滤类型指定为acl_name或者acl_num时生效。<br>- 配置时，ACL名称或ACL号实际下发由内部自动区分，不依照过滤类型。<br>- 不支持空格，区分大小写。<br>- 当输入ACL名称时以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”或下划线“_”的组合。<br>- 当输入ACL号时，取值范围是2000~2999。<br>- 请使用LST ACLGROUP6命令查看已配置的IPv6 ACL规则组。 |
| IPPREFIX | IPv6前缀过滤策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“ip_prefix”时为必选参数。<br>参数含义：该参数用于指定待过滤的IPv6前缀过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：请使用LST IPV6PREFIXFILTERNODE命令查看已配置的IPv6前缀过滤器节点。 |
| ROUTEPLYNAME | 路由策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“route_policy”时为必选参数。<br>参数含义：该参数用于指定路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：请使用LST ROUTEPOLICY命令查看已配置的路由策略。 |
| PROTOCOL | 协议号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“FILTERTYPE”配置为“export”时为可选参数。<br>参数含义：该参数用于指定对某一种协议的路由进行过滤。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- static：静态路由。<br>- bgp：BGP协议。<br>- ospfv3：OSPFv3协议。<br>- wlr：无线路由。<br>默认值：无<br>配置原则：如果不输入该参数，则表示匹配所有协议。 |
| PROTOCOLPROCESSID | 协议进程号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOL”配置为“ospfv3”时为必选参数。<br>参数含义：该参数用于指定对某一进程的路由进行过滤。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：1<br>配置原则：<br>- OSPFv3引入外部路由后，为了避免路由环路的产生，通过过滤策略命令对引入的路由在发布时进行过滤，只将满足条件的外部路由转换为Type-5LSA并发布出去。<br>- 通过指定protocol或process-id对特定的某一种协议或者某一进程的路由进行过滤。如果没有指定protocol和process-id，则OSPFv3将对所有进入的路由信息进行过滤。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFV3FILTERPOLICY]] · OSPFv3过滤策略配置（OSPFV3FILTERPOLICY）

## 使用实例

在设备上建立OSPFv3进程1，并建立acl 2000：

```
ADD OSPFV3FILTERPOLICY: PROCID=1,TOPOID=0,FILTERTYPE=import,TYPE=acl_num,ACLNAMEORNUM="2000";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-OSPFV3FILTERPOLICY.md`
