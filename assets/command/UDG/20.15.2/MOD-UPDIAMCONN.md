---
id: UDG@20.15.2@MMLCommand@MOD UPDIAMCONN
type: MMLCommand
name: MOD UPDIAMCONN（修改Diameter链路）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: UPDIAMCONN
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- Diameter连接
- Diameter链路
status: active
---

# MOD UPDIAMCONN（修改Diameter链路）

## 功能

**适用NF：UPF**

![](修改Diameter链路（MOD UPDIAMCONN）_97080153.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改Diameter链路信息可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。

此命令用于修改SCTP Diameter链路的本端IP地址交换参数REVERSEIP。

## 注意事项

- 该命令执行后立即生效。
- 不指定LocalPort参数或指定LocalPort参数为0，都表示修改未配置本端端口号的connection。指定LocalPort参数为非0的有效值时，表示修改配置了此端口号的connection。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIAMCONNGRP | Diameter链路组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路的Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMCONNGRP命令配置生成。 |
| LOCINTERFACE | 本端接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路的本端接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PEERSCTPENDPT | 对端SCTP端点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP端点名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPSCTPENDPOINT命令配置生成。 |
| REVERSEIP | SCTP建链交换本端IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP建链是否交换本端IP地址。1个本端逻辑接口可以配置主IP地址和子IP地址，当该参数配置为ENABLE时，本地逻辑接口的子IP作为偶联的主用IP，本地逻辑接口的主IP作为偶联的从IP。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- DISABLE：不使能SCTP建链交换本端IP地址。<br>- ENABLE：使能SCTP建链交换本端IP地址。<br>默认值：无<br>配置原则：根据实际规划选择对应的枚举值。 |
| LOCALPORT | 本端端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链接的本端端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，19865～19928。<br>默认值：无<br>配置原则：可配置端口范围按照应用进行区分：Swm应用端口范围19865~19928。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMCONN]] · Diameter链路（UPDIAMCONN）

## 使用实例

根据网络规划，需要将UPF到对端的一条SCTP Diameter链路的本端IP地址交换，则可以按如下配置：

```
MOD UPDIAMCONN: DIAMCONNGRP="Grp1", LOCINTERFACE="swmif1/0/0", PeerSCTPEndpt="ep1", ReverseIP=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-UPDIAMCONN.md`
