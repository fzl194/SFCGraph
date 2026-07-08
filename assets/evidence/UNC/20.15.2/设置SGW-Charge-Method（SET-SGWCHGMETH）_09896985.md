# 设置SGW Charge Method（SET SGWCHGMETH）

- [命令功能](#ZH-CN_CONCEPT_0209896985__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896985__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896985__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896985__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896985__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896985)

**适用NF：SGW-C**

该命令用于设置SGW计费方式。

#### [注意事项](#ZH-CN_CONCEPT_0209896985)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为17。
- 不允许配置ChargeCharValue和掩码取与操作后的值不等于ChargeCharValue。
- 不允许配置ChargeCharValue和掩码取与后的值，与当前已有配置的ChargeCharValue和对应掩码取与后的值相等。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CHARGECHAR | CHARGECHARVALUE | CCMASK | CCPRIORITY | OFFLINEFLAG |
| --- | --- | --- | --- | --- | --- |
| 初始值 | DEFAULT | 0x0000 | 0xFFFF | 0 | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209896985)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896985)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHARGECHAR | 计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGW计费属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PREPAID：表示要配置计费属性为预付费，对应的特殊CC值为0x0400。<br>- NORMAL：表示要配置计费属性为普通计费，对应的特殊CC值为0x0800。<br>- HOT_BILLING：表示要配置计费属性为热计费，对应的特殊CC值为0x0100。<br>- FLAT_BILLING：表示要配置计费属性为统一费率，对应的特殊CC值为0x0200。<br>- SPECIFIC_VALUE：表示要配置计费属性为特殊CC值。<br>- DEFAULT：表示要配置计费属性为缺省，对应的特殊CC值为0x0000。<br>默认值：无<br>配置原则：无 |
| CHARGECHARVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CHARGECHAR”配置为“SPECIFIC_VALUE”时为必选参数。<br>参数含义：该参数用于指定SGW计费属性值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CCMASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CHARGECHAR”配置为“SPECIFIC_VALUE”时为可选参数。<br>参数含义：该参数用于指定SGW计费属性掩码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| CCPRIORITY | 计费属性优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CHARGECHAR”配置为“SPECIFIC_VALUE”时为可选参数。<br>参数含义：该参数用于指定SGW计费属性优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：配置mask时必须指定优先级。 |
| OFFLINEFLAG | 是否离线计费 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGW计费是否生成离线话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不支持离线计费，不生成离线话单。<br>- ENABLE：支持离线计费，生成离线话单。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896985)

根据需求，设置SGW计费方式，则可以如下配置：

```
SET SGWCHGMETH: CHARGECHAR=PREPAID, OFFLINEFLAG=ENABLE;
```
