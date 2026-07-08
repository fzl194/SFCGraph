---
id: UNC@20.15.2@MMLCommand@MOD OMNWCONF
type: MMLCommand
name: MOD OMNWCONF（配置OM网络探测参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: OMNWCONF
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 网络管理
status: active
---

# MOD OMNWCONF（配置OM网络探测参数）

## 功能

![](配置OM网络探测参数（MOD OMNWCONF）_58550741.assets/notice_3.0-zh-cn_2.png)

网络探测参数修改可能导致OMLB服务主备倒换，可能 **导致网管或VNFM断链** ；关闭网络探测时，会导致OM网络故障无法检测。

用于配置OM网络故障探测参数。

## 注意事项

- 该命令仅限角色为Administrators的用户执行。
- 请勿将网络亚健康告警阈值设置过低，否则可能会导致[ALM-136001 OM网络资源故障](../../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-136001 OM网络资源故障_54986794.md)告警上报或清除异常。
- 该命令存在系统初始记录，参数的初始设置值如下：
  | IPTYPE | SWITCH | PERIOD | SWITCHTHRESHOLD |
  | --- | --- | --- | --- |
  | VIRTUALIP(浮动IP) | ON(开) | 2 | 3 |
  | IPTYPE | SWITCH | IPADDRTYPE | PERIOD | ALARMTHRESHOLD | SUBHEALTHTHRESHOLD | SUBHEALTHPERIOD |
  | --- | --- | --- | --- | --- | --- | --- |
  | PHYSICALIP(物理IP) | ON(开) | IPV4/IPV6(IPv4/IPv6类型) | 2 | 15 | 5 | 5 |

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数。<br>参数含义：网络探测的IP类型。<br>取值范围：<br>- VIRTUALIP(浮动IP)：登录OM Portal的浮动IP。<br>- PHYSICALIP(物理IP)：服务器的物理IP。<br>默认值：VIRTUALIP(浮动IP)。<br>配置原则：无。 |
| SWITCH | 网络探测开关 | 可选必选说明：必选参数。<br>参数含义：网络探测开关状态。<br>取值范围：<br>- ON(开)。<br>- OFF(关)。<br>默认值：ON(开)。<br>配置原则：无。 |
| IPADDRTYPE | IP地址类型 | 可选必选说明：该参数在“IPTYPE”配置为“PHYSICALIP(物理IP)”时为条件必选参数。<br>参数含义：IP地址类型。<br>取值范围：<br>- IPV4(IPv4类型)。<br>- IPV6(IPv6类型)。<br>- IPV4/IPV6(IPv4/IPv6类型)<br>默认值：IPV4/IPV6(IPv4/IPv6类型)。<br>配置原则：无。 |
| PERIOD | 探测周期（秒） | 可选必选说明：必选参数。<br>参数含义：探测周期，单位秒(s)。<br>取值范围：1~3600。<br>默认值：2。<br>配置原则：无。 |
| SWITCHTHRESHOLD | 倒换阈值 | 可选必选说明：当IP类型为VIRTUALIP(浮动IP)时为必选参数。<br>参数含义：OMLB服务主备倒换的阈值，当网络探测失败次数达到倒换阈值时，主备倒换。<br>取值范围：1~3600。<br>默认值：3。<br>配置原则：无。 |
| ALARMTHRESHOLD | 告警阈值 | 可选必选说明：当IP类型为PHYSICALIP(物理IP)时为必选参数。<br>参数含义：告警阈值，当网络探测失败/成功次数达到告警阈值时，上报/清除<br>[ALM-136001 OM网络资源故障](../../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-136001 OM网络资源故障_54986794.md)<br>告警。<br>取值范围：1~3600。<br>默认值：15。<br>配置原则：无。 |
| SUBHEALTHTHRESHOLD | 网络亚健康告警阈值（%） | 可选必选说明：当IP类型为PHYSICALIP(物理IP)时为可选参数。<br>参数含义：用于指定在<br>“网络亚健康检测周期（分钟）”<br>内，丢包率达到该参数取值时，上报<br>[ALM-136001 OM网络资源故障](../../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-136001 OM网络资源故障_54986794.md)<br>告警。<br>取值范围：2~10。<br>默认值：5。<br>配置原则：无。 |
| SUBHEALTHPERIOD | 网络亚健康检测周期（分钟） | 可选必选说明：当IP类型为PHYSICALIP(物理IP)时为可选参数。<br>参数含义：用于指定执行网络亚健康检测时，统计丢包率的周期。<br>取值范围：5~30。<br>默认值：5。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OMNWCONF]] · OM网络探测参数（OMNWCONF）

## 使用实例

1. 配置浮动IP探测信息：
  ```
  %%MOD OMNWCONF: IPTYPE=VIRTUALIP, SWITCH=ON, PERIOD=10, SWITCHTHRESHOLD=3;%% 
  RETCODE = 0  操作成功  
  ---    END
  ```
2. 配置物理IP探测信息：
  ```
  %%MOD OMNWCONF: IPTYPE=PHYSICALIP, SWITCH=ON, IPADDRTYPE=IPV4/IPV6, PERIOD=2, ALARMTHRESHOLD=15, SUBHEALTHTHRESHOLD=10, SUBHEALTHPERIOD=5;%% 
  RETCODE = 0  操作成功  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-OMNWCONF.md`
