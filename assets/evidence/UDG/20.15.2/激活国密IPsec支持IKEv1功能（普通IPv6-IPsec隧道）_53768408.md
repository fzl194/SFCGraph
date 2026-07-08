# 激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）

- [操作场景](#ZH-CN_OPI_0000001453768408__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0000001453768408__1.3.2)
- [必备事项](#ZH-CN_OPI_0000001453768408__1.3.3)
- [操作流程](#ZH-CN_OPI_0000001453768408__1.3.4)
- [操作步骤](#ZH-CN_OPI_0000001453768408__1.3.5)
- [任务示例](#ZH-CN_OPI_0000001453768408__1.3.6)

## [操作场景](#ZH-CN_OPI_0000001453768408)

如 [图1](#ZH-CN_OPI_0000001453768408__fd790ab071e0540c788bd4c76b40a0cc1) 所示，网络A和网络B之间采用网关对网关组网模式进行资源传输。网络A和网络B分别通过Device A和Device B连接到Internet，要求通过配置IPsec隧道实现PCA与PCB之间可以安全地互访。

**图1** IPv6 IPsec组网图

<br>

![](激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）_53768408.assets/zh-cn_image_0000001748660798.png)

网络环境描述如下：

- 网络A属于2001:db8:1::/64子网，通过接口interface 2与 Device A 连接。
- 网络B属于2001:db8:4::/64子网，通过接口interface 2与 Device B 连接。
-
  Device A 和 Device B 路由可达。假设Device A往Device B方向下一跳地址为2001:db8:1:1:1::2/64，Device B往Device A方向下一跳地址为2001:db8:1:0:2::2/64。

  *表1 设备接口IP地址（普通IPv6 IPsec隧道）*

  | 设备名称 | 接口 | IP地址 |
  | --- | --- | --- |
  | Device A VNRS微服务 | Ethernet66/0/5 | 2001:db8:1::1/64 |
  | Device A VNRS微服务 | Ethernet66/0/6 | 2001:db8:1:1:1::1/64 |
  | Device A VNRS微服务 | Tunnel27 | 2001:db8:1::1:0:1（需要双配） |
  | Device B VNRS微服务 | Ethernet66/0/5 | 2001:db8:4::1/64 |
  | Device B VNRS微服务 | Ethernet66/0/6 | 2001:db8:1:0:2::1/64 |
  | Device B VNRS微服务 | Tunnel27 | 2001:db8:4::1:0:1（需要双配） |
  | Device A IPsec微服务 | Tunnel27 | 2001:db8:1::1:0:1（IKE协商IP地址） |
  | Device B IPsec微服务 | Tunnel27 | 2001:db8:4::1:0:1（IKE协商IP地址） |
  | PCA | - | 2001:db8:1::2/64 |
  | PCB | - | 2001:db8:4::2/64 |
  | - | Device A侧网关接口 | 2001:db8:1:1:1::2/64 |
  | - | Device B侧网关接口 | 2001:db8:1:0:2::2/64 |

## [对系统的影响](#ZH-CN_OPI_0000001453768408)

本特性对系统无影响。

## [必备事项](#ZH-CN_OPI_0000001453768408)

前提条件

- 操作人员已经登录网管。
- 配置接口的IP地址。
- 配置路由，使隧道两端路由可达。
- IPSec功能由IPSec服务承载，请完成IPSec安装，参见**软件安装**章节中的“安装可选服务 > 安装IPSec服务”。

数据

需要准备的IPsec安全数据如 [表2](#ZH-CN_OPI_0000001453768408__table6941749153719) 所示。

*表2 IPsec安全参数（普通IPv6 IPsec隧道）*

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md) | ACL规则组标识（ACLNAME） | 3027 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 高级ACL规则组标识（ACLNAME） | 3027 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 规则名称（ACLRULENAME） | - rule27_1<br>- rule27_2 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 规则行为（ACLACTION） | Permit | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 协议类型值（ACLPROTOCOL） | 0 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 源IPv6地址（ACLSOURCEIP） | - Device A:- rule27_1：2001:db8:1::2<br>- rule27_2：2001:db8:4::2<br>- Device B:- rule 27_1：2001:db8:4::2<br>- rule27_2：2001:db8:1::2 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 源IPv6地址正掩码（ACLSRCWILD） | 128 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 目的IPv6地址（ACLDESTIP） | - Device A:- rule27_1：2001:db8:4::2<br>- rule27_2：2001:db8:1::2<br>- Device B:- rule27_1：2001:db8:1::2<br>- rule27_2：2001:db8:4::2 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 目的IPv6地址正掩码（ACLDESTWILD） | 128 | 全网规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | 协议选项类型（ACLPROTOCOLTYPE） | Number | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md) | VPN实例名称（VRFNAME） | vrf1 | 本端规划 | 通过ACL规则定义需要保护的数据流。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | Proposal名称（PROPOSALNAME） | tran1 | 本端规划 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | IPsec安全协议（IPSECPROTOCOL） | Esp | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | ESP认证算法（ESPAUTHALGO） | Sha2_256 | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | ESP加密算法（ESPENCRYPTALGO） | Aes_256 | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md) | 封装模式（ENCAPMODE） | Tunnel | 对端协商 | 配置IPsec安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 安全提议号（PROPOSALNUMBER） | 10 | 本端规划 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 认证方法（AUTHMETHOD） | Digital_envelope | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 加密算法（ENCRALGORITHM） | Sm4 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 完整性算法（INTEGALGORITHM） | Sm3 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md) | 非对称加密算法（ASYMENCRALG） | Sm2 | 对端协商 | 配置IKE安全提议。 |
| [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md) | 对等体名称（PEERNAME） | - Device A: b<br>- Device B: a | 对端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md) | 安全提议（PROPOSAL） | 10 | 本端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md) | 远程地址（LOWREMOTEADDR） | - Device A: 2001:db8:4::1:0:1<br>- Device B: 2001:db8:1::1:0:1 | 全网规划 | 配置IKE对等体。 |
| [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md) | SA绑定VPN名称（INVRFNAME） | vrf1 | 本端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md) | 远程地址VPN名称（OUTVRFNAME） | vrf1 | 全网规划 | 配置IKE对等体。 |
| [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md) | 版本2（VERSION2） | FALSE | 对端协商 | 配置IKE对等体。 |
| [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md) | 签名证书文件名（CERTLOCALFILE） | - sm2_c_sig.cer<br>- sm2_s_sig.cer | 本端规划 | 配置IKE对等体。 |
| [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md) | 加密证书文件名（ENCCERTLOCFILE） | - sm2_c_enc.cer<br>- sm2_s_enc.cer | 本端规划 | 配置IKE对等体。 |
| [**ADD IPSECPOLICY6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md) | 策略名称（POLICYNAME） | map1 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号-IPV6（ACL6NUMBER）”<br>；如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称-ipv6（ACL6NAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md) | 序列号（SEQUENCENUMBER） | 10 | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号-IPV6（ACL6NUMBER）”<br>；如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称-ipv6（ACL6NAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md) | 策略模式（POLICYMODE） | Isakmp | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号-IPV6（ACL6NUMBER）”<br>；如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称-ipv6（ACL6NAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md) | 模板模式（TEMPLATEMODE） | None | 对端协商 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号-IPV6（ACL6NUMBER）”<br>；如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称-ipv6（ACL6NAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md) | ACL类型（ACLTYPE） | AclIPv6 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号-IPV6（ACL6NUMBER）”<br>；如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称-ipv6（ACL6NAME）”<br>。此处以ACL规则组编号为例。 |
| [**ADD IPSECPOLICY6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md) | ACL编号-IPV6（ACL6NUMBER） | 3027 | 本端规划 | 配置IPsec安全策略。<br>如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组编号，则IPsec策略中使用<br>“ACL编号-IPV6（ACL6NUMBER）”<br>；如果<br>[**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)<br>中的<br>“规则组标识（ACLNAME）”<br>配置为规则组名称，则IPsec策略中使用<br>“ACL名称-ipv6（ACL6NAME）”<br>。此处以ACL规则组编号为例。 |
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
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 接口名称（INTERFACENAME） | Tunnel27 | 本端规划 | 应用IPsec安全策略。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | Tunnel口协议类型（TNLTYPE） | IPSEC6 | 本端规划 | 应用IPsec安全策略。 |
| [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md) | 策略名称（POLICYNAME） | map1 | 本端规划 | 应用IPsec安全策略。 |

