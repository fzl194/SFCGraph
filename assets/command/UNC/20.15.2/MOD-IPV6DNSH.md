---
id: UNC@20.15.2@MMLCommand@MOD IPV6DNSH
type: MMLCommand
name: MOD IPV6DNSH（修改IPV6 DNS Hostfile记录）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IPV6DNSH
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
- GTP-C接口管理
- DNS
- DNS Hostfile管理
status: active
---

# MOD IPV6DNSH（修改IPV6 DNS Hostfile记录）

## 功能

**适用网元：SGSN、MME**

该命令用于修改网元接口所对应的IPv6地址信息。

## 注意事项

- 该命令执行后立即生效。
- 一个主机名最多能对应64个IP地址，且64个地址中至少有一个有效的单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置主机名。<br>数据来源：整网规划<br>取值范围：1～255位字符串<br>默认值：无<br>配置原则：参见命令<br>[**ADD IPV6DNSH**](增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md)<br>。<br>说明：- “HOSTNAME”和“ADDRSECTION”作为组件查找记录，不能修改。<br>- 主机信息表中配置的IPV6 DNS主机名称不能重复。 |
| ADDRSECTION | 地址区间号 | 可选必选说明：必选参数<br>参数含义：该参数用来划分IP地址区间。对同一个域名最多可以配置64个IP地址，使用此参数可以将64个IP地址划分为8个IP地址区间，每个区间最多8个IP地址，这样可以分8次来配置64个IP地址。<br>数据来源：整网规划<br>取值范围：<br>- “SECTION1(SECTION1)”<br>- “SECTION2(SECTION2)”<br>- “SECTION3(SECTION3)”<br>- “SECTION4(SECTION4)”<br>- “SECTION5(SECTION5)”<br>- “SECTION6(SECTION6)”<br>- “SECTION7(SECTION7)”<br>- “SECTION8(SECTION8)”<br>默认值：无<br>说明：“ADDRSECTION”<br>和<br>“HOSTNAME”<br>作为组件查找记录，不能修改。 |
| IPV6ADDR1_IPV6ADDR8 | IPv6地址1～IPv6地址8 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主机对应的IPV6地址。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。 |
| PRIORITY1_PRIORITY8 | 优先级1～优先级8 | 可选必选说明：可选参数<br>参数含义：该参数用于配置IP地址的优先级。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：<br>- 优先级数值配置越小，代表优先级越高。<br>- IP地址的优先级越高，越排在前面。 |
| WEIGHT1_WEIGHT8 | 权重1～权重8 | 可选必选说明：可选参数<br>参数含义：该参数用于配置IP地址的权重。<br>数据来源：整网规划<br>取值范围：1～255<br>默认值：无<br>配置原则：<br>- 权重数值配置越大，代表权重越大。<br>- 对于同优先级的IP地址，进行随机选择，IP地址的权重越大，被选中的概率就越大。<br>说明：权重高的排在前面的机率越高（所配的数越小，权重越小）。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPV6DNSH]] · IPV6 DNS Hostfile记录（IPV6DNSH）

## 使用实例

网络改造过程中，将网络中某网元的 “主机名” 为 “HUAWEI1.COM.GTP.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG” 的一条记录，ADDRSECTION1下的 “IPv6地址1” 修改为 “2001:db8:10:19:44:55:10:12” 、 “优先级1” 修改为 “10” 、 “权重1” 修改为 “100” ：

MOD IPV6DNSH: HOSTNAME="HUAWEI1.COM.GTP.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV6ADDR1="2001:db8:10:19:44:55:10:12", PRIORITY1=10, WEIGHT1=100;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IPV6DNSH.md`
