---
id: UNC@20.15.2@MMLCommand@ADD GMLCSELGRP
type: MMLCommand
name: ADD GMLCSELGRP（增加GMLC选择策略组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GMLCSELGRP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 192
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC选择策略组
status: active
---

# ADD GMLCSELGRP（增加GMLC选择策略组）

## 功能

**适用网元：MME**

该命令用于增加GMLC选择策略组。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为192。
- 同一GMLC选择策略组索引只能被[**ADD LCSPARAEX**](../LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md)引用一次。
- 此配置涉及位置定位服务（LCS）特性（特性编号：WSFD-106401，license部件编码：LKV2LCS02），请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：必选参数<br>参数含义：该参数在系统内唯一标识一个GMLC选择策略组。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC选择策略组的描述信息。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLCSELGRP]] · GMLC选择策略组（GMLCSELGRP）

## 使用实例

添加一个索引为0的GMLC选择策略组。

ADD GMLCSELGRP: GMLCGRPID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GMLC选择策略组(ADD-GMLCSELGRP)_26145810.md`
