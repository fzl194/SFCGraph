---
id: UNC@20.15.2@MMLCommand@DSP BGPPEERVERBOSE
type: MMLCommand
name: DSP BGPPEERVERBOSE（查询BGP对等体详细信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BGPPEERVERBOSE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP对等体详细信息
status: active
---

# DSP BGPPEERVERBOSE（查询BGP对等体详细信息）

## 功能

该命令用于显示BGP对等体的详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| ADDRESSTYPE | 地址类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为可选参数。<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4。<br>- ipv6：IPv6。<br>默认值：无 |
| REMOTEADDRESSV4 | 对等体IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为可选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于给定对等体IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| REMOTEADDRESSV6 | 对等体IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为可选参数。<br>参数含义：该参数用于给定对等体IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| SOURCEIFNAME | 多源接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于给定多源对等体的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：仅支持Ethernet及其子接口类型，不区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BGPPEERVERBOSE]] · BGP对等体详细信息（BGPPEERVERBOSE）

## 使用实例

显示BGP对等体详细信息：

```
DSP BGPPEERVERBOSE:VRFNAME="vpna",AFTYPE=ipv4uni,REMOTEADDRESSV4="10.1.1.1";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
BGP对等体详细信息  =
         BGP Peer is 10.1.1.1,  remote AS 100
         Type: IBGP link
         BGP version 4, Remote router ID 0.0.0.0
         Update-group ID: 3
         BGP current state: Idle
         BGP current event: IHTimerExpired
         BGP last state: Idle
         BGP Peer Up count: 0
         Configured: Connect-retry Time: 32 sec
Received: Total 0  messages
                  Update messages               0
                  Open messages                 0
                  KeepAlive messages            0
                  Notification messages         0
                  Refresh messages              0
Sent: Total 0  messages
                  Update messages               0
                  Open messages                 0
                  KeepAlive messages            0
                  Notification messages         0
                  Refresh messages              0
Authentication type configured: None
No keepalive received since peer has been configured
No keepalive sent since peer has been configured
No update received since peer has been configured
No update sent since peer has been configured
No refresh received since peer has been configured
No refresh sent since peer has been configured
Minimum route advertisement interval is  15seconds
Optional capabilities:
Route refresh capability has been enabled
4-byte-as capability has been enabled
Peer Preferred Value: 0
Routing policy configured:
No routing policy is configured

(结果个数 = 1)
 ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BGP对等体详细信息（DSP-BGPPEERVERBOSE）_50280714.md`
