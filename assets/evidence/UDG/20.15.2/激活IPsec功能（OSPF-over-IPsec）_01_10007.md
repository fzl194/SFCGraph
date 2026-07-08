# 激活IPsec功能（OSPF over IPsec）

- [操作场景](#ZH-CN_OPI_0000002090949389__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0000002090949389__1.3.2)
- [必备事项](#ZH-CN_OPI_0000002090949389__1.3.3)
- [操作流程](#ZH-CN_OPI_0000002090949389__1.3.4)
- [操作步骤](#ZH-CN_OPI_0000002090949389__1.3.5)
- [任务示例](#ZH-CN_OPI_0000002090949389__1.3.6)

## [操作场景](#ZH-CN_OPI_0000002090949389)

如 [图1 OSPF over IPsec组网图](#ZH-CN_OPI_0000002090949389__fdd852f6d2ca6440a935e9670b2e2477b) 所示，网络A和网络B之间采用网关对网关组网模式进行资源传输。网络A和网络B分别通过Device A和Device B连接到Internet，要求通过配置IPsec隧道实现PCA与PCB之间可以安全地互访，OSPF协议还能在网络拓扑结构发生变化后实现路由的快速收敛。

该网络需实现以下需求：

- **路由协议的安全性：**OSPF over IPsec结合了OSPF和IPsec，为OSPF邻居之间的通信提供了额外的安全层。这确保了OSPF控制消息和路由信息的安全传输。
- **加密和认证：**IPsec用于对OSPF邻居之间的通信进行加密和认证，确保OSPF更新、邻居关系建立等消息的机密性和完整性。
- **完整性保护：**通过IPsec提供的完整性验证，防止OSPF消息在传输过程中被篡改，确保OSPF数据的准确性。
- **支持动态的路由协议：**OSPF是一种支持动态路由的协议，它可以适应网络的拓扑结构变化，提供灵活而可伸缩的路由。
- **适用于中大型网络：**OSPF over IPsec适用于中大型网络，为其提供了安全的动态路由，同时防范了潜在的安全威胁。

**图1** OSPF over IPsec组网图

<br>

![](激活IPsec功能（OSPF over IPsec）_01_10007.assets/zh-cn_image_0000002078526402.png)

网络环境描述如下，以IPv4网络为例：

- 网络A属于10.1.1.0/24子网，通过接口interface2与 Device A 连接。
- 网络B属于10.1.2.0/24子网，通过接口interface2与 Device B 连接。
- Device A 和 Device B 路由可达。假设Device A往Device B方向下一跳地址为192.168.1.2/24，Device B往Device A方向下一跳地址为192.168.2.2/24。

*表1 设备接口IP地址（OSPF over IPsec）*

| 设备名称 | 接口 | IP地址 |
| --- | --- | --- |
| Device A VNRS微服务 | Ethernet66/0/5 | 192.168.1.1/24（IPsec报文的本端物理出接口） |
| Device A VNRS微服务 | Ethernet66/0/6 | 10.1.1.1/24 |
| Device A VNRS微服务 | Tunnel2 | 10.102.101.25/32（需要双配） |
| Device A VNRS微服务 | LoopBack1 | 10.102.105.238/32（OSPF的loopback口） |
| Device B VNRS微服务 | Ethernet66/0/5 | 192.168.2.1/24（IPsec报文的本端物理出接口） |
| Device B VNRS微服务 | Ethernet66/0/6 | 10.1.2.1/24 |
| Device B VNRS微服务 | Tunnel2 | 10.102.101.21/32（需要双配） |
| Device B VNRS微服务 | LoopBack1 | 10.102.105.224/32（OSPF的loopback口） |
| Device A IPsec微服务 | Tunnel2 | 10.102.101.25/32 |
| Device B IPsec微服务 | Tunnel2 | 10.102.101.21/32 |
| Device A IPsec微服务 | LoopBack1 | 10.102.105.238/32 |
| Device B IPsec微服务 | LoopBack1 | 10.102.105.238/32 |
| PCA | - | 10.1.1.2/24 |
| PCB | - | 10.1.2.2/24 |
| - | Device A侧网关接口 | 192.168.1.2/24 |
| - | Device B侧网关接口 | 192.168.2.2/24 |

## [对系统的影响](#ZH-CN_OPI_0000002090949389)

本特性对系统无影响。

## [必备事项](#ZH-CN_OPI_0000002090949389)

前提条件

- 操作人员已经登录网管。
- 配置接口的IP地址。
- 配置路由，使隧道两端路由可达。
- IPSec功能由IPSec服务承载，请完成IPSec安装，参见**软件安装**章节中的“安装可选服务 > 安装IPSec服务”。

数据

需要准备的数据如 [表 IPsec安全参数（OSPF over IPsec）](#ZH-CN_OPI_0000002090949389__table97132238418) 所示。

*表2 IPsec安全参数（OSPF over IPsec）*

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md) | ACL规则组标识（ACLNAME） | 3001 | 本端规划 | - |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | ACL规则组标识（ACLNAME） | 3001 | 本端规划 | - |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 规则名称（ACLRULENAME） | - rule_1<br>- rule_2 | 本端规划 | - |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 规则行为（ACLACTION） | Permit | 本端规划 | - |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 协议类型值（ACLPROTOCOL） | - 0<br>- 89 | 本端规划 | 取值为0表示IP协议，取值为89表示OSPF协议。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | VPN实例名称（VRFNAME） | vrf1 | 本端规划 | - |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | Proposal名称（PROPOSALNAME） | 1 | 本端规划 | - |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | IPsec安全协议（IPSECPROTOCOL） | Esp | 对端协商 | - |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | ESP认证算法（ESPAUTHALGO） | Sha2_256 | 对端协商 | - |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | ESP加密算法（ESPENCRYPTALGO） | Aes_256 | 对端协商 | - |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | 封装模式（ENCAPMODE） | Tunnel | 对端协商 | - |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 安全提议号（PROPOSALNUMBER） | 1 | 本端规划 | - |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 认证方法（AUTHMETHOD） | Pre_share | 对端协商 | - |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 认证算法（AUTHALGORITHM） | Sha2_256 | 对端协商 | - |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 加密算法（ENCRALGORITHM） | Aes_cbc_256 | 对端协商 | - |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 完整性算法（INTEGALGORITHM） | Hmac_sha2_256 | 对端协商 | - |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | DH组（DHGROUP） | Dh_group19 | 对端协商 | - |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | SA持续长度（s）（SADURATION） | 3600 | 本端规划 | - |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 对等体名称（PEERNAME） | - Device A: b<br>- Device B: a | 对端规划 | - |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 预共享密钥（PRESHAREDKEY） | abcde | 对端协商 | - |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 交换模式（EXCHANGEMODE） | Main | 对端协商 | - |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 安全提议（PROPOSAL） | 1 | 本端规划 | - |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 本地ID类型（LOCALIDTYPE） | Ip | 本端规划 | - |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 远程地址（LOWREMOTEADDR） | - Device A: 10.102.105.224<br>- Device B: 10.102.105.238 | 全网规划 | 远程地址为loopback口地址。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | SA绑定VPN名称（INVRFNAME） | vrf1 | 本端规划 | - |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 远程地址VPN名称（OUTVRFNAME） | vrf1 | 全网规划 | - |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 策略名称（POLICYNAME） | policy1 | 本端规划 | - |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 序列号（SEQUENCENUMBER） | 1 | 对端协商 | - |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | - |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | - |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | ACL编号（ACLNUMBER） | 3001 | 本端规划 | 如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 策略名称（POLICYNAME） | policy1 | 本端规划 | - |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 序列号（SEQUENCENUMBER） | 1 | 对端协商 | - |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | - |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | - |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | IPsec安全提议名称（IPSECPROPNAME） | 1 | 本端规划 | - |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 策略名称（POLICYNAME） | policy1 | 本端规划 | - |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 序列号（SEQUENCENUMBER） | 1 | 对端协商 | - |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | - |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | - |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | IKE对等体名称<br>（IKEPEERNAME） | - Device A: b<br>- Device B: a | 本端规划 | - |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 优先级（PEERPRIORITY） | 1 | 本端规划 | - |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 接口名称（INTERFACENAME） | Tunnel2 | 本端规划 | - |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | Tunnel口协议类型（TNLTYPE） | IPSEC | 本端规划 | - |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 策略名称（POLICYNAME） | policy1 | 本端规划 | - |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 源接口名称（SRCIFNAME） | loopback1 | 本端规划 | 源接口设置为loopback口。 |
| [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md) | DPD类型（DPDTYPE） | Periodic | 本端规划 | 如需开启DPD功能，可配置该参数。 |
| [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md) | DPD检查间隔<br>（s）<br>（DPDINTERVAL） | 10 | 本端规划 | 如需开启DPD功能，可配置该参数。 |
| [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md) | DPD重试间隔<br>（s）<br>（DPDRETRYINTRVL） | 3 | 本端规划 | 如需开启DPD功能，可配置该参数。 |
| **[ADD OSPF](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md)** | 进程号（PROCID） | 20214 | 本端规划 | - |
| **[ADD OSPF](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md)** | VPN名称（VRFNAME） | vrf1 | 本端规划 | - |
| **[ADD OSPF](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md)** | 路由器标识（SCHEMAROUID） | - Device A: 10.102.105.238<br>- Device B: 10.102.105.224 | 本端规划 | - |
| **[ADD OSPFAREA](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域配置/创建OSPF区域配置（ADD OSPFAREA）_50120650.md)** | 进程号（PROCID） | 20214 | 本端规划 | - |
| **[ADD OSPFAREA](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域配置/创建OSPF区域配置（ADD OSPFAREA）_50120650.md)** | AREAID（区域号） | 10.102.105.0 | 对端协商 | - |
| **[ADD OSPFNETWORK](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md)** | 进程号（PROCID） | 20214 | 本端规划 | - |
| **[ADD OSPFNETWORK](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md)** | AREAID（区域号） | 10.102.105.0 | 对端协商 | - |
| **[ADD OSPFNETWORK](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md)** | IP地址（IPADDRESS） | 10.102.105.0 | 全网规划 | - |
| **[ADD OSPFNETWORK](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md)** | 反掩码（WILDCARDMASK） | 0.0.0.255 | 全网规划 | - |
| **[ADD OSPFIMPORTROUTE](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/引入外部路由配置/创建OSPF引入路由配置（ADD OSPFIMPORTROUTE）_00601057.md)** | 进程号（PROCID） | 20214 | 本端规划 | - |
| **[ADD OSPFIMPORTROUTE](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/引入外部路由配置/创建OSPF引入路由配置（ADD OSPFIMPORTROUTE）_00601057.md)** | 协议分类（PROTOCOL） | Direct | 本端规划 | - |

## [操作流程](#ZH-CN_OPI_0000002090949389)

IPsec功能通过VNRS微服务和IPsec微服务实现：

-
  VNRS微服务：负责与外部网络通信，将需要保护的流量引到IPsec微服务做加解密，并将加解密后的流量转发出去。

  - 待加密的流量在VNRS微服务查找路由，当出接口是IPsec隧道接口时，根据VNRS微服务中的明文引流表和密文引流表，将报文送到IPsec微服务做加密处理。报文加密完后，IPsec微服务将报文返回给VNRS微服务，VNRS微服务将报文转发出去。
    - 当VNRS微服务收到IKE协商报文或者加密的AH/ESP报文，根据报文的源、目的地址，查找VNRS微服务中的明文引流表和密文引流表，将报文送到IPsec微服务进行解密或者协商。解密后的报文，IPsec微服务将报文返回给VNRS微服务，VNRS微服务将报文转发出去。
- IPsec微服务：负责IKE协商以及加解密。IPsec微服务采用IKE方式建立IPsec隧道需要配置好IKE协商安全策略的信息，由IKE自动协商来创建和维护安全联盟。

> **说明**
> - VNRS微服务和IPsec微服务需要遵循双配原则，即：IPsec协商用到的隧道接口、隧道接口IP、隧道类型、VPN以及指定本端接口建立IPsec隧道的接口需要在VNRS微服务和IPsec微服务上一对一的配置。若未遵循双配原则，会导致业务不通，配置过程中，请保证VNRS微服务和IPsec微服务的配置一致。如需删除隧道接口和VPN，也请同时删除VNRS微服务和IPsec微服务的相关数据。
> - 在建立IPsec隧道时，如果不指定本端其他接口，则默认使用本端隧道接口作为本端IKE协商IP地址。如果指定本端其他接口，则使用本端被指定的接口作为本端IKE协商IP地址。

IPsec功能配置流程如 [图2](#ZH-CN_OPI_0000002090949389__zh-cn_opi_0161317238_f7e7e6e513f4542b59be08973af61493a) 所示。

**图2** IPsec功能配置流程

<br>

![](激活IPsec功能（OSPF over IPsec）_01_10007.assets/zh-cn_image_0161317317.png)

## [操作步骤](#ZH-CN_OPI_0000002090949389)

1. 创建VNRS微服务的VPN、IPsec隧道接口和OSPF的loopback口。
    a. 创建VPN实例。
      [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
      [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    b. 创建OSPF的loopback口。
      [**ADD INTERFACE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
    c. 将VNRS微服务的接口及OSPF的loopback口与VPN实例绑定并配置接口IP地址。
      [**MOD INTERFACE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/修改接口（MOD INTERFACE）_50281674.md)
      [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
      [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    d. 创建IPsec隧道接口，并将IPsec隧道接口与VPN实例绑定。
      [**ADD INTERFACE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
      [**ADD IPSECINTFCFG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/创建IPsec隧道接口（ADD IPSECINTFCFG）_50281406.md)
      [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
      [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
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
10. 配置静态路由用于IPsec引流。
  [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
11. 在VNRS上配置OSPF。
  **[ADD OSPF](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md)**
  **[ADD OSPFAREA](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域配置/创建OSPF区域配置（ADD OSPFAREA）_50120650.md)**
  **[ADD OSPFNETWORK](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md)**
  **[ADD OSPFIMPORTROUTE](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/引入外部路由配置/创建OSPF引入路由配置（ADD OSPFIMPORTROUTE）_00601057.md)**

## [任务示例](#ZH-CN_OPI_0000002090949389)

任务描述

按照 [图1](#ZH-CN_OPI_0000002090949389__fdd852f6d2ca6440a935e9670b2e2477b) 所示，配置IPsec隧道实现PCA与PCB之间可以安全地互访。

脚本

**Device A的配置脚本：**

//创建VNRS微服务的VPN实例。

```
ADD L3VPNINST:VRFNAME="vrf1";
```

```
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
```

//创建OSPF的loopback口，将VNRS微服务的接口及OSPF的loopback口与VPN实例绑定并配置接口IP地址。

```
ADD INTERFACE:IFNAME="LoopBack1",IFADMINSTATUS=up,IFMTU=1500;
```

```
MOD INTERFACE:IFNAME="Ethernet66/0/5", IFADMINSTATUS=up, IFMTU=1500;
```

```
MOD INTERFACE:IFNAME="Ethernet66/0/6", IFADMINSTATUS=up, IFMTU=1500;
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/5", VRFNAME="vrf1";
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/6", VRFNAME="vrf1";
```

```
ADD IPBINDVPN:IFNAME="LoopBack1", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.102.105.238",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5",IFIPADDR="192.168.1.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/6",IFIPADDR="10.1.1.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;
```

//创建VNRS微服务的IPsec隧道接口，绑定VPN并配置IP地址，隧道协议配置为IPSEC。

```
ADD INTERFACE:IFNAME="Tunnel2",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE;
```

```
ADD IPBINDVPN:IFNAME="Tunnel2", VRFNAME="vrf1";
```

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC;
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel2",IFIPADDR="10.102.101.25",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
```

//创建IPsec微服务的VPN实例。

```
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
```

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
```

//创建IPsec微服务的IPsec隧道接口和OSPF接口，并绑定VPN并配置IP地址。

```
ADD INTERFACEIPSEC:IFNAME="Tunnel2",IFADMINSTATUS=Up,IFMTU=1500,IFDF=FALSE;
```

```
ADD INTERFACEIPSEC:IFNAME="LoopBack1",IFADMINSTATUS=Up,IFMTU=1500,IFDF=FALSE;
```

```
ADD IPBINDVPNIPSEC:IFNAME="Tunnel2", VRFNAME="vrf1";
```

```
ADD IPBINDVPNIPSEC:IFNAME="LoopBack1", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="Tunnel2",IFIPADDR="10.102.101.25",SUBNETMASK="255.255.255.255",ADDRTYPE=Main;
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="LoopBack1",IFIPADDR="10.102.105.238",SUBNETMASK="255.255.255.255",ADDRTYPE=Main;
```

//配置高级ACL 3001，允许PCA访问PCB。

```
ADD ACLGROUPIPSEC:ACLNAME="3001";
```

```
ADD ACLRULEADV4IPSEC:ACLNAME="3001",ACLRULENAME="rule_1",ACLRULEID=1,ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=0;
```

```
ADD ACLRULEADV4IPSEC:ACLNAME="3001",ACLRULENAME="rule_2",ACLRULEID=1,ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=89;
```

> **说明**
> 配置高级ACL时，不配置源IP地址和目的IP地址，此外协议类型不光要配置IP协议（参数“ACLPROTOCOL”取值为“0”）还要配置OSPF协议（参数“ACLPROTOCOL”取值为“89”）。

//配置名称为1的IPsec安全提议。

```
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;
```

//配置序号为1的IKE安全提议。

```
ADD IKEPROPOSAL:PROPOSALNUMBER=1,AUTHMETHOD=Pre_share,AUTHALGORITHM=Sha2_256,ENCRALGORITHM=Aes_cbc_256,INTEGALGORITHM=Hmac_sha2_256,DHGROUP=Dh_group19,SADURATION=3600;
```

//配置名称为b的IKE peer。

```
ADD IKEPEER:PEERNAME="b",PRESHAREDKEY="abcde",EXCHANGEMODE=Main,PROPOSAL=1,LOCALIDTYPE=Ip,LOWREMOTEADDR="10.102.105.224",INVRFNAME="vrf1",OUTVRFNAME="vrf1";
```

> **说明**
> 配置IKE对等体时，远程地址（LOWREMOTEADDR）需要配置为对端loopback口的IP地址。

//配置名称为policy1、序号为1的IPsec安全策略。

```
ADD IPSECPOLICY:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3001;
```

//在安全策略中引用安全提议。

```
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="1";
```

//在安全策略中引用IKE Peer。

```
ADD ATTACHIKEPEER:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="b",PEERPRIORITY=1;
```

//在IPsec隧道接口上应用安全策略policy1。

```
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC,POLICYNAME="policy1",SRCIFNAME="loopback1";
```

> **说明**
> 在IPsec隧道接口上应用安全策略时，源接口名称（SRCIFNAME）需要配置为loopback口名称。

//配置DPD功能（可选）。

```
SET IKEGLOBALCONFIG:DPDINTERVAL=10,DPDTYPE=Periodic,DPDRETRYINTRVL=3,NATKLI=30;
```

//配置静态路由用于IPsec引流。

```
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.224",MASKLENGTH=32,NEXTHOP="192.168.2.1",PREFERENCE=60,BFDENABLE=FALSE;
```

> **说明**
> 配置静态路由用于IPsec引流时，路由下一跳（NEXTHOP）需要配置为外联口IP地址。

//在VNRS上配置OSPF。

```
ADD OSPF: PROCID=20214, VRFNAME="vrf1", SCHEMAROUID="10.102.105.238";
```

```
ADD OSPFAREA:PROCID=20214, AREAID="10.102.105.0";
```

```
ADD OSPFNETWORK:PROCID=20214, AREAID="10.102.105.0", IPADDRESS="10.102.105.0", WILDCARDMASK="0.0.0.255";
```

```
ADD OSPFIMPORTROUTE: PROCID=20214, PROTOCOL=Direct;
```

**Device B的配置脚本：**

//创建VNRS微服务的VPN实例。

```
ADD L3VPNINST:VRFNAME="vrf1";
```

```
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
```

//创建OSPF的loopback口，将VNRS微服务的接口及OSPF的loopback口与VPN实例绑定并配置接口IP地址。

```
ADD INTERFACE:IFNAME="LoopBack1",IFADMINSTATUS=up,IFMTU=1500;
```

```
MOD INTERFACE:IFNAME="Ethernet66/0/5", IFADMINSTATUS=up, IFMTU=1500;
```

```
MOD INTERFACE:IFNAME="Ethernet66/0/6", IFADMINSTATUS=up, IFMTU=1500;
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/5", VRFNAME="vrf1";
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/6", VRFNAME="vrf1";
```

```
ADD IPBINDVPN:IFNAME="LoopBack1", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.102.105.224",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5",IFIPADDR="192.168.2.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/6",IFIPADDR="10.1.2.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;
```

//创建VNRS微服务的IPsec隧道接口，绑定VPN并配置IP地址，隧道协议配置为IPSEC。

```
ADD INTERFACE:IFNAME="Tunnel2",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE;
```

```
ADD IPBINDVPN:IFNAME="Tunnel2", VRFNAME="vrf1";
```

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC;
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel2",IFIPADDR="10.102.101.21",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
```

//创建IPsec微服务的VPN实例。

```
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
```

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
```

//创建IPsec微服务的IPsec隧道接口和OSPF接口，并绑定VPN并配置IP地址。

```
ADD INTERFACEIPSEC:IFNAME="Tunnel2",IFADMINSTATUS=Up,IFMTU=1500,IFDF=FALSE;
```

```
ADD INTERFACEIPSEC:IFNAME="LoopBack1",IFADMINSTATUS=Up,IFMTU=1500,IFDF=FALSE;
```

```
ADD IPBINDVPNIPSEC:IFNAME="Tunnel2", VRFNAME="vrf1";
```

```
ADD IPBINDVPNIPSEC:IFNAME="LoopBack1", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="Tunnel2",IFIPADDR="10.102.101.21",SUBNETMASK="255.255.255.255",ADDRTYPE=Main;
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="LoopBack1",IFIPADDR="10.102.105.224",SUBNETMASK="255.255.255.255",ADDRTYPE=Main;
```

//配置高级ACL 3001，允许PCA访问PCB。

```
ADD ACLGROUPIPSEC:ACLNAME="3001";
```

```
ADD ACLRULEADV4IPSEC:ACLNAME="3001",ACLRULENAME="rule_1",ACLRULEID=1,ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=0;
```

```
ADD ACLRULEADV4IPSEC:ACLNAME="3001",ACLRULENAME="rule_2",ACLRULEID=1,ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=89;
```

> **说明**
> 配置高级ACL时，不配置源IP地址和目的IP地址，此外协议类型不光要配置IP协议（参数“ACLPROTOCOL”取值为“0”）还要配置OSPF协议（参数“ACLPROTOCOL”取值为“89”）。

//配置名称为1的IPsec安全提议。

```
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;
```

//配置序号为1的IKE安全提议。

```
ADD IKEPROPOSAL:PROPOSALNUMBER=1,AUTHMETHOD=Pre_share,AUTHALGORITHM=Sha2_256,ENCRALGORITHM=Aes_cbc_256,INTEGALGORITHM=Hmac_sha2_256,DHGROUP=Dh_group19,SADURATION=3600;
```

//配置名称为a的IKE peer。

```
ADD IKEPEER:PEERNAME="a",PRESHAREDKEY="abcde",EXCHANGEMODE=Main,PROPOSAL=1,LOCALIDTYPE=Ip,LOWREMOTEADDR="10.102.105.238",INVRFNAME="vrf1",OUTVRFNAME="vrf1";
```

> **说明**
> 配置IKE对等体时，远程地址（LOWREMOTEADDR）需要配置为对端loopback口的IP地址。

//配置名称为policy1、序号为1的IPsec安全策略。

```
ADD IPSECPOLICY:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3001;
```

//在安全策略中引用安全提议。

```
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="1";
```

//在安全策略中引用IKE Peer。

```
ADD ATTACHIKEPEER:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="a",PEERPRIORITY=1;
```

//在IPsec隧道接口上应用安全策略policy1。

```
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC,POLICYNAME="policy1",SRCIFNAME="loopback1";
```

> **说明**
> 在IPsec隧道接口上应用安全策略时，源接口名称（SRCIFNAME）需要配置为loopback口名称。

//配置DPD功能（可选）。

```
SET IKEGLOBALCONFIG:DPDINTERVAL=10,DPDTYPE=Periodic,DPDRETRYINTRVL=3,NATKLI=30;
```

//配置静态路由用于IPsec引流。

```
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.238",MASKLENGTH=32,NEXTHOP="192.168.1.1",PREFERENCE=60,BFDENABLE=FALSE;
```

> **说明**
> 配置静态路由用于IPsec引流时，路由下一跳（NEXTHOP）需要配置为外联口IP地址。

//在VNRS上配置OSPF。

```
ADD OSPF: PROCID=20214, VRFNAME="vrf1", SCHEMAROUID="10.102.105.224";
```

```
ADD OSPFAREA:PROCID=20214, AREAID="10.102.105.0";
```

```
ADD OSPFNETWORK:PROCID=20214, AREAID="10.102.105.0", IPADDRESS="10.102.105.0", WILDCARDMASK="0.0.0.255";
```

```
ADD OSPFIMPORTROUTE: PROCID=20214, PROTOCOL=Direct;
```
