---
id: UNC@20.15.2@MMLCommand@ADD PERFNGLANGRP
type: MMLCommand
name: ADD PERFNGLANGRP（增加用于性能统计的5G LAN群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PERFNGLANGRP
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 5G LAN组性能统计
status: active
---

# ADD PERFNGLANGRP（增加用于性能统计的5G LAN群组）

## 功能

**适用NF：SMF**

该命令用于配置性能统计的5G LAN群组。当激活一个5G LAN组会话时，SMF会判断该组会话的5G LAN组ID是否与该命令中的5G LAN组ID一致。如果一致，则会对该5G LAN群组进行性能统计。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入512条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 5G LAN组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN群组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是18~37。字母大小写不敏感且全局唯一。<br>默认值：无<br>配置原则：<br>GROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |

## 操作的配置对象

- [用于性能统计的5G LAN群组（PERFNGLANGRP）](configobject/UNC/20.15.2/PERFNGLANGRP.md)

## 使用实例

新增一条群组编号为“A0000001-460-003-01”的5G LAN群组，用于性能统计，执行如下命令:

```
ADD PERFNGLANGRP: GROUPID="A0000001-460-003-01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加用于性能统计的5G-LAN群组（ADD-PERFNGLANGRP）_25214873.md`
