# 命令证据包：RMV LOGICINF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/删除逻辑接口（RMV LOGICINF）_09896725.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

![](删除逻辑接口（RMV LOGICINF）_09896725.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，此操作会删除逻辑接口，可能导致相关业务中断。

该命令用于删除指定的逻辑接口。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 删除的逻辑接口需为系统中存在的逻辑接口，否则命令执行失败。
- 若逻辑接口被某些对象绑定时，则不允许被删除掉。
- 逻辑接口配置不支持在主备SMF之间自动同步，需要在主备SMF上分别配置。
- 此操作会删除逻辑接口，可能导致相关业务中断。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| NAME | 逻辑接口名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/调测到PCRF的数据_31422954.md`**
- 操作步骤上下文（±2 行原文）：
  L153:
    >     a. 执行[**RMV DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/删除Diameter链路（RMV DIAMCONNECTION）_09897268.md)和[**RMV DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.md)命令，删除原有配置。
    >     b. 执行[**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)和[**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)命令，按照规划数据重新配置GGSN/PGW-C的Gx口设备标识。
    >     c. **可选：**如果Gx接口IP与规划值不一致，请执行[**RMV LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/删除逻辑接口（RMV LOGICINF）_09896725.md)命令，删除原有配置。
    >     d. **可选：**执行[**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)命令，按照规划数据重新配置GGSN/PGW-C的Gx接口IP数据。
    >     e. 再次执行[步骤 2](#ZH-CN_OPI_0231422954__stp1)，查看PCRF状态。

## ④ 自动比对
- 命令真相参数（1）：['NAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
