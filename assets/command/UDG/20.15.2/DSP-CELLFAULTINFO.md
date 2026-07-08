---
id: UDG@20.15.2@MMLCommand@DSP CELLFAULTINFO
type: MMLCommand
name: DSP CELLFAULTINFO（显示故障进程历史记录）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CELLFAULTINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP CELLFAULTINFO（显示故障进程历史记录）

## 功能

该命令用于查询进程故障历史记录，支持基于进程名称查询或查询整系统。查询整系统时默认按故障发生时间排序，显示离查询时间最近的前100条记录。

> **说明**
> - 在hafg复位的情况下，无法查询到复位前的历史记录。
> - 该命令最多显示100条记录。
> - 该命令查询成功，但没有显示历史记录，不代表没有进程故障，只是历史数据被清理掉，需要通过告警观察进程故障历史记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJECT | 对象类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示查询可用状态的对象类型：包括进程名称，进程ID。<br>数据来源：本端规划<br>取值范围：<br>- “PROCESSNAME（进程名称）”：进程名称<br>- “PROCESSID（进程ID）”：进程ID<br>默认值：无<br>配置原则：无 |
| CELLNAME | 进程名称 | 可选必选说明：该参数在"OBJECT"配置为"PROCESSNAME"时为条件可选参数。<br>参数含义：该参数用于指定故障进程的进程名称，如果不输入该参数，系统会查询所有故障进程的历史记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| CELLID | 进程ID | 可选必选说明：该参数在"OBJECT"配置为"PROCESSID"时为条件可选参数。<br>参数含义：该参数用于记录故障进程的进程ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CELLFAULTINFO]] · 故障进程历史记录（CELLFAULTINFO）

## 使用实例

查询整系统故障进程历史记录。

```
%%DSP CELLFAULTINFO: OBJECT=PROCESSNAME, CELLNAME="CELL_IPS";%%
RETCODE = 0  操作成功

结果如下
-----------
    序号  =  1
  进程ID  =  appctrl-pod-84f7c4c677-rc8t8192-168-0-160__114__0
进程名称  =  CELL_IPS
节点名称  =  10.0.0.1
故障时间  =  2020-10-05 20:37:23
故障原因  =  0x00006506
恢复时间  =  2020-10-05 20:37:39
故障次数  =  1
故障描述  =  正向监控HAF-Agent心跳超时
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-CELLFAULTINFO.md`
