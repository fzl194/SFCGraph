# 命令证据包：ADD DIAMPEERADDR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。

该命令和PCRF/OCS/DRA等Diameter主机配合使用，指定这些服务器的地址信息，地址分为IP地址和SCTP端点地址。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为510。
- 如果要配置的Diameter主机不存在，则不能配置Diameter链路对端地址信息。
- 一个PCRF/OCS/DRA主机最多可以配置20个IP类型的地址，或者20个SCTP端点类的地址，超出规格后则不能配置。
- 一个Diameter AAA主机最多可以配置2个IP类型的地址，或者2个SCTP端点类的地址，超出规格后则不能配置。
-

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOSTNAME | 主机名称 | 对端协商 | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 150控制是否区分大小写。 |
| ADDRTYPE | 地址类型 | 对端协商 | required | 无 | 枚举类型。 |
| IPV4ADDRESS | IPv4地址 | 对端协商 | conditional | 无 | IPv4地址类型。不支持0.0.0.0和255.255.255.255。 |
| IPV6ADDRESS | IPv6地址 | 对端协商 | conditional | 无 | IPv6地址类型。不支持全F。 |
| PORT | 端口号 | 对端协商 | conditional | 3868 | 整数类型，取值范围为1～65534。 |
| SCTPENDPOINT | SCTP端点名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR: HOSTNAME="3gppaaa",ADDRTYPE=SCTP,SCTPENDPOINT="dc1_AAA01-S6B-SCTPEP01";`
- 操作步骤上下文（±2 行原文）：
  L88:
    > 9. 配置3GPP AAA Server。
    >   [**ADD DIAMETERAAA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA信息/增加Diameter AAA服务器（ADD DIAMETERAAA）_64343821.md)
    >   [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    >     - 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”根据实际规划配置为“IPv4”或“IPv6”。
    >     - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”配置为“SCTP”，“SCTPENDPOINT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
  L89:
    >   [**ADD DIAMETERAAA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA信息/增加Diameter AAA服务器（ADD DIAMETERAAA）_64343821.md)
    >   [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    >     - 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”根据实际规划配置为“IPv4”或“IPv6”。
    >     - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”配置为“SCTP”，“SCTPENDPOINT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
  L90:
    >   [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    >     - 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”根据实际规划配置为“IPv4”或“IPv6”。
    >     - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”配置为“SCTP”，“SCTPENDPOINT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
    >   [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    > - [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | 主机名称（HOSTNAME） | pcrf1<br>pcrf2 | 已配置数据中获取 | 配置PCRF的IP地址。 |
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | 地址类型（ADDRTYPE） | IPv4 | 与对端协商 | 配置PCRF的IP地址。 |
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | IPv4地址（IPV4ADDRESS） | 10.10.10.1<br>10.10.10.2 | 与对端协商 | 配置PCRF的IP地址。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="pcrf1",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1";`
  `ADD DIAMPEERADDR:HOSTNAME="pcrf2",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2";`
