---
id: UNC@20.15.2@MMLCommand@CLR PAEFABDETECT
type: MMLCommand
name: CLR PAEFABDETECT（清除Fabric链路探测结果）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: PAEFABDETECT
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 链路探测
status: active
---

# CLR PAEFABDETECT（清除Fabric链路探测结果）

## 功能

该命令用于清除Fabric平面链路状态探测结果。

## 注意事项

- 该命令执行后立即生效。

- 不支持在探测过程中清理探测结果，如果要强制清除，请先执行[**STP PAEFABDETECT**](停止Fabric链路探测任务（STP PAEFABDETECT）_12631728.md)命令停止探测。
- 清除正处在探测任务中的链路结果会导致简要查询命令的目的端数据出现错误，请谨慎执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASK | 清除结果类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的fabric检测任务。<br>数据来源：本端规划<br>取值范围：<br>- TASK_SINGLE_LINK（单条链路）<br>- TASK_ALL_LINK（所有链路）<br>默认值：无<br>配置原则：无 |
| SRCPODNAME | 源Pod名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。该参数在"TASK"配置为"TASK_ALL_LINK"时为条件可选参数。<br>参数含义：该参数用于指定本端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| DSTPODNAME | 目的Pod名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。该参数在"TASK"配置为"TASK_ALL_LINK"时为条件可选参数。<br>参数含义：该参数用于指定远端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| SRCPORTNAME | 源端口名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。该参数在"TASK"配置为"TASK_ALL_LINK"时为条件可选参数。<br>参数含义：该参数用于指定本端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |
| DSTPORTNAME | 目的端口名称 | 可选必选说明：该参数在"TASK"配置为"TASK_SINGLE_LINK"时为条件必选参数。该参数在"TASK"配置为"TASK_ALL_LINK"时为条件可选参数。<br>参数含义：该参数用于指定远端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEFABDETECT]] · Fabric链路探测任务（PAEFABDETECT）

## 使用实例

清除Fabric链路探测结果：

```
+++    UNC/*MEID:0 MENAME:UNC_z30062954_X86_20241226_1001*/        2024-12-26 16:00:24
O&M    #3309
%%CLR PAEFABDETECT: TASK=TASK_SINGLE_LINK, SRCPODNAME="cslbip-pod-0", DSTPODNAME="vup-pod-0", SRCPORTNAME="eth2", DSTPORTNAME="eth2";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除Fabric链路探测结果（CLR-PAEFABDETECT）_12471964.md`
