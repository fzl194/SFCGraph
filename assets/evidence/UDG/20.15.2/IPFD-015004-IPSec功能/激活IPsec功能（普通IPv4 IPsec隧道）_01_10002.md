# 激活IPsec功能（普通IPv4 IPsec隧道）

- [操作场景](#ZH-CN_OPI_0161317238__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0161317238__1.3.2)
- [必备事项](#ZH-CN_OPI_0161317238__1.3.3)
- [操作流程](#ZH-CN_OPI_0161317238__1.3.4)
- [操作步骤](#ZH-CN_OPI_0161317238__1.3.5)
- [任务示例](#ZH-CN_OPI_0161317238__1.3.6)

## [操作场景](#ZH-CN_OPI_0161317238)

如 [图1](#ZH-CN_OPI_0161317238__f58130c7d29b9434a85c0152fb71100c7) 所示，网络A和网络B之间采用网关对网关组网模式进行资源传输。网络A和网络B分别通过Device A和Device B连接到Internet，要求通过配置IPsec隧道实现PCA与PCB之间可以安全地互访。

**图1** IPv4 IPsec组网图

<br>

![](激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.assets/zh-cn_image_0279003331.png)

网络环境描述如下：

- 网络A属于10.1.1.0/24子网，通过接口interface2与 Device A 连接。
- 网络B属于10.1.2.0/24子网，通过接口interface2与 Device B 连接。
- Device A 和 Device B 路由可达，假设Device A往Device B方向下一跳地址为172.16.163.2/24，Device B往Device A方向下一跳地址为172.16.169.2/24。

*表1 设备接口IP地址（普通IPv4 IPsec隧道）*

| 设备名称 | 接口 | IP地址 |
| --- | --- | --- |
| Device A VNRS微服务 | Ethernet66/0/5 | 10.1.1.1/24 |
| Device A VNRS微服务 | Ethernet66/0/6 | 172.16.163.1/24（IPsec报文的本端物理出接口） |
| Device A VNRS微服务 | Tunnel10 | 192.168.1.1/32（需要双配） |
| Device B VNRS微服务 | Ethernet66/0/5 | 10.1.2.1/24 |
| Device B VNRS微服务 | Ethernet66/0/6 | 172.16.169.1/24（IPsec报文的本端物理出接口） |
| Device B VNRS微服务 | Tunnel10 | 192.168.1.2/32（需要双配） |
| Device A IPsec微服务 | Tunnel10 | 192.168.1.1/32（IKE协商IP地址） |
| Device B IPsec微服务 | Tunnel10 | 192.168.1.2/32（IKE协商IP地址） |
| PCA | - | 10.1.1.2/24 |
| PCB | - | 10.1.2.2/24 |
| - | Device A侧网关接口 | 172.16.163.2/24 |
| - | Device B侧网关接口 | 172.16.169.2/24 |

## [对系统的影响](#ZH-CN_OPI_0161317238)

本特性对系统无影响。

## [必备事项](#ZH-CN_OPI_0161317238)

前提条件

- 操作人员已经登录网管。
- 配置接口的IP地址。
- 配置路由，使隧道两端路由可达。
- IPSec功能由IPSec服务承载，请完成IPSec安装，参见**软件安装**章节中的“安装可选服务 > 安装IPSec服务”。

数据

需要准备的IPsec安全数据如 [表2](#ZH-CN_OPI_0161317238__tab_1) 所示。

*表2 IPsec安全参数（普通IPv4 IPsec隧道）*

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md) | ACL规则组标识（ACLNAME） | 3000 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | ACL规则组标识（ACLNAME） | 3000 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 规则名称（ACLRULENAME） | rule_1 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 规则行为（ACLACTION） | Permit | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 协议类型值（ACLPROTOCOL） | 0 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 源IP地址（ACLSOURCEIP） | - Device A: 10.1.1.2<br>- Device B: 10.1.2.2 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 源IP地址反掩码（ACLSRCWILD） | 0.0.0.0 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 目的IP地址（ACLDESTIP） | - Device A: 10.1.2.2<br>- Device B: 10.1.1.2 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 目的IP地址反掩码（ACLDESTWILD） | 0.0.0.0 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | VPN实例名称（VRFNAME） | vrf1 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | Proposal名称（PROPOSALNAME） | tran1 | 本端规划 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | IPsec安全协议（IPSECPROTOCOL） | Esp | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | ESP认证算法（ESPAUTHALGO） | Sha2_256 | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | ESP加密算法（ESPENCRYPTALGO） | Aes_256 | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | 封装模式（ENCAPMODE） | Tunnel | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 安全提议号（PROPOSALNUMBER） | 10 | 本端规划 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 认证方法（AUTHMETHOD） | Pre_share | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 认证算法（AUTHALGORITHM） | Sha2_256 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 加密算法（ENCRALGORITHM） | Aes_cbc_256 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 完整性算法（INTEGALGORITHM） | Hmac_sha2_256 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | DH组（DHGROUP） | Dh_group19 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 对等体名称（PEERNAME） | - Device A: b<br>- Device B: a | 对端规划 | 配置IKE对等体。<br>如果两个IPsec设备之间存在NAT设备，必须部署IPSec NAT穿越功能，将<br>“Nat穿越”<br>设置为<br>“TRUE”<br>。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 预共享密钥（PRESHAREDKEY） | abcde | 对端协商 | 配置IKE对等体。<br>如果两个IPsec设备之间存在NAT设备，必须部署IPSec NAT穿越功能，将<br>“Nat穿越”<br>设置为<br>“TRUE”<br>。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 安全提议（PROPOSAL） | 10 | 本端规划 | 配置IKE对等体。<br>如果两个IPsec设备之间存在NAT设备，必须部署IPSec NAT穿越功能，将<br>“Nat穿越”<br>设置为<br>“TRUE”<br>。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | Nat穿越（NATTRAVERSAL） | TRUE | 本端规划 | 配置IKE对等体。<br>如果两个IPsec设备之间存在NAT设备，必须部署IPSec NAT穿越功能，将<br>“Nat穿越”<br>设置为<br>“TRUE”<br>。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 远程地址（LOWREMOTEADDR） | - Device A: 192.168.1.2<br>- Device B: 192.168.1.1 | 全网规划 | 配置IKE对等体。<br>如果两个IPsec设备之间存在NAT设备，必须部署IPSec NAT穿越功能，将<br>“Nat穿越”<br>设置为<br>“TRUE”<br>。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | SA绑定VPN名称（INVRFNAME） | vrf1 | 本端规划 | 配置IKE对等体。<br>如果两个IPsec设备之间存在NAT设备，必须部署IPSec NAT穿越功能，将<br>“Nat穿越”<br>设置为<br>“TRUE”<br>。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 远程地址VPN名称（OUTVRFNAME） | vrf1 | 全网规划 | 配置IKE对等体。<br>如果两个IPsec设备之间存在NAT设备，必须部署IPSec NAT穿越功能，将<br>“Nat穿越”<br>设置为<br>“TRUE”<br>。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 策略名称（POLICYNAME） | map1 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 序列号（SEQUENCENUMBER） | 10 | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | ACL编号（ACLNUMBER） | 3000 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 策略名称（POLICYNAME） | map1 | 本端规划 | 在安全策略中引用安全提议。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 序列号（SEQUENCENUMBER） | 10 | 对端协商 | 在安全策略中引用安全提议。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | 在安全策略中引用安全提议。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | 在安全策略中引用安全提议。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | IPsec安全提议名称（IPSECPROPNAME） | tran1 | 本端规划 | 在安全策略中引用安全提议。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 策略名称（POLICYNAME） | map1 | 本端规划 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 序列号（SEQUENCENUMBER） | 10 | 对端协商 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | IKE对等体名称<br>（IKEPEERNAME） | - Device A: b<br>- Device B: a | 本端规划 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 优先级（PEERPRIORITY） | 1 | 本端规划 | 绑定安全策略和IKE对等体。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 接口名称（INTERFACENAME） | Tunnel10 | 本端规划 | 应用IPsec安全策略。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | Tunnel口协议类型（TNLTYPE） | IPSEC | 本端规划 | 应用IPsec安全策略。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 策略名称（POLICYNAME） | map1 | 本端规划 | 应用IPsec安全策略。 |
| [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md) | DPD类型（DPDTYPE） | Periodic | 本端规划 | 可选，如需开启DPD功能可配置该参数。 |
| [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md) | DPD检查间隔<br>（s）<br>（DPDINTERVAL） | 10 | 本端规划 | 可选，如需开启DPD功能可配置该参数。 |
| [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md) | DPD重试间隔<br>（s）<br>（DPDRETRYINTRVL） | 3 | 本端规划 | 可选，如需开启DPD功能可配置该参数。 |
| [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md) | NAT保活时间间隔 (s)（NATKLI） | 30 | 本端规划 | 可选，当通过<br>[**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md)<br>将<br>“Nat穿越（NATTRAVERSAL）”<br>配置为<br>“TRUE”<br>，即开启IPsec NAT穿越功能时，此参数生效。 |

## [操作流程](#ZH-CN_OPI_0161317238)

IPsec功能通过VNRS微服务和IPsec微服务实现：

-
  VNRS微服务：负责与外部网络通信，将需要保护的流量引到IPsec微服务做加解密，并将加解密后的流量转发出去。

  - 待加密的流量在VNRS微服务查找路由，当出接口是IPsec隧道接口时，根据VNRS微服务中的明文引流表和密文引流表，将报文送到IPsec微服务做加密处理。报文加密完后，IPsec微服务将报文返回给VNRS微服务，VNRS微服务将报文转发出去。
    - 当VNRS微服务收到IKE协商报文或者加密的AH/ESP报文，根据报文的源、目的地址，查找VNRS微服务中的明文引流表和密文引流表，将报文送到IPsec微服务进行解密或者协商。解密后的报文，IPsec微服务将报文返回给VNRS微服务，VNRS微服务将报文转发出去。
- IPsec微服务：负责IKE协商以及加解密。IPsec微服务采用IKE方式建立IPsec隧道需要配置好IKE协商安全策略的信息，由IKE自动协商来创建和维护安全联盟。

> **说明**
> - VNRS微服务和IPsec微服务需要遵循双配原则，即：IPsec协商用到的隧道接口、隧道接口IP、隧道类型、VPN以及指定本端接口建立IPsec隧道的接口需要在VNRS微服务和IPsec微服务上一对一的配置。若未遵循双配原则，会导致业务不通，配置过程中，请保证VNRS微服务和IPsec微服务的配置一致。如需删除隧道接口和VPN，也请同时删除VNRS微服务和IPsec微服务的相关数据。
> - 在建立IPsec隧道时，如果不指定本端其他接口，则默认使用本端隧道接口作为本端IKE协商IP地址。如果指定本端其他接口，则使用本端被指定的接口作为本端IKE协商IP地址。

IPsec功能配置流程如 [图2](#ZH-CN_OPI_0161317238__f7e7e6e513f4542b59be08973af61493a) 所示。

**图2** IPsec功能配置流程

<br>

![](激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.assets/zh-cn_image_0161317317.png)

## [操作步骤](#ZH-CN_OPI_0161317238)

1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    a. 创建VPN实例。
      [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
      [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
      [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
      [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    c. 创建IPsec隧道接口，并将IPsec隧道接口与VPN实例绑定。
      [**ADD INTERFACE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
      [**ADD IPSECINTFCFG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/创建IPsec隧道接口（ADD IPSECINTFCFG）_50281406.md)
      [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
      [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    d. 配置到达目的网络的静态路由，并与VPN实例绑定。
      [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
2. 创建IPsec微服务的VPN和IPsec隧道接口。
    a. 创建VPN实例。
      [**ADD L3VPNINSTIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例配置命令/增加L3VPN实例（ADD L3VPNINSTIPSEC）_25830689.md)
      [**ADD VPNINSTAFIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/VPN管理/L3VPN管理/VPN实例地址族配置命令/增加L3VPN实例地址族（ADD VPNINSTAFIPSEC）_26032191.md)
    b. 创建IPsec隧道接口，并将IPsec隧道接口与VPN实例绑定。
      [**ADD INTERFACEIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACEIPSEC）_26150749.md)
      [**ADD IPBINDVPNIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/绑定VPN/增加接口绑定VPN（ADD IPBINDVPNIPSEC）_80751060.md)
      [**ADD IFIPV4ADDRESSIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESSIPSEC）_80432522.md)
3. 定义需要保护的数据流。由用户根据ACL规则来定义，根据不同的数据流特征，定义不同的ACL规则。
  [**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)
  [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md)
  > **说明**
  > ACL只支持源IP和目的IP的配置，如果配置了端口，不会对端口配置生效。
4. 配置IPsec安全提议。
  [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md)
5. 配置IKE安全提议。
  [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md)
  > **说明**
  > - 缺省情况下的认证方法为预共享密钥认证（PSK），需要通过 [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) 配置 “预共享密钥（PRESHAREDKEY）” ，否则建立SA不成功。
  > - DHGROUP参数不能配置为 **None** 或者不配置，建议配置为 **Dh_group19** 。
6. 配置IKE对等体。
  [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md)
  > **说明**
  > - 当配置的认证方式为预共享密钥验证时，必须配置预共享密钥，预共享密钥的配置需要与对端设备相同。此处安全提议为IKE安全提议，IKE对等体被IPsec安全策略引用时，必须配置对端地址。对端地址不能配置为地址段。
  > - 设备同时开启IKEv1和IKEv2，缺省情况下采用IKEv2进行协商。若对端不支持IKEv2，请禁用IKEv2，采用IKEv1进行协商。
7. 配置IPsec安全策略。
    a. 增加IPsec安全策略
      [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md)
    b. 在安全策略中引用安全提议
      [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md)
    c. 绑定IKE对等体
      [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md)
8. 应用IPsec安全策略。
  [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md)
9. 配置DPD功能（可选）。
  [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)

## [任务示例](#ZH-CN_OPI_0161317238)

任务描述

按照 [图1](#ZH-CN_OPI_0161317238__f58130c7d29b9434a85c0152fb71100c7) 所示，配置IPsec隧道实现PCA与PCB之间可以安全地互访，并启用IPsec NAT穿越功能。

脚本

**Device A的配置脚本：**

//创建VNRS微服务的VPN实例。

```
ADD L3VPNINST:VRFNAME="vrf1";
```

```
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
```

//绑定VNRS微服务与VPN实例，并配置接口IP地址。

```
MOD INTERFACE:IFNAME="Ethernet66/0/5", IFADMINSTATUS=up;
```

```
MOD INTERFACE:IFNAME="Ethernet66/0/6", IFADMINSTATUS=up;
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/5", VRFNAME="vrf1";
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/6", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5", IFIPADDR="10.1.1.1", SUBNETMASK="255.255.255.0";
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/6", IFIPADDR="172.16.163.1", SUBNETMASK="255.255.255.0";
```

//创建VNRS微服务的IPsec隧道接口，绑定VPN并配置IP地址，隧道协议配置为IPSEC。

```
ADD INTERFACE:IFNAME="Tunnel10", IFADMINSTATUS=up;
```

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC;
```

```
ADD IPBINDVPN:IFNAME="Tunnel10", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel10", IFIPADDR="192.168.1.1", SUBNETMASK="255.255.255.255";
```

//配置到达目的网络B的静态路由并绑定VPN，到达网络B的出接口为“Tunnel10”下一跳地址为192.168.1.2。假设Device A的下一跳地址为172.16.169.2/24。

```
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";
```

```
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2",IFNAME="Invalid0";
```

//创建IPsec微服务的VPN实例。

```
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
```

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
```

//创建IPsec微服务的IPsec隧道接口，绑定VPN并配置IP地址。

```
ADD INTERFACEIPSEC:IFNAME="Tunnel10", IFADMINSTATUS=Up;
```

```
ADD IPBINDVPNIPSEC:IFNAME="Tunnel10", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="Tunnel10", IFIPADDR="192.168.1.1", SUBNETMASK="255.255.255.255";
```

//配置高级ACL 3000，允许PCA访问PCB。

```
ADD ACLGROUPIPSEC:ACLNAME ="3000";
```

```
ADD ACLRULEADV4IPSEC:ACLNAME="3000",ACLRULENAME="rule_1",ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=0,ACLSOURCEIP="10.1.1.2",ACLSRCWILD="0.0.0.0",ACLDESTIP="10.1.2.2",ACLDESTWILD="0.0.0.0";
```

> **说明**
> 上述 **ADD ACLRULEADV4IPSEC** 命令中 “ACLSRCWILD” 、 “ACLDESTWILD” 分别用于设置IPv4场景下源地址和目的地址反掩码，在反掩码中：二进制的0表示精确匹配，1表示任意，如0.0.0.0表示IP地址每一位需精确匹配。

//配置名称为tran1的IPsec安全提议。

```
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="tran1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;
```

//配置序号为10的IKE安全提议。

```
ADD IKEPROPOSAL:PROPOSALNUMBER=10,AUTHMETHOD=Pre_share, AUTHALGORITHM=Sha2_256,DHGROUP=Dh_group19;
```

> **说明**
> 此处 “PROPOSALNUMBER” 参数取值为 “10” 仅表示本端的一条配置记录，无实际含义，也无需与对端保持一致，该参数支持的配置范围为1~100，其中101为系统默认配置，仅支持查询。

//配置名称为b的IKE peer。

```
ADD IKEPEER:PEERNAME="b",PRESHAREDKEY="abcde",NATTRAVERSAL=TRUE,PROPOSAL=10,LOWREMOTEADDR="192.168.1.2",INVRFNAME="vrf1",OUTVRFNAME="vrf1";
```

//配置名称为map1、序号为10的IPsec安全策略。

```
ADD IPSECPOLICY:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3000;
```

//在安全策略中引用安全提议。

```
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="tran1";
```

//在安全策略中引用IKE Peer。

```
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="b",PEERPRIORITY=1;
```

//在IPsec隧道接口上应用安全策略map1。

```
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC,POLICYNAME="map1";
```

//配置DPD功能（可选）。

```
SET IKEGLOBALCONFIG:DPDINTERVAL=10,DPDTYPE=Periodic,DPDRETRYINTRVL=3,NATKLI=30;
```

**Device B的配置脚本：**

//创建VNRS微服务的VPN实例。

```
ADD L3VPNINST:VRFNAME="vrf1";
```

```
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
```

//绑定VNRS微服务与VPN实例，并配置接口IP地址。

```
MOD INTERFACE:IFNAME="Ethernet66/0/5", IFADMINSTATUS=up;
```

```
MOD INTERFACE:IFNAME="Ethernet66/0/6", IFADMINSTATUS=up;
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/5", VRFNAME="vrf1";
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/6", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5", IFIPADDR="10.1.2.1", SUBNETMASK="255.255.255.0";
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/6", IFIPADDR="172.16.169.1", SUBNETMASK="255.255.255.0";
```

//创建VNRS微服务的IPsec隧道接口，绑定VPN并配置IP地址，隧道协议配置为IPSEC。

```
ADD INTERFACE:IFNAME="Tunnel10", IFADMINSTATUS=up;
```

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC;
```

```
ADD IPBINDVPN:IFNAME="Tunnel10", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel10", IFIPADDR="192.168.1.2", SUBNETMASK="255.255.255.255";
```

//配置到达目的网络A的静态路由，到达网络A的出接口为Tunnel10下一跳地址为192.168.1.1。假设Device B的下一跳地址为172.16.163.2/24。

```
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel10";
```

```
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";
```

//创建IPsec微服务的VPN实例。

```
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
```

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
```

//创建IPsec微服务的IPsec隧道接口，绑定VPN并配置IP地址。

```
ADD INTERFACEIPSEC:IFNAME="Tunnel10", IFADMINSTATUS=Up;
```

```
ADD IPBINDVPNIPSEC:IFNAME="Tunnel10", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="Tunnel10", IFIPADDR="192.168.1.2", SUBNETMASK="255.255.255.255";
```

//配置高级ACL 3000，允许PCA访问PCB。

```
ADD ACLGROUPIPSEC:ACLNAME="3000";
```

```
ADD ACLRULEADV4IPSEC:ACLNAME="3000",ACLRULENAME="rule_1",ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=0,ACLSOURCEIP="10.1.2.2",ACLSRCWILD="0.0.0.0",ACLDESTIP="10.1.1.2",ACLDESTWILD="0.0.0.0";
```

> **说明**
> 上述 **ADD ACLRULEADV4IPSEC** 命令中 “ACLSRCWILD” 、 “ACLDESTWILD” 分别用于设置IPv4场景下源地址和目的地址反掩码，在反掩码中：二进制的0表示精确匹配，1表示任意，如0.0.0.0表示IP地址每一位需精确匹配。

//配置名称为tran1的IPsec安全提议。

```
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="tran1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;
```

//配置序号为10的IKE安全提议。

```
ADD IKEPROPOSAL:PROPOSALNUMBER=10,AUTHMETHOD=Pre_share, AUTHALGORITHM=Sha2_256,DHGROUP=Dh_group19;
```

> **说明**
> 此处 “PROPOSALNUMBER” 参数取值为 “10” 仅表示本端的一条配置记录，无实际含义，也无需与对端保持一致，该参数支持的配置范围为1~100，其中101为系统默认配置，仅支持查询。

//配置名称为a的IKE peer。

```
ADD IKEPEER:PEERNAME="a",PRESHAREDKEY="abcde",NATTRAVERSAL=TRUE,PROPOSAL=10,LOWREMOTEADDR="192.168.1.1",INVRFNAME="vrf1",OUTVRFNAME="vrf1";
```

//配置名称为map1、序号为10的IPsec安全策略。

```
ADD IPSECPOLICY:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3000;
```

//在安全策略中引用安全提议

```
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="tran1";
```

//在安全策略中引用IKE Peer

```
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="a",PEERPRIORITY=1;
```

//在Tunnel接口上应用安全策略map1。

```
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC,POLICYNAME="map1";
```

//配置DPD功能（可选）。

```
SET IKEGLOBALCONFIG:DPDINTERVAL=10,DPDTYPE=Periodic,DPDRETRYINTRVL=3,NATKLI=30;
```
