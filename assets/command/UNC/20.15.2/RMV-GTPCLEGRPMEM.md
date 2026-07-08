---
id: UNC@20.15.2@MMLCommand@RMV GTPCLEGRPMEM
type: MMLCommand
name: RMV GTPCLEGRPMEM（删除GTP-C本地实体组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCLEGRPMEM
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C本地实体组成员
status: active
---

# RMV GTPCLEGRPMEM（删除GTP-C本地实体组成员）

## 功能

![](删除GTP-C本地实体组成员（RMV GTPCLEGRPMEM）_09651766.assets/notice_3.0-zh-cn_2.png)

删除GTPCLEGRPMEM会影响GTP-C建链，请确认要删除的GTPCLEGRPMEM不会被使用。

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于删除GTP-C本地实体组成员。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C本地实体的组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。<br>默认值：无<br>配置原则：<br>该参数需要从ADD GTPCLEGRP命令中已配置的GRPID参数中取值。 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示GTP-C本地实体的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPv4（IPv4）<br>- IPv6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指示GTP-C本地实体的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。<br>IP地址不能与GTPCLE中已配置的IP地址相同。 |
| IPV6ADDR | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指示GTP-C本地实体的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>IP地址不能与GTPCLE中已配置的IP地址相同。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCLEGRPMEM]] · GTP-C本地实体组成员（GTPCLEGRPMEM）

## 使用实例

删除组号为0的GTP-C本地实体组成员，成员IPv4地址为192.168.1.1。

```
RMV GTPCLEGRPMEM:GROUPID=0,IPTYPE=IPv4,IPV4ADDR="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GTPCLEGRPMEM.md`
