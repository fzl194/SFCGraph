# 命令证据包：SET CONTAINERTRIGGER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md`
> 用该命令的特性数：5

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用来配置离线计费容器产生开关。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。
- 只有配置了离线计费模板才能配置此命令。
- 当前版本不支持此命令的CONTTRIGENB参数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CONTTRIGRATCHNG | CONTTRIGQOSCHNG | PCCINIT | CONTTRIGSNCHNG | CONTTRIGCGISAI | CON

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| OFCTEMPLATENAME | 离线计费模板名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| CONTTRIGRATCHNG | Container RAT更新 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGQOSCHNG | QoS更新 | local_planned | optional | 无 | 枚举类型。 |
| PCCINIT | PCRF发起的QoS更新 | local_planned | conditional | 无 | 枚举类型。 |
| CONTTRIGSNCHNG | Serving Node更新 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGCGISAI | CGI/SAI更新 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGECGI | ECGI更新 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGTAI | TAI更新 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGULI | ULI更新 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGPLMNID | Container Serving Node PLMN标识更新 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGRAI | RAI更新 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGTARRIF | 费率切换 | local_planned | optional | 无 | 枚举类型。 |
| CONTTRIGENB | eNodeB更新 | local_planned | optional | 无 | 枚举类型。 |
| USERPLANECHNG | 用户面更新 | local_planned | optional | 无 | 枚举类型。 |
| SPLMNRATECHNG | 服务PLMN控制速率改变 | local_planned | optional | 无 | 枚举类型。 |
| APNRATECHNG | APN控制速率改变 | local_planned | optional | 无 | 枚举类型。 |
| APNRATECHNGCLOSECAUSE | APN速率控制改变流量容器关闭原因值 | 对端协商 | conditional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-216104

**md：`WSFD-216104/WSFD-216104 基于APN的eMTC终端接入速率控制参考信息_75993426.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**RMV DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/删除Diameter字典加载路径（RMV DIAMDICTPATH）_09897249.md)
    > - [**LST DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/查询Diameter字典加载路径（LST DIAMDICTPATH）_09897250.md)
    > - [**SET CONTAINERTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0275993426)

### WSFD-216105

**md：`WSFD-216105/WSFD-216105 基于服务PLMN的eMTC终端接入速率控制参考信息_75993431.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**RMV DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/删除Diameter字典加载路径（RMV DIAMDICTPATH）_09897249.md)
    > - [**LST DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/查询Diameter字典加载路径（LST DIAMDICTPATH）_09897250.md)
    > - [**SET CONTAINERTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0275993431)

### WSFD-215204

**md：`WSFD-215204/WSFD-215204 基于APN的NB-IoT终端接入速率控制参考信息（PGW-C）_77673131.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**RMV DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/删除Diameter字典加载路径（RMV DIAMDICTPATH）_09897249.md)
    > - [**LST DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/查询Diameter字典加载路径（LST DIAMDICTPATH）_09897250.md)
    > - [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0277673131)

### WSFD-215205

**md：`WSFD-215205/WSFD-215205 基于服务PLMN的NB-IoT终端接入速率控制参考信息（S_PGW-C）_77673138.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**RMV DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/删除Diameter字典加载路径（RMV DIAMDICTPATH）_09897249.md)
    > - [**LST DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/查询Diameter字典加载路径（LST DIAMDICTPATH）_09897250.md)
    > - [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0277673138)

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**SET OFCTHRESHOLD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)
    > - [**SET CDRTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费话单产生开关（SET CDRTRIGGER）_09896911.md)
    > - [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)

**md：`WSFD-011201/离线计费话单（GGSN_SGW-C_PGW-C）_92172742.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 容器产生的背景：网络设计者希望话单能够记录足够的信息，包括各种计费条件改变时的计费信息，这会导致生成的话单较大，所以引入容器概念。容器记录计费条件改变时相关的计费信息，一张话单可以包括多个容器，从而在不增加话单量的情况下记录充分多的计费信息。
    > 
    > 容器的分类：UNC与CG支持按照承载粒度（使用流量容器）或业务粒度（使用业务容器）统计用户访问流量，可通过 **SET CONTAINERTRIGGER** 命令配置，如 [表2](#ZH-CN_TOPIC_0292172742__table_03D3EB65) 所示。
    > 
    > *表2 话单容器描述*

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **SET CONTAINERTRIGGER** | 离线计费模板名（OFCTEMPLATENAME） | offlinecharge-test | 已配置数据中获取 | 话单容器产生条件 |
  | **SET CONTAINERTRIGGER** | Container RAT更新（CONTTRIGRATCHNG） | DISABLE | 本端规划 | 话单容器产生条件 |
  | **SET CONTAINERTRIGGER** | QoS更新（CONTTRIGQOSCHNG） | DISABLE | 本端规划 | 话单容器产生条件 |
- 任务示例脚本（该命令行）：
  `SET CONTAINERTRIGGER: OFCTEMPLATENAME="offlinecharge-test";`
- 操作步骤上下文（±2 行原文）：
  L88:
    >       **SET CDRTRIGGER**
    >     d. 配置话单容器产生条件。
    >       **SET CONTAINERTRIGGER**
    > 2. 配置OFCTemplate模板绑定UserProfile对象。
    >     a. 配置UserProfile。如已配置UserProfile，请跳过该步骤。
  L146:
    >   ```
    >   ```
    >   SET CONTAINERTRIGGER: OFCTEMPLATENAME="offlinecharge-test";
    >   ```
    > 2. 任务一：配置UserProfile的离线计费参数。

## ④ 自动比对
- 命令真相参数（17）：['APNRATECHNG', 'APNRATECHNGCLOSECAUSE', 'CONTTRIGCGISAI', 'CONTTRIGECGI', 'CONTTRIGENB', 'CONTTRIGPLMNID', 'CONTTRIGQOSCHNG', 'CONTTRIGRAI', 'CONTTRIGRATCHNG', 'CONTTRIGSNCHNG', 'CONTTRIGTAI', 'CONTTRIGTARRIF', 'CONTTRIGULI', 'OFCTEMPLATENAME', 'PCCINIT', 'SPLMNRATECHNG', 'USERPLANECHNG']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '本端规划': 2}（多值→atom 应考虑 decision_driven）
