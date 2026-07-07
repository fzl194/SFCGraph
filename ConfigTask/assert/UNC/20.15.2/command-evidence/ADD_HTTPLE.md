# 命令证据包：ADD HTTPLE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：该命令用于增加HTTP本端实体。HTTP是Hyper Text Transfer Protocol协议的缩写，是一个基于TCP/IP通讯协议来传递数据的传输协议，工作于客户端-服务端架构上。NF实例既可能是客户端形态也可能是服务端形态，可通过本命令配置该协议的本端地址、端口号并指定为客户端还是服务端。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 客户端和服务端相同IP地址时，服务端端口号不能在[24576,32767]范围内。
- 本端实体类型配置为客户端时，同一个IP地址只能配置一条记录。如果没有配置“TLSIDX”，而实际建立的是HTTPs链路，则使用系统缺省TLS参数创建链路。如果配置了“TLSIDX”，而实际建立的是HTTP链路，则“TLSIDX”不生效。
- 本端实体类型配置为服务端时，同一个I

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| INDEX | HTTPLE本端实体索引 | local_planned | required | 无 | 整数类型，取值范围是1~128。 |
| HTTPLEGRPIDX | HTTP本端实体组标识 | local_planned | required | 无 | 整数类型，取值范围是1~64。 |
| LETYPE | 本端实体类型 | global_planned | required | 无 | <br>- “SERVER（服务端）”：服务端 |
| PORT | 端口号 | global_planned | conditional | 无 | 整数类型，取值范围是1~65535。 |
| TLSFLG | 是否启用TLS | global_planned | conditional | YES | <br>- “NO（NO）”：否 |
| TLSIDX | TLS索引 | global_planned | conditional | 无 | 整数类型，取值范围是1~128。 |
| IPTYPE | IP类型 | global_planned | required | 无 | <br>- “IPv4（IPv4地址）”：IPv4地址 |
| IPV4 | IPv4地址 | global_planned | conditional | 无 | IPv4地址类型。 |
| IPV6 | IPv6地址 | global_planned | conditional | 无 | IPv6地址类型。 |
| VPNNAME | VPN名称 | local_planned | optional | 无 | 字符串类型，输入长度范围是0~31。 |
| DESC | 描述 | local_planned | optional | 无 | 字符串类型，输入长度范围是0~255。 |
| RFLAG | 路由标记 | local_planned | optional | 无 | <br>- TRUE(TRUE) |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010308

