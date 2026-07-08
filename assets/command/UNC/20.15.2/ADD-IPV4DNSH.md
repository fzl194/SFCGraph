---
id: UNC@20.15.2@MMLCommand@ADD IPV4DNSH
type: MMLCommand
name: ADD IPV4DNSH（增加IPV4 DNS Hostfile记录）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPV4DNSH
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS Hostfile管理
status: active
---

# ADD IPV4DNSH（增加IPV4 DNS Hostfile记录）

## 功能

**适用网元：SGSN、MME**

该命令用于配置网元接口所对应的IPv4地址信息，该信息用于网元选择时DNS查询功能。

进行域名解析可以使用两种手段：使用DNS服务器或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。本命令用于配置本地主机信息表Hostfile。

如果配置了多个IP地址，域名解析结果中将会根据 “PRIORITY（优先级）” 和 “WEIGHT（权重）” 进行先后次序排列：

1. 优先级别高的排前面。
2. 同一优先级别的再按照权重来选择，权重越大，则排在前面的概率越高。

## 注意事项

- 本表最大记录数为8192。
- 该命令执行后立即生效。
- 该命令不论LICENSE表中的智能网关选择特性是否启动都可以执行，但只有在该功能开关打开的时候智能网关选择特性才会正常运行。
- 该表中主机信息配置的“主机名”不能重复，最多能配置1024个主机名。
- 一个主机名最多能对应64个IP地址，且64个地址中至少有一个必须配置为有效地址，即“[1.0.0.0,255.255.255.254]”内的IP地址。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSINDEX | 主机名索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网元接口的索引。<br>数据来源：整网规划<br>取值范围：1~1024<br>默认值：无 |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置主机名。<br>数据来源：整网规划<br>取值范围：1~255位字符串<br>默认值：无<br>配置原则：<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。<br>- 配置SGW主机名，格式为<APNNI>.MNC<MNC>.MCC<MCC>.GPRS，其中<MNC>和<MCC>为3位十进制数。<br>- 主机名不能以“.”开始，也不能以“.”结束。<br>- 配置[**ADD DNSN**](../DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md)使用的主机名，例如topon.S5.gw4.cluster1.net27.example.com。依照协议，此类主机名的配置包含三个标签，格式为<"topon" \| "topoff"><single-label-interface-name><canonical-node-name>。各标签含义如下：- "topon" \| "topoff"：指示该主机名是否配置了拓扑信息。开启智能网关选择特性时建议配置为topon，否则只能进行合一节点的选择。- single-label-interface-name：接口名称，仅作为一个标识，并非实际的物理接口。- canonical-node-name：规范的节点名称，可以体现不同主机名间的拓扑关系。从末尾的点分名称开始比较，相同的点分名称越多，表明两个主机名称之间的拓扑关系越近。说明：即使其他两个标签完全相同，接口名称不同，也代表不同的主机名，即主机名称不等同于网元节点名称。 |
| ADDRSECTION | 地址区间号 | 可选必选说明：必选参数<br>参数含义：该参数用来划分IP地址区间。对同一个域名最多可以配置64个IP地址，使用此参数可以将64个IP地址划分为8个IP地址区间，每个区间最多8个IP地址，这样可以分8次来配置64个IP地址。<br>数据来源：整网规划<br>取值范围：<br>- “SECTION1(SECTION1)”<br>- “SECTION2(SECTION2)”<br>- “SECTION3(SECTION3)”<br>- “SECTION4(SECTION4)”<br>- “SECTION5(SECTION5)”<br>- “SECTION6(SECTION6)”<br>- “SECTION7(SECTION7)”<br>- “SECTION8(SECTION8)”<br>默认值：无 |
| IPV4ADDR1_IPV4ADDR8 | IPv4地址1~IPv4地址8 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主机对应的IPv4地址。<br>数据来源：整网规划<br>取值范围：1.0.0.0~255.255.255.254<br>默认值：无<br>配置原则：<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| PRIORITY1_PRIORITY8 | 优先级1~优先级8 | 可选必选说明：可选参数<br>参数含义：该参数用于配置IP地址的优先级。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：127<br>配置原则：<br>- 优先级数值配置越小，代表优先级越高。<br>- IP地址的优先级越高，则顺序越靠前。<br>- 该参数可能受软参BYTE93 BIT3的影响，详情请见软参说明书。 |
| WEIGHT1_WEIGHT8 | 权重1~权重8 | 可选必选说明：可选参数<br>参数含义：该参数用于配置IP地址的权重。<br>数据来源：整网规划<br>取值范围：1~255<br>默认值：127<br>配置原则：<br>- 权重数值配置越大，代表权重越大。<br>- 对于同优先级的IP地址，进行随机选择，IP地址的权重越大，被选中的概率就越大。 |

## 操作的配置对象

- [IPV4 DNS Hostfile记录（IPV4DNSH）](configobject/UNC/20.15.2/IPV4DNSH.md)

## 使用实例

增加一个主机名索引值为2，HOSTNAME为HUAWEI1.COM.GTP.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG，IP地址区间为SECTION1，IP地址为10.10.10.10，优先级为10，权重为100：

ADD IPV4DNSH: HSINDEX=2, HOSTNAME="HUAWEI1.COM.GTP.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.10.10", PRIORITY1=10, WEIGHT1=100;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IPV4-DNS-Hostfile记录(ADD-IPV4DNSH)_26145884.md`