## [操作流程](#ZH-CN_OPI_0000001453768408)

IPsec功能通过VNRS微服务和IPsec微服务实现：

-
  VNRS微服务：负责与外部网络通信，将需要保护的流量引到IPsec微服务做加解密，并将加解密后的流量转发出去。

  - 待加密的流量在VNRS微服务查找路由，当出接口是IPsec隧道接口时，根据VNRS微服务中的明文引流表和密文引流表，将报文送到IPsec微服务做加密处理。报文加密完后，IPsec微服务将报文返回给VNRS微服务，VNRS微服务将报文转发出去。
    - 当VNRS微服务收到IKE协商报文或者加密的AH/ESP报文，根据报文的源、目的地址，查找VNRS微服务中的明文引流表和密文引流表，将报文送到IPsec微服务进行解密或者协商。解密后的报文，IPsec微服务将报文返回给VNRS微服务，VNRS微服务将报文转发出去。
- IPsec微服务：负责IKE协商以及加解密。IPsec微服务采用IKE方式建立IPsec隧道需要配置好IKE协商安全策略的信息，由IKE自动协商来创建和维护安全联盟。

> **说明**
> - VNRS微服务和IPsec微服务需要遵循双配原则，即：IPsec协商用到的隧道接口、隧道接口IP、隧道类型、VPN以及指定本端接口建立IPsec隧道的接口需要在VNRS微服务和IPsec微服务上一对一的配置。若未遵循双配原则，会导致业务不通，配置过程中，请保证VNRS微服务和IPsec微服务的配置一致。如需删除隧道接口和VPN，也请同时删除VNRS微服务和IPsec微服务的相关数据。
> - 在建立IPsec隧道时，如果不指定本端其他接口，则默认使用本端隧道接口作为本端IKE协商IP地址。如果指定本端其他接口，则使用本端被指定的接口作为本端IKE协商IP地址。

