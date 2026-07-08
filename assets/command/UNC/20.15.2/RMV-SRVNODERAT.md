---
id: UNC@20.15.2@MMLCommand@RMV SRVNODERAT
type: MMLCommand
name: RMV SRVNODERAT（删除SGSN/SGW IP与RAT类型间的映射关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SRVNODERAT
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取RAT管理
- IP地址映射RAT
status: active
---

# RMV SRVNODERAT（删除SGSN/SGW IP与RAT类型间的映射关系）

## 功能

**适用NF：GGSN**

该命令用于解除SGSN的IP地址段与RAT类型的映射关系。当运营商需要删除映射表中的一段SGSN的IP地址与RAT类型的映射关系表项时，使用此命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置IP地址版本类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4。<br>- “IPV6（IPV6）”：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SRVNODESTARTV4 | Service Node的起始IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IP地址段的起始IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODEENDV4 | Service Node的结束IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IP地址段的结束IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODESTARTV6 | Service Node的起始IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IP地址段的起始IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SRVNODEENDV6 | Service Node的结束IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IP地址段的结束IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SGSN/SGW IP与RAT类型间的映射关系（SRVNODERAT）](configobject/UNC/20.15.2/SRVNODERAT.md)

## 使用实例

删除映射表中一SGSN IP地址段与RAT的映射关系，IP地址段的起始IP地址为“10.1.1.1”，结束IP地址为“10.2.2.2”：

```
RMV SRVNODERAT: IPVERSION=IPV4, SRVNODESTARTV4="10.1.1.1", SRVNODEENDV4="10.2.2.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SGSN_SGW-IP与RAT类型间的映射关系（RMV-SRVNODERAT）_09653671.md`
