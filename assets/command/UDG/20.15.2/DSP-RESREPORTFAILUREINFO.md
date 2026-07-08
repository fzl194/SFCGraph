---
id: UDG@20.15.2@MMLCommand@DSP RESREPORTFAILUREINFO
type: MMLCommand
name: DSP RESREPORTFAILUREINFO（显示组件上报的故障信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESREPORTFAILUREINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 系统调测
- 异常信息
status: active
---

# DSP RESREPORTFAILUREINFO（显示组件上报的故障信息）

## 功能

该命令用于显示当前系统中存在的组件上报故障信息。

当组件异常时，可执行该命令查看当前系统中是否存在组件上报故障信息，方便定位问题。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCENAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源名称。通过<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>命令可以查询资源信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有资源的信息。使用<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>查看资源名称。 |
| SHOWNUM | 要查询的数据最大个数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示每个资源能够显示的最大记录量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：<br>**20**<br>配置原则：当不输入时，若是某个资源的实际数据量达到此参数的默认值，则显示的数据量为此参数默认值，否则按实际数据量显示。当输入某个值时，若是某个资源的实际数据量达到此参数值，则显示的数据量为此参数值，否则按实际数据量显示。 |
| BEGININDEX | 记录起始位置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示每个资源从第几条记录开始显示。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～99。<br>默认值：无<br>配置原则：当不输入时，从最新的数据开始显示，否则从指定的起始数据索引开始显示。 |
| ISVERBOSE | 是否查询详细信息 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否显示详细信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- **NO**：否。<br>- **YES**：是。<br>默认值：<br>**NO** |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RESREPORTFAILUREINFO]] · 组件上报的故障信息（RESREPORTFAILUREINFO）

## 使用实例

显示所有详细的组件上报故障信息：

```
DSP RESREPORTFAILUREINFO: ISVERBOSE=YES;
```

```
RETCODE = 0  操作成功

结果如下:
--------
        资源名称  =  OMU2
组件上报故障时间  =  2016-04-15 14:26:32
          组件ID  =  0x80f1004e
        进程名称  =  APPLocation10001
        临终信息  =  report_failure
            事件  =  11
        事件参数  =  15
          调用栈  =  
liblocbase.so(VRP_HafRepFailure+0xf5) [0x00007f013d959e35]
libsspbase.so(HAF_DoReportFailure+0xb3) [0x00007f013eacc513] 
libsspbase.so(HAF_ReportSelfFailureWithLog+0x17) [0x00007f013eacc957] 
compa.so(COMPA_ReportSelfFailureHandler+0x9a) [0x00007f01364bf0fa] 
libdefault.so(RTF_MsgProcessCbk+0x101) [0x00007f01429e97a1] 
libdefault.so(rtfScmMessageSchedule+0x24d) [0x00007f01429e87bd] 
libdefault.so(rtfScmCompScheKernelEntryFifo+0xda) [0x00007f01429e955a] 
libdefault.so(rtfScmCompScheDefaultEntry+0x2fa) [0x00007f01429e5b6a] 
libdefault.so(tskAllTaskEntry+0x15f) [0x00007f01427faeff] 
libpthread.so.0(+0x7df5) [0x00007f0143d68df5]
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示组件上报的故障信息（DSP-RESREPORTFAILUREINFO）_51002633.md`
