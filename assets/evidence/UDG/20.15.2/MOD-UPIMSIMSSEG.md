# 修改IMSI和MSISDN号段（MOD UPIMSIMSSEG）

- [命令功能](#ZH-CN_CONCEPT_0000202787041552__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202787041552__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202787041552__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202787041552__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202787041552__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202787041552)

**适用NF：PGW-U、UPF**

该命令用于修改配置IMSI/MSISDN号码段。

#### [注意事项](#ZH-CN_CONCEPT_0000202787041552)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202787041552)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202787041552)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEGMENTTYPE | IMSI/MSISDN号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IMSI：IMSI。<br>- MSISDN：MSISDN。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMSI” 或 “MSISDN”时为必选参数。<br>参数含义：该参数用于指定起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～17。<br>默认值：无<br>配置原则：<br>- SEGMENTTYPE等于IMSI时，SEGSTART取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补0。<br>- SEGMENTTYPE等于MSISDN时，SEGSTART取值范围为1~15位数字，如果开头是19，则取值范围1~17位数字。按照3GPP协议的规定，MSISDN号码的第一个字节应该是0x91，在配置MSISDN时开头可以输入19，SEGSTART截取19之后的字符串存储。SEGSTART过滤开头19后不足15位，系统匹配时自动在末尾补0。<br>- SEGSTART必须小于等于SEGEND。 |
| SEGEND | 号段结束字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMSI” 或 “MSISDN”时为必选参数。<br>参数含义：该参数用于指定结束号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～17。<br>默认值：无<br>配置原则：<br>- SEGMENTTYPE等于IMSI时，SEGEND取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补9。<br>- SEGMENTTYPE等于MSISDN时，SEGEND取值范围为1~15位数字，如果开头是19，则取值范围1~17位数字。按照3GPP协议的规定，MSISDN号码的第一个字节应该是0x91，在配置MSISDN时开头可以输入19，SEGEND截取19之后的字符串存储。SEGEND过滤开头19后不足15位，系统匹配时自动在末尾补9。<br>- SEGEND必须大于等于SEGSTART。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

#### [使用实例](#ZH-CN_CONCEPT_0000202787041552)

修改IMSI和MSISDN号段: SEGMENTNAME为huawei; SEGMENTTYPE为IMSI; SEGSTART为130; SEGEND为139：

```
MOD UPIMSIMSSEG:SEGMENTNAME="huawei",SEGMENTTYPE=IMSI,SEGSTART="130",SEGEND="139";
```
