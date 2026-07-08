---
id: UDG@20.15.2@MMLCommand@MOD OSPFAREAFILTER
type: MMLCommand
name: MOD OSPFAREAFILTER（修改区域过滤策略配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFAREAFILTER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域过滤策略配置
status: active
---

# MOD OSPFAREAFILTER（修改区域过滤策略配置）

## 功能

该命令用于修改对区域内的Type 3 LSA进行过滤配置。

## 注意事项

- 该命令执行后立即生效。
- 只有配置了OSPF进程和OSPF区域后才能使用此命令。
- 此命令仅在ABR上配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| AREAID | 区域ID | 可选必选说明：必选参数<br>参数含义：区域ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| TOPONAME | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- base：基础类型。<br>默认值：无 |
| FILTERTYPE | 过滤方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- import：引入方向的过滤。<br>- export：发布方向的过滤。<br>默认值：无 |
| TYPE | 过滤规则类型 | 可选必选说明：必选参数<br>参数含义：过滤规则类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl_name：ACL名称。<br>- ip_prefix：IP前缀列表。<br>- route_policy：路由策略名。<br>- acl_num：ACL号。<br>默认值：无 |
| ACLNAMEORNUM | ACL名称或ACL号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“acl_name” 或 “acl_num”时为必选参数。<br>参数含义：该参数用于指定ACL规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 当过滤类型指定为acl_name或者acl_num时生效。<br>- 配置时，ACL名称或ACL号实际下发由内部自动区分，不依照过滤类型。<br>- 不支持空格，区分大小写。<br>- 当输入ACL名称时以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”或下划线“_”的组合。<br>- 当输入ACL号时，取值范围是2000~2999。 |
| IPPREFIX | IP前缀过滤策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“ip_prefix”时为必选参数。<br>参数含义：IP前缀过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：不支持空格，区分大小写。 |
| ROUTEPOLICY | 路由策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“route_policy”时为必选参数。<br>参数含义：路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：不支持空格，区分大小写。 |
| INCAGGRFLAG | 包括ABR Summary LSA | 可选必选说明：条件可选参数<br>前提条件：该参数在“FILTERTYPE”配置为“import”时为可选参数。<br>参数含义：包括ABR Summary LSA。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFAREAFILTER]] · 区域过滤策略配置（OSPFAREAFILTER）

## 使用实例

在进程1的区域0.0.0.1下修改出方向过滤策略的地址前缀名称为“ip-prefix1”：

```
MOD OSPFAREAFILTER:PROCID=1,AREAID="0.0.0.1",TOPONAME=base,FILTERTYPE=export,TYPE=ip_prefix,IPPREFIX="ip-prefix1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-OSPFAREAFILTER.md`
