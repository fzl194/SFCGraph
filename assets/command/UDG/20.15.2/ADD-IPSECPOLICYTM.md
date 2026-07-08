---
id: UDG@20.15.2@MMLCommand@ADD IPSECPOLICYTM
type: MMLCommand
name: ADD IPSECPOLICYTM（增加IPsec策略模板）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IPSECPOLICYTM
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec策略模板
status: active
---

# ADD IPSECPOLICYTM（增加IPsec策略模板）

## 功能

![](增加IPsec策略模板（ADD IPSECPOLICYTM）_96044554.assets/notice_3.0-zh-cn.png)

增加配置，影响协商及加解密性能。

该命令用于增加IPsec策略模板。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令的策略模板只支持使用FQDN鉴权方式，否则可能导致IKE协商失败。
> - 当配置“SA按时计长”字段值为0时，该字段会采用[**SET IKEGLOBALCONFIG**](../IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)命令中TIMESADURTN参数的取值。
>
> - 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略模板名称 | 可选必选说明：必选参数<br>参数含义：策略模板名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 策略模板序列号 | 可选必选说明：必选参数<br>参数含义：策略模板序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |
| PEERNAME | IKE对等体名称 | 可选必选说明：必选参数<br>参数含义：IKE对等体名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~15。<br>默认值：无<br>配置原则：<br>该参数可通过<br>[**LST IKEPEER**](../IKE对等体/查询IKE对等体（LST IKEPEER）_80432528.md)<br>查询对等体名称。 |
| IPSECPROPNAME | IPsec安全提议名称 | 可选必选说明：必选参数<br>参数含义：IPsec Proposal名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数可通过<br>[**LST IPSECPROPOSALIPSEC**](../../IPsec/IPsec提议/查询IPsec提议（LST IPSECPROPOSALIPSEC）_80910992.md)<br>查询Proposal名称。 |
| ACLNAME | ACL名称 | 可选必选说明：可选参数<br>参数含义：通过策略指定需要保护的报文，指定ACL的名字（名字是由1-32个字符组成的字符串，需要用a-z或A-Z开头）。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。名字是由1-32个字符组成的字符串，需要用a-z或A-Z开头。<br>默认值：无<br>配置原则：<br>该参数可通过<br>[**LST ACLGROUPIPSEC**](../../../ACL管理/ACL规则组/查询ACL规则组配置（LST ACLGROUPIPSEC）_25830691.md)<br>查询ACL规则组标识。 |
| ACLNUMBER | ACL编号 | 可选必选说明：可选参数<br>参数含义：通过策略指定需要保护的报文，指定ACL的编号，只能是高级ACL。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，3000~3999。<br>默认值：无<br>配置原则：<br>该参数可通过<br>[**LST ACLGROUPIPSEC**](../../../ACL管理/ACL规则组/查询ACL规则组配置（LST ACLGROUPIPSEC）_25830691.md)<br>查询ACL规则组标识。 |
| TRAFFSADISFLG | 去使能SA按流量计长 | 可选必选说明：可选参数<br>参数含义：流量方式触发SA过期。<br>数据来源：本端规划<br>取值范围：<br>- FALSE（FALSE）<br>- TRUE（TRUE）<br>默认值：无<br>配置原则：无 |
| SALIFETIMEKB | SA按流量计长 (mbyte) | 可选必选说明：该参数在"TRAFFSADISFLG"配置为"FALSE"时为条件可选参数。<br>参数含义：基于流量的SA生命周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是8000~200000000，单位是兆字节。<br>默认值：无<br>配置原则：无 |
| SALIFETIMESEC | SA按时计长 (s) | 可选必选说明：可选参数<br>参数含义：SA的生命周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，480~604800。<br>默认值：无<br>配置原则：无 |
| PFS | PFS | 可选必选说明：可选参数<br>参数含义：在IKE协商的第二阶段使用前向安全保护（PFS）。<br>数据来源：对端协商<br>取值范围：<br>- None（无）<br>- “Dh_group1（DH组1）”：DH组1，不安全的DH组<br>- “Dh_group2（DH组2）”：DH组2，不安全的DH组<br>- “Dh_group5（DH组5）”：DH组5，不安全的DH组<br>- “Dh_group14（DH组14）”：DH组14，不安全的DH组<br>- “Dh_group19（DH组19）”：DH组19，推荐的安全DH组<br>- “Dh_group20（DH组20）”：DH组20，推荐的安全DH组<br>- “Dh_group31（DH组31）”：DH组31，推荐的安全DH组<br>默认值：无<br>配置原则：无 |
| DSCPINSELECT | 选择DSCP入方向值 | 可选必选说明：可选参数<br>参数含义：输入入方向的DSCP值。<br>数据来源：本端规划<br>取值范围：<br>- “Af11（Af11）”：DSCP编码af11<br>- “Af12（Af12）”：DSCP编码af12<br>- “Af13（Af13）”：DSCP编码af13<br>- “Af21（Af21）”：DSCP编码af21<br>- “Af22（Af22）”：DSCP编码af22<br>- “Af23（Af23）”：DSCP编码af23<br>- “Af31（Af31）”：DSCP编码af31<br>- “Af32（Af32）”：DSCP编码af32<br>- “Af33（Af33）”：DSCP编码af33<br>- “Af41（Af41）”：DSCP编码af41<br>- “Af42（Af42）”：DSCP编码af42<br>- “Af43（Af43）”：DSCP编码af43<br>- “Cs1（Cs1）”：DSCP编码cs1<br>- “Cs2（Cs2）”：DSCP编码cs2<br>- “Cs3（Cs3）”：DSCP编码cs3<br>- “Cs4（Cs4）”：DSCP编码cs4<br>- “Cs5（Cs5）”：DSCP编码cs5<br>- “Cs6（Cs6）”：DSCP编码cs6<br>- “Cs7（Cs7）”：DSCP编码cs7<br>- “Default（默认值）”：默认值<br>- “Ef（Ef）”：DSCP编码ef<br>- None（无）<br>- “EnterDSCPCode（输入DSCP编码）”：输入DSCP编码<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| DSCPINBOUNDVAL | 输入DSCP入方向值 | 可选必选说明：该参数在"DSCPINSELECT"配置为"EnterDSCPCode"时为条件必选参数。<br>参数含义：输入入方向的DSCP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| DSCPOUTSELECT | 选择DSCP出方向值 | 可选必选说明：可选参数<br>参数含义：输入出方向的DSCP值。<br>数据来源：本端规划<br>取值范围：<br>- “Af11（Af11）”：DSCP编码af11<br>- “Af12（Af12）”：DSCP编码af12<br>- “Af13（Af13）”：DSCP编码af13<br>- “Af21（Af21）”：DSCP编码af21<br>- “Af22（Af22）”：DSCP编码af22<br>- “Af23（Af23）”：DSCP编码af23<br>- “Af31（Af31）”：DSCP编码af31<br>- “Af32（Af32）”：DSCP编码af32<br>- “Af33（Af33）”：DSCP编码af33<br>- “Af41（Af41）”：DSCP编码af41<br>- “Af42（Af42）”：DSCP编码af42<br>- “Af43（Af43）”：DSCP编码af43<br>- “Cs1（Cs1）”：DSCP编码cs1<br>- “Cs2（Cs2）”：DSCP编码cs2<br>- “Cs3（Cs3）”：DSCP编码cs3<br>- “Cs4（Cs4）”：DSCP编码cs4<br>- “Cs5（Cs5）”：DSCP编码cs5<br>- “Cs6（Cs6）”：DSCP编码cs6<br>- “Cs7（Cs7）”：DSCP编码cs7<br>- “Default（默认值）”：默认值<br>- “Ef（Ef）”：DSCP编码ef<br>- None（无）<br>- “EnterDSCPCode（输入DSCP编码）”：输入DSCP编码<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| DSCPOUTBOUNDVAL | 输入DSCP出方向值 | 可选必选说明：该参数在"DSCPOUTSELECT"配置为"EnterDSCPCode"时为条件必选参数。<br>参数含义：输入出方向的DSCP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| ANTIREPLAYENUM | 抗重放 | 可选必选说明：可选参数<br>参数含义：抗重放。<br>数据来源：本端规划<br>取值范围：<br>- “NotConfigured（未配置）”：未配置<br>- “Enable（使能）”：使能<br>- “Disable（未使能）”：未使能<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| WINDOWSIZE | 抗重放窗口大小 | 可选必选说明：该参数在"ANTIREPLAYENUM"配置为"Enable"时为条件可选参数。<br>参数含义：抗重放窗口的大小，超过这个流量的报文会被丢弃。<br>数据来源：本端规划<br>取值范围：<br>- None（无）<br>- “Size_32（32）”：窗口大小32<br>- “Size_64（64）”：窗口大小64<br>- “Size_128（128）”：窗口大小128<br>- “Size_256（256）”：窗口大小256<br>- “Size_512（512）”：窗口大小512<br>- “Size_1024（1024）”：窗口大小1024<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| DFBITCLEAR | 清除分片标记 | 可选必选说明：可选参数<br>参数含义：清除分片标记。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| FRAGBEFOREENCR | 加密前分片报文 | 可选必选说明：可选参数<br>参数含义：加密前分片报文。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| INSPEEDLIMIT | 入方向限速 (kbyte/s) | 可选必选说明：可选参数<br>参数含义：入方向流量限速。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，8~4194303。单位是千字节每秒，取0表示不限速。<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| OUTSPEEDLIMIT | 出方向限速 (kbyte/s) | 可选必选说明：可选参数<br>参数含义：出方向流量限速。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，8~4194303。单位是千字节每秒，取0表示不限速。<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| ACLTYPE | ACL类型 | 可选必选说明：可选参数<br>参数含义：ACL类型。<br>数据来源：本端规划<br>取值范围：当前用户级IPsec仅支持IPv4场景。<br>- “AclIPv4（IPv4）”：IPv4<br>- “AclIPv6（IPv6）”：IPv6<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |
| ESN | 扩展序列号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示扩展序列号是否使能。<br>数据来源：本端规划<br>取值范围：<br>- “Disable（未使能）”：未使能<br>- “Enable（使能）”：使能<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。<br>该参数必须在“ANTIREPLAYENUM”配置为“Enable”时才可配置为"Enable"。只有该参数配置为“Disable”时，“ANTIREPLAYENUM”才可配置为“Disable”或“NotConfigured”。该参数配置为“Enable”时，“WINDOWSIZE”不可配置为空或“None”。 |
| TFCENABLE | 数据流可信使能 | 可选必选说明：可选参数<br>参数含义：数据流可信使能。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>当前用户级IPsec提供该功能，受组网限制不会在加解密流程中生效。 |

## 操作的配置对象

- [IPsec策略模板（IPSECPOLICYTM）](configobject/UDG/20.15.2/IPSECPOLICYTM.md)

## 使用实例

增加策略模板名称为“temp3”，序列号为1，IKE对等体名称为“peer1”，Proposal名称为“prop1”，ACL编号为3001：

```
ADD IPSECPOLICYTM:POLICYNAME="temp3",SEQUENCENUMBER=1,PEERNAME="peer1",IPSECPROPNAME="prop1",ACLNUMBER=3001;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加IPsec策略模板（ADD-IPSECPOLICYTM）_96044554.md`
