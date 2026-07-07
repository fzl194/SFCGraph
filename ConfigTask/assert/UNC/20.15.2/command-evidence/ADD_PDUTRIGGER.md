# 命令证据包：ADD PDUTRIGGER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/增加PDU会话级的trigger参数（ADD PDUTRIGGER）_09653225.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加PDU会话级的trigger参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 最多可输入101条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCTMPLTNAME | QOSCHG | ULCHG | SRVNDCHG | PRACHG | PSDATAOFFCHG | UETZCHG | PLMNCHG | RATCHG | ADDUPF | TIMELIMIT | VOLUMELIMIT |

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
| ADDUPF | 添加UPF | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| TIMELIMIT | 时间阈值 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| VOLUMELIMIT | 流量阈值 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| EVENTLIMIT | 事件阈值 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| MAXNUMCCC | 计费条件改变阈值 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| UCITIMER | 业务停止时长 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF |
| INSERTISMF | 插入I-SMF | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| REMOVALISMF | 删除I-SMF | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| CHANGEISMF | 更新I-SMF | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| SESSAMBRCHG | Session AMBR更新 | local_planned | optional | IMMEDIATE | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| SERVPLMNRTCTCHG | 服务PLMN速率控制更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| APNRATECTRLCHG | APN速率控制更新 | local_planned | optional | DEFERRED | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| TAICHG | 跟踪区标识更新 | local_planned | optional | NONREPORT | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| CGISAICHG | CGISAI更新 | local_planned | optional | NONREPORT | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |
| RAICHG | RAI更新 | local_planned | optional | NONREPORT | <br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**ADD SELECTCCTBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板绑定/增加基于CC配置融合计费模板处理（ADD SELECTCCTBYCC）_09654384.md)
    > - [**ADD PDUTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/增加PDU会话级的trigger参数（ADD PDUTRIGGER）_09653225.md)
    > - [**ADD RGTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/增加RG级的trigger参数（ADD RGTRIGGER）_09653787.md)
    > - [**SET CTXSTARTRATING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置给OCS_CHF发送的消息初始携带的计费属性（SET CTXSTARTRATING）_09897210.md)

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
  | **ADD PDUTRIGGER** | CCTMPLTNAME（CCT模板名称） | cct-test | 本端规划 | 配置Session级/RG级Trigger。 |
  | **ADD PDUTRIGGER** | QOSCHG（QoS更新） | IMMEDIATE | 本端规划 | 配置Session级/RG级Trigger。 |
  | **ADD PDUTRIGGER** | SRVNDCHG（服务节点更新） | DEFERRED | 本端规划 | 配置Session级/RG级Trigger。 |
  | **ADD PDUTRIGGER** | RATCHG（RAT更新） | IMMEDIATE | 本端规划 | 配置Session级/RG级Trigger。 |
- 任务示例脚本（该命令行）：
  `ADD PDUTRIGGER: CCTMPLTNAME="global", QOSCHG=IMMEDIATE, SRVNDCHG=DEFERRED, RATCHG=IMMEDIATE;`
- 操作步骤上下文（±2 行原文）：
  L89:
    > 
    > ```
    > ADD PDUTRIGGER: CCTMPLTNAME="global", QOSCHG=IMMEDIATE, SRVNDCHG=DEFERRED, RATCHG=IMMEDIATE;
    > ADD RGTRIGGER: CCTMPLTNAME="global", ULCHG=NONREPORT, PRACHG=IMMEDIATE, PSDATAOFFCHG=IMMEDIATE;
    > ```

**md：`WSFD-011206/配置SMF与CHF交互的条件和内容_93420840.md`**
- 数据规划表（该命令的参数行）：
  | **ADD PDUTRIGGER** | CCT模板名称（融合计费模板名称） | cct_test | 已配置数据中获取 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD PDUTRIGGER** | QoS更新（QOSCHG） | IMMEDIATE | 全网规划 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD PDUTRIGGER** | 服务节点更新（SRVNDCHG） | DEFERRED | 全网规划 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD PDUTRIGGER** | RAT更新（RATCHG） | IMMEDIATE | 全网规划 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD PDUTRIGGER** | 区域用户位置上报更新（PRACHG） | DEFERRED | 全网规划 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD PDUTRIGGER** | 添加UPF（ADDUPF） | IMMEDIATE | 全网规划 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD PDUTRIGGER** | 插入ISMF（INSERTISMF） | DEFERRED | 全网规划 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD PDUTRIGGER** | CGISAI更新（CGISAICHG） | DEFERRED | 全网规划 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **ADD PDUTRIGGER** | RAI更新（RAICHG） | DEFERRED | 全网规划 | 配置Session级Trigger。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
- 任务示例脚本（该命令行）：
  `ADD PDUTRIGGER: CCTMPLTNAME="cct-test", QOSCHG=IMMEDIATE, SRVNDCHG=DEFERRED, RATCHG=IMMEDIATE, PRACHG=DEFERRED, ADDUPF=IMMEDIATE, INSERTISMF=DEFERRED, CGISAICHG=DEFERRED, RAICHG=DEFERRED;`
- 操作步骤上下文（±2 行原文）：
  L83:
    > 3. **可选：** 配置Session级/RG级Trigger。
    >     a. 配置Session级Trigger。
    >       **ADD PDUTRIGGER**
    >     b. 配置RG级Trigger。
    >       **ADD RGTRIGGER**
  L123:
    > 
    > ```
    > ADD PDUTRIGGER: CCTMPLTNAME="cct-test", QOSCHG=IMMEDIATE, SRVNDCHG=DEFERRED, RATCHG=IMMEDIATE, PRACHG=DEFERRED, ADDUPF=IMMEDIATE, INSERTISMF=DEFERRED, CGISAICHG=DEFERRED, RAICHG=DEFERRED;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（24）：['ADDUPF', 'APNRATECTRLCHG', 'CCTMPLTNAME', 'CGISAICHG', 'CHANGEISMF', 'EVENTLIMIT', 'INSERTISMF', 'MAXNUMCCC', 'PLMNCHG', 'PRACHG', 'PSDATAOFFCHG', 'QOSCHG', 'RAICHG', 'RATCHG', 'REMOVALISMF', 'SERVPLMNRTCTCHG', 'SESSAMBRCHG', 'SRVNDCHG', 'TAICHG', 'TIMELIMIT', 'UCITIMER', 'UETZCHG', 'ULCHG', 'VOLUMELIMIT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 4, '已配置数据中获取': 1, '全网规划': 8}（多值→atom 应考虑 decision_driven）
