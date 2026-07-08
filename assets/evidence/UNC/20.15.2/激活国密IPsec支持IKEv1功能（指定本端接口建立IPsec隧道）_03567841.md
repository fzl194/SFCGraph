# 激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）

- [操作场景](#ZH-CN_OPI_0000001503567841__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0000001503567841__1.3.2)
- [必备事项](#ZH-CN_OPI_0000001503567841__1.3.3)
- [操作流程](#ZH-CN_OPI_0000001503567841__1.3.4)
- [操作步骤](#ZH-CN_OPI_0000001503567841__1.3.5)
- [任务示例](#ZH-CN_OPI_0000001503567841__1.3.6)

## [操作场景](#ZH-CN_OPI_0000001503567841)

指定本端Loopback口建立IPsec隧道作为本端IKE的协商地址，支持多个IPsec隧道指定同一个Loopback口，作为本端IKE的协商地址。

> **说明**
> 被指定的接口需要被IPsec隧道单独使用，如果被其他协议使用，则该协议不生效。

如 [图1](#ZH-CN_OPI_0000001503567841__f5c6cff363e0141d38dfdac8d18a96e45) 所示，网络A和网络B之间采用网关对网关组网模式进行资源传输。网络A和网络B分别通过Device A和Device B连接到Internet。要求通过指定本端接口配置IPsec隧道，实现PCA与PCB之间可以安全地互访。

**图1** 指定本端接口建立IPsec隧道组网图

> **说明**
> 本例中interface1和interface2分别代表Ethernet66/0/3和Ethernet66/0/5。

<br>

![](激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）_03567841.assets/zh-cn_image_0000001503728933_2.png)

网络环境描述如下，以IPv4网络为例：

- 网络A属于10.1.1.0/24子网Device A，通过接口interface2与 Device A 连接。
- 网络B属于10.1.2.0/24子网，通过接口interface2与 Device B 连接。
- Device A 和 Device B 路由可达。假设Device A往Device B方向下一跳地址为192.168.1.2/24，Device B往Device A方向下一跳地址为192.168.2.2/24。

*表1 设备接口IP地址（指定本端接口建立IPsec隧道）*

| 设备名称 | 接口 | IP地址 |
| --- | --- | --- |
| Device A VNRS微服务 | Ethernet66/0/3 | 192.168.1.1/24（IPsec报文的本端物理出接口） |
| Device A VNRS微服务 | Ethernet66/0/5 | 10.1.1.1/24 |
| Device A VNRS微服务 | LoopBack1 | 10.3.3.3/32（需要双配） |
| Device A VNRS微服务 | Tunnel2 | 10.2.2.1/32（需要双配） |
| Device B VNRS微服务 | Ethernet66/0/3 | 192.168.2.1/24（IPsec报文的本端物理出接口） |
| Device B VNRS微服务 | Ethernet66/0/5 | 10.1.2.1/24 |
| Device B VNRS微服务 | LoopBack1 | 10.3.4.3/32（需要双配） |
| Device B VNRS微服务 | Tunnel2 | 10.2.3.1/32（需要双配） |
| Device A IPsec微服务 | LoopBack1 | 10.3.3.3/32（被指定的本端接口地址，同时是本端的协商IP地址） |
| Device A IPsec微服务 | Tunnel2 | 10.2.2.1/32 |
| Device B IPsec微服务 | LoopBack1 | 10.3.4.3/32（被指定的本端接口地址，同时是本端的协商IP地址） |
| Device B IPsec微服务 | Tunnel2 | 10.2.3.1/32 |
| PCA | - | 10.1.1.2/24 |
| PCB | - | 10.1.2.2/24 |
| - | Device A侧网关接口 | 192.168.1.2/24 |
| - | Device B侧网关接口 | 192.168.2.2/24 |

## [对系统的影响](#ZH-CN_OPI_0000001503567841)

本特性对系统无影响。

## [必备事项](#ZH-CN_OPI_0000001503567841)

前提条件

- 操作人员已经登录网管。
- 配置接口的IP地址。
- 配置路由，使隧道两端路由可达。
- IPSec功能由IPSec服务承载，请完成IPSec安装，参见**软件安装**章节中的“安装可选服务 > 安装IPSec服务”。

数据

需要准备的数据如 [表2](#ZH-CN_OPI_0000001503567841__tab_1) 所示。

*表2 IPsec安全参数（指定本端接口建立IPsec隧道）*

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md) | ACL规则组标识（ACLNAME） | 3001 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md) | 规则组步长（ACLSTEP） | 5 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md) | 规则组类型（ACLTYPE） | Advance | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md) | 规则的匹配顺序（ACLMATCHORDER） | Config | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | ACL规则组标识（ACLNAME） | 3001 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 规则名称（ACLRULENAME） | rule_5 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 规则ID（ACLRULEID） | 5 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 规则行为（ACLACTION） | Permit | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 协议类型值（ACLPROTOCOL） | 0 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 源IP地址（ACLSOURCEIP） | 10.1.1.2 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 源IP地址反掩码（ACLSRCWILD） | 0.0.0.0 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 目的IP地址（ACLDESTIP） | 10.1.2.2 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | 目的IP地址反掩码（ACLDESTWILD） | 0.0.0.0 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md) | VPN实例名称（VRFNAME） | vrf1 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | Proposal名称（PROPOSALNAME） | Proposal1 | 本端规划 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | IPsec安全协议（IPSECPROTOCOL） | Esp | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | ESP认证算法（ESPAUTHALGO） | Sha2_256 | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | ESP加密算法（ESPENCRYPTALGO） | Aes_256 | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | AH认证算法（AHAUTHALGO） | Sha2_512 | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | 封装模式（ENCAPMODE） | Tunnel | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 安全提议号（PROPOSALNUMBER） | 1 | 本端规划 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 认证方法（AUTHMETHOD） | Digital_envelope | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 加密算法（ENCRALGORITHM） | Sm4 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 完整性算法（INTEGALGORITHM） | Sm3 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 重认证间隔<br>（s）<br>（REAUTHINTERVAL） | 86400 | 本端规划 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 非对称加密算法（ASYMENCRALG） | Sm2 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 对等体名称（PEERNAME） | 1 | 对端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 交换模式（EXCHANGEMODE） | Main | 对端协商 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 安全提议（PROPOSAL） | 1 | 本端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 本地ID类型（LOCALIDTYPE） | Ip | 本端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 远程地址（LOWREMOTEADDR） | 10.3.4.3 | 全网规划 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | SA绑定VPN名称（INVRFNAME） | vrf1 | 本端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 远程地址VPN名称（OUTVRFNAME） | vrf1 | 全网规划 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 版本1（VERSION1） | TRUE | 对端协商 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 版本2（VERSION2） | FALSE | 对端协商 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 签名证书文件名（CERTLOCALFILE） | - sm2_c_sig.cer<br>- sm2_s_sig.cer | 本端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md) | 加密证书文件名（ENCCERTLOCFILE） | - sm2_c_enc.cer<br>- sm2_s_enc.cer | 本端规划 | 配置IKE对等体。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 策略名称（POLICYNAME） | policy1 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 序列号（SEQUENCENUMBER） | 1 | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | ACL编号（ACLNUMBER） | 3001 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 去使能SA按流量计长（TRAFFSADISFLG） | FALSE | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | SA按流量计长（SALIFETIMEKB） | 1843200 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | SA按时计长（SALIFETIMESEC） | 3600 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | PFS（PFS） | None | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 选择DSCP入方向值（DSCPINSELECT） | None | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 选择DSCP出方向值（DSCPOUTSELECT） | None | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 抗重放（ANTIREPLAYENUM） | NotConfigured | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 清除分片标记（DFBITCLEAR） | FALSE | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 加密前分片报文（FRAGBEFOREENCR） | FALSE | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md) | 日志使能（LOGENABLE） | FALSE | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号（ACLNUMBER）”<br>；如果<br>[**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)<br>中的<br>“ACL规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称（ACLNAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 策略名称（POLICYNAME） | policy1 | 本端规划 | 在安全策略中引用安全提议。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 序列号（SEQUENCENUMBER） | 1 | 对端协商 | 在安全策略中引用安全提议。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | 在安全策略中引用安全提议。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | 在安全策略中引用安全提议。 |
| [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md) | IPsec安全提议名称（IPSECPROPNAME） | Proposal1 | 本端规划 | 在安全策略中引用安全提议。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 策略名称（POLICYNAME） | policy1 | 本端规划 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 序列号（SEQUENCENUMBER） | 1 | 对端协商 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | IKE对等体名称<br>（IKEPEERNAME） | 1 | 本端规划 | 绑定安全策略和IKE对等体。 |
| [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md) | 优先级（PEERPRIORITY） | 1 | 本端规划 | 绑定安全策略和IKE对等体。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 接口名称（INTERFACENAME） | Tunnel2 | 本端规划 | 应用IPsec安全策略。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | Tunnel口协议类型（TNLTYPE） | IPSEC | 本端规划 | 应用IPsec安全策略。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 策略名称（POLICYNAME） | map1 | 本端规划 | 应用IPsec安全策略。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 源接口名称（SRCIFNAME） | LoopBack1 | 本端规划 | 应用IPsec安全策略。 |

