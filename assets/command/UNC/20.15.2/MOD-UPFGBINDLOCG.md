---
id: UNC@20.15.2@MMLCommand@MOD UPFGBINDLOCG
type: MMLCommand
name: MOD UPFGBINDLOCG（修改UPF组与Diameter本端主机组的关联关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: UPFGBINDLOCG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- 关联UPF组与Diameter本端主机组的关联关系
status: active
---

# MOD UPFGBINDLOCG（修改UPF组与Diameter本端主机组的关联关系）

## 功能

**适用NF：PGW-C、SMF**

此命令用于修改指定的UPF组与指定的Diameter本端主机组的绑定关系。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 单个绑定关系组内最多可以有64组UPF组与Diameter本端主机组的绑定关系。
- 在同一个绑定关系组内，UPF组不允许重复。
- UPF组参数不允许修改，可以修改本端主机组和优先级。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | 可选必选说明：必选参数<br>参数含义：该参数设置UPF组与Diameter本端主机组的绑定关系组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPFGLOCGBNDGRP命令配置生成。 |
| UPFGRPNAME | Gx UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD GXUPFGROUP命令配置生成。 |
| DIAMLOCGRPNAME | Diameter本端信息组名称 | 可选必选说明：可选参数<br>参数含义：该参数用户指定Diameter本端主机组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD LOCALHOSTGRP命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定匹配优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～127。值越小优先级越高。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFGBINDLOCG]] · UPF组与Diameter本端主机组的关联关系（UPFGBINDLOCG）

## 使用实例

修改Diameter本端主机名与Diameter本端主机组的绑定关系，绑定关系组名为“abc”，UPF组名为“upfgroup”，修改diameter本端主机组名为“locgroup”，优先级为15：

```
MOD UPFGBINDLOCG: UPFGLOCGBNDGNAME="abc", UPFGRPNAME="upfgroup", DIAMLOCGRPNAME="locgroup", PRIORITY=15;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-UPFGBINDLOCG.md`
