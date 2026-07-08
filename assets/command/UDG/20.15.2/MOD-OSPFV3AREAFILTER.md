---
id: UDG@20.15.2@MMLCommand@MOD OSPFV3AREAFILTER
type: MMLCommand
name: MOD OSPFV3AREAFILTER（修改OSPFv3区域过滤LSA配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFV3AREAFILTER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域过滤LSA配置
status: active
---

# MOD OSPFV3AREAFILTER（修改OSPFv3区域过滤LSA配置）

## 功能

该命令用于修改对区域内Type 3 LSA进行过滤配置。

## 注意事项

- 该命令执行后立即生效。
- 只有配置了OSPFv3进程和OSPFv3区域后才能使用该命令。
- 此命令仅在ABR上配置。
- 对于命名型ACL，使用配置过滤规则时，只有source参数指定的源地址范围和time-range参数指定的时间段对配置规则过滤规则有效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。请使用LST OSPFV3命令查看可用的OSPFv3进程。 |
| AREAID | OSPFv3区域号 | 可选必选说明：必选参数<br>参数含义：OSPFv3区域号。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| FILTERTYPE | 过滤方向 | 可选必选说明：必选参数<br>参数含义：过滤方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- import：引入方向的过滤。<br>- export：发布方向的过滤。<br>默认值：无 |
| TYPE | 过滤类型 | 可选必选说明：必选参数<br>参数含义：过滤规则类型(ACL名称或ACL号/IP前缀过滤策略名称)。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl_name：ACL6名称。<br>- ip_prefix：IPv6前缀池列表。<br>- route_policy：路由策略。<br>- acl_num：ACL号。<br>默认值：无 |
| ACLNAMEORNUM | ACL名称或ACL号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“acl_name” 或 “acl_num”时为必选参数。<br>参数含义：该参数用于指定ACL规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 当过滤类型指定为acl_name或者acl_num时生效。<br>- 配置时，ACL名称或ACL号实际下发由内部自动区分，不依照过滤类型。<br>- 不支持空格，区分大小写。<br>- 当输入ACL名称时以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”或下划线“_”的组合。<br>- 当输入ACL号时，取值范围是2000~2999。 |
| IPPREFIX | IP前缀 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“ip_prefix”时为必选参数。<br>参数含义：IP前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |
| ROUTEPLYNAME | 路由策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“route_policy”时为必选参数。<br>参数含义：路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3区域过滤LSA配置（OSPFV3AREAFILTER）](configobject/UDG/20.15.2/OSPFV3AREAFILTER.md)

## 使用实例

修改OSPFv3对出方向的Type 3 LSA进行过滤名为2500：

```
MOD OSPFV3AREAFILTER:PROCID=1,TOPOID=0,AREAID="0.0.0.1",FILTERTYPE=export,TYPE=acl_num,ACLNAMEORNUM="2500";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPFv3区域过滤LSA配置（MOD-OSPFV3AREAFILTER）_00865537.md`
