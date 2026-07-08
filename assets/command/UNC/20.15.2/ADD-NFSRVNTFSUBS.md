---
id: UNC@20.15.2@MMLCommand@ADD NFSRVNTFSUBS
type: MMLCommand
name: ADD NFSRVNTFSUBS（添加服务回调信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFSRVNTFSUBS
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF服务订阅管理
status: active
---

# ADD NFSRVNTFSUBS（添加服务回调信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于添加服务实例回调信息。在NF向NRF注册时，可以针对NF支持的每个服务实例提供默认的通知注册信息（defaultNotificationSubscription），供NF服务生产者向未在NF服务生产者中显式注册的NF服务消费者提供回调URI（Uniform Resource Identifier，通用资源标识符）信息。例如，作为隐式订阅的解决。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定回调信息对应的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定回调信息对应的服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- 本参数与ADD NFSERVICE命令中的SRVINSTANCEID值一致时生效。<br>- 本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，Service_Instance_0。 |
| NTFICATIONTYPE | 通知类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定回调URI通知类型。<br>数据来源：全网规划<br>取值范围：<br>- NtfInvalid（NtfInvalid）<br>- N1Msg（N1Msg）<br>- N2Info（N2Info）<br>- LocNty（LocNty）<br>- DataRmvNtf（DataRmvNtf）<br>- DataChgNtf（DataChgNtf）<br>- NtfMax（NtfMax）<br>默认值：无<br>配置原则：无 |
| CALLBACKURI | 回调URI | 可选必选说明：可选参数<br>参数含义：除AMF回调URI由系统自动生成，其余网元可用此参数指定回调URI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：<br>优先使用ipv4地址，格式为URI格式，例如：http://192.168.0.1:80/callbackFunc。 |
| N1MESSAGECLASS | N1消息类别 | 可选必选说明：可选参数<br>参数含义：本参数用于指定N1消息类别。<br>数据来源：全网规划<br>取值范围：<br>- EN1Invalid（EN1Invalid）<br>- N1Mm（N1Mm）<br>- N1Sm（N1Sm）<br>- Lpp（Lpp）<br>- Sms（Sms）<br>- N1Updp（N1Updp）<br>- N1Reserved1（N1Reserved1）<br>- EN1Max（EN1Max）<br>默认值：无<br>配置原则：无 |
| N2INFOCLASS | N2消息类别 | 可选必选说明：可选参数<br>参数含义：本参数用于指定N2消息类别。<br>数据来源：全网规划<br>取值范围：<br>- EN2Invalid（EN2Invalid）<br>- N2Sm（N2Sm）<br>- Nrppa（Nrppa）<br>- Pws（Pws）<br>- PwsBcal（PwsBcal）<br>- PwsRf（PwsRf）<br>- N2Ran（N2Ran）<br>- N2Reserved1（N2Reserved1）<br>- EN2Max（EN2Max）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFSRVNTFSUBS]] · 服务回调信息（NFSRVNTFSUBS）

## 使用实例

运营商A需要给NFINSTANCENAME为AMF_Instance_0，SRVINSTANCEID为Service_Instance_0的服务实例添加回调信息，通知类型为N1Msg，回调URI为http://192.168.0.1:80/callbackFunc。

```
ADD NFSRVNTFSUBS: NFINSTANCENAME="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0", NTFICATIONTYPE=N1Msg, CALLBACKURI="http://192.168.0.1:80/callbackFunc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NFSRVNTFSUBS.md`
