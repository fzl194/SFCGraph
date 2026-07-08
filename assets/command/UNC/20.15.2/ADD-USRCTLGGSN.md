---
id: UNC@20.15.2@MMLCommand@ADD USRCTLGGSN
type: MMLCommand
name: ADD USRCTLGGSN（增加手工恢复GGSN地址）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: USRCTLGGSN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 20
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GGSN容灾功能
status: active
---

# ADD USRCTLGGSN（增加手工恢复GGSN地址）

## 功能

**适用网元：SGSN**

该命令用于增加需手工恢复的GGSN地址。

如果由于网络等原因导致到某个GGSN的通信经常中断，为了避免业务的频繁切换，可以通过此命令屏蔽该GGSN，在确认故障完全排除后，再恢复到该GGSN的业务。

当 UNC 检测到本表中配置的GGSN故障恢复后，产生ALM-12605 GTPC路径恢复正常需手工启动新业务接入告警，并且只有在经过操作员人工确认（ [**RES USRCTLGGSN**](恢复可用的GGSN地址(RES USRCTLGGSN)_72345507.md) ）后，才选择故障恢复后的GGSN业务。

## 注意事项

- 本命令执行后立即生效。
- 执行本命令添加一条记录后，指定的GGSN故障恢复后，必须要通过执行[**RES USRCTLGGSN**](恢复可用的GGSN地址(RES USRCTLGGSN)_72345507.md)命令才能使GGSN重新被启用。
- 本表最大记录数为20。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：此参数用于指定GGSN网元的IP地址类型。<br>数据来源：与对端网元协商<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：此参数用于指定GGSN网元的IPv4类型的地址。<br>数据来源：与对端网元协商<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>说明：“0.0.0.0”和“255.255.255.255”是无效的IP地址。<br>配置原则：<br>- IPv4地址不能为0.0.0.0、255.255.255.255和0.x.y.z。<br>- IPv4地址不能为组播地址（如：224.x.y.z）和环回地址(如：127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：此参数用于指定GGSN网元的IPv6类型地址。<br>数据来源：与对端网元协商<br>取值范围： ::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：此参数用于指定记录的描述信息。<br>取值范围：0~32位字符串<br>默认值：无<br>配置原则：描述信息应该是有意义的字符串。 |

## 操作的配置对象

- [手工恢复GGSN地址（USRCTLGGSN）](configobject/UNC/20.15.2/USRCTLGGSN.md)

## 使用实例

增加GGSN地址192.168.66.6为需手工恢复：

ADD USRCTLGGSN: IPT=IPV4, IPV4="192.168.66.6";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加手工恢复GGSN地址(ADD-USRCTLGGSN)_72345505.md`
