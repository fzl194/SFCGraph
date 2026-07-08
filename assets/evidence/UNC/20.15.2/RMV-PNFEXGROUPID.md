# 删除对端NF的外部群组信息（RMV PNFEXGROUPID）

- [命令功能](#ZH-CN_MMLREF_0209652500__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652500__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652500__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652500__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652500)

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于删除本地配置的对端NF实例支持的外部群组标识的信息。

## [注意事项](#ZH-CN_MMLREF_0209652500)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652500)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652500)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。不区分大小写。<br>默认值：无<br>配置原则：<br>建议本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致。 |
| EXGROUPID | 外部群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定外部组标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652500)

删除对端NF的外部群组信息，对端NF实例标识为UDM_Instance_0上，支持外部群组标识为externalGroupId01。

```
RMV PNFEXGROUPID: NFINSTANCEID="UDM_Instance_0", EXGROUPID="externalGroupId01";
```
