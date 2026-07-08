---
id: UDG@20.15.2@MMLCommand@RMV IMSIBINDGRP
type: MMLCommand
name: RMV IMSIBINDGRP（删除IMSI和IMSI组绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IMSIBINDGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- IMSI组配置
status: active
---

# RMV IMSIBINDGRP（删除IMSI和IMSI组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除IMSI和IMSI组的绑定关系。当运行商希望删除IMSI和IMSI组的绑定关系时，则配置该命令。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 如果不输入IMSI名称只输入IMSI组名称，表示删除系统中所有IMSI和该IMSI组的绑定关系。
- 如果不输入IMSI名称和IMSI组，表示删除系统中所有IMSI与IMSI组的绑定关系。
- 如果IMSI组被TO策略匹配规则作为匹配条件，则不允许对该IMSI组进行批量删除操作。
- 如果IMSI组被TO策略匹配规则作为匹配条件，且只有一个IMSI和该IMSI组存在绑定关系时，不允许删除的该IMSI和该IMSI组之间的绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIGROUPNAME | IMSI 组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IMSI组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于表示用户的IMSI号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSIBINDGRP]] · IMSI和IMSI组绑定关系（IMSIBINDGRP）

## 使用实例

运营商需要删除名称为123456789的IMSI和名称为TestIMSIGroupName的IMSI组的绑定关系：

```
RMV IMSIBINDGRP: IMSIGROUPNAME="TestIMSIGroupName", IMSI="123456789";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-IMSIBINDGRP.md`
