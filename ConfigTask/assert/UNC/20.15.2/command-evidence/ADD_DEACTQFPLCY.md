# 命令证据包：ADD DEACTQFPLCY
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF**

该命令用于增加当SMF接收到AMF发送的去激活用户面请求时，专有GBR类型QoS Flow的处理策略。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入255条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NGAPCAUSEGROUP | NGAPCAUSEVALUE | QFPLCY | DELAYTIMER |
| --- | --- | --- | --- |
| RADIO_NETWORK | 20 | NOT_RELEASE | 60 |
| RADIO_NE

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| NGAPCAUSEGROUP | NgApCause组 | local_planned | required | 无 | <br>- RADIO_NETWORK（Radio Network Layer） |
| NGAPCAUSEVALUE | NgApCause值 | local_planned | required | 无 | 整数类型，取值范围是0~255。 |
| QFPLCY | 专有GBR类型QoS Flow处理策略 | local_planned | required | 无 | <br>- RELEASE（释放专有QoS Flow） |
| DELAYTIMER | 延迟释放专有GBR类型QoS Flow时长(秒) | local_planned | conditional | 60 | 整数类型，取值范围是10~100，单位是秒。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**SET DFTIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)
    > - [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
    > - [**ADD DEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0285397060)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 操作步骤上下文（±2 行原文）：
  L100:
    > 9. **可选：**UE无线连接丢失（NGAPCAUSEVALUE=21）时，配置基于APN去活用户面专有QoS Flow策略。
    >   [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
    >   APN粒度优先级>全局粒度。全局粒度的可使用 [**ADD DEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md) 设置。
    > 
    > ## [任务示例](#ZH-CN_OPI_0285397058)

**md：`WSFD-109107/专有QoS Flow相关流程（适用于5G）_85678418.md`**
- 操作步骤上下文（±2 行原文）：
  L63:
    > - 当业务暂停一段时间，业务流老化时，UPF向SMF上报QoS事件从而发起专有QoS Flow释放流程。
    > - 当连接态的UE进入没有无线信号的区域（例如：电梯、隧道）后，超过一定时间，RAN会发起AN Release链接释放请求。
    >   在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost）时，SMF支持根据 [**ADD APNDEACTQFPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) （APN粒度）/ [**ADD DEACTQFPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md) （全局粒度）配置决定是否延迟释放专有QoS Flow及延迟释放时间。
    > 
    > 专有QoS Flow释放成功后，用户即不能使用该数据业务。业务流老化场景，专有QoS Flow释放流程如 [图3](#ZH-CN_TOPIC_0285678418__fig14727124553113) 所示。其他场景SMF释放专有QoS Flow的流程与业务流老化场景类似，仅触发原因不同。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L100:
    > **[LST APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/查询基于APN去活用户面专有QoS Flow策略（LST APNDEACTQFPLCY）_38890149.md)**
    > 
    > [**ADD DEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)
    > 
    > **[RMV DEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/删除去活用户面专有QoS Flow策略（RMV DEACTQFPLCY）_38692983.md)**

### WSFD-221001

**md：`WSFD-221001/参考信息_58365281.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)**
    > - **[删除去活用户面专有QoS Flow策略（RMV DEACTQFPLCY）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/删除去活用户面专有QoS Flow策略（RMV DEACTQFPLCY）_38692983.md)**
    > - **[修改去活用户面专有QoS Flow策略（MOD DEACTQFPLCY）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/修改去活用户面专有QoS Flow策略（MOD DEACTQFPLCY）_92470772.md)**

**md：`WSFD-221001/激活VoNR承载延时保活_11685432.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD DEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)** | NgApCause组（NGAPCAUSEGROUP） | RADIO_NETWORK | 本端规划 | 配置整系统粒度专有QoS Flow去活策略。 |
  | **[ADD DEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)** | NgApCause值（NGAPCAUSEVALUE） | 21 | 本端规划 | 配置整系统粒度专有QoS Flow去活策略。 |
  | **[ADD DEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)** | 专有GBR类型QoS Flow处理策略（QFPLCY） | DELAY_RELEASE | 本端规划 | 配置整系统粒度专有QoS Flow去活策略。 |
  | **[ADD DEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)** | 延迟释放专有GBR类型QoS Flow时长(秒)（DELAYTIMER） | 60 | 本端规划 | 配置整系统粒度专有QoS Flow去活策略。 |
- 任务示例脚本（该命令行）：
  `ADD DEACTQFPLCY: NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
- 操作步骤上下文（±2 行原文）：
  L42:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. **可选：**配置整系统粒度专有QoS Flow去活策略。
    >   **[ADD DEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)**
    > 3. **可选：**配置APN粒度专有QoS Flow去活策略。
    >   **[ADD APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)**
  L63:
    > 
    > ```
    > ADD DEACTQFPLCY: NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（4）：['DELAYTIMER', 'NGAPCAUSEGROUP', 'NGAPCAUSEVALUE', 'QFPLCY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 4}（多值→atom 应考虑 decision_driven）
