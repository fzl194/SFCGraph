---
id: UNC@20.15.2@MMLCommand@RMV DMRTGRP
type: MMLCommand
name: RMV DMRTGRP（删除Diameter路由组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMRTGRP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter路由组
status: active
---

# RMV DMRTGRP（删除Diameter路由组）

## 功能

**适用网元：SGSN、MME**

该命令用于删除一条或多条Diameter路由组配置。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入路由模式，表示删除此路由组下所有路由配置。
- 删除该路由组，将导致引用此路由组的Diameter链路发生中断。
- 当IMSI与HSS的映射关系表引用路由组索引时，不允许删除，可在UNCMML窗口上执行命令[**LST IMSIHSS**](../../../Diameter应用协议/IMSI-HSS转换信息/查询IMSI-HSS对应关系(LST IMSIHSS)_72345053.md)查看路由组索引是否被引用
- 当GMLCSELPLCY表引用路由组索引时，不允许删除，可以在UNCMML窗口上执行命令[**LST GMLCSELPLCY**](../../../业务安全管理/LCS/GMLC选择策略/查询GMLC选择策略(LST GMLCSELPLCY)_26145814.md)查看路由组索引是否被引用。
- 如果Diameter路由组满足以下两个条件：
- 1. IMSI-HSS对应关系表引用该Diameter路由组索引，且该路由组索引对应的Diameter路由组的“路由优选模式”为“REAL_ROUTE_PREFER（优选域路由）”；
- 2. Diameter路由组中相同路由索引的记录只有1条；

则该记录不能删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPIDX | 路由组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由组索引。<br>取值范围：0~1023<br>默认值：无<br>说明：可以通过<br>[**LST DMRTGRP**](查询Diameter路由组(LST DMRTGRP)_26306104.md)<br>命令查看已有配置，确认所要删除的Diameter路由组的索引。 |
| RTMODE | 路由模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该条路由的路由索引对应的路由模式。<br>数据来源：整网规划<br>取值范围：<br>- “REALM_ROUTE(域路由)”<br>- “HOST_ROUTE（主机路由）”<br>默认值：无 |
| ROUTEIDX | 路由索引 | 可选必选说明：可选参数<br>参数含义：该参数用于路由索引。<br>数据来源：本端规划<br>取值范围：0~2047<br>默认值：无 |
| PEERIDX | 对端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于标识目的对端。<br>前提条件：该参数在<br>“路由模式”<br>为<br>“REALM_ROUTE(域路由)”<br>时配置。<br>数据来源：本端规划<br>取值范围：0~639<br>默认值：无 |

## 操作的配置对象

- [Diameter路由组（DMRTGRP）](configobject/UNC/20.15.2/DMRTGRP.md)

## 使用实例

删除索引号为6的Diameter路由组：

RMV DMRTGRP: GRPIDX=6;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter路由组(RMV-DMRTGRP)_72225971.md`
