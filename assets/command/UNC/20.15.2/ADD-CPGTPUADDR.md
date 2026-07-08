---
id: UNC@20.15.2@MMLCommand@ADD CPGTPUADDR
type: MMLCommand
name: ADD CPGTPUADDR（增加CP GTP-U地址）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CPGTPUADDR
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N4 GTP-U管理
- N4 GTP-U地址管理
status: active
---

# ADD CPGTPUADDR（增加CP GTP-U地址）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于增加与UPF对接的本端用户面地址。

## 注意事项

- 该命令执行后立即生效。

- IPv4和IPv6最多可以分别输入1条记录。
- 当UPLOGICINTF的IPVERSION为V4V6时，IPVERSION需配置为IPv6。
- IP地址和VPN名称必须在LOGICIP表中已经配置，可以用LST LOGICIP查询。

- 最多可输入2条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定与UPF对接的本端GTP-U IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定与UPF对接的本端GTP-U IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。IPv4地址类型。业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定与UPF对接的本端GTP-U IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。IPv6地址类型。IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>默认值：无<br>配置原则：无 |
| VPN | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定与UPF对接的本端GTP-U使用的VPN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：_public_<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPGTPUADDR]] · CP GTP-U地址（CPGTPUADDR）

## 使用实例

添加一个与UPF对接的本端GTP-U地址，IPv4地址为192.168.0.20：

```
ADD CPGTPUADDR:IPVERSION=IPV4,IPV4ADDR="192.168.0.20";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CPGTPUADDR.md`
