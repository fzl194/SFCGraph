# 增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）

- [命令功能](#ZH-CN_MMLREF_0209652612__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652612__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652612__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652612__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652612)

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置的对端NF实例支持的服务实例回调信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## [注意事项](#ZH-CN_MMLREF_0209652612)

- 该命令执行后立即生效。

- 最多可输入1024条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209652612)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652612)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |
| NTFICATIONTYPE | 回调URI通知类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定回调URI通知类型。<br>数据来源：全网规划<br>取值范围：<br>- “NtfTypeINVALID（NtfTypeINVALID）”：NtfTypeINVALID<br>- “N1Msg（N1Msg）”：N1Msg<br>- “N2Info（N2Info）”：N2Info<br>- “LocNty（Loc_Nty）”：Loc_Nty<br>- “DataRmvNtf（DataRmvNtf）”：DataRmvNtf<br>- “DataChgNtf（DataChgNtf）”：DataChgNtf<br>- “NtfTypeMAX（NtfTypeMAX）”：NtfTypeMAX<br>默认值：无<br>配置原则：无 |
| CALLBACKURI | 回调URI | 可选必选说明：可选参数<br>参数含义：该参数用于指定回调URI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| N1MESSAGECLASS | N1消息类别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N1消息类别。<br>数据来源：全网规划<br>取值范围：<br>- “EN1MsgINVALID（EN1MsgINVALID）”：EN1MsgINVALID<br>- “N1Mm（N1Mm）”：N1Mm<br>- “N1Sm（N1Sm）”：N1Sm<br>- “Lpp（Lpp）”：Lpp<br>- “Sms（Sms）”：Sms<br>- “N1Updp（N1Updp）”：N1Updp<br>- “N1Reserved1（N1Reserved1）”：N1Reserved1<br>- “EN1MsgMAX（EN1MsgMAX）”：EN1MsgMAX<br>- “Lcs（Lcs）”：Lcs<br>默认值：无<br>配置原则：无 |
| N2INFOCLASS | N2消息类别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2消息类别。<br>数据来源：全网规划<br>取值范围：<br>- “EN2MsgINVALID（EN2MsgINVALID）”：EN2MsgINVALID<br>- “N2Sm（N2Sm）”：N2Sm<br>- “Nrppa（Nrppa）”：Nrppa<br>- “Pws（Pws）”：Pws<br>- “PwsBcal（PwsBcal）”：PwsBcal<br>- “PwsRf（PwsRf）”：PwsRf<br>- “N2Ran（N2Ran）”：N2Ran<br>- “N2Reserved1（N2Reserved1）”：N2Reserved1<br>- “EN2MsgMAX（EN2MsgMAX）”：EN2MsgMAX<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652612)

增加对端NF的服务实例回调信息，NF实例标识为AMF_Instance_1，服务实例标识为Service_Instance_0，通知类型为N1Msg，回调URI为"http://192.168.217.1:5080/ngmlc-loc/hgmlc/v1/provide-location"。

```
ADD PNFSRVNTFSUBS: NFINSTANCEID="AMF_Instance_1", SRVINSTANCEID="Service_Instance_0", NTFICATIONTYPE=N1Msg, CALLBACKURI="http://192.168.217.1:5080/ngmlc-loc/hgmlc/v1/provide-location", N1MESSAGECLASS=N1Mm;
```
