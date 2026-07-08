---
id: UNC@20.15.2@MMLCommand@MOD EMGCFG
type: MMLCommand
name: MOD EMGCFG（修改运营商紧急呼叫功能配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: EMGCFG
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 紧急呼叫配置
- 紧急呼叫功能配置
status: active
---

# MOD EMGCFG（修改运营商紧急呼叫功能配置）

## 功能

**适用网元：MME**

该命令用于修改指定MNO/MVNO对应的紧急呼叫配置数据。运营商需要使用紧急呼叫业务时，通过此命令配置对应MNO或MVNO下的紧急呼叫的策略、紧急业务的APN和QoS相关配置。

## 注意事项

- 此命令执行后立即生效。
- UE发起紧急Attach或者紧急PDN连接请求的时候，是不会携带APN的，需要由此命令配置对应的紧急APN、紧急承载对应的QoS、APN AMBR。
- 此配置涉及VoLTE紧急呼叫特性（特性编号：WSFD-102101，License部件编码：LKV2VLEC01），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：运营商规划<br>取值范围： 0～64，128～254<br>默认值： 无<br>配置原则：<br>“NOID”<br>指定的记录已经通过<br>[**ADD EMGCFG**](增加运营商紧急呼叫功能配置（ADD EMGCFG）_26305316.md)<br>配置了。 |
| EMGMODE | 紧急承载创建模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置紧急承载创建模式。<br>数据来源：运营商规划<br>取值范围：<br>- “VALIDUE（Valid UE only）”<br>- “AUTHUE（Only UEs that are authenticated are allowed）”<br>- “IMSIUE（IMSI required, authenticated optional）”<br>- “ALLUE（All UE are allowed）：”<br>默认值： 无<br>说明：- “VALIDUE（Valid UE only）”：鉴权通过且签约数据正常都成功且接入限制也通过的UE才可以使用紧急呼叫业务<br>- “AUTHUE（Only UEs that are authenticated are allowed）”：鉴权通过的UE就可以使用紧急呼叫业务<br>- “IMSIUE（IMSI required, authenticated optional）”：有USIM卡的UE就可以使用紧急呼叫业务。说明：为了提高切换成功率，建议MME开启获取IMEI信息功能。<br>[**ADD S1IMEICFG**](../../../业务安全管理/设备检查管理/S1模式IMEI配置/增加S1模式IMEI配置(ADD S1IMEICFG)_26305448.md)<br>- “ALLUE（All UE are allowed）：”：所有UE包括无USIM卡的都可以使用紧急呼叫业务 |
| EMGAPN | 紧急APN | 可选必选说明：必选参数<br>参数含义：该参数用于设置紧急PDN连接创建时使用的APN，需要运营商保证全网规划一致，包括MME、P-GW、PCRF等设备。<br>数据来源：运营商规划<br>取值范围： 长度1～62的字符<br>默认值： 无<br>配置原则：<br>- 字符串中不能出现*。<br>- 紧急APN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- DWORD_EX19 BIT26 控制UNC在VoLTE紧急呼叫附着和PDN连接流程中向DNS发送的查询消息中携带的P-GW的FQDN格式。 |
| ULAPNAMBR | 紧急APN的上行APN AMBR速率（kbit/s） | 可选必选说明：可选参数<br>参数含义：该参数用于设置紧急APN的上行APN AMBR速率。<br>数据来源：运营商规划<br>取值范围： 1～256000<br>默认值： 无<br>说明：该参数表明紧急APN非GBR承载的上行最大比特率，即该参数只影响默认紧急承载，用于IMS信令的传输。用于紧急语音传输的紧急专有承载，是GBR类型承载，其QoS由P-GW确定，跟此参数无关。 |
| DLAPNAMBR | 紧急APN的下行APN AMBR速率（kbit/s） | 可选必选说明：可选参数<br>参数含义：该参数用于设置紧急APN的下行APN AMBR速率。<br>数据来源：运营商规划<br>取值范围： 1～256000<br>默认值： 无<br>说明：该参数表明紧急APN非GBR承载的下行最大比特率，即该参数只影响默认紧急承载，用于IMS信令的传输。用于紧急语音传输的紧急专有承载，是GBR类型承载，其QoS由P-GW确定，跟此参数无关。 |
| QCI | 紧急承载的QCI | 可选必选说明：可选参数<br>参数含义：该参数用于设置控制紧急默认承载的QCI，协议规定IMS的信令承载推荐的QCI是5。<br>数据来源：运营商规划<br>取值范围： 5～9<br>默认值： 无 |
| ARPPRL | 紧急ARP优先级级别 | 可选必选说明：可选参数<br>参数含义：该参数用于设置紧急承载的ARP，该参数应该全网规划一致，包括eNodeB、MME、P-GW。eNodeB主要依赖ARP来确定是紧急承载，并针对紧急承载忽略接入限制等处理。ARP包括Priority Level、Pre-emption Capability、Pre-emption Vulnerability参数。<br>数据来源：运营商规划<br>取值范围： 1～15<br>默认值： 无 |
| ARPPCI | 紧急ARP的Pre-emption Capability | 可选必选说明：可选参数<br>参数含义：该参数用于设置紧急ARP的Pre-emption Capability参数，该参数在无线侧使用，表示在资源拥塞的情况下，本承载是否可以抢占其它承载。<br>数据来源：运营商规划<br>取值范围：<br>“NO（否）”<br>，<br>“YES（是）”<br>默认值： 无 |
| ARPPVI | 紧急ARP的Pre-emption Vulnerability | 可选必选说明：可选参数<br>参数含义：该参数用于设置紧急ARP的Pre-emption Vulnerability参数，该参数在无线侧使用，表示在资源拥塞的情况下，本承载是否可以被其它更高优先级的承载抢占。<br>数据来源：运营商规划<br>取值范围：<br>“NO（否）”<br>，<br>“YES（是）”<br>默认值： 无 |
| EMGPGWIDTYPE | 紧急P-GW标识类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急P-GW标识类型。<br>数据来源：运营商规划<br>取值范围：<br>- “FQDN(FQDN)”<br>- “IP_ADDRESS(IP地址)”<br>- “NULL(关闭)”<br>默认值： 无<br>说明：该参数仅对漫游用户或者无卡用户生效。 |
| FQDN | FQDN | 可选必选说明：条件必选参数<br>参数含义：该参数用于标识由RAI、TAI、APN等构建的域名，用来进行网元查询。<br>数据来源：运营商规划<br>取值范围：1~255位字符串<br>默认值：无<br>前提条件：该参数在<br>“EMGPGWIDTYPE”<br>设置为<br>“FQDN(FQDN)”<br>时有效。<br>配置原则：利用构建的FQDN可以查询SGSN、S-GW、P-GW、IWS等网元。其中构建域名的信元组成如下：<br>- S-GW(TAI)：TAC-LB<TAC-LOW-BYTE>.TAC-HB<TAC-HIGH-BYTE>.TAC.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG。例如：TAC-LB01.TAC-HB71.TAC.EPC.MNC123.MCC123.3GPPNETWORK.ORG。<br>- P-GW(APN): <APNNI>.APN.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG。例如：HUAWEI1.COM.APN.EPC.MNC123.MCC123.3GPPNETWORK.ORG。<br>说明：- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。<br>- <TAC-LOW-BYTE>，<TAC-HIGH-BYTE>为2位十六进制数。<br>- <MNC>，<MCC>为3位十进制数 ，<CELL ID>为4位十进制数。<br>- 如果<>（除了<APNNI>）中的内容不足相应的位数，前面以“0”补齐。<br>- FQDN不能以“.”开始，也不能以“.”结束。 |
| IPTYPE | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：运营商规划<br>取值范围：<br>- “ADDR_TYPE_IPV4(IPV4地址)”<br>- “ADDR_TYPE_IPV6(IPV6地址)”<br>默认值： 无 |
| IPV4ADDR | IPV4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定紧急P-GW标识的IPV4地址。<br>前提条件：该参数在<br>“IPTYPE”<br>设置为<br>“ADDR_TYPE_IPV4(IPV4地址)”<br>时有效。<br>数据来源：运营商规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>说明：“0.0.0.0”和“255.255.255.255”是无效的IP地址。<br>配置原则：<br>- IPv4地址不能为0.0.0.0、255.255.255.255和0.x.y.z。<br>- IPv4地址不能为组播地址（如：224.x.y.z）和环回地址(如：127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6ADDR | IPV6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定紧急P-GW标识的IPV6地址。<br>前提条件：该参数在<br>“IPTYPE”<br>设置为<br>“ADDR_TYPE_IPV6(IPV6地址)”<br>时有效。<br>数据来源：运营商规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EMGCFG]] · 运营商紧急呼叫功能配置（EMGCFG）

## 使用实例

修改一条运营商紧急呼叫功能的配置，针对 “运营商标识” 为 “0” ，使 “紧急APN的上行APN AMBR速率（kbit/s）” 为 “10000” ：

MOD EMGCFG: NOID=0, EMGAPN="1", ULAPNAMBR=10000;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改运营商紧急呼叫功能配置（MOD-EMGCFG）_72345103.md`
