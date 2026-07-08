---
id: UNC@20.15.2@MMLCommand@DSP COMTASKDETAIL
type: MMLCommand
name: DSP COMTASKDETAIL（显示SDR通信质量检测结果详情）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMTASKDETAIL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# DSP COMTASKDETAIL（显示SDR通信质量检测结果详情）

## 功能

该命令用于显示SDR通信质量检测结果详情。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHTYPE | 路径类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信质量检测的路径类型。<br>数据来源：本端规划<br>取值范围：<br>- “INTERPOD（Pod间测量）”：SDR点对点检测任务在Pod间测量，探测两个Pod间的网络质量。<br>- “INTERPROC（进程间测量）”：SDR点对点检测任务在进程间测量，探测两个进程间的网络质量。<br>默认值：无<br>配置原则：无 |
| SRCID | 源端ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信质量检测的源端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| TASKID | 任务ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信质量检测的任务ID。由命令DSP COMTASKSUMM查询得到。一个SRCID+一个TASKID表示唯一标识的探测任务。若TASKID与SRCID或PATHTYPE不能匹配，则返回错误。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SDR通信质量检测结果详情（COMTASKDETAIL）](configobject/UNC/20.15.2/COMTASKDETAIL.md)

## 使用实例

显示SDR通信质量检测结果详情：

```
%%DSP COMTASKDETAIL: PATHTYPE=INTERPOD, SRCID="vsm-pod-6b4c899fc9-6rxzp", TASKID=11;%%
RETCODE = 0 操作成功

结果如下
--------
路径类型  源端ID                   目的端ID   任务ID 检测方向 分段          平均时延(微秒) 最小时延(微秒) 最大时延(微秒) 50%点时延(微秒) 90%点时延(微秒) 99%点时延(微秒) 99.9%点时延(微秒) 99.99%点时延(微秒) 丢包数 

Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     端到端   RTT           442            295            1587           352             754             913             913               913                0 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     请求     BDRS2KERNEL_1 18             15             28             16              24              28              28                28                 0 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     请求     KERNEL2BDRS_2 220            31             1099           62              693             952             952               952                0 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     请求     BDRS2APP_3    19             16             29             17              25              29              29                29                 0 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     响应     APP2BDRS_4    13             9              26             11              18              24              24                24                 0 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     响应     BDRS2KERNEL_5 19             13             51             16              26              34              34                34                 0 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     响应     KERNEL2BDRS_6 133            4294966634     464            199             257             359             359               359                0 
Pod间测量 vsm-pod-6b4c899fc9-6rxzp vusn-pod-0 11     响应     BDRS2APP_7    18             15             29             16              24              24              24                24                 0 
(结果个数 = 8)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SDR通信质量检测结果详情（DSP-COMTASKDETAIL）_63673342.md`
