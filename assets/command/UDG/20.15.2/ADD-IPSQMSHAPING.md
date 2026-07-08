---
id: UDG@20.15.2@MMLCommand@ADD IPSQMSHAPING
type: MMLCommand
name: ADD IPSQMSHAPING（增加IPSQM整形配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IPSQMSHAPING
command_category: 配置类
applicable_nf:
- SGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 4000
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM Shaping配置
status: active
---

# ADD IPSQMSHAPING（增加IPSQM整形配置）

## 功能

**适用NF：SGW-U、UPF**

该命令用于配置基于基站的下行流量整形带宽。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为4000。
- 配置IPSQM整形速率功能时会消耗CPU，影响数据转发性能，开启前请联系华为技术人员确认。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：指定对端地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv4”时为必选参数。<br>参数含义：指定基站的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv6”时为必选参数。<br>参数含义：指定基站的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：指定基站所在VPN，如果整形配置的VPN与实际的VPN不一致，则整形失败。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| CIR | 承诺信息速率（兆比特/秒） | 可选必选说明：必选参数<br>参数含义：整形带宽大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10000，单位是兆比特每秒。<br>默认值：无<br>配置原则：无 |
| DESCRIPTION | 描述信息 | 可选必选说明：可选参数<br>参数含义：对端基站的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPSQMSHAPING]] · IPSQM整形配置（IPSQMSHAPING）

## 关联任务

- [[UDG@20.15.2@Task@0-00231]]

## 使用实例

配置基于基站的下行流量整形带宽：

```
ADD IPSQMSHAPING: IPTYPE=IPv4, PEERIPV4="10.0.0.1", CIR=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-IPSQMSHAPING.md`
