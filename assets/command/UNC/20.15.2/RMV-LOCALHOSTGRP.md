---
id: UNC@20.15.2@MMLCommand@RMV LOCALHOSTGRP
type: MMLCommand
name: RMV LOCALHOSTGRP（删除Diameter本端主机组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOCALHOSTGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diamter本端主机组
status: active
---

# RMV LOCALHOSTGRP（删除Diameter本端主机组）

## 功能

**适用NF：PGW-C、SMF**

此命令用于删除指定的Diameter本端主机组。

## 注意事项

- 该命令执行后立即生效。
- 如果其已经绑定到UPF Local绑定组，则禁止删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGRPNAME | Diameter本端信息组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter本端主机组的名字，要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALHOSTGRP]] · Diameter本端主机组（LOCALHOSTGRP）

## 使用实例

删除Diameter主机组，“LOCGRPNAME”为“localgroup”：

```
RMV LOCALHOSTGRP: LOCGRPNAME="localgroup";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter本端主机组（RMV-LOCALHOSTGRP）_29420950.md`
