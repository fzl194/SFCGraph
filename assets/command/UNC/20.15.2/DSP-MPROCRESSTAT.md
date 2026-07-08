---
id: UNC@20.15.2@MMLCommand@DSP MPROCRESSTAT
type: MMLCommand
name: DSP MPROCRESSTAT（查询进程资源数量）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MPROCRESSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP MPROCRESSTAT（查询进程资源数量）

## 功能

该命令用于查询所有被资源管理器管理的进程或指定进程的资源数量信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定进程类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的进程类型。 |
| MEID | 网元 ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询进程的资源数量信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的网元ID。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPROCRESSTAT]] · 进程资源数量（MPROCRESSTAT）

## 使用实例

- 查询所有被资源管理器管理的进程资源数量。
  ```
  %%DSP MPROCRESSTAT:;%%
  RETCODE = 0  操作成功 

  结果如下
  ------------------------
  进程类型      网元ID 进程ID                                              Actor数量

  CELL_SCFM     0     sfm-pod-845bfd885d-njv9l192-168-0-39__107__0        61
  CELL_SdbSim   0     sdbsim-pod-1192-168-1-242__139__0                   107
  CELL_SM       0     vsm-pod-57b8dd4ff6-4rj4g192-168-1-106__1005__0      45
  CELL_NetSim   0     netcssim-pod-776f475944-kg4hm192-168-1-103__134__0  53
  CELL_ADDR     0     vsm-pod-57b8dd4ff6-wgtzx192-168-1-122__1007__0      60
  CELL_PLCM     0     vsm-pod-57b8dd4ff6-wgtzx192-168-1-122__1008__0      161
  (结果个数 = 6)
  ```
- 查询进程类型为CELL_SCFM的所有进程资源数量。
  ```
  %%DSP MPROCRESSTAT: PROCTYPE="CELL_SCFM";%%
  RETCODE = 0  操作成功 

  结果如下
  ------------------------
  进程类型      网元ID 进程ID                                        Actor数量

  CELL_SCFM     0     sfm-pod-845bfd885d-nrm4b192-168-0-7__107__0   42
  CELL_SCFM     0     sfm-pod-845bfd885d-njv9l192-168-0-39__107__0  61
  CELL_SCFM     0     sfm-pod-845bfd885d-tnt46192-168-0-52__107__0  42
  (结果个数 = 3)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MPROCRESSTAT.md`
