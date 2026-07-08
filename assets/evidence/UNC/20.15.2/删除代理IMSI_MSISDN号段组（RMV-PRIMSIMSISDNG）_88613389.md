# 删除代理IMSI/MSISDN号段组（RMV PRIMSIMSISDNG）

- [命令功能](#ZH-CN_MMLREF_0000001188613389__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001188613389__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001188613389__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001188613389__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001188613389)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除代理IMSI/MSISDN号段组。

## [注意事项](#ZH-CN_MMLREF_0000001188613389)

- 该命令执行后立即生效。

- 当不输入SEGMENTNAME时，表示解除该号段组与所有号段的绑定信息。

#### [操作用户权限](#ZH-CN_MMLREF_0000001188613389)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001188613389)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGGROUPNAME | IMSI/MSISDN号段组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。取值范围：字符串类型，输入长度范围为1～31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。字符串类型，输入长度范围为1～31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PRIMSIMSISDNSEG命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0000001188613389)

- 删除“IMSI/MSISDN号段组名称”为“grp1”，“IMSI/MSISDN号段名称”为“imsi1”的代理IMSI/MSISDN号段组配置：
  ```
  RMV PRIMSIMSISDNG: SEGGROUPNAME="grp1", SEGMENTNAME="imsi1";
  ```
- 删除“IMSI/MSISDN号段组名称”为“grp1”的全部代理IMSI/MSISDN号段组配置：
  ```
  RMV PRIMSIMSISDNG: SEGGROUPNAME="grp1";
  ```
