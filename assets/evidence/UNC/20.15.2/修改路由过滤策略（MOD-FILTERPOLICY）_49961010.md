# 修改路由过滤策略（MOD FILTERPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0000001549961010__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549961010__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549961010__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549961010__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549961010__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549961010)

该命令用于修改IPv4或IPv6路由过滤策略。

#### [注意事项](#ZH-CN_CONCEPT_0000001549961010)

- 该命令执行后立即生效。
- EXPORT和IMPORT都是必选参数，但不能相同。
- IMPORT为TRUE时，FILTERPROTOCOL只能为noprotocol。
- FILTERPROTOCOL为noprotocol、direct或static时，FILTERPROCESSID只能为0。
- FILTERPROTOCOL为ospf或ospfv3时，FILTERPROCESSID不能为0。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549961010)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549961010)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| EXPORT | 出口方向 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn”、“ipv6uni” 或 “ipv6vpn”时为必选参数。<br>参数含义：该参数用于指定该过滤策略是否应用在出口方向。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：EXPORT和IMPORT不能相同。 |
| IMPORT | 入口方向 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn”、“ipv6uni” 或 “ipv6vpn”时为必选参数。<br>参数含义：该参数用于该过滤策略是否应用在入口方向。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：EXPORT和IMPORT不能相同。 |
| FILTERPROTOCOL | 路由协议 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn”、“ipv6uni” 或 “ipv6vpn”时为必选参数。<br>参数含义：该参数用于指定发布路由信息的协议，对其进行过滤。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- noprotocol：默认应用所有协议。<br>- direct：直连路由。<br>- ospf：OSPF路由。<br>- static：静态路由。<br>- ospfv3：OSPFv3路由。<br>默认值：无<br>配置原则：如果AFTYPE为VPNv4或VPNv6，该参数只能选择noprotocol。 |
| FILTERPROCESSID | 协议进程ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn”、“ipv6uni” 或 “ipv6vpn”时为必选参数。<br>参数含义：该参数用于指定单播路由协议的进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：当单播路由协议为ospf或者ospfv3时，FILTERPROCESSID不能为0，当协议为noprotocol、direct、static，FILTERPROCESSID只能为0。 |
| ACLNAMEORNUM | ACL规则标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv4vpn”时为可选参数。<br>参数含义：该参数用于指定IPv4访问控制列表ACL的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。只支持ACL number取值范围为2000-2999的基本ACL策略。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- ACLNAMEORNUM和PREFLT4NAME命令行下发时，这两个参数选择其一。被引用的ACL策略中只会生效ACL number为2000-2999的基本ACL策略。 |
| PREFLT4NAME | IPv4前缀过滤策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv4vpn”时为可选参数。<br>参数含义：该参数用于指定IPv4前缀过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- ACLNAMEORNUM和PREFLT4NAME命令行下发时，这两个参数选择其一。 |
| ACL6NAMEORNUM | ACL6规则标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定IPv6访问控制列表ACL的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。只支持ACL number取值范围为2000-2999的基本ACL策略。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- ACL6NAMEORNUM和PREFLT6NAME两个参数必选其一。被引用的ACL策略中只会生效ACL number为2000-2999的基本ACL策略。 |
| PREFLT6NAME | IPv6前缀过滤策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定IPv6前缀过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- ACL6NAMEORNUM和PREFLT6NAME两个参数必选其一。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549961010)

- 在名称为“vrf1”的BGP VPN实例下修改IPv4单播地址族中的过滤策略参数：
  ```
  MOD FILTERPOLICY:VRFNAME="vrf1",AFTYPE=ipv4uni,EXPORT=FALSE,IMPORT=TRUE,FILTERPROTOCOL=noprotocol,FILTERPROCESSID=0,PREFLT4NAME="asssd";
  ```
- 在名称为“vrf1”的BGP VPN实例下修改IPv6单播地址族中的过滤策略参数：
  ```
  MOD FILTERPOLICY:VRFNAME="vrf1",AFTYPE=ipv6uni,EXPORT=FALSE,IMPORT=TRUE,FILTERPROTOCOL=noprotocol,FILTERPROCESSID=0,PREFLT6NAME="asssd";
  ```
