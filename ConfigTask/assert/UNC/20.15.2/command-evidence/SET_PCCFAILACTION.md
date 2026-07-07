# 命令证据包：SET PCCFAILACTION
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用来设置PCC故障处理动作。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- LOCAL_PCC代表本地PCC用户，有PCC功能，占用PCC基本功能的License，但不与PCRF/PCF交互，EPS场景下的本地PCC用户支持业务触发的QoS保证功能。
- 对于Gx接口的回滚策略，当SET FHBYPASS的GXERRRC参数配置为ENABLE时，SET FHBYPASS命令优先级高于此命令。
- 该命令存在系统初

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SELPEERFAILACT | 选择PCRF/PCF失败动作 | global_planned | optional | 无 | 枚举类型。 |
| SELPEERLOCPCC | 选择PCRF/PCF失败回滚为Local PCC用户类型 | global_planned | conditional | 无 | 枚举类型。 |
| SELPEERRDSPCC | 选择PCRF/PCF失败回滚为RADIUS PCC用户类型 | global_planned | conditional | 无 | 枚举类型。 |
| INITIALFAILACT | Initial流程故障处理动作 | global_planned | optional | 无 | 枚举类型。 |
| INITFAILLOCPCC | Initial流程故障回滚为Local PCC用户类型 | global_planned | conditional | 无 | 枚举类型。 |
| INITFAILRDSPCC | Initial流程故障回滚为RADIUS PCC用户类型 | global_planned | conditional | 无 | 枚举类型。 |
| UPDATEFAILACT | Update流程故障处理动作 | global_planned | optional | 无 | 枚举类型。 |
| UPDFAILLOCPCC | Update流程故障回滚为Local PCC用户类型 | global_planned | conditional | 无 | 枚举类型。 |
| UMRFAILACT | 流量上报失败时处理动作 | global_planned | optional | 无 | 枚举类型。 |
| SCPFAILOVERSW | SCP故障重选开关 | global_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-213002