**md：`WSFD-010308/WSFD-010308 SBI接口加密参考信息_70185217.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**删除本端地址组(RMV HTTPLEGRP)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/删除HTTP本端实体组（RMV HTTPLEGRP）_83813640.md)
    > - [**查询本端地址组(LST HTTPLEGRP)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/查询HTTP本端实体组（LST HTTPLEGRP）_83653658.md)
    > - [**增加HTTP本端实体(ADD HTTPLE)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    > - [**删除HTTP本端实体(RMV HTTPLE)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/删除HTTP本端实体（RMV HTTPLE）_28971847.md)
    > - [**修改HTTP本端实体(MOD HTTPLE)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/修改HTTP本端实体（MOD HTTPLE）_28971845.md)

**md：`WSFD-010308/激活SBI接口加密特性(CERT)_70185215.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | HTTPLE本端实体索引 | 服务端：1<br>客户端：2 | 本端规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | HTTP本端实体组标识 | 1 | 本端规划 | 该参数需要提前通过<br>[**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)<br>添加。 |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | 本端实体类型 | 服务端：SERVER<br>客户端：CLIENT | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | 端口号 | 30116 | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | 是否启用TLS | YES | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | TLS索引 | 服务端：1<br>客户端：2 | 全网规划 | 用于指定关联的TLSPARA的索引，需要与<br>[**ADD TLSPARA**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP安全管理/HTTP TLS安全管理/增加TLS参数（ADD TLSPARA）_84132096.md)<br>中配置的<br>“索引”<br>匹配。 |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | IP类型 | IPv4 | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | IPv4地址 | 10.2.144.10 | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | VPN名称 | _public_ | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD HTTPLE: INDEX=1, HTTPLEGRPIDX=1, LETYPE=SERVER, PORT=30116, TLSFLG=YES, TLSIDX=1, IPTYPE=IPv4,IPV4="10.16.1.5", VPNNAME="_public_";`
  `ADD HTTPLE: INDEX=2, HTTPLEGRPIDX=1, LETYPE=CLIENT, TLSIDX=2, IPTYPE=IPv4, IPV4="10.16.1.6",VPNNAME="_public_";`
  `ADD HTTPLE: INDEX=3, HTTPLEGRPIDX=2, LETYPE=SERVER, PORT=30116, TLSFLG=YES, TLSIDX=3, IPTYPE=IPv4,IPV4="10.16.0.7", VPNNAME="_public_";`
  `ADD HTTPLE: INDEX=4, HTTPLEGRPIDX=2, LETYPE=CLIENT, TLSIDX=4, IPTYPE=IPv4, IPV4="10.16.0.8", VPNNAME="_public_";`
- 操作步骤上下文（±2 行原文）：
  L92:
    >       **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
    >     f. 增加AMF作为服务器端的HTTP本端实体。其中， “本端实体类型” 配置为 “SERVER” ， “TLS索引” 需要与 [步骤 4.b](#ZH-CN_OPI_0170185215__substep11258153020169) 中配置的 “索引” 相同。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     g. 增加AMF作为客户端的HTTP本端实体。其中， “本端实体类型” 配置为 “CLIENT” ， “TLS索引” 需要与 [步骤 4.c](#ZH-CN_OPI_0170185215__substep3950173215178) 中配置的 “索引” 相同。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
  L94:
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     g. 增加AMF作为客户端的HTTP本端实体。其中， “本端实体类型” 配置为 “CLIENT” ， “TLS索引” 需要与 [步骤 4.c](#ZH-CN_OPI_0170185215__substep3950173215178) 中配置的 “索引” 相同。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     h. 增加AMF服务化接口的接入点信息。
    >       [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)
  L111:
    >       **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
    >     f. 增加NRF作为服务器端的HTTP本端实体。其中， “本端实体类型” 配置为 “SERVER” ， “TLS索引” 需要与 [步骤 5.b](#ZH-CN_OPI_0170185215__substep2930395211) 中配置的 “索引” 相同。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     g. 增加NRF作为客户端的HTTP本端实体。其中， “本端实体类型” 配置为 “CLIENT” ， “TLS索引” 需要与 [步骤 5.c](#ZH-CN_OPI_0170185215__substep13928222179) 中配置的 “索引” 相同。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)

**md：`WSFD-010308/激活SBI接口加密特性(PSK)_57783838.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | HTTPLE本端实体索引(INDEX) | 服务端：1<br>客户端：2 | 本端规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | HTTP本端实体组标识(HTTPLEGRPIDX) | 1 | 本端规划 | 该参数需要提前通过<br>[**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)<br>添加。 |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | 本端实体类型(LETYPE) | 服务端：SERVER<br>客户端：CLIENT | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | 端口号(PORT) | 30116 | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | 是否启用TLS(TLSFLG) | YES | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | TLS索引(TLSIDX) | 服务端：1<br>客户端：2 | 全网规划 | 用于指定关联的TLSPARA的索引，需要与<br>[**ADD TLSPARA**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP安全管理/HTTP TLS安全管理/增加TLS参数（ADD TLSPARA）_84132096.md)<br>中配置的<br>“索引”<br>匹配。 |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | IP类型(IPTYPE) | IPv4 | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | IPv4地址(IPV4) | 10.2.144.10 | 全网规划 | - |
  | [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md) | VPN名称(VPNNAME) | _public_ | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD HTTPLE: INDEX=1, HTTPLEGRPIDX=1, LETYPE=SERVER, PORT=30116, TLSFLG=YES, TLSIDX=1, IPTYPE=IPv4,IPV4="10.16.1.5", VPNNAME="_public_";`
  `ADD HTTPLE: INDEX=2, HTTPLEGRPIDX=1, LETYPE=CLIENT, TLSIDX=2, IPTYPE=IPv4, IPV4="10.16.1.6",VPNNAME="_public_";`
- 操作步骤上下文（±2 行原文）：
  L79:
    >       **[**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
    >     i. 增加AMF作为服务端的HTTP本端实体。其中， “本端实体类型” 配置为 “SERVER” ， “TLS索引” 需要与 [步骤 1.e](#ZH-CN_OPI_0000001557783838__substep11258153020169) 中配置的 “索引” 相同。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN名称"** 分别与 [步骤 1.h](#ZH-CN_OPI_0000001557783838__substep1774916843911) 。中保持一致。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     j. 增加AMF作为客户端的HTTP本端实体。其中， “本端实体类型” 配置为 “CLIENT” ， “TLS索引” 需要与 [步骤 1.f](#ZH-CN_OPI_0000001557783838__substep3950173215178) 中配置的 “索引” 相同。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN名称"** 分别与 [步骤 1.h](#ZH-CN_OPI_0000001557783838__substep1774916843911) 。中保持一致。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
  L81:
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     j. 增加AMF作为客户端的HTTP本端实体。其中， “本端实体类型” 配置为 “CLIENT” ， “TLS索引” 需要与 [步骤 1.f](#ZH-CN_OPI_0000001557783838__substep3950173215178) 中配置的 “索引” 相同。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN名称"** 分别与 [步骤 1.h](#ZH-CN_OPI_0000001557783838__substep1774916843911) 。中保持一致。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     k. 增加AMF服务化接口的接入点信息。
    >       [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)
  L145:
    > 
    > ```
    > ADD HTTPLE: INDEX=1, HTTPLEGRPIDX=1, LETYPE=SERVER, PORT=30116, TLSFLG=YES, TLSIDX=1, IPTYPE=IPv4,IPV4="10.16.1.5", VPNNAME="_public_";
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/配置QoS能力开放功能_48518810.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | HTTPLE本端实体索引（INDEX） | 7 | 本端规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | HTTP本端实体组标识（HTTPLEGRPIDX） | 3 | 本端规划 | 该参数需要提前通过<br>**[ADD HTTPLEGRP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)**<br>添加。 |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | 本端实体类型（LETYPE） | CLIENT | 全网规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | IP类型（IPTYPE） | IPv6 | 全网规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | IPv6地址（IPV6） | fe80:8029:5008:6B::247 | 全网规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | VPN名称（VPNNAME） | vpn_restif | 本端规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | HTTPLE本端实体索引（INDEX） | 8 | 本端规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | HTTP本端实体组标识（HTTPLEGRPIDX） | 3 | 本端规划 | 该参数需要提前通过<br>**[ADD HTTPLEGRP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)**<br>添加。 |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | 本端实体类型（LETYPE） | SERVER | 本端规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | 端口号（PORT） | 80 | 本端规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | 是否启用TLS（TLSFLG） | NO | 本端规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | IP类型（IPTYPE） | IPv6 | 本端规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | IPv6地址（IPV6） | fe80:8029:5008:6B::248 | 本端规划 | - |
  | **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)** | VPN名称（VPNNAME） | vpn_restif | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD HTTPLE: INDEX=7, HTTPLEGRPIDX=3, LETYPE=CLIENT, DESC="BSF Client", IPTYPE=IPv6, IPV6="`
  `ADD HTTPLE: INDEX=8, HTTPLEGRPIDX=3, LETYPE=SERVER, PORT=80, TLSFLG=NO, DESC="BSF Server", IPTYPE=IPv6, IPV6="`
