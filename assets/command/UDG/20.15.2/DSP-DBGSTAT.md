---
id: UDG@20.15.2@MMLCommand@DSP DBGSTAT
type: MMLCommand
name: DSP DBGSTAT（查询调试信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DBGSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 公共调测
- 调试信息
status: active
---

# DSP DBGSTAT（查询调试信息）

## 功能

该命令用于查询CSLB系统内部运行信息，方便问题定位。内部运行信息不涉及用户敏感数据。

使用方法：先执行 **[DSP DBGSTAT](查询调试信息（DSP DBGSTAT）_29627109.md)** 命令查询PARA1输入参数“0”查询帮助信息，然后根据帮助信息再查询所需的内容。

## 注意事项

- 当前只实现了“PROCTYPE”为“PROC_TYPE_MPEP(PROC_MPEP)”，“PROC_TYPE_MOMP(PROC_MOMP)”，“PROC_TYPE_MNCP(PROC_MNCP)”，PROC_TYPE_MLBP(PROC_MLBP)和“PROC_TYPE_MPCP(PROC_MPCP)”的查询。其他进程类型为预留字段。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所需查询的RU名称，通过<br>**[LST SERVICERUSTATE](../../../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>查询。<br>取值范围： 0~63字符<br>默认值：无 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所需查询的进程类型。<br>取值范围：<br>- “PROC_TYPE_MPEP(PROC_MPEP) ”<br>- “PROC_TYPE_MOMP(PROC_MOMP) ”<br>- “PROC_TYPE_MNCP(PROC_MNCP) ”<br>- “PROC_TYPE_MLBP(PROC_MLBP) ”<br>- “PROC_TYPE_MPCP(PROC_MPCP) ”<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所需查询的进程序号，通过<br>**[DSP LBPROC](../../../../系统管理/进程状态/进程信息/查询CSLB进程（DSP LBPROC）_29627093.md)**<br>命令查询。<br>取值范围：0~63<br>默认值：无 |
| PARA1 | 第一个参数 | 可选必选说明：可选参数<br>参数含义：该参数指定第一个数值型的变量。<br>取值范围：0~63字符<br>默认值：无<br>说明：本参数含义和进程类型相关，详细请参见<br>**[DSP DBGSTAT](查询调试信息（DSP DBGSTAT）_29627109.md)**<br>输入参数补充说明。 |
| PARA2 | 第二个参数 | 可选必选说明：可选参数<br>参数含义：该参数指定第二个数值型的变量。<br>取值范围：0~63字符<br>默认值：无<br>说明：本参数含义和进程类型相关，详细请参见<br>**[DSP DBGSTAT](查询调试信息（DSP DBGSTAT）_29627109.md)**<br>输入参数补充说明。 |
| PARA3 | 第三个参数 | 可选必选说明：可选参数<br>参数含义：该参数指定第三个数值型的变量。<br>取值范围：0~63字符<br>默认值：无<br>说明：本参数含义和进程类型相关，详细请参见<br>**[DSP DBGSTAT](查询调试信息（DSP DBGSTAT）_29627109.md)**<br>输入参数补充说明。 |
| PARA4 | 第四个参数 | 可选必选说明：可选参数<br>参数含义：该参数指定第四个数值型的变量。<br>取值范围：0~63字符<br>默认值：无<br>说明：本参数含义和进程类型相关，详细请参见<br>**[DSP DBGSTAT](查询调试信息（DSP DBGSTAT）_29627109.md)**<br>输入参数补充说明。 |
| PARA5 | 第五个参数 | 可选必选说明：可选参数<br>参数含义：该参数指定第五个数值型的变量。<br>取值范围：0~63字符<br>默认值：无<br>说明：本参数含义和进程类型相关，详细请参见<br>**[DSP DBGSTAT](查询调试信息（DSP DBGSTAT）_29627109.md)**<br>输入参数补充说明。 |
| PARA6 | 第六个参数 | 可选必选说明：可选参数<br>参数含义：该参数指定第六个数值型的变量。该参数为预留参数，设置不生效。<br>取值范围：0~63字符<br>默认值：无<br>说明：本参数含义和进程类型相关，详细请参见<br>**[DSP DBGSTAT](查询调试信息（DSP DBGSTAT）_29627109.md)**<br>输入参数补充说明。 |

## 操作的配置对象

- [调试信息（DBGSTAT）](configobject/UDG/20.15.2/DBGSTAT.md)

## 使用实例

- 查询CSLB系统内部运行信息。
  DSP DBGSTAT: RUNAME="CSLB_IP_RU2_0070", PROCTYPE=PROC_TYPE_MPEP, PROCNO=3, PARA1="3", PARA2="0";

  ```
  %%DSP DBGSTAT: RUNAME="CSLB_IP_RU2_0070", PROCTYPE=PROC_TYPE_MPEP, PROCNO=3, PARA1="3", PARA2="0";%%
  RETCODE = 0  操作成功。
  结果如下:
  -------------------------
         RU名称  =  CSLB_IP_RU2_0070
       进程类型  =  E_PROC_TYPE_MPEP
         进程号  =  3
     第一个参数  =  3
     第二个参数  =  0
     第三个参数  =  NULL
     第四个参数  =  NULL
     第五个参数  =  NULL
     第六个参数  =  NULL
     结果字符串  =  
  E_MPE_RX_APP_PKT_RECV                                      (0x003): 593950708
  E_MPE_RX_RT_PKT_RECV                                       (0x004): 594009191
  E_MPE_RX_GI_FAST_PKT_RECV                                  (0x005): 296576228
  E_MPE_RX_S1U_FAST_PKT_RECV                                 (0x006): 297432963
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询调试信息（DSP-DBGSTAT）_29627109.md`
