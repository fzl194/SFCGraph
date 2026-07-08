---
id: UDG@20.15.2@MMLCommand@RMV APPPOLICYCTRL
type: MMLCommand
name: RMV APPPOLICYCTRL（删除基于应用的质差上报策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: APPPOLICYCTRL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 基于应用的质差策略
status: active
---

# RMV APPPOLICYCTRL（删除基于应用的质差上报策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除基于应用的质差上报策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPIDNAME | 应用ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定重点业务保障的应用组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，区分大小写，长度为1-63位。<br>默认值：无<br>配置原则：无 |
| SUBAPPIDNAME | 子应用ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定重点业务保障的应用名称。<br>数据来源：全网规划<br>取值范围：字符串类型，区分大小写，长度为1-63位。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPPOLICYCTRL]] · 基于应用的质差上报策略（APPPOLICYCTRL）

## 使用实例

删除应用ID为zhibo，子应用ID为huya的基于应用的质差策略，执行如下命令：

```
RMV APPPOLICYCTRL: APPIDNAME="zhibo", SUBAPPIDNAME="huya";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于应用的质差上报策略（RMV-APPPOLICYCTRL）_09982390.md`
