# 删除虚拟UPF实例标识的绑定功能（RMV VUPFIDBINDFUNC）

- [命令功能](#ZH-CN_MMLREF_0000001308039994__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001308039994__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001308039994__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001308039994__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001308039994)

**适用NF：SMF**

该命令用于删除虚拟UPF实例标识绑定的功能。

## [注意事项](#ZH-CN_MMLREF_0000001308039994)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001308039994)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001308039994)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VUPFINSTANCEID | 虚拟UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于虚拟UPF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。该参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD VIRTUALUPFID中参数“VUPFINSTANCEID”保持一致，使用该前需通过ADD VIRTUALUPFID添加一组记录。 |
| FUNCNAME | 功能名称 | 可选必选说明：必选参数<br>参数含义：该参数表示虚拟UPF实例标识绑定的功能。<br>数据来源：本端规划<br>取值范围：<br>- “MULDNN（2B2C漫游双DNN与共享UPF）”：同时支持2B2C漫游双DNN与共享UPF。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001308039994)

删除虚拟UPF实例标识为v_upf1,FUNCNAME为MulDnn：

```
RMV VUPFIDBINDFUNC:VUPFINSTANCEID="v_upf1",FUNCNAME=MULDNN;
```
