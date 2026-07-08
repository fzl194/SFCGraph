---
id: UDG@20.15.2@ConfigObject@IPV4FRAGPLCY
type: ConfigObject
name: IPV4FRAGPLCY（IPv4分片策略）
nf: UDG
version: 20.15.2
object_name: IPV4FRAGPLCY
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# IPV4FRAGPLCY（IPv4分片策略）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用来配置逻辑接口的分片处理策略。

在逻辑接口IPv4组网场景下，报文入隧道加封装后，如果报文长度（根据FRAGLENGTHOPT的配置可以选择内层/外层IP报文长度）大于本端逻辑接口的IPv4 MTU，则做分片处理，可以使用该命令配置分片处理策略：

1、对于加隧道封装后内层是IPv4的报文，存在两种分片策略：一是配置成做内层IPv4分片，二是做外层IPv4分片，若之前未配置过内层为IPv4的分片策略，默认是做外层IPv4分片。在判断是否对内层IPv4报文进行分片时，可以选择与MTU相比较的是内层还是外层IP报文长度，外层报文长度包括内层IP报文长度以及外层封装部分的长度，默认采用内层IP报文长度与MTU比较。

2、对于加隧道封装后内层是IPv6的报文，存在两种策略可配置：一是做外层IPv4分片，二是回复Too Big报文，对于上行报文，给UE侧回复Too Big，对于下行报文，则给SERVER侧回复Too Big。若配置为回复Too Big，则需继续对原报文处理策略，对原报文可选择丢弃或继续按照外层分片转发，默认情况下回复Too Big报文。

3、如果配置为外层IPv4分片策略，并且隧道封装类型是IPv4，按照物理口的MTU值进行分片。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-IPV4FRAGPLCY]] · LST IPV4FRAGPLCY
- [[command/UDG/20.15.2/SET-IPV4FRAGPLCY]] · SET IPV4FRAGPLCY

## 证据

- 原始手册：`evidence/UDG/20.15.2/IPV4FRAGPLCY.md`
- 原始手册：`evidence/UDG/20.15.2/IPV4FRAGPLCY.md`
