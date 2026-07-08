---
id: UNC@20.15.2@MMLCommand@LST PERFNGLANGRP
type: MMLCommand
name: LST PERFNGLANGRP（查询用于性能统计的5G LAN群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFNGLANGRP
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 5G LAN组性能统计
status: active
---

# LST PERFNGLANGRP（查询用于性能统计的5G LAN群组）

## 功能

**适用NF：SMF**

该命令用于查询可用于性能统计的5G LAN群组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 5G LAN组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN群组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是18~37。字母大小写不敏感且全局唯一。<br>默认值：无<br>配置原则：<br>GROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |

## 操作的配置对象

- [用于性能统计的5G LAN群组（PERFNGLANGRP）](configobject/UNC/20.15.2/PERFNGLANGRP.md)

## 使用实例

查询所有可用于性能统计的5G LAN群组，执行如下命令：

```
%%LST PERFNGLANGRP:;%%
RETCODE = 0  操作成功

结果如下
--------
5G LAN组ID  =  a0000001-460-003-01
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用于性能统计的5G-LAN群组（LST-PERFNGLANGRP）_79256716.md`
