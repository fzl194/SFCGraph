# 修改话单通道一级目录映射表（MOD AGFCDRCHLMAP）

- [命令功能](#ZH-CN_MMLREF_0000001224616033__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001224616033__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001224616033__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001224616033__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001224616033)

**适用NF：NCG**

该命令用于修改OCS NFINSTANCEID与话单通道一级目录映射关系。

## [注意事项](#ZH-CN_MMLREF_0000001224616033)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001224616033)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001224616033)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | OCS的NFINSTANCEID值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS的NFINSTANCEID值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。NFINSTANCEID必须来源于PNFPROFILE命令中NFINSTANCEID参数。<br>默认值：无<br>配置原则：无 |
| FIELDTYPE | 决定话单通道分拣的字段 | 可选必选说明：可选参数<br>参数含义：该参数用于指定决定话单分拣的字段。<br>数据来源：本端规划<br>取值范围：<br>- SUPI_GPSI（SUPI或GPSI）<br>- APN（APN）<br>默认值：无<br>配置原则：无 |
| CDRFIRSTDIR | 话单通道一级目录名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定话单一级目录名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~30。当FIELDTYPE取值为SUPI_GPSI时，CDRFIRSTDIR只能填00~31通道名。当FIELDTYPE取值为APN时，CDRFIRSTDIR只能填JASPER、IOT、DEFAULT通道。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001224616033)

修改NFINSTANCEID为"00000000-0000-0000-c000-000000000046"的话单通道一级目录映射关系：

```
MOD AGFCDRCHLMAP: NFINSTANCEID="00000000-0000-0000-c000-000000000046", FIELDTYPE=SUPI_GPSI, CDRFIRSTDIR ="02";
```
