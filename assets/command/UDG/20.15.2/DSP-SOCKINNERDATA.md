---
id: UDG@20.15.2@MMLCommand@DSP SOCKINNERDATA
type: MMLCommand
name: DSP SOCKINNERDATA（查询SOCK诊断信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SOCKINNERDATA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- SOCKET
status: active
---

# DSP SOCKINNERDATA（查询SOCK诊断信息）

## 功能

该命令用于查询SOCK诊断信息。

指定查询类型为APP_BLACK_BOX时，CID为必选参数。指定查询类型为INSTANCE_TRACE时，CID为可选参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 内部数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定内部数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INSTANCE_TRACE：Socket实例轨迹。<br>- APP_BLACK_BOX：APP黑匣子信息。<br>默认值：无 |
| SOCKID | Socket实例ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“INSTANCE_TRACE”时为必选参数。<br>参数含义：该参数用来指定Socket实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0～4294967295。<br>默认值：无 |
| CID | Socket组件CID | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“APP_BLACK_BOX”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“INSTANCE_TRACE”时为可选参数。<br>参数含义：该参数用来指定Socket组件CID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [SOCK诊断信息（SOCKINNERDATA）](configobject/UDG/20.15.2/SOCKINNERDATA.md)

## 使用实例

- 查询Socket实例轨迹诊断信息：
  ```
  DSP SOCKINNERDATA: TYPE=INSTANCE_TRACE, SOCKID=5, CID="0x8065000B";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据  =  BasicInfo:
            Family: IPv4  Proto: TCP   SockCid: 8065008B  AppCid: 80930095  SocketId: 5
          InstTrace:
            create time     2017-06-01 12:16:39
            apply path      2017-06-01 12:16:39
            path active     2017-06-01 12:16:39
            established     2017-06-01 12:16:39
            pub session     2017-06-01 12:16:39
            session done    2017-06-01 12:16:39
            notify accept   2017-06-01 12:16:39
            app accepted    2017-06-01 12:16:39

            ConnectionState: ESTABLISHED
          PacketInfo:
            First FromAPP:  12:16:39  First ToLDM:  12:16:39
            First FromLDM:  12:16:39  First ToAPP:  12:16:39
            Last  FromApp:  16:35:10  Last  ToLDM:  16:35:10
            Last  FromLDM:  16:35:10  Last  ToApp:  16:35:10
            Last  ToSlave:  00:00:00
            CongCnt: 0, DeCongCnt: 0, LastCong: 00:00:00
            MBUF_DESTROY_LABEL_0[0]
            MBUF_DESTROY_LABEL_0[0]
            MBUF_DESTROY_LABEL_0[0]
            Last MBUF_DESTROY_LABEL_0 Time: 0-00-00 00:00:00
            ReTransmissionCounts: 0
          ErrorCode:
            NotifyErrCode   : 255     LastPathReason: 0

          (结果个数 = 1)
          ---    END
  ```
- 查询APP实例黑匣子诊断信息：
  ```
  DSP SOCKINNERDATA: TYPE=APP_BLACK_BOX, CID="0x80650007";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据  =  App common info :
              AppCid:0x80260009  SockCid:0x80650007   Sub:SUBSCRIBE AVAILABLE   State:Sock App Fsm Standalone
              HaType:PENDING     HaMode:PENDING_MODE  RejCon:0    TcpToken(num/renew):50/0
              WaitBB:0     InBB:0       RcvBD:0    SndBD:0
              PktRecv:0    PktSend:0    SendFail:0
              MsgStat: CreateReq:0       DupHandle:0       CreateAck:0
                       CreateNotify:0    CreateReject:0    StateInvalid:0    CreateReqInBb:0
          First send packets :
              No data.
          First receive packets :
              No data.
          Last message :
              No data.
          Error message :
              No data.
          Dropped send packets :
              No data.
          Dropped receive packets :
              No data.

          (结果个数 = 1)
          ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SOCK诊断信息（DSP-SOCKINNERDATA）_50121446.md`
