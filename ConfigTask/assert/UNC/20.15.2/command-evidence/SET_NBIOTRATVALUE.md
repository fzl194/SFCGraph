# 命令证据包：SET NBIOTRATVALUE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用于设置NB-IoT终端接入时UNC给周边网元发送消息时RAT信元中填写的值。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | OCS | CG | AAAACCT | AAAAUTH | PCRF | PGW | CHF | PCF | UPF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | EUT

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| OCS | 和OCS交互使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |
| CG | 和CG交互使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |
| AAAACCT | 和AAA计费服务器交互使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |
| AAAAUTH | 和AAA鉴权服务器交互使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |
| PCRF | 和PCRF交互使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |
| PGW | SGW发送给PGW使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |
| CHF | 和CHF交互使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |
| PCF | 和PCF交互使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |
| UPF | 和UPF交互使用的RAT值 | 对端协商 | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011601

**md：`WSFD-011601/WSFD-011601 NB-IoT终端标准接入参考信息（适用于S_PGW-C）_76669510.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关MML命令如下：
    > 
    > - [**SET NBIOTRATVALUE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md)
    > - [**ADD SRVNODERAT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取RAT管理/IP地址映射RAT/增加SGSN_SGW IP与RAT类型间的映射关系（ADD SRVNODERAT）_09653221.md)
    > - [**SET DFTSRVNODERAT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取RAT管理/全局RAT配置/设置默认RAT类型（SET DFTSRVNODERAT）_09653166.md)

**md：`WSFD-011601/特性概述_76669507.md`**
- 操作步骤上下文（±2 行原文）：
  L111:
    > - 接入控制：NB-IoT终端接入采用独立的RAT接入EPC网络，UNC通过Create Session Request消息携带的RAT Type是否为NB-IoT实现对NB-IoT终端用户的接入控制。
    >   > **说明**
    >   > 可通过 [**SET NBIOTRATVALUE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md) 命令来配置给周边网元交互时使用的RAT Type。
    > - 数据传输：支持控制面优化和用户面优化两种数据传输方式。
    >   > **说明**

### WSFD-215302

**md：`WSFD-215302/WSFD-215302 PCRF免升级参考信息_75808671.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关MML命令如下：
    > 
    > - [**SET NBIOTRATVALUE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0275808671)

**md：`WSFD-215302/激活PCRF免升级_76026862.md`**
- 数据规划表（该命令的参数行）：
  | [**SET NBIOTRATVALUE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md) | 和PCRF交互使用的RAT值（PCRF） | EUTRAN | 本端规划 | PCRF免升级功能 |
- 任务示例脚本（该命令行）：
  `SET NBIOTRATVALUE: PCRF=EUTRAN;`
- 操作步骤上下文（±2 行原文）：
  L34:
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置开启PCRF免升级功能。
    >   [**SET NBIOTRATVALUE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276026862)
  L49:
    > 
    > ```
    > SET NBIOTRATVALUE: PCRF=EUTRAN;
    > ```

**md：`WSFD-215302/特性概述_75804173.md`**
- 操作步骤上下文（±2 行原文）：
  L65:
    > 在部署NB-IoT业务时， UNC 实现了在PCRF免升级的情况下可支持NB-IoT用户接入。具体实现方式如下：
    > 
    > PGW-C在给PCRF发送消息时，将消息携带的RAT-Type（EUTRAN_NB_IOT）替换成PCRF可识别的RAT-Type（EUTRAN）， 该操作可通过配置 **SET NBIOTRATVALUE** 实现 。
    > 
    > #### [计费与话单](#ZH-CN_TOPIC_0275804173)

### WSFD-109101

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 操作步骤上下文（±2 行原文）：
  L173:
    >       [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 17. **可选：**NB-IoT用户接入场景，设置PGW-C向PCRF/PCF发送消息时的RAT信元值。
    >   [**SET NBIOTRATVALUE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md) : PCRF=EUTRAN_NB_IOT, PCF=EUTRAN_NB_IOT;
    >     - 对接PCRF/PCF支持**EUTRAN-NB-IoT**类型时，“PCRF”/“PCF”设置为“EUTRAN_NB_IOT”，PGW-C向PCRF/PCF发送NB-IoT用户的相关消息时，RAT信元值为“EUTRAN-NB-IOT”。系统初始值为“EUTRAN_NB_IOT”。
    >     - 对接PCRF/PCF不支持**EUTRAN-NB-IoT**类型时，“PCRF”/“PCF”设置为“EUTRAN”，PGW-C向PCRF/PCF发送NB-IoT用户的相关消息时，RAT信元值为“EUTRAN”。“PCRF”设置为“EUTRAN”时，还需要开启PCRF免升级License，详细操作请参见[激活PCRF免升级](../../../../NB-IoT业务功能/WSFD-215302 PCRF免升级/激活PCRF免升级_76026862.md)。

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L154:
    >       对端PCF不支持UTRAN时， “UTRAN” 设置为 “FALSE” 。设置为FALSE的场景下，SMF向PCF发送的N7消息不携带RAT-Type，RAT切换不会触发N7更新流程。
    >     8. （可选）NB-IoT用户接入场景，设置SMF向PCF发送消息时的RAT信元值。
    >       [**SET NBIOTRATVALUE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md) : PCF=EUTRAN_NB_IoT;
    >           - 对接PCF支持**EUTRAN-NB-IoT**类型时，“PCF”设置为“EUTRAN_NB_IoT”，SMF向PCF发送NB-IoT用户的相关消息时，RAT信元值为“EUTRAN-NB-IoT”。系统初始值为“EUTRAN_NB_IoT”。
    >           - 对接PCF不支持**EUTRAN-NB-IoT**类型时，“PCF”设置为“EUTRAN”，SMF向PCF发送NB-IoT用户的相关消息时，RAT信元值为“EUTRAN”。

## ④ 自动比对
- 命令真相参数（9）：['AAAACCT', 'AAAAUTH', 'CG', 'CHF', 'OCS', 'PCF', 'PCRF', 'PGW', 'UPF']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1}（多值→atom 应考虑 decision_driven）
