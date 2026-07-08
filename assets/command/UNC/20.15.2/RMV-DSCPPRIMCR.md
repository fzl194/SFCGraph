---
id: UNC@20.15.2@MMLCommand@RMV DSCPPRIMCR
type: MMLCommand
name: RMV DSCPPRIMCR（删除DSCP映射优先级配置表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DSCPPRIMCR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 接口DSCP管理
- DSCP优先级映射管理
status: active
---

# RMV DSCPPRIMCR（删除DSCP映射优先级配置表）

## 功能

**适用网元：MME**

本命令用于删除DSCP映射优先级表。删除DSCP值的映射关系后，对应DSCP值的报文将入“优先级4”的队列。

## 注意事项

- 该命令执行后立即生效。
- 该命令只能删除[**ADD DSCPPRIMCR**](增加DSCP映射优先级配置表(ADD DSCPPRIMCR)_71851003.md)添加的非默认记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SLTPR | 选择操作类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指示删除DSCP映射优先级表的操作类型。<br>数据来源：全网规划<br>取值范围： DSCP(DSCP映射关系)<br>默认值：无<br>配置原则：无 |
| DSCPV | DSCP值 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指示删除DSCP映射优先级表的DSCP值。<br>数据来源：全网规划<br>取值范围：0~63<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DSCPPRIMCR]] · DSCP映射优先级配置表（DSCPPRIMCR）

## 使用实例

删除DSCP为50的映射关系表：

RMV DSCPPRIMCR: SLTPR=DSCP, DSCPV=50;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DSCPPRIMCR.md`
