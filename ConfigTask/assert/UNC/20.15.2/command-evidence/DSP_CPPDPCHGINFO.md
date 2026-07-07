# 命令证据包：DSP CPPDPCHGINFO
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费维护/用户计费信息/查询计费上下文信息（DSP CPPDPCHGINFO）_09897010.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于查询用户在内容计费及PDP计费情况下的上下文信息，检查话单信息或CCR消息信息。
**notes（规格/上限→应投影 atom rule）**：
- 所查询到的用户配额用量为SMF/PGW-C上已收集但未上报的部分。这部分配额用量既不是用户上线以来的总流量，也不是上次上报计费中心以来的总流量，而是上次上报计费中心以后从UPF/PGW-U获取的还未上报计费中心的流量。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBSCRIBERID | 用户标识类型 | local_planned | required | 无 | 枚举类型。 |
| IMSI | IMSI | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～15。 |
| MSISDN | MSISDN | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～15。 |
| IPV4 | IPv4地址 | local_planned | conditional | 无 | IPv4地址类型。 |
| IPV6 | IPv6地址 | global_planned | conditional | 无 | IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。 |
| NSAPI | NSAPI | local_planned | optional | 无 | 整数类型，取值范围为1～63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置异常场景数据_31422947.md`**
- 操作步骤上下文（±2 行原文）：
  L98:
    >   > - GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。
    >   >     - 方式1：通过[**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)“HOLDINGTIME”控制对放通用户的后续处理。
    >   >     - 方式2：通过[**DSP CPPDPCHGINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费维护/用户计费信息/查询计费上下文信息（DSP CPPDPCHGINFO）_09897010.md)查询被放通用户的归属信息。
    > 
    > ## [任务示例](#ZH-CN_OPI_0231422947)

### WSFD-109001

**md：`WSFD-109001/配置DCC处理动作_95923447.md`**
- 操作步骤上下文（±2 行原文）：
  L139:
    >   > - GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。
    >   >     - 方式1：通过**SET FHBYPASS**命令“HOLDINGTIME”控制对放通用户的后续处理，即是否转离线。
    >   >     - 方式2：通过**DSP CPPDPCHGINFO**查询被放通用户的归属信息。
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923447)

## ④ 自动比对
- 命令真相参数（6）：['IMSI', 'IPV4', 'IPV6', 'MSISDN', 'NSAPI', 'SUBSCRIBERID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
