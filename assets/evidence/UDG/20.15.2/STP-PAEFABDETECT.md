# 停止Fabric链路探测任务（STP PAEFABDETECT）

- [命令功能](#ZH-CN_MMLREF_0000002112631728__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002112631728__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002112631728__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002112631728__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000002112631728)

该命令用于停止Fabric平面链路状态探测。

> **说明**
> 该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000002112631728)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002112631728)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASK | 停止检测范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定停止检测的范围。<br>数据来源：本端规划<br>取值范围：<br>- TASK_SINGLE_LINK（单条链路）<br>- TASK_ALL_LINK（所有链路）<br>默认值：无<br>配置原则：无 |
| SRCPODNAME | 源Pod名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。该参数在"TASK"配置为"TASK_ALL_LINK"时为条件可选参数。<br>参数含义：该参数用于指定本端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| DSTPODNAME | 目的Pod名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。该参数在"TASK"配置为"TASK_ALL_LINK"时为条件可选参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| SRCPORTNAME | 源端口名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。该参数在"TASK"配置为"TASK_ALL_LINK"时为条件可选参数。<br>参数含义：该参数用于指定本端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |
| DSTPORTNAME | 目的端口名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。该参数在"TASK"配置为"TASK_ALL_LINK"时为条件可选参数。<br>参数含义：该参数用于指定远端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |

## [使用实例](#ZH-CN_MMLREF_0000002112631728)

停止Fabric链路探测任务：

```
+++    UNC/*MEID:0 MENAME:UNC_z30062954_X86_20241226_1001*/        2024-12-26 15:59:06
O&M    #3305
%%STP PAEFABDETECT: TASK=TASK_SINGLE_LINK, SRCPODNAME="cslbip-pod-0", DSTPODNAME="vup-pod-0", SRCPORTNAME="eth2", DSTPORTNAME="eth2";%%
RETCODE = 0  操作成功

---    END
```
