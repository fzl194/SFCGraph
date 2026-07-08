---
id: UDG@20.15.2@ConfigObject@IPSECPOLICY6
type: ConfigObject
name: IPSECPOLICY6（IPsec IPv6策略）
nf: UDG
version: 20.15.2
object_name: IPSECPOLICY6
object_kind: entity
status: active
---

# IPSECPOLICY6（IPsec IPv6策略）

## 说明

![](增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.assets/notice_3.0-zh-cn.png)

该命令影响协商及加解密性能，命令中的部分配置可能是不安全的。

该命令用于增加IPsec Ipv6策略。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令中的一些配置可能是不安全的。
> - DH组dh_group1、dh_group2、dh_group5和dh_group14都是不安全的，建议dh_group19，但dh_group19计算较慢。
> - 每个policy下最大支持128个sequence。
> - 若IPsec policy绑定Tunnel口后，在新增该policy sequence场景下，新增policy sequence的sequence number必须比已存在的sequence number大。如需增加较小sequence number的policy sequence，需先解绑IPsec policy，会影响现有IPsec业务。
> - 一个ACL组不能同时绑定两个policy。
> - 在指定ACL规则组时，数字型ACL填写于ACLNUMBER、字符型ACL填写于ACLNAME，两者不可同时配置。
> - 使能数据流可信（TFC）会对性能造成很大影响。
> - 当前版本暂不支持双栈，ACLTYPE不可设置为AclIPv4。
> - IKEv1国密IPSEC不支持ESN/RFC 6311/TFC。
> - IKEv1国密IPSEC不支持主备隧道。
> - IPV6不支持“Round_robin（轮询）”工作模式，配置“Round_robin（轮询）”实际以“Master_standby（主备）”工作模式生效。
> - ikev1情况下不支持关闭按流量计长功能。
> - workmode配置为masterstand开启热备功能时，需将主备模式两个IKEPEER配置完整，否则会有呼损的风险。
> - 当配置“SA按时计长”字段值为0时，该字段会采用[**SET IKEGLOBALCONFIG**](../IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)命令中TIMESADURTN参数的取值。
>
> - 最多可输入4000条记录。

## 操作本对象的命令

- [ADD IPSECPOLICY6](command/UDG/20.15.2/ADD-IPSECPOLICY6.md)
- [LST IPSECPOLICY6](command/UDG/20.15.2/LST-IPSECPOLICY6.md)
- [MOD IPSECPOLICY6](command/UDG/20.15.2/MOD-IPSECPOLICY6.md)
- [RMV IPSECPOLICY6](command/UDG/20.15.2/RMV-IPSECPOLICY6.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPsec-IPv6策略（MOD-IPSECPOLICY6）_68200989.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPsec-IPv6策略（RMV-IPSECPOLICY6）_68200999.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPsec-Ipv6策略（ADD-IPSECPOLICY6）_68320981.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPsec-IPv6策略（LST-IPSECPOLICY6）_68200975.md`
