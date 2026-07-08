---
id: UNC@20.15.2@ConfigObject@IFIPV6ADDRPOLICY
type: ConfigObject
name: IFIPV6ADDRPOLICY（IPv6地址策略）
nf: UNC
version: 20.15.2
object_name: IFIPV6ADDRPOLICY
object_kind: entity
status: active
---

# IFIPV6ADDRPOLICY（IPv6地址策略）

## 说明

该命令用于添加IPv6地址策略。当网络管理者需要指定和预知系统发送报文的源/目的地址时，可以通过该命令定义一组地址选择规则，这些规则构成地址选择策略表。该表类似于路由表，使用最长匹配原则查找规则。地址选择的结果是由源地址和目的地址共同决定的。

## 操作本对象的命令

- [ADD IFIPV6ADDRPOLICY](command/UNC/20.15.2/ADD-IFIPV6ADDRPOLICY.md)
- [LST IFIPV6ADDRPOLICY](command/UNC/20.15.2/LST-IFIPV6ADDRPOLICY.md)
- [MOD IFIPV6ADDRPOLICY](command/UNC/20.15.2/MOD-IFIPV6ADDRPOLICY.md)
- [RMV IFIPV6ADDRPOLICY](command/UNC/20.15.2/RMV-IFIPV6ADDRPOLICY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IPv6地址策略（MOD-IFIPV6ADDRPOLICY）_49802314.md`
- 原始手册：`evidence/UNC/20.15.2/删除IPv6地址策略（RMV-IFIPV6ADDRPOLICY）_50121374.md`
- 原始手册：`evidence/UNC/20.15.2/查询IPv6地址策略（LST-IFIPV6ADDRPOLICY）_00840557.md`
- 原始手册：`evidence/UNC/20.15.2/添加IPv6地址策略（ADD-IFIPV6ADDRPOLICY）_49801666.md`
