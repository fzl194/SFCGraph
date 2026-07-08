---
id: UDG@20.15.2@MMLCommand@ADD UPDIAMAAAGRP
type: MMLCommand
name: ADD UPDIAMAAAGRP（增加Diameter AAA服务器组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPDIAMAAAGRP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
max_records: 10
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA组
status: active
---

# ADD UPDIAMAAAGRP（增加Diameter AAA服务器组）

## 功能

**适用NF：UPF**

此命令用于新建一个Diameter AAA组。

## 注意事项

- 该命令执行后对新接入的会话生效。
- 该命令最大记录数为10。
- 此命令为建立会话的核心配置，需绑定到APN后才能生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPDIAMAAAGRP]] · Diameter AAA服务器组（UPDIAMAAAGRP）

## 使用实例

根据网络规划，需要新增一个名称为“diametergroup”的Diameter AAA组：

```
ADD UPDIAMAAAGRP:GROUPNAME="diametergroup";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-UPDIAMAAAGRP.md`
