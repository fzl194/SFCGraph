---
id: UDG@20.15.2@MMLCommand@UBLK RU
type: MMLCommand
name: UBLK RU（解闭CSDB RU）
nf: UDG
version: 20.15.2
verb: UBLK
object_keyword: RU
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 闭塞管理
status: active
---

# UBLK RU（解闭CSDB RU）

## 功能

该命令用于解闭已闭塞的CSDB RU，使其他RU上的数据迁回到RU上。在分批升级之后，执行本命令，将数据迁移回RU上。

## 注意事项

- 该命令执行后，需要通过**[LST BLKHISTORY](查询CSDB RU闭塞信息（LST BLKHISTORY）_36508138.md)**命令查询解闭结果。
- 同一子集群中，待解闭RU的状态为闭塞状态时，才可以执行**[UBLK RU](解闭CSDB RU（UBLK RU）_36508137.md)**操作。
- 在执行**[UBLK RU](解闭CSDB RU（UBLK RU）_36508137.md)**后，RU处于**处理中**和**处理失败**状态时，禁止进行扩缩容和动态上下线操作。
- 该命令在容器场景下不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCALEGROUP | 物理资源组名称 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个物理资源组。<br>数据来源：该物理资源组名称可以通过<br>**[LST SERVICERUSTATE](../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令查询获取，对应<br>**ScaleGroup的名字**<br>。<br>取值范围：字符串类型，长度为1～63。<br>默认值：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RU]] · 解闭CSDB RU（RU）

## 使用实例

解闭“物理资源组名称”为“SG1_CSDB_ForCommon”中已经闭塞的RU:

UBLK RU: SCALEGROUP="SG1_CSDB_ForCommon";

## 证据

- 原始手册：`evidence/UDG/20.15.2/UBLK-RU.md`
