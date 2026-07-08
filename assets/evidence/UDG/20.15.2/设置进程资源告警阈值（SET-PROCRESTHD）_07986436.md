# 设置进程资源告警阈值（SET PROCRESTHD）

- [命令功能](#ZH-CN_MMLREF_0000001307986436__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001307986436__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001307986436__1.3.3)
- [使用实例](#ZH-CN_MMLREF_0000001307986436__1.3.4)
- [输出结果说明](#ZH-CN_MMLREF_0000001307986436__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001307986436)

![](设置进程资源告警阈值（SET PROCRESTHD）_07986436.assets/notice_3.0-zh-cn.png)

告警阈值的调整会影响告警的触发条件，请注意设置合理的告警阈值。

该命令用于设置进程的资源告警上报、清除阈值。

> **说明**
> 告警阈值会持久化到Gauss数据库中，各进程阈值更新会有一定的延迟，可通过 **[DSP PROCRESSTAT](查询进程资源信息（DSP PROCRESSTAT）_08146288.md)** 命令进行查看。
>
> 本命令若按照“进程类型”配置后再次按照“网元级”配置，则不覆盖该网元下的“进程类型”的配置。

## [参数说明](#ZH-CN_MMLREF_0000001307986436)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SETPROCTHD_MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：当前需要设置告警阈值的网元ID，即应用ID。<br>取值范围：整数类型，取值范围0~65535。<br>默认值：无。<br>配置原则：无。 |
| SETPROCTHD_RES_NAME | 资源名称 | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的资源名称。<br>取值范围：<br>- cpu(CPU)<br>- memory(内存)<br>- thread(线程)<br>- fd(文件句柄)<br>默认值：无。<br>配置原则：无。 |
| SETPROCTHD_ALARM_GENERATE_TH | 告警上报阈值(%) | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的告警上报阈值。<br>取值范围：整数类型，取值范围 2~100<br>默认值： 无。<br>配置原则：告警上报阈值应大于告警清除阈值。 |
| SETPROCTHD_ALARM_CLEAR_TH | 告警清除阈值(%) | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的告警清除阈值。<br>取值范围：整数类型 ，取值范围1~99。<br>默认值： 无。<br>配置原则：告警清除阈值应小于告警上报阈值。 |
| SETPROCTHD_ALARM_TYPE | 阈值设置类型 | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的阈值类型。<br>取值范围：<br>- byME（网元级）<br>- byProcessType(进程类型)<br>默认值：无。<br>配置原则：无。 |
| SETPROCTHD_PROC_TYPE | 进程类型 | 可选必选说明：该参数在<br>“阈值设置类型”<br>取值为<br>“byProcessType(进程类型)”<br>时为必选参数。<br>参数含义：用于指示系统按照进程类型设置告警阈值。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询进程类型。 |

## [使用实例](#ZH-CN_MMLREF_0000001307986436)

1. 按照网元设置进程告警上报、清除阈值。
  ```
  %%SET PROCRESTHD: SETPROCTHD_MEID=0, SETPROCTHD_RES_NAME=cpu, SETPROCTHD_ALARM_GENERATE_TH=80, SETPROCTHD_ALARM_CLEAR_TH=75, SETPROCTHD_ALARM_TYPE=byME;%% 
  RETCODE = 0  执行成功    
  操作结果  =  SUCCESS 
  (结果个数 = 1)  
  ---    END
  ```

2. 按照进程类型设置进程告警上报、清除阈值。
  ```
  %%SET PROCRESTHD: SETPROCTHD_MEID=0, SETPROCTHD_RES_NAME=cpu, SETPROCTHD_ALARM_GENERATE_TH=80, SETPROCTHD_ALARM_CLEAR_TH=75, SETPROCTHD_ALARM_TYPE=byProcessType, SETPROCTHD_PROC_TYPE="cse-etcd";%% 
  RETCODE = 0  执行成功    
  操作结果  =  SUCCESS 
  (结果个数 = 1)  
  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0000001307986436)

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如 [表1 输出项说明](#ZH-CN_MMLREF_0000001307986436__zh-cn_mmlref_0000001175903143_table721916042810) 所示。

命令执行失败则返回相应的错误，参见 [表2 错误码列表](#ZH-CN_MMLREF_0000001307986436__zh-cn_mmlref_0000001175903143_table1362814278591) ；命令执行异常，请联系技术支持处理。

*表1 输出项说明*

| 输出项名称 | 输出项解释 |
| --- | --- |
| 执行结果 | 告警阈值是否设置成功。 |

*表2 错误码列表*

| 错误码 | 消息解释 | 原因分析 | 处理建议 |
| --- | --- | --- | --- |
| 20010 | gauss服务状态不正确 | Gauss服务故障或网络异常。 | 重试或联系华为技术支持处理。 |
| 20020 | 该网元不存在 | 输入了不存在的网元ID。 | 修改对应字段后重试。 |
| 20021 | 告警阈值不合法，恢复阈值应小于告警阈值 | 告警清除阈值应小于告警上报阈值。 | 修改对应字段后重试。 |
| 20022 | 无法修改该服务的告警阈值 | 未查询到该服务在线信息或者不支持此项设置。 | 修改对应字段后重试。 |
