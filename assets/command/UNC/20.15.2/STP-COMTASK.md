---
id: UNC@20.15.2@MMLCommand@STP COMTASK
type: MMLCommand
name: STP COMTASK（停止SDR通信质量检测任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: COMTASK
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# STP COMTASK（停止SDR通信质量检测任务）

## 功能

![](停止SDR通信质量检测任务（STP COMTASK）_63673353.assets/notice_3.0-zh-cn_2.png)

该命令是高危命令，操作不当可能会影响性能，请谨慎使用并联系华为技术支持协助操作。

该命令用于强制停止SDR通信质量检测任务。

## 注意事项

- 该命令执行后立即生效。

- 如需确认检测任务是否已经停止，可通过[**DSP COMTASKSUMM**](显示SDR通信质量检测结果概要（DSP COMTASKSUMM）_63673343.md)查询SDR通信质量检测结果概要，若对应检测任务的停止时间不为空，则检测任务已经停止成功。
- SRCID不存在时，停止命令执行成功，但停止任务不生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHTYPE | 路径类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR点对点通信质量检测的路径类型。<br>数据来源：本端规划<br>取值范围：<br>- “INTERPOD（Pod间测量）”：SDR点对点检测任务在Pod间测量，探测两个Pod间的网络质量。<br>- “INTERPROC（进程间测量）”：SDR点对点检测任务在进程间测量，探测两个进程间的网络质量。<br>默认值：无<br>配置原则：无 |
| SRCID | 源端ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信质量检测的源端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>命令输出结果中的Process ID获取。但是Cell ID不能选为SDRE进程类型的Process ID。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@COMTASK]] · SDR通信质量检测任务（COMTASK）

## 使用实例

强制停止SDR通信质量检测任务：

```
%%STP COMTASK: PATHTYPE=INTERPOD, SRCID="vsm-pod-6b4c899fc9-6rxzp";%%
RETCODE = 0 操作成功

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STP-COMTASK.md`
