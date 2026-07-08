---
id: UNC@20.15.2@MMLCommand@DSP MSSSCHTHREADHEADM
type: MMLCommand
name: DSP MSSSCHTHREADHEADM（显示调度线程概要信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSSCHTHREADHEADM
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSSCHTHREADHEADM（显示调度线程概要信息）

## 功能

该命令用于显示SCH的线程控制块信息。

例如，当前需要查看环境上某个线程的使用情况及部署情况，可执行该命令行查看。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| THREADID | 线程ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示线程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：使用<br>**[DSP MSSSCHSUMTAILM](显示调度部署详细信息（DSP MSSSCHSUMTAILM）_92520023.md)**<br>查看线程逻辑ID。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MSSSCHTHREADHEADM]] · 调度线程概要信息（MSSSCHTHREADHEADM）

## 使用实例

显示类型为aa的微服务bb内调度线程概要信息：

```
DSP MSSSCHTHREADHEADM: CELLTYPE="aa", CELLINSTANCE="bb", THREADID=1;
```

```
RETCODE = 0  操作成功。

结果如下
--------
                     线程号占用状态  =  used
                         系统线程号  =  328
                    Pthread库线程号  =  941121584
                       OSAL的任务号  =  1
                       绿色节能开关  =  ON
             绿色节能休眠时间（ns）  =  1000
                   绿色节能休眠阈值  =  100
    绿色节能时间窗口（microsecond）  =  5
                    CPU负载统计开关  =  OFF
              CPU负载统计周期（ms）  =  --
           调度一轮时间最大值（ns）  =  --
           调度一轮时间平均值（ns）  =  --
                     一秒内调度次数  =  --
                     一秒内节能次数  =  --
           实际休眠时间最大值（ns）  =  --
           实际休眠时间平均值（ns）  =  --
       节能模式线程收包计数器最大值  =  --
       节能模式线程收包计数器平均值  =  --
       节能模式调度间隔最大值（ns）  =  --
       节能模式调度间隔平均值（ns）  =  --
                   一秒内非节能次数  =  --
     非节能模式线程收包计数器最大值  =  --
     非节能模式线程收包计数器平均值  =  --
     非节能模式调度间隔最大值（ns）  =  --
     非节能模式调度间隔平均值（ns）  =  --
                       线程调度类型  =  OTHER
                         线程优先级  =  0
                       绿色节能算法  =  DEFAULT
    绿色节能容纳时间（microsecond）  =  --
绿色节能强制睡眠阈值（microsecond）  =  --
绿色节能强制睡眠周期（microsecond）  =  --
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSSCHTHREADHEADM.md`
