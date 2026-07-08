---
id: UNC@20.15.2@MMLCommand@SET IPV6GLOBALCONFIG
type: MMLCommand
name: SET IPV6GLOBALCONFIG（设置IPv6全局配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IPV6GLOBALCONFIG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6全局配置
status: active
---

# SET IPV6GLOBALCONFIG（设置IPv6全局配置）

## 功能

该命令用于设置IPv6全局配置。

## 注意事项

- 该命令执行后立即生效。
- 可选参数至少下发一个。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| BUCKETSIZE | INTERVAL | TIMEOUT | BLACKLISTFLAG | TOOBIGLIMIT |
| --- | --- | --- | --- | --- |
| 10 | 100 | 10 | FALSE | TRUE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BUCKETSIZE | ICMPv6差错报文桶深限制 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICMPv6差错报文的令牌桶可容纳的令牌数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～200。<br>默认值：无 |
| INTERVAL | ICMPv6差错报文速率限制（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定向ICMPv6差错报文令牌桶中放置令牌的间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147483647，单位是毫秒。<br>默认值：无 |
| TIMEOUT | 老化时间（min） | 可选必选说明：可选参数<br>参数含义：该参数用于配置动态PMTU表项的老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～100，单位是分钟。<br>默认值：无 |
| BLACKLISTFLAG | 允许IPv6黑名单报文 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否允许IPv6黑名单报文向源端回应报文。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| TOOBIGLIMIT | TOO-BIG差错报文限制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否限制TOO-BIG差错报文。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPV6GLOBALCONFIG]] · IPv6全局配置（IPV6GLOBALCONFIG）

## 使用实例

设置IPv6全局配置参数：令牌桶深10，每隔10ms放一次令牌，路径MTU的老化时间为10分钟，允许IPv6黑名单报文向源端回应报文，ICMP报文类型为TOO-BIG报文：

```
SET IPV6GLOBALCONFIG:BUCKETSIZE=10,INTERVAL=10,TIMEOUT=10,BLACKLISTFLAG=TRUE,TOOBIGLIMIT=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IPV6GLOBALCONFIG.md`
