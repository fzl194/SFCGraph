---
id: UDG@20.15.2@MMLCommand@DSP RESPARTITIONINFO
type: MMLCommand
name: DSP RESPARTITIONINFO（显示资源的磁盘分区信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESPARTITIONINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 资源管理
- 资源实例管理
status: active
---

# DSP RESPARTITIONINFO（显示资源的磁盘分区信息）

## 功能

该命令用来查询资源的磁盘分区信息，包括分区总大小、分区已使用空间大小、剩余空间大小以及使用率等。

在日常的维护活动中，可使用本命令查看系统当前的磁盘信息，以确认是否有足够的磁盘空间来进行相关的业务操作。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCENAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：用于说明资源名称或容器名称。通过<br>[**DSP RES**](显示资源信息（DSP RES）_59036939.md)<br>命令可以查询资源信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RESPARTITIONINFO]] · 资源的磁盘分区信息（RESPARTITIONINFO）

## 使用实例

显示资源的磁盘分区使用情况：

```
DSP RESPARTITIONINFO:;
```

```
RETCODE = 0  操作成功

结果如下:
--------
资源名称    分区名称    分区空间总大小（Kbytes）   已使用空间大小（Kbytes）   剩余空间大小（Kbytes）   分区使用率（%）

OMU1        OS 1        5692588                    939264                     4464148                   18          
OMU1        home        10321208                   404596                     9392324                   5           
OMU1        logfile     1032088                    36412                      943248                    4           
OMU1        log         3096336                    76332                      2862720                   3           
OMU1        run         5160576                    1747676                    3150756                   36          
OMU1        software    15481840                   2390604                    12304804                  17                    
(结果个数 = 6)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RESPARTITIONINFO.md`
