---
id: UNC@20.15.2@MMLCommand@RMV UPFRDSSVR
type: MMLCommand
name: RMV UPFRDSSVR（删除中转UPF与Radius服务器的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPFRDSSVR
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- UPF中转Radius服务器
status: active
---

# RMV UPFRDSSVR（删除中转UPF与Radius服务器的绑定关系）

## 功能

![](删除中转UPF与Radius服务器的绑定关系（RMV UPFRDSSVR）_35273631.assets/notice_3.0-zh-cn_2.png)

删除RADIUS服务器的相关属性可能会导致RADIUS服务器连接失败，RADIUS鉴权计费失败等问题。

**适用NF：PGW-C、SMF**

删除中转UPF与Radius服务器的绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERTYPE | 服务器类型 | 可选必选说明：必选参数<br>参数含义：指定RADIUS服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- “AUTHENTICATION（鉴权服务器）”：表示鉴权服务器。<br>- “ACCOUNTING（计费服务器）”：表示计费服务器。<br>默认值：无<br>配置原则：无 |
| IPVERSION | 服务器IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS服务器IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”：IPv4<br>- “IPV6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| SERVERIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：RADIUS服务器IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD RDSSVR**](../Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)<br>命令配置生成。 |
| SERVERIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：RADIUS服务器IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD RDSSVR**](../Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)<br>命令配置生成。 |
| UPLISTNAME | UP列表名称 | 可选必选说明：可选参数<br>参数含义：指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |

## 操作的配置对象

- [中转UPF与Radius服务器的绑定关系（UPFRDSSVR）](configobject/UNC/20.15.2/UPFRDSSVR.md)

## 使用实例

当对端删除RADIUS服务器，本端需要根据对端服务器删除配置时：删除地址为“192.168.10.1”的计费服务器：

```
RMV UPFRDSSVR: SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="192.168.10.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除中转UPF与Radius服务器的绑定关系（RMV-UPFRDSSVR）_35273631.md`
