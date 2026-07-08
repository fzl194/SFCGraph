---
id: UNC@20.15.2@MMLCommand@DSP CURSMFIEADAPTER
type: MMLCommand
name: DSP CURSMFIEADAPTER（显示SMF当前信元携带的信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CURSMFIEADAPTER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 业务功能灵活控制
- 信元携带策略管理
status: active
---

# DSP CURSMFIEADAPTER（显示SMF当前信元携带的信息）

## 功能

**适用NF：SMF**

该命令用于显示当前SMF在流程中某一协议消息中的信元携带情况。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ITFNODEROLE | 接口和网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的接口和网元类型。<br>数据来源：本端规划<br>取值范围：<br>- “N16_VSMF（N16_VSMF）”：N16接口上本端网元为V-SMF<br>- “N16_HSMF（N16_HSMF）”：N16接口上本端网元为H-SMF<br>- “N16a_ISMF（N16a_ISMF）”：N16a接口上本端网元为I-SMF<br>- “N16a_HSMF（N16a_HSMF）”：N16a接口上本端网元为H-SMF<br>- “N7（N7）”：N7接口<br>- “N40（N40）”：N40接口<br>- “N16_PROXYSMF（N16_PROXYSMF）”：N16接口上本端网元为PROXYSMF<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的流程类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PROCMSGID | 流程消息标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的流程消息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CURSMFIEADAPTER]] · SMF当前信元携带的信息（CURSMFIEADAPTER）

## 使用实例

查询当前VSMF会话创建流程中发送给HSMFN16的创建消息中的信元携带情况，执行如下命令：

```
%%DSP CURSMFIEADAPTER: ITFNODEROLE=N16_VSMF, PROCTYPE="PduSessionEstAsVsmf", PROCMSGID="PostPduSessionsParameters";%%
RETCODE = 0  操作成功

结果如下
------------------------
名称                                                  结果值  

BinaryDatas                                           enable        
PduSessionCreateData                                  enable        
PduSessionCreateData.AddUeLocation                    enable        
PduSessionCreateData.AdditionalAnType                 disable       
PduSessionCreateData.AdditionalCnTunnelInfo           disable       
PduSessionCreateData.AlwaysOnRequested                disable       
PduSessionCreateData.AmfNfId                          enable        
PduSessionCreateData.AnType                           enable        
PduSessionCreateData.ChargingId                       enable        
PduSessionCreateData.DnaiList                         disable       
PduSessionCreateData.Dnn                              enable        
PduSessionCreateData.EpsBearerCtxStatus               disable       
PduSessionCreateData.EpsBearerId                      disable       
PduSessionCreateData.EpsInterworkingInd               enable        
PduSessionCreateData.Gpsi                             enable        
PduSessionCreateData.Guami                            enable        
PduSessionCreateData.HPcfId                           enable        
PduSessionCreateData.HoPreparationIndication          disable       
PduSessionCreateData.HplmnSnssai                      disable       
PduSessionCreateData.ISmfServiceInstanceId            disable       
PduSessionCreateData.IcnTunnelInfo                    disable       
PduSessionCreateData.IsmfId                           disable       
PduSessionCreateData.IsmfPduSessionUri                disable       
PduSessionCreateData.MaxIntegrityProtectedDataRateDl  enable        
PduSessionCreateData.MaxIntegrityProtectedDataRateUl  enable        
PduSessionCreateData.N1SmInfoFromUe                   enable        
PduSessionCreateData.N9ForwardingTunnelInfo           disable       
PduSessionCreateData.OldPduSessionId                  disable       
PduSessionCreateData.PcfId                            disable       
PduSessionCreateData.PduSessionId                     enable        
PduSessionCreateData.Pei                              enable        
PduSessionCreateData.PgwS8CFteid                      disable       
PduSessionCreateData.PresenceInLadn                   enable        
PduSessionCreateData.RatType                          enable        
PduSessionCreateData.RecoveryTime                     disable       
PduSessionCreateData.RequestType                      enable        
PduSessionCreateData.RoamingChargingProfile           enable        
PduSessionCreateData.RoutingIndicator                 enable        
PduSessionCreateData.SNssai                           enable        
PduSessionCreateData.SecondaryRatUsageInfo            disable       
PduSessionCreateData.SelMode                          enable        
PduSessionCreateData.SelectedDnn                      enable        
PduSessionCreateData.ServingNetwork                   enable        
PduSessionCreateData.Supi                             enable        
PduSessionCreateData.SupportedFeatures                enable        
PduSessionCreateData.UdmGroupId                       enable        
PduSessionCreateData.UeLocation                       enable        
PduSessionCreateData.UeTimeZone                       enable        
PduSessionCreateData.UnauthenticatedSupi              enable        
PduSessionCreateData.UnknownN1SmInfo                  disable       
PduSessionCreateData.UpSecurityInfo                   disable       
PduSessionCreateData.VSmfServiceInstanceId            disable       
PduSessionCreateData.VcnTunnelInfo                    enable        
PduSessionCreateData.VplmnQos                         enable        
PduSessionCreateData.VsmfId                           enable        
PduSessionCreateData.VsmfPduSessionUri                enable        
(结果个数 = 56)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SMF当前信元携带的信息（DSP-CURSMFIEADAPTER）_57616489.md`
