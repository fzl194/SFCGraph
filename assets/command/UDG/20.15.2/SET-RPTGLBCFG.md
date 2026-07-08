---
id: UDG@20.15.2@MMLCommand@SET RPTGLBCFG
type: MMLCommand
name: SET RPTGLBCFG（设置报表功能全局开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RPTGLBCFG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 业务报表管理
- 报表功能管理
- 报表全局开关
status: active
---

# SET RPTGLBCFG（设置报表功能全局开关）

## 功能

**适用NF：PGW-U、UPF**

![](设置报表功能全局开关（SET RPTGLBCFG）_93753143.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

此命令用于设置业务报表全局开关，包括业务报表总开关、DNS业务分析上报开关、TCP业务分析上报开关、UDP业务分析上报开关等。当运营商部署业务报表业务时使用该命令。

## 注意事项

- 该命令配置后对新业务数据流和已经建立的业务数据流均生效。
- 该命令最大记录数为1。
- 全局业务报表上报开关配置修改后，60s后仅对之后发生承载更新的用户或者新激活用户生效。
- DNS业务分析上报开关配置修改后，60s后仅对之后发生承载更新的用户或者新激活用户生效。
- TCP业务分析上报开关配置修改后，60s后仅对之后发生承载更新的用户或者新激活用户生效。
- UDP业务分析上报开关配置修改后，60s后仅对之后发生承载更新的用户或者新激活用户生效。
- SIP上报开关配置修改后，60s后仅对之后发生承载更新的用户或者新激活用户生效。
- VoLTE/VoNR语音质量分析上报开关配置修改后，60s后仅对之后发生承载更新的用户或者新激活用户生效。
- 有License控制的报表功能，还需要使用SET LICENSESWITCH使能对应功能。
- 同时开启用户更新消息触发UFDR_FlowStats开关和对端设备信令地址更新触发UFDR_UserInfo开关，SGSN-IP更新才能触发UFDR_FlowStats上报。
- 该命令会导致用户匹配数发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | GLOBALSWITCH | DNSINSIGHTSW | TCPINSIGHTSW | UDPINSIGHTSW | SUBSPOLICYSW | SUBSCONFIGSW | CACHESW | SIGUFDRSW | SIGADCHGRPTSW | SIPINSIGHTSW | VOLTEINSIGHTSW | VONRINSIGHTSW | USRGRPCTRLINFO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALSWITCH | 全局业务报表上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置全局是否上报业务报表，仅用于控制UFDR上报。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| DNSINSIGHTSW | DNS业务分析上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置全局是否使能对DNS业务分析上报的功能。如果使能DNS业务分析上报功能，系统针对DNS协议支持上报包括服务器地址在内的详细参数，并支持通过Grp接口上报到PRS进行DNS业务分析关联报表分析。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| TCPINSIGHTSW | TCP业务分析上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置全局是否使能TCP传输层质量分析上报的功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| UDPINSIGHTSW | UDP业务分析上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置全局是否使能UDP传输层质量分析上报的功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| SUBSPOLICYSW | 订阅策略开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持订阅接口下发业务订阅策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| SUBSCONFIGSW | 配置策略开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持订阅接口下发业务配置策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| CACHESW | 缓存开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否支持在报表服务器故障场景下在本地缓存单据。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| SIGUFDRSW | 用户更新消息触发UFDR_FlowStats开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置用户更新信令消息是否触发UFDR_FlowStats上报。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| SIGADCHGRPTSW | 对端设备信令地址更新触发UFDR_UserInfo开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置对端设备信令地址更新是否触发UFDR用户单据上报。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：该参数仅在SET RPTGLBPARA命令SIGADDR参数设置为SMF_N4_SGSN时生效。 |
| SIPINSIGHTSW | SIP上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置SIP上报开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| VOLTEINSIGHTSW | VoLTE语音质量分析上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VoLTE语音质量分析上报开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| VONRINSIGHTSW | VoNR语音质量分析上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VoNR语音质量分析上报开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| USRGRPCTRLINFO | 用户组级带宽控制器信息上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否使能用户组级带宽控制器信息上报的功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTGLBCFG]] · 业务报表全局开关（RPTGLBCFG）

## 使用实例

使能TCP业务分析上报开关：

```
SET RPTGLBCFG:TCPINSIGHTSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置报表功能全局开关（SET-RPTGLBCFG）_93753143.md`
