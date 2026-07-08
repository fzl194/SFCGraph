---
id: UNC@20.15.2@MMLCommand@MOD NGUSRGRP
type: MMLCommand
name: MOD NGUSRGRP（修改5G用户群）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGUSRGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 用户群组标识管理
status: active
---

# MOD NGUSRGRP（修改5G用户群）

## 功能

**适用NF：AMF**

该命令用于修改5G用户群的属性，如描述信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRGRPID | 用户群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示用户群标识的描述信息，在运维过程中起到助记的作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGUSRGRP]] · 5G用户群（NGUSRGRP）

## 使用实例

若对标识为20的5G用户群，修改描述信息为“My City”，执行如下命令：

```
MOD NGUSRGRP: USRGRPID=20, DESC="My City";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G用户群（MOD-NGUSRGRP）_44007397.md`
