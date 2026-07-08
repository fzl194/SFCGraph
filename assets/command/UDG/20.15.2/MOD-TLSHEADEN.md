---
id: UDG@20.15.2@MMLCommand@MOD TLSHEADEN
type: MMLCommand
name: MOD TLSHEADEN（修改HTTPS头增强）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: TLSHEADEN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- HTTPS头增强
status: active
---

# MOD TLSHEADEN（修改HTTPS头增强）

## 功能

**适用NF：PGW-U、UPF**

该命令用来修改一个HTTPS头增强的相关配置。用于用户灵活更新HTTPS头增强配置，以便灵活开展业务。

## 注意事项

- 该命令执行后立即生效。
- 已经被绑定到RULE命令中的HTTPS头增强不能修改，若需要重新配置该HTTPS头增强的信息需要先执行“RMV RULE”或“MOD RULE”命令解除绑定关系后，再做修改。
- 该命令误配后会影响系统性能。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。
- 该命令设定后的数据，需要通过LST TLSHEADEN命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HEADERENNAME | 头增强名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置头增强名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置头增强的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSISDN1：指定插入项的类型为MSISDN。<br>- MSISDN2：指定插入项的类型为MSISDN。<br>- MSISDN3：指定插入项的类型为MSISDN。<br>- IMSI1：指定插入项的类型为IMSI。<br>- IMSI2：指定插入项的类型为IMSI。<br>- IMSI3：指定插入项的类型为IMSI。<br>- IMEI1：指定插入项的类型为IMEI。<br>- IMEI2：指定插入项的类型为IMEI。<br>- IMEI3：指定插入项的类型为IMEI。<br>- SGSNIP1：指定插入项的类型为SGSN IP。<br>- SGSNIP2：指定插入项的类型为SGSN IP。<br>- SGSNIP3：指定插入项的类型为SGSN IP。<br>- SUBPROFILE1：指定插入项的类型为Subscriber Profile。<br>- SUBPROFILE2：指定插入项的类型为Subscriber Profile。<br>- SUBPROFILE3：指定插入项的类型为Subscriber Profile。<br>- MSIP1：指定插入项的类型为MS IP。<br>- APN：指定插入项的类型为APN。<br>- ZONEID：指定插入项的类型为Zone ID。<br>- BILLINGTYPE：指定插入项的类型为Billing Type。<br>- CHGCHAR1：指定插入项的类型为Charge Characteristic。<br>- CHGCHAR2：指定插入项的类型为Charge Characteristic。<br>- CHGCHAR3：指定插入项的类型为Charge Characteristic。<br>- RAT1：指定插入项的类型为RAT。<br>- RAT2：指定插入项的类型为RAT。<br>- RAT3：指定插入项的类型为RAT。<br>- ULI1：指定插入项的类型为ULI。<br>- ULI2：指定插入项的类型为ULI。<br>- ULI3：指定插入项的类型为ULI。<br>- CHGID：指定插入项的类型为Charging ID。<br>- ROAMING1：指定插入项的类型为Roaming。<br>- ROAMING2：指定插入项的类型为Roaming。<br>- ROAMING3：指定插入项的类型为Roaming。<br>- SGSN_MCC_MNC1：指定插入项的类型为SGSN MCC MNC。<br>- SGSN_MCC_MNC2：指定插入项的类型为SGSN MCC MNC。<br>- SGSN_MCC_MNC3：指定插入项的类型为SGSN MCC MNC。<br>- USERDEF1：指定插入项的类型为User Defined。<br>- USERDEF2：指定插入项的类型为User Defined。<br>- USERDEF3：指定插入项的类型为User Defined。<br>- USERDEF4：指定插入项的类型为User Defined。<br>- USERPROFALIAS：指定插入项的类型为用户模板别名。<br>- MCC：指定插入项的类型为移动国家码。<br>- MNC：指定插入项的类型为移动网络码。<br>- SESSIONID：指定插入项的类型为用户标识。<br>- GGSNIP1：指定插入项的类型为GGSN IP。<br>- GGSNIP2：指定插入项的类型为GGSN IP。<br>- GGSNIP3：指定插入项的类型为GGSN IP。<br>- TIMESTAMP1：指定插入项的类型为TIMESTAMP。<br>- TIMESTAMP2：指定插入项的类型为TIMESTAMP。<br>- TIMESTAMP3：指定插入项的类型为TIMESTAMP。<br>- MSIP2：指定插入项的类型为MS IP。<br>- MSIP3：指定插入项的类型为MS IP。<br>- UPIPV4：指定插入项的类型为用户面网关逻辑接口的IPv4地址。该逻辑接口地址包含Pa、Sa、N3、S1-U地址之一，按优先级Pa>Sa>N3>S1-U的顺序获取。<br>- UPIPV6：指定插入项的类型为用户面网关逻辑接口的IPv6地址。该逻辑接口地址包含Pa、Sa、N3、S1-U地址之一，按优先级Pa>Sa>N3>S1-U的顺序获取。<br>- RANDNUM：指定插入项的类型为RANDNUM，该随机数作为加密算法MD5/SHA256盐值使用。<br>默认值：无<br>配置原则：<br>- MSISDN（1–3）：指定MSISDN插入项的前缀字段类型，协议头部需要插入用户的MSISDN信息时应配置该参数。<br>- IMSI（1–3）：指定IMSI插入项的前缀字段类型，协议头部需要插入用户的IMSI信息时应配置该参数。<br>- IMEI（1–3）：指定IMEI插入项的前缀字段类型，协议头部需要插入用户的IMEI信息时应配置该参数。<br>- SGSNIP（1–3）：指定SGSNIP插入项的前缀字段类型，协议头部需要插入用户所属的SGSN信令面IP地址/SGW的S5_sif接口地址信息时应配置该参数。GGSN形态下，该插入项的字段值数据源为SGSN信令面IP地址。PGW形态下，该插入项的字段值数据源为SGW的S5_sif接口地址。<br>- SUBPROFILE（1–3）：指定SUBPROFILE插入项的前缀字段类型，协议头部需要插入用户的SUBPROFILE信息时应配置该参数。<br>- MSIP：指定MSIP插入项的前缀字段类型，协议头部需要插入用户的手机端IP地址信息时应配置该参数。<br>- APN：指定APN插入项的前缀字段类型，协议头部需要插入用户所属的APN信息时应配置该参数。<br>- ZONEID：指定ZONEID插入项的前缀字段类型，用户为HomeZone签约用户且协议头部需要插入用户的当前HomeZone信息时应配置该参数。UDG不支持zoneid字段的头增强插入。<br>- BILLINGTYPE：指定BILLINGTYPE插入项的前缀字段类型，协议头部需要插入用户的计费属性信息时应配置该参数，该插入项的字段值数据源为AAA服务器的鉴权响应消息。<br>- CHGCHAR（1–3）：指定CHGCHAR插入项的前缀字段类型，协议头部需要插入用户的CHGCHAR信息时应配置该参数。<br>- RAT（1–3）：指定RAT插入项的前缀字段类型，协议头部需要插入用户的RAT信息时应配置该参数。<br>- ULI（1–3）：指定ULI插入项的前缀字段类型，协议头部需要插入用户的ULI信息时应配置该参数。<br>- ROAMING（1–3）：指定ROAMING属性插入项的前缀字段类型，协议头部需要插入用户的ROAMING属性信息时应配置该参数。<br>- SGSN-MCC-MNC（1–3）：指定SGSN-MCC-MNC插入项的前缀字段类型，协议头部需要插入用户的SGSN-MCC-MNC信息时应配置该参数。<br>- USERDEF（1–4）：指定USERDEF插入项的前缀字段类型和字段值，协议头部需要插入运营商对用户的自定义信息数据时应配置该参数。<br>- USERPROFALIAS：指定USERPROFALIAS插入项的前缀字段类型，协议头部需要插入用户的USERPROFALIAS信息时应配置该参数，该插入项的字段值数据源为USERPROFILE的ALIAS。<br>- MCC：指定MCC插入项的前缀字段类型，协议头部需要插入用户的MCC信息时应配置该参数。<br>- MNC：指定MNC插入项的前缀字段类型，协议头部需要插入用户的MNC信息时应配置该参数。<br>- SESSIONID：指定SESSIONID插入项的前缀字段类型，协议头部需要插入用户的SESSIONID信息时应配置该参数。<br>- TIMESTAMP（1–3）：指定TIMESTAMP插入项的前缀字段类型，协议头部需要插入用户的TIMESTAMP信息时应配置该参数。<br>- UPIPV4: 指定UPIPV4插入项的前缀字段名称，协议头部需要插入用户面网关逻辑接口IPv4地址信息时应配置该参数。<br>- UPIPV6: 指定UPIPV6插入项的前缀字段名称，协议头部需要插入用户面网关逻辑接口IPv6地址信息时应配置该参数。 |
| TLSTYPEVAL | TLS报文头域的TLS Type值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DATATYPE”配置为“APN”、“BILLINGTYPE”、“CHGCHAR1”、“CHGCHAR2”、“CHGCHAR3”、“CHGID”、“GGSNIP1”、“GGSNIP3”、“IMEI1”、“IMEI2”、“IMEI3”、“IMSI1”、“IMSI2”、“IMSI3”、“MCC”、“MNC”、“MSIP1”、“MSISDN1”、“MSISDN2”、“MSISDN3”、“RAT1”、“RAT2”、“RAT3”、“ROAMING1”、“ROAMING2”、“ROAMING3”、“SESSIONID”、“SGSNIP1”、“SGSNIP2”、“SGSNIP3”、“SGSN_MCC_MNC1”、“SGSN_MCC_MNC2”、“SGSN_MCC_MNC3”、“SUBPROFILE1”、“SUBPROFILE2”、“SUBPROFILE3”、“ULI1”、“ULI2”、“ULI3”、“USERDEF1”、“USERDEF2”、“USERDEF3”、“USERDEF4”、“USERPROFALIAS”、“ZONEID”、“GGSNIP2”、“TIMESTAMP1”、“TIMESTAMP2”、“TIMESTAMP3”、“MSIP2”、“MSIP3”、“UPIPV4”、“UPIPV6” 或 “RANDNUM”时为必选参数。<br>参数含义：TLS报文头域的TLS Type值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65534。<br>默认值：无<br>配置原则：无 |
| SUBTLSTYPEVAL | TLS报文头域的Sub TLS Type值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“APN”、“BILLINGTYPE”、“CHGCHAR1”、“CHGCHAR2”、“CHGCHAR3”、“CHGID”、“GGSNIP1”、“GGSNIP3”、“IMEI1”、“IMEI2”、“IMEI3”、“IMSI1”、“IMSI2”、“IMSI3”、“MCC”、“MNC”、“MSIP1”、“MSISDN1”、“MSISDN2”、“MSISDN3”、“RAT1”、“RAT2”、“RAT3”、“ROAMING1”、“ROAMING2”、“ROAMING3”、“SESSIONID”、“SGSNIP1”、“SGSNIP2”、“SGSNIP3”、“SGSN_MCC_MNC1”、“SGSN_MCC_MNC2”、“SGSN_MCC_MNC3”、“SUBPROFILE1”、“SUBPROFILE2”、“SUBPROFILE3”、“ULI1”、“ULI2”、“ULI3”、“USERDEF1”、“USERDEF2”、“USERDEF3”、“USERDEF4”、“USERPROFALIAS”、“ZONEID”、“GGSNIP2”、“TIMESTAMP1”、“TIMESTAMP2”、“TIMESTAMP3”、“MSIP2”、“MSIP3”、“UPIPV4”、“UPIPV6” 或 “RANDNUM”时为可选参数。<br>参数含义：TLS报文头域的Sub TLS Type值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～254。<br>默认值：无<br>配置原则：无 |
| USERDEFINEVAL | 用户自定义值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DATATYPE”配置为“USERDEF1”、“USERDEF2”、“USERDEF3” 或 “USERDEF4”时为必选参数。<br>参数含义：该参数用于指定USEDFEFINE插入项的字段值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。支持空格。<br>默认值：无<br>配置原则：协议头部需要插入运营商对用户的自定义信息数据时应配置该参数。可以按需指定该插入项的字段值。 |
| IMEITYPE | IMEI类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“IMEI1”、“IMEI2” 或 “IMEI3”时为可选参数。<br>参数含义：该参数用于设置在插入用户IMEI信息时，是只插入TAC还是插入完整的用户IMEI信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMEI：插入完整的用户IMEI信息。<br>- TAC：插入TAC信息。<br>默认值：无<br>配置原则：<br>- 配置了IMEI参数且需要指定用户IMEI信息的具体取值时应配置该参数。<br>- 取值为IMEI或TAC。当取值为IMEI时，完整的用户IMEI信息会插入到协议报文头中。当取值为TAC时，只有TAC信息会插入到协议报文头中。 |
| ERRFLGTLSTP | HomeZone功能TLS报文头域的TLS Type值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“ZONEID”时为可选参数。<br>参数含义：HomeZone功能TLS报文头域的TLS Type值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65534。<br>默认值：无<br>配置原则：UDG不支持zoneid字段的头增强插入，无需配置该参数。 |
| ERRFGSUBTLSTP | HomeZone功能TLS报文头域的Sub Type值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“ZONEID”时为可选参数。<br>参数含义：HomeZone功能TLS报文头域的Sub TLS Type值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～254。<br>默认值：无<br>配置原则：UDG不支持zoneid字段的头增强插入，无需配置该参数。 |
| ENCRYALGORI | 加密算法标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“MSISDN1”、“MSISDN2”、“MSISDN3”、“IMSI1”、“IMSI2”、“IMSI3”、“IMEI1”、“IMEI2”、“IMEI3”、“SGSNIP1”、“SGSNIP2”、“SGSNIP3”、“SUBPROFILE1”、“SUBPROFILE2”、“SUBPROFILE3”、“CHGCHAR1”、“CHGCHAR2”、“CHGCHAR3”、“RAT1”、“RAT2”、“RAT3”、“ULI1”、“ULI2”、“ULI3”、“ROAMING1”、“ROAMING2”、“ROAMING3”、“SGSN_MCC_MNC1”、“SGSN_MCC_MNC2”、“SGSN_MCC_MNC3”、“GGSNIP1”、“GGSNIP2”、“GGSNIP3”、“TIMESTAMP1”、“TIMESTAMP2”、“APN”、“MSIP1”、“TIMESTAMP3”、“MSIP2”、“MSIP3”、“UPIPV4” 或 “UPIPV6”时为可选参数。<br>参数含义：该参数用于指定对携带的参数的加密方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NONE：表示不进行加密，有安全风险，不建议使用。<br>- MD5：表示加密类型为MD5，有安全风险，不建议使用。<br>- RC4：表示加密类型为RC4，RC4有安全风险，不建议使用。<br>- AES128：表示加密类型为AES128 CBC模式，AES128 CBC模式有安全风险，不建议使用。<br>- SHA256：表示加密类型为SHA256。<br>- AES256：表示加密类型为AES256 CBC模式，AES256 CBC模式有安全风险，不建议使用。<br>- AES128_GCM：表示加密类型为AES128 GCM模式。<br>- AES128_CTR：表示加密类型为AES128 CTR模式。<br>- AES256_GCM：表示加密类型为AES256 GCM模式。<br>- AES256_CTR：表示加密类型为AES256 CTR模式。<br>默认值：无<br>配置原则：请根据需求选择相应加密算法，建议使用AES128_GCM加密算法，当配置MD5、RC4、AES128、AES256或NONE时有安全风险，不建议使用。 |
| PSWDKEY | 密钥 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENCRYALGORI”配置为“MD5”、“RC4”、“AES128”、“AES256”、“SHA256”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于设置用于参数加密算法的密钥。<br>数据来源：本端规划<br>取值范围：1、如果是MD5 hash算法，密钥长度为1~16；如果是RC4加密算法字符串长度范围是1～255；如果是AES128、AES128_GCM或AES128_CTR算法，密钥长度为1~16；如果是AES256、AES256_GCM或AES256_CTR算法，密钥长度为1~32；如果是SHA256算法，密钥长度为1~255。不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用SET SRVCOMMONPARA命令配置生成。<br>- 建议密钥应不少于8个字符，同时应包含如下至少两种字符的组合：至少包括一个大写字母（A~Z）；至少包括一个小写字母（a~z）；至少包括一个数字字符（0—9）；至少包括1个特殊字符，如：“~、@、^、*、-、_、[、{}、]、:、.、/、？”。 |
| PSWDKEYCONFIRM | 确认密钥 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENCRYALGORI”配置为“AES128”、“MD5”、“RC4”、“AES256”、“SHA256”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于确认加密算法的密钥。<br>数据来源：本端规划<br>取值范围：1、如果是MD5 hash算法，密钥长度为1~16；如果是RC4加密算法字符串长度范围是1～255；如果是AES128、AES128_GCM或AES128_CTR算法，密钥长度为1~16；如果是AES256、AES256_GCM或AES256_CTR算法，密钥长度为1~32；如果是SHA256算法，密钥长度为1~255。不支持空格。<br>默认值：无<br>配置原则：建议密钥应不少于8个字符，同时应包含如下至少两种字符的组合：至少包括一个大写字母（A~Z）；至少包括一个小写字母（a~z）；至少包括一个数字字符（0—9）；至少包括1个特殊字符，如：“~、@、^、*、-、_、[、{}、]、:、.、/、？”。 |
| ANTIFRAUD | 防欺诈标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“MSISDN1”、“MSISDN2”、“MSISDN3”、“IMSI1”、“IMSI2”、“IMSI3”、“IMEI1”、“IMEI2”、“IMEI3”、“SGSNIP1”、“SGSNIP2”、“SGSNIP3”、“SUBPROFILE1”、“SUBPROFILE2”、“SUBPROFILE3”、“CHGCHAR1”、“CHGCHAR2”、“CHGCHAR3”、“MSIP1”、“APN”、“ZONEID”、“BILLINGTYPE”、“RAT1”、“RAT2”、“RAT3”、“ULI1”、“ULI2”、“ULI3”、“CHGID”、“ROAMING1”、“ROAMING2”、“ROAMING3”、“SGSN_MCC_MNC1”、“SGSN_MCC_MNC2”、“SGSN_MCC_MNC3”、“USERDEF1”、“USERDEF2”、“USERDEF3”、“USERDEF4”、“USERPROFALIAS”、“MCC”、“MNC”、“SESSIONID”、“GGSNIP1”、“GGSNIP2”、“GGSNIP3”、“TIMESTAMP1”、“TIMESTAMP2”、“TIMESTAMP3”、“MSIP2”、“MSIP3”、“UPIPV4”、“UPIPV6” 或 “RANDNUM”时为可选参数。<br>参数含义：该参数用于设置头增强的防欺诈标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：通过需求选择是否对当前头增强使能防欺诈。 |
| HEADERFLDLEN | 头域长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“USERPROFALIAS”时为可选参数。<br>参数含义：该参数用于指定插入项的总长度，包括前缀名称、冒号、空格、加号和结束符\r\n。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为31～255。<br>默认值：无<br>配置原则：如果需要修改插入头域的长度限制，则修改该参数。 |
| REMOVEDMCC | 需去除的移动国家码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“MSISDN1”、“MSISDN2” 或 “MSISDN3”时为可选参数。<br>参数含义：该参数用于指定头增强动作插入MSISDN字段需要去除的国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，1~4位数字。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 该字符串为空时，代表无需去除用户的MSISDN信息中国家码。 |
| CCFORMAT | Charge Characteristic格式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“CHGCHAR1”、“CHGCHAR2” 或 “CHGCHAR3”时为可选参数。<br>参数含义：该参数用于指定对携带的charge characteristic格式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DECIMAL：十进制。<br>- HEX：十六进制。<br>默认值：无<br>配置原则：根据需求选择填写charge characteristic在报文中格式。 |
| TSPRECISION | 时间精度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“TIMESTAMP1”、“TIMESTAMP2” 或 “TIMESTAMP3”时为可选参数。<br>参数含义：该参数用于配置时间精度。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SECOND：时间戳精度为秒。<br>- MILLISECOND：时间戳精度为毫秒。<br>默认值：无<br>配置原则：无 |
| SALTSW | 是否添加盐值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENCRYALGORI”配置为“MD5” 或 “SHA256”时为可选参数。<br>参数含义：该参数用于配置是否添加盐值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能，有安全风险，不建议使用。<br>默认值：无<br>配置原则：为了保证更好的安全性，建议配置为ENABLE。 |
| GRAYLIST | 灰名单 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATATYPE”配置为“APN”、“BILLINGTYPE”、“CHGCHAR1”、“CHGCHAR2”、“CHGCHAR3”、“CHGID”、“GGSNIP1”、“GGSNIP2”、“GGSNIP3”、“IMEI1”、“IMEI2”、“IMEI3”、“IMSI1”、“IMSI2”、“IMSI3”、“MCC”、“MNC”、“MSIP1”、“MSIP2”、“MSIP3”、“MSISDN1”、“MSISDN2”、“MSISDN3”、“RAT1”、“RAT2”、“RAT3”、“ROAMING1”、“ROAMING2”、“ROAMING3”、“SESSIONID”、“SGSNIP1”、“SGSNIP2”、“SGSNIP3”、“SGSN_MCC_MNC1”、“SGSN_MCC_MNC2”、“SGSN_MCC_MNC3”、“SUBPROFILE1”、“SUBPROFILE2”、“SUBPROFILE3”、“TIMESTAMP1”、“TIMESTAMP2”、“TIMESTAMP3”、“ULI1”、“ULI2”、“ULI3”、“UPIPV4”、“UPIPV6”、“USERDEF1”、“USERDEF2”、“USERDEF3”、“USERDEF4”、“USERPROFALIAS” 或 “ZONEID”时为可选参数。<br>参数含义：该参数用于是否使能头增强字段灰名单功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- 该参数使能时，启用头增强灰名单功能。<br>- 该参数不使能时，关闭头增强灰名单功能。 |
| RC4KEYMD5EN | RC4的密钥MD5 Hash使能标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENCRYALGORI”配置为“RC4”时为可选参数。<br>参数含义：该参数用于设置RC4的密钥MD5 Hash使能标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：使用HeadEnGlbPara控制RC4加密前是否需要做一次MD5加密。<br>- DISABLE：不使能，RC4加密前不需要做一次MD5加密。<br>- ENABLE：使能，RC4加密前需要做一次MD5加密。<br>默认值：无<br>配置原则：无 |
| CIPHERTXTENCODE | 头增强密文编码方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENCRYALGORI”配置为“AES128”、“AES256”、“MD5”、“RC4”、“SHA256”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为可选参数。<br>参数含义：该参数用于设置头增强密文的编码方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：使用BASE64和BIT475控制是否对头增强密文做特殊编码。<br>- NONE：不对头增强密文做特殊编码。<br>- BASE64：对头增强密文做BASE64编码。<br>- ASCII：对头增强密文做ASCII编码。<br>默认值：无<br>配置原则：<br>- 如果运营商想要对头增强加密结果进行BASE64编码，则配置为BASE64。<br>- 如果运营商想对头增强加密结果进行ASCII编码，则配置为ASCII。 |
| HEADENEQNULLFLG | 头增强等号替换标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CIPHERTXTENCODE”配置为“BASE64”时为可选参数。<br>参数含义：该参数用于设置头增强等号替换标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NORPLC：不对等号进行替换处理。<br>- NULL：删除等号。<br>- RPLC：使用指定字符替换等号。<br>默认值：无<br>配置原则：无 |
| HEADENEQRPLCHR | 头增强等号替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CIPHERTXTENCODE”配置为“BASE64”时为可选参数。<br>参数含义：该参数用于设置头增强等号替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。不支持空格。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| HEADENSLRPLCHR | 头增强斜杠替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CIPHERTXTENCODE”配置为“BASE64”时为可选参数。<br>参数含义：该参数用于设置头增强斜杠替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。不支持空格。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| HEADENPLRPLCHR | 头增强加号替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CIPHERTXTENCODE”配置为“BASE64”时为可选参数。<br>参数含义：该参数用于设置头增强加号替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。不支持空格。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TLSHEADEN]] · HTTPS头增强（TLSHEADEN）

## 使用实例

假如运营商希望把名称为“headen1”的HTTPS头增强修改为支持插入MSISDN，tls-type值为10000，防欺诈功能不开启，选择AES128 GCM加密方式，密钥为XXXXXX：

```
MOD TLSHEADEN:HEADERENNAME="headen1",DATATYPE=MSISDN1,TLSTYPEVAL =10000,ENCRYALGORI=AES128_GCM,PSWDKEY="XXXXXX",PSWDKEYCONFIRM="XXXXXX",ANTIFRAUD=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-TLSHEADEN.md`
