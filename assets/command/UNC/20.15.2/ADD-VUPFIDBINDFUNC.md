---
id: UNC@20.15.2@MMLCommand@ADD VUPFIDBINDFUNC
type: MMLCommand
name: ADD VUPFIDBINDFUNC（增加虚拟UPF实例标识绑定的功能）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: VUPFIDBINDFUNC
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- 虚拟UPF管理
- 功能绑定管理
status: active
---

# ADD VUPFIDBINDFUNC（增加虚拟UPF实例标识绑定的功能）

## 功能

**适用NF：SMF**

该命令用于增加虚拟UPF实例标识绑定的功能。

在主锚点和辅锚点会话或IUPF会话共部署或者多辅锚点会话共部署的场景下，SMF给虚拟UPF实例标识配置绑定的功能，使该虚拟UPF实例标识只能应用于该功能。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入20480条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VUPFINSTANCEID | 虚拟UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于虚拟UPF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。该参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD VIRTUALUPFID中参数“VUPFINSTANCEID”保持一致，使用该前需通过ADD VIRTUALUPFID添加一组记录。 |
| FUNCNAME | 功能名称 | 可选必选说明：必选参数<br>参数含义：该参数表示虚拟UPF实例标识绑定的功能。<br>数据来源：本端规划<br>取值范围：<br>- “MULDNN（2B2C漫游双DNN与共享UPF）”：同时支持2B2C漫游双DNN与共享UPF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [虚拟UPF实例标识的绑定功能（VUPFIDBINDFUNC）](configobject/UNC/20.15.2/VUPFIDBINDFUNC.md)

## 使用实例

增加虚拟UPF实例标识为v_upf1的绑定功能为双域专网：

```
ADD VUPFIDBINDFUNC:VUPFINSTANCEID="v_upf1",FUNCNAME=MULDNN;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加虚拟UPF实例标识绑定的功能（ADD-VUPFIDBINDFUNC）_08199834.md`
