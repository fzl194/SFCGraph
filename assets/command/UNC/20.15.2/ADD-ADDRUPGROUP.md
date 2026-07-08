---
id: UNC@20.15.2@MMLCommand@ADD ADDRUPGROUP
type: MMLCommand
name: ADD ADDRUPGROUP（增加UPF组）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD ADDRUPGROUP（增加UPF组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来增加UPF组。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPFGRPTYPE | UPF组类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组的UE地址规划类型。<br>数据来源：本端规划<br>取值范围：<br>- “Local（本地）”：通过5GC（SMF或UPF）或AAA服务器分配动态地址。<br>- “UDM（UDM）”：通过UDM签约分配静态地址。<br>- “Radius（RADIUS）”：通过外部AAA服务器分配静态地址。<br>- “DHCP（DHCP）”：通过外部DHCP服务器分配静态地址。<br>默认值：Local<br>配置原则：无 |

## 操作的配置对象

- [UPF组（ADDRUPGROUP）](configobject/UNC/20.15.2/ADDRUPGROUP.md)

## 使用实例

增加UPF组, 名称是upfgrp1：

```
ADD ADDRUPGROUP: UPFGRPNAME="upfgrp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UPF组（ADD-ADDRUPGROUP）_49644911.md`
