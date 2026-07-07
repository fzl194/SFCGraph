# 命令证据包：ADD DIAMCONNECTION
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用于增加Diameter链路。

根据网络规划，需要增加UNC到对端网元的一条Diameter链路时，可以在执行完ADD DIAMPEERADDR和ADD DIAMCONNGRP等命令后，执行此命令增加Diameter链路。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为3000。
- 对于同一对ConnGrp和LocInterface，允许多条记录存在，每条记录的地址必须不同。
- 指定地址时，系统根据配置生成一条记录，如果配置重复，则配置失败。
- 配置DiamConnection之后，再增加Addr不会自动增加链路，而是必须配置DiamConnection才会建链。
- 指定地址但不指定对端端口号时，系统根据

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| DIAMCONNGRP | Diameter链路组名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| LOCINTERFACE | 本端接口名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| PEERADDRTYPE | 对端地址类型 | 对端协商 | optional | 无 | 枚举类型。 |
| PEERIPV4ADDR | 对端IPv4地址 | 对端协商 | conditional | 无 | IPv4地址类型。不支持0.0.0.0和255.255.255.255。 |
| PEERIPV6ADDR | 对端IPv6地址 | 对端协商 | conditional | 无 | IPv6地址类型。不支持全F。 |
| PEERPORT | 对端端口号 | 对端协商 | conditional | 无 | 整数类型，取值范围为1～65534。 |
| PEERSCTPENDPT | 对端SCTP端点名称 | 对端协商 | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| REVERSEIP | SCTP建链交换本端IP地址 | 对端协商 | conditional | DISABLE | 枚举类型。 |
| LOCALPORT | 本端端口 | local_planned | optional | 0 | 整数类型，取值范围为0，13200～13263，16400～16463，19765～19784。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b",LOCINTERFACE="S6bif1/0/0",LOCALPORT=19765,PEERADDRTYPE=SCTP,PEERSCTPENDPT="dc1_AAA01-S6B-SCTPEP01";`
- 操作步骤上下文（±2 行原文）：
  L94:
    >   [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > 11. 配置到3GPP AAA Server的链路。
    >   [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    >     - 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)中的“PEERADDRTYPE”根据实际规划配置为“PEERIPV4ADDR”或“PEERIPV6ADDR”。
    >     - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)中的“PEERADDRTYPE”配置为“SCTP”，“PEERSCTPENDPT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
  L95:
    > 11. 配置到3GPP AAA Server的链路。
    >   [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    >     - 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)中的“PEERADDRTYPE”根据实际规划配置为“PEERIPV4ADDR”或“PEERIPV6ADDR”。
    >     - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)中的“PEERADDRTYPE”配置为“SCTP”，“PEERSCTPENDPT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
    >   > **说明**
  L96:
    >   [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    >     - 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)中的“PEERADDRTYPE”根据实际规划配置为“PEERIPV4ADDR”或“PEERIPV6ADDR”。
    >     - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)中的“PEERADDRTYPE”配置为“SCTP”，“PEERSCTPENDPT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
    >   > **说明**
    >   > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    > - [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    > - [**SET PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    > - [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | Diameter链路组名（DIAMCONNGRP） | dconn_pcrf1<br>dconn_pcrf2 | 已配置数据中获取 | 增加Diameter链路。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端接口名（LOCINTERFACE） | gxif1/0/0<br>gxif1/0/1 | 已配置数据中获取 | 增加Diameter链路。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 对端地址类型（PEERADDRTYPE） | IPv4 | 与对端协商 | 增加Diameter链路。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 对端IPv4地址（PEERIPV4ADDR） | 10.11.21.59<br>10.11.21.60<br>10.11.21.61 | 与对端协商 | 增加Diameter链路。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端端口（LOCALPORT） | 16450<br>16451 | 本端规划 | [**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)<br>命令中的<br>“GXCONCENMODE”<br>为<br>“LOCALPORT”<br>时，此处必须配置<br>“本端端口”<br>为非0的有效值；否则不配置<br>“本端端口”<br>或配置为<br>“0”<br>。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | Diameter链路组名（DIAMCONNGRP） | dconn_pcrf1<br>dconn_pcrf2<br>dconn_pcrf3<br>dconn_pcrf4 | 已配置数据中获取 | 增加Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端接口名（LOCINTERFACE） | gxif1/0/0<br>gxif1/0/1 | 已配置数据中获取 | 增加Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 对端地址类型（PEERADDRTYPE） | IPv4 | 与对端协商 | 增加Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 对端IPv4地址（PEERIPV4ADDR） | 10.11.21.59<br>10.11.21.60<br>10.11.21.61 | 与对端协商 | 增加Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
  | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端端口（LOCALPORT） | 16450<br>16451 | 本端规划 | [**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)<br>命令中的<br>“GXCONCENMODE”<br>为<br>“LOCALPORT”<br>时，此处必须配置<br>“本端端口”<br>为非0的有效值；否则不配置<br>“本端端口”<br>或配置为<br>“0”<br>。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf1",LOCINTERFACE="gxif1/0/0",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.59",LOCALPORT=16450;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf2",LOCINTERFACE="gxif1/0/1",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.60",LOCALPORT=16451;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf2",LOCINTERFACE="gxif1/0/1",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.61",LOCALPORT=16451;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf1",LOCINTERFACE="gxif1/0/0",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.59",LOCALPORT=16450;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf2",LOCINTERFACE="gxif1/0/1",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.60",LOCALPORT=16451;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf2",LOCINTERFACE="gxif1/0/1",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.61",LOCALPORT=16451;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf3",LOCINTERFACE="gxif1/0/0",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.59",LOCALPORT=16450;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf4",LOCINTERFACE="gxif1/0/1",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.60",LOCALPORT=16451;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf4",LOCINTERFACE="gxif1/0/1",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.61",LOCALPORT=16451;`
- 操作步骤上下文（±2 行原文）：
  L147:
    >   [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > 9. 配置到PCRF的链路。
    >   [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    >   > **说明**
    >   > - 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
  L150:
    >   > **说明**
    >   > - 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >   > - 当“Gx集中点模式”通过[**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)命令选择为“LOCALPORT”时，可使用[**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)命令设置本端的端口号。
    >   **同一PGW-C对接多个PGW-U，且不同PGW-U下的用户IP存在相同时，必须执行 [步骤 10](#ZH-CN_OPI_0230805096__step38911553714) ~ [步骤 16](#ZH-CN_OPI_0230805096__step3536110122512) ；IP地址不同时，可不配置 [步骤 10](#ZH-CN_OPI_0230805096__step38911553714) ~ [步骤 16](#ZH-CN_OPI_0230805096__step3536110122512) 。**
    > 10. 配置Diameter本端主机组。
  L247:
    >   ```
    >   ```
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_pcrf1",LOCINTERFACE="gxif1/0/0",PEERADDRTYPE=IPv4,PEERIPV4ADDR="10.11.21.59",LOCALPORT=16450;
    >   ```
    >   ```

**md：`WSFD-109101/调测到PCRF的数据_31422954.md`**
- 操作步骤上下文（±2 行原文）：
  L152:
    > 6. 修改GGSN/PGW-C的Gx口设备标识。
    >     a. 执行[**RMV DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/删除Diameter链路（RMV DIAMCONNECTION）_09897268.md)和[**RMV DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.md)命令，删除原有配置。
    >     b. 执行[**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)和[**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)命令，按照规划数据重新配置GGSN/PGW-C的Gx口设备标识。
    >     c. **可选：**如果Gx接口IP与规划值不一致，请执行[**RMV LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/删除逻辑接口（RMV LOGICINF）_09896725.md)命令，删除原有配置。
    >     d. **可选：**执行[**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)命令，按照规划数据重新配置GGSN/PGW-C的Gx接口IP数据。

### WSFD-104508

**md：`WSFD-104508/WSFD-104508 SCTP参考信息_29341126.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    > - **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > - **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    > 
    > #### [告警](#ZH-CN_CONCEPT_0229341126)

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | Diameter链路组名 | dconn_gx | 已配置数据中获取 | 已经通过<br>**[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**<br>命令配置，可以使用<br>**[LST DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/查询Diameter链路组（LST DIAMCONNGRP）_09897264.md)**<br>查询。 |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端接口名（LOCINTERFACE） | gxif1/0/0 | 已配置数据中获取 | 已经通过<br>**[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**<br>命令配置，可以使用<br>**[LST LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/查询逻辑接口（LST LOGICINF）_09896726.md)**<br>查询。 |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端端口（LOCALPORT） | 16400 | 本端规划 | - |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 对端SCTP端点名称（PEERSCTPENDPT） | pcrfendb<br>pcrfendc | 已配置数据中获取 | SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 对端地址类型（PEERADDRTYPE） | SCTP | 与对端协商 | - |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | SCTP建链交换本端IP地址（REVERSEIP） | ENABLE | 与对端协商 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx",LOCINTERFACE="gxif1/0/0",LOCALPORT=16400,PEERADDRTYPE=SCTP,PEERSCTPENDPT="pcrfendb";`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx",LOCINTERFACE="gxif1/0/0",LOCALPORT=16400,PEERADDRTYPE=SCTP,PEERSCTPENDPT="pcrfendc";`
- 操作步骤上下文（±2 行原文）：
  L113:
    >   **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > 12. 建立本端到对端SCTP端点的链路。
    >   **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    >   > **说明**
    >   > 当 “Gx集中点模式” 通过 **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，支持使用 **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
  L115:
    >   **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    >   > **说明**
    >   > 当 “Gx集中点模式” 通过 **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，支持使用 **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    > 
    > ## [验证方法](#ZH-CN_OPI_0230442391)
  L201:
    > 
    > ```
    > ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx",LOCINTERFACE="gxif1/0/0",LOCALPORT=16400,PEERADDRTYPE=SCTP,PEERSCTPENDPT="pcrfendb";
    > ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx",LOCINTERFACE="gxif1/0/0",LOCALPORT=16400,PEERADDRTYPE=SCTP,PEERSCTPENDPT="pcrfendc";
    > ```

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | Diameter链路组名 | dconn_gy | 已配置数据中获取 | 已经通过<br>**[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**<br>命令配置，可以使用<br>**[LST DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/查询Diameter链路组（LST DIAMCONNGRP）_09897264.md)**<br>查询。 |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端接口名（LOCINTERFACE） | gyif1/0/0 | 已配置数据中获取 | 已经通过<br>[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>命令配置，可以使用<br>[**LST LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/查询逻辑接口（LST LOGICINF）_09896726.md)<br>查询。 |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端端口（LOCALPORT） | 13200 | 本端规划 | - |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 对端SCTP端点名称（PEERSCTPENDPT） | ocsend | 已配置数据中获取 | SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 对端地址类型（PEERADDRTYPE） | SCTP | 与对端协商 | - |
  | **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | SCTP建链交换本端IP地址（REVERSEIP） | ENABLE | 与对端协商 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gy",LOCINTERFACE="gyif1/0/0",LOCALPORT=13200,PEERADDRTYPE=SCTP,PEERSCTPENDPT="ocsend";`
- 操作步骤上下文（±2 行原文）：
  L110:
    >   **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > 12. 建立本端到对端SCTP端点的链路。
    >   **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    >   > **说明**
    >   > 当 “Gy集中点模式” 通过 **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，支持使用 **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
  L112:
    >   **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    >   > **说明**
    >   > 当 “Gy集中点模式” 通过 **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，支持使用 **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    > 
    > ## [验证方法](#ZH-CN_OPI_0230602207)
  L192:
    > 
    > ```
    > ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gy",LOCINTERFACE="gyif1/0/0",LOCALPORT=13200,PEERADDRTYPE=SCTP,PEERSCTPENDPT="ocsend";
    > ```

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    > - [**ADD OCSGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)
    > - [**ADD OCSBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    > - [**ADD OCSGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)
    > - [**ADD OCSBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMCONNECTION** | Diameter链路组名（DIAMCONNGRP） | dia1<br>dia2 | 已配置数据中获取 | 增加Diameter链路。 |
  | **ADD DIAMCONNECTION** | 本端接口名（LOCINTERFACE） | Gyif1/0/1 | 已配置数据中获取 | 增加Diameter链路。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNECTION: DIAMCONNGRP="dia1", LOCINTERFACE="Gyif1/0/0"`
- 操作步骤上下文（±2 行原文）：
  L106:
    >       **ADD DIAMCONNGRP**
    >       **ADD DIAMPEERADDR**
    >       **ADD DIAMCONNECTION**
    >       > **说明**
    >       > 当 “Gy集中点模式” 通过 **SET CONCENPOINT** 命令选择为 “LOCALPORT” 时，可使用 **ADD DIAMCONNECTION** 命令设置本端的端口号。
  L108:
    >       **ADD DIAMCONNECTION**
    >       > **说明**
    >       > 当 “Gy集中点模式” 通过 **SET CONCENPOINT** 命令选择为 “LOCALPORT” 时，可使用 **ADD DIAMCONNECTION** 命令设置本端的端口号。
    >     c. 配置在线计费系统的OCS组。
    >       **ADD OCSGROUP**
  L177:
    >   ```
    >   ```
    >   ADD DIAMCONNECTION: DIAMCONNGRP="dia1", LOCINTERFACE="Gyif1/0/0"
    >   , LOCALPORT=13201
    >   , PEERADDRTYPE=IPv4, PEERIPV4ADDR="10.11.21.59", PEERPORT=3868;

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    > - **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    > - **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
    > - **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | Diameter链路组名 | dconn_gx1<br>dconn_gx2 | 本端规划 | - |
  | **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端接口名（LOCINTERFACE） | gxif1/0/0 | 本端规划 | - |
  | **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端端口（LOCALPORT） | 16401<br>16402 | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx2",LOCINTERFACE="gxif1/0/0",LOCALPORT=16402;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401,PEERADDRTYPE=SCTP,PEERSCTPENDPT="endpoint0";`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401,PEERADDRTYPE=SCTP,PEERSCTPENDPT="endpoint1";`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx2",LOCINTERFACE="gxif1/0/0",LOCALPORT=16402,PEERADDRTYPE=SCTP,PEERSCTPENDPT="endpoint2";`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx2",LOCINTERFACE="gxif1/0/0",LOCALPORT=16402,PEERADDRTYPE=SCTP,PEERSCTPENDPT="endpoint3";`
- 操作步骤上下文（±2 行原文）：
  L161:
    >       **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    >     d. 配置到DRA的链路。
    >       **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    >       > **说明**
    >       > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
  L165:
    >       > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >       >
    >       > 当 “Gx集中点模式” 通过 **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，可使用 **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    >     e. 配置PCRF域的Diameter路由。
    >       **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
  L251:
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx1",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host1.example.com",SELECTMODE=SESSION_ID;
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx2",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host2.example.com",SELECTMODE=SESSION_ID;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx2",LOCINTERFACE="gxif1/0/0",LOCALPORT=16402;
    >   ADD DIAMRTREALM:REALMNAME="pcrf.huawei.com",APPLICATION=GX,SELECTMODE=MASTER_SLAVE;

### WSFD-011133

**md：`WSFD-011133/WSFD-011133 Gy over DRA参考信息_29725462.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    > - **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > - **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    > - **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
    > - **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)**

**md：`WSFD-011133/实现原理_30001131.md`**
- 操作步骤上下文（±2 行原文）：
  L51:
    > #### [Diameter链路建立与维护](#ZH-CN_CONCEPT_0230001131)
    > 
    > GGSN/PGW-C 与OCS或DRA之间的Diameter链路可以建立多条，基于TCP协议的链路通过IP+Port区分（如 [图2](#ZH-CN_CONCEPT_0230001131__fig1146711923820) 所示），基于SCTP协议的通过Endpoint区分。支持通过 **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令指定Gy接口与指定对端IP+Port建立Diameter链路。
    > 
    > **图2** Diameter链路建立方式（以TCP协议为例）
  L118:
    >     - 手工静态配置Realm：无法获取到IMSI时（例如紧急呼叫用户）需要使用该种方式。
    > 2. 基于Realm选择Diameter路由，Diameter路由可以通过 **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)** 命令的 **SELECTMODE** 参数配置为主备或负荷分担。
    >     - 互为主备的Diameter路由：GGSN/PGW-C优先选择主用Diameter路由，当检测到主用路由故障时，GGSN/PGW-C再选择备用Diameter路由重发消息。通过**[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** 命令指定的 “SEQUENCE” 数值最小的DRA为主用，其他DRA都为备用；通过**[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**命令配置的第一条DRA的Diameter链路为主用链路，其他链路为备用。
    >     - 互为负荷分担的Diameter路由：GGSN/PGW-C支持基于Session-id（用户粒度）或基于Round-robin（消息粒度）进行Diameter路由的负荷分担选择。
    > 

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_dra1<br>dconn_dra2 | 本端规划 | 配置链路信息、端口。 |
  | **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端接口名（LOCINTERFACE） | gyif1/0/0<br>gyif1/0/1 | 本端规划 | 配置链路信息、端口。 |
  | **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端端口（LOCALPORT） | 13201<br>13202 | 本端规划 | “13201”对应gyif1/0/0接口的端口号，“13202”对应gyif1/0/1接口的端口号。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra1",LOCINTERFACE="gyif1/0/0",LOCALPORT=13201;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra2",LOCINTERFACE="gyif1/0/1",LOCALPORT=13202;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra1",LOCINTERFACE="gyif1/0/0",LOCALPORT=13201;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra2",LOCINTERFACE="gyif1/0/1",LOCALPORT=13202;`
- 操作步骤上下文（±2 行原文）：
  L152:
    >             **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    >           - 配置到DRA的链路。
    >             **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    >             > **说明**
    >             > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
  L156:
    >             > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >             >
    >             > 当 “Gy集中点模式” 通过 **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，可使用 **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    >     d. 配置Diameter路由。
    >       **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
  L269:
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra1",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host1.example.com",SELECTMODE=MASTER_SLAVE;
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra2",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host2.example.com",SELECTMODE=MASTER_SLAVE;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra1",LOCINTERFACE="gyif1/0/0",LOCALPORT=13201;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra2",LOCINTERFACE="gyif1/0/1",LOCALPORT=13202;
    >   ADD DIAMRTREALM:REALMNAME="ocs.huawei.com",APPLICATION=GY,SELECTMODE=MASTER_SLAVE;

### WSFD-011134

**md：`WSFD-011134/实现原理_75821601.md`**
- 操作步骤上下文（±2 行原文）：
  L69:
    > Diameter链路组内的Diameter链路间可以通过 [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) / [**MOD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/修改Diameter链路组（MOD DIAMCONNGRP）_09897262.md) 命令配置为主备（MASTER_SLAVE）或负荷分担（SESSION_ID、ROUND_ROBIN）。
    > 
    > - 互为主备的Diameter链路：GGSN/PGW-C优先选择主用Diameter链路，当检测到主用Diameter链路故障时，GGSN/PGW-C再选择备用Diameter链路重发消息。GGSN/PGW-C与通过[**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)配置的第一条DRA的Diameter链路为主用Diameter链路。
    > - 互为负荷分担的Diameter链路：GGSN/PGW-C支持基于session-id（用户粒度）或基于round-robin（消息粒度）进行Diameter链路的负荷分担选择。
    > 

**md：`WSFD-011134/激活S6b over DRA（静态路由+BFD组网）_75821602.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | Diameter链路组名 | dconn_s6b1<br>dconn_s6b2 | 本端规划 | - |
  | [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端接口名（LOCINTERFACE） | s6bif1/0/0<br>s6bif1/0/1 | 本端规划 | - |
  | [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端端口号（LOCALPORT） | 19766<br>19767 | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b1",LOCINTERFACE="s6bif1/0/0",LOCALPORT=19766;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b2",LOCINTERFACE="s6bif1/0/1",LOCALPORT=19767;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b1",LOCINTERFACE="s6bif1/0/0",LOCALPORT=19766;`
  `ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b2",LOCINTERFACE="s6bif1/0/1",LOCALPORT=19767;`
- 操作步骤上下文（±2 行原文）：
  L135:
    >       [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    >     d. 配置到DRA的链路。
    >       [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    >       > **说明**
    >       > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
  L139:
    >       > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
    >       >
    >       > 当 “S6b集中点模式” 通过 [**SET CONCENPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) 命令选择为 “LOCALPORT” 时，可使用 [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) 命令设置本端的端口号。
    >     e. 配置Diameter路由。
    >       [**ADD DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)
  L230:
    >   ```
    >   ```
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b1",LOCINTERFACE="s6bif1/0/0",LOCALPORT=19766;
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（9）：['DIAMCONNGRP', 'LOCALPORT', 'LOCINTERFACE', 'PEERADDRTYPE', 'PEERIPV4ADDR', 'PEERIPV6ADDR', 'PEERPORT', 'PEERSCTPENDPT', 'REVERSEIP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 12, '与对端协商': 8, '本端规划': 13}（多值→atom 应考虑 decision_driven）
