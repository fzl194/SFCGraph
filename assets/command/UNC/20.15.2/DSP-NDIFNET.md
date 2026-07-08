---
id: UNC@20.15.2@MMLCommand@DSP NDIFNET
type: MMLCommand
name: DSP NDIFNET（查询使能IPv6接口ND控制块内容）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NDIFNET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- ND
status: active
---

# DSP NDIFNET（查询使能IPv6接口ND控制块内容）

## 功能

该命令用于查询使能了IPv6的接口的ND控制块内容。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFQUERYTYPE | 查询接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定接口查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IFINDEX：接口索引。<br>- IFNAME：接口名称。<br>默认值：无 |
| IFINDEX | 接口索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IFQUERYTYPE”配置为“IFINDEX”时为必选参数。<br>参数含义：该参数用来指定接口索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967294。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IFQUERYTYPE”配置为“IFNAME”时为必选参数。<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NDIFNET]] · 使能IPv6接口ND控制块内容（NDIFNET）

## 使用实例

查询使能了IPv6的接口的ND控制块内容：

```
DSP NDIFNET: IFQUERYTYPE=IFNAME, IFNAME="LoopBack1";
```

```

RETCODE = 0  操作成功。

结果如下
--------
查询接口控制块的具体内容  =    ND_IFNET:
    IfIndex        : 16
    PID            : 0x73003B
    IfGroupID      : 7
    RouteTypeFlag  : 1
    BeginVlanid    : 0
    EndVlanid      : 0
    VrIndex        : 0
    VrfIndex       : 0
    Mtu            : 1500
    IfPhyType      : 19
    MainIfPhyType  : 19
    LinkFlag       : 1
    IfPhyState     : 1
    Loopback       : 0
    RouteType      : 0
    HaveLinkLocal  : 1
    IPv6EnableFlag : 1
    IfIsSubif      : 0
    IfIP6CPState   : 0
    IfLinkType     : 255
    CollectedFlag  : 1
    IntfUpflag     : 0
    MacAddr        : 00E0-FCA1-0200
    LinkLocalExist : 1
    WorkIfIndex    : 0
    VlanId         : 0
    IfEncapType    : 255
    SubIfVlanType  : 0
    NsMcastFlag    : 0
    IntfOnOffState : 1
    LastAlarmTime  : 0
    DycmicNBlimit  : 0
  NdCB:
    LinkLocalAddr         : FE80::512B:94C5:B34:FCB4
    DADNum                : 0
    DadAttempts           : 1
    InterfaceState        : 1
    InterfaceReachableTime: 1200000
    LastTimeNaSentTime    : 0
    NSInterval            : 1000
    StaleTimeout          : 0
    TotalEntryNum         : 0
    StaticEntryNum        : 0
    DynamicEntryNum       : 0
  LinkLocalAddr:
    Addr: FE80::512B:94C5:B34:FCB4  Status:[OK]  Length:10 Type:0 Origin:0 HaveSendPrefix:0
              uiDADAttempts:0, uiExpire:0
  GlobalAddr:
    Addr: 2001:db8::11  Status:[OK]  Length:11 Type:1 Origin:0 HaveSendPrefix:1
              uiDADAttempts:0, uiExpire:0
  GlobalCGAAddr:
  RAInfo:
    MFlag          : 0
    OFlag          : 0
    RtLifetimeFlag : 1
    SendRAFlag     : 0
    IfHopLimit     : 64
    MinConfig      : 0
    DstAddr        : ::0
    IPv6AddrDel    : ::0
    IPv6AddrAdd    : FE80::512B:94C5:B34:FCB4
    IfHopLmtCfgFlag: 0
    SendRANum      : 0
    Rtlifetime     : 1800
    Reachable      : 0
    Retrans        : 0
    RaIntervalMax  : 600
    RaIntervalMin  : 200
    LastSendTime   : 0
    Time           : 0
    FinalRa        : 0
    UnicastAddr    : ::0
    SendUnicastRA  : 0
    NextMcastRATime: 0
    RouterPrefer   : 0
    CarryPrefixFlag: 1
    CarryMtuFlag   : 1

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询使能IPv6接口ND控制块内容（DSP-NDIFNET）_00600869.md`
