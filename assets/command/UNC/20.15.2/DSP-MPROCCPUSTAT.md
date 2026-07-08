---
id: UNC@20.15.2@MMLCommand@DSP MPROCCPUSTAT
type: MMLCommand
name: DSP MPROCCPUSTAT（查询进程CPU信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MPROCCPUSTAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP MPROCCPUSTAT（查询进程CPU信息）

## 功能

该命令用于查询所有被资源管理器管理的进程或指定进程的CPU信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定进程类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的进程类型。 |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：本参数用于指定进程ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的进程ID。 |
| MEID | 网元 ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询进程的cpu信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的网元ID。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPROCCPUSTAT]] · 进程CPU信息（MPROCCPUSTAT）

## 使用实例

- 查询所有被资源管理器管理的进程CPU信息。
  ```
  %%DSP MPROCCPUSTAT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  进程类型      进程ID                                              网元ID  CPU配额   CPU绝对使用率(%)  CPU相对使用率(%)
   
  CELL_SM       vsm-pod-6954885569-2sqtb172-16-1-202__1005__0      0       8          1.03                   0.13
  CELL_ADDR     vsm-pod-6954885569-2sqtb172-16-1-202__1007__0      0       8          2.07                   0.26
  CELL_SCFM     sfm-pod-654865744-mdxtr172-16-0-56__107__0         0       8          2.08                   0.26
  CELL_SCFM     sfm-pod-654865744-rqkq9172-16-0-43__107__0         0       8          2.09                   0.26
  (结果个数 = 4)
  ```
- 查询进程类型为CELL_SCFM的所有进程CPU信息。
  ```
  %%DSP MPROCCPUSTAT: PROCTYPE="CELL_SCFM";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  进程类型      进程ID                                              网元ID  CPU配额   CPU绝对使用率(%)  CPU相对使用率(%)
     
  CELL_SCFM     sfm-pod-654865744-mdxtr172-16-0-56__107__0         0      8          2.08                   0.26
  CELL_SCFM     sfm-pod-654865744-rqkq9172-16-0-43__107__0         0      8          2.09                   0.26
  (结果个数 = 2)
  ```
- 查询进程id为sfm-pod-654865744-mdxtr172-16-0-56__107__0的进程CPU信息。
  ```
  %%DSP MPROCCPUSTAT: PROCID="sfm-pod-654865744-mdxtr172-16-0-56__107__0";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
          进程类型  =  CELL_SCFM
            进程ID  =  sfm-pod-654865744-mdxtr172-16-0-56__107__0
            网元ID  =  0
           CPU配额  =  8.00
  CPU绝对使用率(%)  =  3.09
  CPU相对使用率(%)  =  0.39
  (结果个数 = 1)
  ```
- 查询进程类型为CELL_SCFM，且进程id为sfm-pod-654865744-mdxtr172-16-0-56__107__0的进程CPU信息。
  ```
  %%DSP MPROCCPUSTAT: PROCTYPE="CELL_SCFM", PROCID="sfm-pod-654865744-mdxtr172-16-0-56__107__0";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
          进程类型  =  CELL_SCFM
            进程ID  =  sfm-pod-654865744-mdxtr172-16-0-56__107__0
            网元ID  =  0
           CPU配额  =  8.00
  CPU绝对使用率(%)  =  3.09
  CPU相对使用率(%)  =  0.39
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MPROCCPUSTAT.md`
