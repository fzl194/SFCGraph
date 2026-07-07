# 命令证据包：ADD DIAMCONNGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。本端主机名，对端主机名唯一确定了一组Diameter链路。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 配置LOCALHOSTNAME需要保证已经配置了Local Info。
- 配置PEERHOSTNAME时，需要保证已经配置了与APPLICATION对应类型的服务器。
- APPLICATION和对端主机名的应用类型必须一致。
- PEERHOSTNAME和LOCALHOSTNAME不能重复。
- 每个Peer与Gx/Gy应用最多

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CONNGROUPNAME | Diameter链路组名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| LOCALHOSTNAME | 本端主机名 | global_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。 |
| APPLICATION | Diameter应用 | global_planned | required | 无 | 枚举类型。 |
| PEERHOSTNAME | 对端主机名 | global_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。 |
| SELECTMODE | 链路选择模式 | global_planned | optional | SESSION_ID | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNGRP: CONNGROUPNAME="dconn_s6b",LOCALHOSTNAME="unc_1",APPLICATION=S6b,PEERHOSTNAME="3gppaaa";`
- 操作步骤上下文（±2 行原文）：
  L92:
    >     - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”配置为“SCTP”，“SCTPENDPOINT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
    >   [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > 11. 配置到3GPP AAA Server的链路。
    >   [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
  L163:
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
    >   ```
    >   ADD DIAMCONNGRP: CONNGROUPNAME="dconn_s6b",LOCALHOSTNAME="unc_1",APPLICATION=S6b,PEERHOSTNAME="3gppaaa";
    >   ```
    > 11. 配置到3GPP AAA Server的链路。

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    > - [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    > - [**SET PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)

**md：`WSFD-109101/实现原理_29056158.md`**
- 操作步骤上下文（±2 行原文）：
  L97:
    > #### [链路可靠性-多Diameter链路](#ZH-CN_TOPIC_0229056158)
    > 
    > UNC 支持与一个PCRF的多个IP或多个SCTP端点建立多条直连Diameter链路，构成一个链路组，链路组内的多条链路间支持主备或负荷分担模式（链路选择模式通过 [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) 命令中的 “SELECTMODE” 参数来设置）。当链路组内的一条链路故障时， UNC 选择链路组内的其他可用链路进行消息交互，增强信令组网的可靠性。
    > 
    > UNC 支持通过TCP或SCTP协议来承载Diameter协议，可以分别构建多Diameter链路：

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | Diameter链路组名（CONNGROUPNAME） | dconn_pcrf1<br>dconn_pcrf2 | 本端规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 本端主机名（LOCALHOSTNAME） | pgwc_1 | 全网规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | Diameter应用（APPLICATION） | GX | 本端规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 对端主机名（PEERHOSTNAME） | pcrf_1<br>pcrf_2 | 本端规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 链路选择模式（SELECTMODE） | SESSION_ID<br>ROUND-ROBIN | 全网规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | Diameter链路组名（CONNGROUPNAME） | dconn_pcrf1<br>dconn_pcrf2<br>dconn_pcrf3<br>dconn_pcrf4 | 本端规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 本端主机名（LOCALHOSTNAME） | pgwc_1<br>pgwc_2 | 全网规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | Diameter应用（APPLICATION） | GX | 本端规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 对端主机名（PEERHOSTNAME） | pcrf_1<br>pcrf_2 | 本端规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
  | [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 链路选择模式（SELECTMODE） | SESSION_ID<br>ROUND-ROBIN | 全网规划 | 该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。<br>本端主机名有2个或多个时使用。<br>例如，CU Full Mesh组网中，同一SGW-C\PGW-C接入2个SGW-U\PGW-U组，且这2个SGW-U\PGW-U组下的用户存在相同IP时，每对接一个PCRF，需要规划2个Diameter链路组。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_pcrf1",LOCALHOSTNAME="pgw_1",APPLICATION=GX,PEERHOSTNAME="pcrf_1",SELECTMODE=SESSION_ID;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_pcrf2",LOCALHOSTNAME="pgw_1",APPLICATION=GX,PEERHOSTNAME="pcrf_2",SELECTMODE=ROUND_ROBIN;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_pcrf1",LOCALHOSTNAME="pgwc_1",APPLICATION=GX,PEERHOSTNAME="pcrf_1",SELECTMODE=SESSION_ID;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_pcrf2",LOCALHOSTNAME="pgwc_1",APPLICATION=GX,PEERHOSTNAME="pcrf_2",SELECTMODE=ROUND_ROBIN;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_pcrf3",LOCALHOSTNAME="pgwc_2",APPLICATION=GX,PEERHOSTNAME="pcrf_1",SELECTMODE=SESSION_ID;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_pcrf4",LOCALHOSTNAME="pgwc_2",APPLICATION=GX,PEERHOSTNAME="pcrf_2",SELECTMODE=SESSION_ID;`
