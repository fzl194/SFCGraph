---
id: UNC@20.15.2@MMLCommand@RMV GTPCLE
type: MMLCommand
name: RMV GTPCLE（删除GTP-C本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCLE
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- Gtpc本端实体管理
status: active
---

# RMV GTPCLE（删除GTP-C本地实体）

## 功能

![](删除GTP-C本地实体(RMV GTPCLE)_72225645.assets/notice_3.0-zh-cn_2.png)

删除GTP-C本地实体可能导致大量业务失败。

**适用网元：SGSN、MME、AMF**

该命令用于删除GTPC本地实体。

## 注意事项

- 该命令在版本升级过程中不能执行。
- 非0号组的记录执行删除时，若该记录是本组的最后一个IP地址记录，且被GTP-C IP地址接口属性表（[**LST GTPCINTFATTR**](../GTP-C接口类型属性/查询GTP-C IP地址接口属性(LST GTPCINTFATTR)_26145902.md)）引用，则删除失败。
- 若删除的记录的IP地址被GTP-C路径白名单表（[**LST GTPCWHITELIST**](../GTP-C协议管理/GTP-C路径白名单/查询GTP-C路径白名单(LST GTPCWHITELIST)_26305728.md)）引用，则删除失败。
- 若删除的记录的IP地址被S11接口子网配置（[**LST S11INTFSUBNET**](../S11接口管理/S-GWIP地址配置/查询S11接口子网配置 (LST S11INTFSUBNET)_19337754.md)）引用，则删除失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DELTYPE | 删除类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定删除GTPC本端实体的Key类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYINDEX(根据记录索引)”<br>- “BYIP(根据IP地址)”<br>默认值：“BYINDEX(根据记录索引)” |
| LEINDEX | GTP-C本端实体标识 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定删除GTPC本端实体的记录索引。<br>前提条件：该参数在<br>“删除类型”<br>参数配置为<br>“BYINDEX(根据记录索引)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无<br>说明：使用<br>[**LST GTPCLE**](查询GTP-C本地实体(LST GTPCLE)_72345567.md)<br>查询记录的索引。 |
| GROUPID | 组号 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体对应的组号。组号用于组网规划时不同接口，或者不同用户范围使用独立的GTPC本端实体。<br>前提条件：该参数在<br>“删除类型”<br>参数配置为<br>“BYIP(根据IP地址)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~32<br>默认值：无<br>说明：组号的应用参考<br>[**ADD GTPCINTFATTR**](../GTP-C接口类型属性/增加GTP-C IP地址接口属性(ADD GTPCINTFATTR)_72225579.md)<br>命令帮助。 |
| IPTYPE | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的IP地址类型。<br>前提条件：该参数在<br>“删除类型”<br>参数配置为<br>“BYIP(根据IP地址)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPv4)”<br>- “TPTADDR_TYPE_IPV6(IPv6)”<br>默认值：无 |
| LEIPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV4(IPv4)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LEIPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV6(IPv6)”<br>后生效。<br>数据来源：本端规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCLE]] · GTP-C本地实体（GTPCLE）

## 使用实例

删除索引为1的GTPC本地实体：

RMV GTPCLE: DELTYPE=BYINDEX, LEINDEX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GTPCLE.md`