IPsec功能配置流程如 [图2](#ZH-CN_OPI_0000001453768408__zh-cn_opi_0161317238_f7e7e6e513f4542b59be08973af61493a) 所示。

**图2** IPsec功能配置流程

<br>

![](激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）_53768408.assets/zh-cn_image_0161317317.png)

## [操作步骤](#ZH-CN_OPI_0000001453768408)

1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    a. 创建VPN实例。
      [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
      [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
      [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
      [**SET IFIPV6ENABLE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6使能/修改接口IPv6使能（SET IFIPV6ENABLE）_00601329.md)
      [**ADD IFIPV6ADDRESS**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESS）_49961222.md)
    c. 创建IPsec隧道接口，并将IPsec隧道接口与VPN实例绑定。
      [**ADD INTERFACE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
      [**SET IFIPV6ENABLE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6使能/修改接口IPv6使能（SET IFIPV6ENABLE）_00601329.md)
      [**ADD IFIPV6ADDRESS**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESS）_49961222.md)
      [**ADD IPSECINTFCFG**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/创建IPsec隧道接口（ADD IPSECINTFCFG）_50281406.md)
      [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
    d. 配置到达目的网络的静态路由，并与VPN实例绑定。
      [**ADD SRROUTE6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv6静态路由/增加IPv6静态路由（ADD SRROUTE6）_50280922.md)
2. 创建IPsec微服务的VPN和IPsec隧道接口。
    a. 创建VPN实例。
      [**ADD L3VPNINSTIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例配置命令/增加L3VPN实例（ADD L3VPNINSTIPSEC）_25830689.md)
      [**ADD VPNINSTAFIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/VPN管理/L3VPN管理/VPN实例地址族配置命令/增加L3VPN实例地址族（ADD VPNINSTAFIPSEC）_26032191.md)
    b. 创建IPsec隧道接口，并将IPsec隧道接口与VPN实例绑定。
      [**ADD INTERFACEIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACEIPSEC）_26150749.md)
      [**ADD IPBINDVPNIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/绑定VPN/增加接口绑定VPN（ADD IPBINDVPNIPSEC）_80751060.md)
      [**SET IFIPV6ENABLEIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/IPv6使能/设置接口IPv6使能（SET IFIPV6ENABLEIPSEC）_68201005.md)
      [**ADD IFIPV6ADDRESSIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESSIPSEC）_21521206.md)
3. 定义需要保护的数据流。由用户根据ACL规则来定义，根据不同的数据流特征，定义不同的ACL规则。
  [**ADD ACLGROUP6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/IPv6 ACL规则组/增加IPv6 ACL规则组（ADD ACLGROUP6IPSEC）_21521202.md)
  [**ADD ACLRULEADV6IPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/ACL管理/高级IPv6 ACL规则/增加高级IPv6 ACL规则（ADD ACLRULEADV6IPSEC）_68200943.md)
  > **说明**
  > ACL只支持源IP和目的IP的配置，如果配置了端口，不会对端口配置生效。
4. 执行 [**SET FWSOFTPARA**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/软参配置管理/设置ServiceFabric软参（SET FWSOFTPARA）_18818231.md) 命令，设置 **DWORD 1401** ，打开国密算法开关。
  ```
  SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;
  ```
5. 配置IPsec安全提议。
  [**ADD IPSECPROPOSALIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/IPsec/IPsec提议/增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.md)
6. 配置IKE安全提议。
  [**ADD IKEPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE安全提议/增加IKE提议（ADD IKEPROPOSAL）_26032189.md)
7. 配置IKE对等体。
  [**ADD IKEPEER6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE对等体IPv6/增加IPv6 IKE对等体（ADD IKEPEER6）_21361306.md)
8. 配置IPsec安全策略。
    a. 增加IPsec安全策略
      [**ADD IPSECPOLICY6**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md)
    b. 在安全策略中引用安全提议
      [**ADD PROPATTACHIPSECPROPOSAL**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IPsec安全提议/增加IPsec策略绑定提议（ADD PROPATTACHIPSECPROPOSAL）_80592500.md)
    c. 绑定IKE对等体
      [**ADD ATTACHIKEPEER**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/绑定的IKE对等体/增加绑定IKE对等体（ADD ATTACHIKEPEER）_80910984.md)
9. 应用IPsec安全策略。
  [**ADD IPSECINTFCFGIPSEC**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md)

## [任务示例](#ZH-CN_OPI_0000001453768408)

任务描述

按照 [图1](#ZH-CN_OPI_0000001453768408__fd790ab071e0540c788bd4c76b40a0cc1) 所示，配置IPsec隧道实现PCA与PCB之间可以安全地互访。

脚本

**Device A的配置脚本：**

//创建VNRS微服务的VPN实例。

```
ADD L3VPNINST:VRFNAME="vrf1";
```

```
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
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
SET IFIPV6ENABLE:IFNAME="Ethernet66/0/5", ENABLEFLAG=TRUE;
```

```
SET IFIPV6ENABLE:IFNAME="Ethernet66/0/6", ENABLEFLAG=TRUE;
```

```
ADD IFIPV6ADDRESS:IFNAME="Ethernet66/0/5", IPV6ADDRESS="2001:db8:1::1", PREFIXLEN=96;
```

```
ADD IFIPV6ADDRESS:IFNAME="Ethernet66/0/6", IPV6ADDRESS="2001:db8:1:1:1::1", PREFIXLEN=96;
```

//创建VNRS微服务的IPsec隧道接口，绑定VPN并配置IP地址，隧道协议配置为IPSEC。

```
ADD INTERFACE:IFNAME="Tunnel27", IFADMINSTATUS=up;
```

```
SET IFIPV6ENABLE:IFNAME="Tunnel27", ENABLEFLAG=TRUE;
```

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel27",TNLTYPE=IPSEC6;
```

```
ADD IPBINDVPN:IFNAME="Tunnel27", VRFNAME="vrf1";
```

```
ADD IFIPV6ADDRESS:IFNAME="Tunnel27", IPV6ADDRESS="2001:db8:1::1:0:1", PREFIXLEN=96;
```

//配置到达目的网络B的静态路由并绑定VPN，到达网络B的出接口为“Tunnel27”下一跳地址为2001:db8:4::1:0:1。假设Device A的下一跳地址为2001:db8:1:1:1::2。

```
ADD SRROUTE6:VRFNAME="vrf1",AFTYPE=ipv6unicast,PREFIX="2001:db8:4::2",MASKLENGTH=128,DESTVRFNAME="vrf1",NEXTHOP="2001:db8:4::1:0:1",IFNAME="Tunnel27";
```

```
ADD SRROUTE6:VRFNAME="vrf1",AFTYPE=ipv6unicast,PREFIX="2001:db8:4::1:0:1",MASKLENGTH=128,DESTVRFNAME="vrf1",NEXTHOP="2001:db8:1:1:1::2";
```

//创建IPsec微服务的VPN实例。

```
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
```

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv6uni;
```

//创建IPsec微服务的IPsec隧道接口，绑定VPN并配置IP地址。

```
ADD INTERFACEIPSEC:IFNAME="Tunnel27", IFADMINSTATUS=Up;
```

```
SET IFIPV6ENABLEIPSEC:IFNAME="Tunnel27", ENABLEFLAG=TRUE;
```

```
ADD IPBINDVPNIPSEC:IFNAME="Tunnel27", VRFNAME="vrf1";
```

```
ADD IFIPV6ADDRESSIPSEC:IFNAME="Tunnel27", IFIP6ADDR="2001:db8:1::1:0:1", ADDRPREFIXLEN=96;
```

//配置高级ACL 3027，允许PCA访问PCB。

```
ADD ACLGROUP6IPSEC:ACLNAME ="3027";
```

```
ADD ACLRULEADV6IPSEC:ACLNAME="3027",ACLRULENAME="rule27_1",ACLACTION=Permit,VRFNAME="vrf1",ACLSOURCEIP="2001:db8:1::2",ACLSRCWILD=128,ACLDESTIP="2001:db8:4::2",ACLDESTWILD=128,ACLPROTOCOLTYPE=Number,ACLPROTOCOL=0;
```

```
ADD ACLRULEADV6IPSEC:ACLNAME="3027",ACLRULENAME="rule27_2",ACLACTION=Permit,VRFNAME="vrf1",ACLSOURCEIP="2001:db8:4::2",ACLSRCWILD=128,ACLDESTIP="2001:db8:1::2",ACLDESTWILD=128,ACLPROTOCOLTYPE=Number,ACLPROTOCOL=0;
```

> **说明**
> 上述 **ADD ACLRULEADV6IPSEC** 命令中 “ACLSRCWILD” 、 “ACLDESTWILD” 分别用于设置IPv6场景下源地址和目的地址正掩码，正掩码取值“128”表示精确匹配，取值 “0” 表示任意。

//设置软参 **DWORD 1401** 为1，打开支持国密算法开关。

```
SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;
```

//配置名称为tran1的IPsec安全提议。

```
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="tran1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;
```

//配置序号为10的IKE安全提议。

```
ADD IKEPROPOSAL:PROPOSALNUMBER=10,AUTHMETHOD=Digital_envelope,ENCRALGORITHM=Sm4,INTEGALGORITHM=Sm3,ASYMENCRALG=Sm2;
```

> **说明**
> 此处 “PROPOSALNUMBER” 参数取值为 “10” 仅表示本端的一条配置记录，无实际含义，也无需与对端保持一致，该参数支持的配置范围为1~100，其中101为系统默认配置，仅支持查询。

//配置名称为b的IKE peer。

```
ADD IKEPEER6:PEERNAME="b",PROPOSAL=10,LOWREMOTEADDR="2001:db8:4::1:0:1",INVRFNAME="vrf1",OUTVRFNAME="vrf1",VERSION2=FALSE,CERTLOCALFILE="sm2_c_sig.cer",ENCCERTLOCFILE="sm2_c_enc.cer";
```

//配置名称为map1、序号为10的IPsec安全策略。

```
ADD IPSECPOLICY6:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLTYPE=AclIPv6,ACL6NUMBER=3027;
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
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel27",TNLTYPE=IPSEC6,POLICYNAME="map1";
```

**Device B的配置脚本：**

//创建VNRS微服务的VPN实例。

```
ADD L3VPNINST:VRFNAME="vrf1";
```

```
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
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
SET IFIPV6ENABLE:IFNAME="Ethernet66/0/5", ENABLEFLAG=TRUE;
```

```
SET IFIPV6ENABLE:IFNAME="Ethernet66/0/6", ENABLEFLAG=TRUE;
```

```
ADD IFIPV6ADDRESS:IFNAME="Ethernet66/0/5", IPV6ADDRESS="2001:db8:4::1", PREFIXLEN=96;
```

```
ADD IFIPV6ADDRESS:IFNAME="Ethernet66/0/6", IPV6ADDRESS="2001:db8:1:0:2::1", PREFIXLEN=96;
```

//创建VNRS微服务的IPsec隧道接口，绑定VPN并配置IP地址，隧道协议配置为IPSEC。

```
ADD INTERFACE:IFNAME="Tunnel27", IFADMINSTATUS=up;
```

```
SET IFIPV6ENABLE:IFNAME="Tunnel27", ENABLEFLAG=TRUE;
```

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel27",TNLTYPE=IPSEC6;
```

```
ADD IPBINDVPN:IFNAME="Tunnel27", VRFNAME="vrf1";
```

```
ADD IFIPV6ADDRESS:IFNAME="Tunnel27", IPV6ADDRESS="2001:db8:4::1:0:1", PREFIXLEN=96;
```

//配置到达目的网络A的静态路由，到达网络A的出接口为Tunnel27下一跳地址为2001:db8:1::1:0:1。假设Device B的下一跳地址为2001:db8:1:0:2::2/24。

```
ADD SRROUTE6:VRFNAME="vrf1",AFTYPE=ipv6unicast,PREFIX="2001:db8:1::2",MASKLENGTH=128,DESTVRFNAME="vrf1",NEXTHOP="2001:db8:1::1:0:1",IFNAME="Tunnel27";
```

```
ADD SRROUTE6:VRFNAME="vrf1",AFTYPE=ipv6unicast,PREFIX="2001:db8:1::1:0:1",MASKLENGTH=128,DESTVRFNAME="vrf1",NEXTHOP="2001:db8:1:0:2::2";
```

//创建IPsec微服务的VPN实例。

```
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
```

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv6uni;
```

//创建IPsec微服务的IPsec隧道接口，绑定VPN并配置IP地址。

```
ADD INTERFACEIPSEC:IFNAME="Tunnel27", IFADMINSTATUS=Up;
```

```
SET IFIPV6ENABLEIPSEC:IFNAME="Tunnel27", ENABLEFLAG=TRUE;
```

```
ADD IPBINDVPNIPSEC:IFNAME="Tunnel27", VRFNAME="vrf1";
```

```
ADD IFIPV6ADDRESSIPSEC:IFNAME="Tunnel27", IFIP6ADDR="2001:db8:4::1:0:1", ADDRPREFIXLEN=96;
```

//配置高级ACL 3027，允许PCA访问PCB。

```
ADD ACLGROUP6IPSEC:ACLNAME="3027";
```

```
ADD ACLRULEADV6IPSEC:ACLNAME="3027",ACLRULENAME="rule27_1",ACLACTION=Permit,VRFNAME="vrf1",ACLSOURCEIP="2001:db8:4::2",ACLSRCWILD=128,ACLDESTIP="2001:db8:1::2",ACLDESTWILD=128,ACLPROTOCOLTYPE=Number,ACLPROTOCOL=0;
```

```
ADD ACLRULEADV6IPSEC:ACLNAME="3027",ACLRULENAME="rule27_2",ACLACTION=Permit,VRFNAME="vrf1",ACLSOURCEIP="2001:db8:1::2",ACLSRCWILD=128,ACLDESTIP="2001:db8:4::2",ACLDESTWILD=128,ACLPROTOCOLTYPE=Number,ACLPROTOCOL=0;
```

> **说明**
> 上述 **ADD ACLRULEADV6IPSEC** 命令中 “ACLSRCWILD” 、 “ACLDESTWILD” 分别用于设置IPv6场景下源地址和目的地址正掩码，正掩码取值“128”表示精确匹配，取值 “0” 表示任意。

//设置软参 **DWORD 1401** 为1，打开支持国密算法开关。

```
SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;
```

//配置名称为tran1的IPsec安全提议。

```
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="tran1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;
```

//配置序号为10的IKE安全提议。

```
ADD IKEPROPOSAL:PROPOSALNUMBER=10,AUTHMETHOD=Digital_envelope,ENCRALGORITHM=Sm4,INTEGALGORITHM=Sm3,ASYMENCRALG=Sm2;
```

> **说明**
> 此处 “PROPOSALNUMBER” 参数取值为 “10” 仅表示本端的一条配置记录，无实际含义，也无需与对端保持一致，该参数支持的配置范围为1~100，其中101为系统默认配置，仅支持查询。

//配置名称为a的IKE peer。

```
ADD IKEPEER6:PEERNAME="a",PROPOSAL=10,LOWREMOTEADDR="2001:db8:1::1:0:1",INVRFNAME="vrf1",OUTVRFNAME="vrf1",VERSION2=FALSE,CERTLOCALFILE="sm2_s_sig.cer",ENCCERTLOCFILE="sm2_s_enc.cer";
```

//配置名称为map1、序号为10的IPsec安全策略。

```
ADD IPSECPOLICY6:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLTYPE=AclIPv6,ACL6NUMBER=3027;
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
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel27",TNLTYPE=IPSEC6,POLICYNAME="map1";
```
