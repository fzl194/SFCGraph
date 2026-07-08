---
id: UDG@20.15.2@MMLCommand@RMV ECHOIPLIST
type: MMLCommand
name: RMV ECHOIPLIST（删除GTP路径管理IP地址）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ECHOIPLIST
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP协议参数管理
- 路径地址列表
status: active
---

# RMV ECHOIPLIST（删除GTP路径管理IP地址）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来删除对端网元所属的GTP信令面或者数据面IP地址段，即GTP路径管理黑白名单中的地址段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定GTP路径管理黑白名单中的IPv4地址段的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4MASK | IP掩码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用来指定IPv4掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定GTP路径管理黑白名单中的IPv6地址段的地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6MASK | IP掩码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用来指定IPv6掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ECHOIPLIST]] · GTP路径管理IP地址（ECHOIPLIST）

## 使用实例

删除GTP路径管理黑白名单中IP地址为10.36.0.2，mask为27的IP地址段：

```
RMV ECHOIPLIST: IPVERSION=IPV4, IPV4ADDR="10.36.0.2", IPV4MASK=27;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除GTP路径管理IP地址（RMV-ECHOIPLIST）_82837220.md`
