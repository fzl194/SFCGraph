---
id: UNC@20.15.2@MMLCommand@MOD CHGPLMNCG
type: MMLCommand
name: MOD CHGPLMNCG（修改PLMN-CG配置参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CHGPLMNCG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- PLMN CG 配置
status: active
---

# MOD CHGPLMNCG（修改PLMN-CG配置参数）

## 功能

**适用网元：SGSN**

该命令用于修改为PLMN配置CG IP的地址。该PLMN上产生的话单会优先发往这些已配置过的CG。

## 注意事项

- 该命令执行后立即生效。执行后会影响修改后话单发送的CG选择。
- 该命令中配置的CG，需要先在CG配置表（[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)）中进行配置。CG配置表中会配置该CG的属性，如端口号，支持的协议版本等，这样SGSN才能与CG建立正常的链路，话单只能发给链路正常的CG。
- 最多可以为一个PLMN配置5个CG，优先选用CG1，如果CG1链路不正常，则依次选择本表中其它链路正常的CG。当[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令的“EXTRANGE”为“NO”时，如果没有为某个PLMN配置CG IP地址，或已配置的CG链路均不正常，SGSN会将话单存在硬盘上；当[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令人“EXTRANGE”为“YES”时，如果没有为某个PLMN配置CG IP地址，或已配置的CG链路均不正常，根据优先级选择“缺省CG标识”属性为“YES”的CG。请参见[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)命令说明。
- 修改数据时，需要参照[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)中的参数“EXTRANGE”。如果“EXTRANGE”设置为“禁止非PLMNCG”时，新增记录和表中各记录之间的CGIP1，CGIP2，CGIP3，CGIP4，CGIP5要么完全相同，要么完全不同，否则赋值报错。如果“EXTRANGE”设置为“允许非PLMNCG”时，则无需判断。
- 在[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)中参数“PLMNCG范围扩展”为“NO”的情况下，若在配置该CG地址的最后一条[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)中“缺省CG”为“YES”时，当前命令不能用来为PLMN配置此CG地址。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示PLMN的移动国家号码。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示PLMN的移动网号码。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示CG的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPV4地址)”<br>- “IPV6(IPV6地址)”<br>默认值：无 |
| CGIP1 | CG1的IPV4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG1的IPV4地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV4(IPV4地址)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>说明：“0.0.0.0”<br>和<br>“255.255.255.255”<br>是无效的IP地址。 |
| CGIP2 | CG2的IPV4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG2的IPV4地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV4(IPV4地址)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>说明：“0.0.0.0”<br>和<br>“255.255.255.255”<br>是无效的IP地址。 |
| CGIP3 | CG3的IPV4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG3的IPV4地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV4(IPV4地址)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>说明：“0.0.0.0”<br>和<br>“255.255.255.255”<br>是无效的IP地址。 |
| CGIP4 | CG4的IPV4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG4的IPV4地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV4(IPV4地址)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>说明：“0.0.0.0”<br>和<br>“255.255.255.255”<br>是无效的IP地址。 |
| CGIP5 | CG5的IPV4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG5的IPV4地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV4(IPV4地址)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>说明：“0.0.0.0”<br>和<br>“255.255.255.255”<br>是无效的IP地址。 |
| CG1IPV6 | CG1的IPV6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG1的IPV6地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV6(IPV6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| CG2IPV6 | CG2的IPV6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG2的IPV6地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV6(IPV6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPV6地址必须是全球单播地址，不能为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| CG3IPV6 | CG3的IPV6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG3的IPV6地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV6(IPV6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPV6地址必须是全球单播地址，不能为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| CG4IPV6 | CG4的IPV6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG4的IPV6地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV6(IPV6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPV6地址必须是全球单播地址，不能为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| CG5IPV6 | CG5的IPV6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示CG5的IPV6地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV6(IPV6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPV6地址必须是全球单播地址，不能为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [PLMN-CG配置参数（CHGPLMNCG）](configobject/UNC/20.15.2/CHGPLMNCG.md)

## 使用实例

修改PLMN为123001的优先发送话单的CG IPV4地址，两个CG IPV4地址分别修改为“192.168.66.5”和“192.168.177.18”：

MOD CHGPLMNCG: MCC="123", MNC="001", IPT=IPV4, CGIP1="192.168.66.5", CGIP2="192.168.177.18";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PLMN-CG配置参数(MOD-CHGPLMNCG)_72344989.md`
