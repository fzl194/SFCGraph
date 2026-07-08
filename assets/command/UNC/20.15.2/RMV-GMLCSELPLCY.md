---
id: UNC@20.15.2@MMLCommand@RMV GMLCSELPLCY
type: MMLCommand
name: RMV GMLCSELPLCY（删除GMLC选择策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GMLCSELPLCY
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
- GMLC选择策略
status: active
---

# RMV GMLCSELPLCY（删除GMLC选择策略）

## 功能

**适用网元：MME**

该命令用于删除指定条件下的GMLC选择策略。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：必选参数<br>参数含义：该参数在系统内唯一标识一个GMLC组。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无<br>配置原则：该参数需要在<br>[**ADD GMLCSELGRP**](../GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md)<br>中事先配置，可执行<br>[**LST GMLCSELGRP**](../GMLC选择策略组/查询GMLC选择策略组(LST GMLCSELGRP)_72345411.md)<br>进行查看。 |
| LCSCLIENTTYPE | LCS客户端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识LCS客户端类型。<br>数据来源：整网规划<br>取值范围：<br>- “EMERGENCY_SERVICES(紧急业务)”<br>- “VALUE_ADDED_SERVICES(增值业务)”<br>- “PLMN_OPERATOR_SERVICES(运营商业务)”<br>- “LAWFUL_INTERCEPT_SERVICES(合法定位)”<br>默认值：无 |
| LOCATIONTYPE | 位置区标识类型 | 可选必选说明：必选参数<br>参数含义：该参数标识位置标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “ECI(小区标识)”<br>- “TAC(跟踪区编码)”<br>默认值：无 |
| TACBEGIN | 跟踪区起始编码 | 可选必选说明：条件必选参数<br>参数含义：该参数表示跟踪区起始编码。<br>前提条件：该参数在"位置区标识类型"参数配置为"跟踪区编码"后生效。<br>数据来源：整网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| ECIBEGIN | 小区起始标识 | 可选必选说明：条件必选参数<br>参数含义：该参数表示E-UTRAN小区起始标识。<br>前提条件：该参数在"位置区标识类型"参数配置为"小区标识"后生效。<br>数据来源：整网规划<br>取值范围：0~268435455<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLCSELPLCY]] · GMLC选择策略（GMLCSELPLCY）

## 使用实例

删除索引为0的GMLC选择策略组内一条选择策略。该记录的LCS客户端类型为EMERGENCY_SERVICES（紧急业务）、小区起始标识为1。

RMV GMLCSELPLCY: GMLCGRPID=0, LCSCLIENTTYPE=EMERGENCY_SERVICES, LOCATIONTYPE=ECI, ECIBEGIN=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GMLC选择策略(RMV-GMLCSELPLCY)_26305622.md`
