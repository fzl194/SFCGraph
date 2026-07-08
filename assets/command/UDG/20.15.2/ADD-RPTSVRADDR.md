---
id: UDG@20.15.2@MMLCommand@ADD RPTSVRADDR
type: MMLCommand
name: ADD RPTSVRADDR（添加报表服务器接入点配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RPTSVRADDR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 110
category_path:
- 业务报表管理
- 报表服务器管理
- 报表服务器地址
status: active
---

# ADD RPTSVRADDR（添加报表服务器接入点配置）

## 功能

**适用NF：PGW-U、UPF**

该命令增加报表服务器接入点。在配置好报表服务器后，增加接入点时执行该命令。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为110。
- 一个报表服务器最多配置10个接入点。
- 当报表消息类型为EXP时，无需本端规划报表服务器地址。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACCESSNAME | 接入点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置对应的接入点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RPTSVRNAME | 报表服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置对应的报表服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：报表服务器名称是RptSvr已经配置的报表服务器名称。 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Ip地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4_ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于设置IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6_ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于设置Ipv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SVRPORT | 端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置报表服务器端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：10700<br>配置原则：无 |
| VPNINSTANCE | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无<br>配置原则：<br>- 绑定VPN时需要确保该VPN已经配置（ADD VPNINST）。<br>- 若ADD LOGICINF中绑定VPN实例，此参数也需要绑定VPN实例。 |

## 操作的配置对象

- [报表服务器接入点配置（RPTSVRADDR）](configobject/UDG/20.15.2/RPTSVRADDR.md)

## 使用实例

增加报表服务器IP接入点时，配置该命令：

```
ADD RPTSVRADDR: ACCESSNAME="access01", RPTSVRNAME="report01", IPTYPE=IPV4, IPV4_Addr="192.168.2.3";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加报表服务器接入点配置（ADD-RPTSVRADDR）_06213372.md`
