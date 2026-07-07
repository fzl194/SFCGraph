# 命令证据包：ADD DIAMLOCINFO
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用来增加Diameter本端信息。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为128。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOSTNAME | 本端主机名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格。 |
| REALMNAME | 本端域名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格。 |
| PRODUCTNAME | 产品名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| VENDORID | Vendor-Id AVP值 | local_planned | optional | 10415 | 整数类型，取值范围为0～4294967295。 |
| FIRMWAREREV | Firmware-Revision AVP值 | local_planned | optional | 0 | 整数类型，取值范围为0～4294967295。 |
| ORIGINSTATEID | Origin-State-Id AVP使能开关 | local_planned | optional | DISABLE | 枚举类型。 |
| SUPPORTVENDORID | Supported-Vendor-Id AVP使能开关 | local_planned | optional | DISABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO: HOSTNAME="unc_1",REALMNAME="apn2",PRODUCTNAME="unc";`
- 操作步骤上下文（±2 行原文）：
  L85:
    >   **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
    > 8. 配置本端端点的主机信息。
    >   [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > 9. 配置3GPP AAA Server。
    >   [**ADD DIAMETERAAA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA信息/增加Diameter AAA服务器（ADD DIAMETERAAA）_64343821.md)
  L152:
    > 8. 配置本端端点的主机信息，端口号固定，由系统自动生成。
    >   ```
    >   ADD DIAMLOCINFO: HOSTNAME="unc_1",REALMNAME="apn2",PRODUCTNAME="unc";
    >   ```
    > 9. 配置3GPP AAA Server的设备标识及其主机信息。

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
    > - [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端主机名（HOSTNAME） | pgwc_1 | 全网规划 | GGSN/PGW-C的本端信息。 |
  | [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端域名（REALMNAME） | huawei.com | 全网规划 | GGSN/PGW-C的本端信息。 |
  | [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 产品名称（PRODUCTNAME） | unc@huawei.com | 本端规划 | GGSN/PGW-C的本端信息。 |
  | [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端主机名（HOSTNAME） | pgwc_1<br>pgwc_2 | 全网规划 | GGSN/PGW-C的本端信息。 |
  | [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端域名（REALMNAME） | huawei.com | 全网规划 | GGSN/PGW-C的本端信息。 |
  | [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 产品名称（PRODUCTNAME） | unc@huawei.com | 本端规划 | GGSN/PGW-C的本端信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO:HOSTNAME="pgw_1",REALMNAME="huawei.com", PRODUCTNAME="unc@huawei.com";`
  `ADD DIAMLOCINFO:HOSTNAME="pgwc_1",REALMNAME="huawei.com", PRODUCTNAME="unc@huawei.com";`
  `ADD DIAMLOCINFO:HOSTNAME="pgwc_2",REALMNAME="huawei.com", PRODUCTNAME="unc@huawei.com";`
