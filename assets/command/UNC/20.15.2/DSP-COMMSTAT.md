---
id: UNC@20.15.2@MMLCommand@DSP COMMSTAT
type: MMLCommand
name: DSP COMMSTAT（显示通信统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMMSTAT
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 平台调测
- 通信调测
status: active
---

# DSP COMMSTAT（显示通信统计）

## 功能

**适用网元：SGSN、MME**

该命令用于遇到系统内部通信消息处理有问题时，查询通信统计。

## 注意事项

当只输入必选参数时，由于输出结果内容过多，会导致在结果输出区域的“通用维护”页签中无法显示全部内容，建议在结果输出区单击右键选用“重定向”输出。该命令为调测命令，用于华为技术支持定位问题，如需使用，请联系华为技术支持。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询通信统计的进程类型。数据来源：无。<br>取值范围：<br>- “SPP”<br>- “SGP”<br>- “GBP”<br>- “LCP”<br>- “UPP”<br>- “CDP”<br>- “OMP”<br>- “HSP”<br>默认值： 无。 |
| PROCNO | 进程序列号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询通信统计的进程序号。<br>数据来源：无。<br>取值范围：0~20<br>默认值： 无。 |
| MSGSTATTYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询通信统计的统计类型。<br>数据来源：无。<br>取值范围：<br>- “MSG_FLOW（消息流类型统计）”<br>- “RECV_PID（接收PID）”<br>- “SOCK_IDX（SOCK索引）”<br>- “COMPAT_MSG_ID（兼容消息ID）”<br>默认值： 无。 |
| MSGFLOW | 消息流类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定查询通信统计的消息流类型。<br>前提条件：该参数在<br>“统计类型”<br>配置为<br>“MSG_FLOW（消息流类型统计）”<br>时生效。<br>数据来源：无。<br>取值范围：<br>- “PF（PF管理消息流）”<br>- “vCPU（vCPU管理维护消息流）”<br>- “Trc（跟踪消息流）”<br>- “SAAL（SAAL消息流）”<br>- “SNDCP（SNDCP消息流）”<br>- “SCTP（SCTP消息流）”<br>- “GTPC（GTPC消息流）”<br>- “GTPU（GTPU消息流）”<br>- “DNS（DNS消息流）”<br>- “CDR（计费消息流）”<br>- “NS_IP（Gb Over IP消息流）”<br>- “SGSN_heart（SGSN心跳通道消息流）”<br>- “GB_fwd（GB转发消息流）”<br>- “X1（X1接口消息流）”<br>- “X2（X2接口消息流）”<br>- “X3（X3接口消息流）”<br>- “VRP_data（VRP数据消息流）”<br>- “NTP（NTP消息流）”<br>- “BFD（BFD消息流）”<br>- “TPDU_FWD（TPDU转发消息流）”<br>- “ERRIND_FWD（ERR INDICATION转发消息流）”<br>- “SCTP_S1（S1接口消息流）”<br>- “SCTP_S1_AGT（S1Agent转发消息流）”<br>- “DYN_SCTP（动态SCTP消息流）”<br>- “TPDU_DIRECT_OUT（GPTU转发消息流）”<br>- “DIRECT_VP_FWD（业务进程间VP转发消息流）”<br>- “S102（S102接口消息流）”<br>- “GTPC_PATH_FWD（GTPC path转发消息）”<br>- “ESMDATA（ESMDATA消息流）”<br>默认值： 无。 |
| RECVPID | 接收PID | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定查询通信统计的接收PID。<br>前提条件：该参数在<br>“统计类型”<br>配置为<br>“RECV_PID（接收PID）”<br>时生效。<br>数据来源：无。<br>取值范围：0~350<br>默认值： 无。 |
| SOCKIDX | Socket索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定查询通信统计的Socket索引。<br>前提条件：该参数在<br>“统计类型”<br>配置为<br>“SOCK_IDX（SOCK索引）”<br>时生效。<br>数据来源：无。<br>取值范围：0~300<br>默认值： 无。 |
| MSGID | 兼容消息ID | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定查询通信统计的兼容消息ID。<br>前提条件：该参数在<br>“统计类型”<br>配置为<br>“COMPAT_MSG_ID（兼容消息ID）”<br>时生效。<br>数据来源：无。<br>取值范围：0~65535<br>默认值： 无。 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@COMMSTAT]] · 通信统计（COMMSTAT）

## 使用实例

查询USN_SP_RU_0065下UPP进程CDR消息流的通信统计：

DSP COMMSTAT: RUNAME="USN_SP_RU_0065", PROCTYPE=UPP, PROCNO=0, MSGSTATTYPE=MSG_FLOW, MSGFLOW=CDR, SERVICETYPE="USN_VNFC";

```
%%DSP COMMSTAT: RUNAME="USN_SP_RU_0065", PROCTYPE=UPP, PROCNO=0, MSGSTATTYPE=MSG_FLOW, MSGFLOW=CDR, 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。
操作结果如下
--------------
  RU名称    =  USN_SP_RU_0065
  进程类型  =  UPP
进程序列号  =  0
  统计类型  =  Msg flow type
  统计信息  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-COMMSTAT.md`
