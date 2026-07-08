---
id: UDG@20.15.2@MMLCommand@SET TORELIABLECFG
type: MMLCommand
name: SET TORELIABLECFG（设置TCP可靠性配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TORELIABLECFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP可靠性配置
status: active
---

# SET TORELIABLECFG（设置TCP可靠性配置）

## 功能

**适用NF：UPF**

该命令用于设置TCP可靠性配置信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TCPRETRIES1 | TCPRETRIES2 | KEEPALIVETIME | TCPREORDERING | TCPMTUPROBING | FLOWCTRLSW | TCPEARLYRETRANS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 3 | 5 | 480 | 3 | DISABLE | CTRL_BESED_APP_BUFFER | 2 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TCPRETRIES1 | TCP重试次数1 | 可选必选说明：可选参数<br>参数含义：设置放弃回应一个未完成建链的TCP连接前﹐需要进行多少次重试。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围3～100。<br>默认值：无<br>配置原则：无 |
| TCPRETRIES2 | TCP重试次数2 | 可选必选说明：可选参数<br>参数含义：设置放弃回应一个已完成建链的TCP连接前﹐需要进行多少次重试。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围3～100。<br>默认值：无<br>配置原则：无 |
| KEEPALIVETIME | TCP保活探测时间 | 可选必选说明：可选参数<br>参数含义：设置TCP保活探测时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～7200。<br>默认值：无<br>配置原则：无 |
| TCPREORDERING | TCP流中重排序的数据报最大数量 | 可选必选说明：可选参数<br>参数含义：设置TCP流中重排序的数据报最大数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～100。<br>默认值：无<br>配置原则：无 |
| TCPMTUPROBING | TCP的MTU探测功能 | 可选必选说明：可选参数<br>参数含义：设置开启TCP的MTU探测功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| FLOWCTRLSW | TCP流控策略 | 可选必选说明：可选参数<br>参数含义：设置应用层的TCP流控策略。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：DISABLE。<br>- CTRL_BASED_TCP_SNDBUFF：按照TCP发送缓存是否阻塞控制。<br>- CTRL_BESED_APP_BUFFER：按照应用层缓存规格控制。<br>默认值：无<br>配置原则：无 |
| TCPEARLYRETRANS | 是否启动ER和TLP算法 | 可选必选说明：可选参数<br>参数含义：设置是否启动(Early Retransmit)ER和(Tail Loss Probe)TLP算法。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～4。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TORELIABLECFG]] · TCP可靠性配置（TORELIABLECFG）

## 使用实例

设置TCP重试次数1为3，设置TCP重试次数2为5，设置TCP保活探测时间为480秒，设置TCP流中重排序的数据报最大数量为3，开启TCP的MTU探测功能，关闭TCP流控策略，启动ER和TLP算法：

```
SET TORELIABLECFG: TCPRETRIES1=3, TCPRETRIES2=5, KEEPALIVETIME=480, TCPREORDERING=3, TCPMTUPROBING=ENABLE, FLOWCTRLSW=DISABLE, TCPEARLYRETRANS=3;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TCP可靠性配置（SET-TORELIABLECFG）_31139809.md`
