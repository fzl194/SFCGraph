# 修改计费星期表（MOD WEEKDAY）

- [命令功能](#ZH-CN_CONCEPT_0209896832__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896832__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896832__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896832__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896832__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896832)

**适用NF：SGW-C、PGW-C、SMF**

该命令用来修改指定周日期的费率类型为工作日或周末。

#### [注意事项](#ZH-CN_CONCEPT_0209896832)

- 该命令执行后立即生效。
- 此命令不支持修改计费属性优先级，如需修改，必须先通过RMV WEEKDAY命令删除原来的配置，然后通过ADD WEEKDAY命令重新增加。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896832)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896832)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALFLG | 全局配置 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：<br>- GLOBAL：当GLOBALFLG值为GLOBAL时，表示要配置全局计费星期表。<br>- CHARGE_CHARACT：当GLOBALFLG值为CHARGE_CHARACT时，表示要通过计费属性配置计费星期表。 |
| CCVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：该参数用于指定特殊的CC值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CCMASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：该参数用于指定计费属性的掩码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| CCPRIORITY | 计费属性优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：该参数用于设置优先级。相同的周日期下，不允许指定相同的优先级。配置mask时必须指定优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| DAYOFWEEK | 周日期 | 可选必选说明：必选参数<br>参数含义：该参数用于设置周日期号。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SUNDAY：指定为周日。<br>- MONDAY：指定为周一。<br>- TUESDAY：指定为周二。<br>- WEDNESDAY：指定为周三。<br>- THURSDAY：指定为周四。<br>- FRIDAY：指定为周五。<br>- SATURDAY：指定为周六。<br>默认值：无<br>配置原则：无 |
| TARIFFTYPE | 费率类型 | 可选必选说明：必选参数<br>参数含义：该参数用于修改费率类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- WORKDAY<br>- WEEKEND<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896832)

修改计费属性值为0x0400的用户星期三的费率类型为周末：GLOBALFLG为CHARGE_CHARACT，CCVALUE为0x0400，CCPRIORITY为1，DAYOFWEEK为WEDNESDAY，TARIFFTYPE为WEEKEND：

```
MOD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x400",CCPRIORITY=1,DAYOFWEEK=WEDNESDAY,TARIFFTYPE=WEEKEND;
```
