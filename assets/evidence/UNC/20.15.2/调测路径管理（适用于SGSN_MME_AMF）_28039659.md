# 调测路径管理（适用于SGSN/MME/AMF）

- [操作场景](#ZH-CN_OPI_0228039659__1.3.1)
- [必备事项](#ZH-CN_OPI_0228039659__1.3.2)
- [操作步骤](#ZH-CN_OPI_0228039659__1.3.3)

## [操作场景](#ZH-CN_OPI_0228039659)

当已经部署路径管理功能时，需要对本功能进行调测，确保功能可以正常使用。

> **说明**
> 适用于 SGSN、 MME、AMF。

## [必备事项](#ZH-CN_OPI_0228039659)

前提条件

- 请仔细阅读[WSFD-010600 路径管理特性概述](特性概述_28039656.md)。
- 完成[激活路径管理（适用于SGSN/MME/AMF）](激活路径管理（适用于SGSN_MME_AMF）_28039657.md)。

数据

该操作无需准备数据。

工具

OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0228039659)

1. 创建用户跟踪任务和GTP-C /GTP-U 接口跟踪任务。
  预期结果：可观察到GTP-C /GTP-U 公共表配置信息。
2. 用户开机发起附着请求。
  预期结果：用户成功附着到 SGSN/ MME/AMF。
3. 用户发起PDP上下文激活请求，请求Background类的QoS。
  预期结果：用户成功激活PDP上下文。
4. 通过GTP-C /GTP-U 跟踪窗口观察消息。
  预期结果：在GTP-C /GTP-U 跟踪窗口中可以看到， SGSN/ MME/AMF定时向对端发送Echo Request消息，对端返回Echo Response消息。
5. 设定对端故障。
  预期结果：在GTP-C /GTP-U 跟踪窗口中可以看到， SGSN/ MME/AMF定时向对端发送Echo Request消息，对端没有返回Echo Response消息。
6. T3*N3时间内都没有收到路径探测消息的响应消息。
  预期结果：通过 **[DSP GTPCPATH](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C路径管理/显示GTP-C路径(DSP GTPCPATH)_72225591.md)** / **[DSP GTPUPATH](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/数据转发管理/GTP-U/GTP-U路径管理/显示GTP-U路径(DSP GTPUPATH)_26305650.md)** 查询到路径状态为 “故障” 。
