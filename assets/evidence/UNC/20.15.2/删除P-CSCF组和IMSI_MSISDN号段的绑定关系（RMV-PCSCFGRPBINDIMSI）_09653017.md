# 删除P-CSCF组和IMSI/MSISDN号段的绑定关系（RMV PCSCFGRPBINDIMSI）

- [命令功能](#ZH-CN_MMLREF_0209653017__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653017__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653017__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653017__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653017)

**适用NF：SMF、GGSN、PGW-C**

该命令用于删除UNC设备p-cscf组与IMSI/MSISDN号段的绑定关系。在需要把p-cscf组与新的号段绑定时，需要先执行该命令删除P-CSCF组和原有的IMSI/MSISDN号段的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0209653017)

- 该命令执行后立即生效。

- 当UNC上没有用户的情况下删除P-CSCF组和IMSI/MSISDN号段的绑定关系。

#### [操作用户权限](#ZH-CN_MMLREF_0209653017)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653017)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于号段名称。指定某号段绑定到p-cscf组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFIMSISDNSEG命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0209653017)

在需要把p-cscf组与新的号段绑定时，需要先执行该命令删除P-CSCF组和原有的IMSI/MSISDN号段的绑定关系。举例：号段名称为myseg：

```
RMV PCSCFGRPBINDIMSI:IMSIMSISDNSEG="myseg";
```
