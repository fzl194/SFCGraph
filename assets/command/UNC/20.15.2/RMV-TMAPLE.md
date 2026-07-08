---
id: UNC@20.15.2@MMLCommand@RMV TMAPLE
type: MMLCommand
name: RMV TMAPLE（删除TMAP本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TMAPLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Tm接口管理
- Tm接口参数管理
status: active
---

# RMV TMAPLE（删除TMAP本地实体）

## 功能

**适用网元：MME**

该命令用于删除TMAP本地实体。

## 注意事项

- 该命令执行后立即生效。
- 删除本端TMAP本地实体后，与对端实体无法交互并且将导致宽带集群业务功能不能使用。

## 权限

manage-ug，system-ug，monitor-ug，visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMINTFTP | Tm接口类型 | 可选必选说明：必选参数<br>参数含义：宽带集群业务Tm接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “Tm1(用户会话接口)”<br>默认值 ：无<br>配置原则：<br>- Tm1接口需要配置不同的IP地址，作为本端服务IP地址，否则将配置失败。 |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定TMAP本地实体的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值 ：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IP地址类型”参数配置为“IPV4”后生效。<br>参数含义：本参数用于指定TMAP本地实体的IPv4地址。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>说明：IP地址必须在SERVICEIP表中已经配置，可以用<br>[**LST SERVICEIP**](../../业务IP管理/业务IP/查询业务IP(LST SERVICEIP)_72226047.md)<br>查询。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IP地址类型”参数配置为“IPV6”后生效。<br>参数含义：本参数用于指定TMAP本地实体的IPv6地址。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- IP地址不能与GTPCLEGRPMEM中已配置的IP地址相同。<br>说明：- IP地址必须在SERVICEIP表中已经配置，可以用[**LST SERVICEIP**](../../业务IP管理/业务IP/查询业务IP(LST SERVICEIP)_72226047.md)查询。<br>- 系统暂不支持IPV6地址。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TMAPLE]] · TMAP本地实体（TMAPLE）

## 使用实例

删除“IPv4地址”为“10.10.10.1”的TMAP本地实体时，执行命令。

```
RMV TMAPLE: TMINTFTP=Tm1,IPT=IPV4, IPV4="10.10.10.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除TMAP本地实体(RMV-TMAPLE)_41153601.md`
