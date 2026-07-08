---
id: UDG@20.15.2@MMLCommand@DSP OMDBGDATA
type: MMLCommand
name: DSP OMDBGDATA（显示OM模块的调试信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OMDBGDATA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- OM调测
status: active
---

# DSP OMDBGDATA（显示OM模块的调试信息）

## 功能

此命令用于查询当前网元OM服务或组件的调试信息。

该命令的使用场景：在OM服务或组件日常维护场景下，进行维护调试。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBGTYPE | 调试类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定调试信息发送对象类型。<br>数据来源：本端规划<br>取值范围：<br>- CELLID（进程标识）<br>- CELLNAME（进程类型名称）<br>默认值：无<br>配置原则：无 |
| CELLID | 进程ID | 可选必选说明：该参数在"DBGTYPE"配置为"CELLID"时为条件必选参数。<br>参数含义：该参数用于指定进程ID。可以通过DSP MSPROCESS命令查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：无 |
| CELLNAME | 进程类型名称 | 可选必选说明：该参数在"DBGTYPE"配置为"CELLNAME"时为条件必选参数。<br>参数含义：该参数用于指定进程类型名称。可以通过DSP MSPROCTYPE命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |
| MODULE | 模块 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OM模块。<br>数据来源：本端规划<br>取值范围：<br>- CHR_SERVER（CHR服务端）<br>- CHR_CLIENT（CHR客户端）<br>- DATA_SHOW（Datashow服务）<br>- LICCTRL_SERVER（Licctrl服务端）<br>- LICCTRL_CLIENT（Licctrl客户端）<br>- OMP_SERVER（OMP服务端）<br>- NET_COMPLAINT_SERVER（网投查询服务端）<br>- MASSIVE_ALARM（海量告警）<br>- SERVICE_CONFIG（ServiceConfig服务）<br>- UCF_CTRL（UCF主控服务）<br>- UCF_EXEC（Ucf转发服务）<br>- UCF_CLIENT（UCF客户端）<br>- VPROBE_CTRL（vProbe主控服务）<br>- VPROBE_EXEC（vProbe转发服务）<br>- VPROBE_CLIENT（vProbe客户端）<br>- OMCM_SDK（配置SDK）<br>- PRIVATELOG_SDK（私有日志SDK）<br>- PLATFORM_SDK（公共SDK）<br>- TRACE_SDK（跟踪SDK）<br>- FILETRANSFER_SDK（文件传输SDK）<br>- PERF_CLIENT（话统客户端）<br>- MML_CLIENT（MML客户端）<br>- KPIMONITOR_SERVER（TAI指标检测服务端）<br>- KPIMONITOR_CLIENT（TAI指标检测客户端）<br>默认值：无<br>配置原则：无 |
| DEBUGNAME | 调试信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定调试信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。不能为非法字符，只允许输入英文字母（大小写敏感），数字，空格，“-”和“\|”。输入格式为1个或多个字符串，使用“\|”分割不同参数。例如：“cmd \| -n 1 \| -a 0”。当前支持的调试命令包括“report”、“record”、“successful record”、“failed record”、“count”，均支持可选调试参数：“-n”、“-a”。<br>默认值：无<br>配置原则：<br>- 可选调试参数：-n [number]：取值范围为-2147483648~2147483647，具体含义由对应模块自定义，不携带时默认值为0。-a [appid]：用于指定要查询的网元ID，取值范围为当前环境的所有网元ID，仅Framework场景支持填写其他网元ID，不携带时默认为当前网元ID。<br>- 支持的调试命令：report：该命令用于查询当前模块的调试报文，携带参数“-n”时，表示本模块的报文分类，取值范围由当前模块自定义。record：该命令用于查询当前模块的记录，携带参数“-n”时，表示最大返回条数。successful record：该命令用于查询当前模块的成功记录，携带参数“-n”时，表示最大返回条数。failed record：该命令用于查询当前模块的失败记录，携带参数“-n”时，表示最大返回条数。count：该命令用于查询当前模块的调试计数，携带参数“-n”时，表示本模块的计数分类，取值范围由当前模块自定义。 |

## 操作的配置对象

- [OM模块的调试信息（OMDBGDATA）](configobject/UDG/20.15.2/OMDBGDATA.md)

## 使用实例

查询操作对象为进程类型名称，进程类型名称为CELL_VPROBECTRL，模块为VPROBE_CTRL，调试信息为report时的调试信息：

```
%%DSP OMDBGDATA: DBGTYPE=CELLNAME, CELLNAME="CELL_VPROBECTRL", MODULE=VPROBE_CTRL, DEBUGNAME="report";%%
RETCODE = 0  操作成功

结果如下
--------
进程ID                                               进程类型名称     调测输出                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

vprobectrl-pod-6c6578fff6-hlh24192-168-2-56__165__0  CELL_VPROBECTRL  Standby controller start at: 2022-10-19 17:55:15, report make at: 2022-10-21 17:22:27

[Metric report hour]
	         Last Recv Time	  Call Count	    Max Cost	    Min Cost	    Avg Cost	Msg Name
	    2022-10-21 16:55:18	           1	   988.525us	   988.525us	   988.525us	LB_Plugin_Msg_PlugReq
	    2022-10-21 17:22:24	         367	   247.882us	     2.725us	    42.886us	LB_Plugin_Msg_Trans
[Metric report all]
	         Last Recv Time	  Call Count	    Max Cost	    Min Cost	    Avg Cost	Msg Name
	    2022-10-19 17:55:15	           1	   232.044us	   232.044us	   232.044us	CellStage:1
	    2022-10-19 17:55:15	           1	       424ns	       424ns	       424ns	CellStage:2

[Query All Table Data]
	[0x9473aceb] Table:CLASSID_DAMVIEW_UDRSVRIP, Results:
	0	Index:9, AccessName:VPROBE_SFTP, SvrName:VPROBE_SFTP, Port:22, IPv4:10.10.0.99

[Message]
1	UDR_CtrlMsgRegPlugIn @ 2022-10-19 17:55:17, sep:100001, APPNlsId:999, ServsType:1, ServsInst:4, AppTransType:0, CSId:12453616167623787265, MPF_SRV_PLUG_SVC_REG_OPER:51, cost:233.991us

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示OM模块的调试信息（DSP-OMDBGDATA）_63666972.md`
