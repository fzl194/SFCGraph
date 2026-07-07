# 命令证据包：ADD SELECTCHFGBYCC
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/增加基于CC选择CHF处理（ADD SELECTCHFGBYCC）_09652118.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加基于CC选择CHF处理。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入20条记录。
- 不允许配置的CCVALUE和掩码CCMASK取与后的值不等于CCVALUE。
- 不允许配置的CCVALUE和掩码CCMASK取与后的值，与当前已有配置的CCVALUE和对应的CCMASK取与后的值相等。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTYPE | Charge Characteristic类型 | local_planned | required | 无 | <br>- DEFAULT（未指定Charge Characteristic的值） |
| CCVALUE | Charge Characteristic值 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| MASK | Charge Characteristic特定值掩码 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| PRIORITY | Charge Characteristic优先级 | local_planned | conditional | 无 | 整数类型，取值范围是1~65535。 |
| PRIMARYCHFGRP | 主CHF组 | global_planned | optional | 无 | 字符串类型，输入长度范围是1~63。该参数输入空格或者null（不区分大小写）清空参数值。 |
| SECONDARYCHFGRP | 备CHF组 | global_planned | optional | 无 | 字符串类型，输入长度范围是1~63。该参数输入空格或者null（不区分大小写）清空参数值。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**ADD TNFGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/增加目标NF组（ADD TNFGRP）_09651791.md)
    > - [**ADD TNFBINDGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/增加目标NF实例绑定组（ADD TNFBINDGRP）_09651533.md)
    > - [**ADD SELECTCHFGBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/增加基于CC选择CHF处理（ADD SELECTCHFGBYCC）_09652118.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)

**md：`WSFD-011206/融合计费可靠性（未部署NCG）_75816427.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > 
    > > **说明**
    > > 主备CHF可以通过PCF下发，也可以通过 **ADD SELECTCHFGBYCC** 命令的“主CHF组”和“备CHF组”配置。
    > 
    > **图2** 主备CHF切换示意图

**md：`WSFD-011206/计费会话创建流程_01_10001.md`**
- 操作步骤上下文（±2 行原文）：
  L67:
    >       UDM下发的CC有两种：Session级的CC和基于APN/DNN的CC，DNN/APN级CC优先级更高。
    >     e. SMF通过NRF发现CHF。该方式下不支持3GPP 29510协议中规定的通过主备方式选择CHF，仅支持通过优先级和权重选择CHF。
    >     f. SMF根据本地配置**ADD SELECTCHFGBYCC**命令选择CHF，即基于本地配置的CC选择CHF。
    > 9. SMF发送[Nchf_ConvergedCharging_ChargingDataCreate Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_30f76786/Nchf_ConvergedCharging_ChargingDataCreate Request_23690012.md)消息到CHF，申请授权业务使用以及申请配额。消息中携带用户标识、PDU会话信息等标识信息，以及可能的一个或多个配额申请信息，每个配额申请对应一个费率组RG，携带的配额申请信息通过UNC上的**SET CTXSTARTRATING**命令配置。Nchf_ConvergedCharging_Create Request请求消息中携带的信元举例如下所示：
    >   ```

**md：`WSFD-011206/配置CHF选择方式_92091086.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SELECTCHFGBYCC** | Charge Characteristic类型（CCTYPE） | VALUE | 固定取值 | 配置CC和CHF Group的关联关系。 |
  | **ADD SELECTCHFGBYCC** | Charge Characteristic值（CCVALUE） | 0x1111 | 已配置数据中获取/从对端获取 | 本地CC时，从已配置数据中获取。<br>从UDM获取签约CC时，从对端获取。 |
  | **ADD SELECTCHFGBYCC** | Charge Characteristic特定值掩码（MASK） | 0xffff | 本端规划 | - |
  | **ADD SELECTCHFGBYCC** | Charge Characteristic优先级（PRIORITY） | 2 | 全网规划 | 数值越小，优先级越高。 |
  | **ADD SELECTCHFGBYCC** | 主CHF组（PRIMARYCHFGRP） | ChfGroup1 | 已配置数据中获取 | - |
  | **ADD SELECTCHFGBYCC** | SECONDARYCHFGRP（备CHF组） | ChfGroup2 | 已配置数据中获取 | - |
- 任务示例脚本（该命令行）：
  `ADD SELECTCHFGBYCC: CCTYPE=VALUE, CCVALUE="0x1111", MASK="0xffff", PRIORITY=2, PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";`
- 操作步骤上下文（±2 行原文）：
  L86:
    >             **ADD TNFBINDGRP**
    >     3. 配置基于CC选择CHF组。
    >       **ADD SELECTCHFGBYCC**
    > - 配置基于标准化服务发现选择的CHF。服务化发现CHF存在以下两种方式：
    >     1. 基于NRF选择CHF，不需要专有配置。
  L173:
    > ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;
    > ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;
    > ADD SELECTCHFGBYCC: CCTYPE=VALUE, CCVALUE="0x1111", MASK="0xffff", PRIORITY=2, PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（6）：['CCTYPE', 'CCVALUE', 'MASK', 'PRIMARYCHFGRP', 'PRIORITY', 'SECONDARYCHFGRP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'固定取值': 1, '已配置数据中获取/从对端获取': 1, '本端规划': 1, '全网规划': 1, '已配置数据中获取': 2}（多值→atom 应考虑 decision_driven）
