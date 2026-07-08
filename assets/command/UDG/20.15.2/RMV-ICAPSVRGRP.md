---
id: UDG@20.15.2@MMLCommand@RMV ICAPSVRGRP
type: MMLCommand
name: RMV ICAPSVRGRP（删除ICAP服务器组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ICAPSVRGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器组
status: active
---

# RMV ICAPSVRGRP（删除ICAP服务器组）

## 功能

**适用NF：PGW-U、UPF**

![](删除ICAP服务器组（RMV ICAPSVRGRP）_32582493.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令可能导致无可用的ICAP服务器。

该命令用于删除指定名称的ICAP Server Group实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ICAPSVRGRP]] · ICAP服务器组（ICAPSVRGRP）

## 使用实例

删除指定名称为isg1的ICAP Server Group实例：

```
RMV ICAPSVRGRP: ICAPSVRGRPNAME="isg1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ICAPSVRGRP.md`
