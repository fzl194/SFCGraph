# 命令证据包：ADD VPNINST
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md`
> 用该命令的特性数：15

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于创建指定的VPN实例。创建VPN实例后，还需要对VPN实例进行一系列的配置，必要的操作如下：

- 将VPN实例与PE上连向VPN网络的接口绑定。
- 通过配置接口与VPN实例绑定，该接口成为私网接口，从该接口进入的报文使用VPN实例中的转发信息进行转发。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- “_public_”是公网缺省VPN的实例名，不允许用户配置。

- 最多可输入10000条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| VPNINSTANCE | VPN实例名 | global_planned | required | 无 | 字符串类型，输入长度范围是1~31。区分大小写，不支持空格。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010504

**md：`WSFD-010504/WSFD-010504 控制面地址分配方式参考信息_77813716.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 
    > - [**ADD ADDRPOOL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md)

### WSFD-104005

**md：`WSFD-104005/WSFD-104005 DHCPv6地址分配参考信息_61255173.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[ADD ADDRPOOL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md)**
    > - [**ADD AGENTIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/代理IP管理/增加远端地址池代理IP信息（ADD AGENTIP）_32224047.md)

### WSFD-104413

**md：`WSFD-104413/WSFD-104413 DHCP功能参考信息_61065989.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[ADD ADDRPOOL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md)**
    > - [**ADD AGENTIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/代理IP管理/增加远端地址池代理IP信息（ADD AGENTIP）_32224047.md)

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_3gpp_aaa";`
- 操作步骤上下文（±2 行原文）：
  L72:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 配置VPN实例。
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 3. 配置L3VPN实例。
    >   **[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**
  L125:
    > 2. 配置VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_3gpp_aaa";
    >   ```
    > 3. 创建VPN实例。

### WSFD-109101

**md：`WSFD-109101/配置QoS能力开放功能_48518810.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_restif | 全网规划 | 创建VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="`
- 操作步骤上下文（±2 行原文）：
  L68:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建一个VPN实例。
    >   [**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. 配置Restif逻辑接口地址。
    >   [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
  L95:
    > 1. 创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="
    >   vpn_restif
    >   ";

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_gxif | 全网规划 | 创建VPN实例。 |
  | [**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_gxif | 全网规划 | 创建VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_gxif";`
  `ADD VPNINST:VPNINSTANCE="vpn_gxif";`
- 操作步骤上下文（±2 行原文）：
  L120:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建一个VPN实例。
    >   [**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：**配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   [**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
  L204:
    > 2. 创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_gxif";
    >   ```
    > 3. 配置Gx接口Diameter应用集中点模式。
  L261:
    > 2. 创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_gxif";
    >   ```
    > 3. 配置Gx接口Diameter应用集中点模式。

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    > - **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)

**md：`WSFD-011306/配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_pdn<br>vpn_aaa | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST: VPNINSTANCE ="vpn_pdn";`
  `ADD VPNINST:VPNINSTANCE="vpn_aaa";`
- 操作步骤上下文（±2 行原文）：
  L92:
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建VPN实例。
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 5. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
  L157:
    > 
    > ```
    > ADD VPNINST: VPNINSTANCE ="vpn_pdn";
    > ADD VPNINST:VPNINSTANCE="vpn_aaa";
    > ```
  L158:
    > ```
    > ADD VPNINST: VPNINSTANCE ="vpn_pdn";
    > ADD VPNINST:VPNINSTANCE="vpn_aaa";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）_31879931.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_pdn | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST: VPNINSTANCE ="vpn_pdn";`
- 操作步骤上下文（±2 行原文）：
  L94:
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建VPN实例。
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 5. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
  L147:
    > 
    > ```
    > ADD VPNINST: VPNINSTANCE ="vpn_pdn";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_enterprise | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_enterprise";`
- 操作步骤上下文（±2 行原文）：
  L124:
    >   > 如果需要一同配置IPv6的GRE隧道，则步骤b、d均需要先使用 **[**SET IFIPV6ENABLE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6使能/修改接口IPv6使能（SET IFIPV6ENABLE）_00601329.md)** 命令开启IPv6使能，再使用 **[**ADD IFIPV6ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESS）_49961222.md)** 命令配置IPv6地址，步骤e需要使用 **[**ADD SRROUTE6**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv6静态路由/增加IPv6静态路由（ADD SRROUTE6）_50280922.md)** 命令配置IPv6静态路由。
    > 5. 创建VPN实例。
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 6. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
  L224:
    > 
    > ```
    > ADD VPNINST:VPNINSTANCE="vpn_enterprise";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_aaa<br>vpn_enterprise | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_enterprise";`
  `ADD VPNINST:VPNINSTANCE="vpn_aaa";`
- 操作步骤上下文（±2 行原文）：
  L124:
    >   > 如果需要一同配置IPv6的GRE隧道，则步骤b、d均需要先使用 **[**SET IFIPV6ENABLE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6使能/修改接口IPv6使能（SET IFIPV6ENABLE）_00601329.md)** 命令开启IPv6使能，再使用 **[**ADD IFIPV6ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESS）_49961222.md)** 命令配置IPv6地址，步骤e需要使用 **[**ADD SRROUTE6**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv6静态路由/增加IPv6静态路由（ADD SRROUTE6）_50280922.md)** 命令配置IPv6静态路由。
    > 5. 创建VPN实例。
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 6. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
  L237:
    > 
    > ```
    > ADD VPNINST:VPNINSTANCE="vpn_enterprise";
    > ```
    > 
  L241:
    > 
    > ```
    > ADD VPNINST:VPNINSTANCE="vpn_aaa";
    > ```
    > 

### WSFD-104004

**md：`WSFD-104004/WSFD-104004 IPv6前缀代理参考信息_76459529.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - [**RMV VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/删除VPN实例（RMV VPNINST）_09651424.md)
    > - [**LST VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)

**md：`WSFD-104004/激活IPv6前缀代理_76459527.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTACE） | vpn1 | 全网规划 | 配置VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD VPNINST`
- 操作步骤上下文（±2 行原文）：
  L48:
    > 3. 配置IPv6 VPN。
    >     a. 创建VPN实例。
    >       [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    >     b. 使能IPv6地址族。
    >       **[**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**
  L85:
    > 
    > ```
    > ADD VPNINST
    > : VPNINSTANCE="vpn1";
    > ADD L3VPNINST: VRFNAME="vpn1";

### WSFD-011307

**md：`WSFD-011307/激活支持RADIUS抄送功能_33769357.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpntest | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST: VPNINSTANCE="vpntest";`
- 操作步骤上下文（±2 行原文）：
  L56:
    >   **[ADD RDSSVRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)**
    > 3. 创建VPN实例。
    >   [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：** 配置UP列表。
    >   [**ADD UPLIST4RDS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)
  L86:
    > 
    > ```
    > ADD VPNINST: VPNINSTANCE="vpntest";
    > ```
    > 

### WSFD-104508

**md：`WSFD-104508/WSFD-104508 SCTP参考信息_29341126.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > - [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名称（VPNINSTANCE） | vpn_gxif | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST: VPNINSTANCE="vpn_gxif";`
- 操作步骤上下文（±2 行原文）：
  L151:
    > 
    > ```
    > ADD VPNINST: VPNINSTANCE="vpn_gxif";
    > ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.20.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";
    > ```

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名称（VPNINSTANCE） | vpn_gyif | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST: VPNINSTANCE="vpn_gyif";`
- 操作步骤上下文（±2 行原文）：
  L144:
    > 
    > ```
    > ADD VPNINST: VPNINSTANCE="vpn_gyif";
    > ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
    > ```

### WSFD-011201

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **ADD VPNINST** | VPN实例名（VPNINSTANCE） | vpn_ga | 本端规划 | 创建VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_ga";`
- 操作步骤上下文（±2 行原文）：
  L65:
    >   **ADD L3VPNINST**
    > 3. 创建VPN实例。
    >   **ADD VPNINST**
    > 4. 配置Ga接口集中点的部署模式。
    >   **SET CONCENPOINT**
  L126:
    > 3. 创建VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_ga";
    >   ```
    > 4. 配置Ga接口集中点的部署模式。

### WSFD-109001

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD VPNINST** | VPN实例名（VPNINSTANCE） | vpn_gy | 本端规划 | 创建VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_gy";`
- 操作步骤上下文（±2 行原文）：
  L81:
    > 1. 参考 **《UNC产品手册》：UNC初始配置与调测->** **组网路由配置->** **配置VNF侧IP路由数据（非SDN）->** **手动部署** **->** **配置静态路由+BFD组网（IPv4）** 配置对应的组网。
    > 2. 创建VPN实例。
    >   **ADD VPNINST**
    > 3. 创建L3VPN实例。
    >   **ADD L3VPNINST**
  L139:
    > 2. 创建VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_gy";
    >   ```
    > 3. 创建L3VPN实例。

### WSFD-102101

**md：`WSFD-102101/激活VoLTE紧急呼叫（适用于SGW-C_PGW-C）_30394882.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn1 | 本端规划 | 配置APN所属的VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn1";`
- 操作步骤上下文（±2 行原文）：
  L49:
    > 3. 配置APN参数。
    >     a. 配置APN所属的VPN实例。
    >       [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    >     b. 创建APN实例，使能紧急呼叫功能。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
  L76:
    >   //配置APN所属的VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn1";
    >   ```
    >   //创建APN实例，使能紧急呼叫功能。

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)**
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名(VPNINSTANCE) | vpn_gxif | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_gxif";`
  `ADD VPNINST:VPNINSTANCE="vpn_gxif";`
- 操作步骤上下文（±2 行原文）：
  L124:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建一个VPN实例。
    >   [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：**配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
  L215:
    >   //创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_gxif";
    >   ```
    >   //配置Gx接口Diamteter应用集中点模式。
  L305:
    >   //创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_gxif";
    >   ```
    >   //配置Gx接口Diamteter应用集中点模式。

### WSFD-011133

**md：`WSFD-011133/WSFD-011133 Gy over DRA参考信息_29725462.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名(VPNINSTANCE) | vpn_gyif | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_gyif";`
  `ADD VPNINST:VPNINSTANCE="vpn_gyif";`
- 操作步骤上下文（±2 行原文）：
  L116:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建一个VPN实例。
    >   [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：**配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
  L192:
    >   //创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_gyif";
    >   ```
    >   //配置Gy接口Diamteter应用集中点模式。
  L304:
    >   //创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_gyif";
    >   ```
    >   //配置Gy接口Diamteter应用集中点模式。

### WSFD-011134

**md：`WSFD-011134/激活S6b over DRA（静态路由+BFD组网）_75821602.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_s6bif | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINST:VPNINSTANCE="vpn_s6bif";`
  `ADD VPNINST:VPNINSTANCE="vpn_s6bif";`
- 操作步骤上下文（±2 行原文）：
  L96:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建一个VPN实例。
    >   [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：**配置S6b接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   [**SET CONCENPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
  L175:
    >   //创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_s6bif";
    >   ```
    >   //配置S6b接口Diameter应用集中点模式。
  L287:
    >   //创建一个VPN实例。
    >   ```
    >   ADD VPNINST:VPNINSTANCE="vpn_s6bif";
    >   ```
    >   //配置S6b接口Diameter应用集中点模式。

## ④ 自动比对
- 命令真相参数（1）：['VPNINSTANCE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 4, '本端规划': 13}（多值→atom 应考虑 decision_driven）
