# 命令证据包：SET PCCFUNC
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用于设置动态PCC功能。使能或关闭全局用户的动态PCC功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- ARPEXTAVPSW、LOCSLCTMODE、LOCALHOSTNAME参数仅对Gx接口生效。
- N7接口承载绑定默认使用ARP信元中的所有参数。
- 该命令的LOCSLCTMODE和LOCALHOSTNAME参数值修改后只对新激活用户生效。
- 当用户使用Gx接口激活时，如果没有绑定PCRF Group，只配置了域信息，但

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOMEPCCSWITCH | 本地用户动态PCC功能 | local_planned | optional | 无 | 枚举类型。 |
| ROAMPCCSWITCH | 漫游用户动态PCC功能 | local_planned | optional | 无 | 枚举类型。 |
| VISITPCCSWITCH | 拜访用户动态PCC功能 | local_planned | optional | 无 | 枚举类型。 |
| REPORTLEVEL | 缺省上报级别 | 对端协商 | optional | 无 | 枚举类型。 |
| METERMETHOD | 缺省离线计费统计方式 | 对端协商 | optional | 无 | 枚举类型。 |
| ARPEXTAVPSW | 承载绑定ARP扩展参数开关 | 对端协商 | optional | 无 | 枚举类型。 |
| PREEMPTCAPVALUE | Pre-emption-Capability缺省值 | 对端协商 | conditional | 无 | 枚举类型。 |
| PREEMPTVULVALUE | Pre-emption-Vulnerability缺省值 | 对端协商 | conditional | 无 | 枚举类型。 |
| COMPOLICY | 公共策略 | 对端协商 | optional | 无 | 枚举类型。 |
| LOCSLCTMODE | PCC本端主机名选择模式 | local_planned | optional | 无 | 枚举类型。 |
| LOCALHOSTNAME | 本端主机名 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～127。 |
| URLCATEINTEGSW | URL分类集成开关 | local_planned | optional | 无 | 枚举类型。 |
| QOSREQNOGXRESP | Gx接口不回复UE侧QoS请求时的处理 | local_planned | optional | 无 | 枚举类型。 |
| MKPARSEFORMAT | Monitoring-Key的解析方式 | 对端协商 | optional | 无 | 枚举类型。 |
| LOCALPCCSELECT | 本地PCC策略选择模式 | local_planned | optional | 无 | 枚举类型。 |
| N7FEATURELIST | N7接口特性列表 | 对端协商 | optional | 无 | 位域类型。 |
| PCFSELECTMODE | 选择PCF方式 | global_planned | optional | 无 | 位域类型。 |
| REDIRECTSWITCH | 重定向功能开关 | local_planned | optional | 无 | 枚举类型。 |
| N7FAILOVERSW | N7 Failover功能开关 | 对端协商 | optional | 无 | 枚举类型。 |
| PCFFINDREMOTESW | 远端查询PCF开关 | global_planned | optional | 无 | 枚举类型。 |
| PCFLBPARA | PCF负荷分担参数 | 对端协商 | optional | 无 | 枚举类型。 |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| USEN15PCFSW | 优先使用N15 PCF开关 | global_planned | optional | 无 | 枚举类型。 |
| DISCCUSTOM | PCF状态过滤参数 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-213002

