---
id: UDG@20.15.2@MMLCommand@DSP MSSSCHTHREADHEAD
type: MMLCommand
name: DSP MSSSCHTHREADHEAD（查询调度线程概要信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSSCHTHREADHEAD
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

# DSP MSSSCHTHREADHEAD（查询调度线程概要信息）

## 功能

该命令用于查询SCH的线程控制块信息。

例如，当前需要查看环境上某个线程的使用情况及部署情况，可执行该命令行查看。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| THREADID | 线程ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示线程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSSCHTHREADHEAD]] · 调度线程概要信息（MSSSCHTHREADHEAD）

## 使用实例

查询调度线程概要信息：

```
DSP MSSSCHTHREADHEAD:THREADID = 1,RUNAME = "VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------
                     线程号占用状态  =  used
                       线程调度类型  =  FIFO
                         线程优先级  =  32
                       线程绑定核号  =  2
                         系统线程号  =  8380
                    Pthread库线程号  =  1478125312
                       OSAL的任务号  =  2
                 当期调度的调度组号  =  0
                 当前正在调度功能块  =  NULL
                           维测开关  =  OFF
                     可调度的组数量  =  1
                 输入输出调度任务数  =  2
                   线程私有队列长度  =  4096
               线程私有队列入队个数  =  0
               线程私有队列出队个数  =  0
                 线程私有队列头指针  =  0
                 线程私有队列尾指针  =  0
                       绿色节能开关  =  OFF
              绿色节能休眠时间（ns） =  NULL
                   绿色节能休眠阈值  =  NULL
     绿色节能时间窗口（microsecond） =  NULL
                       绿色节能算法  =  SEMIAUTO
     绿色节能容纳时间（microsecond） =  100
 绿色节能强制睡眠阈值（microsecond） =  100
 绿色节能强制睡眠周期（microsecond） =  100
                    CPU负载统计开关  =  OFF
               CPU负载统计周期（ms） =  NULL
       调度一轮时间最大/平均值（ns） =  NULL
                     一秒内调度次数  =  NULL
                     一秒内节能次数  =  NULL
       实际休眠时间最大/平均值（ns） =  NULL
  节能模式线程收包计数器最大/平均值  =  NULL
   节能模式调度间隔最大/平均值（ns） =  NULL
                   一秒内非节能次数  =  NULL
非节能模式线程收包计数器最大/平均值  =  NULL
 非节能模式调度间隔最大/平均值（ns） =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询调度线程概要信息（DSP-MSSSCHTHREADHEAD）_00440609.md`
