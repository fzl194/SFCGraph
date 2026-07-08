---
id: UNC@20.15.2@MMLCommand@RMV IPSECPROPOSAL
type: MMLCommand
name: RMV IPSECPROPOSAL（删除IPsec提议）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPSECPROPOSAL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- IPsec
- IPsec提议
status: active
---

# RMV IPSECPROPOSAL（删除IPsec提议）

## 功能

该命令用于删除IP安全提议。

## 注意事项

- 该命令执行后立即生效。
- 当安全提议被安全联盟SA（Security Association）引用时，安全提议不能被删除。如果需要删除安全提议，必须先删除安全提议的引用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROPOSALNAME | Proposal名称 | 可选必选说明：必选参数<br>参数含义：Proposal名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无 |

## 操作的配置对象

- [IPsec提议（IPSECPROPOSAL）](configobject/UNC/20.15.2/IPSECPROPOSAL.md)

## 使用实例

删除名称为“asdf2”的IP安全提议：

```
RMV IPSECPROPOSAL:PROPOSALNAME="asdf2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IPsec提议（RMV-IPSECPROPOSAL）_50120786.md`
