# 增加融合计费Proxy基于CC处理动作（ADD CCPCCACT）

- [命令功能](#ZH-CN_MMLREF_0245110906__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0245110906__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0245110906__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0245110906__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0245110906)

**适用NF：NCG**

该命令用于增加融合计费Proxy基于CC的处理动作。

## [注意事项](#ZH-CN_MMLREF_0245110906)

- 该命令执行后立即生效。

- 最多可输入101条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0245110906)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0245110906)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTYPE | CC类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CC的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的CC设置处理动作）<br>- VALUE（针对CC设置处理动作）<br>默认值：无<br>配置原则：无 |
| CHGCHAR | 指定计费属性值 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定计费属性的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~6。十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CHGCHARMASK | 指定计费属性掩码 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于指定计费属性的掩码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~6。十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：0xFFFF<br>配置原则：无 |
| FWDOCSENABLE | 是否转发OCS | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否转发OCS。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| FOTNM | Failover模板标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费Proxy Failover模板的名称，FOTNM参数来源是ADD CCPFOT:FOTNM。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| GENCHGDATAREF | 是否生成计费数据标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否生成数据计费标识(ChargingDataRef)。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：FALSE<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0245110906)

增加指定计费属性值为“0x1234”的融合计费Proxy基于CC处理动作：

```
ADD CCPCCACT: CCTYPE=VALUE, CHGCHAR="0x1234", FWDOCSENABLE=TRUE, FOTNM="ccpfot1", GENCHGDATAREF=FALSE;
```
