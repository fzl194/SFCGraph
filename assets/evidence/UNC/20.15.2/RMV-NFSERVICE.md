# 删除NF服务实例（RMV NFSERVICE）

- [命令功能](#ZH-CN_MMLREF_0209652678__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652678__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652678__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652678__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652678)

![](删除NF服务实例（RMV NFSERVICE）_09652678.assets/notice_3.0-zh-cn_2.png)

该命令用于删除NF的服务实例，该命令执行以后，对应的服务功能删除，无法对外提供对应的服务，可能业务无法正常触发，请谨慎操作。

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于在NF实例下删除服务实例信息。

## [注意事项](#ZH-CN_MMLREF_0209652678)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652678)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652678)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NFS实例所归属的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>本参数来源于ADD NFUUID命令中的“NF实例名称”参数。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NFS实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线“-”和下划线“_”，例如，Service_Instance_0。 |

## [使用实例](#ZH-CN_MMLREF_0209652678)

运营商A需要删除NF实例名称为SMF_Instance_0，服务实例标识为Service_Instance_0的服务实例。

```
RMV NFSERVICE: NFINSTANCENAME="SMF_Instance_0", SRVINSTANCEID="Service_Instance_0";
```
