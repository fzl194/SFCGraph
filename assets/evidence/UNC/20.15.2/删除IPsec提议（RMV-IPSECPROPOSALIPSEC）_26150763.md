# 删除IPsec提议（RMV IPSECPROPOSALIPSEC）

- [命令功能](#ZH-CN_MMLREF_0000001226150763__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001226150763__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001226150763__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001226150763__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001226150763)

![](删除IPsec提议（RMV IPSECPROPOSALIPSEC）_26150763.assets/notice_3.0-zh-cn_2.png)

删除该配置会影响业务流量使用IPSEC进行加解密功能，有业务影响。

该命令用于删除IPsec安全提议。

## [注意事项](#ZH-CN_MMLREF_0000001226150763)

- 该命令执行后立即生效。

- 当安全提议被IPsec策略引用时，安全提议不能被删除。如果需要删除安全提议，必须先删除安全提议的引用。

#### [操作用户权限](#ZH-CN_MMLREF_0000001226150763)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001226150763)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROPOSALNAME | Proposal名称 | 可选必选说明：必选参数<br>参数含义：Proposal名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001226150763)

删除名称为“asdf2”的IPsec安全提议：

```
RMV IPSECPROPOSALIPSEC:PROPOSALNAME="asdf2";
```
