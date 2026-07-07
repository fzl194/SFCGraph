# 命令证据包：SET FAILHANDLING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：![](设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.assets/notice_3.0-zh-cn_2.png)

配置N40接口超时时长不合理可能导致在超时场景下，激活响应的总时长过长。在前期规划时，建议产品配置的等待右侧网元的最大时长小于产品ADD GTPCT3N3命令配置的T3N3时长及左侧（MME\SGSN\AMF等）的T3N3时长。

**适用NF
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令的CCTMPLTNAME参数使用ADD CCT命令配置生成。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCTMPLTNAME | FHACTION | FAILOVERSUP | AUTOFAILBACK | TXTIMER | HOLDINGTIME | RANGETIME | CNVCHGRECOVER | RECOVER

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | local_planned | required | 无。 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| FHACTION | FH处理动作 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- “TERMINATE（去活PDU会话）”：去活PDU会话 |
| FAILOVERSUP | 支持failover使能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- DISABLE（不使能） |
| AUTOFAILBACK | failback使能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- DISABLE（不使能） |
| TXTIMER | Tx定时器时长(秒) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | 整数类型，取值范围是0~20。 |
| HOLDINGTIME | 用户保持时长(分钟) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | 整数类型，取值范围是0~2880。 |
| RANGETIME | 用户保持调整时长(分钟) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | 整数类型，取值范围是0~60。 |
| CNVCHGRECOVER | 融合计费自动恢复功能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- DISABLE（不使能） |
| RECOVERINTERVAL | 融合计费自动恢复间隔 (分钟) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | 整数类型，取值范围是0~60。 |
| UPDCONTTERM | Update消息触发业务放通结束计费会话开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- DISABLE（不使能） |
| SCPFAILOVERSW | SCP故障重选开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- SCP_NOT_FAILOVER（SCP故障不进行重选） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > - [**ADD RGTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/增加RG级的trigger参数（ADD RGTRIGGER）_09653787.md)
    > - [**SET CTXSTARTRATING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置给OCS_CHF发送的消息初始携带的计费属性（SET CTXSTARTRATING）_09897210.md)
    > - [**SET FAILHANDLING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)
    > - [**SET N40MSGSTG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md)
    > - [**SET STGTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置融合计费消息缓存期间融合计费消息生成的trigger（SET STGTRIGGER）_34667406.md)

