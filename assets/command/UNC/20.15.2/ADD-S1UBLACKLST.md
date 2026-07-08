---
id: UNC@20.15.2@MMLCommand@ADD S1UBLACKLST
type: MMLCommand
name: ADD S1UBLACKLST（增加S1-U IP地址黑名单记录）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: S1UBLACKLST
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1-U黑名单管理
- S1-U黑名单维护
status: active
---

# ADD S1UBLACKLST（增加S1-U IP地址黑名单记录）

## 功能

**适用网元：MME**

暂不支持本命令。该命令用于增加S1-U IP地址黑名单记录。当 **[SET S1UBLACKLSTPARA](../S1-U黑名单规则/设置S1-U黑名单参数(SET S1UBLACKLSTPARA)_89145434.md)** 中 **SNDBLKLSTPLCY** 配置为NO时，如果系统在流程中接收到S-GW发送的消息中携带的S1-U IP地址为该命令中配置的IP地址时，确保系统不向eNodeB发送携带该IP地址消息。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令后，因为S1-U IP地址可能匹配中黑名单记录，4G Attach、PDN连接、TAU、Handover、SR等流程的成功率会有所下降。
- 此命令的最大记录数为256。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型，标识S1-U黑名单IP地址的类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无<br>配置原则：系统目前仅支持IPV4地址。 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要配置的S1-U IPv4黑名单地址。<br>前提条件：该参数在"IP类型"参数配置为"IPV4"后生效。<br>数据来源：整网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- IPv4地址不能为0.0.0.0、255.255.255.255和0.x.y.z。<br>- IPv4地址在本命令内必须唯一，即该命令配置的所有IPv4地址都不允许相同。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要配置的S1-U IPv6黑名单地址。<br>前提条件：该参数在"IP类型"参数配置为"IPV6"后生效。<br>数据来源：整网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、未指定地址（::）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址。<br>- IPv6地址在本命令内必须唯一，即该命令配置的所有IPv6地址都不允许相同。 |

## 操作的配置对象

- [S1-U IP地址黑名单记录（S1UBLACKLST）](configobject/UNC/20.15.2/S1UBLACKLST.md)

## 使用实例

配置系统不向eNodeB发送携带S1-U黑名单IP地址的消息，增加一条S1-U IP地址为"10.1.1.1"的黑名单记录:

ADD S1UBLACKLST: IPTYPE=IPV4, IPV4="10.1.1.1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加S1-U-IP地址黑名单记录(ADD-S1UBLACKLST)_24385877.md`
