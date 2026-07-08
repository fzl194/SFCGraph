---
id: UNC@20.15.2@MMLCommand@DSP WLRBLACKBOX
type: MMLCommand
name: DSP WLRBLACKBOX（显示无线路由黑匣子信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRBLACKBOX
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由全局信息
status: active
---

# DSP WLRBLACKBOX（显示无线路由黑匣子信息）

## 功能

该命令用于显示无线路由黑匣子信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| BOXID | 黑匣子ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定黑匣子ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：<br>- 当前黑匣子ID：- 组件级黑匣子，黑匣子ID：1。<br>- 组件API调用失败信息，黑匣子ID：2。<br>- 组件收到错误消息，黑匣子ID：3。<br>- 组件内警告信息，黑匣子ID：4。<br>- 消息重传信息，黑匣子ID：5。<br>- MPF发送PAEG信息，黑匣子ID：6。<br>- FEI通知PAE信息，黑匣子ID：7。<br>- 发给MPF的订阅更新信息，黑匣子ID：8。<br>- MPF发送路由前缀信息，黑匣子ID：9。<br>- 路由前缀老化信息，黑匣子ID：10。<br>- PAEG老化信息，黑匣子ID：11。<br>- Peer表项状态机信息，黑匣子ID：12。<br>- WLRv6向WLRv4订阅PAEG，黑匣子ID：13。<br>- FES组件partner状态信息，黑匣子ID：14。<br>- 与FES收发消息，黑匣子ID：15。<br>- 与FES更新引流表信息，黑匣子ID：16。<br>- 与FES更新PAE信息，黑匣子ID：17。<br>- 引流表组更新信息，黑匣子ID：18。<br>- 引流表老化信息，黑匣子ID：19。<br>- Diameter组件partner状态信息，黑匣子ID：20。<br>- 与RM更新路由前缀信息，黑匣子ID：21。<br>- RM组件partner状态信息，黑匣子ID：22。<br>- 下发信令无线路由信息，黑匣子ID：23。 |

## 操作的配置对象

- [无线路由黑匣子信息（WLRBLACKBOX）](configobject/UNC/20.15.2/WLRBLACKBOX.md)

## 使用实例

显示无线路由黑匣子信息：

```
DSP WLRBLACKBOX: AFTYPE=ipv4unicast,BOXID=1;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  黑匣子ID  =  1
黑匣子消息  =  <0000>1230-155618 Patch Fun When Patch DeActive
<0001>1230-155618 Patch Fun When Patch DeActive Again
<0002>1230-155618 Patch Fun When Patch Active
<0003>1230-155618 Patch Fun When Patch Active Again
<0004>1230-155618 ComFSM:(0)0->(1)1
<0005>1230-155618 DelayTime:30000
<0006>1230-155618 max prefix limit value:1000000
<0007>1230-155618 ComFSM:(1)1->(1)6
<0008>1230-155618 ComFSM:(1)2->(3)2
<0009>1230-155618 Partner(113,pid=0x714659) status:1->0
<000A>1230-155618 Partner(121,pid=0x7903f8) status:1->1
<000B>1230-155618 Partner(475,pid=0x1db4652) status:1->1
<000C>1230-155618 Partner(475,pid=0x1db4652) status:1->0
<000D>1230-155618 RmFSM:(0)0->(1)1
<000E>1230-155618 RmFSM:(1)1->(2)2
<0010>1230-155618 RmFSM:(2)2->(3)3
<0011>1230-155618 RmFSM:(3)3->(4)4
<0013>1230-155619 Partner(121,pid=0x7903f8) status:1->0
<0014>1230-155622 GresmFSM(IID):(0)0->(1)1
<0015>1230-155622 GRESM: smooth begin(restype:0)
<0016>1230-155622 GresmFSM(IID):(1)1->(2)2
<0017>1230-155622 GresmFSM(IID):(2)4->(3)5
<0018>1230-155622 GresmFSM(IID):(3)5->(4)6
<0019>1230-155622 GRESM: smooth end(0)
<001A>1230-155637 new backup(81da0448)
<001B>1230-155637 MbFSM:(0)0->(1)1
<001C>1230-155637 MbFSM:(1)1->(2)2
<001D>1230-155637 MbFSM:(2)2->(3)3
<001E>1230-155637 MbIIDFSM:(0)0->(1)1
<001F>1230-155637 MbIFFSM:(0)0->(1)1
<0020>1230-155637 MbRouteFSM:(0)0->(1)1
<0021>1230-155637 MbIIDFSM:(1)1->(2)2
<0022>1230-155637 MbIIDFSM:(2)2->(3)3
<0023>1230-155637 MbIFFSM:(1)1->(2)2
<0024>1230-155637 MbRouteFSM:(1)1->(2)2
<0025>1230-155637 MbIIDFSM:(3)3->(4)4
<0026>1230-155637 MbIFFSM:(2)2->(3)3
<0027>1230-155637 MbRouteFSM:(2)2->(3)3
<0028>1230-155637 MbIFFSM:(3)3->(4)4
<0029>1230-155637 MbRouteFSM:(3)3->(4)4
<002A>1230-155637 MbFSM:(3)4->(4)5
<002B>1230-155637 MbFSM:(4)5->(5)6
<002C>1230-155653 Partner(127,pid=0x7f4661) status:1->0
<002D>1230-155658 Partner(127,pid=0x7f4666) status:1->0
<002E>1230-155702 PAE->MPF DelayTime:30000
<002F>1230-155708 PAE->MPF DelayTime:30000

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示无线路由黑匣子信息（DSP-WLRBLACKBOX）_50281226.md`
