# 删除NF服务版本信息（RMV NFSERVICEVER）

- [命令功能](#ZH-CN_MMLREF_0209652116__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652116__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652116__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652116__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652116)

**适用NF：AMF、SMF、NSSF、NRF、SMSF、NCG**

该命令用于删除NF服务实例下的版本信息。当服务实例不再支持某个版本时，需要对版本信息进行删除。

## [注意事项](#ZH-CN_MMLREF_0209652116)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652116)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652116)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NFS实例所归属的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NFS实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数与ADD NFSERVICE命令中的SRVINSTANCEID值一致时生效。 |
| APIFULLVERSION | API版本信息 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NFS的全量版本信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- 本参数的构成字符建议是字母A～Z或a～z、数字0～9、点“.”、加号“+”，和中划线“-”，例如1.0.0，1.0.0-alpha.1，3.0.1+orange.2020-09。<br>- 此参数点分格式的第一段即为注册到NRF的API缩略版本信息，即例如此参数为1.0.0，则API缩略版本信息为v1。 |

## [使用实例](#ZH-CN_MMLREF_0209652116)

运营商A需要在NFINSTANCENAME为AMF_Instance_0,SRVINSTANCEID为Service_Instance_0的服务实例下删除1.0.0版本号。

```
RMV NFSERVICEVER:NFINSTANCENAME="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0", APIFULLVERSION="1.0.0";
```
