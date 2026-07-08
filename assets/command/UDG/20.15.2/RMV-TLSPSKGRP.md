---
id: UDG@20.15.2@MMLCommand@RMV TLSPSKGRP
type: MMLCommand
name: RMV TLSPSKGRP（删除TLS预共享密钥组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TLSPSKGRP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS预共享密钥组管理
status: active
---

# RMV TLSPSKGRP（删除TLS预共享密钥组）

## 功能

该命令用于删除预共享密钥组。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSKGRPIDX | 预共享密钥组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TLS预共享密钥组的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [预共享密钥组信息（TLSPSKGRP）](configobject/UDG/20.15.2/TLSPSKGRP.md)

## 使用实例

若需要删除组索引为1的预共享密钥组，执行如下命令：

```
RMV TLSPSKGRP: PSKGRPIDX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除TLS预共享密钥组（RMV-TLSPSKGRP）_07589321.md`
