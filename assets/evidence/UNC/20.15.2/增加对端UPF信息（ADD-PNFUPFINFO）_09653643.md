# 增加对端UPF信息（ADD PNFUPFINFO）

- [命令功能](#ZH-CN_MMLREF_0209653643__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653643__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653643__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653643__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653643)

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加本地配置的对端UPF实例的相关信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## [注意事项](#ZH-CN_MMLREF_0209653643)

- 该命令执行后立即生效。

- 最多可输入1024条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209653643)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653643)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4；不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| IWKEPSIND | UPF是否支持与EPS的互通 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF是否支持与EPS的互通。此参数当前版本不使用。<br>数据来源：全网规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| PDUSESSIONTYPE | PDU会话类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF支持的DNN所支持的PDU会话类型。当所有PduSessionType类型均设置为0时（如IPV4-0 & IPV6-0 & IPV4V6-0 & UNSTRUCTURED-0 & ETHERNET-0），代表支持所有PDU会话类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4（IPV4）”：IPV4<br>- “IPV6（IPV6）”：IPV6<br>- “IPV4V6（IPV4V6）”：IPV4V6<br>- “UNSTRUCTURED（UNSTRUCTURED）”：非结构化网络<br>- “ETHERNET（ETHERNET）”：以太网<br>默认值：IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653643)

增加对端UPF相关信息，NF实例标识为UPF_Instance_0，UPF支持与EPS的互通。

```
ADD PNFUPFINFO: NFINSTANCEID="UPF_Instance_0", IWKEPSIND=TRUE;
```
