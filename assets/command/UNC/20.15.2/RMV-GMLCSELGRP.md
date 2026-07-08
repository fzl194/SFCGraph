---
id: UNC@20.15.2@MMLCommand@RMV GMLCSELGRP
type: MMLCommand
name: RMV GMLCSELGRP（删除GMLC选择策略组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GMLCSELGRP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC选择策略组
status: active
---

# RMV GMLCSELGRP（删除GMLC选择策略组）

## 功能

**适用网元：MME**

该命令用于删除GMLC选择策略组。

## 注意事项

- 该命令执行后立即生效。
- 当GMLC选择策略组内有选择策略时，无法删除，需要删除该策略组内的所有选择策略。可以执行[**LST GMLCSELPLCY**](../GMLC选择策略/查询GMLC选择策略(LST GMLCSELPLCY)_26145814.md)查看具体情况。
- 当GMLC选择策略组索引被[**ADD LCSPARAEX**](../LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md)命令引用时，无法删除。可以执行[**LST LCSPARAEX**](../LCS扩展参数/查询LCS扩展参数(LST LCSPARAEX)_72225495.md)查看引用情况。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：必选参数<br>参数含义：该参数在系统内唯一标识一个GMLC选择策略组。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GMLCSELGRP]] · GMLC选择策略组（GMLCSELGRP）

## 使用实例

删除索引为0的GMLC选择策略组。

RMV GMLCSELGRP: GMLCGRPID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GMLCSELGRP.md`
