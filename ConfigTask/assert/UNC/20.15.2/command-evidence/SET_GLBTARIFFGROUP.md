# 命令证据包：SET GLBTARIFFGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用于绑定全局费率切换组，UNC优先选择user-profile实例、APN实例绑定的费率切换组，当上述两者都没有绑定时，UNC选择全局配置的费率切换组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置的费率切换组名GLBTARIFFGROUP时，要执行ADD TARIFFGROUP命令添加费率切换组名。如果没有添加，则执行命令失败。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GLBTARIFFGRP | 费率切换组名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > - [**ADD WEEKDAY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > - [**SET GLBCDRFLDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/全局话单字段模板/设置全局话单模板（SET GLBCDRFLDTEMP）_09896895.md)

**md：`WSFD-011201/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBTARIFFGROUP** | 费率切换组名（GLBTARIFFGRP） | testtarif | 本端规划 | 绑定全局费率切换组。 |
- 任务示例脚本（该命令行）：
  `SET GLBTARIFFGROUP: GLBTARIFFGRP="testtarif";`
- 操作步骤上下文（±2 行原文）：
  L65:
    >       **ADD TARIFFGROUP**
    > 2. 配置全局费率切换组。
    >   **SET GLBTARIFFGROUP**
    > 3. 配置APN下的费率切换组。
    >     a. 配置APN。如已配置APN，请跳过该步骤。
  L141:
    > 2. 任务一：配置全局的费率切换组。
    >   ```
    >   SET GLBTARIFFGROUP: GLBTARIFFGRP="testtarif";
    >   ```
    > 3. 任务二：基于APN **apn-test** 配置费率切换组。

**md：`WSFD-011201/调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBTARIFFGROUP** | 费率切换组名（GLBTARIFFGRP） | testtariff | 本端规划 | 绑定全局费率切换组 |

### WSFD-011206

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBTARIFFGROUP** | 费率切换组名（GLBTARIFFGRP） | tar_nb | 本端规划 | 绑定全局费率切换组。 |
- 任务示例脚本（该命令行）：
  `SET GLBTARIFFGROUP: GLBTARIFFGRP="tar_nb";`
- 操作步骤上下文（±2 行原文）：
  L72:
    >       > - 当“TCMODE”参数配置为“MONTHLY”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，月初第一天00：00再强制进行费率切换，生效范围为所有用户。
    > 2. 配置全局费率切换组。
    >   **SET GLBTARIFFGROUP**
    > 
    > ## [任务示例](#ZH-CN_OPI_0286411191)
  L131:
    > 2. 配置全局的费率切换组。
    >   ```
    >   SET GLBTARIFFGROUP: GLBTARIFFGRP="tar_nb";
    >   ```

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L46:
    > - [**ADD WEEKDAY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L46:
    > - [**ADD WEEKDAY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)

## ④ 自动比对
- 命令真相参数（1）：['GLBTARIFFGRP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 3}（多值→atom 应考虑 decision_driven）
