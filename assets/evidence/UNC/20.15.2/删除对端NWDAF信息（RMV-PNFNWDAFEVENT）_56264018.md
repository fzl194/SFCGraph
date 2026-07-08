# 删除对端NWDAF信息（RMV PNFNWDAFEVENT）

- [命令功能](#ZH-CN_MMLREF_0000002056264018__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002056264018__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002056264018__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002056264018__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000002056264018)

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于删除本地配置的对端NWDAF的信息。

## [注意事项](#ZH-CN_MMLREF_0000002056264018)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000002056264018)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002056264018)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一指定某一个NWDAF实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~38。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，NWDAF_Instance_0。<br>默认值：无<br>配置原则：无 |
| NWDAFINFOID | NwdafInfo标识 | 可选必选说明：可选参数<br>参数含义：该参数用于唯一标识NWDAF实例中的某个NwdafInfo。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000002056264018)

删除对端NWDAF信息，NF实例标识为NWDAF_Instance_1，NwdafInfo标识为central。

```
RMV PNFNWDAFEVENT: NFINSTANCEID="NWDAF_Instance_1", NWDAFINFOID="central";
```
