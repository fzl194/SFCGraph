---
id: UNC@20.15.2@MMLCommand@ADD SCTPTEMPLATE
type: MMLCommand
name: ADD SCTPTEMPLATE（增加SCTP模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCTPTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 20
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- SCTP管理
- SCTP模板
status: active
---

# ADD SCTPTEMPLATE（增加SCTP模板）

## 功能

**适用NF：PGW-C、SMF**

此命令用于创建SCTP模板，根据现网规划，当UNC需要使用SCTP承载逻辑接口信令时，可以使用此命令创建SCTP模板并配置SCTP协议参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为20。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPTEMPLNAME | SCTP模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| HEARTBEATINTVAL | SCTP发送心跳消息的间隔周期（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端向远端IP地址发送心跳消息的间隔周期。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为10～60000，单位是毫秒。<br>默认值：30000<br>配置原则：<br>- 当耦联SCTP在指定时间内没有将数据发送至远端IP地址，则耦联SCTP会向该IP地址发送心跳消息，检查远端IP地址是否激活。<br>- 心跳消息发送间隔由HEARTBEATINTVAL参数和SET GLBSCTPPARA命令的RTOMINVALUE参数共同控制。 |
| MAXASSOCRETRY | SCTP耦联上消息重传的最大次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在一个SCTP耦联上允许消息连续重传的最大次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～254。<br>默认值：5<br>配置原则：<br>- 如果SCTP耦联消息连续重发次数大于本参数，则系统认为对端SCTP端点不可达，于是会自动放弃SCTP耦联，并通知SCTP用户层该SCTP耦联不可用。<br>- 该参数取值不得大于所有偶联远端地址的最大路径重发次数总和，并且不得小于最大路径重发次数。 |
| MAXPATHRETRY | SCTP到特定IP消息重传的最大次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在一个SCTP耦联上允许向某个特定的IP地址进行消息连续重传的最大次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～253。<br>默认值：4<br>配置原则：如果某个SCTP耦联上向某个特定的IP地址进行消息连续重传的最大次数大于最大路径重发次数，则认为对端IP地址不可达。此时，如果数据配置了多个对端目的IP，本耦联将自动将当前使用的目的IP切换为下一个可用的IP地址，需要指出的是，如果本耦联优先使用主用IP，则当主用IP从不可用状态变为可用状态时，该SCTP耦联将自动切换到主用IP上。 |
| CHECKSUMTYPE | SCTP协议校验和算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端的SCTP协议支持哪种校验和算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CRC32：表示本端的SCTP协议支持的校验和算法为CRC32。<br>- ADLER32：表示本端的SCTP协议支持的校验和算法为ADLER32。<br>默认值：CRC32<br>配置原则：无 |
| CONGESTLEVEL | 拥塞状态门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP耦联处于拥塞状态时的缓存占用百分比门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～79，单位是百分比。<br>默认值：60<br>配置原则：当发送缓存与总发送缓存的比值大于该参数指定的门限并且小于“80”时，耦联处于低拥塞状态（从无拥塞状态算起）。 |
| CONGESTCLRLEVEL | 解除拥塞状态门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP耦联进入拥塞状态以后，SCTP耦联的信令负荷解除拥塞状态的缓存占用百分比门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为40～59，单位是百分比。<br>默认值：40<br>配置原则：门限是指信令发送缓冲区被占用的百分比。当SCTP耦联进入拥塞状态后，如果后续已经使用的发送缓冲区与总发送缓冲区的比值小于该参数指定的门限时，则系统将解除SCTP耦联的拥塞状态。 |
| DELIVERYMODE | SCTP Data Chunk传输模式 | 可选必选说明：可选参数<br>参数含义：该参数用户设置SCTP协议Data Chunk的传输模式。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- ORDERED：SCTP Data Chunk传输模式为顺序传输。<br>- UNORDERED：SCTP Data Chunk传输模式为非顺序传输。<br>默认值：ORDERED<br>配置原则：<br>- 设置UNC发送SCTP协议DATA chunk的传输模式为非顺序传输时，Diameter对端需要对非顺序到达的消息能够正常处理，否则将会对业务造成影响。<br>- UNC支持对Diameter对端按顺序模式或非顺序模式发送SCTP协议DATA chunk，且不需要配置控制。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPTEMPLATE]] · SCTP模板（SCTPTEMPLATE）

## 使用实例

根据网络规划，需要新增一个SCTP模板，则可以按如下配置：

```
ADD SCTPTEMPLATE: SCTPTEMPLNAME="sctp_tp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SCTPTEMPLATE.md`
