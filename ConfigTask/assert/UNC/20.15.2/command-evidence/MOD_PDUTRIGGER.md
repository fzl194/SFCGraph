# 命令证据包：MOD PDUTRIGGER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/修改PDU会话级的trigger参数（MOD PDUTRIGGER）_09653719.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于修改PDU会话级的trigger参数。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后只对新激活用户生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| QOSCHG | QoS更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| ULCHG | 用户位置更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| SRVNDCHG | 服务节点更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| PRACHG | 区域用户位置上报更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| PSDATAOFFCHG | PS数据关闭状态更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| UETZCHG | 用户时区更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| PLMNCHG | PLMN更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| RATCHG | RAT更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| ADDUPF | 添加UPF | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| TIMELIMIT | 时间阈值 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| VOLUMELIMIT | 流量阈值 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| EVENTLIMIT | 事件阈值 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| MAXNUMCCC | 计费条件改变阈值 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| UCITIMER | 业务停止时长 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| INSERTISMF | 插入I-SMF | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| REMOVALISMF | 删除I-SMF | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| CHANGEISMF | 更新I-SMF | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| SESSAMBRCHG | Session AMBR更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| SERVPLMNRTCTCHG | 服务PLMN速率控制更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| APNRATECTRLCHG | APN速率控制更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| TAICHG | 跟踪区标识更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| CGISAICHG | CGISAI更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| RAICHG | RAI更新 | local_planned | optional | 无 | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/调测融合计费的计费Trigger上报功能_89257220.md`**
- 操作步骤上下文（±2 行原文）：
  L63:
    > 6. 执行 [**LST PDUTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/查询PDU会话级的trigger参数（LST PDUTRIGGER）_09653638.md) / [**LST RGTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/查询RG级的trigger参数（LST RGTRIGGER）_09653261.md) 命令，查询SMF本地是否配置Session级或RG级的对应Trigger类型。
    >     - 如果本地已经配置，请执行[步骤 7](#ZH-CN_OPI_0289257220__step107941927143319)。
    >     - 如果本地未配置，请执行[**MOD PDUTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/修改PDU会话级的trigger参数（MOD PDUTRIGGER）_09653719.md)/[**MOD RGTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/修改RG级的trigger参数（MOD RGTRIGGER）_09653135.md)命令，本地按照规划配置Session级或RG级的对应Trigger类型，并再次执行[步骤 3](#ZH-CN_OPI_0289257220__step2585105420194)。
    > 7. 执行 [**LST PDUTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/查询PDU会话级的trigger参数（LST PDUTRIGGER）_09653638.md) / [**LST RGTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/查询RG级的trigger参数（LST RGTRIGGER）_09653261.md) 命令，查询SMF本地配置的Session级或RG级对应Trigger类型的生效原则是否正确。
    >     - 如果本地配置的生效原则错误，请执行[**MOD PDUTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/修改PDU会话级的trigger参数（MOD PDUTRIGGER）_09653719.md)/[**MOD RGTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/修改RG级的trigger参数（MOD RGTRIGGER）_09653135.md)命令，本地按照规划配置Session级或RG级对应Trigger类型的生效原则，并再次执行[步骤 3](#ZH-CN_OPI_0289257220__step2585105420194)。
  L65:
    >     - 如果本地未配置，请执行[**MOD PDUTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/修改PDU会话级的trigger参数（MOD PDUTRIGGER）_09653719.md)/[**MOD RGTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/修改RG级的trigger参数（MOD RGTRIGGER）_09653135.md)命令，本地按照规划配置Session级或RG级的对应Trigger类型，并再次执行[步骤 3](#ZH-CN_OPI_0289257220__step2585105420194)。
    > 7. 执行 [**LST PDUTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/查询PDU会话级的trigger参数（LST PDUTRIGGER）_09653638.md) / [**LST RGTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/查询RG级的trigger参数（LST RGTRIGGER）_09653261.md) 命令，查询SMF本地配置的Session级或RG级对应Trigger类型的生效原则是否正确。
    >     - 如果本地配置的生效原则错误，请执行[**MOD PDUTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/修改PDU会话级的trigger参数（MOD PDUTRIGGER）_09653719.md)/[**MOD RGTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/修改RG级的trigger参数（MOD RGTRIGGER）_09653135.md)命令，本地按照规划配置Session级或RG级对应Trigger类型的生效原则，并再次执行[步骤 3](#ZH-CN_OPI_0289257220__step2585105420194)。
    >     - 如果本地配置的生效原则正确，请执行[步骤 8](#ZH-CN_OPI_0289257220__step1829245425110)。
    > 8. 收集信息并寻求技术支持。

## ④ 自动比对
- 命令真相参数（24）：['ADDUPF', 'APNRATECTRLCHG', 'CCTMPLTNAME', 'CGISAICHG', 'CHANGEISMF', 'EVENTLIMIT', 'INSERTISMF', 'MAXNUMCCC', 'PLMNCHG', 'PRACHG', 'PSDATAOFFCHG', 'QOSCHG', 'RAICHG', 'RATCHG', 'REMOVALISMF', 'SERVPLMNRTCTCHG', 'SESSAMBRCHG', 'SRVNDCHG', 'TAICHG', 'TIMELIMIT', 'UCITIMER', 'UETZCHG', 'ULCHG', 'VOLUMELIMIT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
