---
id: UNC@20.15.2@MMLCommand@SET TRC_CFG
type: MMLCommand
name: SET TRC_CFG（设置跟踪参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TRC_CFG
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 跟踪配置管理
- 跟踪参数管理
status: active
---

# SET TRC_CFG（设置跟踪参数）

## 功能

**适用网元：SGSN、MME**

该命令用于设置GB、GB NS接口跟踪、随机用户跟踪和用户跟踪参数。用户跟踪表示跟踪以IMSI（International Mobile Subscriber Identity）或MSISDN（Mobile Station International ISDN Number）为标识的特定用户消息；随机用户跟踪表示基于设置的条件，随机性的选择满足触发条件的任何用户并上报其用户跟踪；接口跟踪表示跟踪接口的消息。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 执行该命令后，需要删除原来已经创建的用户跟踪和GB、GB NS接口跟踪，然后重新创建对应的跟踪，修改才能生效。
- 设置GB、GB NS接口跟踪为不允许时，将无法创建对应的接口跟踪。
- 设置随机用户跟踪为不允许时，将无法创建随机用户跟踪。
- 设置用户跟踪消息类型或方向为不允许时，用户跟踪任务仍然能够创建，但是不能跟踪到相应消息类型或方向的用户跟踪消息。

## 权限

manage-ug
G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRCTP | 跟踪类型 | 可选必选说明：必选参数<br>参数含义：该参数用来确定需要设置的跟踪类型。<br>数据来源：本端规划。<br>取值范围：<br>- “INTERFACE(接口跟踪任务)”<br>- “USER(用户跟踪任务)”<br>- “RANDOM_USER(随机用户跟踪任务)”<br>系统初始设置值：无 |
| GBFLG | 是否允许GB接口跟踪 | 可选必选说明：条件可选参数<br>参数含义：该参数用来指定是否允许创建GB接口跟踪。GB接口跟踪用于查看指定NSE（Network Service Entity）号码或小区号码的GB接口的SIG（信令）管理消息或DATA（数据）消息。<br>前提条件：该参数在<br>“跟踪类型”<br>设置为<br>“INTERFACE(接口跟踪任务)”<br>时有效。<br>数据来源：本端规划。<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：无 |
| GBNSFLG | 是否允许GB NS接口跟踪 | 可选必选说明：条件可选参数<br>参数含义：该参数用来确定是否允许创建GB NS接口跟踪。此跟踪用于查看GB接口NS层信令消息。<br>前提条件：该参数在<br>“跟踪类型”<br>设置为<br>“INTERFACE(接口跟踪任务)”<br>时有效。<br>数据来源：本端规划。<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：无 |
| MSGT | 允许的用户跟踪消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用来确定允许那些消息类型。<br>前提条件：该参数在<br>“跟踪类型”<br>设置为<br>“USER(用户跟踪任务)”<br>时有效。<br>数据来源：本端规划。<br>取值范围：<br>- “DIAMETER(DIAMETER消息)”<br>- “S1AP(S1AP消息)”<br>- “SS(Iu/Gb接口SS消息)”<br>- “MM(S1/Iu/Gb/Gn/Gp接口MM消息)”<br>- “SM(S1/Iu/Gb/Gn/Gp接口SM消息)”<br>- “SMS(Iu/Gb接口SMS消息)”<br>- “BSSAP+(Gs/Gd/Gr接口BSSAP+消息)”<br>- “MAP(Gs/Gd/Gr接口MAP消息)”<br>- “CAP(Ge接口CAP消息)”<br>- “LCS(LCS消息)”<br>- “RANAP(Iu接口RANAP消息)”<br>- “SCCP(Iu接口SCCP消息)”<br>- “LLC(Gb接口LLC消息)”<br>- “PTP(Gb接口PTP消息)”<br>- “SNDCP(Gb接口SNDCP消息)”<br>- “GTPU(Gn/Gp接口GTPU消息)”<br>系统初始设置值：全部选中 |
| DRCT | 允许的用户跟踪消息方向 | 可选必选说明：条件可选参数<br>参数含义：该参数用来确定用户跟踪中被允许的GTPU消息。<br>前提条件：该参数在<br>“跟踪类型”<br>设置为<br>“USER(用户跟踪任务)”<br>时有效。<br>数据来源：本端规划。<br>取值范围：<br>- “INPUT(入口)”：跟踪通过GTPU接口收到的消息。<br>- “OUTPUT(出口)”：跟踪通过GTPU接口发出的消息。<br>系统初始设置值：全部选中 |
| MSGLEN | GTPU消息长度 | 可选必选说明：条件可选参数<br>参数含义：用户跟踪GTPU数据净荷部分的长度由默认上报长度和可配置长度两部分组成。本参数用来约束可配置长度部分，单位为字节。默认上报长度根据净荷部分的数据协议类型，区分TCPIP报文和非TCPIP报文。<br>- TCPIP报文默认上报TCP和IP头长度。<br>- 非TCPIP报文默认上报40字节。<br>前提条件：该参数在<br>“跟踪类型”<br>设置为<br>“USER(用户跟踪任务)”<br>时有效。<br>数据来源：本端规划。<br>取值范围： 0~300<br>系统初始设置值：0 |
| CTRLFLG | 是否允许随机用户跟踪 | 可选必选说明：条件可选参数<br>参数含义：该参数用来确定是否允许创建随机用户跟踪。此跟踪基于设置的条件，随机性的选择满足触发条件的任何用户并上报其用户跟踪。<br>前提条件：该参数在<br>“跟踪类型”<br>设置为<br>“RANDOM_USER(随机用户跟踪任务)”<br>时有效。<br>数据来源：本端规划。<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：<br>“YES(是)” |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRC_CFG]] · 跟踪参数（TRC_CFG）

## 使用实例

1. 设置跟踪参数，跟踪类型为INTERFACE(接口跟踪任务)，不允许创建GB接口跟踪：
  SET TRC_CFG: TRCTP=INTERFACE, GBFLG=NO;
2. 设置跟踪参数，跟踪类型为USER(用户跟踪任务)，不允许跟踪Iu/Gb接口SS消息、S1/Iu/Gb/Gn/Gp接口MM消息，不允许跟踪GTPU出口消息：
  SET TRC_CFG: TRCTP=USER, MSGT=SS-0&MM-0, DRCT=OUTPUT-0;
3. 设置跟踪参数，跟踪类型为RANDOM_USER(随机用户跟踪任务)，不允许创随机用户跟踪：
  SET TRC_CFG: TRCTP=RANDOM_USER, CTRLFLG=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-TRC_CFG.md`
