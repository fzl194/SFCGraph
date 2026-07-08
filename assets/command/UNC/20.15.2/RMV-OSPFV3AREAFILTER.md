---
id: UNC@20.15.2@MMLCommand@RMV OSPFV3AREAFILTER
type: MMLCommand
name: RMV OSPFV3AREAFILTER（删除OSPFv3区域过滤LSA配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV OSPFV3AREAFILTER（删除OSPFv3区域过滤LSA配置）

## 功能

该命令用于删除对区域内Type 3 LSA进行过滤配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：必选参数<br>参数含义：OSPFv3区域号。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| FILTERTYPE | 过滤方向 | 可选必选说明：必选参数<br>参数含义：过滤方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- import：引入方向的过滤。<br>- export：发布方向的过滤。<br>默认值：无 |
| TYPE | 过滤类型 | 可选必选说明：可选参数<br>参数含义：过滤规则类型(ACL名称或ACL号/IP前缀过滤策略名称)。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl_name：ACL6名称。<br>- ip_prefix：IPv6前缀池列表。<br>- route_policy：路由策略。<br>- acl_num：ACL号。<br>默认值：无 |
| ACLNAMEORNUM | ACL名称或ACL号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“acl_name” 或 “acl_num”时为必选参数。<br>参数含义：该参数用于指定ACL规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| IPPREFIX | IP前缀 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“ip_prefix”时为必选参数。<br>参数含义：IP前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |
| ROUTEPLYNAME | 路由策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“route_policy”时为必选参数。<br>参数含义：路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3区域过滤LSA配置（OSPFV3AREAFILTER）](configobject/UNC/20.15.2/OSPFV3AREAFILTER.md)

## 使用实例

删除OSPFv3对出方向的Type 3 LSA的过滤配置：

```
RMV OSPFV3AREAFILTER:PROCID=1,AREAID="0.0.0.1",FILTERTYPE=export,TYPE=acl_num,ACLNAMEORNUM="2500";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除OSPFv3区域过滤LSA配置（RMV-OSPFV3AREAFILTER）_50121814.md`
