---
id: UDG@20.15.2@MMLCommand@SET DNSIPRESOURCE
type: MMLCommand
name: SET DNSIPRESOURCE（设置DNS IP地址资源列表）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DNSIPRESOURCE
command_category: 配置类
applicable_nf:
- CloudEPSN
effect_mode: 立即生效
is_dangerous: false
max_records: 2
category_path:
- SFIP管理
- 第三方应用管理
- IP资源管理
status: active
---

# SET DNSIPRESOURCE（设置DNS IP地址资源列表）

## 功能

**适用NF：CloudEPSN**

该命令用于设置DNS的管理接口和业务接口IP地址资源列表。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | INTERFACETYPE | IPVERSION | IPV4ADDRS |
| --- | --- | --- | --- |
| 初始值 | Mgt | IPV4_IPV6 |  |
| 初始值 | Dns | IPV4 | 192.168.0.1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACETYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：接口类型。<br>数据来源：全网规划<br>取值范围：仅支持输入“Mgt”、“Dns”。Mgt：管理接口；Dns：业务接口。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：可选参数<br>参数含义：IP地址版本。<br>数据来源：本端规划<br>取值范围：<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>- IPV4_IPV6：同时支持IPv4和IPv6。<br>默认值：无<br>配置原则：当接口类型输入“Mgt”时，该字段不支持配置。 |
| IPV4ADDRS | IPv4地址列表 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4” 或 “IPV4_IPV6”时为必选参数。<br>参数含义：IPv4地址资源列表。<br>数据来源：全网规划<br>取值范围：不支持输入0开头的IP地址。<br>默认值：无<br>配置原则：输入合法的IP地址列表，多个IP地址之间使用空格分隔。 |
| IPV6ADDRS | IPv6地址列表 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6” 或 “IPV4_IPV6”时为必选参数。<br>参数含义：IPv6地址资源列表。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：输入合法的IP地址列表，多个IP地址之间使用空格分隔。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DNSIPRESOURCE]] · DNS IP地址资源列表（DNSIPRESOURCE）

## 使用实例

设置Dns接口类型，IPV4地址列表为192.168.0.1、192.168.0.2，运行如下命令：

```
+++    CloudEPSN/*MEID:0 MENAME:APP-VNF-CloudEPSN-X86-B003_IP60*/        2024-02-20 13:05:28
O&M    #3700
%%SET DNSIPRESOURCE: INTERFACETYPE="Dns", IPVERSION=IPV4, IPV4ADDRS="192.168.0.1 192.168.0.2";%%
RETCODE = 0  操作成功
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-DNSIPRESOURCE.md`
