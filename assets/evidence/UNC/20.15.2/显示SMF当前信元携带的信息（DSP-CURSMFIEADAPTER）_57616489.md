# 显示SMF当前信元携带的信息（DSP CURSMFIEADAPTER）

- [命令功能](#ZH-CN_MMLREF_0000001357616489__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001357616489__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001357616489__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001357616489__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001357616489__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001357616489)

**适用NF：SMF**

该命令用于显示当前SMF在流程中某一协议消息中的信元携带情况。

## [注意事项](#ZH-CN_MMLREF_0000001357616489)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001357616489)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001357616489)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ITFNODEROLE | 接口和网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的接口和网元类型。<br>数据来源：本端规划<br>取值范围：<br>- “N16_VSMF（N16_VSMF）”：N16接口上本端网元为V-SMF<br>- “N16_HSMF（N16_HSMF）”：N16接口上本端网元为H-SMF<br>- “N16a_ISMF（N16a_ISMF）”：N16a接口上本端网元为I-SMF<br>- “N16a_HSMF（N16a_HSMF）”：N16a接口上本端网元为H-SMF<br>- “N7（N7）”：N7接口<br>- “N40（N40）”：N40接口<br>- “N16_PROXYSMF（N16_PROXYSMF）”：N16接口上本端网元为PROXYSMF<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的流程类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PROCMSGID | 流程消息标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的流程消息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001357616489)

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

## [输出结果说明](#ZH-CN_MMLREF_0000001357616489)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 名称 | 查询结果名称。 |
| 结果值 | 查询的结果值。 |
