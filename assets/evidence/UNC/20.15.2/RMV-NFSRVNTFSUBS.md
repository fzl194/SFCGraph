# 删除服务回调信息（RMV NFSRVNTFSUBS）

- [命令功能](#ZH-CN_MMLREF_0209654366__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209654366__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209654366__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209654366__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209654366)

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于删除服务实例的回调信息。

## [注意事项](#ZH-CN_MMLREF_0209654366)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209654366)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209654366)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定回调信息对应的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定回调信息对应的服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- 本参数与ADD NFSERVICE命令中的SRVINSTANCEID值一致时生效。<br>- 本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，Service_Instance_0。 |
| NTFICATIONTYPE | 通知类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定回调URI通知类型。<br>数据来源：全网规划<br>取值范围：<br>- NtfInvalid（NtfInvalid）<br>- N1Msg（N1Msg）<br>- N2Info（N2Info）<br>- LocNty（LocNty）<br>- DataRmvNtf（DataRmvNtf）<br>- DataChgNtf（DataChgNtf）<br>- NtfMax（NtfMax）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209654366)

运营商A需要删除NFINSTANCENAME为AMF_Instance_0，SRVINSTANCEID为Service_Instance_0的服务实例下通知类型为N1Msg的回调信息。

```
RMV NFSRVNTFSUBS: NFINSTANCENAME="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0", NTFICATIONTYPE=N1Msg;
```
