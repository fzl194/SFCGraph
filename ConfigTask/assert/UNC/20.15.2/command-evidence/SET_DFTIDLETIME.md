# 命令证据包：SET DFTIDLETIME
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置全局的默认空闲上下文定时器和不活动上下文定时器开关和时长。

- 空闲上下文定时器：会话无数据传输的时长超过定时器时长后，删除会话、承载或Qos Flow。对2G、3G、4G和5G用户都生效。
- 不活动上下文定时器：会话无数据传输的时长超过定时器时长后，释放会话的用户面资源。仅对5G用户生效。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 该命令不适用于NB-IoT终端，因为此类终端很长时间才和网络交互一次，NB-IoT终端的空闲上下文功能参考软参BYTE801。
- SMF会话不活动定时器时长配置值需小于等于SMF会话空闲定时器时长。
- 当GUL承载级别参数指定为会话级时，对于4G用户，与GUL承载级别参数指定承载级且缺省承载和默认GBR的定时器指定使用承载定时器的效果相同。
- I-

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SCTXCHKSW | SGW-C空闲上下文核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “DISABLE（去使能）”：去使能 |
| PCTXCHKSW | PGW-C和SGW-C/PGW-C网元的上下文核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “DISABLE（去使能）”：去使能 |
| GCTXCHKSW | GGSN空闲上下文核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “DISABLE（去使能）”：去使能 |
| HCTXCHKSW | H-SMF空闲上下文核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “DISABLE（去使能）”：去使能 |
| HCTXINACHKSW | H-SMF不活动上下文核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “ENABLE（使能）”：使能 |
| ICTXCHKSW | I-SMF/V-SMF空闲上下文核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “DISABLE（去使能）”：去使能 |
| ICTXINACHKSW | I-SMF/V-SMF不活动上下文核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “ENABLE（使能）”：使能 |
| GULTIMERLEVEL | GUL承载级别参数 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “SESSION（会话级）”：会话级 |
| DFTBEARPOLICY | 缺省承载和默认GBR的定时器 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “ONEDAY（一天）”：一天 |
| BEARERTIMER | 承载定时器时长(min) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | 整数类型，取值范围是5~12000，单位是分钟。 |
| SESSIONTIMER | 会话定时器时长(min) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | 整数类型，取值范围是5~12000，单位是分钟。 |
| SMFSESIDLETIMER | SMF会话空闲定时器时长(min) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | 整数类型，取值范围是5~12000，单位是分钟。 |
| SMFSESINATIMER | SMF会话不活动定时器时长(min) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | 整数类型，取值范围是5~12000，单位是分钟。 |
| IDLEUPDATEMSG | 空闲超时发送更新消息 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “DISABLE（去使能）”：去使能 |
| HSMFTIMERLEVEL | H-SMF空闲上下文核查级别 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- SESSION（会话级） |
| DEDQFIDLETIMER | 专有QoS Flow空闲定时器时长(min) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | 整数类型，取值范围是5~12000。 |
| DFTQFIDLETIMER | 缺省QoS Flow空闲定时器时长(min) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | 整数类型，取值范围是0，5~12000。 |
| DFTBRPLCYGGSN | GGSN一次激活上下文定时器 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “ONEDAY（一天）”：一天 |
| PROS8CTXCHKSW | Proxy-SMF S8空闲上下文核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | <br>- “DISABLE（去使能）”：去使能 |
| PROXYSMFCHKSW | Proxy-SMF 空闲上下文检查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTI | 如果开关由去使能修改为使能，则对新创建的上下文进行检查，SMF会话空闲定时器时长生效。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-205105