- 操作步骤上下文（±2 行原文）：
  L145:
    >       [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > 8. 配置到PCRF的链路组信息。
    >   [**ADD DIAMCONNGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > 9. 配置到PCRF的链路。
    >   [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
  L241:
    >   ```
    >   ```
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_pcrf1",LOCALHOSTNAME="pgw_1",APPLICATION=GX,PEERHOSTNAME="pcrf_1",SELECTMODE=SESSION_ID;
    >   ```
    >   ```
  L244:
    >   ```
    >   ```
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_pcrf2",LOCALHOSTNAME="pgw_1",APPLICATION=GX,PEERHOSTNAME="pcrf_2",SELECTMODE=ROUND_ROBIN;
    >   ```
    >   ```

### WSFD-104508

**md：`WSFD-104508/WSFD-104508 SCTP参考信息_29341126.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    > - **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > - **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    > 

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_gx | 本端规划 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 对端主机名（PEERHOSTNAME） | pcrf | 与对端协商 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter应用（APPLICATION） | GX | 全网规划 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 链路选择模式（SELECTMODE） | SESSION_ID | 全网规划 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="pcrf",SELECTMODE=SESSION_ID;`
- 操作步骤上下文（±2 行原文）：
  L98:
    >     b. 重复执行 **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** 命令，配置多个对端端点。
    >       > **说明**
    >       > GGSN/PGW-C可以与一个PCRF的多个SCTP端点间建立多条SCTP偶联，各偶联间为主备还是负荷分担模式通过 **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** 命令中的 “SELECTMODE” 参数来设置。
    > 8. 配置SCTP重传超时（RTO，Retransmission Time-Out）参数，缺省使用初始值；配置SCTP偶联内使用路径的模式，本场景采用全路径模式。
    >   **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)**
  L109:
    >       > **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** 的主机名 “HOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
    >   **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > 11. 配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
  L191:
    > 
    > ```
    > ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="pcrf",SELECTMODE=SESSION_ID;
    > ```
    > 

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_gy | 本端规划 | - |
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | - |
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 对端主机名（PEERHOSTNAME） | ocs | 与对端协商 | - |
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter应用（APPLICATION） | GY | 全网规划 | - |
  | **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 链路选择模式（SELECTMODE） | SESSION_ID | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gy",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="ocs",SELECTMODE=SESSION_ID;`
- 操作步骤上下文（±2 行原文）：
  L95:
    >     b. 重复执行 **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** 命令，配置多个对端端点。
    >       > **说明**
    >       > GGSN/PGW-C可以与一个OCS的多个SCTP端点间建立多条SCTP偶联，各偶联间为主备还是负荷分担模式通过 [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) 命令中的 “SELECTMODE” 参数来设置。
    > 8. 配置SCTP偶联内使用路径的模式，本场景采用全路径模式，即SCTP多归属模式。
    >   **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)**
  L106:
    >       > **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** 的主机名 “OCSHOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
    >   **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > 11. 配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
  L182:
    > 
    > ```
    > ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gy",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="ocs",SELECTMODE=SESSION_ID;
    > ```
    > 

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - [**ADD OCS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - [**ADD OCS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)

**md：`WSFD-109001/OCS组网和链路可靠性_95110432.md`**
- 操作步骤上下文（±2 行原文）：
  L46:
    > #### [链路可靠性-多Diameter链路](#ZH-CN_TOPIC_0295110432)
    > 
    > PGW-C支持与一个OCS的多个IP或多个SCTP端点建立多条直连Diameter链路，构成一个链路组，链路组内的多条链路间支持主备和负荷分担模式 （链路选择模式通过 **ADD DIAMCONNGRP** 命令中的“SELECTMODE”参数来设置） 。当链路组内的一条链路故障时，PGW-C选择链路组内的其他可用链路进行消息交互，增强信令组网的可靠性。
    > 
    > PGW-C支持通过TCP或SCTP协议来承载Diameter协议，可以分别构建多条Diameter链路：

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMCONNGRP** | Diameter链路组名（CONNGROUPNAME） | dia1<br>dia2 | 本端规划 | 该命令用于指定GGSN/PGW-C与指定OCS之间建立一组Diameter链路。 |
  | **ADD DIAMCONNGRP** | 本端主机名（LOCALHOSTNAME） | pgw1 | 全网规划 | 该命令用于指定GGSN/PGW-C与指定OCS之间建立一组Diameter链路。 |
  | **ADD DIAMCONNGRP** | Diameter应用（APPLICATION） | GY | 本端规划 | 该命令用于指定GGSN/PGW-C与指定OCS之间建立一组Diameter链路。 |
  | **ADD DIAMCONNGRP** | 对端主机名（PEERHOSTNAME） | ocs1 | 本端规划 | 该命令用于指定GGSN/PGW-C与指定OCS之间建立一组Diameter链路。 |
  | **ADD DIAMCONNGRP** | 链路选择模式（SELECTMODE） | MASTER_SLAVE | 全网规划 | 该命令用于指定GGSN/PGW-C与指定OCS之间建立一组Diameter链路。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNGRP: CONNGROUPNAME="dia1", LOCALHOSTNAME="pgw1", APPLICATION=GY, PEERHOSTNAME="ocs1"`
- 操作步骤上下文（±2 行原文）：
  L104:
    >       > OCS Server绑定的VPN实例必须和Gy逻辑接口绑定的VPN实例一致。
    >     b. Diameter链路信息。
    >       **ADD DIAMCONNGRP**
    >       **ADD DIAMPEERADDR**
    >       **ADD DIAMCONNECTION**
  L169:
    >   ```
    >   ```
    >   ADD DIAMCONNGRP: CONNGROUPNAME="dia1", LOCALHOSTNAME="pgw1", APPLICATION=GY, PEERHOSTNAME="ocs1"
    >   , SELECTMODE=MASTER_SLAVE
    >   ;

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)**
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**

**md：`WSFD-011132/实现原理_30001130.md`**
- 操作步骤上下文（±2 行原文）：
  L50:
    >   又称为轮选。顺序选择链路组内的链路发送信令，发消息时从上一次成功发送消息的链路开始查找链路组内的下一条链路。当检测到当前使用的链路故障， GGSN/PGW-C 从该链路开始，遍历查找链路组中下一条可用链路，在新选择的链路上发送消息。
    > 
    > 对于直连链路，网关通过 [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) 命令中的参数 **SELECTMODE** ，实现主备或者负荷分担。
    > 
    > 对于非直连链路，因为DRA支持配置多地址(IP地址或者SCTP端点)， GGSN/PGW-C 允许与DRA间建立多条Diameter链路。链路可以是 GGSN/PGW-C 与DRA间建立的TCP链路或是SCTP偶联。不同的非直连链路间，使用主备或者负荷分担。

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_gx1<br>dconn_gx2 | 本端规划 | - |
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | - |
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 对端主机名（PEERHOSTNAME） | host1.example.com<br>host2.example.com | 全网规划 | - |
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter应用（APPLICATION） | GX | 全网规划 | - |
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 链路选择模式（SELECTMODE） | SESSION_ID | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx1",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host1.example.com",SELECTMODE=SESSION_ID;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx2",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host2.example.com",SELECTMODE=SESSION_ID;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx1",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host1.example.com",SELECTMODE=SESSION_ID;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx2",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host2.example.com",SELECTMODE=SESSION_ID;`
- 操作步骤上下文（±2 行原文）：
  L159:
    >       > - DRA与Diameter实体PCRF/OCS/AAA的主机名不能重复。
    >     c. 配置到DRA的链路组信息。
    >       **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    >     d. 配置到DRA的链路。
    >       **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
  L249:
    >   //配置网元对接。
    >   ```
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx1",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host1.example.com",SELECTMODE=SESSION_ID;
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx2",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host2.example.com",SELECTMODE=SESSION_ID;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401;
  L250:
    >   ```
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx1",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host1.example.com",SELECTMODE=SESSION_ID;
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx2",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host2.example.com",SELECTMODE=SESSION_ID;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx2",LOCINTERFACE="gxif1/0/0",LOCALPORT=16402;

### WSFD-011133

**md：`WSFD-011133/WSFD-011133 Gy over DRA参考信息_29725462.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    > - **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    > - **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
    > - **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**

**md：`WSFD-011133/实现原理_30001131.md`**
- 操作步骤上下文（±2 行原文）：
  L121:
    >     - 互为负荷分担的Diameter路由：GGSN/PGW-C支持基于Session-id（用户粒度）或基于Round-robin（消息粒度）进行Diameter路由的负荷分担选择。
    > 
    > 例如 [图5](#ZH-CN_CONCEPT_0230001131__fig194271383457) 中， GGSN/PGW-C 到Realm1的Diameter路由有两条：经DRA1或经DRA2，这两条路由可设置为主备或负荷分担模式。通过查找Diameter路由选定DRA后， GGSN/PGW-C 在与该DRA建立的所有Diameter链路组中选择链路。Diameter链路组内的每个链路间可以通过 **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** 命令的 **SELECTMODE** 参数配置为主备或负荷分担。
    > 
    > **图5** DRA选择

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_dra1<br>dconn_dra2 | 本端规划 | 配置链路组信息。 |
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | 配置链路组信息。 |
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 对端主机名（PEERHOSTNAME） | host1.example.com<br>host2.example.com | 全网规划 | 配置链路组信息。 |
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter应用（APPLICATION） | GY | 全网规划 | 配置链路组信息。 |
  | **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 链路选择模式（SELECTMODE） | MASTER_SLAVE | 全网规划 | 配置链路组信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra1",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host1.example.com",SELECTMODE=MASTER_SLAVE;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra2",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host2.example.com",SELECTMODE=MASTER_SLAVE;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra1",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host1.example.com",SELECTMODE=MASTER_SLAVE;`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra2",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host2.example.com",SELECTMODE=MASTER_SLAVE;`
- 操作步骤上下文（±2 行原文）：
  L150:
    >             > 对于同一个DRA，不允许同时配置IP地址和SCTP端点。
    >           - 配置到DRA的链路组信息。
    >             **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    >           - 配置到DRA的链路。
    >             **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
  L267:
    >   //配置网元对接。
    >   ```
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra1",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host1.example.com",SELECTMODE=MASTER_SLAVE;
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra2",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host2.example.com",SELECTMODE=MASTER_SLAVE;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra1",LOCINTERFACE="gyif1/0/0",LOCALPORT=13201;
  L268:
    >   ```
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra1",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host1.example.com",SELECTMODE=MASTER_SLAVE;
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra2",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host2.example.com",SELECTMODE=MASTER_SLAVE;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra1",LOCINTERFACE="gyif1/0/0",LOCALPORT=13201;
    >   ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra2",LOCINTERFACE="gyif1/0/1",LOCALPORT=13202;

### WSFD-011134

**md：`WSFD-011134/实现原理_75821601.md`**
- 操作步骤上下文（±2 行原文）：
  L67:
    > #### [Diameter链路选择及Diameter链路故障倒换](#ZH-CN_CONCEPT_0275821601)
    > 
    > Diameter链路组内的Diameter链路间可以通过 [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) / [**MOD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/修改Diameter链路组（MOD DIAMCONNGRP）_09897262.md) 命令配置为主备（MASTER_SLAVE）或负荷分担（SESSION_ID、ROUND_ROBIN）。
    > 
    > - 互为主备的Diameter链路：GGSN/PGW-C优先选择主用Diameter链路，当检测到主用Diameter链路故障时，GGSN/PGW-C再选择备用Diameter链路重发消息。GGSN/PGW-C与通过[**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)配置的第一条DRA的Diameter链路为主用Diameter链路。

**md：`WSFD-011134/激活S6b over DRA（静态路由+BFD组网）_75821602.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | Diameter链路组名（CONNGROUPNAME） | dconn_s6b1<br>dconn_s6b2 | 本端规划 | - |
  | [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 本端主机名（LOCALHOSTNAME） | pgw_1<br>pgw_2 | 全网规划 | - |
  | [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 对端主机名（PEERHOSTNAME） | host1.example.com<br>host2.example.com | 全网规划 | - |
  | [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | Diameter应用（APPLICATION） | S6B | 全网规划 | - |
  | [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 链路选择模式（SELECTMODE） | SESSION_ID | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b1",LOCALHOSTNAME="pgw_1",APPLICATION=S6B,PEERHOSTNAME="host1.example.com";`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b2",LOCALHOSTNAME="pgw_2",APPLICATION=S6B,PEERHOSTNAME="host2.example.com";`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b1",LOCALHOSTNAME="pgw_1",APPLICATION=S6B,PEERHOSTNAME="host1.example.com";`
  `ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b2",LOCALHOSTNAME="pgw_2",APPLICATION=S6B,PEERHOSTNAME="host2.example.com";`
- 操作步骤上下文（±2 行原文）：
  L133:
    >       > - DRA与Diameter实体PCRF/OCS/AAA的主机名不能重复。
    >     c. 配置到DRA的链路组信息。
    >       [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    >     d. 配置到DRA的链路。
    >       [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
  L224:
    >   //配置网元对接。
    >   ```
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b1",LOCALHOSTNAME="pgw_1",APPLICATION=S6B,PEERHOSTNAME="host1.example.com";
    >   ```
    >   ```
  L227:
    >   ```
    >   ```
    >   ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b2",LOCALHOSTNAME="pgw_2",APPLICATION=S6B,PEERHOSTNAME="host2.example.com";
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（5）：['APPLICATION', 'CONNGROUPNAME', 'LOCALHOSTNAME', 'PEERHOSTNAME', 'SELECTMODE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 14, '全网规划': 24, '与对端协商': 2}（多值→atom 应考虑 decision_driven）
