# 命令证据包：MOD PCRFBINDGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/修改PCRF与PCRF Group的关联关系（MOD PCRFBINDGRP）_09897097.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

此命令用于修改指定的PCRF与PCRF分组绑定关系的参数。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCRFGRPNAME | PCRF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。 |
| PCRFHOSTNAME | PCRF主机名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。 |
| WEIGHT | PCRF权重 | local_planned | optional | 无 | 整数类型，取值范围为1～100。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/调测PCRF负荷分担功能_31422955.md`**
- 操作步骤上下文（±2 行原文）：
  L109:
    >   ```
    >     - 如果各PCRF上的配置的“权重”值与规划值一致，请执行[步骤 5](#ZH-CN_OPI_0231422955__stp7)。
    >     - 如果不一致，请执行[**MOD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/修改PCRF与PCRF Group的关联关系（MOD PCRFBINDGRP）_09897097.md)命令重新配置。
    > 5. 请联系PCRF设备工程师，检查PCRF设备的业务承载性能。
    >     - 如果PCRF设备性能不足以承载当前业务量，请联系运营商重新规划PCRF。

## ④ 自动比对
- 命令真相参数（3）：['PCRFGRPNAME', 'PCRFHOSTNAME', 'WEIGHT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
