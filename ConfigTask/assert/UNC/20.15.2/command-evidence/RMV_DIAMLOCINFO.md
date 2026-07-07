# 命令证据包：RMV DIAMLOCINFO
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

![](删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除Diameter本端信息可能导致Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

此命令用来删除Diameter本端信息。支持批量删除，不给HOSTNAME字段赋
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 当未指定本端主机名时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 该命令用于删除Gx或IP-CAN Session接口相关的标识信息。当被删除的标识信息已经在用时，对已建立的IP-CAN Session影响较大。
- 删除后，将导致所有Group下使用该LocalInfo的链路断开，已经建立的IP-CAN Session会话状态不受影响

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOSTNAME | 本端主机名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～127。不支持空格。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/调测到PCRF的数据_31422954.md`**
- 操作步骤上下文（±2 行原文）：
  L151:
    >     - 如果配置不一致，请执行[步骤 6](#ZH-CN_OPI_0231422954__stp5)。
    > 6. 修改GGSN/PGW-C的Gx口设备标识。
    >     a. 执行[**RMV DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/删除Diameter链路（RMV DIAMCONNECTION）_09897268.md)和[**RMV DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.md)命令，删除原有配置。
    >     b. 执行[**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)和[**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)命令，按照规划数据重新配置GGSN/PGW-C的Gx口设备标识。
    >     c. **可选：**如果Gx接口IP与规划值不一致，请执行[**RMV LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/删除逻辑接口（RMV LOGICINF）_09896725.md)命令，删除原有配置。

### WSFD-109001

**md：`WSFD-109001/调测到OCS的数据_95923404.md`**
- 操作步骤上下文（±2 行原文）：
  L61:
    >     - 如果配置不一致，请执行[步骤 6](#ZH-CN_OPI_0295923404__step5)。
    > 6. 修改GGSN/PGW-C设备标识。
    >     a. 执行 **RMV DIAMLOCINFO** 命令，删除原有配置。
    >     b. 执行 **ADD DIAMLOCINFO** 命令，按照规划数据重新配置GGSN/PGW-C的设备标识。
    >     c. 再次执行 [步骤 1](#ZH-CN_OPI_0295923404__step1) ，查看OCS状态。

### WSFD-011132

**md：`WSFD-011132/调测Gx over DRA_29578142.md`**
- 操作步骤上下文（±2 行原文）：
  L128:
    >     - 如果配置不一致，请执行[步骤 7](#ZH-CN_OPI_0229578142__stp5)。
    > 7. 修改 GGSN/PGW-C 的Gx口设备标识。
    >     a. 执行 **[RMV DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.md)** 命令，删除原有配置。
    >     b. 执行 **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** 命令，按照规划数据重新配置 GGSN/PGW-C 的Gx口设备标识。
    >     c. 再次执行 [步骤 2](#ZH-CN_OPI_0229578142__stp0) ，查看DRA的链路组状态。

## ④ 自动比对
- 命令真相参数（1）：['HOSTNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
