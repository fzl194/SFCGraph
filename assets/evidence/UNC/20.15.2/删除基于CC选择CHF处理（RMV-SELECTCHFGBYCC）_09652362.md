# 删除基于CC选择CHF处理（RMV SELECTCHFGBYCC）

- [命令功能](#ZH-CN_MMLREF_0209652362__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652362__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652362__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652362__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652362)

**适用NF：PGW-C、SMF**

该命令用于删除基于CC选择CHF处理。

## [注意事项](#ZH-CN_MMLREF_0209652362)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652362)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652362)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTYPE | Charge Characteristic类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费属性。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（未指定Charge Characteristic的值）<br>- VALUE（指定Charge Characteristic的值）<br>默认值：无<br>配置原则：无 |
| CCVALUE | Charge Characteristic值 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定特殊的Charge Characteristic值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| MASK | Charge Characteristic特定值掩码 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于指定计费属性的掩码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。配置的计费属性掩码计费属性值参数做与运算后，需要等于计费属性值，否则配置失败。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652362)

删除基于CC选择CHF处理：

```
RMV SELECTCHFGBYCC: CCTYPE=VALUE, CCVALUE="1234", MASK="ff";
```
