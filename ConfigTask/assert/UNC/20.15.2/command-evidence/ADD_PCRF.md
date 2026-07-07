# 命令证据包：ADD PCRF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md`
> 用该命令的特性数：7

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

该命令用于增加PCRF的基本信息，配置PCRF主机名、域名、VPN实例、PCRF动态协商参数。

此命令为PCC策略控制的核心配置。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOSTNAME | PCRF主机名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否 |
| REALMNAME | PCRF域名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否 |
| VPNINSTANCE | VPN实例 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，区分大小写。 |
| SUPFEANEGOSW | Supported-Features动态协商开关 | 对端协商 | optional | DISABLE | 枚举类型。 |
| CARRYSUPFEASW | Supported-Feature AVP携带开关 | global_planned | conditional | ENABLE | 枚举类型。 |
| FEATURELIST | Feature列表 | 对端协商 | optional | 无 | 位域类型。 |
| DSCPV | DSCP值 | global_planned | optional | 255 | 整数类型，取值范围为0～63，255。 |
| WALVALUE | wal值 | local_planned | optional | 0 | 整数类型，取值范围为0～4294967295。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011521

**md：`WSFD-011521/WSFD-011521 NSA 用户QoS管理参考信息_27675788.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**MOD DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/修改Diameter字典加载路径（MOD DIAMDICTPATH）_09897248.md)
    > - [**LOD DIAMDICT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载字典/加载Diameter字典（LOD DIAMDICT）_09897254.md)
    > - [**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    > - [**ADD GLBDIAMREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)
    > - [**ADD REALMBINDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)

**md：`WSFD-011521/激活NSA用户QoS管理_27675786.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF主机名（HOSTNAME） | pcrf1 | 本端规划 | 增加PCRF的基本信息<br>说明：“FEATURELIST”<br>需要同时配置为<br>“RELEASE8”<br>和<br>“EXTENDED_BW_NR”<br>。 |
  | [**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF域名（REALMNAME） | pcrf.huawei.com | 本端规划 | 增加PCRF的基本信息<br>说明：“FEATURELIST”<br>需要同时配置为<br>“RELEASE8”<br>和<br>“EXTENDED_BW_NR”<br>。 |
  | [**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | Feature列表（FEATURELIST） | RELEASE8<br>EXTENDED_BW_NR | 与对端协商 | 增加PCRF的基本信息<br>说明：“FEATURELIST”<br>需要同时配置为<br>“RELEASE8”<br>和<br>“EXTENDED_BW_NR”<br>。 |
  | [**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | Supported-Features动态协商开关（SUPFEANEGOSW） | ENABLE | 对端协商 | 增加PCRF的基本信息<br>说明：“FEATURELIST”<br>需要同时配置为<br>“RELEASE8”<br>和<br>“EXTENDED_BW_NR”<br>。 |
- 任务示例脚本（该命令行）：
  `ADD PCRF:HOSTNAME="pcrf1",REALMNAME="pcrf.huawei.com",FEATURELIST=EXTENDED_BW_NR-1&RELEASE8-1,SUPFEANEGOSW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L61:
    >   > UNC 主机软件加载时，会自动加载Diameter控制文件。如果文件不存在，或者文件加载失败，也可以通过命令 [**LOD DIAMDICT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载字典/加载Diameter字典（LOD DIAMDICT）_09897254.md) 手工加载Diameter控制文件。
    > 4. 配置PCRF的域信息，并使能动态协商参数及扩展QoS功能。
    >   [**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    > 5. 基于IMSI/MSISDN号段或全局配置Realm，并使能动态协商参数及扩展QoS功能。
    >   [**ADD GLBDIAMREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)
  L94:
    > 
    > ```
    > ADD PCRF:HOSTNAME="pcrf1",REALMNAME="pcrf.huawei.com",FEATURELIST=EXTENDED_BW_NR-1&RELEASE8-1,SUPFEANEGOSW=ENABLE;
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    > - [**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    > - [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)

**md：`WSFD-109101/实现原理_29056158.md`**
- 操作步骤上下文（±2 行原文）：
  L142:
    > 为了可以更加灵活的与支持不同协议版本和不同能力的PCRF进行对接， UNC 支持Supported Features动态协商功能，即 UNC 与PCRF在IP-CAN Session建立过程中进行协商，决定 UNC 和PCRF之间的会话按照哪个协议版本进行交互，或指示 UNC 和PCRF是否具有相应的feature能力。
    > 
    > UNC 支持的feature列表，请参见 [**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) 中的 “FEATURELIST” 参数的取值范围。
    > 
    > UNC 的Supported Features动态协商功能使能，则 UNC 与PCRF之间Feature能力的协商过程分如下两种：
  L148:
    > - UNC本地配置的PCRF Feature能力与对端PCRF实际支持的Feature能力不一致，协商过程如[图1](#ZH-CN_TOPIC_0229056158__fig108761642112613)所示的首个用户上线过程和下个用户上线过程。
    > - UNC本地配置的PCRF Feature能力与对端PCRF实际支持的Feature能力一致，首个用户上线的协商过程如[图1](#ZH-CN_TOPIC_0229056158__fig108761642112613)中下个用户上线过程类似，均只需要一次协商过程，唯一差别在于CCR-I消息中携带的Feature能力的获取来源不同。
    >     - 首个用户上线：来源于本地[**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)命令配置的feature能力。
    >     - 下个用户上线：来源于本地存储的第一个IP-CAN会话的Supported Features动态协商结果。
    > 

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF主机名（HOSTNAME） | pcrf1<br>pcrf2 | 本端规划 | 配置PCRF的基本信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF域名（REALMNAME） | host1.example.com<br>host2.example.com | 本端规划 | 配置PCRF的基本信息。 |
- 任务示例脚本（该命令行）：
  `ADD PCRF:HOSTNAME="pcrf1",REALMNAME="host1.example.com";`
  `ADD PCRF:HOSTNAME="pcrf2",REALMNAME="host2.example.com";`
- 操作步骤上下文（±2 行原文）：
  L55:
    > 2. 配置PCRF信息。
    >     a. 配置PCRF信息。重复执行本步骤可增加多个PCRF信息。
    >       [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    >     b. 配置PCRF组。
    >       [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
  L83:
    > 1. 配置主备PCRF设备标识。
    >   ```
    >   ADD PCRF:HOSTNAME="pcrf1",REALMNAME="host1.example.com";
    >   ```
    >   ```
  L86:
    >   ```
    >   ```
    >   ADD PCRF:HOSTNAME="pcrf2",REALMNAME="host2.example.com";
    >   ```
    >   ```

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF主机名（HOSTNAME） | pcrf_1<br>pcrf_2 | 本端规划 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF域名（REALMNAME） | example.com | 本端规划 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | VPN实例（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | Supported-Features动态协商开关（SUPFEANEGOSW） | ENABLE | 与对端协商 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | Feature列表（FEATURELIST） | RELEASE8-1&RELEASE9-1&RELEASE10-1 | 与对端协商 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF主机名（HOSTNAME） | pcrf_1<br>pcrf_2 | 本端规划 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF域名（REALMNAME） | example.com | 本端规划 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | VPN实例（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | Supported-Features动态协商开关（SUPFEANEGOSW） | ENABLE | 与对端协商 | PCRF信息。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | Feature列表（FEATURELIST） | RELEASE8-1&RELEASE9-1&RELEASE10-1 | 与对端协商 | PCRF信息。 |
- 任务示例脚本（该命令行）：
  `ADD PCRF:HOSTNAME="pcrf_1",REALMNAME="example.com",VPNINSTANCE="vpn_gxif",SUPFEANEGOSW=ENABLE,FEATURELIST=RELEASE8-1&RELEASE9-1&RELEASE10-1;`
  `ADD PCRF:HOSTNAME="pcrf_2",REALMNAME="example.com",VPNINSTANCE="vpn_gxif",SUPFEANEGOSW=ENABLE,FEATURELIST=RELEASE8-1&RELEASE9-1&RELEASE10-1;`
  `ADD PCRF:HOSTNAME="pcrf_1",REALMNAME="example.com",VPNINSTANCE="vpn_gxif",SUPFEANEGOSW=ENABLE,FEATURELIST=RELEASE8-1&RELEASE9-1&RELEASE10-1;`
  `ADD PCRF:HOSTNAME="pcrf_2",REALMNAME="example.com",VPNINSTANCE="vpn_gxif",SUPFEANEGOSW=ENABLE,FEATURELIST=RELEASE8-1&RELEASE9-1&RELEASE10-1;`
- 操作步骤上下文（±2 行原文）：
  L134:
    > 7. 配置PCRF的信息。
    >     a. 配置PCRF的设备标识。
    >       [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    >       > **说明**
    >       > - PCRF绑定的VPN实例必须和Gx逻辑接口绑定的VPN实例一致。
  L138:
    >       > - PCRF绑定的VPN实例必须和Gx逻辑接口绑定的VPN实例一致。
    >       > - 如果GGSN/PGW-C与PCRF之间在TCP传输模式下采用多Diameter链路组网模式，则需要配置多个PCRF IP地址和端口，并配置链路选择模式“SELECTMODE”。
    >       > - 如果需要与指定PCRF进行Supported Features动态协商，则需要将 [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) 命令中的 “SUPFEANEGOSW” 参数设置为 “ENABLE” ，并选择对应的feature选项，且添加到同一个PCRF Group中的PCRF支持的feature能力必须一致。
    >       > - 根据PCRF的接收能力，通过设置“WAL”参数以限制向PCRF发送的消息数。
    >     b. 如果supported-features-negotiation功能使能，且需要定时或手工删除本地缓存的对端PCRF能力，需要配置动态协商定时器的时长，缺省使用默认值。
  L226:
    >   配置PCRF设备标识。其中GGSN/PGW-C与pcrf1之间建立一条Diameter链路，与pcrf2之间建立两条Diameter链路，不同的用户会话将负荷分担到不同链路上。
    >   ```
    >   ADD PCRF:HOSTNAME="pcrf_1",REALMNAME="example.com",VPNINSTANCE="vpn_gxif",SUPFEANEGOSW=ENABLE,FEATURELIST=RELEASE8-1&RELEASE9-1&RELEASE10-1;
    >   ```
    >   ```

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF主机名（HOSTNAME） | pcrf_1<br>pcrf_2<br>pcrf_3<br>pcrf_4 | 本端规划 | “pcrf_1”和“pcrf_2”属于“pcrf_group_1”，“pcrf_group_1”内的PCRF按配置的百分比进行负荷分担。“pcrf_3”和“pcrf_4”属于“pcrf_group_2”，“pcrf_group_2”内的PCRF为主备模式，且“pcrf_3”为主用PCRF。 |
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF域名（REALMNAME） | pcrf.huawei.com | 本端规划 | “pcrf_1”和“pcrf_2”属于“pcrf_group_1”，“pcrf_group_1”内的PCRF按配置的百分比进行负荷分担。“pcrf_3”和“pcrf_4”属于“pcrf_group_2”，“pcrf_group_2”内的PCRF为主备模式，且“pcrf_3”为主用PCRF。 |
- 任务示例脚本（该命令行）：
  `ADD PCRF:HOSTNAME="pcrf_1",REALMNAME="pcrf.huawei.com";`
  `ADD PCRF:HOSTNAME="pcrf_2",REALMNAME="pcrf.huawei.com";`
  `ADD PCRF:HOSTNAME="pcrf_3",REALMNAME="pcrf.huawei.com";`
  `ADD PCRF:HOSTNAME="pcrf_4",REALMNAME="pcrf.huawei.com";`
- 操作步骤上下文（±2 行原文）：
  L101:
    > 4. 配置PCRF分组信息。
    >     a. 配置PCRF。
    >       [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    >     b. 配置PCRF分组。
    >       [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
  L176:
    > 3. 配置PCRF分组信息，设置pcrf_group_1组内的PCRF按配置比例进行负荷分担，pcrf_group_2组内的PCRF之间为主备备份。
    >   ```
    >   ADD PCRF:HOSTNAME="pcrf_1",REALMNAME="pcrf.huawei.com";
    >   ```
    >   ```
  L179:
    >   ```
    >   ```
    >   ADD PCRF:HOSTNAME="pcrf_2",REALMNAME="pcrf.huawei.com";
    >   ```
    >   ```

**md：`WSFD-109101/调测PCRF负荷分担功能_31422955.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF名称（HOSTNAME） | pcrf_1<br>pcrf_2 | 已配置数据中获取 | GGSN/PGW-C上PCRF设备标识。 |

**md：`WSFD-109101/调测到PCRF的数据_31422954.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF主机名（HOSTNAME） | pcrf_1<br>pcrf_2 | 已配置数据中获取 | 取自<br>[配置与PCRF对接数据](../激活PCC基本功能/配置与PCRF对接数据_30805096.md)<br>中配置的数据。 |
- 操作步骤上下文（±2 行原文）：
  L116:
    > 4. 修改GGSN/PGW-C上PCRF设备标识。
    >     a. 执行[**RMV PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令，删除原有配置。
    >     b. 执行[**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)命令，按照规划数据和PCRF上的数据重新配置GGSN/PGW-C的PCRF信息。
    >     c. 再次执行[步骤 2](#ZH-CN_OPI_0231422954__stp1)，查看PCRF状态。
    >     - 如果检测PCRF状态正常，则GGSN/PGW-C和PCRF之间的链路互通调测结束。

### WSFD-109104

**md：`WSFD-109104/实现原理（Gx）_29961018.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > | 3GPP标准的Usage Monitoring机制 | [ Usage-Monitoring-Support ] | 指示Monitoring Key值的配额监控去使能。 | Usage-Report |
    > 
    > 采用3GPP标准的Usage Monitoring机制时，对于包月用户，会要求在某个时间点（例如月末）进行配额重置，如PCRF同时要求所有在线用户上报流量，会增加Gx接口的信令负荷，造成信令拥塞；如果PCRF分批要求在线用户上报流量，则流量上报有延迟，且上报不准确。为了解决该问题，引入UMCH（Usage Monitoring Congestion Handling）机制，PCRF通过Monitoring-Time AVP提前指定配额重置的时间点，PCEF分别统计配额重置时间点前后的流量，并通过重置后最近一次的流量上报流程一起上报给PCRF，从而避免Gx接口的Usage Monitoring信令拥塞。若开启该功能，需要 [**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) 命令中的 “Feature列表（FEATURELIST）” 参数包含 “UMCH” 。
    > 
    > 基于Gx的业务累计流量的策略控制流程如 [图1](#ZH-CN_TOPIC_0229961018__fig91071515191915) 所示。

### WSFD-211009

**md：`WSFD-211009/实现原理（Gx）_29039989.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > | 3GPP标准的Usage Monitoring机制 | [ Usage-Monitoring-Support ] | 指示Monitoring Key值的配额监控去使能。 | Usage-Report |
    > 
    > 采用3GPP标准的Usage Monitoring机制时，对于包月用户，会要求在某个时间点（例如月末）进行配额重置，如PCRF/PCF同时要求所有在线用户上报流量，会增加Gx接口的信令负荷，造成信令拥塞；如果PCRF/PCF分批要求在线用户上报流量，则流量上报有延迟，且上报不准确。为了解决该问题，引入UMCH（Usage Monitoring Congestion Handling）机制，PCRF通过Monitoring-Time AVP提前指定配额重置的时间点，PCEF分别统计配额重置时间点前后的流量，并通过重置后最近一次的流量上报流程一起上报给PCRF/PCF，从而避免Gx接口的Usage Monitoring信令拥塞。若开启该功能，需要 [**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) 命令中的 “Feature列表（FEATURELIST）” 参数包含 “UMCH” 。
    > 
    > 对于2/3/4G用户，基于业务累计流量的策略控制流程如 [图1](#ZH-CN_TOPIC_0229039989__fig91071515191915) 所示。

### WSFD-010802

**md：`WSFD-010802/WSFD-010802 周边网元过载保护（Gx_Gy_Ga_Gi接口流控功能）参考信息_30753122.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > [**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    > 
    > [**MOD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)

**md：`WSFD-010802/激活Gx_Gy_Ga_Gi接口流控功能_30753120.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | PCRF主机名（HOSTNAME） | PCRF1 | 本端规划 | 设置<br>UNC<br>每秒发送给某PCRF的最大CCR消息数。 |
  | **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | PCRF域名（REALMNAME） | www.huawei.com | 本端规划 | 设置<br>UNC<br>每秒发送给某PCRF的最大CCR消息数。 |
  | **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | wal值（WALVALUE） | 1000 | 本端规划 | 设置<br>UNC<br>每秒发送给某PCRF的最大CCR消息数。 |
- 任务示例脚本（该命令行）：
  `ADD PCRF:HOSTNAME="pcrf1",REALMNAME="www.huawei.com", WALVALUE=1000;`
- 操作步骤上下文（±2 行原文）：
  L53:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 设置 UNC 每秒发送给某PCRF的最大CCR消息数。
    >   **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    > 3. 设置 UNC 每秒发送给某OCS的最大消息数。
    >   **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**
  L74:
    > 
    > ```
    > ADD PCRF:HOSTNAME="pcrf1",REALMNAME="www.huawei.com", WALVALUE=1000;
    > ```
    > 

### WSFD-104508

**md：`WSFD-104508/WSFD-104508 SCTP参考信息_29341126.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
    > - **[SET GLBSCTPPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)**
    > - **[ADD PCRF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    > - **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**
    > - **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | PCRF主机名（HOSTNAME） | pcrf | 与对端协商 | PCC架构中PCRF的设备信息。 |
  | **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | PCRF域名（REALMNAME） | pcrf.huawei.com | 全网规划 | PCC架构中PCRF的设备信息。 |
  | **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | VPN实例（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD PCRF:HOSTNAME="pcrf",REALMNAME="pcrf.huawei.com",VPNINSTANCE="vpn_gxif";`
- 操作步骤上下文（±2 行原文）：
  L103:
    > 9. 配置对端端点的主机信息。
    >     a. 配置PCRF。
    >       **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    >     b. 配置PCRF的SCTP端点。
    >       **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
  L107:
    >       **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
    >       > **说明**
    >       > **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** 的主机名 “HOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
    > 10. 建立本端与对端的链路组，并配置链路选择模式。
    >   **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
  L183:
    > 
    > ```
    > ADD PCRF:HOSTNAME="pcrf",REALMNAME="pcrf.huawei.com",VPNINSTANCE="vpn_gxif";
    > ADD DIAMPEERADDR:HOSTNAME="pcrf",ADDRTYPE=SCTP,SCTPENDPOINT="pcrfendb";
    > ADD DIAMPEERADDR:HOSTNAME="pcrf",ADDRTYPE=SCTP,SCTPENDPOINT="pcrfendc";

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)**
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - **[ADD PCRF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    > - **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
    > 

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 操作步骤上下文（±2 行原文）：
  L137:
    > 7. 配置PCRF信息及动态PCRF主机列表表项老化时长。
    >     a. 配置PCRF信息。
    >       **[ADD PCRF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    >       > **说明**
    >       > 如果PCRF未配置域信息，则需要在本步骤中进行配置。

## ④ 自动比对
- 命令真相参数（8）：['CARRYSUPFEASW', 'DSCPV', 'FEATURELIST', 'HOSTNAME', 'REALMNAME', 'SUPFEANEGOSW', 'VPNINSTANCE', 'WALVALUE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 13, '与对端协商': 6, '对端协商': 1, '已配置数据中获取': 5, '全网规划': 1}（多值→atom 应考虑 decision_driven）
