---
id: UDG@20.15.2@MMLCommand@DSP MSSSCHTRACE
type: MMLCommand
name: DSP MSSSCHTRACE（查询调度线程轨迹信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSSCHTRACE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 调度统计查询
status: active
---

# DSP MSSSCHTRACE（查询调度线程轨迹信息）

## 功能

该命令用于查询调度线程线轨迹统计信息。

当轨迹统计开关打开时，可使用调度线程轨迹统计信息查询线程主动或者被动切换异常情况。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称，执行DSP RU查看RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| THREADID | 线程ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示线程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSSCHTRACE]] · 调度线程轨迹信息（MSSSCHTRACE）

## 使用实例

查询调度线程的轨迹信息：

```
DSP MSSSCHTRACE:THREADID=1,RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------
阶段               时间段（microsecond）    计数    平均执行时间（microsecond）    最大执行时间（microsecond）

Start              0-31                          101475    1                                17
Start              32-127                        0         0                                0
Start              128-1023                      0         0                                0
Start              1024-4095                     0         0                                0
Start              4096-Infinity                 0         0                                0
Before-sleep       0-31                          0         0                                0
Before-sleep       32-127                        0         0                                0
Before-sleep       128-1023                      0         0                                0
Before-sleep       1024-4095                     0         0                                0
Before-sleep       4096-Infinity                 0         0                                0
Sleep              0-31                          0         0                                0
Sleep              32-127                        0         0                                0
Sleep              128-1023                      0         0                                0
Sleep              1024-4095                     0         0                                0
Sleep              4096-Infinity                 0         0                                0
Before-dispatch    0-31                          9074      1                                26
Before-dispatch    32-127                        92400     59                               110
Before-dispatch    128-1023                      1         214                              214
Before-dispatch    1024-4095                     0         0                                0
Before-dispatch    4096-Infinity                 0         0                                0
Dispatch           0-31                          101475    1                                26
Dispatch           32-127                        0         0                                0
Dispatch           128-1023                      0         0                                0
Dispatch           1024-4095                     0         0                                0
Dispatch           4096-Infinity                 0         0                                0
(结果个数 = 25)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询调度线程轨迹信息（DSP-MSSSCHTRACE）_50121034.md`
