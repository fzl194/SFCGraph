---
id: UNC@20.15.2@MMLCommand@DSP BGPPEERSTATE
type: MMLCommand
name: DSP BGPPEERSTATE（查询BGP对等体状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BGPPEERSTATE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP对等体状态信息
status: active
---

# DSP BGPPEERSTATE（查询BGP对等体状态信息）

## 功能

该命令用于显示BGP对等体的状态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| ADDRESSTYPE | 地址类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4。<br>- ipv6：IPv6。<br>默认值：无 |
| REMOTEADDRESSV4 | 对等体IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn” 或 “ipv6vpn”时为必选参数。<br>参数含义：该参数用于给定对等体IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| REMOTEADDRESSV6 | 对等体IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为必选参数。<br>参数含义：该参数用于给定对等体IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| SOURCEIFNAME | 多源接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于给定多源对等体的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：仅支持Ethernet及其子接口类型，不区分大小写。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPPEERSTATE]] · BGP对等体状态信息（BGPPEERSTATE）

## 使用实例

显示BGP对等体状态信息：

```
DSP BGPPEERSTATE:VRFNAME="vpna",AFTYPE=ipv4uni,REMOTEADDRESSV4="10.1.1.1";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
BGP对等体状态信息  =
Last   Read     : -----
Last   Write    : -----
Last Try Connect: 2016-07-02 07:23:14
Last Try Create Connect Fail Reason: BNM_FAIL_SYNCHRONIZE_VRF_CFG
Last Peer Down Reason: 4
Last Recv Msg Time: -----
Last Send Msg Time: -----
BFD State: 0, BFD PrevState: 0, BFD Fsm Event: 0
BFD State: 0, BFD PrevState: 0, BFD Fsm Event: 0

Event Timers:
TimerID          Name        Type         Mode         TimerLeft(ms)     Expire
Times
0                CRTimer     CYCLIC       IDLE         -----             0

0                KATimer     CYCLIC       IDLE         -----             0

0                HLTimer     CYCLIC       IDLE         -----             0

139807697692080  IHTimer     CYCLIC       RUNNING      9000              7

0                DOTimer     CYCLIC       IDLE         -----             0

Out interface(4294967295) current state: 0
                     Listen SOCKET       Main SOCKET         Second SOCKET

Socket ID:           2                   -1                  0

Option Flag:         0                   0                   0

Current State:       2                   0                   0

Prev State:          2                   0                   0

Fsm Event:           53                  52                  0

Out Pipe(id/state): (4294967295/0)      (4294967295/0)      (0/0)
In Pipe(id/state):  (4294967295/0)      (4294967295/0)      (0/0)
InBD State:          3                   0                   0

OutBD State:         3                   0                   0

BD Require:          false               false               false

Congestion Flag:     0                   0                   0

Congestion Times:    0                   0                   0

Close Flag:          0                   0                   0

             LastCreateFail             LastNotifyError             LastCreateSeqError             LastCloseSocketSeqError
Socket ID:   -1                         -1                          -1                             -1
Error Code:  0                          0                           0                              0
Occur Time:  -----                      -----                       -----                          -----

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BGPPEERSTATE.md`
