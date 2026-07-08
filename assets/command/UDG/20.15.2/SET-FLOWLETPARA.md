---
id: UDG@20.15.2@MMLCommand@SET FLOWLETPARA
type: MMLCommand
name: SET FLOWLETPARA（设置大流优化参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FLOWLETPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
- SGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 流量转发管理
- 大流检测功能
status: active
---

# SET FLOWLETPARA（设置大流优化参数）

## 功能

![](设置大流优化参数(SET FLOWLETPARA)_83137140.assets/notice_3.0-zh-cn.png)

修改该参数配置会影响数据转发性能和大流优化效果，请谨慎修改。

**适用NF：PGW-U、UPF、SGW-U**

该命令为配置类命令，用于配置大流优化参数。

> **说明**
> - 该命令执行后立即生效。
> - 最多可输入1条记录。
> - 执行该命令修改参数配置会影响数据转发性能和大流优化效果，请谨慎修改。
> - 该命令存在系统初始记录，参数的初始设置值如下表：
>   | FLOWOPTSW | THREADUPDINT | FLOWCHKPPS | FLOWGUARDPKTNUM | FLOWGUARDTIME | CPUOVERLOADTHR | CPUBIASDIFF |
>   | --- | --- | --- | --- | --- | --- | --- |
>   | DISABLE | 256 | 78000 | 64 | 10 | 80 | 15 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWOPTSW | 大流优化功能 | 可选必选说明：可选参数<br>参数含义：该参数用于配置大流优化功能开关。<br>数据来源：本端规划<br>取值范围：<br>- "DISABLE(关闭大流优化)"：关闭大流优化<br>- "ENABLE(开启大流优化)"：开启大流优化<br>- "FLOWCHK(开启大流检测)"：开启大流检测<br>默认值：无<br>配置原则：无 |
| THREADUPDINT | 线程负载更新间隔 | 可选必选说明：<br>- 该参数在"FLOWOPTSW"配置为"FLOWCHK"时为条件可选参数。<br>- 该参数在"FLOWOPTSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数表示线程CPU负载更新周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64~256，单位是毫秒。64-256。<br>默认值：无<br>配置原则：无 |
| FLOWCHKPPS | 大流检测速率 | 可选必选说明：<br>- 该参数在"FLOWOPTSW"配置为"FLOWCHK"时为条件可选参数。<br>- 该参数在"FLOWOPTSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数设置大流检测速率，当某个业务访问的速率超过参数时，会认定为大象流。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为50000~5000000，单位是包每秒。50000-5000000。<br>默认值：无<br>配置原则：无 |
| FLOWGUARDPKTNUM | 大流优化保护报文数 | 可选必选说明：<br>- 该参数在"FLOWOPTSW"配置为"FLOWCHK"时为条件可选参数。<br>- 该参数在"FLOWOPTSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数表示启动大流优化后，两次优化间的切换报文数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~65535，单位是包数。0-65535。<br>默认值：无<br>配置原则：无 |
| FLOWGUARDTIME | 大流优化的保护时间 | 可选必选说明：<br>- 该参数在"FLOWOPTSW"配置为"FLOWCHK"时为条件可选参数。<br>- 该参数在"FLOWOPTSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数表示启动大流优化后，两次优化间的切换保护时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~500，单位是毫秒。5-500。<br>默认值：无<br>配置原则：无 |
| CPUOVERLOADTHR | 启动优化的线程CPU阈值 | 可选必选说明：<br>- 该参数在"FLOWOPTSW"配置为"FLOWCHK"时为条件可选参数。<br>- 该参数在"FLOWOPTSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置启动大流优化线程CPU阈值。当线程CPU占用率同时满足优化启动阈值和偏差阈值时，启动大流优化。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为50~90，单位是百分比。50-90。<br>默认值：无<br>配置原则：无 |
| CPUBIASDIFF | 启动优化的线程CPU偏差阈值 | 可选必选说明：<br>- 该参数在"FLOWOPTSW"配置为"FLOWCHK"时为条件可选参数。<br>- 该参数在"FLOWOPTSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置启动大流优化线程CPU偏差阈值。线程CPU偏差阈值表示线程CPU占用率与进程CPU平均占用率的差值，当线程CPU占用率同时满足优化启动阈值和偏差阈值时，启动大流优化。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~50，单位是百分比。5-50。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FLOWLETPARA]] · 大流优化参数（FLOWLETPARA）

## 关联任务

- [[UDG@20.15.2@Task@0-00279]]

## 使用实例

```
SET FLOWLETPARA: FLOWOPTSW=FLOWCHK, THREADUPDINT=256, FLOWCHKPPS=78000, FLOWGUARDPKTNUM=64, FLOWGUARDTIME=10, CPUOVERLOADTHR=80, CPUBIASDIFF=15;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-FLOWLETPARA.md`
