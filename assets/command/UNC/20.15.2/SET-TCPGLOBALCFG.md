---
id: UNC@20.15.2@MMLCommand@SET TCPGLOBALCFG
type: MMLCommand
name: SET TCPGLOBALCFG（设置TCP全局配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TCPGLOBALCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- TCP全局配置
status: active
---

# SET TCPGLOBALCFG（设置TCP全局配置）

## 功能

该命令用来设置TCP相关的全局配置。

以下参数说明IPv4和IPv6共用：

设置TCP FIN-Wait超时时间：当TCP的连接状态由FIN_WAIT_1变为FIN_WAIT_2时启动FIN-Wait定时器。若FIN-Wait定时器超时前仍未收到FIN报文，则TCP连接被终止。

设置TCP SYN-Wait超时时间：当发送SYN报文时，TCP启动SYN-Wait定时器，若SYN-Wait超时前未收到回应报文，则TCP连接将被终止。

设置TCP连接的MSS最大值大小：TCP在建立连接时，会协商MSS值(Maximum Segment Size)，它表示本端所能接收报文（TCP报文的静荷，不包含TCP头）的最大长度。

设置面向连接Socket的窗口值：该配置会变更TCP默认缓冲区窗口大小，当TCP连接建立时会使用这个设置的缓冲区值协商建立TCP会话。

## 注意事项

- 该命令执行后立即生效。
- 可选参数至少下发一个。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| TCPFINTIMEOUT | TCPSYNTIMEOUT | TCPWINDOW | ENABLEPMTU | TCP6FINTIMEOUT | TCP6SYNTIMEOUT | TCP6WINDOW | TCPMAXMSS | TCP6MAXMSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 675 | 75 | 8 | FALSE | 675 | 75 | 8 | 65535 | 65535 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TCPFINTIMEOUT | TCP FIN-Wait超时时间（s） | 可选必选说明：可选参数<br>参数含义：该参数表示TCP FIN-Wait定时器的取值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为76～3600，单位是秒。<br>默认值：无 |
| TCPSYNTIMEOUT | TCP SYN-Wait超时时间（s） | 可选必选说明：可选参数<br>参数含义：该参数表示TCP SYN-Wait定时器的取值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～600，单位是秒。<br>默认值：无 |
| TCPWINDOW | TCP窗口值（KB） | 可选必选说明：可选参数<br>参数含义：该参数表示面向连接Socket的缓冲区大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32，单位是千字节。<br>默认值：无 |
| ENABLEPMTU | PMTU功能开关 | 可选必选说明：可选参数<br>参数含义：该参数表示是否使能PMTU开关。只有使能了该标记，TCPPMTUTIMEOUT才可进行配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：去使能。<br>- TRUE：使能。<br>默认值：无 |
| TCPPMTUTIMEOUT | PMTU老化时间（min） | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENABLEPMTU”配置为“TRUE”时为必选参数。<br>参数含义：该参数表示PMTU老化时间。当同一网络上的主机互相进行通信时，该网络的MTU对通信双方非常重要。但当主机间要通过很多网络才能通信时，对通信双方最重要的是通信路径中最小的MTU，因为在通信路径上不同网络的链路层MTU不同。通信路径中最小的MTU被称为路径MTU（PMTU）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～100，单位是分钟。<br>默认值：无 |
| TCP6FINTIMEOUT | IPv6 TCP FIN-Wait超时时间（s） | 可选必选说明：可选参数<br>参数含义：该参数表示IPv6 TCP FIN-Wait定时器的取值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为76～3600，单位是秒。<br>默认值：无 |
| TCP6SYNTIMEOUT | IPv6 TCP SYN-Wait超时时间（s） | 可选必选说明：可选参数<br>参数含义：该参数表示IPv6 TCP SYN-Wait定时器的取值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～600，单位是秒。<br>默认值：无 |
| TCP6WINDOW | IPv6 TCP窗口值（KB） | 可选必选说明：可选参数<br>参数含义：该参数表示IPv6面向连接Socket的缓冲区大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32，单位是千字节。<br>默认值：无 |
| TCPMAXMSS | 最大MSS值（byte） | 可选必选说明：可选参数<br>参数含义：该参数表示TCP连接的MSS最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为32～9600，65535，单位是字节。65535为无效值。<br>默认值：无 |
| TCP6MAXMSS | IPv6最大MSS值（byte） | 可选必选说明：可选参数<br>参数含义：该参数表示IPv6 TCP连接的MSS最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为32～9600，65535，单位是字节。65535为无效值。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TCPGLOBALCFG]] · TCP全局配置（TCPGLOBALCFG）

## 使用实例

设置全局TCP配置：

```
SET TCPGLOBALCFG: TCPFINTIMEOUT=1000, TCPSYNTIMEOUT=500, TCPWINDOW=16, ENABLEPMTU=FALSE, TCP6FINTIMEOUT=1000, TCP6SYNTIMEOUT=500, TCP6WINDOW=16, TCPMAXMSS=1500;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置TCP全局配置（SET-TCPGLOBALCFG）_00440885.md`
