---
id: UNC@20.15.2@MMLCommand@ACT RECYCLE
type: MMLCommand
name: ACT RECYCLE（回收地址）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: RECYCLE
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 回收地址
status: active
---

# ACT RECYCLE（回收地址）

## 功能

![](回收地址（ACT RECYCLE）_64343816.assets/notice_3.0-zh-cn_2.png)

使用该命令后会将强制回收正在使用的地址，对应的正常在线用户将被强制下线。

**适用NF：PGW-C、SMF、GGSN**

ACT RECYCLE命令用于回收本地或DHCP类型的地址池中的一个或一段地址。修改系统配置时，如果需要对某个地址池/段进行动态修改或删除，但地址池内有地址已经分配出去，这时候就需要利用ACT RECYCLE命令来强制回收分配出去的地址。

## 注意事项

- 该命令执行后立即生效。

- 该命令仅适用于本地或DHCP类型的地址池。
- 如果想要修改和删除的地址池中地址已经分配出去，首先要锁定地址所在的地址池或地址段，然后强制回收已分配的地址或地址段，最后才能够对地址池或地址段进行动态修改或删除。
- 回收地址范围不可以跨地址段。这里回收的不一定是整个段，可以是地址段内的某个子段。当起始地址和结束地址相同时，表示只回收一个地址。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| RECYCLETYPE | 回收类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址回收类型。<br>数据来源：本端规划<br>取值范围：<br>- IPSEGMENT（IP网段回收）<br>- POOL（地址池回收）<br>- SECTION（地址段回收）<br>默认值：IPSEGMENT<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：该参数在"RECYCLETYPE"配置为"IPSEGMENT"时为条件必选参数。<br>参数含义：该参数用于指定地址池的地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4<br>- “IPv6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| V4STARTIP | IPv4起始地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：1.0.0.0~255.255.255.254。<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址（127.x.y.z）。<br>- IPv4地址必须是A、B或者C类地址。<br>- 起始IP地址必须小于或等于结束IP地址。 |
| V4ENDIP | IPv4结束地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4地址段的结束地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：1.0.0.0~255.255.255.254。<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址（127.x.y.z）。<br>- IPv4地址必须是A、B或者C类地址。<br>- 结束IP地址必须大于或等于起始IP地址。 |
| V6PREFIXSTART | IPv6前缀起始地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6地址段的起始地址前缀。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。<br>- 前缀地址段的起始地址必须小于或等于结束地址，每个IPv6地址段最多可以配置1048576个地址，且同一VPN下，各个前缀地址段里的地址不能相互重叠，IPv6地址的前缀长度默认为64 bit。 |
| V6PREFIXEND | IPv6前缀结束地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6地址段的结束地址前缀。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。<br>- 前缀地址段的起始地址必须小于或等于结束地址，每个IPv6地址段最多可以配置1048576个地址，且同一VPN下，各个前缀地址段里的地址不能相互重叠，IPv6地址的前缀长度默认为64 bit。 |
| SECTIONINDEX | 地址段编号 | 可选必选说明：该参数在"RECYCLETYPE"配置为"SECTION"时为条件必选参数。<br>参数含义：该参数在地址回收类型为地址段的场景下，用于指定地址回收网段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RECYCLE]] · 回收地址（RECYCLE）

## 使用实例

强制回收本地IPv4地址池lap中的地址“10.1.1.0~10.1.1.20”，“POOLNAME”为“lap”，“IPVERSION”为“IPv4”，“STARTIP”为“10.1.1.0”，“ENDIP”为“10.1.1.20”：

```
ACT RECYCLE: POOLNAME="lap", IPVERSION=IPv4, V4STARTIP="10.1.1.0", V4ENDIP="10.1.1.20", CONFIRM=Y;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-RECYCLE.md`
