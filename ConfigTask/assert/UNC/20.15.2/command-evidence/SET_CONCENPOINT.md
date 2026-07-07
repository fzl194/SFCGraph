# 命令证据包：SET CONCENPOINT
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

![](设置集中点部署模式（SET CONCENPOINT）_09896704.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改集中点模式可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。涉及Diameter链路的接口为Gx、Gy、S6b接口。

此命令用于设置信令集中点的部署模式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- LOCALIP_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
- LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。Loc

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GACONCENMODE | Ga集中点模式 | local_planned | optional | 无 | 枚举类型。 |
| GXCONCENMODE | Gx集中点模式 | local_planned | optional | 无 | 枚举类型。 |
| GYCONCENMODE | Gy集中点模式 | local_planned | optional | 无 | 枚举类型。 |
| S6BCONCENMODE | S6b集中点模式 | local_planned | optional | 无 | 枚举类型。 |
| GAPORTPERPROC | Ga每进程端口数 | local_planned | conditional | 无 | 整数类型，取值范围为1~5。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT:S6BCONCENMODE=LOCALPORT;`
- 操作步骤上下文（±2 行原文）：
  L77:
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. **可选：**配置S6b接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
    > 5. 创建S6bif接口。
    >   [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
  L100:
    >   > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >   >
    >   > 当 “S6b集中点模式” 通过 [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) 命令选择为 “LOCALPORT” 时，可使用 [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) 命令设置本端的端口号。
    > 12. 配置PGW-C identity的属性。
    >   [**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)
  L136:
    > 4. 配置S6b接口Diameter应用集中点模式。
    >   ```
    >   SET CONCENPOINT:S6BCONCENMODE=LOCALPORT;
    >   ```
    > 5. 创建S6bif接口。

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
    > - [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) | Gx集中点模式（GXCONCENMODE） | LOCALPORT | 本端规划 | Diameter应用集中点模式。 |
  | [**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) | Gx集中点模式（GXCONCENMODE） | LOCALPORT | 本端规划 | Diameter应用集中点模式。 |
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT: GXCONCENMODE=LOCALPORT;`
  `SET CONCENPOINT: GXCONCENMODE=LOCALPORT;`
- 操作步骤上下文（±2 行原文）：
  L122:
    >   [**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：**配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   [**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
    > 5. 配置Gx逻辑接口。
    >     a. 配置逻辑IP地址。
  L150:
    >   > **说明**
    >   > - 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >   > - 当“Gx集中点模式”通过[**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)命令选择为“LOCALPORT”时，可使用[**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)命令设置本端的端口号。
    >   **同一PGW-C对接多个PGW-U，且不同PGW-U下的用户IP存在相同时，必须执行 [步骤 10](#ZH-CN_OPI_0230805096__step38911553714) ~ [步骤 16](#ZH-CN_OPI_0230805096__step3536110122512) ；IP地址不同时，可不配置 [步骤 10](#ZH-CN_OPI_0230805096__step38911553714) ~ [步骤 16](#ZH-CN_OPI_0230805096__step3536110122512) 。**
    > 10. 配置Diameter本端主机组。
  L208:
    > 3. 配置Gx接口Diameter应用集中点模式。
    >   ```
    >   SET CONCENPOINT: GXCONCENMODE=LOCALPORT;
    >   ```
    > 4. 配置Gx逻辑接口。

### WSFD-104508

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 数据规划表（该命令的参数行）：
  | **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** | Gx集中点模式(GXCONCENMODE) | LOCALPORT | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT:GXCONCENMODE=LOCALPORT;`
- 操作步骤上下文（±2 行原文）：
  L111:
    >   **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > 11. 配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > 12. 建立本端到对端SCTP端点的链路。
    >   **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
  L115:
    >   **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    >   > **说明**
    >   > 当 “Gx集中点模式” 通过 **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，支持使用 **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    > 
    > ## [验证方法](#ZH-CN_OPI_0230442391)
  L197:
    > 
    > ```
    > SET CONCENPOINT:GXCONCENMODE=LOCALPORT;
    > ```
    > 

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 数据规划表（该命令的参数行）：
  | **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** | Gy集中点模式(GYCONCENMODE) | LOCALPORT | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT:GYCONCENMODE=LOCALPORT;`
- 操作步骤上下文（±2 行原文）：
  L108:
    >   **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > 11. 配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > 12. 建立本端到对端SCTP端点的链路。
    >   **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
  L112:
    >   **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    >   > **说明**
    >   > 当 “Gy集中点模式” 通过 **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，支持使用 **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    > 
    > ## [验证方法](#ZH-CN_OPI_0230602207)
  L188:
    > 
    > ```
    > SET CONCENPOINT:GYCONCENMODE=LOCALPORT;
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **SET CONCENPOINT** | Ga集中点模式（GACONCENMODE） | SINGLE_CONNECT | 本端规划 | 如果对端CG网元需要本端提供足够多的Ga链路，可配置GACONCENMODE参数为MULTI_PORT，并根据GAPORTPERPROC参数调整Ga链路数，否则配置GACONCENMODE参数为SINGLE_CONNECT。 |
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT: GACONCENMODE=SINGLE_CONNECT;`
- 操作步骤上下文（±2 行原文）：
  L67:
    >   **ADD VPNINST**
    > 4. 配置Ga接口集中点的部署模式。
    >   **SET CONCENPOINT**
    > 5. 配置Ga逻辑接口。
    >     a. 配置逻辑IP地址。
  L130:
    > 4. 配置Ga接口集中点的部署模式。
    >   ```
    >   SET CONCENPOINT: GACONCENMODE=SINGLE_CONNECT;
    >   ```
    > 5. 配置组级Ga逻辑接口。

### WSFD-109001

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **SET CONCENPOINT** | Gy集中点模式（GYCONCENMODE） | LOCALPORT | 本端规划 | Diameter应用集中点模式。 |
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT: GYCONCENMODE=LOCALPORT;`
- 操作步骤上下文（±2 行原文）：
  L85:
    >   **ADD L3VPNINST**
    > 4. **可选：**配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **SET CONCENPOINT**
    > 5. 配置Gy逻辑接口。
    >     a. 配置逻辑IP地址。
  L108:
    >       **ADD DIAMCONNECTION**
    >       > **说明**
    >       > 当 “Gy集中点模式” 通过 **SET CONCENPOINT** 命令选择为 “LOCALPORT” 时，可使用 **ADD DIAMCONNECTION** 命令设置本端的端口号。
    >     c. 配置在线计费系统的OCS组。
    >       **ADD OCSGROUP**
  L149:
    > 4. 配置Gy接口Diameter应用集中点模式。
    >   ```
    >   SET CONCENPOINT: GYCONCENMODE=LOCALPORT;
    >   ```
    > 5. 配置Gy逻辑接口。

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > - **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** | Gx集中点模式(GXCONCENMODE) | LOCALPORT | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT:GXCONCENMODE=LOCALPORT;`
  `SET CONCENPOINT:GXCONCENMODE=LOCALPORT;`
- 操作步骤上下文（±2 行原文）：
  L126:
    >   [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：**配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    >   > **说明**
    >   > - LOCALIP_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
  L165:
    >       > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >       >
    >       > 当 “Gx集中点模式” 通过 **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，可使用 **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    >     e. 配置PCRF域的Diameter路由。
    >       **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
  L219:
    >   //配置Gx接口Diamteter应用集中点模式。
    >   ```
    >   SET CONCENPOINT:GXCONCENMODE=LOCALPORT;
    >   ```
    >   //配置Gx逻辑接口。

### WSFD-011133

**md：`WSFD-011133/WSFD-011133 Gy over DRA参考信息_29725462.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > - **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 数据规划表（该命令的参数行）：
  | **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** | Gy集中点模式(GYCONCENMODE) | LOCALPORT | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT:GYCONCENMODE=LOCALPORT;`
  `SET CONCENPOINT:GYCONCENMODE=LOCALPORT;`
- 操作步骤上下文（±2 行原文）：
  L118:
    >   [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：**配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    >   > **说明**
    >   > - LOCALIP_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
  L156:
    >             > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >             >
    >             > 当 “Gy集中点模式” 通过 **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，可使用 **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    >     d. 配置Diameter路由。
    >       **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
  L196:
    >   //配置Gy接口Diamteter应用集中点模式。
    >   ```
    >   SET CONCENPOINT:GYCONCENMODE=LOCALPORT;
    >   ```
    >   //配置Gy逻辑接口。

### WSFD-011134

**md：`WSFD-011134/激活S6b over DRA（静态路由+BFD组网）_75821602.md`**
- 数据规划表（该命令的参数行）：
  | [**SET CONCENPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) | S6b集中点模式（S6BCONCENMODE） | LOCALPORT | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `SET CONCENPOINT:S6BCONCENMODE=LOCALPORT;`
  `SET CONCENPOINT:S6BCONCENMODE=LOCALPORT;`
- 操作步骤上下文（±2 行原文）：
  L98:
    >   [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 4. **可选：**配置S6b接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   [**SET CONCENPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
    >   > **说明**
    >   > - LOCALIP_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
  L139:
    >       > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >       >
    >       > 当 “S6b集中点模式” 通过 [**SET CONCENPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) 命令选择为 “LOCALPORT” 时，可使用 [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) 命令设置本端的端口号。
    >     e. 配置Diameter路由。
    >       [**ADD DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)
  L179:
    >   //配置S6b接口Diameter应用集中点模式。
    >   ```
    >   SET CONCENPOINT:S6BCONCENMODE=LOCALPORT;
    >   ```
    >   //配置S6b逻辑接口。

## ④ 自动比对
- 命令真相参数（5）：['GACONCENMODE', 'GAPORTPERPROC', 'GXCONCENMODE', 'GYCONCENMODE', 'S6BCONCENMODE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 9}（多值→atom 应考虑 decision_driven）