## [操作流程](#ZH-CN_OPI_0000001503567841)

IPsec功能通过VNRS微服务和IPsec微服务实现：

-
  VNRS微服务：负责与外部网络通信，将需要保护的流量引到IPsec微服务做加解密，并将加解密后的流量转发出去。

  - 待加密的流量在VNRS微服务查找路由，当出接口是IPsec隧道接口时，根据VNRS微服务中的明文引流表和密文引流表，将报文送到IPsec微服务做加密处理。报文加密完后，IPsec微服务将报文返回给VNRS微服务，VNRS微服务将报文转发出去。
    - 当VNRS微服务收到IKE协商报文或者加密的AH/ESP报文，根据报文的源、目的地址，查找VNRS微服务中的明文引流表和密文引流表，将报文送到IPsec微服务进行解密或者协商。解密后的报文，IPsec微服务将报文返回给VNRS微服务，VNRS微服务将报文转发出去。
- IPsec微服务：负责IKE协商以及加解密。IPsec微服务采用IKE方式建立IPsec隧道需要配置好IKE协商安全策略的信息，由IKE自动协商来创建和维护安全联盟。

> **说明**
> - VNRS微服务和IPsec微服务需要遵循双配原则，即：IPsec协商用到的隧道接口、隧道接口IP、隧道类型、VPN以及指定本端接口建立IPsec隧道的接口需要在VNRS微服务和IPsec微服务上一对一的配置。若未遵循双配原则，会导致业务不通，配置过程中，请保证VNRS微服务和IPsec微服务的配置一致。如需删除隧道接口和VPN，也请同时删除VNRS微服务和IPsec微服务的相关数据。
> - 在建立IPsec隧道时，如果不指定本端其他接口，则默认使用本端隧道接口作为本端IKE协商IP地址。如果指定本端其他接口，则使用本端被指定的接口作为本端IKE协商IP地址。

