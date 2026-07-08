# 修改AMF N8接口兼容性策略（MOD AMFN8CMPTPLCY）

- [命令功能](#ZH-CN_MMLREF_0000001589742609__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001589742609__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001589742609__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001589742609__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001589742609)

**适用NF：AMF**

该命令用于对指定的用户（群）修改AMF N8接口兼容性策略。

## [注意事项](#ZH-CN_MMLREF_0000001589742609)

下一次移动性流程生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001589742609)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001589742609)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用N8接口兼容性策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户。<br>- “HOME_USER（本网用户）”：本网用户。<br>- “FOREIGN_USER（外网用户）”：外网用户。<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀。<br>- “SPECIFIC_IMSI（指定IMSI）”：指定IMSI。<br>默认值：无<br>配置原则：<br>对于指定的用户（群），N8接口兼容性策略的匹配优先级从高到低依次为：“SPECIFIC_IMSI(指定IMSI)”，“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用N8接口兼容性策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~14。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件必选参数。<br>参数含义：该参数用于指定应用N8接口兼容性策略的用户的IMSI（完整IMSI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| REDCAPRAT | 是否支持RedCap RAT | 可选必选说明：可选参数<br>参数含义：该参数用于指定N8接口是否支持携带NR_REDCAP作为RatType。RedCap用户接入AMF，当本参数设置为“YES（是）”时，AMF和UDM交互的服务化请求消息中携带NR_REDCAP作为RatType，否则携带NR作为RatType。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：<br>本参数与SET AMFREDCAPFUNC命令RATCMPTSW参数均可对N8接口的RatType信元进行兼容性控制。AMF会首先匹配本命令的配置记录，若发现AMF中不存在或不匹配本命令的配置记录，才会匹配SET AMFREDCAPFUNC命令的配置记录。 |
| GMLCSW | 是否携带V-GMLC地址 | 可选必选说明：可选参数<br>参数含义：该参数用于控制漫游用户通过AMF向UDM注册时是否携带V-GMLC地址。<br>当本参数设置为“YES（是）”时，AMF向UDM发送Nudm_UEContextManagement_Registration请求消息时携带vgmlcAddress信元，当网络侧需要向漫游用户发起定位时，H-GMLC从UDM获取到V-GMLC地址后，通过V-GMLC向用户所在的AMF发起定位流程，从而获得用户位置。该功能仅针对漫游用户生效，本网用户不生效。<br>ADD AMFN8CMPTPLCY命令的GMLCSW参数开关优先级高于SET AMFROAMFUNC命令的VGMLCSW参数开关。优先按照号段匹配ADD AMFN8CMPTPLCY命令的GMLCSW参数开关，匹配到则按照ADD AMFN8CMPTPLCY命令的GMLCSW参数开关进行控制，匹配不到则按SET AMFROAMFUNC命令的VGMLCSW参数开关进行控制。<br>漫游用户选择V-GMLC时使用的客户端类型，可以通过SET AMFROAMFUNC中的VGMLCCTYPE设置。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：<br>当网络侧需要对漫游用户定位，且H-GMLC不支持服务发现获取V-GMLC地址时，推荐本参数设置为"YES"。 |

## [使用实例](#ZH-CN_MMLREF_0000001589742609)

修改外网用户的N8接口兼容性策略为支持携带NR_REDCAP作为RatType，执行如下命令：

```
MOD AMFN8CMPTPLCY:SUBRANGE=FOREIGN_USER,REDCAPRAT=YES;
```
