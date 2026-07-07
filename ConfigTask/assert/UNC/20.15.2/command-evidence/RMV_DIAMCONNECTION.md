# 命令证据包：RMV DIAMCONNECTION
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/删除Diameter链路（RMV DIAMCONNECTION）_09897268.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

![](删除Diameter链路（RMV DIAMCONNECTION）_09897268.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除Diameter链路信息可能导致Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

该命令用于删除所有Diameter链路配置信息，或者删除指定Diameter链
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 当未指定Diameter链路组名时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 所有参数都不指定，则删除所有记录。
- 不指定LOCALPORT参数，表示删除由所有其他输入参数锁定的CONNECTION记录，包括系统指定端口或用户指定端口的记录；指定LOCALPORT参数为0时，表示删除系统指定端口CONNECTION记录；指定LOCA

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| DIAMCONNGRP | Diameter链路组名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| LOCINTERFACE | 本端接口名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| PEERADDRTYPE | 对端地址类型 | 对端协商 | optional | 无 | 枚举类型。 |
| PEERIPV4ADDR | 对端IPv4地址 | 对端协商 | conditional | 无 | IPv4地址类型。不支持0.0.0.0和255.255.255.255。 |
| PEERIPV6ADDR | 对端IPv6地址 | 对端协商 | conditional | 无 | IPv6地址类型。不支持全F。 |
| PEERPORT | 对端端口号 | 对端协商 | conditional | 无 | 整数类型，取值范围为1～65534。 |
| PEERSCTPENDPT | 对端SCTP端点名称 | 对端协商 | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| LOCALPORT | 本端端口 | local_planned | optional | 无 | 整数类型，取值范围为0，13200～13263，16400～16463，19765～19784。 |

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

## ④ 自动比对
- 命令真相参数（8）：['DIAMCONNGRP', 'LOCALPORT', 'LOCINTERFACE', 'PEERADDRTYPE', 'PEERIPV4ADDR', 'PEERIPV6ADDR', 'PEERPORT', 'PEERSCTPENDPT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