- 操作步骤上下文（±2 行原文）：
  L89:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="pcrf1",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1";
    >   ```
    >   ```
  L92:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="pcrf2",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2";
    >   ```
    > 2. 配置PCRF组。

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | 主机名称（HOSTNAME） | pcrf_1<br>pcrf_2 | 已配置数据中获取 | GGSN/PGW-C与pcrf_1之间构建一条IP链路，pcrf_1的IP地址为10.11.21.59。GGSN/PGW-C与pcrf_2之间构建两条IP链路，pcrf_2上的两个IP地址为10.11.21.60和10.11.21.61。 |
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | 地址类型（ADDRTYPE） | IPv4 | 本端规划 | GGSN/PGW-C与pcrf_1之间构建一条IP链路，pcrf_1的IP地址为10.11.21.59。GGSN/PGW-C与pcrf_2之间构建两条IP链路，pcrf_2上的两个IP地址为10.11.21.60和10.11.21.61。 |
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | IPv4地址（IPV4ADDRESS） | 10.11.21.59<br>10.11.21.60<br>10.11.21.61 | 全网规划 | GGSN/PGW-C与pcrf_1之间构建一条IP链路，pcrf_1的IP地址为10.11.21.59。GGSN/PGW-C与pcrf_2之间构建两条IP链路，pcrf_2上的两个IP地址为10.11.21.60和10.11.21.61。 |
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | 主机名称（HOSTNAME） | pcrf_1<br>pcrf_2 | 已配置数据中获取 | GGSN/PGW-C与pcrf_1之间构建一条IP链路，pcrf_1的IP地址为10.11.21.59。GGSN/PGW-C与pcrf_2之间构建两条IP链路，pcrf_2上的两个IP地址为10.11.21.60和10.11.21.61。 |
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | 地址类型（ADDRTYPE） | IPv4 | 本端规划 | GGSN/PGW-C与pcrf_1之间构建一条IP链路，pcrf_1的IP地址为10.11.21.59。GGSN/PGW-C与pcrf_2之间构建两条IP链路，pcrf_2上的两个IP地址为10.11.21.60和10.11.21.61。 |
  | [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | IPv4地址（IPV4ADDRESS） | 10.11.21.59<br>10.11.21.60<br>10.11.21.61 | 全网规划 | GGSN/PGW-C与pcrf_1之间构建一条IP链路，pcrf_1的IP地址为10.11.21.59。GGSN/PGW-C与pcrf_2之间构建两条IP链路，pcrf_2上的两个IP地址为10.11.21.60和10.11.21.61。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="pcrf_1",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.59";`
  `ADD DIAMPEERADDR:HOSTNAME="pcrf_2",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.60";`
  `ADD DIAMPEERADDR:HOSTNAME="pcrf_2",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.61";`
  `ADD DIAMPEERADDR:HOSTNAME="pcrf_1",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.59";`
  `ADD DIAMPEERADDR:HOSTNAME="pcrf_2",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.60";`
  `ADD DIAMPEERADDR:HOSTNAME="pcrf_2",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.61";`
