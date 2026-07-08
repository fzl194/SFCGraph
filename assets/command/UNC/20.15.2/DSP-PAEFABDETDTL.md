---
id: UNC@20.15.2@MMLCommand@DSP PAEFABDETDTL
type: MMLCommand
name: DSP PAEFABDETDTL（显示Fabric链路探测任务的详细结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEFABDETDTL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 链路探测
status: active
---

# DSP PAEFABDETDTL（显示Fabric链路探测任务的详细结果）

## 功能

该命令用于查询Fabric平面链路状态探测详细结果。

## 注意事项

不支持在探测过程查询详细探测结果，如果要强制查询，请先执行 [**STP PAEFABDETECT**](停止Fabric链路探测任务（STP PAEFABDETECT）_12631728.md) 命令停止探测。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASK | 查询范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的fabric检测任务。<br>数据来源：本端规划<br>取值范围：<br>- TASK_SINGLE_LINK（单条链路）<br>默认值：无<br>配置原则：无 |
| SRCPODNAME | 源Pod名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。<br>参数含义：该参数用于指定本端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| DSTPODNAME | 目的Pod名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。<br>参数含义：该参数用于指定远端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| SRCPORTNAME | 源端口名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。<br>参数含义：该参数用于指定本端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |
| DSTPORTNAME | 目的端口名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。<br>参数含义：该参数用于指定远端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |

## 操作的配置对象

- [Fabric链路探测任务的详细结果（PAEFABDETDTL）](configobject/UNC/20.15.2/PAEFABDETDTL.md)

## 使用实例

显示Fabric链路探测任务的详细结果：

```
+++    UNC/*MEID:0 MENAME:UNC_z30062954_X86_20241226_1001*/        2024-12-26 15:59:33
O&M    #3307
%%DSP PAEFABDETDTL: TASK=TASK_SINGLE_LINK, SRCPODNAME="cslbip-pod-0", DSTPODNAME="vup-pod-0", SRCPORTNAME="eth2", DSTPORTNAME="eth2";%%
RETCODE = 0  操作成功

结果如下
--------
   源Pod名称  =  cslbip-pod-0
 目的Pod名称  =  vup-pod-0
  源端口名称  =  eth2
目的端口名称  =  eth2
Fabric平面ID  =  0
探测报文长度  =  报文长度512字节
    探测间隔  =  200
源端发送包数  =  159
源端接收包数  =  159
丢包率（‰）  =  0
错包率（‰）  =  0
最大时延时间  =  486
最小时延时间  =  43
平均时延时间  =  229
最大抖动时间  =  306
最小抖动时间  =  0
平均抖动时间  =  93
    探测状态  =  完成探测
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示Fabric链路探测任务的详细结果（DSP-PAEFABDETDTL）_12471968.md`
