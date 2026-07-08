---
id: UDG@20.15.2@MMLCommand@MOD TLSPSKGRP
type: MMLCommand
name: MOD TLSPSKGRP（修改预共享密钥组信息）
nf: UDG
version: 20.15.2
verb: MOD
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

# MOD TLSPSKGRP（修改预共享密钥组信息）

## 功能

该命令用于修改预共享密钥组描述信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSKGRPIDX | 预共享密钥组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TLS预共享密钥组的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TLS预共享密钥组的描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TLSPSKGRP]] · 预共享密钥组信息（TLSPSKGRP）

## 使用实例

若需要修改组索引为1的TLS预共享密钥组的描述信息为“test”，执行如下命令：

```
MOD TLSPSKGRP: PSKGRPIDX=1, DESC="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-TLSPSKGRP.md`
