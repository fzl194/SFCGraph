# 调测路径管理（适用于GGSN/SGW-C/PGW-C/SMF）

- [操作场景](#ZH-CN_OPI_0228039660__1.3.1)
- [必备事项](#ZH-CN_OPI_0228039660__1.3.2)
- [操作步骤](#ZH-CN_OPI_0228039660__1.3.3)

## [操作场景](#ZH-CN_OPI_0228039660)

当已经部署路径管理功能时，需要对本功能进行调测，确保功能可以正常使用。

> **说明**
> 适用于GGSN/SGW-C/PGW-C/SMF。

## [必备事项](#ZH-CN_OPI_0228039660)

前提条件

- 请仔细阅读[WSFD-010600 路径管理特性概述](特性概述_28039656.md)。
- 完成[激活路径管理（适用于GGSN/SGW-C/PGW-C/SMF）](激活路径管理（适用于GGSN_SGW-C_PGW-C_SMF）_28039658.md)。

数据

该操作无需准备数据。

工具

OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0228039660)

1. 创建用户跟踪任务和PFCP接口跟踪任务。
  预期结果：可观察到PFCP公共表配置信息。
2. 用户发起PDU会话请求。
  预期结果：用户成功建立PDU会话。
3. 通过PFCP跟踪窗口观察消息。
  预期结果：在PFCP跟踪窗口中可以看到，SMF定时向对端发送Heartbeat Request消息，对端返回Heartbeat Response消息。
4. 设置对端故障。
  预期结果：在PFCP跟踪窗口中可以看到，SMF定时向对端发送Heartbeat Request消息，对端不返回Heartbeat Response消息。
5. Heartbeat Request消息发送次数到达阈值后SMF还未收到Heartbeat Response消息。
  预期结果：通过 **[DSP PFCPASSOC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP路径管理/PFCP路径查询/查询PFCP偶联相关数据（DSP PFCPASSOC）_09651529.md)** 查询到链路状态为 “DEACTIVATED” 。
