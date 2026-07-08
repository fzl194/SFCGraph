---
id: UNC@20.15.2@MMLCommand@RMV CPCGBINDING
type: MMLCommand
name: RMV CPCGBINDING（删除抄送CG绑定）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CPCGBINDING
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- 抄送CG绑定
status: active
---

# RMV CPCGBINDING（删除抄送CG绑定）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来删除抄送CG绑定关系。支持批量删除，给CPCGGRPID字段赋值，删除指定CPCGGRPID的记录；给CPCGGRPID和CGIPADDR/CGIPADDR字段赋值，删除满足条件的记录。

## 注意事项

- 该命令执行后立即生效。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPCGGRPID | 抄送CG组ID | 可选必选说明：必选参数<br>参数含义：指定抄送CG组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。整数1。<br>默认值：无<br>配置原则：无 |
| CGIPVERSION | CG IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CG IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：无<br>配置原则：无 |
| CGIPV4ADDR | CG IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CGIPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：CG服务器IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CGIPV6ADDR | CG IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CGIPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：CG服务器的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CGPORT | CG端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CGIPVERSION”配置为“IPV4” 或 “IPV6”时为可选参数。<br>参数含义：CG服务器端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1024～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [抄送CG绑定关系（CPCGBINDING）](configobject/UNC/20.15.2/CPCGBINDING.md)

## 使用实例

删除CG绑定关系，抄送CG组ID为1，CG的IP地址为192.168.0.2，CG的端口号为25009，抄送CG组ID为1：

```
RMV CPCGBINDING: CPCGGRPID=1, CGIPVERSION=IPV4, CGIPV4ADDR="192.168.0.2", CGPORT=25009;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除抄送CG绑定（RMV-CPCGBINDING）_09896871.md`