**md：`WSFD-213002/激活 N7接口PCF Group_13564475.md`**
- 数据规划表（该命令的参数行）：
  | **[**SET PCCFAILACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 全网规划 | 设置PCC故障处理动作。 |
  | **[**SET PCCFAILACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | LOCAL_PCC | 全网规划 | 设置PCC故障处理动作。 |
- 任务示例脚本（该命令行）：
  `SET PCCFAILACTION: UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=LOCAL_PCC;`
- 操作步骤上下文（±2 行原文）：
  L46:
    >   **[**SET NFDISCPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/NF发现策略管理/设置NF的服务发现策略（SET NFDISCPLCY）_09651764.md)**
    > 6. 设置PCC故障处理动作。
    >   **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
    > 
    > ## [任务示例](#ZH-CN_OPI_0213564475)
  L89:
    > 
    > ```
    > SET PCCFAILACTION: UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=LOCAL_PCC; 
    > ```

### WSFD-109304

**md：`WSFD-109304/特性概述_95611472.md`**
- 操作步骤上下文（±2 行原文）：
  L95:
    > 2. 有PCRF/PCF部署时，会话创建流程中UNC与PCRF/PCF正常交互，PCRF/PCF没有下发动态规则触发any to any GBR专有承载的创建。
    >   如果PCRF/PCF没有下发动态规则触发创建any to any GBR专有承载， UNC 遵从PCRF/PCF的指示，不主动触发创建。
    > 3. 有PCRF/PCF部署时，会话创建流程中UNC与PCRF/PCF交互失败，根据命令[**SET PCCFAILACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)的配置回滚为本地用户激活。
    >   按照无PCRF/PCF部署的场景中描述的方式触发创建any to any GBR专有承载。
    > 4. 无PCRF/PCF部署时，根据命令[**SET DFTGBRBEARER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/缺省GBR承载/设置缺省GBR承载参数（SET DFTGBRBEARER）_09897061.md)的相关配置，在缺省承载创建成功后立即触发创建any to any GBR专有承载，此场景下的承载创建不依赖于业务触发，所创建的GBR专有承载的生命周期和缺省承载一致。

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > - [**SET DFTGLBPCRFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md)
    > - [**ADD PCRFGRPBNDAPN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
    > - [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)
    > - [**ADD RESULTCODECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
    > - [**SET FHBYPASS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)

**md：`WSFD-109101/实现原理_29056158.md`**
- 操作步骤上下文（±2 行原文）：
  L127:
    > | N4接口响应超时或返回异常返回码 | UNC<br>发送PFCP Session Modification Request消息给GGSN-U/PGW-U，GGSN-U/PGW-U响应超时或者返回异常响应，或者GGSN-U/PGW-U发送PFCP Session Report Request消息给<br>UNC<br>，响应超时或者返回异常响应。 | 如果<br>UNC<br>发起消息，GGSN-U/PGW-U无响应或返回异常返回码，则<br>UNC<br>通过PFCP Session Deletion Request消息向GGSN-U/PGW-U发起去活请求。<br>如果GGSN-U/PGW-U发起消息，<br>UNC<br>无响应或返回异常返回码，则GGSN-U/PGW-U通过PFCP Session Report Request消息向<br>UNC<br>发起去活请求。 |
    > 
    > 在等待PCRF响应超时、Gx接口链路故障、CCA消息中携带异常返回码故障场景下， UNC 支持根据 [**SET FHBYPASS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md) 的配置改变异常处理策略。该命令仅用于故障场景下的紧急处理，优先级高于 [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 、 [**ADD RESULTCODECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) 的配置。由于该命令的配置将影响用户的控制策略，只有在获得了客户的书面认可后方可使用。
    > 
    > > **说明**

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 操作步骤上下文（±2 行原文）：
  L10:
    > ## [操作场景](#ZH-CN_OPI_0231422950)
    > 
    > 当用户初始激活或进行业务时，GGSN/PGW-C发送CCR请求消息给PCRF，在指定消息重传时间间隔时间内未收到PCRF的响应消息，即可判断PCRF服务器状态异常。如果 [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) 命令中 “FAILOVERSW” 参数值为 “ENABLE” ，则进行failover处理；否则按照 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令设置的动作进行处理。
    > 
    > GGSN/PGW-C向备PCRF重发消息，如果备PCRF也没有响应或者备PCRF因状态异常、消息发送速率超过wal值等导致不可用，可以根据 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令配置情况去活用户或者转为非PCC用户/本地PCC用户继续进行业务。
  L12:
    > 当用户初始激活或进行业务时，GGSN/PGW-C发送CCR请求消息给PCRF，在指定消息重传时间间隔时间内未收到PCRF的响应消息，即可判断PCRF服务器状态异常。如果 [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) 命令中 “FAILOVERSW” 参数值为 “ENABLE” ，则进行failover处理；否则按照 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令设置的动作进行处理。
    > 
    > GGSN/PGW-C向备PCRF重发消息，如果备PCRF也没有响应或者备PCRF因状态异常、消息发送速率超过wal值等导致不可用，可以根据 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令配置情况去活用户或者转为非PCC用户/本地PCC用户继续进行业务。
    > 
    > 实现failover功能需要具备以下几个条件：

**md：`WSFD-109101/配置异常场景数据_31422947.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 全网规划 | 配置激活过程中根据号段匹配选择PCRF/PCF-Group和realm失败情况下系统执行的动作。 |
  | [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) | 选择PCRF/PCF失败回滚为Local PCC用户类型（SELPEERLOCPCC） | LOCAL_PCC | 全网规划 | 配置激活过程中根据号段匹配选择PCRF/PCF-Group和realm失败情况下系统执行的动作。 |
  | [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) | 选择PCRF/PCF失败回滚为RADIUS PCC用户类型（SELPEERRDSPCC） | LOCAL_PCC | 全网规划 | 配置激活过程中根据号段匹配选择PCRF/PCF-Group和realm失败情况下系统执行的动作。 |
  | [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 全网规划 | 配置激活过程中Gx链路故障、流控丢消息或响应超时情况下系统执行的动作。 |
  | [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) | Initial流程故障回滚为Local PCC用户类型（INITFAILLOCPCC） | LOCAL_PCC | 全网规划 | 配置激活过程中Gx链路故障、流控丢消息或响应超时情况下系统执行的动作。 |
  | [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) | Initial流程故障回滚为RADIUS PCC用户类型（INITFAILRDSPCC） | LOCAL_PCC | 全网规划 | 配置激活过程中Gx链路故障、流控丢消息或响应超时情况下系统执行的动作。 |
  | [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 全网规划 | 配置激活过程中Gx链路故障、流控丢消息或响应超时情况下系统执行的动作。 |
  | [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | LOCAL_PCC | 全网规划 | 配置激活过程中Gx链路故障、流控丢消息或响应超时情况下系统执行的动作。 |
- 任务示例脚本（该命令行）：
  `SET PCCFAILACTION:SELPEERFAILACT=DEFAULT,INITIALFAILACT=ROLLBACK,INITFAILLOCPCC=LOCAL_PCC,INITFAILRDSPCC=LOCAL_PCC,UPDATEFAILACT=ROLLBACK,UPDFAILLOCPCC=LOCAL_PCC;`
- 操作步骤上下文（±2 行原文）：
  L74:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 配置GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式，缺省使用默认值。
    >       [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)
    >     3. **可选：**配置PCC用户回滚后的在线保持时长，缺省使用默认值。
    >       [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
  L94:
    >   [**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)
    >   > **说明**
    >   > - 本命令优先级高于[**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)和[**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)。
    >   > - 由于配置[**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)将影响用户的控制策略，只有在取得了客户的书面认可后方可使用。
    >   > - GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。
  L114:
    > 1. 配置Gx接口链路故障或CCA消息响应超时系统的处理动作。
    >   ```
    >   SET PCCFAILACTION:SELPEERFAILACT=DEFAULT,INITIALFAILACT=ROLLBACK,INITFAILLOCPCC=LOCAL_PCC,INITFAILRDSPCC=LOCAL_PCC,UPDATEFAILACT=ROLLBACK,UPDFAILLOCPCC=LOCAL_PCC;
    >   ```
    >   ```

**md：`WSFD-109101/WSFD-109101 PCC基本功能特性概述（适用于5G）_71770359.md`**
- 操作步骤上下文（±2 行原文）：
  L99:
    >   **PCF发现和选择**
    >   AMF/SMF在首次向PCF发起交互之前，需要先通过PCF发现和选择流程，确定与哪个PCF进行交互，如 [表1](#ZH-CN_CONCEPT_0171770359__table1340181019275) 所示。
    >   SMF支持PCF主备容灾。SMF支持PCF主备容灾时，对同一条消息执行一次failover。例如，建立PDU会话时，SMF向当前PCF发送消息，若超时未收到响应消息，则选择另一个PCF；如果向新选择的PCF发送成功，则新选中的PCF被记录为主用PCF。如果SMF向新选择的PCF发送消息也超时，则根据 [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 配置决定是回落到本地PCC，还是会话建立失败。
    >   *表1 AMF/SMF发现和选择PCF的方式和因素*
    > 

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L62:
    > **[LST PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/查询PCC功能（LST PCCFUNC）_21559291.md)**
    > 
    > **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
    > 
    > **[LST PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/查询PCC故障处理（LST PCCFAILACTION）_33684768.md)**

**md：`WSFD-201207/实现原理（N7接口）_85304236.md`**
- 操作步骤上下文（±2 行原文）：
  L127:
    >   **步骤** **5** ：SMF发送Nsmf_PDUSession_UpdateSmContext Response给AMF。
    >   **步骤** **6** ：（可选）QoS改变需要通知(R)AN侧时，进行该流程，(R)AN侧接受策略修改。
    >   **步骤** **7-8** ：（可选）QoS参数修改涉及UPF侧修改时，SMF将更新的QoS信息通知UPF，根据 **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** 和 **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** 中 “Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC）” 参数值决定是否使用激活时安装的PCC策略：值为 “LOCAL_PCC” 时，通知UPF删除激活时安装的动态PCC策略，安装本地配置的静态PCC策略（用于语音专有QoS Flow\专有承载创建的静态PCC策略）；值为 “INHERIT_PCC” 时，继续使用激活时安装的PCC策略。
    >   **步骤** **9** ：（可选）QoS改变需要通知UE侧时，进行该流程，UE侧接受策略修改。
    > 

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 本端规划 | 配置PCRF故障处理动作。 |
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 本端规划 | 配置PCRF故障处理动作。 |
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 本端规划 | 配置PCRF故障处理动作。 |
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | INHERIT_PCC | 本端规划 | 配置PCRF故障处理动作。 |
- 任务示例脚本（该命令行）：
  `SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;`
  `SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;`
- 操作步骤上下文（±2 行原文）：
  L254:
    > 
    >   a. 配置全局PCRF故障处理动作。
    >       **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
    >     b. 配置全局Holding Time。
    >       **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
  L385:
    > 
    >       ```
    >       SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;
    >       ```
    >       //配置全局Holding Time。
  L499:
    > 
    >       ```
    >       SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;
    >       ```
    >       //配置全局Holding Time。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 本端规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 本端规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 本端规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | INHERIT_PCC | 本端规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
  | **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | SCP故障重选开关（SCPFAILOVERSW） | SCP_FAILOVER | 全网规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
- 任务示例脚本（该命令行）：
  `SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;`
  `SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;`
  `SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;`
  `SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;`
  `SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;`
  `SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;`
- 操作步骤上下文（±2 行原文）：
  L275:
    >       [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    >     b. 配置全局PCF故障处理动作。
    >       **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
    >     c. 配置全局Holding Time。
    >       **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
  L419:
    > 
    >             ```
    >             SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;
    >             ```
    >             //配置全局Holding Time。
  L471:
    > 
    >             ```
    >             SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;
    >             ```
    >             //配置全局Holding Time。

## ④ 自动比对
- 命令真相参数（10）：['INITFAILLOCPCC', 'INITFAILRDSPCC', 'INITIALFAILACT', 'SCPFAILOVERSW', 'SELPEERFAILACT', 'SELPEERLOCPCC', 'SELPEERRDSPCC', 'UMRFAILACT', 'UPDATEFAILACT', 'UPDFAILLOCPCC']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 11, '本端规划': 8}（多值→atom 应考虑 decision_driven）