**md：`WSFD-205105/WSFD-205105 上下文回收管理参考信息_28341923.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[SET DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)**
    > - **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)**
    > - **[SET DFTSESSIONTIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认会话上下文定时器（SET DFTSESSIONTIME）_96243108.md)**

**md：`WSFD-205105/激活上下文回收管理_27434204.md`**
- 数据规划表（该命令的参数行）：
  | **[SET DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)** | H-SMF空闲上下文核查开关（HCTXCHKSW） | ENABLE | 本端规划 | 配置默认空闲上下文定时器开关和时长。 |
  | **[SET DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)** | H-SMF空闲上下文核查级别（HSMFTIMERLEVEL） | SESSION | 本端规划 | 配置默认空闲上下文定时器开关和时长。 |
  | **[SET DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)** | SMF会话空闲定时器时长(min)（SMFSESIDLETIMER） | 1000 | 本端规划 | 配置默认空闲上下文定时器开关和时长。 |
- 任务示例脚本（该命令行）：
  `SET DFTIDLETIME: HCTXCHKSW=ENABLE, HSMFTIMERLEVEL=SESSION, SMFSESIDLETIMER=1000;`
- 操作步骤上下文（±2 行原文）：
  L51:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 配置全局默认空闲上下文定时器开关和时长。
    >   **[SET DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)**
    > 3. 配置指定APN的空闲上下文定时器开关和时长。
    >   **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)**
  L76:
    >   //配置全局默认SMF空闲上下文核查开关为打开，核查级别为会话级，会话空闲定时器时长为1000分钟。
    >   ```
    >   SET DFTIDLETIME: HCTXCHKSW=ENABLE, HSMFTIMERLEVEL=SESSION, SMFSESIDLETIMER=1000;
    >   ```
    >   //打开本特性的License配置开关。

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    > - [**SET DFTIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)
    > - [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
    > - [**ADD DEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 操作步骤上下文（±2 行原文）：
  L96:
    > 8. **可选：**系统初始值不符合要求时，修改指定APN级别的专有QoS Flow级别的空闲定时器时长。
    >   [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    >   APN粒度优先级>全局粒度。全局粒度的可使用 [**SET DFTIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md) 设置。
    >   修改参数 “专有QoS Flow空闲定时器时长（DEDQFIDLETIMER）” 后，对新激活的用户生效，且仅对专有QoS Flow生效。
    > 9. **可选：**UE无线连接丢失（NGAPCAUSEVALUE=21）时，配置基于APN去活用户面专有QoS Flow策略。

**md：`WSFD-109107/专有QoS Flow相关流程（适用于5G）_85678418.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    >   SMF收到消息后处理上报事件，基于QoS策略触发QoS Flow的更新操作，并向UPF下发PFCP Session Report Response消息，消息携带Update PDR、Update QER等信元组，包含PDR ID、URR ID、SDF等信元。
    > 3. SMF向UPF发送PFCP Session Modification Request消息，携带QoS Flow Identifier、QER ID、Gate Status等信元，提供用于该专有QoS Flow的数据监测，报告规则，CN隧道信息，QoS Flow级别的空闲上下文最大时长等，UPF向SMF发送PFCP Session Modification Response响应。
    >   SMF支持向UPF下发专有QoS Flow的空闲上下文最大时长，可通过 [**SET APNIDLETIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) （APN粒度）/ [**SET DFTIDLETIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md) （全局粒度）命令的 “专有QoS Flow空闲定时器时长(min)（DEDQFIDLETIMER）” 参数设置专有QoS Flow的空闲上下文最大时长。
    > 4. SMF向AMF发送Namf_Communication_N1N2MessageTransfer（Namf_N1N2MessageTransfer Request）消息，携带的信息包括发送给(R)AN的N2 SM Information，其中包含QFI、 QoS Profile、CN Tunnel Info等信息，发送给UE的N1 SM Container（PDU Session Modification Command），通知(R)AN和UE需要建立专有QoS Flow。
    >   PDU Session Modification Command中包含PDU Session ID、QoS rule(s)、QoS Flow级别的QoS参数等信息。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L88:
    > **[LST APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/查询APN空闲上下文定时器配置（LST APNIDLETIME）_09653829.md)**
    > 
    > [**SET DFTIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)
    > 
    > **[LST DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/查询默认空闲上下文定时器配置（LST DFTIDLETIME）_09653130.md)**

## ④ 自动比对
- 命令真相参数（20）：['BEARERTIMER', 'DEDQFIDLETIMER', 'DFTBEARPOLICY', 'DFTBRPLCYGGSN', 'DFTQFIDLETIMER', 'GCTXCHKSW', 'GULTIMERLEVEL', 'HCTXCHKSW', 'HCTXINACHKSW', 'HSMFTIMERLEVEL', 'ICTXCHKSW', 'ICTXINACHKSW', 'IDLEUPDATEMSG', 'PCTXCHKSW', 'PROS8CTXCHKSW', 'PROXYSMFCHKSW', 'SCTXCHKSW', 'SESSIONTIMER', 'SMFSESIDLETIMER', 'SMFSESINATIMER']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 3}（多值→atom 应考虑 decision_driven）