- 操作步骤上下文（±2 行原文）：
  L143:
    >       [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    >     c. 配置PCRF地址信息。
    >       [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > 8. 配置到PCRF的链路组信息。
    >   [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
  L232:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="pcrf_1",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.59";
    >   ```
    >   ```
  L235:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="pcrf_2",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.60";
    >   ```
    >   ```

### WSFD-104508

**md：`WSFD-104508/WSFD-104508 SCTP参考信息_29341126.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - **[ADD PCRF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    > - **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    > - **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > - **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | PCRF主机名（HOSTNAME） | pcrf | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | pcrfendb<br>pcrfendc | 已配置数据中获取 | 配置直连PCRF的SCTP端点名称，SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="pcrf",ADDRTYPE=SCTP,SCTPENDPOINT="pcrfendb";`
  `ADD DIAMPEERADDR:HOSTNAME="pcrf",ADDRTYPE=SCTP,SCTPENDPOINT="pcrfendc";`
- 操作步骤上下文（±2 行原文）：
  L105:
    >       **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    >     b. 配置PCRF的SCTP端点。
    >       **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    >       > **说明**
    >       > **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** 的主机名 “HOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
  L107:
    >       **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    >       > **说明**
    >       > **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** 的主机名 “HOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
    >   **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
  L184:
    > ```
    > ADD PCRF:HOSTNAME="pcrf",REALMNAME="pcrf.huawei.com",VPNINSTANCE="vpn_gxif";
    > ADD DIAMPEERADDR:HOSTNAME="pcrf",ADDRTYPE=SCTP,SCTPENDPOINT="pcrfendb";
    > ADD DIAMPEERADDR:HOSTNAME="pcrf",ADDRTYPE=SCTP,SCTPENDPOINT="pcrfendc";
    > ```

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | Ocs主机名称（OCSHOSTNAME） | ocs | 已配置数据中获取 | 已通过<br>**[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**<br>命令配置，可以通过<br>**[LST OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/查询OCS（LST OCS）_09896957.md)**<br>命令进行查询。 |
  | **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | 配置直连OCS的SCTP端点名称，SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
  | **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | ocsend | 已配置数据中获取 | 配置直连OCS的SCTP端点名称，SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="ocs",ADDRTYPE=SCTP,SCTPENDPOINT="ocsend";`
- 操作步骤上下文（±2 行原文）：
  L102:
    >       **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**
    >     b. 配置OCS的SCTP端点。
    >       **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    >       > **说明**
    >       > **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** 的主机名 “OCSHOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
  L104:
    >       **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    >       > **说明**
    >       > **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** 的主机名 “OCSHOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
    >   **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
  L176:
    > ```
    > ADD OCS:OCSHOSTNAME="ocs",REALMNAME="ocs.huawei.com",VPNINSTANCE="vpn_gyif";
    > ADD DIAMPEERADDR:HOSTNAME="ocs",ADDRTYPE=SCTP,SCTPENDPOINT="ocsend";
    > ```
    > 

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**ADD OCS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    > - [**ADD OCSGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**ADD OCS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    > - [**ADD OCSGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMPEERADDR** | 主机名称（HOSTNAME） | ocs1 | 已配置数据中获取 | 增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。 |
  | **ADD DIAMPEERADDR** | 地址类型（ADDRTYPE） | IPv4 | 本端规划 | 增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。 |
  | **ADD DIAMPEERADDR** | IPv4地址（IPV4ADDRESS） | 10.11.21.59<br>10.11.21.60 | 全网规划 | 增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。 |
  | **ADD DIAMPEERADDR** | 端口号（PORT） | 3868 | 全网规划 | 增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR: HOSTNAME="ocs1", ADDRTYPE=IPv4, IPV4ADDRESS="10.11.21.59", PORT=3868;`
- 操作步骤上下文（±2 行原文）：
  L105:
    >     b. Diameter链路信息。
    >       **ADD DIAMCONNGRP**
    >       **ADD DIAMPEERADDR**
    >       **ADD DIAMCONNECTION**
    >       > **说明**
  L174:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR: HOSTNAME="ocs1", ADDRTYPE=IPv4, IPV4ADDRESS="10.11.21.59", PORT=3868;
    >   ```
    >   ```

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMPEERADDR** | 主机名称（HOSTNAME） | ocs_host | 已配置数据中获取 | OCS信息。 |
  | **ADD DIAMPEERADDR** | 地址类型（ADDRTYPE） | IPv4 | 本端规划 | OCS信息。 |
  | **ADD DIAMPEERADDR** | IPv4地址（IPV4ADDRESS） | 192.168.40.10 | 全网规划 | OCS信息。 |
  | **ADD DIAMPEERADDR** | 端口号（PORT） | 3868 | 全网规划 | OCS信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR: HOSTNAME="ocs_host", ADDRTYPE=IPv4, IPV4ADDRESS="192.168.40.10";`
- 操作步骤上下文（±2 行原文）：
  L167:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR: HOSTNAME="ocs_host", ADDRTYPE=IPv4, IPV4ADDRESS="192.168.40.10";
    >   ```
    >   ```

**md：`WSFD-109001/配置OCS Failover功能_95923411.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMPEERADDR** | 主机名称（HOSTNAME） | ocs_host1<br>ocs_host2 | 已配置数据中获取 | 增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。 |
  | **ADD DIAMPEERADDR** | 地址类型（ADDRTYPE） | IPv4 | 本端规划 | 增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。 |
  | **ADD DIAMPEERADDR** | IPv4地址（IPV4ADDRESS） | 10.11.21.59<br>10.11.21.60 | 全网规划 | 增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。 |
  | **ADD DIAMPEERADDR** | 端口号（PORT） | 3868 | 全网规划 | 增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host1",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.59";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host2",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.60";`
- 操作步骤上下文（±2 行原文）：
  L60:
    >       **ADD OCS**
    >     b. 配置Diameter链路对端的OCS地址信息。
    >       **ADD DIAMPEERADDR**
    >     c. 配置OCS组。
    >       **ADD OCSGROUP**
  L118:
    > 
    > ```
    > ADD DIAMPEERADDR:HOSTNAME="ocs_host1",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.59";
    > ```
    > 
  L122:
    > 
    > ```
    > ADD DIAMPEERADDR:HOSTNAME="ocs_host2",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.60";
    > ```
    > 

**md：`WSFD-109001/配置OCS负荷分担_95923468.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMPEERADDR** | 主机名称（HOSTNAME） | ocs_host1<br>ocs_host2<br>ocs_host3<br>ocs_host4 | 已配置数据中获取 | OCS信息。 |
  | **ADD DIAMPEERADDR** | 地址类型（ADDRTYPE） | IPv4 | 本端规划 | OCS信息。 |
  | **ADD DIAMPEERADDR** | IPv4地址（IPV4ADDRESS） | 192.168.40.10<br>192.168.40.11<br>192.168.40.12<br>192.168.40.13 | 全网规划 | OCS信息。 |
  | **ADD DIAMPEERADDR** | 端口号（PORT） | 3868 | 全网规划 | OCS信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host1",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.10";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host2",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.11";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host3",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.12";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host4",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.13";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host5",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.14";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host5",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.15";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host5",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.16";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host5",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.17";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host1",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.10";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host2",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.11";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host3",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.12";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host4",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.13";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host1",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.10";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host2",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.11";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host3",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.12";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host4",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.13";`
- 操作步骤上下文（±2 行原文）：
  L132:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="ocs_host1",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.10";
    >   ```
    >   ```
  L135:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="ocs_host2",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.11";
    >   ```
    >   ```
  L138:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="ocs_host3",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.12";
    >   ```
    >   ```

**md：`WSFD-109001/配置基于CC+用户号段选择OCS_95923602.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMPEERADDR** | 主机名称（HOSTNAME） | ocs_host1<br>ocs_host2<br>ocs_host3<br>ocs_host4 | 已配置数据中获取 | OCS信息。 |
  | **ADD DIAMPEERADDR** | 地址类型（ADDRTYPE） | IPv4 | 本端规划 | OCS信息。 |
  | **ADD DIAMPEERADDR** | IPv4地址（IPV4ADDRESS） | 192.168.40.10<br>192.168.40.11<br>192.168.40.12<br>192.168.40.13 | 全网规划 | OCS信息。 |
  | **ADD DIAMPEERADDR** | 端口号（PORT） | 3868 | 全网规划 | OCS信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host1",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.10";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host2",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.11";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host3",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.12";`
  `ADD DIAMPEERADDR:HOSTNAME="ocs_host4",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.13";`
- 操作步骤上下文（±2 行原文）：
  L132:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="ocs_host1",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.10";
    >   ```
    >   ```
  L135:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="ocs_host2",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.11";
    >   ```
    >   ```
  L138:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="ocs_host3",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.40.12";
    >   ```
    >   ```

**md：`WSFD-109001/调测到OCS的数据_95923404.md`**
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="HUAWEIocs",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.5.118";`
- 操作步骤上下文（±2 行原文）：
  L113:
    >       ```
    >       ```
    >       ADD DIAMPEERADDR:HOSTNAME="HUAWEIocs",ADDRTYPE=IPv4,IPV4ADDRESS="192.168.5.118";
    >       ```
    >       CEA中携带的origin-host是huawei，如 [图2](#ZH-CN_OPI_0295923404__fig2) 所示。

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)**
    > - **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    > - **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    > - **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | IPv4 | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | IPv4地址（IPV4ADDRESS） | 10.10.0.1<br>10.10.0.2<br>10.10.10.1<br>10.10.10.2 | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | endpoint0<br>endpoint1<br>endpoint2<br>endpoint3 | 与对端协商 | DRA绑定的SCTP端点已经通过<br>**[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>命令查询。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.0.1";`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.0.2";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2";`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint0";`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint1";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint2";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint3";`
- 操作步骤上下文（±2 行原文）：
  L151:
    >     b. 配置DRA主机名以及地址信息。
    >       **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**
    >       **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    >       > **说明**
    >       > - 只有App与IP/SCTP都配置才会生效。
  L155:
    >       > - 只有App与IP/SCTP都配置才会生效。
    >       > - 对于同一个DRA，不允许同时配置IP地址和SCTP端点。
    >       >     - 如果配置IP地址，则**[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**中ADDRTYPE需要配置为IPv4，且需要在IPV4ADDRESS中输入对应的IPv4地址；
    >       >     - 如果配置SCTP端点，则**[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**ADDRTYPE需要配置为SCTP，且需要再SCTPENDPOINT中输入对应的SCTP端点名称。
    >       > - DRA与Diameter实体PCRF/OCS/AAA的主机名不能重复。
  L156:
    >       > - 对于同一个DRA，不允许同时配置IP地址和SCTP端点。
    >       >     - 如果配置IP地址，则**[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**中ADDRTYPE需要配置为IPv4，且需要在IPV4ADDRESS中输入对应的IPv4地址；
    >       >     - 如果配置SCTP端点，则**[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**ADDRTYPE需要配置为SCTP，且需要再SCTPENDPOINT中输入对应的SCTP端点名称。
    >       > - DRA与Diameter实体PCRF/OCS/AAA的主机名不能重复。
    >     c. 配置到DRA的链路组信息。

### WSFD-011133

**md：`WSFD-011133/WSFD-011133 Gy over DRA参考信息_29725462.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)**
    > - **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    > - **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > - **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**

**md：`WSFD-011133/实现原理_30001131.md`**
- 操作步骤上下文（±2 行原文）：
  L74:
    > 下面以 GGSN/PGW-C 同时与OCS、DRA对接为例，介绍首条Diameter消息发送时的路径选择过程。如 [图3](#ZH-CN_CONCEPT_0230001131__fig372172520419) 所示， GGSN/PGW-C 配置了主备OCS Group，主OCS Group中有2个OCS：1个直连1个非直连，备OCS Group中有2个OCS：2个直连。 GGSN/PGW-C 在主备OCS Group中选择OCS，如果与直连OCS之间的Diameter链路不可用，可以基于该直连OCS的Realm查找Diameter路由，选择DRA进行Diameter消息的发送。
    > 
    > - 直连OCS：通过**[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**和**[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**命令配置了Realm和IP地址的OCS。
    > - 非直连OCS：通过**[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**命令配置了Realm但未配置IP地址的OCS。
    > 

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 已通过<br>**[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**<br>命令配置。 |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型<br>（ADDRTYPE） | SCTP | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | endpoint0<br>endpoint1 | 已配置数据中获取 | 已通过<br>**[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>配置。 |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 已通过<br>**[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**<br>命令配置。 |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | IPv4地址（IPV4ADDRESS） | 10.10.10.1<br>10.10.10.2<br>10.10.11.1<br>10.10.11.2 | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 端口号（PORT） | 3396<br>3397 | 全网规划 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型<br>（ADDRTYPE） | IPv4 | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | ocs1<br>ocs4 | 已配置数据中获取 | 已通过<br>**[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**<br>命令配置。 |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | IPv4地址（IPV4ADDRESS） | 10.11.21.1<br>10.11.21.2 | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 端口号（PORT） | 3868 | 全网规划 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型<br>（ADDRTYPE） | IPv4 | 与对端协商 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="ocs1",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.1",PORT=3868;`
  `ADD DIAMPEERADDR:HOSTNAME="ocs4",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.2",PORT=3868;`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1",PORT=3396;`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2",PORT=3397;`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.11.1",PORT=3396;`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.11.2",PORT=3397;`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint0";`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint1";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint2";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint3";`
- 操作步骤上下文（±2 行原文）：
  L146:
    >           - 配置DRA主机名以及地址信息。
    >             **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**
    >             **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    >             > **说明**
    >             > 对于同一个DRA，不允许同时配置IP地址和SCTP端点。
  L219:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="ocs1",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.1",PORT=3868;
    >   ```
    >   ```
  L222:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="ocs4",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.2",PORT=3868;
    >   ```
    >   ```

**md：`WSFD-011133/调测Gy over DRA_29725461.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 
    > 1. 断开 GGSN/PGW-C 与OCS1、OCS4的连接，例如删除 GGSN/PGW-C 到OCS的路由，这里主要调测经DRA转交Diameter消息的场景。调测结束后，请恢复 GGSN/PGW-C 与OCS1、OCS4的连接。
    > 2. 在OM Portal上创建Gy接口跟踪，在“对端IP地址”栏输入DRA的IP地址（ **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** 命令指定的 “SEQUENCE” 值最小的DRA ， **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的第一个DRA的IP地址）。
    > 3. 测试终端使用APN“apn-test”接入网络，用户访问业务。
    > 4. 查看消息跟踪，观察 GGSN/PGW-C 是否向DRA发送了CCR消息，如 [图1](#ZH-CN_OPI_0229725461__fig1) 所示。

### WSFD-011134

**md：`WSFD-011134/激活S6b over DRA（静态路由+BFD组网）_75821602.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | IPv4 | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | IPv4地址（IPV4ADDRESS） | 10.10.10.1<br>10.10.10.2<br>10.10.11.1<br>10.10.11.2 | 对端获取 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | - |
  | **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | endpoint0<br>endpoint1<br>endpoint2<br>endpoint3 | 与对端协商 | DRA绑定的SCTP端点已经通过<br>[**ADD SCTPENDPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)<br>命令配置，可以使用<br>[**LST SCTPENDPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)<br>命令查询。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1";`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.11.1";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.11.2";`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint0";`
  `ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint1";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint2";`
  `ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint3";`
- 操作步骤上下文（±2 行原文）：
  L128:
    >     b. 配置DRA主机名以及地址信息。
    >       [**ADD DRA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)
    >       [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    >       > **说明**
    >       > - 对于同一个DRA，不允许同时配置IP地址和SCTP端点。
  L203:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1";
    >   ```
    >   ```
  L206:
    >   ```
    >   ```
    >   ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2";
    >   ```
    >   ```

**md：`WSFD-011134/调测S6b over DRA_75821603.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > ## [操作步骤](#ZH-CN_OPI_0275821603)
    > 
    > 1. 在OM Portal上创建S6b接口跟踪，在“对端IP地址”栏输入DRA的IP地址（ [**ADD DIAMRTNEXTHOP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md) 命令指定的 “SEQUENCE” 值最小的DRA ， [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) 命令配置的第一个DRA的IP地址）。
    > 2. 测试终端使用APN“apn-test”接入网络，用户访问业务。
    > 3. 查看消息跟踪，观察 GGSN/PGW-C 是否向DRA发送了AAR消息，如 [图1](#ZH-CN_OPI_0275821603__fig1) 所示。

## ④ 自动比对
- 命令真相参数（6）：['ADDRTYPE', 'HOSTNAME', 'IPV4ADDRESS', 'IPV6ADDRESS', 'PORT', 'SCTPENDPOINT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 17, '与对端协商': 17, '本端规划': 7, '全网规划': 14, '对端获取': 1}（多值→atom 应考虑 decision_driven）
