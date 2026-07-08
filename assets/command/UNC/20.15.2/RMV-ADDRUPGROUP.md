---
id: UNC@20.15.2@MMLCommand@RMV ADDRUPGROUP
type: MMLCommand
name: RMV ADDRUPGROUP（删除UPF组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ADDRUPGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配UPF组管理
status: active
---

# RMV ADDRUPGROUP（删除UPF组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除指定的UPF组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADDRUPGROUP]] · UPF组（ADDRUPGROUP）

## 使用实例

删除UPF组, 名称是upfgrp1：

```
RMV ADDRUPGROUP: UPFGRPNAME="upfgrp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ADDRUPGROUP.md`
