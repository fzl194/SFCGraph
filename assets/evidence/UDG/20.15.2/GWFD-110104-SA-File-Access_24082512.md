# GWFD-110104 SA-File Access

- [适用NF](#ZH-CN_CONCEPT_0124082512__1.4.1.1)
- [定义](#ZH-CN_CONCEPT_0124082512__1.4.2.1)
- [客户价值](#ZH-CN_CONCEPT_0124082512__1.4.3.1)
- [应用场景](#ZH-CN_CONCEPT_0124082512__1.4.4.1)
- [可获得性](#ZH-CN_CONCEPT_0124082512__1.4.5.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0124082512__1.4.6.1)
- [对系统的影响](#ZH-CN_CONCEPT_0124082512__1.4.7.1)
- [应用限制](#ZH-CN_CONCEPT_0124082512__1.4.8.1)
- [原理概述](#ZH-CN_CONCEPT_0124082512__1.4.9.1)
- [计费与话单](#ZH-CN_CONCEPT_0124082512__1.4.10.1)
- [特性规格](#ZH-CN_CONCEPT_0124082512__1.4.11.1)
- [遵循标准](#ZH-CN_CONCEPT_0124082512__1.4.12.1)
- [发布历史](#ZH-CN_CONCEPT_0124082512__1.4.13.1)

#### [适用NF](#ZH-CN_CONCEPT_0124082512)

SGW-U、PGW-U、UPF

#### [定义](#ZH-CN_CONCEPT_0124082512)

SA-File Access是指 UDG 支持对File Access报文进行业务感知，判断访问内容，感知业务，对不同业务进行不同的计费和动作处理。

#### [客户价值](#ZH-CN_CONCEPT_0124082512)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 限制文件传输的带宽，避免文件传输业务占用大量带宽；也可以对文件传输提供较大带宽，提升用户感受。 |
| 用户 | 用户不感知该特性。 |

#### [应用场景](#ZH-CN_CONCEPT_0124082512)

限制文件传输的带宽，避免文件传输业务占用大量带宽；也可以对文件传输提供较大带宽，提升用户感受。

#### [可获得性](#ZH-CN_CONCEPT_0124082512)

**涉及NF**

| 涉及<br>**NF** | 支持版本 | 功能说明 |
| --- | --- | --- |
| SGW-U/PGW-U/UPF | UDG 20.0.0及后续版本 | 用于对报文进行识别和解析，根据解析结果匹配规则，对不同业务进行不同的计费和动作处理。 |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82209756 LKV3G5SAFA01 SA-File Access”。

该License项控制的协议组包括的协议可以通过 **[LST DFTPROTGRP](../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/协议组/查询默认协议组（LST DFTPROTGRP）_82837345.md)** 命令查询。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0124082512)

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
| --- | --- | --- | --- |
| 依赖 | [GWFD-110101 SA-Basic](GWFD-110101 SA-Basic_24082506.md) | 82209749 SA-Basic | SA-Basic是SA的基本功能，必须开启。 |

#### [对系统的影响](#ZH-CN_CONCEPT_0124082512)

当在 UDG 上开启SA-File Access特性后， 由于匹配到规则的用户业务流的所有报文都需要进行报文的业务感知，因此系统处理负荷将增加，报文转发性能和吞吐量将下降。

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

#### [应用限制](#ZH-CN_CONCEPT_0124082512)

SA-File Access特性依赖于File Access协议识别，File Access协议的应用类型非常多，而且不断有新的应用类型出现和更新，所以需要定期更新SA识别特征库以支持新的File Access协议类型的识别。

#### [原理概述](#ZH-CN_CONCEPT_0124082512)

**File Access 文件访问类协议特征**

该类协议的主要特征为通过特定软件或应用工具对服务器的文件进行访问或下载。例如： FTP（File Transfer Protocol）、TFTP（Trivial File Transfer Protocol） 。

FTP是一种TCP/IP协议。该协议使得文件可以通过网络从一台计算机传送到另一台计算机。在FTP传输中，两台计算机必须支持它们各自的FTP角色：一台必须是FTP客户端，另一台是FTP服务器。

TFTP是文件传输协议FTP的另一种小型简单协议形式。TFTP协议用于客户端和服务器之间不需要复杂交互的应用上，它把业务限制在简单的文件传输上，不需要进行验证。TFTP协议很小，可以存储在ROM上，用于引导没有硬盘的设备。

SA-File Access支持解析的子协议类型个数，由加载的协议特征库决定。

**系统实现**

三四层解析、协议识别和业务流程的详细描述请参见 [GWFD-110101 SA-Basic](GWFD-110101 SA-Basic_24082506.md) 。

**七层解析**

如果 UDG 识别出报文协议为FTP\TFTP后，按照FTP\TFTP标准协议对报文进行解析，解析出报文中Method和Filename字段。然后进行七层规则匹配，对报文实施不同的计费和控制策略。如 [表1](#ZH-CN_CONCEPT_0124082512__tab11) 所示。

*表1 FTP七层解析*

| 协议 | 上下行 | 关键信息 | 说明 |
| --- | --- | --- | --- |
| FTP | UP | Method：port、pasv、retr、stor、cwd、cdup；client-port；File-name(including path) | 解析Method、协商客户端的端口、文件名。其他method的报文无需继续处理。 |
| FTP | DOWN | Method；server-port；File-name(including path) | 解析Method、协商的服务器端口、文件名。以上信息解析完整即无需继续解析。 |
| TFTP | UP | Method；File name | 解析Method、文件名信息。 |
| TFTP | DOWN | Method；ErrorCode | 解析Method和ErrorCode。 |

#### [计费与话单](#ZH-CN_CONCEPT_0124082512)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_CONCEPT_0124082512)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_CONCEPT_0124082512)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF | 959 | File Transfer Protocol (FTP) |
| IETF | 1350 | The TFTP Protocol (Revision 2) |

#### [发布历史](#ZH-CN_CONCEPT_0124082512)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
