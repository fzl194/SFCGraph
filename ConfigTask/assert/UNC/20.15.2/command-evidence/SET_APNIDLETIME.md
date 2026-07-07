# 命令证据包：SET APNIDLETIME
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md`
> 用该命令的特性数：5

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置指定APN空闲上下文时长。在运营商网络中存在长时间在线的用户，为防止出现垃圾上下文和浪费无线侧资源可以配置该功能。其功能包括空闲上下文定时器时长和不活动上下文定时器时长。

- 空闲上下文定时器：会话无数据传输的时长超过定时器时长后，删除会话、承载或Qos Flow。对2G、3G、4G和5G用户都生效。
- 不活动上下文定
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 该命令不适用于NB-IoT终端，因为此类终端很长时间才和网络交互一次，NB-IoT终端的空闲上下文功能参考软参BYTE801。
- SMF会话不活动定时器时长配置值需小于等于SMF会话空闲定时器时长。
- 当GUL承载级别参数指定为会话级时，对于4G用户，与GUL承载级别参数指定承载级且缺省承载和默认GBR的定时器指定使用承载定时器的效果相同。
- I-

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无。 | 字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| INHERIT | 继承默认开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “YES（是）”：继承默认配置 |
| SCTXCHKSW | SGW-C空闲上下文核查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| PCTXCHKSW | PGW-C和SGW-C/PGW-C空闲上下文检查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| GCTXCHKSW | GGSN空闲上下文检查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| HCTXCHKSW | H-SMF空闲上下文核查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| HCTXINACHKSW | H-SMF不活动上下文核查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| ICTXCHKSW | I-SMF/V-SMF空闲上下文核查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| ICTXINACHKSW | I-SMF/V-SMF不活动上下文核查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| GULTIMERLEVEL | GUL承载级别参数 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “SESSION（会话级）”：会话级 |
| DFTBEARPOLICY | 缺省承载和默认GBR的定时器 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ONEDAY（一天）”：一天 |
| BEARERTIMER | 承载定时器(min) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | 整数类型，取值范围是5~12000，单位是分钟。 |
| SESSIONTIMER | 会话定时器时长(min) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | 整数类型，取值范围是5~12000，单位是分钟。 |
| SMFSESIDLETIMER | SMF会话空闲定时器时长(min) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | 整数类型，取值范围是5~12000，单位是分钟。 |
| SMFSESINATIMER | SMF会话不活动定时器时长(min) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | 整数类型，取值范围是5~12000，单位是分钟。 |
| IDLEUPDATEMSG | 空闲超时发送更新消息 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| HSMFTIMERLEVEL | H-SMF空闲上下文核查级别 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- SESSION（会话级） |
| DEDQFIDLETIMER | 专有QoS Flow空闲定时器时长(min) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | 整数类型，取值范围是5~12000。 |
| DFTQFIDLETIMER | 缺省QoS Flow空闲定时器时长(min) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | 整数类型，取值范围是0，5~12000。 |
| DFTBRPLCYGGSN | GGSN一次激活上下文定时器 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ONEDAY（一天）”：一天 |
| DFTBEARERTIMER | 缺省承载定时器时长(min) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | 整数类型，取值范围是0~255，单位是分钟。 |
| PROS8CTXCHKSW | Proxy-SMF S8空闲上下文核查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |
| PROXYSMFCHKSW | Proxy-SMF 空闲上下文核查开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNI | <br>- “ENABLE（使能）”：使能 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-205105

**md：`WSFD-205105/WSFD-205105 上下文回收管理参考信息_28341923.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - **[SET DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)**
    > - **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)**
    > - **[SET DFTSESSIONTIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认会话上下文定时器（SET DFTSESSIONTIME）_96243108.md)**
    > - **[SET APNSESSIONTIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN会话上下文定时器配置（SET APNSESSIONTIME）_96243086.md)**