**md：`WSFD-213002/WSFD-213002 NF业务可靠性保障参考信息_13564477.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - **[**SET NFDISCPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/NF发现策略管理/设置NF的服务发现策略（SET NFDISCPLCY）_09651764.md)**
    > - **[**LST NFDISCPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/NF发现策略管理/查询NF的服务发现策略（LST NFDISCPLCY）_09651379.md)**
    > - **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
    > - **[LST PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/查询PCC功能（LST PCCFUNC）_21559291.md)**
    > 

**md：`WSFD-213002/激活 N7接口PCF Group_13564475.md`**
- 数据规划表（该命令的参数行）：
  | **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)** | PCF负荷分担参数（PCFLBPARA） | GROUPID | 与对端协商 | 配置SMF选择PCF的负荷分担参数。 |
- 任务示例脚本（该命令行）：
  `SET PCCFUNC: PCFLBPARA=GROUPID;`
- 操作步骤上下文（±2 行原文）：
  L40:
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 配置SMF选择PCF的负荷分担参数。
    >   **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
    > 4. 增加本地配置的对端NF实例的群组信息。
    >   **[**ADD PNFGROUPID**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF组管理/增加对端NF的群组信息（ADD PNFGROUPID）_09653180.md)**
  L69:
    > 
    > ```
    > SET PCCFUNC: PCFLBPARA=GROUPID;
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    > - [**SET PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    > - [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | PCC本端主机名选择模式（LOCSLCTMODE） | UPFGRP | 固定取值 | 基于全局配置PCC本端主机名选择模式。 |
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | UPF组与Diameter本端主机组的绑定关系组名称（UPFGLOCGBNDGNAME） | test | 已配置数据中获取 | 基于全局配置PCC本端主机名选择模式。 |
- 操作步骤上下文（±2 行原文）：
  L171:
    >             [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >     - 基于全局设置PCC本端主机名选择方式。
    >       [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 17. **可选：**NB-IoT用户接入场景，设置PGW-C向PCRF/PCF发送消息时的RAT信元值。
    >   [**SET NBIOTRATVALUE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md) : PCRF=EUTRAN_NB_IOT, PCF=EUTRAN_NB_IOT;

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 本地用户PCC功能（HOMEPCCSWITCH） | ENABLE | 本端规划 | 使能GGSN/PGW-C上的全局用户的PCC功能。 |
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 漫游用户PCC功能（ROAMPCCSWITCH） | ENABLE | 本端规划 | 使能GGSN/PGW-C上的全局用户的PCC功能。 |
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 拜访用户PCC功能（VISITPCCSWITCH） | ENABLE | 本端规划 | 使能GGSN/PGW-C上的全局用户的PCC功能。 |
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 公共策略（COMPOLICY） | LOCALAAA | 对端协商 | 此处以基于LOCALAAA实现公共策略为例。 |
- 任务示例脚本（该命令行）：
  `SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,COMPOLICY=LOCALAAA;`
- 操作步骤上下文（±2 行原文）：
  L116:
    >       [**SET DFTGLBPCRFGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md)
    >     b. 针对全局配置PCC使能开关。
    >       [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    >       > **说明**
    >       > 缺省REPORTLEVEL、缺省METERMETHOD和PCC用户激活时Common Policy的选择原则为可选配置，缺省使用默认值。
  L217:
    > 5. 配置全局缺省的PCC开关。
    >   ```
    >   SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,COMPOLICY=LOCALAAA;
    >   ```
    > 6. 配置2个APN下的PCC开关，其中APN apn-test1的PCC开关为 “ENABLE” ，并绑定PCRF组 “pcrf_group_2” ，APN apn-test2的PCC开关为 “INHERIT” ，当通过该APN接入的用户的特定号段未与PCRF组绑定时，使用全局缺省的PCRF组“pcrf_group_1”。

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 本地用户PCC功能（HOMEPCCSWITCH） | DISABLE | 本端规划 | 使能GGSN/PGW-C上的全局用户的本地PCC功能。<br>网络中未部署PCRF时，设置为DISABLE。否则需要设置为ENABLE。<br>APN粒度（<br>[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)<br>）的优先级高于全局粒度（<br>[**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>）。 |
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 漫游用户PCC功能（ROAMPCCSWITCH） | DISABLE | 本端规划 | 使能GGSN/PGW-C上的全局用户的本地PCC功能。<br>网络中未部署PCRF时，设置为DISABLE。否则需要设置为ENABLE。<br>APN粒度（<br>[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)<br>）的优先级高于全局粒度（<br>[**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>）。 |
  | [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 拜访用户PCC功能（VISITPCCSWITCH） | DISABLE | 本端规划 | 使能GGSN/PGW-C上的全局用户的本地PCC功能。<br>网络中未部署PCRF时，设置为DISABLE。否则需要设置为ENABLE。<br>APN粒度（<br>[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)<br>）的优先级高于全局粒度（<br>[**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>）。 |
- 任务示例脚本（该命令行）：
  `SET PCCFUNC:HOMEPCCSWITCH=DISABLE,ROAMPCCSWITCH=DISABLE,VISITPCCSWITCH=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L78:
    >   [**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 关闭全局粒度的动态PCC功能。关闭后，开启的是全局粒度的本地PCC功能。
    >   [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 4. 开启APN下的PCC开关。
    >     a. 配置PCC模板。
  L131:
    > 2. 关闭全局粒度的动态PCC开关。关闭后，开启的是全局粒度的本地PCC功能。
    >   ```
    >   SET PCCFUNC:HOMEPCCSWITCH=DISABLE,ROAMPCCSWITCH=DISABLE,VISITPCCSWITCH=DISABLE;
    >   ```
    > 3. 配置指定APN的PCC开关。

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 本地用户动态PCC功能（HOMEPCCSWITCH） | ENABLE | 本端规划 | 使能SMF上的全局用户的动态PCC功能。 |
  | [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 漫游用户动态PCC功能（ROAMPCCSWITCH） | ENABLE | 本端规划 | 使能SMF上的全局用户的动态PCC功能。 |
  | [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 拜访用户动态PCC功能（VISITPCCSWITCH） | ENABLE | 本端规划 | 使能SMF上的全局用户的动态PCC功能。 |
  | [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | N7 Failover功能开关（N7FAILOVERSW） | ENABLE | 与对端协商 | PCF采用主备容灾组网时，设置为<br>“ENABLE”<br>。PCF故障，如没有可用的备PCF时，设置为<br>“DISABLE”<br>。<br>该开关支持APN粒度（<br>[**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>）和全局粒度（<br>[**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>），请根据实际PCF能力规划。 |
  | [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | PCF负荷分担参数（PCFLBPARA） | GROUPID | 与对端协商 | 此处以基于GROUPID实现负荷分担为例。<br>- 支持PCF主备容灾且“PCF负荷分担参数（PCFLBPARA）”取值为“GROUPID”时，SMF要求主备PCF的GroupID必须相同。<br>- 支持PCF主备容灾且“PCF负荷分担参数（PCFLBPARA）”取值为“PRIORITY”时，SMF要求主备PCF的PRIORITY必须不同。 |
  | [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | 公共策略（COMPOLICY） | LOCALAAA | 与对端协商 | 此处以基于LOCALAAA实现公共策略为例。 |
- 任务示例脚本（该命令行）：
  `SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,COMPOLICY=LOCALAAA;`
  `SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,COMPOLICY=LOCALAAA;`
  `SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,COMPOLICY=LOCALAAA;`
- 操作步骤上下文（±2 行原文）：
  L140:
    >       [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     3. 使能SMF上的全局用户的PCC功能。
    >       [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    >     4. （可选）PCF不支持下发packetFilterUsage属性时需要配置。设置从N7接口收到的FlowInformation中不包含PacketFilterUsage时，SMF将FlowInformation映射成的Filter推送给UE。
    >       [**SET N7RCVATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/N7接收分发控制/设置N7接收信元处理控制（SET N7RCVATTRCTRL）_09653677.md) : NOPKTFLTUSAGE=SEND_PKTFLT_TO_UE;
  L150:
    >       对端PCF不支持GERAN时， “GERAN” 设置为 “FALSE” 。设置为FALSE的场景下，SMF向PCF发送的N7消息不携带RAT-Type，RAT切换不会触发N7更新流程。
    >     7. （可选）3G用户接入场景，使用N7接口获取策略信息时需要配置。设置N7接口在3G用户接入时支持发送携带3G相关的接入类型、位置和服务节点类型等信息。
    >       此时需要 [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) 命令中参数“ **N7FEATURELIST** ”的取值中包括“UtranSupport”。
    >       [**SET N7SNDATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/23G接入控制/设置N7发送信元处理控制（SET N7SNDATTRCTRL）_72001557.md) : UTRAN=TRUE;
    >       对端PCF不支持UTRAN时， “UTRAN” 设置为 “FALSE” 。设置为FALSE的场景下，SMF向PCF发送的N7消息不携带RAT-Type，RAT切换不会触发N7更新流程。
  L239:
    > 
    > ```
    > SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,COMPOLICY=LOCALAAA;
    > ```
    > 

### WSFD-109103

**md：`WSFD-109103/WSFD-109103 IPv6 SA参考信息_78881328.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)

### WSFD-109104

**md：`WSFD-109104/WSFD-109104 基于累计流量的策略控制参考信息_29056192.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)

**md：`WSFD-109104/激活基于累计流量的策略控制_29056190.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | Monitoring-Key的解析方式（MKPARSEFORMAT） | UNSIGNED32 | 与对端协商 | 该参数需要与PCRF保持一致。 |
- 任务示例脚本（该命令行）：
  `SET PCCFUNC:MKPARSEFORMAT=UNSIGNED32;`
- 操作步骤上下文（±2 行原文）：
  L41:
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置累计流量的上报方式。
    >   [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 4. 与PCRF通过Gx接口交互时，使能流量监控拥塞处理（UMCH）功能。
    >   [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)
  L65:
    > 
    > ```
    > SET PCCFUNC:MKPARSEFORMAT=UNSIGNED32;
    > ```
    > 

### WSFD-211009

**md：`WSFD-211009/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)

**md：`WSFD-211009/激活基于业务累计流量的策略控制_27915156.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | Monitoring-Key的解析方式（MKPARSEFORMAT） | UNSIGNED32 | 与对端协商 | 该参数需要与PCRF/PCF保持一致。 |
- 操作步骤上下文（±2 行原文）：
  L51:
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置Monitoring-Key的解析方式。
    >   [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 4. 配置URR标识与监控属性值的绑定关系。
    >   [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)

### WSFD-102001

**md：`WSFD-102001/激活VoLTE基础语音业务（适用于SGW-C_PGW-C）_67930995.md`**
- 任务示例脚本（该命令行）：
  `SET PCCFUNC: HOMEPCCSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 
    > 3. 开启全局缺省PCC开关。
    >   [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 4. 开启APN下的PCC开关。
    >   [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
  L75:
    > 
    > ```
    > SET PCCFUNC: HOMEPCCSWITCH=ENABLE;
    > ```
    > 

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L58:
    > **[LST RULEBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/查询用户模板和规则的绑定关系（LST RULEBINDING）_09897218.md)**
    > 
    > [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 
    > **[LST PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/查询PCC功能（LST PCCFUNC）_21559291.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | N7 Failover功能开关（N7FAILOVERSW） | ENABLE | 与对端协商 | 策略接口使用N7接口且PCF采用主备容灾组网时，使能N7接口failover功能。 |
- 任务示例脚本（该命令行）：
  `SET PCCFUNC:N7FAILOVERSW=ENABLE;`
  `SET PCCFUNC:N7FAILOVERSW=ENABLE;`
  `SET PCCFUNC:N7FAILOVERSW=ENABLE;`
  `SET PCCFUNC:N7FAILOVERSW=ENABLE;`
  `SET PCCFUNC:N7FAILOVERSW=ENABLE;`
  `SET PCCFUNC:N7FAILOVERSW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L273:
    > 
    >   a. 配置全局Failover开关。
    >       [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    >     b. 配置全局PCF故障处理动作。
    >       **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
  L414:
    > 
    >             ```
    >             SET PCCFUNC:N7FAILOVERSW=ENABLE;
    >             ```
    >             //配置全局PCF故障处理动作。
  L466:
    > 
    >             ```
    >             SET PCCFUNC:N7FAILOVERSW=ENABLE;
    >             ```
    >             //配置全局PCF故障处理动作。

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
    > - **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**
    > - **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
    > - **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)**
    > - **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)** | 本地用户动态PCC功能（HOMEPCCSWITCH） | ENABLE | 本端规划 | 配置全局PCC开关。 |
  | **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)** | 漫游用户动态PCC功能（ROAMPCCSWITCH） | ENABLE | 本端规划 | 配置全局PCC开关。 |
  | **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)** | 拜访用户动态PCC功能（VISITPCCSWITCH） | ENABLE | 本端规划 | 配置全局PCC开关。 |
- 任务示例脚本（该命令行）：
  `SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;`
  `SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L182:
    >       **[ADD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)**
    >     b. 使能全局PCC开关。
    >       **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
    >       > **说明**
    >       > GGSN/PGW-C支持基于用户的漫游属性开启PCC功能，可通过本命令使能本地用户、漫游用户和/或拜访用户的PCC功能。
  L273:
    >   ```
    >   ```
    >   SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
    >   ```
    >   ```
  L391:
    >   ```
    >   ```
    >   SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（24）：['ARPEXTAVPSW', 'COMPOLICY', 'DISCCUSTOM', 'HOMEPCCSWITCH', 'LOCALHOSTNAME', 'LOCALPCCSELECT', 'LOCSLCTMODE', 'METERMETHOD', 'MKPARSEFORMAT', 'N7FAILOVERSW', 'N7FEATURELIST', 'PCFFINDREMOTESW', 'PCFLBPARA', 'PCFSELECTMODE', 'PREEMPTCAPVALUE', 'PREEMPTVULVALUE', 'QOSREQNOGXRESP', 'REDIRECTSWITCH', 'REPORTLEVEL', 'ROAMPCCSWITCH', 'UPFGLOCGBNDGNAME', 'URLCATEINTEGSW', 'USEN15PCFSW', 'VISITPCCSWITCH']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'与对端协商': 7, '固定取值': 1, '已配置数据中获取': 1, '本端规划': 12, '对端协商': 1}（多值→atom 应考虑 decision_driven）
