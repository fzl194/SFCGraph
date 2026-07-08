---
id: UNC@20.15.2@MMLCommand@RMV GTPULE
type: MMLCommand
name: RMV GTPULE（删除GTP-U本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPULE
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-U接口管理
- Gtpu本端实体管理
status: active
---

# RMV GTPULE（删除GTP-U本地实体）

## 功能

**适用网元：SGSN、MME**

本命令用于删除GTPU本端实体。

## 注意事项

- 本命令执行后立即生效。
- 删除GTPU本端实体会造成使用该GTPU本端实体的在线用户的数传中断，用户需重新激活才能恢复。
- 非0号组且非32号组的记录执行删除时，若该记录是本组的最后一个IP地址记录，且被GTP-U IP地址接口属性表（[**LST GTPUINTFATTR**](../GTP-U接口类型属性/查询GTP-U IP地址接口属性(LST GTPUINTFATTR)_72345585.md)）引用，则删除失败。
- 若删除的记录的IP地址被S11接口子网配置（[**LST S11INTFSUBNET**](../../GTP-C接口管理/S11接口管理/S-GWIP地址配置/查询S11接口子网配置 (LST S11INTFSUBNET)_19337754.md)）引用，则删除失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DELTYPE | 删除类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定删除GTPU本端实体的Key类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYINDEX(根据记录索引)”<br>- “BYIP(根据IP地址)”<br>默认值：BYINDEX(根据记录索引) |
| INDEX | 记录索引 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定删除GTPU本端实体的记录索引。<br>前提条件：该参数在<br>“删除条件”<br>参数配置为<br>“BYINDEX(根据记录索引)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~65535<br>默认值：无<br>说明：使用<br>[**LST GTPULE**](查询GTP-U本地实体(LST GTPULE)_26305792.md)<br>查询记录的索引。 |
| GROUPID | 组号 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPU本端实体对应的组号。组号用于组网规划时不同接口，或者不同用户范围使用独立的GTPU本端实体。<br>前提条件：该参数在<br>“删除条件”<br>参数配置为<br>“BYIP(根据IP地址)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~32<br>默认值：无<br>说明：组号的应用参考<br>[**ADD GTPUINTFATTR**](../GTP-U接口类型属性/增加GTP-U IP地址接口属性(ADD GTPUINTFATTR)_26145984.md)<br>命令帮助。 |
| IPTYPE | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPU本端实体的IP地址类型。<br>前提条件：该参数在<br>“删除条件”<br>参数配置为<br>“BYIP(根据IP地址)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPV4)”<br>- “TPTADDR_TYPE_IPV6(IPV6)”<br>默认值：无 |
| LEIPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPU本端实体的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV4(IPV4)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LEIPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPU本端实体的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV6(IPV6)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPULE]] · GTP-U本地实体（GTPULE）

## 使用实例

删除GTPU本地实体，索引为1：

RMV GTPULE: DELTYPE=BYINDEX, INDEX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GTPULE.md`
