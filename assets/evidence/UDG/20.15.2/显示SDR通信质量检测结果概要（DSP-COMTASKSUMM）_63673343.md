# 显示SDR通信质量检测结果概要（DSP COMTASKSUMM）

- [命令功能](#ZH-CN_MMLREF_0263673343__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0263673343__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0263673343__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0263673343__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0263673343__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0263673343)

该命令用于显示SDR通信质量检测结果概要。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0263673343)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0263673343)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHTYPE | 路径类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信质量检测的路径类型。<br>数据来源：本端规划<br>取值范围：<br>- “INTERPOD（Pod间测量）”：SDR点对点检测任务在Pod间测量，探测两个Pod间的网络质量。<br>- “INTERPROC（进程间测量）”：SDR点对点检测任务在进程间测量，探测两个进程间的网络质量。<br>默认值：无<br>配置原则：无 |
| SRCID | 源端ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信质量检测的源端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| DSTID | 目的端ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识SDR通信质量检测的目的端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0263673343)

显示SDR通信质量检测结果概要：

```
%%DSP COMTASKSUMM: PATHTYPE=INTERPOD, SRCID="vsm-pod-6b4c899fc9-6rxzp";%%
RETCODE = 0 操作成功

结果如下
--------
路径类型  源端ID                   目的端ID   任务ID 任务类型   通信平面类型 开始时间                结束时间                检测报文的长度(字节) 检测时长(秒) 检测协议类型 检测报文速率(个/秒) 发送检测报文数量 接收检测报文数量 丢包率 错包率 平均时延(微秒)

Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-1 8      P2PCOMTASK Base         2020-08-18 11:55:41.182 2020-08-18 11:55:51.281 1508                 10           UDP协议      1                   10               10               0      0      555 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-1 10     P2PCOMTASK Base         2020-08-18 11:57:44.406 2020-08-18 11:58:46.575 1508                 1000         UDP协议      1                   63               63               0      0      360 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     P2PCOMTASK Base         2020-08-18 14:17:58.250 2020-08-18 14:18:28.388 1508                 30           UDP协议      1                   30               30               0      0      442 
(结果个数 = 3)

--- END
```

## [输出结果说明](#ZH-CN_MMLREF_0263673343)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 路径类型 | 该参数用于标识SDR通信质量检测的路径类型。<br>取值说明：<br>- “INTERPOD（Pod间测量）”：SDR点对点检测任务在Pod间测量，探测两个Pod间的网络质量。<br>- “INTERPROC（进程间测量）”：SDR点对点检测任务在进程间测量，探测两个进程间的网络质量。 |
| 源端ID | 该参数用于标识SDR通信质量检测的源端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。 |
| 目的端ID | 该参数用于标识SDR通信质量检测的目的端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。 |
| 任务ID | 该参数用于标识SDR通信质量检测的任务ID。 |
| 任务类型 | 该参数用于标识SDR通信质量检测的任务类型。<br>取值说明：<br>- “P2PCOMTASK（P2PCOMTASK）”：点对点通信探测任务<br>- “TRANSCOMTASK（TRANSCOMTASK）”：进程间透明通信探测任务 |
| 通信平面类型 | 该参数用于标识SDR传输平面类型。<br>取值说明：<br>- “BASE（Base）”：Base平面<br>- “FABRIC（Fabric）”：Fabric平面 |
| 开始时间 | 该参数用于标识SDR通信质量检测的开始时间。 |
| 结束时间 | 该参数用于标识SDR通信质量检测的结束时间。 |
| 检测报文的长度(字节) | 该参数用于标识SDR通信质量检测报文的长度。 |
| 检测时长(秒) | 该参数用于标识SDR通信质量检测时长。 |
| 检测协议类型 | 该参数用于标识SDR通信质量检测的协议类型。<br>取值说明：<br>- “UDP（UDP协议）”：SDR点对点检测任务使用UDP协议，表示非可靠传输。<br>- “TCP（TCP协议）”：SDR点对点检测任务使用TCP协议，表示可靠传输。<br>- “TLS（TLS协议）”：SDR点对点检测任务使用TLS协议，表示加密传输。 |
| 检测报文速率(个/秒) | 该参数用于标识SDR通信质量检测的检测报文速率。 |
| 发送检测报文数量 | 该参数用于标识SDR通信质量检测的发送检测报文数量。 |
| 接收检测报文数量 | 该参数用于标识SDR通信质量检测的接收检测报文数量。 |
| 丢包率 | 该参数用于标识SDR通信质量检测的丢包率，单位：千分比。 |
| 错包率 | 该参数用于标识SDR通信质量检测的错包率，单位：千分比。 |
| 平均时延(微秒) | 该参数用于标识SDR通信质量检测的平均时延。 |
