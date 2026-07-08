# 删除IMSI和MSISDN号段（RMV PCSCFIMSISDNSEG）

- [命令功能](#ZH-CN_MMLREF_0209651695__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651695__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651695__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651695__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651695)

**适用NF：SMF、PGW-C、GGSN**

该命令用于删除IMSI/MSISDN号码段。

## [注意事项](#ZH-CN_MMLREF_0209651695)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209651695)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651695)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651695)

删除IMSI和MSISDN号段：IMSI/MSISDN号段名称为huawei，命令为：

```
RMV PCSCFIMSISDNSEG:SEGMENTNAME="huawei";
```
