# 删除IPsec策略（RMV IPSECPOLICY）

- [命令功能](#ZH-CN_MMLREF_0000001226032203__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001226032203__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001226032203__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001226032203__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001226032203)

![](删除IPsec策略（RMV IPSECPOLICY）_26032203.assets/notice_3.0-zh-cn_2.png)

删除IPsec策略，影响业务流量使用IPSEC进行加解密功能，有业务影响。

该命令用于删除IPsec策略。

## [注意事项](#ZH-CN_MMLREF_0000001226032203)

- 该命令执行后立即生效。

- 当IPsec策略被IPsec隧道引用时，IPsec策略不能被删除。如果需要删除IPsec策略，必须先删除IPsec策略的引用。

#### [操作用户权限](#ZH-CN_MMLREF_0000001226032203)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001226032203)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 序列号 | 可选必选说明：必选参数<br>参数含义：序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |
| POLICYMODE | 策略模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定策略模式。<br>数据来源：对端协商<br>取值范围：<br>- “Isakmp（ISAKMP模式）”：使用IKE建立IPsec安全联盟的模式<br>默认值：无<br>配置原则：无 |
| TEMPLATEMODE | 模板模式 | 可选必选说明：必选参数<br>参数含义：模板模式-绑定一个策略模板到ISAKMP（使用策略模板建立IPsec安全联盟）。<br>数据来源：对端协商<br>取值范围：<br>- None（无）<br>- “PolicyTemplate（策略模板模式）”：使用策略模板模式创建策略，仅支持用户级IPsec。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001226032203)

删除策略名称为“pol2”，序列号为1，策略模式为“Isakmp”，模板模式为“None”的IPsec策略：

```
RMV IPSECPOLICY:POLICYNAME="pol2",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None;
```
