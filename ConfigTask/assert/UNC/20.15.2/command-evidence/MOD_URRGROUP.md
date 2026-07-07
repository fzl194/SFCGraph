# 命令证据包：MOD URRGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/修改URR组（MOD URRGROUP）_09897194.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于修改使用量上报规则组，通过该命令可以指定上下行发起使用的URR名称，即指定上下行报文如何计费。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 此命令采取覆盖重写模式，即会删除URRGroupName的原配置后新建配置。
- 如果引用了该使用量上报规则组的上下文激活时，特定URR记录存在，则不允许修改。
- 修改之后，UPURRNAME1，DOWNURRNAME1，UPURRNAME2，DOWNURRNAME2，UPURRNAME3，DOWNURRNAME3至少要存在其中任意一个。
- 同一个URRGROU

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| URRGROUPNAME | 使用量上报规则组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| UPURRNAME1 | 上行发起URR名称1 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| UPURRNAME2 | 上行发起URR名称2 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| UPURRNAME3 | 上行发起URR名称3 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| DOWNURRNAME1 | 下行发起URR名称1 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| DOWNURRNAME2 | 下行发起URR名称2 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| DOWNURRNAME3 | 下行发起URR名称3 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| NOCHARGINGFLAG | 不计费标记 | local_planned | optional | 无 | 枚举类型。 |

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
  L24:
    > **[RMV URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/删除URR组（RMV URRGROUP）_09897195.md)**
    > 
    > **[MOD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/修改URR组（MOD URRGROUP）_09897194.md)**
    > 
    > **[LST URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/查询URR组（LST URRGROUP）_09897196.md)**

## ④ 自动比对
- 命令真相参数（8）：['DOWNURRNAME1', 'DOWNURRNAME2', 'DOWNURRNAME3', 'NOCHARGINGFLAG', 'UPURRNAME1', 'UPURRNAME2', 'UPURRNAME3', 'URRGROUPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
