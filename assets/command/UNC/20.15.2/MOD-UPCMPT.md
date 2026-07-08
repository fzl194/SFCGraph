---
id: UNC@20.15.2@MMLCommand@MOD UPCMPT
type: MMLCommand
name: MOD UPCMPT（修改UP节点协议兼容性配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: UPCMPT
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP节点协议兼容性管理
status: active
---

# MOD UPCMPT（修改UP节点协议兼容性配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于修改UP节点协议兼容性配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD UPNODE中参数“NFINSTANCENAME”保持一致，使用该前需通过ADD UPNODE添加一组记录。 |
| APNPOLICY | APN/DNN编码格式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的APN/DNN信元编码格式。<br>数据来源：对端协商<br>取值范围：<br>- “WITHOUTOI（不携带OI信息）”：APN或者DNN不携带APN OI或者DNN OI。<br>- “WITHOI（携带OI信息）”：APN或者DNN携带的是APNNI+APNOI或者DNNNI+DNNOI。<br>默认值：无<br>配置原则：<br>如果用户面要求携带OI信息，则设置为WITHOI，否则默认为WITHOUTOI。 |
| SNSSAI | 网络切片选择辅助信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的SNSSAI信元是否为标准信元。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承）”：PFCP Session Establishment Request消息中S-NSSAI使用华为私有信元或协议标准的信元，继承SET PFCPPVTEXT命令配置中S_NSSAI功能是否开启。<br>- “OFF（关闭）”：PFCP Session Establishment Request消息中S-NSSAI使用华为私有信元。<br>- “ON（开启）”：PFCP Session Establishment Request消息中S-NSSAI使用协议标准的信元。<br>默认值：无<br>配置原则：无 |
| NODEIDFQDNFMT | Node ID信元FQDN编码格式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的FQDN类型Node ID信元的编码格式。<br>数据来源：对端协商<br>取值范围：<br>- DOT（点分格式）<br>- LV（LV格式）<br>默认值：无<br>配置原则：无 |
| POOLPLACEHOLDER | 是否携带地址池占位符 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP消息是否携带地址池占位符。UNC向UDG申请双栈地址的时候，如果只有IPv6类型的地址池，则将IPv4地址池的位置用*代替，即为占位符。<br>以免对端将IPv6类型的地址池识别成IPv4类型。<br>数据来源：对端协商<br>取值范围：<br>- INHERIT（继承全局）<br>- TRUE（是）<br>- FALSE（否）<br>默认值：无<br>配置原则：<br>该参数取值为INHERIT时，应用SET PFCPCMPT中POOLPLACEHOLDER取值。 |
| CUSTOMRATTYPE | 是否携带运营商定制的RAT Type信元 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment/Modification Request消息中是否携带运营商定制的RAT Type信元。<br>数据来源：对端协商<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>当SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment/Modification Request消息中需要携带运营商定制的RAT Type信元时，配置为ENABLE。 |
| CUSTOML2TPPCO | 是否携带运营商定制的L2TP User Info信元 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的L2TP User Info信元。<br>数据来源：对端协商<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>当SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中需要携带运营商定制的L2TP User Info信元时，配置为ENABLE。 |
| CUSTOML2TPTNL | 是否携带运营商定制的L2TP Tunnel Info信元 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的L2TP Tunnel Info信元。<br>数据来源：对端协商<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>当SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中需要携带运营商定制的L2TP Tunnel Info信元时，配置为ENABLE。 |
| CUSTOMULI | 是否携带运营商定制的User Location Information信元 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的User Location Information信元。<br>数据来源：对端协商<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>当SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中需要携带运营商定制的User Location Information信元时，配置为ENABLE。 |
| UEIPADDRSDFLAG | 是否携带UE IP Address信元的S/D标记位 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE IP Address信元是否携带S/D标记位。<br>数据来源：对端协商<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>对接UPF校验UE IP Address信元中的S/D标记位时，配置为ENABLE。 |
| NWINSTDNFMT | 网络实例Domian Name编码格式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络实例携带Domain Name时的编码格式。配置为点分格式时，部分场景下会使用点分格式。配置为LV格式时仅使用LV编码格式。<br>数据来源：对端协商<br>取值范围：<br>- DOT（点分格式）<br>- LV（LV格式）<br>默认值：无<br>配置原则：无 |
| ISOPENUPF | 是否支持OpenUPF | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端UPF是否是OpenUPF。<br>数据来源：对端协商<br>取值范围：<br>- “DISABLE（不支持OpenUPF）”：不支持OpenUPF<br>- “ENABLE（支持OpenUPF）”：支持OpenUPF<br>默认值：无<br>配置原则：无 |
| UPSTRICTPAITF | UPF Pa接口配置严格匹配 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPLOGICINTF的Pa接口(Gn/S5S8 Pgw/n9a)配置是否严格匹配。如果开关关闭，SMF上UPLOGICINTF的Pa接口(Gn/S5S8 Pgw/n9a)可以共用。如果开关开启，UPLOGICINTF配置的Pa接口(Gn/S5S8 Pgw/n9a)不可以共用。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（关闭Pa接口严格匹配）”：关闭Pa接口严格匹配<br>- “ENABLE（开启Pa接口严格匹配）”：开启Pa接口严格匹配<br>默认值：无<br>配置原则：<br>当UPF为Open UPF或需要对UPLOGICINTF的Pa接口(Gn/S5S8 Pgw/n9a)进行严格匹配时，配置为ENABLE。 |
| L2TPTNL | L2TP隧道信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给UPF的L2TP隧道信息是否是华为私有信元格式。<br>数据来源：全网规划<br>取值范围：<br>- “INHERIT（继承）”：PFCP Session Establishment Request消息中L2TP隧道信元使用华为私有信元或协议标准信元，继承SET PFCPPVTEXT配置命令中L2TP_TNL功能是否开启。<br>- “ENABLE（使能）”：PFCP Session Establishment Request消息中L2TP隧道信息使用华为私有信元。<br>- “DISABLE（不使能）”：PFCP Session Establishment Request消息中L2TP隧道信息使用协议标准信元。<br>默认值：无<br>配置原则：<br>枚举项L2TPTNL和L2TPPCO同时使能或同时不使能，如果设置其中一个枚举值，另一个枚举值同时被设置。 |
| L2TPPCO | L2TP用户PCO信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给UPF的L2TP用户PCO信息是否是华为私有信元格式。<br>数据来源：全网规划<br>取值范围：<br>- “INHERIT（继承）”：PFCP Session Establishment Request消息中L2TP用户PCO信息使用华为私有信元或协议标准信元，继承SET PFCPPVTEXT配置命令中L2TP_PCO功能是否开启。<br>- “ENABLE（使能）”：PFCP Session Establishment Request消息中L2TP用户PCO信息使用华为私有信元。<br>- “DISABLE（不使能）”：PFCP Session Establishment Request消息中L2TP用户PCO信息使用协议标准信元。<br>默认值：无<br>配置原则：<br>枚举项L2TPTNL和L2TPPCO同时使能或同时不使能，如果设置其中一个枚举值，另一个枚举值同时被设置。 |
| HTTPRDTDSTITF | HTTP重定向对端接口值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP重定向对端接口值。<br>数据来源：全网规划<br>取值范围：<br>- Core（Core）<br>- Access（Access）<br>默认值：无<br>配置原则：无 |
| CUSUEIPADDR | 定制携带UE IP地址的方式 | 可选必选说明：可选参数<br>参数含义：该参数用于通用DNN漫游分流特性中专网会话SMF是否通过运营商定制的信元格式携带大网UE IP地址信息给锚点UPF。<br>数据来源：对端协商<br>取值范围：<br>- “DISABLE（不使能）”：通过华为私有信元格式携带大网UE IP地址信息给锚点UPF。<br>- “ENABLE（使能）”：通过运营商定制的信元格式携带大网UE IP地址信息给锚点UPF。<br>默认值：无<br>配置原则：<br>如果对端专网UPF为华为设备，该参数配置为DISABLE；如果为其他厂商设备，该UPF支持处理PFCP消息中ReplacedUeIpAddress字段，参数配置为ENABLE。 |
| PMUSERIDFM | 路径迁移UserID信元编码格式 | 可选必选说明：该参数在"PMUSERIDSW"配置为"WITH"时为条件可选参数。<br>参数含义：该参数用于设置路径迁移UserID信元编码格式。<br>数据来源：全网规划<br>取值范围：<br>- CUSTOM（定制信元格式）<br>- STANDARD（标准信元格式）<br>默认值：无<br>配置原则：无 |
| PMUSERIDSW | 路径迁移是否携带UserID信元 | 可选必选说明：可选参数<br>参数含义：该参数用于设置路径迁移是否携带UserID信元。<br>数据来源：全网规划<br>取值范围：<br>- “WITH（携带）”：消息携带UserID信元<br>- “WITHOUT（不携带）”：消息不携带UserID信元<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPCMPT]] · UP节点协议兼容性配置（UPCMPT）

## 使用实例

修改UPF实例标识为upf_instance_1的UP节点协议兼容性配置，APP/DNN的编码格式为WITHOI，执行命令如下：

```
MOD UPCMPT:UPFINSTANCEID="upf_instance_1",APNPOLICY=WITHOI;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UP节点协议兼容性配置（MOD-UPCMPT）_88377448.md`
