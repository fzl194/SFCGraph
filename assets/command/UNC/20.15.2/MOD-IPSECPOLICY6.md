---
id: UNC@20.15.2@MMLCommand@MOD IPSECPOLICY6
type: MMLCommand
name: MOD IPSECPOLICY6（修改IPsec IPv6策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IPSECPOLICY6
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec策略IPv6
status: active
---

# MOD IPSECPOLICY6（修改IPsec IPv6策略）

## 功能

![](修改IPsec IPv6策略（MOD IPSECPOLICY6）_68200989.assets/notice_3.0-zh-cn_2.png)

该命令影响协商及加解密性能，命令中的部分配置可能是不安全的。

该命令用于配置IPsec Ipv6策略。

## 注意事项

- 该命令执行后立即生效。

- 该命令中的一些配置可能是不安全的。
- DH组dh_group1、dh_group2、dh_group5和dh_group14都是不安全的，建议dh_group19，但dh_group19计算较慢。
- 每个policy下最大支持128个sequence。
- IPsec policy绑定Tunnel口后，不允许进行修改。修改时需先解绑IPsec policy，但会影响现有IPsec业务。
- 一个ACL组不能同时绑定两个policy。
- 在指定ACL规则组时，数字型ACL填写于ACLNUMBER、字符型ACL填写于ACLNAME，两者不可同时配置。
- 使能数据流可信（TFC）会对性能造成很大影响。
- IKEv1国密IPSEC不支持ESN/RFC 6311/TFC。
- IKEv1国密IPSEC不支持主备隧道。
- IPV6不支持“Round_robin（轮询）”工作模式，配置“Round_robin（轮询）”实际以“Master_standby（主备）”工作模式生效。
- 当配置“SA按时计长”字段值为0时，该字段会采用[**SET IKEGLOBALCONFIG**](../IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)命令中TIMESADURTN参数的取值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 序列号 | 可选必选说明：必选参数<br>参数含义：序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |
| POLICYMODE | 策略模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定策略模式。<br>数据来源：对端协商<br>取值范围：<br>- “Isakmp（ISAKMP模式）”：使用IKE建立IPsec安全联盟的模式<br>默认值：无<br>配置原则：无 |
| TEMPLATEMODE | 模板模式 | 可选必选说明：必选参数<br>参数含义：模板模式-绑定一个策略模板到ISAKMP（使用策略模板建立IPsec安全联盟）。<br>数据来源：对端协商<br>取值范围：<br>- None（无）<br>- “PolicyTemplate（策略模板模式）”：使用策略模板模式创建策略，仅支持用户级IPsec。<br>默认值：无<br>配置原则：无 |
| ACLNUMBER | ACL编号 | 可选必选说明：该参数在"ACLTYPE"配置为"AclIPv4"时为条件可选参数。<br>参数含义：通过策略指定需要保护的报文，指定ACL的编号，只能是高级ACL。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是3000~3999，0。<br>默认值：无<br>配置原则：无 |
| ACLNAME | ACL名称 | 可选必选说明：该参数在"ACLTYPE"配置为"AclIPv4"时为条件可选参数。<br>参数含义：通过策略指定需要保护的报文，指定ACL的名字（名字是由1-32个字符组成的字符串，需要用a-z或A-Z开头）。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。名字是由1-32个字符组成的字符串，需要用a-z或A-Z开头。<br>默认值：无<br>配置原则：无 |
| TRAFFSADISFLG | 去使能SA以流量计长 | 可选必选说明：可选参数<br>参数含义：流量方式触发SA过期。<br>数据来源：本端规划<br>取值范围：<br>- FALSE（FALSE）<br>- TRUE（TRUE）<br>默认值：无<br>配置原则：<br>大流量环境该值建议设置为TRUE。 |
| SALIFETIMEKB | SA按流量计长 (mbyte) | 可选必选说明：该参数在"TRAFFSADISFLG"配置为"FALSE"时为条件可选参数。<br>参数含义：基于流量的SA生命周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是8000~200000000，单位是兆字节。<br>默认值：无<br>配置原则：无 |
| SALIFETIMESEC | SA按时计长 (s) | 可选必选说明：可选参数<br>参数含义：SA的生命周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，480~604800，单位是秒。<br>默认值：无<br>配置原则：<br>该参数默认采用<br>[**SET IKEGLOBALCONFIG**](../IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)<br>命令中TIMESADURTN参数的取值。默认为3600。 |
| PFS | PFS | 可选必选说明：可选参数<br>参数含义：在IKE协商的第二阶段使用前向安全保护（PFS）。<br>数据来源：对端协商<br>取值范围：<br>- None（无）<br>- “Dh_group1（DH组1）”：DH组1，不安全的DH组<br>- “Dh_group2（DH组2）”：DH组2，不安全的DH组<br>- “Dh_group5（DH组5）”：DH组5，不安全的DH组<br>- “Dh_group14（DH组14）”：DH组14，不安全的DH组<br>- “Dh_group19（DH组19）”：DH组19，推荐的安全DH组<br>- “Dh_group20（DH组20）”：DH组20，推荐的安全DH组<br>- “Dh_group31（DH组31）”：DH组31，推荐的安全DH组<br>默认值：无<br>配置原则：无 |
| DSCPINSELECT | 选择DSCP入方向值 | 可选必选说明：可选参数<br>参数含义：输入入方向的DSCP值。<br>数据来源：本端规划<br>取值范围：<br>- “Af11（Af11）”：DSCP编码af11<br>- “Af12（Af12）”：DSCP编码af12<br>- “Af13（Af13）”：DSCP编码af13<br>- “Af21（Af21）”：DSCP编码af21<br>- “Af22（Af22）”：DSCP编码af22<br>- “Af23（Af23）”：DSCP编码af23<br>- “Af31（Af31）”：DSCP编码af31<br>- “Af32（Af32）”：DSCP编码af32<br>- “Af33（Af33）”：DSCP编码af33<br>- “Af41（Af41）”：DSCP编码af41<br>- “Af42（Af42）”：DSCP编码af42<br>- “Af43（Af43）”：DSCP编码af43<br>- “Cs1（Cs1）”：DSCP编码cs1<br>- “Cs2（Cs2）”：DSCP编码cs2<br>- “Cs3（Cs3）”：DSCP编码cs3<br>- “Cs4（Cs4）”：DSCP编码cs4<br>- “Cs5（Cs5）”：DSCP编码cs5<br>- “Cs6（Cs6）”：DSCP编码cs6<br>- “Cs7（Cs7）”：DSCP编码cs7<br>- “Default（默认值）”：默认值<br>- “Ef（Ef）”：DSCP编码ef<br>- None（无）<br>- “EnterDSCPCode（输入DSCP编码）”：输入DSCP编码<br>默认值：无<br>配置原则：无 |
| DSCPINBOUNDVAL | 输入DSCP入方向值 | 可选必选说明：该参数在"DSCPINSELECT"配置为"EnterDSCPCode"时为条件必选参数。<br>参数含义：输入入方向的DSCP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |
| DSCPOUTSELECT | 选择DSCP出方向值 | 可选必选说明：可选参数<br>参数含义：输入出方向的DSCP值。<br>数据来源：本端规划<br>取值范围：<br>- “Af11（Af11）”：DSCP编码af11<br>- “Af12（Af12）”：DSCP编码af12<br>- “Af13（Af13）”：DSCP编码af13<br>- “Af21（Af21）”：DSCP编码af21<br>- “Af22（Af22）”：DSCP编码af22<br>- “Af23（Af23）”：DSCP编码af23<br>- “Af31（Af31）”：DSCP编码af31<br>- “Af32（Af32）”：DSCP编码af32<br>- “Af33（Af33）”：DSCP编码af33<br>- “Af41（Af41）”：DSCP编码af41<br>- “Af42（Af42）”：DSCP编码af42<br>- “Af43（Af43）”：DSCP编码af43<br>- “Cs1（Cs1）”：DSCP编码cs1<br>- “Cs2（Cs2）”：DSCP编码cs2<br>- “Cs3（Cs3）”：DSCP编码cs3<br>- “Cs4（Cs4）”：DSCP编码cs4<br>- “Cs5（Cs5）”：DSCP编码cs5<br>- “Cs6（Cs6）”：DSCP编码cs6<br>- “Cs7（Cs7）”：DSCP编码cs7<br>- “Default（默认值）”：默认值<br>- “Ef（Ef）”：DSCP编码ef<br>- None（无）<br>- “EnterDSCPCode（输入DSCP编码）”：输入DSCP编码<br>默认值：无<br>配置原则：无 |
| DSCPOUTBOUNDVAL | 输入DSCP出方向值 | 可选必选说明：该参数在"DSCPOUTSELECT"配置为"EnterDSCPCode"时为条件必选参数。<br>参数含义：输入出方向的DSCP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |
| ANTIREPLAYENUM | 抗重放 | 可选必选说明：可选参数<br>参数含义：抗重放。<br>数据来源：本端规划<br>取值范围：<br>- “NotConfigured（未配置）”：未配置<br>- “Enable（使能）”：使能<br>- “Disable（未使能）”：未使能<br>默认值：无<br>配置原则：无 |
| WINDOWSIZE | 抗重放窗口大小 | 可选必选说明：该参数在"ANTIREPLAYENUM"配置为"Enable"时为条件可选参数。<br>参数含义：抗重放窗口的大小，超过这个流量的报文会被丢弃。<br>数据来源：本端规划<br>取值范围：<br>- None（无）<br>- “Size_32（32）”：窗口大小32<br>- “Size_64（64）”：窗口大小64<br>- “Size_128（128）”：窗口大小128<br>- “Size_256（256）”：窗口大小256<br>- “Size_512（512）”：窗口大小512<br>- “Size_1024（1024）”：窗口大小1024<br>默认值：无<br>配置原则：无 |
| DFBITCLEAR | 清除分片标记 | 可选必选说明：可选参数<br>参数含义：清除分片标记。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| FRAGBEFOREENCR | 加密前分片报文 | 可选必选说明：可选参数<br>参数含义：加密前分片报文。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| INSPEEDLIMIT | 入方向限速 (kbyte/s) | 可选必选说明：可选参数<br>参数含义：入方向流量限速。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是8~4194303，0。单位是千字节每秒，取0表示不限速。<br>默认值：无<br>配置原则：无 |
| OUTSPEEDLIMIT | 出方向限速 (kbyte/s) | 可选必选说明：可选参数<br>参数含义：出方向流量限速。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是8~4194303，0。单位是千字节每秒，取0表示不限速。<br>默认值：无<br>配置原则：无 |
| LOGENABLE | 日志使能 | 可选必选说明：可选参数<br>参数含义：日志使能。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| WORKMODE | 工作模式 | 可选必选说明：可选参数<br>参数含义：工作模式，如轮循模式、主备模式。<br>数据来源：本端规划<br>取值范围：<br>- “Round_robin（轮询）”：轮询工作模式<br>- “Master_standby（主备）”：主备隧道工作模式<br>默认值：无<br>配置原则：<br>配置为轮循模式或者主备模式时，SA协商方式为自动协商。推荐使用主备工作模式。 |
| AUTOSWITCHBACK | 自动切回开关 | 可选必选说明：该参数在"WORKMODE"配置为"Master_standby"时为条件必选参数。<br>参数含义：若开启自动切回开关，主恢复后，流量重新切回主隧道；不开启自动切回开关，主恢复后，流量仍在备隧道。<br>数据来源：本端规划<br>取值范围：<br>- “Disable（未使能）”：未使能<br>- “Enable（使能）”：使能<br>默认值：无<br>配置原则：无 |
| ACL6NUMBER | ACL编号-IPv6 | 可选必选说明：该参数在"ACLTYPE"配置为"AclIPv6"时为条件可选参数。<br>参数含义：通过策略指定需要保护的报文，指定ACL的编号，只能是高级ACL。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，3000~3999。<br>默认值：无<br>配置原则：无 |
| ACL6NAME | ACL名称-IPv6 | 可选必选说明：该参数在"ACLTYPE"配置为"AclIPv6"时为条件可选参数。<br>参数含义：通过策略指定需要保护的报文，指定ACL的名字（名字是由1-32个字符组成的字符串，需要用a-z或A-Z开头）。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。名字是由0-32个字符组成的字符串，需要用a-z或A-Z开头。<br>默认值：无<br>配置原则：无 |
| ACLTYPE | ACL类型 | 可选必选说明：必选参数<br>参数含义：ACL类型。<br>数据来源：本端规划<br>取值范围：<br>- “AclIPv4（IPv4）”：IPv4<br>- “AclIPv6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| ESN | 扩展序列号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示扩展序列号是否使能。<br>数据来源：本端规划<br>取值范围：<br>- “Disable（未使能）”：未使能<br>- “Enable（使能）”：使能<br>默认值：无<br>配置原则：<br>该参数必须在“ANTIREPLAYENUM”配置为“Enable”时才可配置为"Enable"。只有该参数配置为“Disable”时，“ANTIREPLAYENUM”才可配置为“Disable”或“NotConfigured”。该参数配置为“Enable”时，“WINDOWSIZE”不可配置为空或“None”。 |
| TFCENABLE | 数据流可信使能 | 可选必选说明：可选参数<br>参数含义：数据流可信使能。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECPOLICY6]] · IPsec IPv6策略（IPSECPOLICY6）

## 使用实例

修改IPsec策略：

```
MOD IPSECPOLICY6:POLICYNAME="pol2",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLTYPE=AclIPv6;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IPsec-IPv6策略（MOD-IPSECPOLICY6）_68200989.md`
