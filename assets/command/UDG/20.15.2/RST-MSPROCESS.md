---
id: UDG@20.15.2@MMLCommand@RST MSPROCESS
type: MMLCommand
name: RST MSPROCESS（复位微服务进程）
nf: UDG
version: 20.15.2
verb: RST
object_keyword: MSPROCESS
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# RST MSPROCESS（复位微服务进程）

## 功能

![](复位微服务进程（RST MSPROCESS）_09587898.assets/notice_3.0-zh-cn.png)

复位进程可能会造成业务的短时中断，在存储故障期间执行该命令复位进程后，该进程在存储故障恢复期都无法启动。请谨慎使用并联系华为技术支持协助操作。

此命令用于重启进程。

> **说明**
> - 该命令执行后立即生效。
>
> - 复位进程可能会造成业务的短时中断。
> - 复位有主备模式的主进程，会导致备升主。
> - 在存储故障期间执行该命令复位进程后，该进程在存储故障恢复期都无法启动。
> - 执行本命令批量复位CELL_SCFA进程可能会导致业务故障。建议执行本命令批量复位CELL_SCFA进程前，先执行[**SET MSFAULTTOLERANCE**](设置故障检测参数（SET MSFAULTTOLERANCE）_09587879.md)命令修改进程级正向监控心跳超时周期数为24，进程级反向监控心跳超时周期数为22。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCOBJECT | 操作对象 | 可选必选说明：必选参数<br>参数含义：该参数用于表示复位进程的关键字：进程类型名或进程ID。<br>数据来源：本端规划<br>取值范围：<br>- “PROCNAME（进程类型名）”：进程类型<br>- “PROCID（进程ID）”：进程ID<br>默认值：无<br>配置原则：无 |
| PROCNAME | 进程类型 | 可选必选说明：该参数在"PROCOBJECT"配置为"PROCNAME"时为条件必选参数。<br>参数含义：该参数用于表示进程类型名，根据进程类型名复位进程。进程类型名可以通过<br>[**DSP MSPROCTYPE**](显示微服务进程类型（DSP MSPROCTYPE）_09587905.md)<br>命令查询。该命令不支持复位部分进程例如CSDB，MPEP，MPCP，MNCP，MLBP，MOMP。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |
| PROCID | 进程ID | 可选必选说明：该参数在"PROCOBJECT"配置为"PROCID"时为条件必选参数。<br>参数含义：该参数用于表示需要复位进程的ID。<br>[**DSP MSPROCESS**](显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>命令按进程类型名查询会返回该类型的所有进程ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~100。<br>默认值：无<br>配置原则：无 |
| MEID | 网元ID | 可选必选说明：该参数在"PROCOBJECT"配置为"PROCNAME"、"PROCID"时为条件可选参数。<br>参数含义：该参数表示需复位的进程应属于哪一个网元；网元ID可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询出来。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：<br>若该参数不输入，则表示需复位进程可属于任意网元。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSPROCESS]] · 复位微服务进程（MSPROCESS）

## 使用实例

- 按进程类型，复位指定网元下的进程
  ```
  %%RST MSPROCESS: PROCOBJECT=PROCNAME, PROCNAME="CELL_SBIM", MEID="0";%%
  RETCODE = 0  操作成功

  ---    END
  ```
- 按进程ID，复位指定网元下的进程
  ```
  %%RST MSPROCESS: PROCOBJECT=PROCID, PROCID="srvcssim-pod-6bf59959f6-qvkbq192-168-1-1__133__0", MEID="0";%%
  RETCODE = 0  操作成功

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RST-MSPROCESS.md`
