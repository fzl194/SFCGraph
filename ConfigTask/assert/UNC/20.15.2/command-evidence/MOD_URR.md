# 命令证据包：MOD URR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/修改URR（MOD URR）_09897159.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于修改使用量上报规则信息。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 如果引用了该使用量上报规则信息的计费属性记录存在，则当使用量上报模式USAGERPTMODE为在线计费ONLINE时，只允许修改ONLMETERINGTYPE；当使用量上报模式USAGERPTMODE为离线计费OFFLINE时，只允许修改OFFMETERINGTYPEE。
- 当同时配置UPSID、DOWNSID且不配置离线RG时，离线计费话单中RG取值使用配置的D

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| URRNAME | 使用量上报规则名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| URRID | URR标识 | local_planned | optional | 无 | 整数类型，取值范围为0～2147483646。 |
| USAGERPTMODE | 使用量上报模式 | local_planned | optional | 无 | 枚举类型。 |
| OFFCOMPOUNDTYPE | 离线计费标识组成类型 | local_planned | conditional | 无 | 枚举类型。 |
| ONLCOMPOUNDTYPE | 在线计费标识组成类型 | local_planned | conditional | 无 | 枚举类型。 |
| RG | 离线计费组 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| SID | 离线业务标识 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| UPSID | 离线上行业务标识 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| DOWNSID | 离线下行业务标识 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| ONLINERG | 在线计费组 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| ONLINESID | 在线业务标识 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| OFFMETERINGTYPE | 离线计费统计类型 | local_planned | conditional | 无 | 枚举类型。 |
| ONLMETERINGTYPE | 在线计费统计类型 | local_planned | conditional | 无 | 枚举类型。 |
| TIMERSUVALUE | 时间配额值（秒） | 对端协商 | conditional | 无 | 整数类型，取值范围为0～3600000。 |
| VOLUMERSUVALUE | 流量配额值（字节） | 对端协商 | conditional | 无 | 整数类型，取值范围为0～4294967295。 |
| OFCSRVTMPLNAME | 离线业务模板名 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| REDIRENDTOKEN | Gy重定向结束Token | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| MONITORINGKEY | 监控属性值 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。4294967295是无效值，初始化时MonitoringKey |
| EVENTRSUVALUE | 事件配额值（次） | 对端协商 | conditional | 无 | 整数类型，取值范围为0～5000。 |
| N40AGESW | N40接口场景下是否允许老化 | global_planned | conditional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/调测融合计费的流量计费功能_89257221.md`**
- 操作步骤上下文（±2 行原文）：
  L56:
    >           - 如果绑定了计费RG，且匹配中业务流，请执行[步骤 8](#ZH-CN_OPI_0289257221__step1829245425110)。
    >           - 如果没有绑定计费RG，请执行[步骤 7.b](#ZH-CN_OPI_0289257221__substep469521910418)。
    >     b. 执行 [**MOD URR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/修改URR（MOD URR）_09897159.md) 、 [**MOD URRGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/修改URR组（MOD URRGROUP）_09897194.md) 、 [**MOD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md) 、 [**MOD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/修改规则（MOD RULE）_09897202.md) ，按照规划值为用户绑定RG。重新激活用户，观察N40接口计费流量与用户实际访问流量是否一致。
    >           - 如果一致，调测完成。
    >           - 如果不一致，请执行[步骤 8](#ZH-CN_OPI_0289257221__step1829245425110)。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > **[RMV URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/删除URR（RMV URR）_09897160.md)**
    > 
    > **[MOD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/修改URR（MOD URR）_09897159.md)**
    > 
    > **[LST URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/查询URR（LST URR）_09897161.md)**

## ④ 自动比对
- 命令真相参数（20）：['DOWNSID', 'EVENTRSUVALUE', 'MONITORINGKEY', 'N40AGESW', 'OFCSRVTMPLNAME', 'OFFCOMPOUNDTYPE', 'OFFMETERINGTYPE', 'ONLCOMPOUNDTYPE', 'ONLINERG', 'ONLINESID', 'ONLMETERINGTYPE', 'REDIRENDTOKEN', 'RG', 'SID', 'TIMERSUVALUE', 'UPSID', 'URRID', 'URRNAME', 'USAGERPTMODE', 'VOLUMERSUVALUE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
