---
id: UNC@20.15.2@MMLCommand@ADD CHGBEHA
type: MMLCommand
name: ADD CHGBEHA（增加计费行为参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHGBEHA
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 12
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费行为参数配置
status: active
---

# ADD CHGBEHA（增加计费行为参数）

## 功能

**适用网元：SGSN**

该命令用于增加计费行为参数。计费行为是指对特定费率的用户计费时的特殊处理，例如向指定的CG发送话单。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为12。
- 以下的四种计费行为只能配置一次：关闭空闲PDP长定时器、关闭空闲PDP短定时器、禁止使用漫游用户本地的GGSN、禁止网络发起QoS变更。
- 同一种计费属性不能同时支持关闭空闲PDP长定时器、关闭空闲PDP短定时器两种计费行为。
- 对于不生成S-SMO-CDR的SMSC地址、不生成S-SMT-CDR的SMSC地址、不生成SMS-CDR的SMSC地址三种行为属性，均只对本网用户的R4及以上版本话单有效，并受[**SET CHGPLMNCHAR**](../PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md)控制，且当记录中“行为属性”相同时，“SMSC地址”不能相同。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。
- 不同命令配置的CG优先级从高到低的次序是：[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)，[**ADD CHGBEHA**](增加计费行为参数(ADD CHGBEHA)_26145366.md)，[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)，[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CB | 计费行为 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费行为的编号。<br>数据来源：整网规划<br>取值范围：<br>- “B1(B1)”<br>- “B2(B2)”<br>- “B3(B3)”<br>- “B4(B4)”<br>- “B5(B5)”<br>- “B6(B6)”<br>- “B7(B7)”<br>- “B8(B8)”<br>- “B9(B9)”<br>- “B10(B10)”<br>- “B11(B11)”<br>- “B12(B12)”<br>默认值：无<br>配置原则：不同记录的CB的取值不能重复。 |
| BA | 行为属性 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费行为的含义。<br>数据来源：整网规划<br>取值范围：<br>- “PLT(关闭空闲PDP长定时器)”：表示关闭空闲PDP长定时器，具有该计费行为的用户如果在此时间段内，没有任何的数据传输，将会被强制去激活。<br>- “PST(关闭空闲PDP短定时器)”：表示关闭空闲PDP短定时器，具有该计费行为的用户如果在此时间段内，没有任何的数据传输，将会被强制去激活。<br>- “NOROAMING(禁止漫游用户使用本地的GGSN)”：表示禁止漫游用户使用本地的GGSN，具有该计费行为的漫游用户将不能使用本地的GGSN。<br>- “NOQOS(禁止网络发起QoS变更)”：表示禁止网络发起QoS变更，具有该计费行为的用户将被禁止网络侧发起QoS变更。<br>- “CGIP(CG的IP地址)”：表示CG的IP地址，具有该计费行为的用户话单将会优先发往该CG。该CG的优先级高于计费属性指定的CG，GGSN或其他CG推荐的CG，和运营商配置的CG。<br>- “SMSC(不生成S-SMO-CDR的SMSC地址)”：表示不生成S-SMO-CDR的SMSC地址，具有该计费行为的本网用户如果向该SMSC地址发送短消息，S-SMO-CDR话单将不会产生。<br>- “SMSCMT(不生成S-SMT-CDR的SMSC地址)”：表示不生成S-SMT-CDR的SMSC地址，具有该计费行为的本网用户如果收到该SMSC地址发送的短消息，S-SMT-CDR话单将不会产生。<br>- “SMSCMOMT(不生成SMS-CDR的SMSC地址)”：表示不生成SMS-CDR的SMSC地址，SMS-CDR包括S-SMO-CDR与S-SMT-CDR。具有该计费行为的本网用户如果与该SMSC地址间有短消息业务，S-SMO-CDR与S-SMT-CDR话单都将不会产生。<br>默认值：无<br>配置原则：当参数设置为<br>“PLT(关闭空闲PDP长定时器)”<br>或者<br>“PST(关闭空闲PDP短定时器)”<br>时，“去激活空闲PDP上下文”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>106206<br>，License项：<br>LKV2DAPDP02<br>）。 |
| PURGELEN | 关闭空闲PDP定时器时长（min） | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定关闭空闲PDP定时器时长，配置了该计费行为的某种计费属性的用户，如果在此时长内没有任何的数据传输，将被强制去激活。为了避免PDP上下文去激活速度过快对系统造成的影响，系统将平缓处理PDP上下文的去激活。因此，当较短时间内有大量PDP上下文去激活时，关闭空闲PDP长/短定时器的超时时间可能会延迟5～10分钟。<br>前提条件：该参数在<br>“BA”<br>设置为<br>“PLT(关闭空闲PDP长定时器)”<br>或<br>“PST(关闭空闲PDP短定时器)”<br>时有效。<br>数据来源：整网规划<br>取值范围：30～1440<br>默认值：无<br>配置原则：在小于GGSN设置的空闲PDP时长的前提下，建议以5分钟或者10分钟步长渐进调整。<br>说明：受用户数及业务流量等因素的影响，空闲PDP上下文去激活的实际时长可能稍大于操作员设置的时长。 |
| SMSCADDR | SMSC地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SMSC地址，配置了该计费行为的某种计费属性的本网用户，如果用户与此SMSC间有短消息业务，将不会生成S-SMO-CDR或S-SMT-CDR或两者都不会生成。<br>前提条件：该参数在<br>“BA”<br>设置为<br>“SMSC(不生成S-SMO-CDR的SMSC地址)”<br>或<br>“SMSCMT(不生成S-SMT-CDR的SMSC地址)”<br>或<br>“SMSCMOMT(不生成SMS-CDR的SMSC地址)”<br>时有效。<br>数据来源：整网规划<br>取值范围：长度不超过16的数字<br>默认值：无<br>配置原则：同一种行为属性的SMSC地址取值不能重复。 |
| IPT | IP地址类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CG的IP地址类型。<br>前提条件：该参数在<br>“BA”<br>设置为<br>“CGIP(CG的IP地址)”<br>时有效。<br>数据来源：整网规划<br>取值范围：枚举类型<br>- “IPV4(IPV4地址)”<br>- “IPV6(IPV6地址)”<br>默认值：<br>“IPV4(IPV4地址)” |
| CGIP | CG的IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CG的IPv4地址，具有该计费行为的某种计费属性用户的话单优先发往CG的IPv4地址。该CG的优先级高于计费属性指定的CG、GGSN、其他CG推荐的CG或运营商配置的CG。<br>前提条件：<br>- 该参数在“IPT”设置为“IPV4(IPv4地址)”时有效。<br>- 只有[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)命令配置的CG，才能在[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)、[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)和此命令中生效。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>配置原则：每种计费属性只能配置一个CG IPv4的计费行为，但可以有几个SMSC地址的计费行为。<br>说明：“0.0.0.0”和“255.255.255.255”是无效的IPv4地址。 不同记录的CG IPv4地址的取值不能重复。不同命令配置的CG优先级从高到低的次序是：<br>[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)<br>，<br>[**ADD CHGBEHA**](增加计费行为参数(ADD CHGBEHA)_26145366.md)<br>，<br>[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)<br>，<br>[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)<br>。 |
| CGIPV6 | CG的IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CG的IPv6地址，具有该计费行为的某种计费属性用户的话单优先发往CG的IPv6地址。该CG的优先级高于计费属性指定的CG、GGSN、其他CG推荐的CG或运营商配置的CG。<br>前提条件：<br>- 该参数在“IPT”设置为“IPV6(IPv6地址)”时有效。<br>- 只有[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)命令配置的CG，才能在[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)、[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)和此命令中生效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：每种计费属性只能配置一个CG IPv6的计费行为，但可以有几个SMSC地址的计费行为。<br>说明：“::”和“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”是无效的IPv6地址。 不同记录的CG IPv6地址的取值不能重复。不同命令配置的CG优先级从高到低的次序是：<br>[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)<br>，<br>[**ADD CHGBEHA**](增加计费行为参数(ADD CHGBEHA)_26145366.md)<br>，<br>[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)<br>，<br>[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)<br>。 |
| ACC | 支持的计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费行为支持的计费属性。<br>数据来源：整网规划<br>取值范围：<br>- “HOTBILLING(实时计费)”：表示实时计费属性，按照此种方式计费的用户将在短时间或流量达到某个值时及时生成话单，保证运营商对此类用户及时收费。<br>- “FLATRATE(包月制)”：表示包月制计费属性，按照此种方式计费的用户在一个月内的收费是固定的。<br>- “PREPAID(预付费)”：表示预付费计费属性，按照此种方式计费的用户在获取某种服务之前需要预支付一定的费用。<br>- “NORMAL(普通计费)”：表示普通计费属性，按照此种方式计费的用户按照常规的方式支付费用。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGBEHA]] · 计费行为参数（CHGBEHA）

## 使用实例

1. 增加一个计费行为，计费行为B1，行为属性为关闭空闲PDP长定时器，关闭空闲PDP定时器时长为60分钟，支持的计费属性包括普通计费属性、预付费计费属性、包月制计费属性和实时计费属性，配置格式为：
  ADD CHGBEHA: CB=B1, BA=PLT, PURGELEN=60, ACC=HOTBILLING-1&FLATRATE-1&PREPAID-1&NORMAL-1;
2. 增加一个计费行为，计费行为B2，行为属性为CG的IP地址，CG的IP地址为172.24.6.101，支持的计费属性包括包月制计费属性和实时计费属性，配置格式为：
  ADD CHGBEHA: CB=B2, BA=CGIP, IPT=IPV4, CGIP="172.24.6.101", ACC=HOTBILLING-1&FLATRATE-1&PREPAID-0&NORMAL-0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CHGBEHA.md`
