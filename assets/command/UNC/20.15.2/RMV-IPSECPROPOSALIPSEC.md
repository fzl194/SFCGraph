---
id: UNC@20.15.2@MMLCommand@RMV IPSECPROPOSALIPSEC
type: MMLCommand
name: RMV IPSECPROPOSALIPSEC（删除IPsec提议）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPSECPROPOSALIPSEC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- IPsec
- IPsec提议
status: active
---

# RMV IPSECPROPOSALIPSEC（删除IPsec提议）

## 功能

![](删除IPsec提议（RMV IPSECPROPOSALIPSEC）_26150763.assets/notice_3.0-zh-cn_2.png)

删除该配置会影响业务流量使用IPSEC进行加解密功能，有业务影响。

该命令用于删除IPsec安全提议。

## 注意事项

- 该命令执行后立即生效。

- 当安全提议被IPsec策略引用时，安全提议不能被删除。如果需要删除安全提议，必须先删除安全提议的引用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROPOSALNAME | Proposal名称 | 可选必选说明：必选参数<br>参数含义：Proposal名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPSECPROPOSALIPSEC]] · IPsec提议（IPSECPROPOSALIPSEC）

## 使用实例

删除名称为“asdf2”的IPsec安全提议：

```
RMV IPSECPROPOSALIPSEC:PROPOSALNAME="asdf2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IPSECPROPOSALIPSEC.md`
