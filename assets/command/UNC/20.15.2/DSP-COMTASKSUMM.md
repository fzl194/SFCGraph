---
id: UNC@20.15.2@MMLCommand@DSP COMTASKSUMM
type: MMLCommand
name: DSP COMTASKSUMM（显示SDR通信质量检测结果概要）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMTASKSUMM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# DSP COMTASKSUMM（显示SDR通信质量检测结果概要）

## 功能

该命令用于显示SDR通信质量检测结果概要。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHTYPE | 路径类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信质量检测的路径类型。<br>数据来源：本端规划<br>取值范围：<br>- “INTERPOD（Pod间测量）”：SDR点对点检测任务在Pod间测量，探测两个Pod间的网络质量。<br>- “INTERPROC（进程间测量）”：SDR点对点检测任务在进程间测量，探测两个进程间的网络质量。<br>默认值：无<br>配置原则：无 |
| SRCID | 源端ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信质量检测的源端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| DSTID | 目的端ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识SDR通信质量检测的目的端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@COMTASKSUMM]] · SDR通信质量检测结果概要（COMTASKSUMM）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-COMTASKSUMM.md`
