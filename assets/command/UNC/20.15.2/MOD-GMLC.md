---
id: UNC@20.15.2@MMLCommand@MOD GMLC
type: MMLCommand
name: MOD GMLC（修改GMLC配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GMLC
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC配置
status: active
---

# MOD GMLC（修改GMLC配置）

## 功能

**适用网元：SGSN、MME**

此命令用于修改配置互联的GMLC信息及对应的接口配置。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCID | GMLC 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GMLC标识。<br>数据来源：整网规划<br>取值范围：0～639<br>默认值：无 |
| MCC | GMLC所属MCC | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC所属移动国家码。<br>数据来源：整网规划<br>取值范围：3位BCD码<br>默认值：无 |
| MNC | GMLC所属MNC | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC所属移动网码。<br>数据来源：整网规划<br>取值范围：2～3位的BCD码<br>默认值：无 |
| GMLCIPT | GMLC IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>“IPV4(IPv4)”<br>、<br>“IPV6(IPv6)”<br>默认值：无 |
| GMLCIPV4 | GMLC IPV4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GMLC IPV4地址。<br>前提条件：当<br>“GMLC IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时本参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- “GMLC IPV4地址”不能为“0.0.0.0”、“255.255.255.255”和“0.x.y.z”。<br>- “GMLC IPV4地址”不能为组播地址(“224.x.y.z”)和环回地址(“127.x.y.z”)。<br>- “GMLC IPV4地址”必须是A、B或者C类地址。 |
| GMLCIPV6 | GMLC IPV6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GMLC IPV6地址。<br>前提条件：当<br>“GMLC IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时本参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>“GMLC IPV6地址”<br>必须是全球单播地址，不能为<br>“::”<br>、<br>“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”<br>、环回地址(<br>“::1”<br>)、链路本地地址(<br>“FE80::/10”<br>)和组播地址(<br>“FF00::/8”<br>)。<br>说明：目前不支持IPV6地址的配置。 |
| GMLCNO | GMLC 号码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC号码。<br>数据来源：整网规划<br>取值范围：1～16位BCD码<br>默认值：无 |
| HSNM | GMLC 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC主机名，用于GMLC发送PLR时<br>UNC<br>会与消息中携带的orgin-host信元进行比较，如果消息中携带的orgin-host信元在本配置中找不到匹配记录，则返回失败。<br>数据来源：整网规划<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”，大小写不敏感。例如：gmlc.epc.mnc123.mcc123.3gppnetwork.org。<br>- 在E-UTRAN网络中，GMLC主机名必须配置。 |
| IFTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC和<br>UNC<br>之间的接口类型，用来区分不同网络的GMLC。<br>数据来源：整网规划<br>取值范围：<br>- “Lg”：表示该GMLC只支持Lg接口。<br>- “SLg”：表示该GMLC只支持SLg接口。<br>- “Lg-SLg”：表示该GMLC同时支持Lg和Slg接口。<br>默认值 ：无<br>说明：在GERAN和UTRAN网络中，GMLC和<br>UNC<br>间的接口为Lg接口。在E-UTRAN网络中，GMLC和<br>UNC<br>间的接口为SLg接口。 |
| SPTLOCINFO | 支持定位信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC支持的定位信息。MME通过Subscriber Location Report和Provide Subscriber Location Answer消息将定位信息上报给GMLC（3GPP TS 29.172）。<br>数据来源：整网规划<br>配置原则：当<br>“接口类型”<br>参数<br>“SLg(SLg)”<br>被勾选时，该参数生效，请根据GMLC支持的实际情况勾选。<br>取值范围：<br>- “EUTRAN_CELL_ID(E-UTRAN Cell Identifier)”：ESMLC-Cell-Info信元中的ECGI字段。<br>- “CELL_PORTION_ID(Cell Portion ID)”：ESMLC-Cell-Info信元中的Cell-Portion-ID字段。<br>- “CIVIC_ADDR(Civic Address)”：Civic-Address信元。<br>- “BAR_PRESSURE(Barometric Pressure)”：Barometric-Pressure信元。<br>- “VEL_EST(Velocity Estimate)”：Velocity-Estimate信元。<br>- “ADD_POSIT_DATA(Additional Positioning Data)”：EUTRAN-Positioning-Data信元中的Additional Positioning Data字段。<br>默认值 ：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLC]] · GMLC配置（GMLC）

## 使用实例

修改 “GMLC 标识” 为 “1” 的GMLC配置记录，其中 “GMLC IP地址类型” 为 “IPV4(IPv4)” ， “GMLC IPV4地址” 为 “10.10.10.13” ：

MOD GMLC: GMLCID=1, GMLCIPT=IPV4, GMLCIPV4="10.10.10.13";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GMLC.md`
