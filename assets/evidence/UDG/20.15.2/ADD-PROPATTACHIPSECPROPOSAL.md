# 增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）

- [命令功能](#ZH-CN_MMLREF_0000001180592500__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001180592500__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001180592500__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001180592500__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001180592500)

该命令用于增加IPsec策略的提议。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令不支持用户级IPSEC。
>
> - 最多可输入2000条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001180592500)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001180592500)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：IPsec策略的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 序列号 | 可选必选说明：必选参数<br>参数含义：序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |
| POLICYMODE | 策略模式 | 可选必选说明：必选参数<br>参数含义：策略模式： ISAKMP：表明使用IKE建立IPsec安全联盟。<br>数据来源：对端协商<br>取值范围：<br>- “Isakmp（ISAKMP模式）”：使用IKE建立IPsec安全联盟的模式<br>默认值：无<br>配置原则：无 |
| TEMPLATEMODE | 模板模式 | 可选必选说明：必选参数<br>参数含义：模板模式-绑定一个策略模板到ISAKMP（使用策略模板建立IPsec安全联盟）。<br>数据来源：对端协商<br>取值范围：<br>- None（无）<br>- “PolicyTemplate（策略模板模式）”：使用策略模板模式创建策略，仅支持用户级IPsec。<br>默认值：无<br>配置原则：无 |
| IPSECPROPNAME | IPsec安全提议名称 | 可选必选说明：必选参数<br>参数含义：Proposal名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001180592500)

增加IPsec策略的提议：

```
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="pol2",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="asdf2";
```
