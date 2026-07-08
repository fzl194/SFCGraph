---
id: UDG@20.15.2@MMLCommand@ADD INTERFACEIPSEC
type: MMLCommand
name: ADD INTERFACEIPSEC（增加接口）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: INTERFACEIPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- 接口配置
status: active
---

# ADD INTERFACEIPSEC（增加接口）

## 功能

该命令用于增加逻辑接口并初始化该接口的相关配置，逻辑接口是指能够实现数据交换功能但物理上不存在、需要通过配置建立的接口。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令在版本升级过程中禁止执行。
>
> - 最多可输入65535条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：无 |
| IFDESCR | 接口描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口描述，可标识接口的用途。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~242。<br>默认值：无<br>配置原则：无 |
| IFADMINSTATUS | 管理状态 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该接口的管理状态。<br>数据来源：本端规划<br>取值范围：<br>- “Down（接口Down）”：接口Down<br>- “Up（接口Up）”：接口Up<br>默认值：无<br>配置原则：无 |
| IFMTU | 接口最大传输单元 (byte) | 可选必选说明：可选参数<br>参数含义：该参数用于设置该接口的最大传输单元。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是46~9600，单位是字节。<br>默认值：无<br>配置原则：<br>- 接口MTU默认值为1500。<br>- 正常通信情况下，建议MTU的值不要随意更改，采用系统默认值1500。由于部分协议对最小报文有限制，如果配置过小会导致协议邻居无法建立。 |
| IFDF | 接口不分片标记 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该接口是否启用IP报文强制分片功能。IP报文头中包含一个用于指示是否允许对报文分片的标志位DF（Don't Fragment）。通常情况下，如果DF被置为1，则设备不能再对该报文分片。当IP报文长度大于接口的MTU时，例如由于协议封装导致长度增加，该报文将被丢弃并发送ICMP差错报文，从而引起数据丢失。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：FALSE<br>配置原则：无 |
| IFSTATIENABLE | 接口统计使能标记 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该接口统计使能标志。若用户需要查看接口接收、发送报文的统计计数时，必须先使能接口流量统计功能。<br>数据来源：本端规划<br>取值范围：<br>- FALSE（不使能）<br>- TRUE（使能）<br>默认值：无<br>配置原则：无 |
| IFTRAPENABLE | 接口Trap使能标记 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否使能接口Down的告警上报。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| IFSTATITVL | 接口统计时间间隔 (s) | 可选必选说明：可选参数<br>参数含义：该参数用于设置接口的流量统计时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~600，单位是秒。<br>默认值：无<br>配置原则：<br>统计间隔必须是10的倍数。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@INTERFACEIPSEC]] · 接口（INTERFACEIPSEC）

## 使用实例

新建Loopback接口LoopBack4，并将接口description设置为“huawei”：

```
ADD INTERFACEIPSEC: IFNAME="LoopBack4", IFDESCR="huawei";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-INTERFACEIPSEC.md`
