# 命令证据包：ADD APNDEACTQFPLCY
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF**

该命令用于增加基于APN的当SMF接收到AMF发送的去激活用户面请求时，专有GBR类型QoS Flow的处理策略。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入20000条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| NGAPCAUSEGROUP | NgApCause组 | local_planned | required | 无 | <br>- RADIO_NETWORK（Radio Network Layer） |
| NGAPCAUSEVALUE | NgApCause值 | local_planned | required | 无 | 整数类型，取值范围是0~255。 |
| QFPLCY | 专有GBR类型QoS Flow处理策略 | local_planned | required | 无 | <br>- RELEASE（释放专有QoS Flow） |
| DELAYTIMER | 延迟释放专有GBR类型QoS Flow时长(秒) | local_planned | conditional | 60 | 整数类型，取值范围是10~100，单位是秒。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    > - [**SET DFTIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)
    > - [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
    > - [**ADD DEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)
    > 

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | APN名称（APN） | imsapn.com | 已配置数据中获取 | 在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | NgApCause组（NGAPCAUSEGROUP） | RADIO_NETWORK | 固定取值 | 在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | NgApCause值（NGAPCAUSEVALUE） | 21 | 固定取值 | 在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | 专有GBR类型QoS Flow处理策略（QFPLCY） | DELAY_RELEASE | 固定取值 | 在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | 延迟释放专有GBR类型QoS Flow时长(秒)（DELAYTIMER） | 60 | 全网规划 | 在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
- 任务示例脚本（该命令行）：
  `ADD APNDEACTQFPLCY: APN="huawei.com", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
- 操作步骤上下文（±2 行原文）：
  L99:
    >   修改参数 “专有QoS Flow空闲定时器时长（DEDQFIDLETIMER）” 后，对新激活的用户生效，且仅对专有QoS Flow生效。
    > 9. **可选：**UE无线连接丢失（NGAPCAUSEVALUE=21）时，配置基于APN去活用户面专有QoS Flow策略。
    >   [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
    >   APN粒度优先级>全局粒度。全局粒度的可使用 [**ADD DEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md) 设置。
    > 
  L173:
    > 
    > ```
    > ADD APNDEACTQFPLCY: APN="huawei.com", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
    > ```

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
  L92:
    > **[LST DFTIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/查询默认空闲上下文定时器配置（LST DFTIDLETIME）_09653130.md)**
    > 
    > [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
    > 
    > **[RMV APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/删除基于APN去活用户面专有QoS Flow策略（RMV APNDEACTQFPLCY）_92310840.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | APN名称（APN） | ims | 已配置数据中获取 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | NgApCause组（NGAPCAUSEGROUP） | RADIO_NETWORK | 固定取值 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | NgApCause值（NGAPCAUSEVALUE） | 21 | 固定取值 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | 专有GBR类型QoS Flow处理策略（QFPLCY） | DELAY_RELEASE | 固定取值 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
  | [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | 延迟释放专有GBR类型QoS Flow时长(秒)（DELAYTIMER） | 60 | 全网规划 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
- 任务示例脚本（该命令行）：
  `ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
  `ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
  `ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
  `ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
  `ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
  `ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
- 操作步骤上下文（±2 行原文）：
  L303:
    >       [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    >     l. 配置专有GBR类型QoS Flow的延迟释放时长。
    >       [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
    > 4.
    >   配置相关软参。
  L460:
    > 
    >             ```
    >             ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
    >             ```
    >           - 策略接口为N7接口，MODEL C组网
  L529:
    > 
    >             ```
    >             ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
    >             ```
    >           - 策略接口为N7接口，MODEL D组网

### WSFD-221001

**md：`WSFD-221001/参考信息_58365281.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - **[修改去活用户面专有QoS Flow策略（MOD DEACTQFPLCY）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/修改去活用户面专有QoS Flow策略（MOD DEACTQFPLCY）_92470772.md)**
    > - **[查询去活用户面专有QoS Flow策略（LST DEACTQFPLCY）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/查询去活用户面专有QoS Flow策略（LST DEACTQFPLCY）_92022694.md)**
    > - **[增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)**
    > - **[删除基于APN去活用户面专有QoS Flow策略（RMV APNDEACTQFPLCY）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/删除基于APN去活用户面专有QoS Flow策略（RMV APNDEACTQFPLCY）_92310840.md)**
    > - **[修改基于APN去活用户面专有QoS Flow策略（MOD APNDEACTQFPLCY）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/修改基于APN去活用户面专有QoS Flow策略（MOD APNDEACTQFPLCY）_92151170.md)**

**md：`WSFD-221001/激活VoNR承载延时保活_11685432.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)** | APN名称（APN） | ims | 本端规划 | 配置APN粒度专有QoS Flow去活策略。 |
  | **[ADD APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)** | NgApCause组（NGAPCAUSEGROUP） | RADIO_NETWORK | 本端规划 | 配置APN粒度专有QoS Flow去活策略。 |
  | **[ADD APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)** | NgApCause值（NGAPCAUSEVALUE） | 21 | 本端规划 | 配置APN粒度专有QoS Flow去活策略。 |
  | **[ADD APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)** | 专有GBR类型QoS Flow处理策略（QFPLCY） | DELAY_RELEASE | 本端规划 | 配置APN粒度专有QoS Flow去活策略。 |
  | **[ADD APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)** | 延迟释放专有GBR类型QoS Flow时长(秒)（DELAYTIMER） | 60 | 本端规划 | 配置APN粒度专有QoS Flow去活策略。 |
- 任务示例脚本（该命令行）：
  `ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;`
- 操作步骤上下文（±2 行原文）：
  L44:
    >   **[ADD DEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加去活用户面专有QoS Flow策略（ADD DEACTQFPLCY）_38788437.md)**
    > 3. **可选：**配置APN粒度专有QoS Flow去活策略。
    >   **[ADD APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)**
    > 4. **可选：**配置插入或删除I-SMF场景下QoS Flow去活策略。
    >   **[SET QOSFLOWFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/设置QoS Flow扩展功能（SET QOSFLOWFUNC）_38788439.md)**
  L69:
    > 
    > ```
    > ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（5）：['APN', 'DELAYTIMER', 'NGAPCAUSEGROUP', 'NGAPCAUSEVALUE', 'QFPLCY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 2, '固定取值': 6, '全网规划': 2, '本端规划': 5}（多值→atom 应考虑 decision_driven）
