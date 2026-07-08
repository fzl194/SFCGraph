---
id: UNC@20.15.2@MMLCommand@MOD IPV4DNSH
type: MMLCommand
name: MOD IPV4DNSH（修改IPV4 DNS Hostfile记录）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IPV4DNSH
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

# MOD IPV4DNSH（修改IPV4 DNS Hostfile记录）

## 功能

**适用网元：SGSN、MME**

该命令用于修改网元接口所对应的IPv4地址信息。

## 注意事项

- 该命令执行后立即生效。
- 一个主机名最多能对应64个IP地址，且64个地址中至少有一个必须配置为有效地址，即“[1.0.0.0，255.255.255.254]”内的IP地址。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置主机名。<br>数据来源：整网规划<br>取值范围：1~255位字符串<br>默认值：无<br>配置原则：参见命令<br>[**ADD IPV4DNSH**](增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)<br>。<br>说明：- “HOSTNAME”和“ADDRSECTION”作为组件查找记录，不能修改。<br>- 主机信息表中配置的IPV4 DNS主机名称不能重复。<br>- 主机名不能以“.”开始，也不能以“.”结束。 |
| ADDRSECTION | 地址区间号 | 可选必选说明：必选参数<br>参数含义：该参数用来划分IP地址区间。对同一个域名最多可以配置64个IP地址，使用此参数可以将64个IP地址划分为8个IP地址区间，每个区间最多8个IP地址，这样可以分8次来配置64个IP地址。<br>数据来源：整网规划<br>取值范围：<br>- “SECTION1(SECTION1)”<br>- “SECTION2(SECTION2)”<br>- “SECTION3(SECTION3)”<br>- “SECTION4(SECTION4)”<br>- “SECTION5(SECTION5)”<br>- “SECTION6(SECTION6)”<br>- “SECTION7(SECTION7)”<br>- “SECTION8(SECTION8)”<br>默认值：无<br>说明：- “ADDRSECTION”和“HOSTNAME”作为组件查找记录，不能修改。 |
| IPV4ADDR1_IPV4ADDR8 | IPv4地址1~IPv4地址8 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主机对应的IPV4地址。<br>数据来源：整网规划<br>取值范围：1.0.0.0~255.255.255.254<br>默认值：无<br>说明：- IPv4地址不能为255.255.255.255和0.x.y.z。<br>- IPv4地址设置为0.0.0.0，则该地址无效，为缺省值。<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| PRIORITY1_PRIORITY8 | 优先级1~优先级8 | 可选必选说明：可选参数<br>参数含义：该参数用于配置IP地址的优先级。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：无<br>说明：- 优先级数值配置越小，代表优先级越高。<br>- IP地址的优先级越高，越排在前面。 |
| WEIGHT1_WEIGHT8 | 权重1~权重8 | 可选必选说明：可选参数<br>参数含义：该参数用于配置IP地址的权重。<br>数据来源：整网规划<br>取值范围：1~255<br>默认值：无<br>配置原则：<br>- 权重数值配置越大，代表权重越大。<br>- 对于同优先级的IP地址，进行随机选择，IP地址的权重越大，被选中的概率就越大。<br>说明：权重高的排在前面的机率越高（所配的数越小，权重越小）。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPV4DNSH]] · IPV4 DNS Hostfile记录（IPV4DNSH）

## 使用实例

将HOSTNAME为HUAWEI1.COM.GTP.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG的一条记录，ADDRSECTION1下的IP地址修改为10.10.10.10、优先级修改为10、权重修改为100：

MOD IPV4DNSH: HOSTNAME="HUAWEI1.COM.GTP.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.10.10", PRIORITY1=10, WEIGHT1=100;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IPV4DNSH.md`
