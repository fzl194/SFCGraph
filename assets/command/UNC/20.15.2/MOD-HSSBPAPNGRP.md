---
id: UNC@20.15.2@MMLCommand@MOD HSSBPAPNGRP
type: MMLCommand
name: MOD HSSBPAPNGRP（修改HSS BYPASS最小APN签约数据群组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: HSSBPAPNGRP
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
- 可靠性管理
- HSS BYPASS最小签约数据配置管理
status: active
---

# MOD HSSBPAPNGRP（修改HSS BYPASS最小APN签约数据群组）

## 功能

**适用网元：MME**

此命令用于修改HSS BYPASS最小APN签约数据群组。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNGRPID | APN群组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN本地配置签约群组ID。<br>数据来源：本端规划<br>取值范围：0~511<br>默认值：无<br>配置原则：无 |
| APNSUBIDX | APN本地签约索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN群组包含的APN本地签约数据索引。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无<br>配置原则：须先在<br>[ADD HSSBPAPNSUB](增加HSS BYPASS最小APN签约数据配置 (ADD HSSBPAPNSUB)_11385437.md)<br>中配置取值相同的<br>“APNSUBIDX”<br>参数。 |
| DEFAULTAPN | 是否默认APN | 可选必选说明：可选参数<br>参数含义：该参数用于指示APN本地签约数据索引对应的APN，是否为本APN群组内的默认APN。<br>数据来源：本端规划<br>取值范围：<br>- NO（否）<br>- YES（是）<br>默认值：无<br>配置原则：<br>- 一个APN群组里最多只能有一个默认APN。<br>- 默认APN的APNNI不支持通配符。<br>- 当APN群组里有多条APN时，要指定其中一个为默认APN。 |

## 操作的配置对象

- [HSS BYPASS最小APN签约数据群组（HSSBPAPNGRP）](configobject/UNC/20.15.2/HSSBPAPNGRP.md)

## 使用实例

修改HSS BYPASS最小APN签约数据群组配置，可以用如下命令：

```
MOD HSSBPAPNGRP: APNGRPID=1, APNSUBIDX=1, DEFAULTAPN=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改HSS-BYPASS最小APN签约数据群组-(MOD-HSSBPAPNGRP)_64021102.md`
