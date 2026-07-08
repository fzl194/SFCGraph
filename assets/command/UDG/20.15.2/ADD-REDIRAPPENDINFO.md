---
id: UDG@20.15.2@MMLCommand@ADD REDIRAPPENDINFO
type: MMLCommand
name: ADD REDIRAPPENDINFO（增加重定向携带信息）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: REDIRAPPENDINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 重定向公共参数管理
- 重定向携带信息
status: active
---

# ADD REDIRAPPENDINFO（增加重定向携带信息）

## 功能

**适用NF：PGW-U、UPF**

此命令用于运营商配置新的重定向携带信息。运营商可以选择在重定向的报文中是否携带原始URL、MSISDN、IMSI、IMEI、MSIP、时间戳信息以及自定义各信息前缀名称，并可以使用AES或blowfish算法对携带MSISDN、IMSI、IMEI、MSIP、时间戳信息进行加密。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 对于原始请求的URL、MSISDN、IMSI、IMEI、MSIP、时间戳，若配置为携带还可设定字段名称，不配置字段名称就采用默认值，默认的原始请求URL字段名称为dest_url，默认的MSISDN字段名称为msisdn，默认的IMSI字段名称为imsi，默认的IMEI字段名称为imei，默认的MSIP字段名称为msip，默认的时间戳字段名称为u。
- 当需要配置密码时，需要同时输入密码确认，两次输入一致才能配置成功。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPENDINFONAME | 重定向携带信息名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置重定向携带信息名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| REQURLFLAG | 请求URL标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否在重定向的目标URL里带上请求的原始URL。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 当运营商需要在URL重定向时在目标URL里带上请求的原始URL，需要打开此开关，将参数需配置为ENABLE。<br>- 当运营商需要在URL重定向时在目标URL里不带上请求的原始URL，需要关闭此开关，将参数需配置为DISABLE。 |
| REQURLNAME | 请求URL名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“REQURLFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定重定向的目标URL中携带的原始请求URL的前缀名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：dest_url<br>配置原则：无 |
| MSISDNFLAG | MSISDN携带标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否在重定向的目标URL里带上用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 当运营商需要在URL重定向时在目标URL里带上用户的MSISDN信息，需要打开此开关，将参数需配置为ENABLE。<br>- 当运营商需要在URL重定向时在目标URL里不带上用户的MSISDN信息，需要关闭此开关，将参数需配置为DISABLE。 |
| MSISDNNAME | MSISDN名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSISDNFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定重定向的目标URL中携带的MSISDN信息的前缀名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：msisdn<br>配置原则：无 |
| MSISDNENCRYALGORI | MSISDN加密算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSISDNFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定对重定向的目标URL中携带的MSISDN信息进行加密的算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NONE：表示不进行加密，有安全风险，不建议使用。<br>- AES128：使用128位密钥的AES CBC模式加密算法，AES128 CBC模式有安全风险，不建议使用。<br>- BLOWFISH128：使用128位密钥的blowfish算法，有安全风险，不建议使用。<br>- AES256：使用256位密钥的AES CBC模式加密算法，AES256 CBC模式有安全风险，不建议使用。<br>- AES128_GCM：表示加密类型为AES128 GCM模式。<br>- AES128_CTR：表示加密类型为AES128 CTR模式。<br>- AES256_GCM：表示加密类型为AES256 GCM模式。<br>- AES256_CTR：表示加密类型为AES256 CTR模式。<br>默认值：AES256_GCM<br>配置原则：<br>- 当运营商需要指定对携带的MSISDN信息进行加密的算法为aes128时，需要配置该参数为AES128。<br>- 当运营商需要指定对携带的MSISDN信息进行加密的算法为aes256时，需要配置该参数为AES256。<br>- 当运营商需要指定对携带的MSISDN信息进行加密的算法为blowfish128时，需要配置该参数为BLOWFISH128。<br>- 当运营商不需要对MSISDN信息加密时则不配置该参数。<br>- 请根据需求选择相应加密算法，建议使用AES128_GCM或AES256_GCM加密算法，当配置为BLOWFISH128，AES128，AES256或为空时有安全风险，不建议使用。 |
| MSISDNSECRETKEY | MSISDN密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MSISDNENCRYALGORI”配置为“AES128”、“BLOWFISH128”、“AES256”、“AES128_CTR”、“AES256_CTR”、“AES256_GCM” 或 “AES128_GCM”时为必选参数。<br>参数含义：该参数用于指定对MSISDN信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| MSISDNSECRETKEYCONFIRM | 确认MSISDN密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MSISDNENCRYALGORI”配置为“AES128”、“BLOWFISH128”、“AES256”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于确认对MSISDN信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| IMSIFLAG | IMSI携带标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否在重定向的目标URL里带上用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 当运营商需要在URL重定向时在目标URL里带上用户的IMSI信息，需要打开此开关，将参数需配置为ENABLE。<br>- 当运营商需要在URL重定向时在目标URL里不带上用户的IMSI信息，需要关闭此开关，将参数需配置为DISABLE。 |
| IMSINAME | IMSI名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IMSIFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定重定向的目标URL中携带的IMSI信息的前缀名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：imsi<br>配置原则：无 |
| IMSIENCRYALGORI | IMSI加密算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IMSIFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定对重定向的目标URL中携带的IMSI信息进行加密的算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NONE：表示不进行加密，有安全风险，不建议使用。<br>- AES128：使用128位密钥的AES CBC模式加密算法，AES128 CBC模式有安全风险，不建议使用。<br>- BLOWFISH128：使用128位密钥的blowfish算法，有安全风险，不建议使用。<br>- AES256：使用256位密钥的AES CBC模式加密算法，AES256 CBC模式有安全风险，不建议使用。<br>- AES128_GCM：表示加密类型为AES128 GCM模式。<br>- AES128_CTR：表示加密类型为AES128 CTR模式。<br>- AES256_GCM：表示加密类型为AES256 GCM模式。<br>- AES256_CTR：表示加密类型为AES256 CTR模式。<br>默认值：AES256_GCM<br>配置原则：<br>- 当运营商需要指定对携带的IMSI信息进行加密的算法为aes128时，需要配置该参数为AES128。<br>- 当运营商需要指定对携带的IMSI信息进行加密的算法为aes256时，需要配置该参数为AES256。<br>- 当运营商需要指定对携带的IMSI信息进行加密的算法为blowfish128时，需要配置该参数为BLOWFISH128。<br>- 当运营商不需要对IMSI信息加密时则不配置该参数。<br>- 请根据需求选择相应加密算法，建议使用AES128_GCM或AES256_GCM加密算法，当配置为BLOWFISH128，AES128，AES256或为空时有安全风险，不建议使用。 |
| IMSISECRETKEY | IMSI密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMSIENCRYALGORI”配置为“AES128”、“BLOWFISH128”、“AES256”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于指定对IMSI信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| IMSISECRETKEYCONFIRM | 确认IMSI密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMSIENCRYALGORI”配置为“AES128”、“BLOWFISH128”、“AES256”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于确认对IMSI信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| IMEIFLAG | IMEI携带标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否在重定向的目标URL里带上用户的IMEI信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 当运营商需要在URL重定向时在目标URL里带上用户的IMEI信息，需要打开此开关，将参数需配置为ENABLE。<br>- 当运营商需要在URL重定向时在目标URL里不带上用户的IMEI信息，需要关闭此开关，将参数需配置为DISABLE。 |
| IMEINAME | IMEI名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IMEIFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定重定向的目标URL中携带的IMEI信息的前缀名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：imei<br>配置原则：无 |
| IMEIENCRYALGORI | IMEI加密算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IMEIFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定对重定向目标URL中携带的IMEI信息进行加密的算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NONE：表示不进行加密，有安全风险，不建议使用。<br>- AES128：使用128位密钥的AES CBC模式加密算法，AES128 CBC模式有安全风险，不建议使用。<br>- BLOWFISH128：使用128位密钥的blowfish算法，有安全风险，不建议使用。<br>- AES256：使用256位密钥的AES CBC模式加密算法，AES256 CBC模式有安全风险，不建议使用。<br>- AES128_GCM：表示加密类型为AES128 GCM模式。<br>- AES128_CTR：表示加密类型为AES128 CTR模式。<br>- AES256_GCM：表示加密类型为AES256 GCM模式。<br>- AES256_CTR：表示加密类型为AES256 CTR模式。<br>默认值：AES256_GCM<br>配置原则：<br>- 当运营商需要指定对携带的IMEI信息进行加密的算法为aes128时，需要配置该参数为AES128。<br>- 当运营商需要指定对携带的IMEI信息进行加密的算法为aes256时，需要配置该参数为AES256。<br>- 当运营商需要指定对携带的IMEI信息进行加密的算法为blowfish128时，需要配置该参数为BLOWFISH128。<br>- 当运营商不需要对IMEI信息加密时则不配置该参数。<br>- 请根据需求选择相应加密算法，建议使用AES128_GCM或AES256_GCM加密算法，当配置为BLOWFISH128，AES128，AES256或为空时有安全风险，不建议使用。 |
| IMEISECRETKEY | IMEI密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMEIENCRYALGORI”配置为“AES128”、“AES256”、“BLOWFISH128”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于指定对IMEI信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| IMEISECRETKEYCONFIRM | 确认IMEI密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMEIENCRYALGORI”配置为“AES128”、“AES256”、“BLOWFISH128”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于确认对IMEI信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| MSIPFLAG | MSIP携带标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否在重定向的目标URL中是否携带MSIP。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 当运营商需要在URL重定向报文中携带MSIP，需要打开此开关，将参数需配置为ENABLE。<br>- 当运营商需要在URL重定向报文中不携带MSIP，需要关闭此开关，将参数需配置为DISABLE。 |
| MSIPNAME | MSIP名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSIPFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定重定向的目标URL中携带的MSIP信息的前缀名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：msip<br>配置原则：无 |
| MSIPENCRYALGORI | MSIP加密算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSIPFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定对重定向的目标URL中携带的MSIP信息进行加密的算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NONE：表示不进行加密，有安全风险，不建议使用。<br>- AES128：使用128位密钥的AES CBC模式加密算法，AES128 CBC模式有安全风险，不建议使用。<br>- BLOWFISH128：使用128位密钥的blowfish算法，有安全风险，不建议使用。<br>- AES256：使用256位密钥的AES CBC模式加密算法，AES256 CBC模式有安全风险，不建议使用。<br>- AES128_GCM：表示加密类型为AES128 GCM模式。<br>- AES128_CTR：表示加密类型为AES128 CTR模式。<br>- AES256_GCM：表示加密类型为AES256 GCM模式。<br>- AES256_CTR：表示加密类型为AES256 CTR模式。<br>默认值：AES256_GCM<br>配置原则：<br>- 当运营商需要指定对携带的MSIP信息进行加密的算法为aes128时，需要配置该参数为AES128。<br>- 当运营商需要指定对携带的MSIP信息进行加密的算法为aes256时，需要配置该参数为AES256。<br>- 当运营商需要指定对携带的MSIP信息进行加密的算法为blowfish128时，需要配置该参数为BLOWFISH128。<br>- 当运营商不需要对MSIP信息加密时则不配置该参数。<br>- 请根据需求选择相应加密算法，建议使用AES128_GCM或AES256_GCM加密算法，当配置为BLOWFISH128，AES128，AES256或为空时有安全风险，不建议使用。 |
| MSIPSECRETKEY | MSIP密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MSIPENCRYALGORI”配置为“AES128”、“AES256”、“BLOWFISH128”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于指定对MSIP信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| MSIPSECRETKEYCONFIRM | 确认MSIP密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MSIPENCRYALGORI”配置为“AES128”、“AES256”、“BLOWFISH128”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于确认对MSIP信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| TIMEFLAG | 时间戳携带标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否在重定向的目标URL里带上时间信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 当运营商需要在URL重定向时在目标URL里带上时间戳信息，需要打开此开关，将参数需配置为ENABLE。<br>- 当运营商需要在URL重定向时在目标URL里不带上时间戳信息，需要关闭此开关，将参数需配置为DISABLE。 |
| TIMENAME | 时间戳名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TIMEFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定重定向的目标URL中携带的时间标识信息的前缀名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：u<br>配置原则：无 |
| TIMETYPE | 时间戳类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TIMEFLAG”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定加密时间戳的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCAL：指定时间格式为localtime。 localtime表示本地时间，是指根据时区或者当地的夏令时规定而设置的时间。<br>- UTC：指定时间格式为utc，utc表示（Universal Time Coordinated）世界协调时间，时区的改变以及夏令时的实施都不会改变UTC时间。<br>- RELATIVE：当前UTC时间，相对于1970年1月1日0时0分0秒的时间差秒数。<br>默认值：LOCAL<br>配置原则：Local：当地时间，精确到秒，格式为年月日时分秒，如20181009164805。 UTC：UTC时间，精确到秒，格式为年月日时分秒，如20181009164805。 Relative：当前UTC时间，相对于1970年1月1日0时0分0秒 的时间差秒数。 |
| TIMEENCRYALGORI | 时间戳加密算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TIMEFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定对重定向的目标URL中携带的时间戳信息进行加密的算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NONE：表示不进行加密，有安全风险，不建议使用。<br>- AES128：使用128位密钥的AES CBC模式加密算法，AES128 CBC模式有安全风险，不建议使用。<br>- BLOWFISH128：使用128位密钥的blowfish算法，有安全风险，不建议使用。<br>- AES256：使用256位密钥的AES CBC模式加密算法，AES256 CBC模式有安全风险，不建议使用。<br>- AES128_GCM：表示加密类型为AES128 GCM模式。<br>- AES128_CTR：表示加密类型为AES128 CTR模式。<br>- AES256_GCM：表示加密类型为AES256 GCM模式。<br>- AES256_CTR：表示加密类型为AES256 CTR模式。<br>默认值：AES256_GCM<br>配置原则：<br>- 当运营商需要指定对携带的时间戳信息进行加密的算法为aes128时，需要配置该参数为AES128。<br>- 当运营商需要指定对携带的时间戳信息进行加密的算法为blowfish128时，需要配置该参数为BLOWFISH128。<br>- 当运营商不需要对时间戳信息加密时则不配置该参数。<br>- 请根据需求选择相应加密算法，建议使用AES128_GCM加密算法，当配置为BLOWFISH128、AES128、AES256或为空时有安全风险，不建议使用。 |
| TIMESECRETKEY | 时间戳密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TIMEENCRYALGORI”配置为“AES128”、“BLOWFISH128”、“AES256”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于指定对时间戳信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| TIMESECRETKEYCONFIRM | 确认时间戳密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TIMEENCRYALGORI”配置为“AES128”、“BLOWFISH128”、“AES256”、“AES128_CTR”、“AES128_GCM”、“AES256_CTR” 或 “AES256_GCM”时为必选参数。<br>参数含义：该参数用于确认对时间戳信息加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，“AES256_CTR”、“AES256_GCM”输入长度范围为1～32，其余算法输入长度为1～16。不支持空格。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@REDIRAPPENDINFO]] · 重定向携带信息（REDIRAPPENDINFO）

## 关联任务

- [[UDG@20.15.2@Task@0-00023]]

## 使用实例

运营商规划定义一个名为“testredirappendinfo”的重定向携带信息，需要携带原始URL、MSISDN、IMSI、IMEI、MS-IP和时间戳信息，原始请求URL前缀名称设为“dest_url”，MSISDN前缀名称设为“msisdn”，IMSI前缀名称设为“imsi”，IMEI前缀名称设为“imei”，MS-IP前缀名称设为“msip”，时间戳前缀名称设为“u”：

```
ADD REDIRAPPENDINFO: APPENDINFONAME="testredirappendinfo", REQURLFLAG=ENABLE, MSISDNFLAG=ENABLE, MSISDNENCRYALGORI=NONE, IMSIFLAG=ENABLE, IMSIENCRYALGORI=NONE, IMEIFLAG=DISABLE, MSIPFLAG=ENABLE, TIMEFLAG=ENABLE, TIMETYPE=LOCAL, TIMEENCRYALGORI=NONE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-REDIRAPPENDINFO.md`
