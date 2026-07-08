---
id: UNC@20.15.2@MMLCommand@DSP MPROCMEMSTAT
type: MMLCommand
name: DSP MPROCMEMSTAT（查询进程内存信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MPROCMEMSTAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP MPROCMEMSTAT（查询进程内存信息）

## 功能

该命令用于查询所有被资源管理器管理的进程或指定进程的内存信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定进程类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的进程类型。 |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：本参数用于指定进程ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的进程ID。 |
| MEID | 网元 ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询进程的内存信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的网元ID。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MPROCMEMSTAT]] · 进程内存信息（MPROCMEMSTAT）

## 使用实例

- 查询所有被资源管理器管理的进程内存信息。
  ```
  %%DSP MPROCMEMSTAT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  进程类型      进程ID                                              网元ID   内存配额(MB)     内存使用量(MB)    内存使用率(%)

  CELL_SdbSim   sdbsim-pod-1172-16-1-254__139__0                   0        31995                610           1.91
  CELL_AM       vsm-pod-6954885569-2sqtb172-16-1-202__1006__0      0        31995                684           2.14
  CELL_SrvSim   srvcssim-pod-6767776644-zqhcr172-16-1-154__133__0  0        31995                203           0.63
  CELL_SrvSim   srvcssim-pod-6767776644-bbhp9172-16-1-199__133__0  0        31995                206           0.65
  (Number of results = 4)      
  (结果个数 = 4)
  ```
- 查询进程类型为CELL_SrvSim的所有进程内存信息。
  ```
  %%DSP MPROCMEMSTAT: PROCTYPE="CELL_SrvSim";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  进程类型      进程ID                                              网元ID     内存配额(MB)     内存使用量(MB)    内存使用率(%)
     
  CELL_SrvSim   srvcssim-pod-6767776644-zqhcr172-16-1-154__133__0  0          31995               203             0.63
  CELL_SrvSim   srvcssim-pod-6767776644-bbhp9172-16-1-199__133__0  0          31995               206             0.65
  (结果个数 = 2)
  ```
- 查询进程id为srvcssim-pod-6767776644-bbhp9172-16-1-199__133__0的进程内存信息。
  ```
  %%DSP MPROCMEMSTAT: PROCID="srvcssim-pod-6767776644-bbhp9172-16-1-199__133__0";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        进程类型  =  CELL_SrvSim
          进程ID  =  srvcssim-pod-6767776644-bbhp9172-16-1-199__133__0
          网元ID = 0
    内存配额(MB)  =  31995
  内存使用量(MB)  =  622
   内存使用率(%)  =  1.95
  (结果个数 = 1)
  ```
- 查询进程类型为CELL_SrvSim，且进程id为srvcssim-pod-6767776644-bbhp9172-16-1-199__133__0的进程内存信息。
  ```
  %%DSP MPROCMEMSTAT: PROCTYPE="CELL_SrvSim", PROCID="srvcssim-pod-6767776644-bbhp9172-16-1-199__133__0";
  RETCODE = 0  操作成功

  结果如下
  ------------------------
    进程类型  =  CELL_SrvSim
      进程ID  =  srvcssim-pod-6767776644-bbhp9172-16-1-199__133__0
      网元ID =  0
    内存配额  =  31995
  内存使用量  =  622
  内存使用率  =  1.95
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MPROCMEMSTAT.md`
