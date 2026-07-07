# 命令证据包：ADD LOGICIP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md`
> 用该命令的特性数：7

## ② 命令真相（mml_commands.jsonl）
**功能**：该命令用于增加逻辑IP地址。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令最多支持添加10240条逻辑IP。
- 该命令只在UNC网元下生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| IPVERSION | IP地址类型 | global_planned | required | 无 | <br>- “IPv4（IPv4）”：IPv4地址 |
| LOGICIPV4 | IPv4地址 | global_planned | conditional | 无 | IPv4地址类型。业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127 |
| LOGICIPV6 | IPv6地址 | global_planned | conditional | 无 | IPv6地址类型。IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF |
| IPV4MTU | IPv4 MTU | global_planned | conditional | 1500 | 整数类型，取值范围是328~9600。 |
| IPV6MTU | IPv6 MTU值 | global_planned | conditional | 1500 | 整数类型，取值范围是1280~9600。 |
| VPNINSTNAME | VPN实例名称 | global_planned | optional | 无 | 字符串类型，输入长度范围是1~31。 |
| DESC | 描述 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~255。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010308

**md：`WSFD-010308/激活SBI接口加密特性(CERT)_70185215.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IP地址类型(IPVERSION) | IPv4 | 全网规划 | - |
  | **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IPv4地址(LOGICIPV4) | 10.2.144.10 | 全网规划 | - |
  | **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | VPN实例名称(VPNINSTNAME) | _public_ | 全网规划 | - |
  | **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | 描述(DESC) | test | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.5", VPNINSTNAME="_public_", DESC="test";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.6", VPNINSTNAME="_public_", DESC="test";`
