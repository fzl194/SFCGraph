---
id: UNC@20.15.2@MMLCommand@ACT P2PCOMTASK
type: MMLCommand
name: ACT P2PCOMTASK（激活SDR点对点通信质量检测任务）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: P2PCOMTASK
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# ACT P2PCOMTASK（激活SDR点对点通信质量检测任务）

## 功能

![](激活SDR点对点通信质量检测任务（ACT P2PCOMTASK）_63673341.assets/notice_3.0-zh-cn_2.png)

该命令是高危命令，操作不当可能会影响性能，请谨慎使用并联系华为技术支持协助操作。

该命令用于激活SDR点对点通信质量检测任务。

## 注意事项

- 该命令执行后立即生效。

- 执行此激活命令前需要确保DTP开关处于开启状态，执行[**LST SDRPARAMS**](../TCP开关控制/查询SDR参数（LST SDRPARAMS）_09587932.md)命令查询DTP开关状态，执行[**SET SDRPARAMS**](../TCP开关控制/设置SDR参数（SET SDRPARAMS）_09587912.md)命令设置DTP开关。
- 只有PROTOCOLTYPE选择UDP可以探测丢包率，选择TCP或TLS测出的丢包率始终为0。
- SRCID不存在时，激活命令执行成功，但激活任务不生效。
- FLATTYPE为BASE时不支持PROTOCOLTYPE为TLS的通信探测。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLATTYPE | 通信平面类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR传输平面类型。<br>数据来源：本端规划<br>取值范围：<br>- “BASE（Base）”：Base平面<br>- “FABRIC（Fabric）”：Fabric平面<br>默认值：无<br>配置原则：无 |
| PATHTYPE | 路径类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR点对点通信质量检测的路径类型。<br>数据来源：本端规划<br>取值范围：<br>- “INTERPOD（Pod间测量）”：SDR点对点检测任务在Pod间测量，探测两个Pod间的网络质量。<br>- “INTERPROC（进程间测量）”：SDR点对点检测任务在进程间测量，探测两个进程间的网络质量。<br>默认值：无<br>配置原则：无 |
| PROTOCOLTYPE | 协议类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR点对点通信质量检测的协议类型。探测是否有丢包时优选UDP，探测时延则根据消息实际走的通道选择UDP、TCP或TLS。<br>数据来源：本端规划<br>取值范围：<br>- “UDP（UDP协议）”：SDR点对点检测任务使用UDP协议，表示非可靠传输。<br>- “TCP（TCP协议）”：SDR点对点检测任务使用TCP协议，表示可靠传输。<br>- “TLS（TLS协议）”：SDR点对点检测任务使用TLS协议，表示加密传输。<br>默认值：无<br>配置原则：无 |
| SRCID | 源端ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR点对点通信质量检测的源端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>命令输出结果中的Process ID获取。但是Cell ID不能选为SDRE进程类型的Process ID。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| DSTID | 目的端ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR点对点通信质量检测的目的端ID。PATHTYPE为INTERPROC时，该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>命令输出结果中的Process ID获取。但是Cell ID不能选为SDRE进程类型的Process ID。PATHTYPE为INTERPOD时，该ID为Pod Name(PaaS分配的Pod ID)，可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PKGLENMODE | 检测报文长度的模式 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR点对点通信质量检测报文长度的模式。<br>数据来源：本端规划<br>取值范围：<br>- “MIXEDLEN（混合包长模式）”：探测报文的长度模式为混合模式，自动按预定的包长发包，覆盖不同包长，包长为1024、1500、2000，循环发送这些长度的包。<br>- “FIXEDLEN（指定包长模式）”：探测报文的长度模式为指定长度模式，包长由参数PKGLEN指定，取值范围为1024~10000，单位是字节。<br>默认值：无<br>配置原则：无 |
| PKGLEN | 检测报文的长度(字节) | 可选必选说明：该参数在"PKGLENMODE"配置为"FIXEDLEN"时为条件必选参数。<br>参数含义：该参数用于标识SDR点对点通信质量检测报文的长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1024~10000，单位是字节。<br>默认值：1024<br>配置原则：无 |
| DURATION | 检测时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于标识SDR点对点通信质量检测时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~86400，单位是秒。<br>默认值：10<br>配置原则：无 |
| PKGRATE | 检测包速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于标识SDR点对点通信质量检测的检测包速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000，单位是包每秒。<br>默认值：1<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/P2PCOMTASK]] · SDR点对点通信质量检测任务（P2PCOMTASK）

## 使用实例

激活SDR点对点通信质量检测任务：

```
%%ACT P2PCOMTASK: FLATTYPE=BASE, PATHTYPE=INTERPOD, PROTOCOLTYPE=UDP, SRCID="vsm-pod-6b4c899fc9-6rxzp", DSTID="vusn-pod-0", PKGLENMODE=MIXEDLEN, DURATION=30;%%
RETCODE = 0 操作成功

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-P2PCOMTASK.md`
