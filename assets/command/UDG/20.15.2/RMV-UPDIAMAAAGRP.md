---
id: UDG@20.15.2@MMLCommand@RMV UPDIAMAAAGRP
type: MMLCommand
name: RMV UPDIAMAAAGRP（删除Diameter AAA服务器组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPDIAMAAAGRP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA组
status: active
---

# RMV UPDIAMAAAGRP（删除Diameter AAA服务器组）

## 功能

**适用NF：UPF**

此命令用于删除一个Diameter AAA组。当某个Diameter AAA组没有绑定到任何APN下，且该组不再被使用时，操作员可以执行此命令删除该组。

## 注意事项

- 该命令执行后立即生效。
- 如果Diameter AAA组已经绑定到APN，则不允许删除。 如果Diameter AAA组下已经绑定了Diameter AAA，则相应的Diameter AAA绑定关系（DiamAAABndGrp）会删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMAAAGRP]] · Diameter AAA服务器组（UPDIAMAAAGRP）

## 使用实例

根据网络规划，删除名称为“diametergroup”的Diameter AAA组：

```
RMV UPDIAMAAAGRP:GROUPNAME="diametergroup";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Diameter-AAA服务器组（RMV-UPDIAMAAAGRP）_45432714.md`
