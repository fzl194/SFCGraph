---
id: UDG@20.15.2@MMLCommand@SET TORESMGTCFG
type: MMLCommand
name: SET TORESMGTCFG（设置TCP资源管理配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TORESMGTCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP资源管理配置
status: active
---

# SET TORESMGTCFG（设置TCP资源管理配置）

## 功能

**适用NF：UPF**

该命令用于设置TCP资源管理配置信息。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TCPTWREUSESW | TCPFINTIMEOUT | FINWAIT2TIMEOUT | MAXTWBUCKETS |
| --- | --- | --- | --- | --- |
| 初始值 | ENABLE | 5 | 5 | 6000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TCPTWREUSESW | 重用处于time_wait的socket | 可选必选说明：可选参数<br>参数含义：设置是否开启快速回收处于TIME-WAIT状态的sockets。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| TCPFINTIMEOUT | TCP在FIN_WAIT_2状态的时间 | 可选必选说明：可选参数<br>参数含义：设置TCP在FIN_WAIT_2状态的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～72。<br>默认值：无<br>配置原则：无 |
| FINWAIT2TIMEOUT | 应用层控制的FIN_WAIT_2状态存活时间的计算因子 | 可选必选说明：可选参数<br>参数含义：设置应用层控制的FIN_WAIT_2状态存活时间的计算因子。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1000。<br>默认值：无<br>配置原则：无 |
| MAXTWBUCKETS | TCP代理允许处于TIME_WAIT状态的socket个数的上限值 | 可选必选说明：可选参数<br>参数含义：设置TCP代理允许处于TIME_WAIT状态的socket个数的上限值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～1000000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TORESMGTCFG]] · TCP资源管理配置（TORESMGTCFG）

## 使用实例

设置开启快速回收处于TIME-WAIT状态的sockets，设置TCP在FIN_WAIT_2状态的时间为3秒，应用层控制的FIN_WAIT_2状态存活时间的计算因子为3，TCP代理允许处于TIME_WAIT状态的socket个数的上限值为5000：

```
SET TORESMGTCFG: TCPTWREUSESW=ENABLE, TCPFINTIMEOUT=3, FINWAIT2TIMEOUT=3, MAXTWBUCKETS=5000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TCP资源管理配置（SET-TORESMGTCFG）_44249098.md`