- 操作步骤上下文（±2 行原文）：
  L74:
    >   **[ADD HTTPLEGRP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)**
    > 6. 配置HTTP本端端点信息。
    >   **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)**
    > 7. 配置服务化接口本端实体。
    >   **[ADD SBIAPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)**
  L126:
    > 
    >   ```
    >   ADD HTTPLE: INDEX=7, HTTPLEGRPIDX=3, LETYPE=CLIENT, DESC="BSF Client", IPTYPE=IPv6, IPV6="
    >   fe80:8029:5008:6B::247
    >   ", VPNNAME="
  L134:
    > 
    >   ```
    >   ADD HTTPLE: INDEX=8, HTTPLEGRPIDX=3, LETYPE=SERVER, PORT=80, TLSFLG=NO, DESC="BSF Server", IPTYPE=IPv6, IPV6="
    >   fe80:8029:5008:6B::248
    >   ", VPNNAME="

## ④ 自动比对
- 命令真相参数（12）：['DESC', 'HTTPLEGRPIDX', 'INDEX', 'IPTYPE', 'IPV4', 'IPV6', 'LETYPE', 'PORT', 'RFLAG', 'TLSFLG', 'TLSIDX', 'VPNNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 15, '全网规划': 17}（多值→atom 应考虑 decision_driven）
