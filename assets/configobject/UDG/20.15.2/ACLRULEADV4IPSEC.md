---
id: UDG@20.15.2@ConfigObject@ACLRULEADV4IPSEC
type: ConfigObject
name: ACLRULEADV4IPSEC（高级ACL规则）
nf: UDG
version: 20.15.2
object_name: ACLRULEADV4IPSEC
object_kind: entity
status: active
---

# ACLRULEADV4IPSEC（高级ACL规则）

## 说明

该命令用于创建高级ACL规则。

高级ACL可以基于五元组（源目的IP，源目的端口号，协议号）进行报文匹配。

> **说明**
> - 该命令执行后立即生效。
>
> - 增加ACL规则前必须先执行[**ADD ACLGROUPIPSEC**](../ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)指定所在规则组。
> - 参数ACLPROTOCOL为TCP(6)、UDP(17)时，端口号相关参数(ACLSRCPORTOP、ACLSRCPORTBEGIN、ACLSRCPORTEND、ACLDESTPORTOP、ACLDESTPORTBEGIN、ACLDESTPORTEND)才生效。当OP选项为“Lt”时，只有结束端口号可以输入值，当OP选项为“Gt”、“Eq”、“Neq”时，只有起始端口号可以输入，当前OP选项为“Range”时，起始和结束端口号都必须输入值。
> - 参数ACLSYNFLAG只有在参数ACLPROTOCOL为TCP(6)时才生效。
> - 参数ACLICMPNAME、ACLICMPTYPE、ACLICMPCODE只有在参数ACLPROTOCOL为ICMP(1)时才生效。可以通过ACLICMPNAME直接输入知名ICMP报文，而不用输入ICMPTYPE和ICMPCODE，如果用户需要自定义输入ICMPTYPE和ICMPCODE，ACLICMPNAME需要输入为“Custom”。
> - 参数ACLTTLOP，ACLTTL，ACLTTLEND之间存在输入限制。当参数ACLTTLOP选项为“Lt”时，只有ACLTTLEND可以输入值；当ACLTTLOP选项为“Gt”、“Eq”、“Neq”时，只有ACLTTL可以输入值；当ACLTTLOP选项为“Range”时，ACLTTL和ACLTTLEND都必须输入值。
> - ACL规则中不可带有重复或具有包含关系的源目的地址。
> - IKEv1场景下的ACL规则不支持narrow down。即一端配置的ACL规则范围被包含于另一端配置的ACL规则范围内的情况下，仍能正常协商出IPSEC SA。
>
> - 最多可输入65535条记录。

## 操作本对象的命令

- [ADD ACLRULEADV4IPSEC](command/UDG/20.15.2/ADD-ACLRULEADV4IPSEC.md)
- [LST ACLRULEADV4IPSEC](command/UDG/20.15.2/LST-ACLRULEADV4IPSEC.md)
- [MOD ACLRULEADV4IPSEC](command/UDG/20.15.2/MOD-ACLRULEADV4IPSEC.md)
- [RMV ACLRULEADV4IPSEC](command/UDG/20.15.2/RMV-ACLRULEADV4IPSEC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改高级ACL规则（MOD-ACLRULEADV4IPSEC）_80751068.md`
- 原始手册：`evidence/UDG/20.15.2/删除高级ACL规则（RMV-ACLRULEADV4IPSEC）_25830699.md`
- 原始手册：`evidence/UDG/20.15.2/增加高级ACL规则（ADD-ACLRULEADV4IPSEC）_80751058.md`
- 原始手册：`evidence/UDG/20.15.2/查询高级ACL规则配置（LST-ACLRULEADV4IPSEC）_80592502.md`
