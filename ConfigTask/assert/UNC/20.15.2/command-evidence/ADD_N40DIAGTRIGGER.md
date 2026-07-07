# 命令证据包：ADD N40DIAGTRIGGER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/N40诊断值Trigger/增加N40去活原因的映射关系（ADD N40DIAGTRIGGER）_35102633.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加用户去活时内部诊断字段取值到去活原因的映射关系。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入1001条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| DIAGNOSTICS | 诊断原因值 | local_planned | required | 无 | 整数类型，取值范围是0~1000。 |
| RELEASETRIGGER | 去活原因 | local_planned | required | 无 | <br>- FINAL（正常去活） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/计费会话释放流程_01_10003.md`**
- 操作步骤上下文（±2 行原文）：
  L131:
    >   > 融合计费场景中，当用户采用离线计费，即无配额管理时， [Nchf_ConvergedCharging_ChargingDataRelease Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_86c6dbcf/Nchf_ConvergedCharging_ChargingDataRelease Request_71969829.md) 消息中的quotaManagementIndicator信元标识为 **OFFLINE_CHARGING** 。
    >   >
    >   > 在 [Nchf_ConvergedCharging_ChargingDataRelease Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_86c6dbcf/Nchf_ConvergedCharging_ChargingDataRelease Request_71969829.md) 消息中，当用户正常去活时，triggerType信元填写FINAL；当用户异常去活时，由 **ADD N40DIAGTRIGGER** 命令的 “RELEASETRIGGER” 参数和 **SET CNVRGDCHGPARA** 命令的 “SPTABNTRIGGER” 参数控制triggerType信元填写FINAL或AbnormalRelease， **ADD N40DIAGTRIGGER** 命令优先级更高，具体控制原则如下：
    >   >
    >   > - 当**ADD N40DIAGTRIGGER**配置用户去活原因时，按照“RELEASETRIGGER”参数配置生效。
  L133:
    >   > 在 [Nchf_ConvergedCharging_ChargingDataRelease Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_86c6dbcf/Nchf_ConvergedCharging_ChargingDataRelease Request_71969829.md) 消息中，当用户正常去活时，triggerType信元填写FINAL；当用户异常去活时，由 **ADD N40DIAGTRIGGER** 命令的 “RELEASETRIGGER” 参数和 **SET CNVRGDCHGPARA** 命令的 “SPTABNTRIGGER” 参数控制triggerType信元填写FINAL或AbnormalRelease， **ADD N40DIAGTRIGGER** 命令优先级更高，具体控制原则如下：
    >   >
    >   > - 当**ADD N40DIAGTRIGGER**配置用户去活原因时，按照“RELEASETRIGGER”参数配置生效。
    >   > - 当**ADD N40DIAGTRIGGER**未配置用户去活原因时，如果**SET CNVRGDCHGPARA**命令的“SPTABNTRIGGER”参数配置为ENABLE，则支持triggerType填写AbnormalRelease；如果配置为DISABLE，则不支持triggerType填写AbnormalRelease，将triggerType改为FINAL。
    > 5. CHF对SMF上报的用量进行扣费处理，并关闭CHF-CDR。
  L134:
    >   >
    >   > - 当**ADD N40DIAGTRIGGER**配置用户去活原因时，按照“RELEASETRIGGER”参数配置生效。
    >   > - 当**ADD N40DIAGTRIGGER**未配置用户去活原因时，如果**SET CNVRGDCHGPARA**命令的“SPTABNTRIGGER”参数配置为ENABLE，则支持triggerType填写AbnormalRelease；如果配置为DISABLE，则不支持triggerType填写AbnormalRelease，将triggerType改为FINAL。
    > 5. CHF对SMF上报的用量进行扣费处理，并关闭CHF-CDR。
    > 6. CHF向SMF返回[Nchf_ConvergedCharging_ChargingDataRelease Response](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_86c6dbcf/Nchf_ConvergedCharging_ChargingDataRelease Response_71849853.md)消息，消息携带的信元举例如下所示：

## ④ 自动比对
- 命令真相参数（2）：['DIAGNOSTICS', 'RELEASETRIGGER']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