**md：`WSFD-205105/激活上下文回收管理_27434204.md`**
- 数据规划表（该命令的参数行）：
  | **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)** | APN名称（APN） | huawei.com | 本端规划 | 配置指定APN空闲上下文定时器开关和时长。 |
  | **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)** | 继承默认开关（INHERIT） | NO | 本端规划 | 配置指定APN空闲上下文定时器开关和时长。 |
  | **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)** | H-SMF空闲上下文核查开关（HCTXCHKSW） | ENABLE | 本端规划 | 配置指定APN空闲上下文定时器开关和时长。 |
  | **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)** | H-SMF空闲上下文核查级别（HSMFTIMERLEVEL） | QOSFLOW（QoS Flow级） | 本端规划 | 配置指定APN空闲上下文定时器开关和时长。 |
  | **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)** | 缺省QoS Flow空闲定时器时长(min)<br>（DFTQFIDLETIMER） | 1440 | 本端规划 | 配置指定APN空闲上下文定时器开关和时长。 |
  | **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)** | 专有QoS Flow空闲定时器时长(min)（DEDQFIDLETIMER） | 1440 | 本端规划 | 配置指定APN空闲上下文定时器开关和时长。 |
- 操作步骤上下文（±2 行原文）：
  L53:
    >   **[SET DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)**
    > 3. 配置指定APN的空闲上下文定时器开关和时长。
    >   **[SET APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)**
    > 4. 配置全局默认会话上下文定时器开关和时长。
    >   **[SET DFTSESSIONTIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认会话上下文定时器（SET DFTSESSIONTIME）_96243108.md)**

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    > - [**SET DFTIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)
    > - [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | APN名称（APN） | huawei.com | 已配置数据中获取 | - |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 继承默认开关（INHERIT） | NO | 本端规划 | - |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | H-SMF空闲上下文核查级别（HSMFTIMERLEVEL） | QOSFLOW | 固定取值 | 设置QoS Flow级别的SMF（N11）上下文空闲定时器时长时，必须使用样例值。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 专有QoS Flow空闲定时器时长(min)（DEDQFIDLETIMER） | 600 | 本端规划 | 根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制拆话，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以600分钟为例，请以局点规划数据为准。 |
- 任务示例脚本（该命令行）：
  `SET APNIDLETIME: APN="huawei.com", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=600;`
- 操作步骤上下文（±2 行原文）：
  L95:
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 8. **可选：**系统初始值不符合要求时，修改指定APN级别的专有QoS Flow级别的空闲定时器时长。
    >   [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    >   APN粒度优先级>全局粒度。全局粒度的可使用 [**SET DFTIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md) 设置。
    >   修改参数 “专有QoS Flow空闲定时器时长（DEDQFIDLETIMER）” 后，对新激活的用户生效，且仅对专有QoS Flow生效。
  L167:
    > 
    > ```
    > SET APNIDLETIME: APN="huawei.com", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=600;
    > ```
    > 

**md：`WSFD-109107/专有QoS Flow相关流程（适用于5G）_85678418.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    >   SMF收到消息后处理上报事件，基于QoS策略触发QoS Flow的更新操作，并向UPF下发PFCP Session Report Response消息，消息携带Update PDR、Update QER等信元组，包含PDR ID、URR ID、SDF等信元。
    > 3. SMF向UPF发送PFCP Session Modification Request消息，携带QoS Flow Identifier、QER ID、Gate Status等信元，提供用于该专有QoS Flow的数据监测，报告规则，CN隧道信息，QoS Flow级别的空闲上下文最大时长等，UPF向SMF发送PFCP Session Modification Response响应。
    >   SMF支持向UPF下发专有QoS Flow的空闲上下文最大时长，可通过 [**SET APNIDLETIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) （APN粒度）/ [**SET DFTIDLETIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md) （全局粒度）命令的 “专有QoS Flow空闲定时器时长(min)（DEDQFIDLETIMER）” 参数设置专有QoS Flow的空闲上下文最大时长。
    > 4. SMF向AMF发送Namf_Communication_N1N2MessageTransfer（Namf_N1N2MessageTransfer Request）消息，携带的信息包括发送给(R)AN的N2 SM Information，其中包含QFI、 QoS Profile、CN Tunnel Info等信息，发送给UE的N1 SM Container（PDU Session Modification Command），通知(R)AN和UE需要建立专有QoS Flow。
    >   PDU Session Modification Command中包含PDU Session ID、QoS rule(s)、QoS Flow级别的QoS参数等信息。

### WSFD-102101

**md：`WSFD-102101/激活VoLTE紧急呼叫（适用于SGW-C_PGW-C）_30394882.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 承载定时器(min)(BEARERTIMER) | 60 | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
- 任务示例脚本（该命令行）：
  `SET APNIDLETIME: APN="sos", INHERIT=NO, SCTXCHKSW=ENABLE, PCTXCHKSW=ENABLE, GCTXCHKSW=ENABLE, HCTXCHKSW=ENABLE, ICTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=ONEDAY, BEARERTIMER=60;`
- 操作步骤上下文（±2 行原文）：
  L57:
    >       [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > 4. 配置紧急呼叫结束后释放缺省承载。
    >   [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    >   > **说明**
    >   > 紧急呼叫缺省承载创建以后，除非用户关机，否则缺省承载不会被删除。这样系统资源会被一直占用，为了回收系统资源，需要配置 [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) 命令来释放缺省承载，考虑到可能会有回呼的场景， “BEARERTIMER” 的时间不能设置为0，建议保持缺省值60分钟。
  L59:
    >   [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    >   > **说明**
    >   > 紧急呼叫缺省承载创建以后，除非用户关机，否则缺省承载不会被删除。这样系统资源会被一直占用，为了回收系统资源，需要配置 [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) 命令来释放缺省承载，考虑到可能会有回呼的场景， “BEARERTIMER” 的时间不能设置为0，建议保持缺省值60分钟。
    > 
    > ## [任务示例](#ZH-CN_OPI_0230394882)
  L88:
    > 3. 配置紧急呼叫结束后释放缺省承载。
    >   ```
    >   SET APNIDLETIME: APN="sos", INHERIT=NO, SCTXCHKSW=ENABLE, PCTXCHKSW=ENABLE, GCTXCHKSW=ENABLE, HCTXCHKSW=ENABLE, ICTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=ONEDAY, BEARERTIMER=60;
    >   ```

### WSFD-102706

**md：`WSFD-102706/激活VoNR紧急呼叫_46685913.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 承载定时器(min)(BEARERTIMER) | 60 | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | APN名称（APN） | sos | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 继承默认开关（INHERIT） | NO | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | SGW-C空闲上下文核查开关（SCTXCHKSW） | ENABLE | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | PGW-C和SGW-C/PGW-C空闲上下文检查开关（PCTXCHKSW） | ENABLE | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | GGSN空闲上下文检查开关（GCTXCHKSW） | ENABLE | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | H-SMF空闲上下文核查开关（HCTXCHKSW） | ENABLE | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | I-SMF/V-SMF空闲上下文核查开关（ICTXCHKSW） | ENABLE | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | GUL承载级别参数（GULTIMERLEVEL） | BEARER | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 缺省承载和默认GBR的定时器（DFTBEARPOLICY） | ONEDAY | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 会话定时器时长(min)（SESSIONTIMER） | 120 | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |
- 任务示例脚本（该命令行）：
  `SET APNIDLETIME:APN="sos", INHERIT=NO, SCTXCHKSW=ENABLE, PCTXCHKSW=ENABLE, GCTXCHKSW=ENABLE, HCTXCHKSW=ENABLE, ICTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=ONEDAY, BEARERTIMER=60, SESSIONTIMER=120;`
- 操作步骤上下文（±2 行原文）：
  L109:
    >   **[ADD SMFEMGCFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/紧急呼叫会话配置/增加运营商紧急呼叫会话功能配置（ADD SMFEMGCFG）_91124570.md)**
    > 10. 配置紧急呼叫结束后释放缺省承载。
    >   [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001446685913)
  L191:
    > 
    > ```
    > SET APNIDLETIME:APN="sos", INHERIT=NO, SCTXCHKSW=ENABLE, PCTXCHKSW=ENABLE, GCTXCHKSW=ENABLE, HCTXCHKSW=ENABLE, ICTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=ONEDAY, BEARERTIMER=60, SESSIONTIMER=120;
    > ```

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L84:
    > **[LST APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/查询APN PCC功能（LST APNPCCFUNC）_09897035.md)**
    > 
    > [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    > 
    > **[LST APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/查询APN空闲上下文定时器配置（LST APNIDLETIME）_09653829.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | APN名称（APN） | ims | 已配置数据中获取 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 继承默认开关（INHERIT） | NO | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | PGW-C和SGW-C/PGW-C空闲上下文检查开关(PCTXCHKSW) | ENABLE | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | GUL承载级别参数（GULTIMERLEVEL） | BEARER | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 缺省承载和默认GBR的定时器（DFTBEARPOLICY） | OFF | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 承载定时器(min)（BEARERTIMER） | 5 | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
- 任务示例脚本（该命令行）：
  `SET APNIDLETIME: APN="ims", INHERIT=NO, PCTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=OFF, BEARERTIMER=5;`
  `SET APNIDLETIME: APN="ims", INHERIT=NO, PCTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=OFF, BEARERTIMER=5;`
- 操作步骤上下文（±2 行原文）：
  L277:
    >       [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >     i. 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。
    >       [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    > 4.
    >   配置相关软参。
  L438:
    > 
    >       ```
    >       SET APNIDLETIME: APN="ims", INHERIT=NO, PCTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=OFF, BEARERTIMER=5;
    >       ```
    >     4. 配置相关软参。
  L552:
    > 
    >       ```
    >       SET APNIDLETIME: APN="ims", INHERIT=NO, PCTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=OFF, BEARERTIMER=5;
    >       ```
    >     3. 配置相关软参。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | APN名称（APN） | ims | 已配置数据中获取 | 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除QoS Flow，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以5分钟为例，请以局点规划数据为准。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 继承默认开关（INHERIT） | NO | 本端规划 | 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除QoS Flow，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以5分钟为例，请以局点规划数据为准。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | H-SMF空闲上下文核查级别（HSMFTIMERLEVEL） | QOSFLOW | 固定取值 | 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除QoS Flow，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以5分钟为例，请以局点规划数据为准。 |
  | [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 专有QoS Flow空闲定时器时长(min)（DEDQFIDLETIMER） | 5 | 本端规划 | 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除QoS Flow，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以5分钟为例，请以局点规划数据为准。 |
- 任务示例脚本（该命令行）：
  `SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;`
  `SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;`
  `SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;`
  `SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;`
  `SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;`
  `SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;`
- 操作步骤上下文（±2 行原文）：
  L301:
    >       [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >     k. 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。
    >       [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    >     l. 配置专有GBR类型QoS Flow的延迟释放时长。
    >       [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
  L455:
    > 
    >             ```
    >             SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;
    >             ```
    >             //配置专有GBR类型QoS Flow的延迟释放时长。
  L524:
    > 
    >             ```
    >             SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;
    >             ```
    >             //配置专有GBR类型QoS Flow的延迟释放时长。

## ④ 自动比对
- 命令真相参数（23）：['APN', 'BEARERTIMER', 'DEDQFIDLETIMER', 'DFTBEARERTIMER', 'DFTBEARPOLICY', 'DFTBRPLCYGGSN', 'DFTQFIDLETIMER', 'GCTXCHKSW', 'GULTIMERLEVEL', 'HCTXCHKSW', 'HCTXINACHKSW', 'HSMFTIMERLEVEL', 'ICTXCHKSW', 'ICTXINACHKSW', 'IDLEUPDATEMSG', 'INHERIT', 'PCTXCHKSW', 'PROS8CTXCHKSW', 'PROXYSMFCHKSW', 'SCTXCHKSW', 'SESSIONTIMER', 'SMFSESIDLETIMER', 'SMFSESINATIMER']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 27, '已配置数据中获取': 3, '固定取值': 2}（多值→atom 应考虑 decision_driven）
