# 删除定位服务权限配置（RMV LCSPERMITCFG）

- [命令功能](#ZH-CN_MMLREF_0000001218115686__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001218115686__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001218115686__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001218115686__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001218115686)

**适用NF：AMF**

该命令用于删除定位服务权限配置。

## [注意事项](#ZH-CN_MMLREF_0000001218115686)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001218115686)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001218115686)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 定位服务操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定定位服务的服务操作类型。<br>数据来源：全网规划<br>取值范围：<br>- “Namf_Location_ProvidePositioningInfo（请求UE地理位置信息）”：NF服务消费者（例如GMLC）调用此服务请求UE地理位置信息。<br>- “Namf_Location_ProvideLocationInfo（请求网络侧提供UE位置信息）”：NF服务消费者（例如UDM）调用此服务请求网络侧提供UE位置信息。<br>- “Namf_Location_EventNotify（位置事件通知）”：用于通知NF服务消费者（例如GMLC）关于与紧急业务或延迟定位等UE位置相关的事件信息。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定定位服务消费者的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPTypeV4（IPTypeV4）”：IPv4<br>- “IPTypeV6（IPTypeV6）”：IPv6<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定定位服务消费者的IPV4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0表示无效值。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定定位服务消费者的IPV6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。0:0:0:0:0:0:0:0表示无效值。<br>默认值：无<br>配置原则：无 |
| USRGRPID | 用户群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：<br>该用户群标识必须已经通过ADD NGUSRGRP命令添加成功，可执行LST NGUSRGRP进行查看，用户群中的用户可通过ADD NGUSRGRPMEM添加。 |

## [使用实例](#ZH-CN_MMLREF_0000001218115686)

删除定位服务操作为Namf_Location_ProvidePositioningInfo，IPV4地址为“10.10.10.10”，用户群组标识为1的权限配置，执行如下命令：

```
RMV LCSPERMITCFG: OPTYPE=Namf_Location_ProvidePositioningInfo, IPTYPE=IPTypeV4, IPV4ADDRESS="10.10.10.10", USRGRPID=1;
```
