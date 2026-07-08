---
id: UNC@20.15.2@MMLCommand@SET PROCRESTHD
type: MMLCommand
name: SET PROCRESTHD（设置进程资源告警阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PROCRESTHD
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 进程管理
status: active
---

# SET PROCRESTHD（设置进程资源告警阈值）

## 功能

![](设置进程资源告警阈值（SET PROCRESTHD）_07986436.assets/notice_3.0-zh-cn_2.png)

告警阈值的调整会影响告警的触发条件，请注意设置合理的告警阈值。

该命令用于设置进程的资源告警上报、清除阈值。

## 注意事项

告警阈值会持久化到Gauss数据库中，各进程阈值更新会有一定的延迟，可通过 **[DSP PROCRESSTAT](查询进程资源信息（DSP PROCRESSTAT）_08146288.md)** 命令进行查看。

本命令若按照“进程类型”配置后再次按照“网元级”配置，则不覆盖该网元下的“进程类型”的配置。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SETPROCTHD_MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：当前需要设置告警阈值的网元ID，即应用ID。<br>取值范围：整数类型，取值范围0~65535。<br>默认值：无。<br>配置原则：无。 |
| SETPROCTHD_RES_NAME | 资源名称 | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的资源名称。<br>取值范围：<br>- cpu(CPU)<br>- memory(内存)<br>- thread(线程)<br>- fd(文件句柄)<br>默认值：无。<br>配置原则：无。 |
| SETPROCTHD_ALARM_GENERATE_TH | 告警上报阈值(%) | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的告警上报阈值。<br>取值范围：整数类型，取值范围 2~100<br>默认值： 无。<br>配置原则：告警上报阈值应大于告警清除阈值。 |
| SETPROCTHD_ALARM_CLEAR_TH | 告警清除阈值(%) | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的告警清除阈值。<br>取值范围：整数类型 ，取值范围1~99。<br>默认值： 无。<br>配置原则：告警清除阈值应小于告警上报阈值。 |
| SETPROCTHD_ALARM_TYPE | 阈值设置类型 | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的阈值类型。<br>取值范围：<br>- byME（网元级）<br>- byProcessType(进程类型)<br>默认值：无。<br>配置原则：无。 |
| SETPROCTHD_PROC_TYPE | 进程类型 | 可选必选说明：该参数在<br>“阈值设置类型”<br>取值为<br>“byProcessType(进程类型)”<br>时为必选参数。<br>参数含义：用于指示系统按照进程类型设置告警阈值。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询进程类型。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROCRESTHD]] · 进程资源告警阈值（PROCRESTHD）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PROCRESTHD.md`