**md：`WSFD-011206/融合计费可靠性（未部署NCG）_75816427.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > ![](融合计费可靠性（未部署NCG）_75816427.assets/zh-cn_image_0275893663_2.png)
    > 
    > 场景一：当SMF感知到主用CHF异常（ **SET FAILHANDLING** 配置的TXTIMER定时器超时），向备CHF重发计费请求消息。备用CHF正常处理、正常返回计费响应消息。
    > 
    > 场景二：当SMF超时（ **SET FAILHANDLING** 配置的TXTIMER定时器）未收到响应消息，向备CHF重发计费请求消息（ **SET FAILHANDLING** 配置FHACTION参数为CONTINUE或RETRY_AND_TERM）。备用CHF正常处理、正常返回计费响应消息。
  L40:
    > 场景一：当SMF感知到主用CHF异常（ **SET FAILHANDLING** 配置的TXTIMER定时器超时），向备CHF重发计费请求消息。备用CHF正常处理、正常返回计费响应消息。
    > 
    > 场景二：当SMF超时（ **SET FAILHANDLING** 配置的TXTIMER定时器）未收到响应消息，向备CHF重发计费请求消息（ **SET FAILHANDLING** 配置FHACTION参数为CONTINUE或RETRY_AND_TERM）。备用CHF正常处理、正常返回计费响应消息。
    > 
    > 场景三：当SMF收到的响应消息携带异常响应码时，向备CHF重发计费请求消息（ **ADD PDUSCACT** 配置SCACT参数为FAILOVER）。备用CHF正常处理、正常返回计费响应消息。
  L44:
    > 场景三：当SMF收到的响应消息携带异常响应码时，向备CHF重发计费请求消息（ **ADD PDUSCACT** 配置SCACT参数为FAILOVER）。备用CHF正常处理、正常返回计费响应消息。
    > 
    > P4：当SMF感知到主用CHF正常，会将计费消息发往主用CHF（ **SET FAILHANDLING** 配置AUTOFAILBACK），完成回切。
    > 
    > #### [计费消息缓存](#ZH-CN_TOPIC_0275816427)

**md：`WSFD-011206/使用全局CCT模板进行融合计费实例_93029782.md`**
- 数据规划表（该命令的参数行）：
  | **SET FAILHANDLING** | CCTMPLTNAME（融合计费模板名称） | cct-test | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。 |
  | **SET FAILHANDLING** | FHACTION（FH处理动作） | RETRY_AND_TERM | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。 |
  | **SET FAILHANDLING** | FAILOVERSUP（支持failover使能开关） | ENABLE | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。 |
  | **SET FAILHANDLING** | AUTOFAILBACK（failback使能开关） | ENABLE | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。 |
  | **SET FAILHANDLING** | TXTIMER（Tx定时器时长(秒)） | 5 | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。 |
  | **SET FAILHANDLING** | HOLDINGTIME（用户保持时长(分钟)） | 10 | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。 |
- 任务示例脚本（该命令行）：
  `SET FAILHANDLING: CCTMPLTNAME="global", FHACTION=RETRY_AND_TERM, FAILOVERSUP=ENABLE, AUTOFAILBACK=ENABLE, TXTIMER=5, HOLDINGTIME=10;`
- 操作步骤上下文（±2 行原文）：
  L96:
    > 
    > ```
    > SET FAILHANDLING: CCTMPLTNAME="global", FHACTION=RETRY_AND_TERM, FAILOVERSUP=ENABLE, AUTOFAILBACK=ENABLE, TXTIMER=5, HOLDINGTIME=10;
    > ```
    > 

**md：`WSFD-011206/配置异常返回码和异常信元动作_93260161.md`**
- 数据规划表（该命令的参数行）：
  | ****SET FAILHANDLING**** | 融合计费模板名称（CCTMPLTNAME） | cct-test | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时，向备CHF重发消息。 |
  | ****SET FAILHANDLING**** | FH处理动作（FHACTION） | CONTINUE | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时，向备CHF重发消息。 |
  | ****SET FAILHANDLING**** | 支持failover使能开关（FAILOVERSUP） | ENABLE | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时，向备CHF重发消息。 |
  | ****SET FAILHANDLING**** | failback使能开关（AUTOFAILBACK） | ENABLE | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时，向备CHF重发消息。 |
  | ****SET FAILHANDLING**** | Tx定时器时长(秒)（TXTIMER） | 5 | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时，向备CHF重发消息。 |
  | ****SET FAILHANDLING**** | 用户保持时长(分钟)（HOLDINGTIME） | 10 | 本端规划 | 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时，向备CHF重发消息。 |
- 任务示例脚本（该命令行）：
  `SET FAILHANDLING: CCTMPLTNAME="cct-test", FHACTION=CONTINUE, FAILOVERSUP=ENABLE, AUTOFAILBACK=ENABLE, TXTIMER=5, HOLDINGTIME=10;`
- 操作步骤上下文（±2 行原文）：
  L47:
    > 1. 进入“MML命令行-UNC”窗口。
    > 2. **可选：** 配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。
    >   ****SET FAILHANDLING****
    > 3. **可选：** 配置当SMF收到CHF的PDU级异常返回码时的动作。
    >   ****ADD PDUSCACT****
  L59:
    >   > - 当“IGNORERSPAVP”参数配置为“INVOCATIONNUM”时，表示忽略CHF响应消息中的Invocation Sequence Number，不检查是否跟请求消息一致。
    >   > - 当“IGNORERSPAVP”参数配置为“FUI”时，表示当CHF返回RG级异常返回码和FUI时，忽略CHF响应消息中的FinalUnitIndication，按照对应****ADD RGRCACT****配置的“RCACT”动作执行。当**ADD RGRCACT**未配置时，执行默认动作。
    >   > - 当“IGNORERSPAVP”参数配置为“SESSIONFAILOVER”时，表示忽略CHF响应消息中的SessionFailover，使用对应CCT模板通过****SET FAILHANDLING****配置的“FAILOVERSUP”动作，“FAILOVERSUP”表示主CHF故障时，向备CHF发送计费消息进行处理。
    >   > - 当“IGNORERSPAVP”参数配置为“FAILUREHANDLING”时，表示忽略CHF响应消息中的FailureHandling，使用对应CCT模板通过**SET FAILHANDLING**配置的“FHACTION”动作。
    > 
  L60:
    >   > - 当“IGNORERSPAVP”参数配置为“FUI”时，表示当CHF返回RG级异常返回码和FUI时，忽略CHF响应消息中的FinalUnitIndication，按照对应****ADD RGRCACT****配置的“RCACT”动作执行。当**ADD RGRCACT**未配置时，执行默认动作。
    >   > - 当“IGNORERSPAVP”参数配置为“SESSIONFAILOVER”时，表示忽略CHF响应消息中的SessionFailover，使用对应CCT模板通过****SET FAILHANDLING****配置的“FAILOVERSUP”动作，“FAILOVERSUP”表示主CHF故障时，向备CHF发送计费消息进行处理。
    >   > - 当“IGNORERSPAVP”参数配置为“FAILUREHANDLING”时，表示忽略CHF响应消息中的FailureHandling，使用对应CCT模板通过**SET FAILHANDLING**配置的“FHACTION”动作。
    > 
    > ## [任务示例](#ZH-CN_OPI_0193260161)

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 操作步骤上下文（±2 行原文）：
  L115:
    >       **ADD QUOTAEXHAUSTACT**
    >       > **说明**
    >       > 当计费事件触发SMF发起Charging Data Request[Update]更新消息申请配额，Total Volume到达后仍未收到CHF响应消息，且SMF本地通过 **SET FAILHANDLING** 命令配置的TXTIMER超时时长未到达时，RG配额耗尽后的默认动作根据 “ACTION” 参数配置生效。
    >       >
    >       > - 当参数配置为“BLOCK”时，SMF在N4接口下发的该业务的URR绑定的FAR动作为drop，即在线RG配额耗尽后阻塞业务，使业务不能继续进行。

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 数据规划表（该命令的参数行）：
  | **SET FAILHANDLING** | CCTMPLTNAME（融合计费模板名称） | cct-test | 本端规划 | 融合计费模板名称，<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>已经配置。 |
  | **SET FAILHANDLING** | FHACTION（FH处理动作） | CONTINUE | 固定取值 | 当CHF不可用，SMF允许用户继续使用业务，不再进行配额管理和配额上报。<br>固定配置，开启计费消息缓存的前提条件。 |
  | **SET FAILHANDLING** | TXTIMER（Tx定时器时长(秒)） | 5 | 本端规划 | 配置Tx定时器时长。 |
  | **SET FAILHANDLING** | UPDCONTTERM（Update消息触发业务放通结束计费会话开关） | ENABLE | 本端规划 | 配置Update消息触发的计费缓存场景，SMF发送Terminate消息结束计费会话。 |
  | **SET FAILHANDLING** | CNVCHGRECOVER（融合计费自动恢复功能开关） | ENABLE | 本端规划 | 配置CHF故障恢复后重建计费会话功能。 |
  | **SET FAILHANDLING** | RECOVERINTERVAL（融合计费自动恢复间隔 (分钟)） | 20 | 本端规划 | 配置CHF故障恢复后重建计费会话功能。 |
- 任务示例脚本（该命令行）：
  `SET FAILHANDLING: CCTMPLTNAME="cct-test", FHACTION=CONTINUE, TXTIMER=5, UPDCONTTERM=ENABLE, CNVCHGRECOVER=ENABLE, RECOVERINTERVAL=5;`
- 操作步骤上下文（±2 行原文）：
  L55:
    > - 进入 “MML命令行-UNC” 窗口。
    > - 配置当CHF故障，SMF放通业务，不进行配额管理和配额上报；配置当CHF故障恢复后重建计费会话功能。
    >   **SET FAILHANDLING**
    > - 配置当SMF收到CHF的PDU级异常返回码时的动作。
    >   **ADD PDUSCACT**
  L88:
    > 
    > ```
    > SET FAILHANDLING: CCTMPLTNAME="cct-test", FHACTION=CONTINUE, TXTIMER=5, UPDCONTTERM=ENABLE, CNVCHGRECOVER=ENABLE, RECOVERINTERVAL=5;
    > ```
    > 

**md：`WSFD-011206/调测融合计费的主备CHF的可靠性_89257222.md`**
- 操作步骤上下文（±2 行原文）：
  L51:
    > 7. 执行 [**LST CCT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/查询融合计费模板（LST CCT）_09653820.md) 命令查询SMF本地配置是否使能failover功能，查看与当前用户所使用的融合计费模板对应的 “支持failover使能开关” 是否配置为 “使能”
    >     - 如果配置为使能，请执行[步骤 8](#ZH-CN_OPI_0289257222__step13334556133920)。
    >     - 如果配置为不使能，请执行与当前用户所使用的融合计费模板对应的[**SET FAILHANDLING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)命令，将“FAILOVERSUP”参数配置为“ENABLE”，即SMF支持在主用CHF故障时向备用CHF发送计费消息。
    > 8. 在告警服务台上检查UNC是否产生 [ALM-100072 目的NF服务不可达](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100072 目的NF服务不可达_26182301.md) 告警，查询备CHF的N40接口的通信是否存在故障。
    >     - 如果存在告警，请根据告警信息进行处理，待告警恢复后再次执行[步骤 3](#ZH-CN_OPI_0289257222__step2585105420194)。

**md：`WSFD-011206/调测融合计费的缓存消息回放功能_90005269.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开内容计费基本功能对应的License配置开关。
    > 2. 开启计费缓存功能。
    >     - [**SET FAILHANDLING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)命令“FHACTION”参数配置为“CONTINUE”。
    >     - [**ADD PDUSCACT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级结果码处理动作/增加PDU异常返回码动作（ADD PDUSCACT）_09652165.md)命令“SCACT”参数配置为“FAILOVER”或“CONTINUE”。
    >     - [**SET N40MSGSTG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md)命令“STGSWITCH”参数配置为“ENABLE”。

## ④ 自动比对
- 命令真相参数（11）：['AUTOFAILBACK', 'CCTMPLTNAME', 'CNVCHGRECOVER', 'FAILOVERSUP', 'FHACTION', 'HOLDINGTIME', 'RANGETIME', 'RECOVERINTERVAL', 'SCPFAILOVERSW', 'TXTIMER', 'UPDCONTTERM']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 17, '固定取值': 1}（多值→atom 应考虑 decision_driven）
