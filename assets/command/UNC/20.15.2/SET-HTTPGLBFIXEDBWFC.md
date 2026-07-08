---
id: UNC@20.15.2@MMLCommand@SET HTTPGLBFIXEDBWFC
type: MMLCommand
name: SET HTTPGLBFIXEDBWFC（设置HTTP全局固定带宽流控）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HTTPGLBFIXEDBWFC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP全局固定带宽流控管理
status: active
---

# SET HTTPGLBFIXEDBWFC（设置HTTP全局固定带宽流控）

## 功能

![](设置HTTP全局固定带宽流控（SET HTTPGLBFIXEDBWFC）_56474481.assets/notice_3.0-zh-cn_2.png)

门限值由本端和对端网元的消息处理能力决定。设置过低会导致消息被丢弃，设置过高起不到保护本端和对端网元不过载的作用。

该命令用于设置HTTP全局固定带宽流控门限等信息，设置后所有链路都使用相同的参数控制。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SENDFCSWITCH | RECVFCSWITCH | SENDTHD | RECVTHD | SENDBIGPKTTHD | RECVBIGPKTTHD | STATUSCODE |
| --- | --- | --- | --- | --- | --- | --- |
| OFF | OFF | 0 | 0 | 0 | 0 | TooManyRequests |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SENDFCSWITCH | 全局固定带宽流控出局开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置全局固定带宽流控出局开关。<br>数据来源：全网规划<br>取值范围：<br>- “ON（开启）”：开启HTTP全局固定带宽流控功能<br>- “OFF（关闭）”：关闭HTTP全局固定带宽流控功能<br>默认值：无。<br>配置原则：无 |
| RECVFCSWITCH | 全局固定带宽流控入局开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置全局固定带宽流控入局开关。<br>数据来源：全网规划<br>取值范围：<br>- “ON（开启）”：开启HTTP全局固定带宽流控功能<br>- “OFF（关闭）”：关闭HTTP全局固定带宽流控功能<br>默认值：无。<br>配置原则：无 |
| SENDTHD | 发送消息带宽流控门限(KBytes/s) | 可选必选说明：该参数在"SENDFCSWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于指定发送消息带宽流控门限，控制粒度为链路，设置后所有链路都生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPGLBFIXEDBWFC查询当前参数配置值。<br>配置原则：<br>门限值由对端网元的消息处理能力决定。设置过低会导致消息被丢弃，设置过高起不到保护对端网元不过载的作用。 |
| RECVTHD | 接收消息带宽流控门限(KBytes/s) | 可选必选说明：该参数在"RECVFCSWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于指定接收消息带宽流控门限，控制粒度为链路，设置后所有链路都生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPGLBFIXEDBWFC查询当前参数配置值。<br>配置原则：<br>门限值由本端网元的消息处理能力决定。设置过低会导致消息被丢弃，设置过高起不到保护本端网元不过载的作用。 |
| SENDBIGPKTTHD | 发送消息大包阈值(KByte) | 可选必选说明：该参数在"SENDFCSWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于指定发送消息大包阈值，超过该阈值的报文才会被丢弃，小于该阈值的报文不流控。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是千字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPGLBFIXEDBWFC查询当前参数配置值。<br>配置原则：无 |
| RECVBIGPKTTHD | 接收消息大包阈值(KByte) | 可选必选说明：该参数在"RECVFCSWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于指定接收消息大包阈值，超过该阈值的报文才会被丢弃，小于该阈值的报文不流控。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是千字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPGLBFIXEDBWFC查询当前参数配置值。<br>配置原则：无 |
| STATUSCODE | 状态码 | 可选必选说明：该参数在"SENDFCSWITCH"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指定接收消息速率超过流控门限时，给对端网元响应的HTTP消息中的Status Code。<br>数据来源：全网规划<br>取值范围：<br>- “TooManyRequests（Too Many Requests）”：当NF服务生产者检测到给定NF服务消费者发送过多的流量时，可以发送该状态代码告知NF服务消费者生产者端即将过载。<br>- “ServiceUnavailable（Service Unavailable）”：当NF服务生产者检测到给定NF服务消费者发送过多的流量时，可以发送该状态代码告知NF服务消费者生产者端已经过载。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPGLBFIXEDBWFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPGLBFIXEDBWFC]] · HTTP全局固定带宽流控（HTTPGLBFIXEDBWFC）

## 使用实例

以开启出局带宽流控，大包阈值为1024KB，接收带宽阈值为15000KB/s为例，配置如下：

```
SET HTTPGLBFIXEDBWFC: SENDFCSWITCH=ON,RECVFCSWITCH=OFF,SENDTHD=15000,SENDBIGPKTTHD=1024;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-HTTPGLBFIXEDBWFC.md`
