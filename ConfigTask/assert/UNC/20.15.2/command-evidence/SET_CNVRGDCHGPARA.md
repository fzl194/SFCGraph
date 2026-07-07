# 命令证据包：SET CNVRGDCHGPARA
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/全局配置/设置融合计费全局参数（SET CNVRGDCHGPARA）_09653056.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置融合计费全局参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 参数OFLRGTIMECALC和CHGDATAREFFMT功能仅针对新用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MULTIUPFQUOTAM | ROAMHSMFQBC | MLOCMISSPRC | CHGDATAREFGEN | STARTTRIGGER | IPV6ITFID | RGTRIGGERFILL | OF

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| MULTIUPFQUOTAM | 多UPF场景配额管理 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “QUOTAINDEP（独立配额）”：各UPF独立使用CHF下发的配额 |
| ROAMHSMFQBC | 漫游用户归属地QBC计费 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “DISABLE（不使能）”：漫游用户在归属地关闭QBC功能。 |
| MLOCMISSPRC | 位置信息必选信元缺失处理 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “ABSENCE（不携带）”：缺失的必选位置信息不携带。 |
| CHGDATAREFGEN | ChargingDataRef生成方式 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- CHF（CHF生成ChargingDataRef） |
| STARTTRIGGER | 携带Start Trigger开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- DISABLE（不使能） |
| IPV6ITFID | IPv6地址Interface Identifier | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | 对于N40接口，在UPF/PGW-U不产生流量时，仍然可能会与CHF有交互，此时携带的interfa |
| RGTRIGGERFILL | RG级Trigger填写方式 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “DISABLE（不使能）”：当仅对PDU会话有效的Trigger发生时，生成的业务容器 |
| OFLRGTIMECALC | 离线RG时长计算方式 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “PACKETTRIGGERED（PACKETTRIGGERED）”：统计周期内收到第一 |
| RPTBASEDONGU | 基于GrantedUnit上报用量 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “DISABLE（不使能）”：不使能，则不基于GrantedUnit上报用量，即按实际用 |
| DEFERPDUTRIG | 延时上报PDU级Trigger携带方式 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “PDULVLNOTCARRY（PDU级不携带）”：PDU级延时上报的Trigger不在 |
| PDULIMITTRIG | PDU级门限Trigger适用范围 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “ONLINE（在线计费用户）”：PDU级门限Trigger适用于在线计费用户。 |
| RGLIMITTRIG | RG级门限Trigger适用范围 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “OFFLINE（离线计费用户）”：RG级门限Trigger适用于离线计费用户。 |
| MERGERGVTSW | RG VT事件合并上报开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “DISABLE（不使能）”：每个RG VT事件单独上报CHF，不做消息合并。 |
| IGNORERSPAVP | 忽略CHF响应消息的信元列表 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “INVOCATIONNUM（忽略Invocation Sequence Number） |
| BADRSPACT | CHF响应消息信元错误的处理动作 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “TERMINATE（去活会话）”：去活PDU会话。 |
| SPTABNTRIGGER | Trigger中是否支持填写AbnormalRelease | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “ENABLE（使能）”：支持Trigger填写AbnormalRelease。 |
| TIMEROUNDMODE | 控制Nchf消息中时间戳的计算方式 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “ROUNDOFF（四舍五入）”：Nchf消息中时间戳相关的信元，将毫秒转换为秒时按四舍 |
| DELDYNRULENTYUP | 删除动态规则是否通知用户面 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “ENABLE（使能）”：通知UPF删除URR。 |
| IGNORETRIGGER | 忽略CHF下发的Trigger列表 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “MAXNUMCCC（计费条件改变阈值）”：忽略CHF响应消息中的MAX_NUMBER_ |
| NOSRVRPTSW | 无业务上报开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “ENABLE（使能）”：上报CHF。 |
| CHGDATAREFFMT | ChargingDataRef格式 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “CHGDATAREF_FMT_DEFAULT（ChargingDataRef默认格式） |
| WAITUPDRSPSW | 去活等待更新消息响应开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- DISABLE（不使能） |
| CHGDATAREFUSE | ChargingDataRef使用方式 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- SMF（使用SMF生成的ChargingDataRef） |
| IGNOREERRTRIGS | 忽略CHF下发非法Triggers | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- DISABLE（不使能） |
| CONTINUEALARM | 缓存未开启放通告警开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVR | <br>- “DISABLE（不使能）”：不使能，则不开启“融合计费用户放通不计费”告警功能。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/计费事件触发条件_90776688.md`**
- 操作步骤上下文（±2 行原文）：
  L67:
    > | Abort request is received from the CHF | 收到CHF发送的中止计费会话请求 | Session | 立即上报 | 否 | 否 | Charging Data Request [Termination] |
    > 
    > **SET CNVRGDCHGPARA** 命令的 “IGNORETRIGGER” 参数用于SMF处理CHF响应消息时，忽略CHF下发指定的Trigger控制，使用SMF本地通过 **ADD PDUTRIGGER** 和 **ADD RGTRIGGER** 命令配置的Trigger生效。该参数是位域类型的取值，可配置的忽略CHF下发的Trigger列表为：计费条件改变阈值、会话级时间阈值、会话级流量阈值、RG级时间阈值、RG级流量阈值、配额保持时长。
    > 
    > 当CHF在响应消息中携带了Trigger列表，但未携带 “IGNORETRIGGER” 参数配置的忽略Trigger，则该被忽略的Trigger仍然采用本地配置值。

**md：`WSFD-011206/计费会话创建流程_01_10001.md`**
- 操作步骤上下文（±2 行原文）：
  L224:
    >   | "volumeQuotaThreshold":2000 | 代表流量配额门限为2000字节。 |
    >   > **说明**
    >   > 当CHF返回的响应消息携带了异常信元，导致SMF无法计费时，如果 **SET CNVRGDCHGPARA** 命令的 “BADRSPACT” 参数配置为 “CONTINUE” ，用户业务会继续进行，不会被去激活，并且不再进行配额管理。
    > 12. SMF本地保存配额信息，向UPF发送[PFCP Session Modification Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)消息，请求修改PFCP会话，消息中包含Create PDR、Create FAR、Create URR，以及它们之间的关联关系，URR中包含计费事件和计费参数，FAR中包含欠费处理策略。其中，用于指示UPF如何上报的用量上报规则Create URR包含的主要信元如[表6](#ZH-CN_TOPIC_0278888683__table5217133513420)所示。
    >   *表6 Create URR包含的主要信元*

**md：`WSFD-011206/计费会话更新流程_01_10002.md`**
- 操作步骤上下文（±2 行原文）：
  L141:
    >   > **说明**
    >   > - SMF发起更新计费会话的机制由计费Trigger定义，当计费Trigger发生时，SMF立即或延迟向CHF发送消息。
    >   > - SMF上报计费信息时，可以通过**SET CNVRGDCHGPARA**命令的“RPTBASEDONGU”参数配置上报的方式。
    >   >     - 不使能：SMF基于实际使用量上报。
    >   >     - 使能：SMF基于CHF下发的GrantedUnit做配额管理，用量上报不会超过CHF下发的配额。
  L186:
    > 1. SMF通过**ADD CCT**命令本地配置RG级配额的有效时长，SMF收到CHF下发的配额后会按照有效时长启动定时器，超时后SMF将向UPF查询配额用量并上报CHF。即SMF首先向UPF发送[PFCP Session Modification Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)消息，发起计费即时查询，查询配额用量。
    > 2. UPF向SMF返回[PFCP Session Modification Response](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)消息，根据指示上报计费信息。
    > 3. SMF向CHF发送[Nchf_ConvergedCharging_ChargingDataUpdate Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_f4a8bbee/Nchf_ConvergedCharging_ChargingDataUpdate Request_23690004.md)消息，更新计费会话，申请新的配额。当**SET CNVRGDCHGPARA**命令“MERGERGVTSW”参数配置为“ENABLE”时，支持对同时发生的RG级VT事件进行合并，一起上报给CHF。当“MERGERGVTSW”参数配置为“DISABLE”时，每个RG级VT事件单独上报CHF，不做消息合并。
    > 4. CHF对SMF上报的用量进行扣费处理，并更新CHF-CDR。CHF会生成一张CDR原始话单，同时转换生成CDR最终话单，存储到最终话单临时文件中。当最终话单临时文件达到转正阈值（默认1M大小或半小时），则转正为最终话单文件。
    > 5. CHF返回[Nchf_ConvergedCharging_ChargingDataUpdate Response](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_f4a8bbee/Nchf_ConvergedCharging_ChargingDataUpdate Response_23370256.md)消息，携带授权的配额。

**md：`WSFD-011206/计费会话释放流程_01_10003.md`**
- 操作步骤上下文（±2 行原文）：
  L131:
    >   > 融合计费场景中，当用户采用离线计费，即无配额管理时， [Nchf_ConvergedCharging_ChargingDataRelease Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_86c6dbcf/Nchf_ConvergedCharging_ChargingDataRelease Request_71969829.md) 消息中的quotaManagementIndicator信元标识为 **OFFLINE_CHARGING** 。
    >   >
    >   > 在 [Nchf_ConvergedCharging_ChargingDataRelease Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_86c6dbcf/Nchf_ConvergedCharging_ChargingDataRelease Request_71969829.md) 消息中，当用户正常去活时，triggerType信元填写FINAL；当用户异常去活时，由 **ADD N40DIAGTRIGGER** 命令的 “RELEASETRIGGER” 参数和 **SET CNVRGDCHGPARA** 命令的 “SPTABNTRIGGER” 参数控制triggerType信元填写FINAL或AbnormalRelease， **ADD N40DIAGTRIGGER** 命令优先级更高，具体控制原则如下：
    >   >
    >   > - 当**ADD N40DIAGTRIGGER**配置用户去活原因时，按照“RELEASETRIGGER”参数配置生效。
  L134:
    >   >
    >   > - 当**ADD N40DIAGTRIGGER**配置用户去活原因时，按照“RELEASETRIGGER”参数配置生效。
    >   > - 当**ADD N40DIAGTRIGGER**未配置用户去活原因时，如果**SET CNVRGDCHGPARA**命令的“SPTABNTRIGGER”参数配置为ENABLE，则支持triggerType填写AbnormalRelease；如果配置为DISABLE，则不支持triggerType填写AbnormalRelease，将triggerType改为FINAL。
    > 5. CHF对SMF上报的用量进行扣费处理，并关闭CHF-CDR。
    > 6. CHF向SMF返回[Nchf_ConvergedCharging_ChargingDataRelease Response](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_86c6dbcf/Nchf_ConvergedCharging_ChargingDataRelease Response_71849853.md)消息，消息携带的信元举例如下所示：

**md：`WSFD-011206/配置异常返回码和异常信元动作_93260161.md`**
- 数据规划表（该命令的参数行）：
  | ****SET CNVRGDCHGPARA**** | 忽略CHF响应消息的信元列表（IGNORERSPAVP） | FUI | 全网规划 | 配置SMF处理CHF响应消息时，忽略CHF下发的指定信元。 |
  | ****SET CNVRGDCHGPARA**** | CHF响应消息信元错误的处理动作（BADRSPACT） | TERMINATE | 全网规划 | 如果CHF返回的响应消息携带了异常信元，导致SMF无法计费时：<br>- “BADRSPACT”参数配置为“TERMINATE”时，PDU会话去活。<br>- “BADRSPACT”参数配置为“CONTINUE”时，用户业务会继续进行，并且不再进行配额管理。 |
- 任务示例脚本（该命令行）：
  `SET CNVRGDCHGPARA: IGNORERSPAVP=FUI, BADRSPACT=TERMINATE;`
- 操作步骤上下文（±2 行原文）：
  L53:
    >   ****ADD RGRCACT****
    > 5. **可选：** 配置忽略CHF响应消息的信元列表。
    >   ****SET CNVRGDCHGPARA****
    >   > **说明**
    >   > ****SET CNVRGDCHGPARA**** 命令的 “IGNORERSPAVP” 参数的取值范围是位域类型，支持如下参数单独配置或同时配置：
  L55:
    >   ****SET CNVRGDCHGPARA****
    >   > **说明**
    >   > ****SET CNVRGDCHGPARA**** 命令的 “IGNORERSPAVP” 参数的取值范围是位域类型，支持如下参数单独配置或同时配置：
    >   >
    >   > - 当“IGNORERSPAVP”参数配置为“INVOCATIONNUM”时，表示忽略CHF响应消息中的Invocation Sequence Number，不检查是否跟请求消息一致。
  L99:
    > 
    > ```
    > SET CNVRGDCHGPARA: IGNORERSPAVP=FUI, BADRSPACT=TERMINATE;
    > ```

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 数据规划表（该命令的参数行）：
  | **SET CNVRGDCHGPARA** | CHGDATAREFGEN（ChargingDataRef生成方式） | SMF | 全网规划 | 指定由SMF生成ChargingDataRef。 |
- 任务示例脚本（该命令行）：
  `SET CNVRGDCHGPARA: CHGDATAREFGEN=SMF;`
- 操作步骤上下文（±2 行原文）：
  L63:
    >   **SET STGTRIGGER**
    > - 配置由SMF生成ChargingDataRef。
    >   **SET CNVRGDCHGPARA**
    > - 配置全局默认CHF组。
    >   **SET GLBDFTCHFGROUP**
  L112:
    > 
    > ```
    > SET CNVRGDCHGPARA: CHGDATAREFGEN=SMF;
    > ```
    > 

**md：`WSFD-011206/调测融合计费的缓存消息回放功能_90005269.md`**
- 操作步骤上下文（±2 行原文）：
  L41:
    >     - [**ADD PDUSCACT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级结果码处理动作/增加PDU异常返回码动作（ADD PDUSCACT）_09652165.md)命令“SCACT”参数配置为“FAILOVER”或“CONTINUE”。
    >     - [**SET N40MSGSTG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md)命令“STGSWITCH”参数配置为“ENABLE”。
    >     - [**SET CNVRGDCHGPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/全局配置/设置融合计费全局参数（SET CNVRGDCHGPARA）_09653056.md)命令“CHGDATAREFGEN”参数配置为“SMF”。
    > 3. 在OM Portal上创建用户跟踪任务。
    > 4. 测试终端使用 “apn-test” DNN接入网络。

### WSFD-109003

**md：`WSFD-109003/基于业务时长的计费（适用于融合计费）_66402116.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    >   > **说明**
    >   > - 对于基于用户的计费，使用时长从用户激活上线时开始统计，直到用户下线去激活时结束，即无论用户是否进行业务，全部时长均作为有效计费时间，如图中User的业务统计时长。
    >   > - 离线RG的业务时长统计方式也可以修改为与带配额时长统计方式相同，通过[**SET CNVRGDCHGPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/全局配置/设置融合计费全局参数（SET CNVRGDCHGPARA）_09653056.md)命令的“OFLRGTIMECALC”参数控制，统计方式可以配置为从UPF首次收到授权的配额成功时开始，直到用户去激活时或者该配额管理实例终止结束。

## ④ 自动比对
- 命令真相参数（25）：['BADRSPACT', 'CHGDATAREFFMT', 'CHGDATAREFGEN', 'CHGDATAREFUSE', 'CONTINUEALARM', 'DEFERPDUTRIG', 'DELDYNRULENTYUP', 'IGNOREERRTRIGS', 'IGNORERSPAVP', 'IGNORETRIGGER', 'IPV6ITFID', 'MERGERGVTSW', 'MLOCMISSPRC', 'MULTIUPFQUOTAM', 'NOSRVRPTSW', 'OFLRGTIMECALC', 'PDULIMITTRIG', 'RGLIMITTRIG', 'RGTRIGGERFILL', 'ROAMHSMFQBC', 'RPTBASEDONGU', 'SPTABNTRIGGER', 'STARTTRIGGER', 'TIMEROUNDMODE', 'WAITUPDRSPSW']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 3}（多值→atom 应考虑 decision_driven）
