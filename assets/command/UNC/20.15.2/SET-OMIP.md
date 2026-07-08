---
id: UNC@20.15.2@MMLCommand@SET OMIP
type: MMLCommand
name: SET OMIP（设置OM IP）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OMIP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# SET OMIP（设置OM IP）

## 功能

![](设置OM IP (SET OMIP)_76163350.assets/notice_3.0-zh-cn_2.png)

该类命令执行之后 **可能会导致OM Portal断链** 、网管断链以及VNFM断链，需使用修改后IP重新登录OM Portal，并重新对接网管以及修改VNFM侧对应网元的IP。该命令若执行不当， **会导致所有业务中断** 。

用于修改系统OM网络配置参数，包括外部浮动IP地址、外部物理IP、子网掩码（IPV4场景）/前缀长度（IPV6场景）、默认网关。

## 注意事项

- 该命令仅限角色为Administrators的用户执行。
- 执行该命令修改浮动IP时，请参考网元的改造OM网络方案改造OM网络。
- 执行该命令设置物理IP时，如果系统已预置物理IP，会删除系统预置的物理IP。如需保留系统预置的物理IP，请先执行[LST OMIP](查询OM IP (LST OMIP)_76163349.md)查询，在执行该命令设置IP时，同时添加系统预置的物理IP。在双栈场景，如果系统预置地址的IP版本与需新设置地址的IP版本不同，需要分别执行该命令设置。
- 执行该命令删除物理IP时，如果当前系统没有已配置的物理IP，系统将自动添加预置的物理IP。
- 当系统回退到低版本时，若需要修改浮动IP地址，需要在回退前执行SET OMIP删除手动配置的物理IP地址。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OMIPTYPE | IP版本 | 可选必选说明：可选参数<br>参数含义：浮动IP类型<br>取值范围：<br>- IPV4(IPv4版本)<br>- IPV6(IPv6版本)<br>默认值：IPV4(IPv4版本)<br>配置原则：无 |
| OMSETTYPE | IP设置类型 | 可选必选说明：当IP版本为IPV4时，此为可选参数。<br>参数含义：用于指定IPV4设置的类型。<br>取值范围：<br>- SET_IP(设置IP)<br>- DELETE_FLOAT_IP(删除浮动IP)<br>- DELETE_PHYSICAL_IP(删除物理IP)<br>默认值：SET_IP(设置IP)<br>配置原则：无 |
| OMSETTYPE1 | IP设置类型 | 可选必选说明：当IP版本为IPV6时，此为可选参数。<br>参数含义：用于指定IPV6设置的类型。<br>取值范围：<br>- SET_IP(设置IP)<br>- DELETE_FLOAT_IP(删除浮动IP)<br>- DELETE_PHYSICAL_IP(删除物理IP)<br>默认值：SET_IP(设置IP)<br>配置原则：无 |
| OMFIPADDR | 浮动IP地址 | 可选必选说明：该参数在“IP版本”配置为“IPV4(IPv4版本)”且“IP设置类型”配置为“SET_IP(设置IP)”时为可选参数。<br>参数含义：IPv4地址<br>取值范围：有效的IPv4地址<br>默认值：无<br>配置原则：无 |
| OMNETMASK | 子网掩码 | 可选必选说明：该参数在“IP版本”配置为“IPV4(IPv4版本)”且“IP设置类型”配置为“SET_IP(设置IP)”时为可选参数。<br>参数含义：IPv4子网掩码<br>取值范围：有效的IPv4子网掩码<br>默认值：无<br>配置原则：无 |
| OMIPV4GATEWAY | 默认网关 | 可选必选说明：该参数在“IP版本”配置为“IPV4(IPv4版本)”且“IP设置类型”配置为“SET_IP(设置IP)”时为可选参数。<br>参数含义：IPv4 默认网关<br>取值范围：有效的IPv4默认网关<br>默认值：无<br>配置原则：无 |
| OMFIPV6ADDR | 浮动IP地址 | 可选必选说明：该参数在“IP版本”配置为“IPV6(IPv6版本)”且“IP设置类型”配置为“SET_IP(设置IP)”时为可选参数。<br>参数含义：IPv6地址<br>取值范围：有效的IPv6地址<br>默认值：无<br>配置原则：无 |
| OMIPV6PREFIX | 前缀长度 | 可选必选说明：该参数在“IP版本”配置为“IPV6(IPv6版本)”且“IP设置类型”配置为“SET_IP(设置IP)”时为可选参数。<br>参数含义：IPv6 前缀<br>取值范围：有效的IPv6前缀<br>默认值：无<br>配置原则：无 |
| OMIPV6GATEWAY | 默认网关 | 可选必选说明：当IP版本为IPv6时，当IP设置类型为SET_IP时，此为可选参数<br>参数含义：IPv6默认网关<br>取值范围：有效的IPv6默认网关<br>默认值：无<br>配置原则：无 |
| OMHOST1IPV4 | 物理IP1 | 可选必选说明：当IP版本为IPv4时，当IP设置类型为SET_IP时，此为可选参数<br>参数含义：物理IPv4地址<br>取值范围：有效的物理IPv4地址<br>默认值：无<br>配置原则：物理IP地址需要与浮动IP地址在同一网段。 |
| OMHOST2IPV4 | 物理IP2 | 可选必选说明：当IP版本为IPv4时，当IP设置类型为SET_IP时，此为可选参数<br>参数含义：物理IPv4地址2<br>取值范围：有效的物理IPv4地址2<br>默认值：无<br>配置原则：物理IP地址需要与浮动IP地址在同一网段。 |
| OMHOST1IPV6 | 物理IP1 | 可选必选说明：当IP版本为IPv6时，当IP设置类型为SET_IP时，此为可选参数<br>参数含义：物理IPv6地址<br>取值范围：有效的物理IPv6地址<br>默认值：无<br>配置原则：物理IP地址需要与浮动IP地址在同一网段。 |
| OMHOST2IPV6 | 物理IP2 | 可选必选说明：当IP版本为IPv6时，当IP设置类型为SET_IP时，此为可选参数<br>参数含义：物理IPv6地址2<br>取值范围：有效的物理IPv6地址2<br>默认值：无<br>配置原则：物理IP地址需要与浮动IP地址在同一网段。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OMIP]] · OM IP（OMIP）

## 使用实例

1. 设置物理IP信息：
  ```
  %%SET OMIP: OMIPTYPE=IPV6, OMSETTYPE1=SET_IP, OMFIPV6ADDR="2001:db8:0000:4202:0156:0110:0202:0510", OMHOST2IPV6="2001:db8:0:4202:156:110:202:192";%% 
  RETCODE = 0  操作成功
  ---    END
  ```
2. 删除物理IP信息：
  ```
  %%SET OMIP: OMIPTYPE=IPV4, OMSETTYPE=DELETE_PHYSICAL_IP;%% 
  RETCODE = 0  操作成功
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-OMIP.md`
