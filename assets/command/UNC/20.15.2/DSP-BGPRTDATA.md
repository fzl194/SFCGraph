---
id: UNC@20.15.2@MMLCommand@DSP BGPRTDATA
type: MMLCommand
name: DSP BGPRTDATA（查询BGP路由数据结构信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BGPRTDATA
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP路由数据结构信息
status: active
---

# DSP BGPRTDATA（查询BGP路由数据结构信息）

## 功能

该命令用于显示BGP路由数据结构信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | BGP地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>默认值：ipv4uni |
| IPV4ADDR | BGP IPv4地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| MASK | 掩码长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| UPGINDEX | BGP打包组索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP打包组索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：通过display bgp update-peer-group命令可以查询BGP打包组索引。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPRTDATA]] · BGP路由数据结构信息（BGPRTDATA）

## 使用实例

显示BGP路由数据结构信息：

```
DSP BGPRTDATA:IPV4ADDR="10.1.1.1";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
BGP数据信息  =
 BGP local router ID : 10.1.1.21
 Local AS number : 100

 Route Head Information:
 RtEntryCount = 1
 RefCount = 1
 BitSetForSuppressRt = 0
 AppliedLabel = 4294967295
 InTobeUpdateCount = 0
 AdvSuppCount = 0
 AdvSuppFlagFst = 0
 AdvSuppFlagSec: 0
 InTobeUpdSllFst = 0
 InTobeUpdSllSec: 0
 RthUpgFlags = 0
 LblRiboutCount = 0
 RtHeadFlags = 0

 BGP routing table entry information of 10.1.1.1/32:
 Imported route.
 From: 0.0.0.0 (0.0.0.0)
, origin incomplete, MED 0, pref-val 0, valid, local, best, select, pre 60

 Route Entry Information:
 RtEntryFlags = 540016648
 ExtraFlags = 4
 AttrChangeFlags = 0
 TimeStamp = 80932
 ReceivedLabel = 4294967295
 Version = 2
 WorseReason = 0

 Public Attribute Information:
 Refcount = 1
 PrefVal = 0
 Preference = 60
 LocalPathID = 255
 RecvPathID = 0

 Attribute Information:
 AttributeFlag = 262159
 AttrID = 16777217
 RtRefCount = 1
 ActiveRtRefCount = 1
 BestRtRefCount = 1
 TotalRefCount = 1
 RtAdvRefCount = 0
 VpnroRibOutFst = 0
 VpnroRibOutSec: 0
 AttrStRibOutFst = 0
 AttrStRibOutSec: 0
 AttrUpgFlags = 0

 Nexthop Information:
 TotalRef = 2
 Type = 2
 RelayStatus = 65536
 DeleteStatus = true
 Version = 0

 RouteQuery Info:
 RtqBestRtRef = 1
 RtqActiveRtRef = 1
 RtqRtRef = 1
 RtqTotalRef = 1
 RtqQueryType = 5
 RtqRelayStatus = 65537
 RtqFlag = 268435456

 IIDInfo:
 RtqIIDInfoFlag = 1
 qr_qry_fsm_state = 0
 RtqIIDCBIID = 1828716976
 RtqIIDCBType = 0
 RtqStIIDUpgFlg = 268435456
 RtqStIIDRef = 0

 RelayInfo:
 qr_qry_fsm_state = 0
 RtqCost = 0
 RtqRelayNum = 1
 RtqIterDepth = 0
 RtqDest = 0
 RtqMask = 0

（结果个数 = 1）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BGPRTDATA.md`
