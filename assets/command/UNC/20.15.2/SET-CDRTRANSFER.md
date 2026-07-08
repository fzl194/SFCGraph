---
id: UNC@20.15.2@MMLCommand@SET CDRTRANSFER
type: MMLCommand
name: SET CDRTRANSFER（设置话单发送控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CDRTRANSFER
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- 话单发送参数
status: active
---

# SET CDRTRANSFER（设置话单发送控制参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

设置话单发送控制参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- SET CDRTRANSFER命令的五个字段都是可选参数，如果参数没有输入，不做任何修改；如果参数有输入，则修改输入的字段。
- CG故障或者负载过重的情况下，话单重传时间间隔会有所延长。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | GTPPMAXPAYLOAD | RETRANSTIMES | RETRANSINTERVAL | NARESTRANSINTVL | CGSELECTIONMODE | UDPCHECKSUM |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 1400 | 3 | 3 | 5 | PDP_BASED_LB | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPPMAXPAYLOAD | GTP'消息最大可携带的话单字节数 | 可选必选说明：可选参数<br>参数含义：设置通过GTP’消息发送话单时，每个GTP’消息携带话单数据的最大字节数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1200～7180。<br>默认值：无<br>配置原则：该参数仅对新生成的GTP’消息生效。当配置值改大时，可能出现对端CG由于自身处理能力较弱而无法响应GTP’消息的情况，这可能引发UNC产生“ALM-81021 CG无响应”告警。建议修改前请联系华为技术工程师。 |
| RETRANSTIMES | Echo and Data Record Transfer Request重传次数 | 可选必选说明：可选参数<br>参数含义：用于配置遵循GTP’协议的Echo Request消息和Data Record Transfer Request消息的重发次数。该参数表示UNC发送Echo Request消息或者Data Record Transfer Request消息次数达到该值仍未收到CG服务器的响应，将认为CG服务器的状态是异常的，继续发送EchoRequest消息或Data Record Transfer Request消息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～3。<br>默认值：无<br>配置原则：无 |
| RETRANSINTERVAL | Data Record Transfer Request重传时间间隔（秒） | 可选必选说明：可选参数<br>参数含义：用于配置遵循GTP’协议的Data Record Transfer Request消息的重发时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。<br>默认值：无<br>配置原则：无 |
| NARESTRANSINTVL | Node Alive消息重传时间间隔（秒） | 可选必选说明：可选参数<br>参数含义：指定node-alive消息的超时重发时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～600。<br>默认值：无<br>配置原则：无 |
| CGSELECTIONMODE | CG选择模式 | 可选必选说明：可选参数<br>参数含义：控制发送话单时如何选择CG。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSG_BASED_LB：基于消息的负载均衡。如果配置为MSG_BASED_LB，表示发送话单时根据负载均衡算法选择发送的CG，即从状态正常、优先级最高的CG中选择当前发送窗口负载最少的CG。<br>- PDP_BASED_LB：基于PDP/Bearer的负载均衡。如果配置为PDP_BASED_LB，表示发送话单时，如果激活时获取的CG状态正常，则向此CG发送话单。如果激活时获取的CG状态不正常，则以轮选算法重新获取CG地址发送话单，即从状态正常、优先级最高的CG中依次获取CG。<br>默认值：无<br>配置原则：当CGSELECTIONMODE配置为PDP_BASED_LB时，PCRF下发的备CG不生效。 |
| UDPCHECKSUM | GTP'报文CheckSum开关 | 可选必选说明：可选参数<br>参数含义：该参数表示GTP'报文是否携带checksum。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRTRANSFER]] · 话单发送控制参数（CDRTRANSFER）

## 使用实例

设置话单发送控制参数，GTPPMaxPayload为“2000”，Echo and Data Record Transfer Request重传次数为“3”，Data Record Transfer Request重传时间间隔为“3”，Node Alive消息重传时间间隔为“10”，CGSelectionMode为“MSG_BASED_LOAD_SHARING”：

```
SET CDRTRANSFER:GTPPMAXPAYLOAD=2000,RETRANSTIMES=3,RETRANSINTERVAL=3,NARESTRANSINTVL=10,CGSELECTIONMODE=MSG_BASED_LB;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CDRTRANSFER.md`
