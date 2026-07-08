# 查询BGP对等体日志信息（DSP BGPPEERLOG）

- [命令功能](#ZH-CN_CONCEPT_0000001600840825__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600840825__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600840825__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600840825__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600840825__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600840825__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600840825)

该命令用于显示BGP对等体的日志信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600840825)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600840825)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600840825)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| ADDRESSTYPE | 地址类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4。<br>- ipv6：IPv6。<br>默认值：无 |
| REMOTEADDRESSV4 | 对等体IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn” 或 “ipv6vpn”时为必选参数。<br>参数含义：该参数用于给定对等体IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| REMOTEADDRESSV6 | 对等体IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为必选参数。<br>参数含义：该参数用于给定对等体IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| VERBOSE | 是否输出详细信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否输出详细信息。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| SOURCEIFNAME | 多源接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于给定多源对等体的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：仅支持Ethernet及其子接口类型，不区分大小写。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600840825)

显示BGP对等体日志信息：

```
DSP BGPPEERLOG:AFTYPE=ipv4uni,REMOTEADDRESSV4="192.168.7.1",VERBOSE=TRUE;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
BGP对等体日志信息  =

Peer : 192.168.7.1

Date/Time     : 2016-07-01 03:49:46
State         : Up

Date/Time     : 2016-07-01 03:49:36
State         : Down
Error Code    : 5(Finite State Machine Error)
Error Subcode : 0(UnSpecific)
Notification  : Receive Tcp Fail

Date/Time     : 2016-06-30 13:38:05
State         : Up

Date/Time     : 2016-06-30 13:37:06
State         : Down
Error Code    : 6(CEASE)
Error Subcode : 6(Other Configuration Change)
Notification  : Send Notification

Date/Time     : 2016-06-30 13:23:05
State         : Up
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600840825)

| 输出项名称 | 输出项解释 |
| --- | --- |
| BGP对等体日志信息 | 用于输出BGP对等体日志信息。 |
