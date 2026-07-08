---
id: UNC@20.15.2@MMLCommand@LST PFCPPVTEXT
type: MMLCommand
name: LST PFCPPVTEXT（查询PFCP私有信元携带配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PFCPPVTEXT
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP私有信元管理
status: active
---

# LST PFCPPVTEXT（查询PFCP私有信元携带配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询PFCP私有信元携带配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FEATURE | 特性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定特性名称。<br>数据来源：本端规划<br>取值范围：<br>- “QER_TYPE（QER类型）”：QER类型区分功能。功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息的Create QER/Update QER信元中允许携带QER Type字段。功能关闭时，不允许携带QER Type字段。<br>- “BWM（带宽控制）”：带宽控制功能。功能开启时，在PFCP Session Establishment/Modification Request消息的Create QER/Update QER信元中通过Non Control Flag字段指示是否进行带宽控制。功能关闭时，按照TS 3GPP 29.244协议标准定义，通过带宽信息（MBR/GBR）指示是否进行带宽控制。<br>- “UPA（用户面分配UE IP地址）”：用户面分配UE IP地址功能。功能开启时，在PFCP Session Establishment/Modification Request消息的UE IP address信元通过私有的方式指示用户面分配UE IP地址。功能关闭时，按照TS 3GPP 29.244-g20协议版本标准定义，通过UE IP Address中CHV6/CHV4标志来控制用户面分配UE IP地址。<br>- “SESSION_ROLE_TYPE（网元形态的流量、会话等KPI指标统计）”：网元形态的流量、会话等KPI指标统计。功能开启的时候，在PFCP Session Establishment/Modification Request消息中的私有信元SessionRoleType携带用户角色信息用于网元形态的流量、会话等KPI指标统计。<br>- “DNAI（指示U面区分主锚点会话和辅锚点会话）”：功能开启的时候，在PFCP Session Establishment Request消息中的携带私有信元DNAI用于区分主锚点会话和辅锚点会话。<br>- “QCI（QoS类别标识）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息的Create QER/Update QER信元中允许携带QCI字段。功能关闭时，不允许携带QCI字段。<br>- “ARP（分配保留优先级）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息的Create QER/Update QER信元中允许携带ARP字段。功能关闭时，不允许携带ARP字段。<br>- “URR_CHARGING_TYPE（URR计费类型）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息的Create URR/Update URR信元中允许携带urrcharingtype字段。功能关闭时，不允许携带urrcharingtype字段。<br>- “RG（费率组）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息的Create URR/Update URR信元中允许携带RG字段。功能关闭时，不允许携带RG字段。<br>- “SID（业务标识）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息的Create URR/Update URR信元中允许携带SID字段。功能关闭时，不允许携带SID字段。<br>- “HW_EVENT_MEASUREMENT（华为事件计量）”：在PFCP Session Establishment Request/PFCP Session Modification Request消息的Create URR/Update URR信元中允许携带HW Event Measurement字段。功能关闭时，不允许携带HW Event Measurement字段。<br>- “S_NSSAI（网络切片选择辅助信息）”：功能开启时，PFCP Session Establishment Request消息中S-NSSAI使用协议标准的信元。功能关闭时，使用华为私有信元。<br>- “SELF_SEID（本端N4会话标识）”：功能开启时，会话上下文核查的PFCP Session Modification Request消息携带私有信元SelfSeid，功能关闭时，不携带私有信元SelfSeid。<br>- “SGW_STATE_INFO（SGW状态信息）”：功能开启时，PFCP Association Update Request消息携带私有信元SGW State Info，功能关闭时，不携带私有信元SGW State Info。<br>- “NGLAN（5G LAN）”：功能开启时，PFCP Session Establishment Request消息携带私有信元5GLan Session Type和5G VN Instance。功能关闭时，不携带私有信元5GLan Session Type和5G VN Instance。<br>- “L2TP_TNL（L2TP隧道信息）”：功能开启时，在PFCP Session Establishment Request消息中允许携带L2TpTunnelInfo字段。功能关闭时，按照TS 3GPP 29.244-h30协议版本标准定义，通过L2TP Tunnel Information携带L2TP隧道信息。<br>- “L2TP_PCO（L2TP用户PCO信息）”：功能开启时，在PFCP Session Establishment Request消息中允许携带L2TpPco字段。功能关闭时，按照TS 3GPP 29.244-h30协议版本标准定义，通过L2TP Session Information携带L2TP用户PCO信息。<br>- “MultiDNN_Type（双DNN特性会话类型）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息携带私有信元MultiDNN Session Type。功能关闭时，不携带上述私有信元。<br>- “MultiDNN_DNN（双DNN特性专用DNN会话DNN ）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息PDR IE中携带私有信元Multi DNN。功能关闭时，不携带上述私有信元。<br>- “MultiDNN_Snssai（双DNN特性专用DNN会话的切片）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息PDR IE中携带私有信元Snssai。功能关闭时，不携带上述私有信元。<br>- “MultiDNN_IP_Address（双DNN特性普通DNN会话和专用DNN会话的IP地址）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息携带私有信元MultiDNN IP Address。功能关闭时，不携带上述私有信元。<br>- “MultiDNN_Rat_Type（双DNN特性专用I-UPF左侧接入类型）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息PDR IE中携带私有信元MultiDNN Rat Type。功能关闭时，不携带上述私有信元。<br>- “MultiDNN_DNS_Filter（双DNN特性园区域名信息）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息PDR IE中携带私有信元MultiDNN DNS Filter。功能关闭时，不携带上述私有信元。<br>- “MultiDNN_Filter_Indication（双DNN特性园区域名或IP复用指示）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息PDR IE中携带私有信元MultiDNNFilterIndication。功能关闭时，不携带上述私有信元。<br>- “URR_PERF_TYPE（URR话统类型）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息的Create URR/Update URR信元中允许携带URR Perf Type字段。功能关闭时，不允许携带URR Perf Type字段。<br>- “AUTH_CLASS（鉴权类型）”：功能开启时，在PFCP Session Establishment Request消息携带私有信元AuthClass。功能关闭时，不携带上述私有信元。<br>- “CHARGING_TYPE（计费类型）”：功能开启时，在PFCP Session Establishment Request消息携带私有信元ChargingType。功能关闭时，不携带上述私有信元。<br>- “Qos_Analysis（指示SRR中下发QoS Analysis Information）”：功能开启时，在PFCP Session Modification Request消息SRR IE中携带私有信元QoS Analysis Information。功能关闭时，不携带上述私有信元。<br>- “EXTEND_ROAMING_TYPE（拓展漫游类型）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元Extend Roaming Type。功能关闭时，不携带上述私有信元。<br>- “EXTEND_PROXY_TYPE（拓展代理类型）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元Extend Proxy Type。功能关闭时，不携带上述私有信元。<br>- “Session_Delete_Cause（N4会话删除原因）”：指示UPF是否释放家庭组内的IKE会话。功能开启时，在PFCP Session Deletion Request消息中携带私有信元SessionDeleteCause。功能关闭时，不携带上述私有信元。<br>- “Qos_Experience（指示SRR中下发QoS Experience Information）”：功能开启时，在PFCP Session Modification Request消息SRR IE中携带私有信元QoS Experience Information。功能关闭时，不携带上述私有信元。<br>- “Feature_Rule（业务规则）”：功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。功能关闭时，不携带上述私有信元。<br>- “Qos_Quality_Indicate（质差检测标识）”：功能开启时，在PFCP Session Modification Request消息中的CreateSRR和UpdateSRR携带私有信元QosQualityIndicate。功能关闭时，不携带上述私有信元。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PFCPPVTEXT]] · PFCP私有信元携带配置（PFCPPVTEXT）

## 使用实例

查询PFCP私有信元携带配置： LST PFCPPVTEXT:;

```
%%LST PFCPPVTEXT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
特性名称                           私有信元携带开关  

QER类型                            不使能                    
带宽控制                           使能                     
用户面分配UE IP地址                使能                     
网元形态的流量、会话等KPI指标统计  使能
指示U面区分主锚点会话和辅锚点会话  使能
QOS类别标识                        使能
分配保留优先级                     使能
URR计费类型                        使能
费率组                             使能
业务标识                           使能
华为事件计量                       使能
SGW状态信息                        不使能
(结果个数 = 12)

---  END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PFCPPVTEXT.md`
