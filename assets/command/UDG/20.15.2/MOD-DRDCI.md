---
id: UDG@20.15.2@MMLCommand@MOD DRDCI
type: MMLCommand
name: MOD DRDCI（修改DC间通信通道信息）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: DRDCI
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# MOD DRDCI（修改DC间通信通道信息）

## 功能

![](修改DC间通信通道信息（MOD DRDCI）_85910093.assets/notice_3.0-zh-cn.png)

该命令为修改容灾控制通道信息，可能导致业务中断，需要按照激活主备容灾指导书进行操作，请勿自行执行该命令。

该命令用于修改DC间通信通道信息。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定容灾组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：<br>可通过<br>[**LST DRGROUPINFO**](查询容灾组信息（LST DRGROUPINFO）_74835153.md)<br>命令获取返回结果中的容灾组标识作为参数输入。 |
| IPVERSION | IP版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于配置容灾控制通道IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4类型地址）<br>- IPV6（IPv6类型地址）<br>默认值：无<br>配置原则：无 |
| LDCIP | 本端DC通信IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于配置本端容灾控制通道IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PDCIP | 对端DC通信IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于配置对端容灾控制通道IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LDCIPV6 | 本端DC通信IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于配置本端容灾控制通道IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PDCIPV6 | 对端DC通信IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于配置对端容灾控制通道IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>输入的参数VPN实例名称，需要提前通过ADD VPNINST命令进行配置，或者使用默认的VPN实例“_public_”。“_public_”是公网缺省的VPN实例名，不能通过LST VPNINST命令查询出来。 |
| HBINTERVAL | 心跳探测时长(100ms) | 可选必选说明：可选参数<br>参数含义：该参数用于配置容灾控制通道的心跳探测时长，单位为100ms。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：无<br>配置原则：无 |
| HBTIMES | 心跳重传次数 | 可选必选说明：可选参数<br>参数含义：该参数用于配置容灾控制通道的心跳重传次数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~30。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DC间通信通道信息（DRDCI）](configobject/UDG/20.15.2/DRDCI.md)

## 使用实例

修改DC间通信通道信息

```
%%MOD DRDCI: DRGROUPID=1, IPVERSION=IPV4, LDCIP="172.16.3.4", PDCIP="172.16.5.6", VPNINSTANCE="12345", HBINTERVAL=5, HBTIMES=5;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改DC间通信通道信息（MOD-DRDCI）_85910093.md`
