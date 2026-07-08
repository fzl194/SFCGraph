---
id: UDG@20.15.2@MMLCommand@RMV TOPOLICYMATCH
type: MMLCommand
name: RMV TOPOLICYMATCH（删除TCP优化策略匹配规则）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TOPOLICYMATCH
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- TCP优化服务管理
- TCP优化策略匹配
status: active
---

# RMV TOPOLICYMATCH（删除TCP优化策略匹配规则）

## 功能

**适用NF：PGW-U、UPF**

![](删除TCP优化策略匹配规则（RMV TOPOLICYMATCH）_87096440.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定或所有TCP优化策略匹配规则，可能影响TCP优化效果，请谨慎使用。

该命令用于删除TCP优化策略匹配规则。当运营商希望删除TCP优化策略匹配规则时，则配置该命令。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 如果CellGroupName/IMSIGroupName/RATtype都不输入，表示删除系统中所有TCP优化策略匹配规则。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLGROUPNAME | 小区组名称 | 可选必选说明：可选参数<br>参数含义：指定小区组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CELLBINDGRP命令配置生成。 |
| IMSIGROUPNAME | IMSI 组名称 | 可选必选说明：可选参数<br>参数含义：指定IMSI组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD IMSIBINDGRP命令配置生成。 |
| RATTYPE | RAT类型 | 可选必选说明：可选参数<br>参数含义：无线接入技术类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- UTRAN：3G用户。<br>- EUTRAN：4G用户。<br>- NR：5G用户。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOPOLICYMATCH]] · TCP优化策略匹配规则（TOPOLICYMATCH）

## 使用实例

运营商需要删除匹配条件为小区组名称是TestCellGroupName的小区：

```
RMV TOPOLICYMATCH: CELLGROUPNAME="TestCellGroupName";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除TCP优化策略匹配规则（RMV-TOPOLICYMATCH）_87096440.md`