IPsec功能配置流程如 [图2](#ZH-CN_OPI_0000001503567841__zh-cn_opi_0161317238_f7e7e6e513f4542b59be08973af61493a) 所示。

**图2** IPsec功能配置流程

<br>

![](激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）_03567841.assets/zh-cn_image_0161317317_2.png)

## [操作步骤](#ZH-CN_OPI_0000001503567841)

1. 创建VNRS微服务的VPN和IPsec隧道接口、Loopback接口，并配置静态路由用于IPsec引流。
    a. 创建VPN实例。
      [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
      [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
      [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
      [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    c. 创建IPsec隧道接口和Loopback接口，并将其与VPN实例绑定。
      [**ADD INTERFACE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
      [**ADD IPSECINTFCFG**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/创建IPsec隧道接口（ADD IPSECINTFCFG）_50281406.md)
      [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
      [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    d. 配置静态有用于IPsec引流。
      [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
2. 创建IPsec微服务的VPN和IPsec隧道接口、Loopback接口。
    a. 创建VPN实例。
      [**ADD L3VPNINSTIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例配置命令/增加L3VPN实例（ADD L3VPNINSTIPSEC）_25830689.md)
      [**ADD VPNINSTAFIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/VPN管理/L3VPN管理/VPN实例地址族配置命令/增加L3VPN实例地址族（ADD VPNINSTAFIPSEC）_26032191.md)
    b. 创建IPsec隧道接口和Loopback接口，并将其与VPN实例绑定。
      [**ADD INTERFACEIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACEIPSEC）_26150749.md)
      [**ADD IPBINDVPNIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/绑定VPN/增加接口绑定VPN（ADD IPBINDVPNIPSEC）_80751060.md)
      [**ADD IFIPV4ADDRESSIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESSIPSEC）_80432522.md)
3. 定义需要保护的数据流。由用户根据ACL规则来定义，根据不同的数据流特征，定义不同的ACL规则。
  [**ADD ACLGROUPIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/ACL规则组/增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)
  [**ADD ACLRULEADV4IPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级ACL规则/增加高级ACL规则（ADD ACLRULEADV4IPSEC）_80751058.md)
  > **说明**
  > ACL只支持源IP和目的IP的配置，如果配置了端口，不会对端口配置生效。
4. 执行 [**SET FWSOFTPARA**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软参配置管理/设置ServiceFabric软参（SET FWSOFTPARA）_18818231.md) 命令，设置 **DWORD 1401** ，打开国密算法开关。
  ```
  SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;
  ```
5. 配置IPsec安全提议。
  [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md)
6. 配置IKE安全提议。
  [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md)
7. 配置IKE对等体。
  [**ADD IKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体/增加IKE对等体（ADD IKEPEER）_80592498.md)
8. 配置IPsec安全策略。
    a. 增加IPsec安全策略
      [**ADD IPSECPOLICY**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md)
    b. 在安全策略中引用安全提议
      [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md)
    c. 绑定IKE对等体
      [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md)
9. 应用IPsec安全策略。
  [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md)

## [任务示例](#ZH-CN_OPI_0000001503567841)

任务描述

按照 [图1](#ZH-CN_OPI_0000001503567841__f5c6cff363e0141d38dfdac8d18a96e45) 所示，配置IPsec隧道实现PCA与PCB之间可以安全地互访。

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
MOD INTERFACE:IFNAME="Ethernet66/0/3",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE,IFSTATIENABLE=TRUE,IFSTATITVL=20;
```

```
MOD INTERFACE:IFNAME="Ethernet66/0/5",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE,IFSTATIENABLE=TRUE,IFSTATITVL=20;
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/3", VRFNAME="vrf1";
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/5", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/3",IFIPADDR="192.168.1.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5",IFIPADDR="10.1.1.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;
```

//创建VNRS微服务的IPsec隧道接口和Loopback接口，绑定VPN并配置IP地址。

```
ADD INTERFACE:IFNAME="LoopBack1";
```

```
ADD IPBINDVPN:IFNAME="LoopBack1", VRFNAME="vrf1";
```

```
ADD INTERFACE:IFNAME="Tunnel2",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE,IFSTATITVL=20;
```

```
ADD IPBINDVPN:IFNAME="Tunnel2", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.3.3.3",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel2",IFIPADDR="10.2.2.1",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
```

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC;
```

//配置静态路由用于IPsec引流。

```
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,VRFNAME="vrf1",IFNAME="Tunnel2",NEXTHOP="10.3.4.3",PREFERENCE=60,BFDENABLE=FALSE;
```

```
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.3.4.3",MASKLENGTH=32,VRFNAME="vrf1",IFNAME="Ethernet66/0/3",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;
```

//创建IPsec微服务的VPN实例。

```
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
```

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
```

//创建IPsec微服务的IPsec隧道接口和Loopback接口，绑定VPN并配置IP地址。

```
ADD INTERFACEIPSEC:IFNAME="LoopBack1";
```

```
ADD IPBINDVPNIPSEC:IFNAME="LoopBack1", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="LoopBack1",IFIPADDR="10.3.3.3",SUBNETMASK="255.255.255.255",ADDRTYPE=Main;
```

```
ADD INTERFACEIPSEC:IFNAME="Tunnel2",IFADMINSTATUS=Up,IFMTU=1500,IFDF=FALSE,IFSTATITVL=20;
```

```
ADD IPBINDVPNIPSEC:IFNAME="Tunnel2", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="Tunnel2",IFIPADDR="10.2.2.1",SUBNETMASK="255.255.255.255",ADDRTYPE=Main;
```

//配置高级ACL 3001，允许PCA访问PCB。

```
ADD ACLGROUPIPSEC:ACLNAME="3001",ACLSTEP=5,ACLTYPE=Advance,ACLMATCHORDER=Config;
```

```
ADD ACLRULEADV4IPSEC:ACLNAME="3001",ACLRULENAME="rule_5",ACLRULEID=5,ACLACTION=Permit,VRFNAME="vrf1",ACLSOURCEIP="10.1.1.2",ACLSRCWILD="0.0.0.0",ACLPROTOCOL=0,ACLDESTIP="10.1.2.2",ACLDESTWILD="0.0.0.0";
```

//设置软参 **DWORD 1401** 为1，打开支持国密算法开关。

```
SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;
```

//配置名称为Proposal1的IPsec安全提议。

```
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="Proposal1",IPSECPROTOCOL=Esp,ESPAUTHALGO=Sha2_512,ESPENCRYPTALGO=Aes_256,ENCAPMODE=Tunnel;
```

//配置序号为1的IKE安全提议。

```
ADD IKEPROPOSAL:PROPOSALNUMBER=1,AUTHMETHOD=Digital_envelope,ENCRALGORITHM=Sm4,INTEGALGORITHM=Sm3,SADURATION=86400,ASYMENCRALG=Sm2;
```

//配置名称为1的IKE peer。

```
ADD IKEPEER:PEERNAME="1",EXCHANGEMODE=Main,PROPOSAL=1,LOCALIDTYPE=Ip,LOWREMOTEADDR="10.3.4.3",INVRFNAME="vrf1",OUTVRFNAME="vrf1",VERSION1=TRUE,VERSION2=FALSE,CERTLOCALFILE="sm2_c_sig.cer",ENCCERTLOCFILE="sm2_c_enc.cer";
```

//配置名称为policy1、序号为1的IPsec安全策略。

```
ADD IPSECPOLICY:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3001,TRAFFSADISFLG=FALSE,SALIFETIMEKB=1843200,SALIFETIMESEC=3600,PFS=None,DSCPINSELECT=None,DSCPOUTSELECT=None,ANTIREPLAYENUM=NotConfigured,DFBITCLEAR=FALSE,FRAGBEFOREENCR=FALSE,LOGENABLE=FALSE;
```

//在安全策略中引用安全提议。

```
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="Proposal1";
```

//在安全策略中引用IKE Peer。

```
ADD ATTACHIKEPEER:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="1",PEERPRIORITY=1;
```

//在IPsec隧道接口上应用安全策略policy1，指定本端接口LoopBack1。

```
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC,POLICYNAME="policy1",SRCIFNAME="LoopBack1";
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
MOD INTERFACE:IFNAME="Ethernet66/0/3",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE,IFSTATIENABLE=TRUE,IFSTATITVL=20;
```

```
MOD INTERFACE:IFNAME="Ethernet66/0/5",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE,IFSTATIENABLE=TRUE,IFSTATITVL=20;
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/3", VRFNAME="vrf1";
```

```
ADD IPBINDVPN:IFNAME="Ethernet66/0/5", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/3",IFIPADDR="192.168.2.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;
```

```
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5",IFIPADDR="10.1.2.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;
```

///创建VNRS微服务的IPsec隧道接口和Loopback接口，绑定VPN并配置IP地址。

```
ADD INTERFACE:IFNAME="LoopBack1";
```

```
ADD IPBINDVPN:IFNAME="LoopBack1", VRFNAME="vrf1";
```

```
ADD INTERFACE:IFNAME="Tunnel2",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE,IFSTATITVL=5;
```

```
ADD IPBINDVPN:IFNAME="Tunnel2", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.3.4.3",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel2",IFIPADDR="10.2.3.1",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
```

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC;
```

//创建IPsec微服务的VPN实例。

```
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
```

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
```

//创建IPsec微服务的IPsec隧道接口和Loopback接口，绑定VPN并配置IP地址。

```
ADD INTERFACEIPSEC:IFNAME="LoopBack1";
```

```
ADD IPBINDVPNIPSEC:IFNAME="LoopBack1", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="LoopBack1",IFIPADDR="10.3.4.3",SUBNETMASK="255.255.255.255",ADDRTYPE=Main;
```

```
ADD INTERFACEIPSEC:IFNAME="Tunnel2",IFADMINSTATUS=Up,IFMTU=1500,IFDF=FALSE,IFSTATITVL=5;
```

```
ADD IPBINDVPNIPSEC:IFNAME="Tunnel2", VRFNAME="vrf1";
```

```
ADD IFIPV4ADDRESSIPSEC:IFNAME="Tunnel2",IFIPADDR="10.2.3.1",SUBNETMASK="255.255.255.255",ADDRTYPE=Main;
```

//配置静态路由用于IPsec引流。

```
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,VRFNAME="vpn1",IFNAME="Tunnel2",NEXTHOP="10.3.3.3",PREFERENCE=60,BFDENABLE=FALSE;
```

```
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.3.3.3",MASKLENGTH=32,VRFNAME="vpn1",IFNAME="Ethernet66/0/3",NEXTHOP="192.168.1.2",PREFERENCE=60,BFDENABLE=FALSE;
```

//配置高级ACL 3001，允许PCA访问PCB。

```
ADD ACLGROUPIPSEC:ACLNAME="3001",ACLSTEP=5,ACLTYPE=Advance,ACLMATCHORDER=Config;
```

```
ADD ACLRULEADV4IPSEC:ACLNAME="3001",ACLRULENAME="rule_5",ACLRULEID=5,ACLACTION=Permit,VRFNAME="vrf1",ACLSOURCEIP="10.1.2.2",ACLSRCWILD="0.0.0.0",ACLPROTOCOL=0,ACLDESTIP="10.1.1.2",ACLDESTWILD="0.0.0.0";
```

//设置软参 **DWORD 1401** 为1，打开支持国密算法开关。

```
SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;
```

//配置名称为Proposal1的IPsec安全提议。

```
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="Proposal1",IPSECPROTOCOL=Esp,ESPENCRYPTALGO=Aes_256,ESPAUTHALGO=Sha2_512,ENCAPMODE=Tunnel;
```

//配置序号为1的IKE安全提议。

```
ADD IKEPROPOSAL:PROPOSALNUMBER=1,AUTHMETHOD=Digital_envelope,ENCRALGORITHM=Sm4,INTEGALGORITHM=Sm3,SADURATION=86400,ASYMENCRALG=Sm2;
```

//配置名称为1的IKE peer。

```
ADD IKEPEER:PEERNAME="1",EXCHANGEMODE=Main,PROPOSAL=1,LOCALIDTYPE=Ip,LOWREMOTEADDR="10.3.3.3",INVRFNAME="vrf1",OUTVRFNAME="vrf1",VERSION1=TRUE,VERSION2=FALSE,CERTLOCALFILE="sm2_s_sig.cer",ENCCERTLOCFILE="sm2_s_enc.cer";
```

//配置名称为policy1、序号为1的IPsec安全策略。

```
ADD IPSECPOLICY:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3001,TRAFFSADISFLG=FALSE,SALIFETIMEKB=1843200,SALIFETIMESEC=3600,PFS=None,DSCPINSELECT=None,DSCPOUTSELECT=None,ANTIREPLAYENUM=NotConfigured,DFBITCLEAR=FALSE,FRAGBEFOREENCR=FALSE,LOGENABLE=FALSE;
```

//在安全策略中引用安全提议。

```
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="Proposal1";
```

//在安全策略中引用IKE Peer。

```
ADD ATTACHIKEPEER:POLICYNAME="policy1",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="1",PEERPRIORITY=1;
```

//在IPsec隧道接口上应用安全策略policy1，指定本端接口LoopBack1。

```
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC,POLICYNAME="policy1",SRCIFNAME="LoopBack1";
```
