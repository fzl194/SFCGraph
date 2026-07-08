---
id: UNC@20.15.2@MMLCommand@RMV IPV6IFICMPSECURITY
type: MMLCommand
name: RMV IPV6IFICMPSECURITY（删除接口下安全配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPV6IFICMPSECURITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- 接口下IPv6安全配置
status: active
---

# RMV IPV6IFICMPSECURITY（删除接口下安全配置）

## 功能

该命令用于删除接口下安全配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ACTION | 发送还是接收 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对ICMP数据包采取的操作的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- rcvPkt：接收报文。<br>- sndPkt：发送报文。<br>默认值：无 |
| CONFIGTYPE | 配置的类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示配置的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- USER：用户自定义。<br>- PKTTYPE：报文类型。<br>默认值：无 |
| ICMPTYPE | 收发报文的TYPE | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“USER”时为必选参数。<br>参数含义：该参数用于表示ICMP6报文类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| ICMPCODE | 收发报文的CODE | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“USER”时为必选参数。<br>参数含义：该参数用于表示ICMP6报文编码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| PKTTYPE | 报文类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“PKTTYPE”时为必选参数。<br>参数含义：该参数用于表示报文类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HOST_UNREATCHABLE：主机不可达（Type=1, Code=3）。<br>- PORT_UNREATCHABLE：端口不可达（Type=1, Code=4）。<br>- HOP_LIMIT_EXCEEDED：TTL超时（Type=3, Code=0）。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6IFICMPSECURITY]] · 接口下安全配置（IPV6IFICMPSECURITY）

## 使用实例

删除接口下安全配置：

```
RMV IPV6IFICMPSECURITY:IFNAME="Ethernet65/0/8",ACTION=sndPkt,CONFIGTYPE=PKTTYPE,PKTTYPE=HOST_UNREATCHABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IPV6IFICMPSECURITY.md`