- 操作步骤上下文（±2 行原文）：
  L27:
    > 数据
    > 
    > 同一PGW-C下对接多个PGW-U，不同PGW-U的用户IP不同或PCRF没有要求UE IP + GxLocalHost（GxLocalHost通过 [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) 命令的参数“HOSTNAME”配置）能唯一确定一个用户时，请规划 [表1](#ZH-CN_OPI_0230805096__table2142990478175815) 中的数据；同一PGW-C下对接多个PGW-U，不同PGW-U下的用户IP存在相同或重叠，且PCRF要求UE IP + GxLocalHost能唯一确定一个用户时，请规划 [表2](#ZH-CN_OPI_0230805096__table69333922118) 中的数据。
    > 
    > *表1 待规划数据（不同PGW-U下的用户IP不同）*
  L62:
    > | [**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端端口（LOCALPORT） | 16450<br>16451 | 本端规划 | [**SET CONCENPOINT**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)<br>命令中的<br>“GXCONCENMODE”<br>为<br>“LOCALPORT”<br>时，此处必须配置<br>“本端端口”<br>为非0的有效值；否则不配置<br>“本端端口”<br>或配置为<br>“0”<br>。 |
    > 
    > 同一PGW-C对接多个PGW-U，不同PGW-U下的用户IP存在相同或重叠，且PCRF要求UE IP + GxLocalHost（GxLocalHost通过 [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) 命令的参数“HOSTNAME”配置）能唯一确定一个用户时，需要规划 [表2](#ZH-CN_OPI_0230805096__table69333922118) 中的数据。否则，不需要规划 [表2](#ZH-CN_OPI_0230805096__table69333922118) 中的数据。
    > 
    > *表2 待规划数据（不同PGW-U下的用户IP存在相同）*
  L131:
    >   > [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) 中的“IP地址+VPN实例名称”和 [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) 命令中的“IP地址+VPN实例名称”必须一致。
    > 6. 配置GGSN/PGW-C的设备标识。
    >   [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > 7. 配置PCRF的信息。
    >     a. 配置PCRF的设备标识。

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
  L14:
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > - [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - **[ADD SCTPTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)**
    > - **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端主机名（HOSTNAME） | unc_1 | 与对端协商 | - |
  | [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端域名（REALMNAME） | example.com | 与对端协商 | - |
  | [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 产品名称（PRODUCTNAME） | unc | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example.com",PRODUCTNAME="unc";`
- 操作步骤上下文（±2 行原文）：
  L88:
    >   > 在对端的端口号为奇数时，可以通过 **[MOD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/修改Diameter链路（MOD DIAMCONNECTION）_09897267.md)** 命令设置 “REVERSEIP” 为 “ENABLE” 来颠倒本端的主从IP地址，与对端建立偶联，即本端配置的从IP作为偶联的主IP，本端配置的主IP作为偶联的从IP。
    > 5. 配置本端端点的主机信息。
    >   [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > 6. 配置SCTP模板参数。
    >   **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)**
  L158:
    > 
    > ```
    > ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example.com",PRODUCTNAME="unc";
    > ```
    > 

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端主机名（HOSTNAME） | unc_1 | 与对端协商 | GGSN/PGW-C的设备信息。其中host和realm需要与OCS上配置的一致。 |
  | [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端域名（REALMNAME） | example.com | 与对端协商 | GGSN/PGW-C的设备信息。其中host和realm需要与OCS上配置的一致。 |
  | [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 产品名称（PRODUCTNAME） | unc | 与对端协商 | GGSN/PGW-C的设备信息。其中host和realm需要与OCS上配置的一致。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example.com",PRODUCTNAME="unc";`
- 操作步骤上下文（±2 行原文）：
  L85:
    >   > 在对端的端口号为奇数时，可以通过 [**MOD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/修改Diameter链路（MOD DIAMCONNECTION）_09897267.md) 命令设置 “REVERSEIP” 为 “ENABLE” 来颠倒本端的主从IP地址，与对端建立偶联，即本端配置的从IP作为偶联的主IP，本端配置的主IP作为偶联的从IP。
    > 5. 配置本端端点的主机信息。
    >   [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > 6. 配置SCTP模板参数。
    >   **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)**
  L151:
    > 
    > ```
    > ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example.com",PRODUCTNAME="unc";
    > ```
    > 

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**SET CMDLEVDFTBEH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板命令层缺省返回码动作（SET CMDLEVDFTBEH）_09896928.md)
    > - [**SET MSCCLEVDFTBEH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板MSCC层缺省返回码动作（SET MSCCLEVDFTBEH）_09896929.md)
    > - [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - [**ADD OCS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**SET CMDLEVDFTBEH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板命令层缺省返回码动作（SET CMDLEVDFTBEH）_09896928.md)
    > - [**SET MSCCLEVDFTBEH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板MSCC层缺省返回码动作（SET MSCCLEVDFTBEH）_09896929.md)
    > - [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - [**ADD OCS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)
    > - [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMLOCINFO** | 本端主机名（HOSTNAME） | pgw1 | 全网规划 | GGSN/PGW-C的本端信息。 |
  | **ADD DIAMLOCINFO** | 本端域名（REALMNAME） | huawei.com | 全网规划 | GGSN/PGW-C的本端信息。 |
  | **ADD DIAMLOCINFO** | 产品名称（PRODUCTNAME） | unc@huawei.com | 本端规划 | GGSN/PGW-C的本端信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO: HOSTNAME="pgw1", REALMNAME="huawei.com", PRODUCTNAME="unc@huawei.com";`
- 操作步骤上下文（±2 行原文）：
  L94:
    >   > **ADD LOGICINF** 中的“IP地址+VPN实例名称”和 **ADD LOGICIP** 命令中的“IP地址+VPN实例名称”必须一致。
    > 6. 配置在线计费中GGSN/PGW-C的设备标识。
    >   **ADD DIAMLOCINFO**
    > 
    >   > **说明**
  L162:
    > 6. 配置用于通信的本端设备信息。
    >   ```
    >   ADD DIAMLOCINFO: HOSTNAME="pgw1", REALMNAME="huawei.com", PRODUCTNAME="unc@huawei.com";
    >   ```
    > 7. 配置用于通信的OCS信息。

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMLOCINFO** | 本端主机名（HOSTNAME） | pgw1 | 本端规划 | GGSN/PGW-C信息。 |
  | **ADD DIAMLOCINFO** | 本端域名（REALMNAME） | huawei.com | 本端规划 | GGSN/PGW-C信息。 |
  | **ADD DIAMLOCINFO** | 产品名称（PRODUCTNAME） | unc@huawei.com | 本端规划 | GGSN/PGW-C信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";`
- 操作步骤上下文（±2 行原文）：
  L103:
    > 5. 配置在线计费设备标识。
    >     a. 配置在线计费中通信的GGSN/PGW-C设备标识，重复执行本步可添加多个Gy应用的本地信息。
    >       **ADD DIAMLOCINFO**
    >     b. 配置OCS信息。重复执行本步可增加多个OCS信息。
    >       **ADD OCS**
  L161:
    > 5. 配置在线计费设备标识。
    >   ```
    >   ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";
    >   ```
    >   ```

**md：`WSFD-109001/配置OCS负荷分担_95923468.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMLOCINFO** | 本端主机名（HOSTNAME） | pgw1 | 本端规划 | GGSN/PGW-C信息。 |
  | **ADD DIAMLOCINFO** | 本端域名（REALMNAME） | huawei.com | 本端规划 | GGSN/PGW-C信息。 |
  | **ADD DIAMLOCINFO** | 产品名称（PRODUCTNAME） | unc@huawei.com | 本端规划 | GGSN/PGW-C信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";`
  `ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";`
  `ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";`
- 操作步骤上下文（±2 行原文）：
  L70:
    >   > **说明**
    >   > UNC 的Gx应用和Gy应用的本端主机名可以相同，但是同时要求 “REALMNAME” 参数和 “PRODUCTNAME” 参数也必须相同。
    >   **ADD DIAMLOCINFO**
    > 2. 配置平均进行OCS负荷分担。
    >     a. 配置OCS信息。重复执行本步骤可增加多个OCS信息。
  L115:
    > 1. 配置GGSN/PGW-C设备标识。
    >   ```
    >   ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";
    >   ```
    > 2. 配置OCS平均负荷分担。
  L204:
    > 1. 配置GGSN/PGW-C设备标识。
    >   ```
    >   ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";
    >   ```
    > 2. 配置基于用户号段进行OCS负荷分担。

**md：`WSFD-109001/配置基于CC+用户号段选择OCS_95923602.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DIAMLOCINFO** | 本端主机名（HOSTNAME） | pgw1 | 本端规划 | GGSN/PGW-C信息。 |
  | **ADD DIAMLOCINFO** | 本端域名（REALMNAME） | huawei.com | 本端规划 | GGSN/PGW-C信息。 |
  | **ADD DIAMLOCINFO** | 产品名称（PRODUCTNAME） | unc@huawei.com | 本端规划 | GGSN/PGW-C信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";`
- 操作步骤上下文（±2 行原文）：
  L69:
    >   > **说明**
    >   > UNC 的Gx应用和Gy应用的本端主机名可以相同，但是同时要求 “REALMNAME” 参数和 “PRODUCTNAME” 也必须相同。
    >   **ADD DIAMLOCINFO**
    > 2. 配置基于用户号段进行OCS负荷分担。
    >     a. 配置OCS信息。重复执行本步骤可增加多个OCS信息。
  L115:
    > 1. 配置GGSN/PGW-C设备标识。
    >   ```
    >   ADD DIAMLOCINFO: HOSTNAME="pgw1",REALMNAME="huawei.com",PRODUCTNAME="unc@huawei.com";
    >   ```
    > 2. 配置基于用户号段进行OCS负荷分担。

**md：`WSFD-109001/调测到OCS的数据_95923404.md`**
- 操作步骤上下文（±2 行原文）：
  L62:
    > 6. 修改GGSN/PGW-C设备标识。
    >     a. 执行 **RMV DIAMLOCINFO** 命令，删除原有配置。
    >     b. 执行 **ADD DIAMLOCINFO** 命令，按照规划数据重新配置GGSN/PGW-C的设备标识。
    >     c. 再次执行 [步骤 1](#ZH-CN_OPI_0295923404__step1) ，查看OCS状态。
    >           - 如果OCS状态正常，该调测任务结束。
  L108:
    >   **问题分析：**
    >     1. 查看Gy接口跟踪消息，发现TCP的链接已经建立成功，GGSN/PGW-C成功向OCS发出了CER，OCS响应了CEA，说明OCS已经收到并处理了GGSN/PGW-C的CER消息。
    >     2. 分析现场配置文件中的 **ADD OCS** 和GGSN/PGW-C的 **ADD DIAMLOCINFO** ，与Gy接口的CER和CEA消息中的origin-host和origin-realm对比，发现CEA消息中的origin-host和数据规划的ocs host不一致，数据规划的OCS的host信息是ocs1，对应GGSN/PGW-C的配置命令是：
    >       ```
    >       ADD OCS:OCSHOSTNAME="HUAWEIocs",REALMNAME="huawei.com";

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
    > - **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)**
    > - **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
    > - **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**
    > - **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 本端主机名（HOSTNAME） | unc_1 | 本端规划 | PCC架构中的设备信息。 |
  | **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 本端域名（REALMNAME） | example1.com | 与对端协商 | PCC架构中的设备信息。 |
  | **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 产品名称（PRODUCTNAME） | unc | 本端规划 | PCC架构中的设备信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";`
  `ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";`
- 操作步骤上下文（±2 行原文）：
  L134:
    >   **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. 配置GGSN/PGW-C的设备标识。
    >   **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
    > 7. 配置PCRF信息及动态PCRF主机列表表项老化时长。
    >     a. 配置PCRF信息。
  L245:
    >   //配置GGSN/PGW-C的设备标识。
    >   ```
    >   ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";
    >   ```
    >   //配置网元对接。
  L361:
    >   //配置GGSN/PGW-C的设备标识。
    >   ```
    >   ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";
    >   ```
    >   //配置网元对接。

**md：`WSFD-011132/调测Gx over DRA_29578142.md`**
- 操作步骤上下文（±2 行原文）：
  L129:
    > 7. 修改 GGSN/PGW-C 的Gx口设备标识。
    >     a. 执行 **[RMV DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.md)** 命令，删除原有配置。
    >     b. 执行 **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** 命令，按照规划数据重新配置 GGSN/PGW-C 的Gx口设备标识。
    >     c. 再次执行 [步骤 2](#ZH-CN_OPI_0229578142__stp0) ，查看DRA的链路组状态。
    >           - 如果检测DRA的链路组状态正常，则GGSN/PGW-C和DRA之间的链路互通调测结束。

### WSFD-011133

**md：`WSFD-011133/WSFD-011133 Gy over DRA参考信息_29725462.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > - **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
    > - **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**
    > - **[ADD OCSGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)**

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 本端主机名（HOSTNAME） | unc_1 | 全网规划 | 配置设备信息。 |
  | **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 本端域名（REALMNAME） | example1.com | 与对端协商 | 配置设备信息。 |
  | **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 产品名称（PRODUCTNAME） | unc | 本端规划 | 配置设备信息。 |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";`
  `ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";`
- 操作步骤上下文（±2 行原文）：
  L126:
    >   **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. 配置GGSN/PGW-C的设备标识信息。
    >   **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
    > 7. **可选：**配置直连OCS相关信息。
    >   > **说明**
  L263:
    >   //配置GGSN/PGW-C的设备标识。
    >   ```
    >   ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";
    >   ```
    >   //配置网元对接。
  L359:
    >   //配置GGSN/PGW-C的设备标识。
    >   ```
    >   ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";
    >   ```
    >   //配置网元对接。

### WSFD-011134

**md：`WSFD-011134/激活S6b over DRA（静态路由+BFD组网）_75821602.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端主机名（HOSTNAME） | pgw_1<br>pgw_2 | 本端规划 | - |
  | [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端域名（REALMNAME） | example1.com | 与对端协商 | - |
  | [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 产品名称（PRODUCTNAME） | unc | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD DIAMLOCINFO:HOSTNAME="pgw_1",REALMNAME="example1.com",PRODUCTNAME="unc";`
  `ADD DIAMLOCINFO:HOSTNAME="pgw_2",REALMNAME="example1.com",PRODUCTNAME="unc";`
  `ADD DIAMLOCINFO:HOSTNAME="pgw_1",REALMNAME="example1.com",PRODUCTNAME="unc";`
  `ADD DIAMLOCINFO:HOSTNAME="pgw_2",REALMNAME="example1.com",PRODUCTNAME="unc";`
- 操作步骤上下文（±2 行原文）：
  L105:
    >   [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > 6. 配置GGSN/PGW-C的设备标识。
    >   [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > 7. 配置3GPP AAA相关信息。
    >   > **说明**
  L217:
    >   //配置GGSN/PGW-C的设备标识。
    >   ```
    >   ADD DIAMLOCINFO:HOSTNAME="pgw_1",REALMNAME="example1.com",PRODUCTNAME="unc";
    >   ```
    >   ```
  L220:
    >   ```
    >   ```
    >   ADD DIAMLOCINFO:HOSTNAME="pgw_2",REALMNAME="example1.com",PRODUCTNAME="unc";
    >   ```
    >   //配置网元对接。

## ④ 自动比对
- 命令真相参数（7）：['FIRMWAREREV', 'HOSTNAME', 'ORIGINSTATEID', 'PRODUCTNAME', 'REALMNAME', 'SUPPORTVENDORID', 'VENDORID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 7, '本端规划': 18, '与对端协商': 8}（多值→atom 应考虑 decision_driven）
