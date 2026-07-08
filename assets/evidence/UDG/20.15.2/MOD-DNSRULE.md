# 修改DNS规则（MOD DNSRULE）

- [命令功能](#ZH-CN_CONCEPT_0235373557__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0235373557__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0235373557__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0235373557__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0235373557__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0235373557)

**适用NF：PGW-U、UPF**

该命令用于修改一条DNS规则。

#### [注意事项](#ZH-CN_CONCEPT_0235373557)

- 该命令执行后立即生效。
- APPLICATIONID与DNSRULENAME唯一标识一条记录。
- 当SET DNSLITEPARA中DNSLPOLICYSW使能后该规则才生效。
- 每个APPLICATIONID和DOMAIN下配置的IPADDRESS不可以重复。
- 每个APPLICATIONID下的DOMAIN配置的IPV4ADDRESS最大不超过16个。
- 每个APPLICATIONID下的DOMAIN配置的IPV6ADDRESS最大不超过16个。
- 当domian达到上限时，不支持mod操作。

#### [操作用户权限](#ZH-CN_CONCEPT_0235373557)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0235373557)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATIONID | 应用标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置DNS列表所属的应用标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：该参数用于和SMF下发的PDR中携带的Application ID进行匹配。 |
| DNSRULENAME | DNS规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置DNS规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| DOMAIN | 域名 | 可选必选说明：可选参数<br>参数含义：该参数用于设置DNS规则的服务器域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| IPVERSION | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS域名的IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：该DOMAIN对应的地址类型。 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定域名对应的IPv4类型的服务器地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定域名对应的IPv6类型的服务器地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DNSTTL | DNS TTL | 可选必选说明：可选参数<br>参数含义：该参数用于设置域名解析信息在DNS中的存在时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

#### [使用实例](#ZH-CN_CONCEPT_0235373557)

在需要修改轻量DNS规则时，执行该命令修改现有规则：

```
MOD DNSRULE: APPLICATIONID="app1", DNSRULENAME="rule1", DOMAIN="huawei11.com", IPVERSION=IPV4, IPV4ADDRESS="10.0.0.11", DNSTTL=11;
```
