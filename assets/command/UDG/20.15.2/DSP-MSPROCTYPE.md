---
id: UDG@20.15.2@MMLCommand@DSP MSPROCTYPE
type: MMLCommand
name: DSP MSPROCTYPE（显示微服务进程类型）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSPROCTYPE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP MSPROCTYPE（显示微服务进程类型）

## 功能

此命令用于查询系统内所有微服务进程类型。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询进程类型；网元ID可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询出来。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：<br>若该参数不输入，则表示查询所有网元下的进程类型。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSPROCTYPE]] · 微服务进程类型（MSPROCTYPE）

## 使用实例

- 查询所有微服务进程类型
  ```
  %%DSP MSPROCTYPE:;%%
  RETCODE = 0  操作成功 

  结果如下
  ------------------------
  进程类型      进程类型名       网元ID

  1019          CELL_AUTH          0      
  1011          CELL_NRF           0      
  129           CELL_CPM           0      
  125           CELL_RCCTRL        0      
  1022          CELL_SBILINK       0     
  (结果个数 = 5)

  ---    END
  ```
- 查询指定网元ID下的所有微服务进程类型
  ```
  %%DSP MSPROCTYPE: MEID="0";%%
  RETCODE = 0  操作成功 

  结果如下
  ------------------------
  进程类型      进程类型名       网元ID
    
  1011          CELL_NRF           0      
  125           CELL_RCCTRL        0      
  112           CELL_RMFEXEC       0      
  116           CELL_MMCS          0      
  (结果个数 = 4)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSPROCTYPE.md`