- 操作步骤上下文（±2 行原文）：
  L90:
    >       [**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)
    >     e. 增加逻辑IP地址。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN实例名称"** 全网规划。
    >       **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
    >     f. 增加AMF作为服务器端的HTTP本端实体。其中， “本端实体类型” 配置为 “SERVER” ， “TLS索引” 需要与 [步骤 4.b](#ZH-CN_OPI_0170185215__substep11258153020169) 中配置的 “索引” 相同。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
  L109:
    >       [**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)
    >     e. 增加逻辑IP地址。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN实例名称"** 全网规划。
    >       **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
    >     f. 增加NRF作为服务器端的HTTP本端实体。其中， “本端实体类型” 配置为 “SERVER” ， “TLS索引” 需要与 [步骤 5.b](#ZH-CN_OPI_0170185215__substep2930395211) 中配置的 “索引” 相同。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
  L155:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.5", VPNINSTNAME="_public_", DESC="test";
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.6", VPNINSTNAME="_public_", DESC="test";
    > ```

**md：`WSFD-010308/激活SBI接口加密特性(PSK)_57783838.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IP地址类型(IPVERSION) | IPv4 | 全网规划 | - |
  | **[**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IPv4地址(LOGICIPV4) | 10.2.144.10 | 全网规划 | - |
  | **[**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | VPN实例名称(VPNINSTNAME) | _public_ | 全网规划 | - |
  | **[**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | 描述(DESC) | test | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.5", VPNINSTNAME="_public_", DESC="test";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.6", VPNINSTNAME="_public_", DESC="test";`
- 操作步骤上下文（±2 行原文）：
  L77:
    >       [**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)
    >     h. 增加逻辑IP地址。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN实例名称"** 全网规划。
    >       **[**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
    >     i. 增加AMF作为服务端的HTTP本端实体。其中， “本端实体类型” 配置为 “SERVER” ， “TLS索引” 需要与 [步骤 1.e](#ZH-CN_OPI_0000001557783838__substep11258153020169) 中配置的 “索引” 相同。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN名称"** 分别与 [步骤 1.h](#ZH-CN_OPI_0000001557783838__substep1774916843911) 。中保持一致。
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
  L138:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.5", VPNINSTNAME="_public_", DESC="test";
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.6", VPNINSTNAME="_public_", DESC="test";
    > ```
  L139:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.5", VPNINSTNAME="_public_", DESC="test";
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.16.1.6", VPNINSTNAME="_public_", DESC="test";
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/配置QoS能力开放功能_48518810.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICIP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IP地址类型（IPVERSION） | IPv6 | 全网规划 | 配置Restif逻辑接口 |
  | **[ADD LOGICIP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IPv6地址（LOGICIPV6） | fe80:8029:5008:6B::247 | 全网规划 | 配置Restif逻辑接口 |
  | **[ADD LOGICIP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | VPN实例名称（VPNINSTNAME） | vpn_restif | 全网规划 | 配置Restif逻辑接口 |
  | **[ADD LOGICIP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | 描述（DESC） | Restful_IPv6_Client | 全网规划 | 配置Restif逻辑接口 |
  | **[ADD LOGICIP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IP地址类型（IPVERSION） | IPv6 | 全网规划 | 配置Restif逻辑接口 |
  | **[ADD LOGICIP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IPv6地址（LOGICIPV6） | fe80:8029:5008:6B::248 | 全网规划 | 配置Restif逻辑接口 |
  | **[ADD LOGICIP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | VPN实例名称（VPNINSTNAME） | vpn_restif | 全网规划 | 配置Restif逻辑接口 |
  | **[ADD LOGICIP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | 描述（DESC） | Restful_IPv6_Server | 全网规划 | 配置Restif逻辑接口 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP:IPVERSION=`
  `ADD LOGICIP:IPVERSION=`
- 操作步骤上下文（±2 行原文）：
  L70:
    >   [**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. 配置Restif逻辑接口地址。
    >   [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    > 5. 配置HTTP本端端点组信息。
    >   **[ADD HTTPLEGRP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)**
  L101:
    > 2. 配置即Restif逻辑接口地址（HTTP本端端点的逻辑地址信息）。
    >   ```
    >   ADD LOGICIP:IPVERSION=
    >   IPv6
    >   , LOGICIPV6="
  L110:
    >   ```
    >   ```
    >   ADD LOGICIP:IPVERSION=
    >   IPv6
    >   , LOGICIPV6="

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口名称（NAME） | gxif1/0/0<br>gxif1/0/1 | 本端规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.10.1<br>10.8.10.2 | 全网规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | VPN实例名（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | 已通过命令<br>[**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口名称（NAME） | gxif1/0/0<br>gxif1/0/1 | 本端规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.10.1<br>10.8.10.2 | 全网规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | VPN实例名（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | 已通过命令<br>[**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1", VPNINSTNAME="vpn_gxif";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2", VPNINSTNAME="vpn_gxif";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1", VPNINSTNAME="vpn_gxif";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2", VPNINSTNAME="vpn_gxif";`
- 操作步骤上下文（±2 行原文）：
  L125:
    > 5. 配置Gx逻辑接口。
    >     a. 配置逻辑IP地址。
    >       [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >     b. 配置Gx逻辑接口。
    >       [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
  L129:
    >       [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    >   > **说明**
    >   > [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) 中的“IP地址+VPN实例名称”和 [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) 命令中的“IP地址+VPN实例名称”必须一致。
    > 6. 配置GGSN/PGW-C的设备标识。
    >   [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
  L212:
    > 4. 配置Gx逻辑接口。
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1", VPNINSTNAME="vpn_gxif";
    >   ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_gxif";
    >   ```

### WSFD-011306

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - 完成[增加APN配置](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)。
    > - **该功能需要与UPF/PGW-U共同完成配置**。配置该功能前，需要确保已在UPF/PGW-U上配置完成使用的过滤器和绑定的流过滤器、规则等业务感知信息。
    > - 已通过[**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)配置完成逻辑接口使用到的逻辑IP。
    > 
    > 数据

**md：`WSFD-011306/配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
  | [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IPv4地址（LOGICIPV4） | 10.8.20.1<br>10.8.20.2 | 本端规划 | 逻辑接口使用的逻辑IP。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_aaa";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_aaa";`
- 操作步骤上下文（±2 行原文）：
  L94:
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 5. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
  L166:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_aaa";
    > ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
    > ```
  L173:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_aaa";
    > ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
    > ```

**md：`WSFD-011306/配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）_31879931.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
  | [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IPv4地址（LOGICIPV4） | 10.8.20.1<br>10.8.20.2 | 本端规划 | 逻辑接口使用的逻辑IP。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";`
- 操作步骤上下文（±2 行原文）：
  L96:
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 5. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
  L155:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
    > ```
  L162:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
    > ```

**md：`WSFD-011306/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
  | [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IPv4地址（LOGICIPV4） | 10.8.20.1<br>10.8.20.2 | 本端规划 | 逻辑接口使用的逻辑IP。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";`
- 操作步骤上下文（±2 行原文）：
  L126:
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 6. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 7. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
  L232:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_enterprise";
    > ```
  L239:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_enterprise";
    > ```

**md：`WSFD-011306/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
  | [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IPv4地址（LOGICIPV4） | 10.8.20.1<br>10.8.20.2 | 本端规划 | 逻辑接口使用的逻辑IP。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";`
- 操作步骤上下文（±2 行原文）：
  L126:
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 6. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 7. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
  L249:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
    > ```
  L256:
    > 
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
    > ```

### WSFD-011201

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **ADD LOGICIP** | IP地址类型（IPVERSION） | IPv4 | 全网规划 | 用户增加逻辑IP。 |
  | **ADD LOGICIP** | IPv4地址（LOGICIPV4） | 192.168.10.63 | 全网规划 | 用户增加逻辑IP。 |
  | **ADD LOGICIP** | VPN实例名称（VPNINSTNAME） | vpn_ga | 已配置数据中获取 | 用户增加逻辑IP。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="192.168.10.63", VPNINSTNAME="vpn_ga";`
- 操作步骤上下文（±2 行原文）：
  L70:
    > 5. 配置Ga逻辑接口。
    >     a. 配置逻辑IP地址。
    >       **ADD LOGICIP**
    >     b. 配置Ga逻辑接口。
    >       **ADD LOGICINF**
  L74:
    >       **ADD LOGICINF**
    >   > **说明**
    >   > **ADD LOGICINF** 中的“IP地址+VPN实例名称”和 **ADD LOGICIP** 命令中的“IP地址+VPN实例名称”必须一致。
    > 6. 配置CG信息。
    >     a. 配置CG信息。
  L134:
    > 5. 配置组级Ga逻辑接口。
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="192.168.10.63", VPNINSTNAME="vpn_ga";
    >   ADD LOGICINF: NAME="gaif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="192.168.10.63", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_ga";
    >   ```

### WSFD-109001

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD LOGICIP** | IP地址类型（IPVERSION） | IPv4 | 全网规划 | 用户增加逻辑IP。 |
  | **ADD LOGICIP** | IPv4地址（LOGICIPV4） | 10.8.20.1<br>10.8.20.2 | 全网规划 | 用户增加逻辑IP。 |
  | **ADD LOGICIP** | VPN实例名称（VPNINSTNAME） | vpn_gy | 已配置数据中获取 | 用户增加逻辑IP。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_gy";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_gy";`
- 操作步骤上下文（±2 行原文）：
  L88:
    > 5. 配置Gy逻辑接口。
    >     a. 配置逻辑IP地址。
    >       **ADD LOGICIP**
    >     b. 配置Gy逻辑接口。
    >       **ADD LOGICINF**
  L92:
    >       **ADD LOGICINF**
    >   > **说明**
    >   > **ADD LOGICINF** 中的“IP地址+VPN实例名称”和 **ADD LOGICIP** 命令中的“IP地址+VPN实例名称”必须一致。
    > 6. 配置在线计费中GGSN/PGW-C的设备标识。
    >   **ADD DIAMLOCINFO**
  L153:
    > 5. 配置Gy逻辑接口。
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_gy";
    >   ADD LOGICINF: NAME="Gyif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="10.8.20.1", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_gy";
    >   ```

### WSFD-011132

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
  | **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IPv4地址（LOGICIPV4） | 10.8.10.1<br>10.8.10.2 | 本端规划 | 逻辑接口使用的逻辑IP。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";`
- 操作步骤上下文（±2 行原文）：
  L23:
    > - 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
    > - 提前进行Gx接口信令组网规划，获取DRA以及PCRF所属Realm等配置信息。
    > - 已通过**[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**配置完成逻辑接口使用到的逻辑IP。
    > 
    > 数据
  L131:
    >   > - LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
    > 5. 配置Gx逻辑接口。
    >   **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
    >   **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. 配置GGSN/PGW-C的设备标识。
  L224:
    > 
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";
    >   ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";

### WSFD-011133

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
  | [**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IPv4地址（LOGICIPV4） | 10.8.10.1<br>10.8.10.2<br>10.8.10.4<br>10.8.10.5 | 本端规划 | 逻辑接口使用的逻辑IP。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.4";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";`
  `ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.5";`
- 操作步骤上下文（±2 行原文）：
  L123:
    >   > - LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
    > 5. 配置Gy逻辑接口。
    >   [**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. 配置GGSN/PGW-C的设备标识信息。
  L201:
    > 
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.4";
    >   ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.11.4",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
  L202:
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.4";
    >   ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.11.4",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
    >   ```

## ④ 自动比对
- 命令真相参数（7）：['DESC', 'IPV4MTU', 'IPV6MTU', 'IPVERSION', 'LOGICIPV4', 'LOGICIPV6', 'VPNINSTNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 22, '本端规划': 16, '固定取值': 2, '已配置数据中获取': 4}（多值→atom 应考虑 decision_driven）
