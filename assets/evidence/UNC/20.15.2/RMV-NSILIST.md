# 删除NF支持切片信息（RMV NSILIST）

- [命令功能](#ZH-CN_MMLREF_0209651541__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651541__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651541__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651541__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651541)

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于删除NF实例支持的网络切片实例标识。

## [注意事项](#ZH-CN_MMLREF_0209651541)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209651541)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651541)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| NSI | 网络切片实例标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定网络切片实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，NS_Instance_0。 |

## [使用实例](#ZH-CN_MMLREF_0209651541)

运营商A需要在NFINSTANCENAME为AMF_Instance_0的NF实例下删除网络切片实例NS_Instance_0。

```
RMV NSILIST: NFINSTANCENAME="AMF_Instance_0", NSI="NS_Instance_0";
```
