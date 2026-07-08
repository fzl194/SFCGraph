---
id: UNC@20.15.2@MMLCommand@ADD UPFGBINDLOCG
type: MMLCommand
name: ADD UPFGBINDLOCG（增加UPF组与Diameter本端主机组的关联关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPFGBINDLOCG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 3000
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- 关联UPF组与Diameter本端主机组的关联关系
status: active
---

# ADD UPFGBINDLOCG（增加UPF组与Diameter本端主机组的关联关系）

## 功能

**适用NF：PGW-C、SMF**

此命令用于添加指定的UPF组与指定的Diameter本端主机组的绑定关系。在用户根据PCRF或者DRA的相关配置选择对端主机后，可以根据此配置选择用户使用的本端主机。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为3000。
- 单个UPF组与Diameter本端主机组的绑定关系组内最多可以有64组绑定关系。
- 在同一个绑定关系组内，UPF组不允许重复。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | 可选必选说明：必选参数<br>参数含义：该参数设置UPF组与Diameter本端主机组的绑定关系组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPFGLOCGBNDGRP命令配置生成。 |
| UPFGRPNAME | Gx UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD GXUPFGROUP命令配置生成。 |
| DIAMLOCGRPNAME | Diameter本端信息组名称 | 可选必选说明：必选参数<br>参数含义：该参数用户指定Diameter本端主机组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD LOCALHOSTGRP命令配置生成。 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～127。值越小优先级越高。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UPF组与Diameter本端主机组的关联关系（UPFGBINDLOCG）](configobject/UNC/20.15.2/UPFGBINDLOCG.md)

## 使用实例

增加Diameter本端主机名与Diameter本端主机组的绑定关系，组名为“abc”，UPF组名为“upfgroup”，diameter本端主机组名为“locgroup”，优先级为15：

```
ADD UPFGBINDLOCG: UPFGLOCGBNDGNAME="abc", UPFGRPNAME="upfgroup", DIAMLOCGRPNAME="locgroup", PRIORITY=15;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UPF组与Diameter本端主机组的关联关系（ADD-UPFGBINDLOCG）_29660172.md`
