# 命令证据包：ADD RGTRIGGER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/增加RG级的trigger参数（ADD RGTRIGGER）_09653787.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加RG级的trigger参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 最多可输入101条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCTMPLTNAME | QOSCHG | ULCHG | SRVNDCHG | PRACHG | PSDATAOFFCHG | UETZCHG | PLMNCHG | RATCHG | TIMELIMIT | VOLUMELIMIT | EVENTLIM

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| QOSCHG | QoS更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| ULCHG | 用户位置更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| SRVNDCHG | 服务节点更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| PRACHG | 区域用户位置上报更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| PSDATAOFFCHG | PS数据关闭状态更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| UETZCHG | 用户时区更新 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| PLMNCHG | PLMN更新 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| RATCHG | RAT更新 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| TIMELIMIT | 时间阈值 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| VOLUMELIMIT | 流量阈值 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| EVENTLIMIT | 事件阈值 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| QUOTATHRESHOLD | 配额阈值 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| VT | 配额有效时长 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| QHT | 配额保持时长 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| SERVPLMNRTCTCHG | 服务PLMN速率控制更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| APNRATECTRLCHG | APN速率控制更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| TAICHG | 跟踪区标识更新 | local_planned | optional | NONREPORT | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| CGISAICHG | CGISAI更新 | local_planned | optional | NONREPORT | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| RAICHG | RAI更新 | local_planned | optional | NONREPORT | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L31:
    > - [**ADD SELECTCCTBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板绑定/增加基于CC配置融合计费模板处理（ADD SELECTCCTBYCC）_09654384.md)
    > - [**ADD PDUTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/增加PDU会话级的trigger参数（ADD PDUTRIGGER）_09653225.md)
    > - [**ADD RGTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/增加RG级的trigger参数（ADD RGTRIGGER）_09653787.md)
    > - [**SET CTXSTARTRATING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置给OCS_CHF发送的消息初始携带的计费属性（SET CTXSTARTRATING）_09897210.md)
    > - [**SET FAILHANDLING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)

**md：`WSFD-011206/计费事件触发条件_90776688.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > > 对于Session级和RG级同时生效的计费Trigger，如果订阅存在冲突，以Session级Trigger的规则优先。
    > 
    > 计费Trigger可以由CHF下发，也可以在SMF上通过 **ADD PDUTRIGGER** 和 **ADD RGTRIGGER** 命令本地配置，CHF下发的Trigger优先级更高。当CHF只下发Trigger不下发对应计费参数时，SMF按照本地配置的计费参数实现。缺省计费Trigger样例如 [表1](#ZH-CN_TOPIC_0190776688__table79836176453) 所示，完整信息可参见3GPP 32.255。
    > 
    > *表1 缺省计费Trigger*
  L67:
    > | Abort request is received from the CHF | 收到CHF发送的中止计费会话请求 | Session | 立即上报 | 否 | 否 | Charging Data Request [Termination] |
    > 
    > **SET CNVRGDCHGPARA** 命令的 “IGNORETRIGGER” 参数用于SMF处理CHF响应消息时，忽略CHF下发指定的Trigger控制，使用SMF本地通过 **ADD PDUTRIGGER** 和 **ADD RGTRIGGER** 命令配置的Trigger生效。该参数是位域类型的取值，可配置的忽略CHF下发的Trigger列表为：计费条件改变阈值、会话级时间阈值、会话级流量阈值、RG级时间阈值、RG级流量阈值、配额保持时长。
    > 
    > 当CHF在响应消息中携带了Trigger列表，但未携带 “IGNORETRIGGER” 参数配置的忽略Trigger，则该被忽略的Trigger仍然采用本地配置值。

**md：`WSFD-011206/使用全局CCT模板进行融合计费实例_93029782.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RGTRIGGER** | CCTMPLTNAME（CCT模板名称） | cct-test | 本端规划 | 配置Session级/RG级Trigger。 |
  | **ADD RGTRIGGER** | ULCHG（用户位置更新） | NONREPORT | 本端规划 | 配置Session级/RG级Trigger。 |
  | **ADD RGTRIGGER** | PRACHG（区域用户位置上报更新） | IMMEDIATE | 本端规划 | 配置Session级/RG级Trigger。 |
  | **ADD RGTRIGGER** | PSDATAOFFCHG（PS数据关闭状态更新） | IMMEDIATE | 本端规划 | 配置Session级/RG级Trigger。 |
- 任务示例脚本（该命令行）：
  `ADD RGTRIGGER: CCTMPLTNAME="global", ULCHG=NONREPORT, PRACHG=IMMEDIATE, PSDATAOFFCHG=IMMEDIATE;`
- 操作步骤上下文（±2 行原文）：
  L90:
    > ```
    > ADD PDUTRIGGER: CCTMPLTNAME="global", QOSCHG=IMMEDIATE, SRVNDCHG=DEFERRED, RATCHG=IMMEDIATE;
    > ADD RGTRIGGER: CCTMPLTNAME="global", ULCHG=NONREPORT, PRACHG=IMMEDIATE, PSDATAOFFCHG=IMMEDIATE;
    > ```
    > 

**md：`WSFD-011206/配置SMF与CHF交互的条件和内容_93420840.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RGTRIGGER** | CCT模板名称（融合计费模板名称） | cct_test | 已配置数据中获取 | 配置RG级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD RGTRIGGER** | 用户位置更新（ULCHG） | NONREPORT | 全网规划 | 配置RG级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD RGTRIGGER** | 区域用户位置上报更新（PRACHG） | IMMEDIATE | 全网规划 | 配置RG级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD RGTRIGGER** | PS数据关闭状态更新（PSDATAOFFCHG） | IMMEDIATE | 全网规划 | 配置RG级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
- 任务示例脚本（该命令行）：
  `ADD RGTRIGGER: CCTMPLTNAME="cct_test", ULCHG=NONREPORT, PRACHG=IMMEDIATE, PSDATAOFFCHG=IMMEDIATE;`
- 操作步骤上下文（±2 行原文）：
  L85:
    >       **ADD PDUTRIGGER**
    >     b. 配置RG级Trigger。
    >       **ADD RGTRIGGER**
    > 4. 配置RG老化功能。
    >   ****SET RGRESCTRL****
  L129:
    > 
    > ```
    > ADD RGTRIGGER: CCTMPLTNAME="cct_test", ULCHG=NONREPORT, PRACHG=IMMEDIATE, PSDATAOFFCHG=IMMEDIATE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（20）：['APNRATECTRLCHG', 'CCTMPLTNAME', 'CGISAICHG', 'EVENTLIMIT', 'PLMNCHG', 'PRACHG', 'PSDATAOFFCHG', 'QHT', 'QOSCHG', 'QUOTATHRESHOLD', 'RAICHG', 'RATCHG', 'SERVPLMNRTCTCHG', 'SRVNDCHG', 'TAICHG', 'TIMELIMIT', 'UETZCHG', 'ULCHG', 'VOLUMELIMIT', 'VT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 4, '已配置数据中获取': 1, '全网规划': 3}（多值→atom 应考虑 decision_driven）
