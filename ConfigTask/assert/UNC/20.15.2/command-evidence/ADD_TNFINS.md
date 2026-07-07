# 命令证据包：ADD TNFINS
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/增加目标NF实例（ADD TNFINS）_09652354.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加目标NF实例的配置。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令配置时，如果在ADD PNFPROFILE中配置了相同的CHF，即ADD TNFINS中的参数TNFINSNAME和ADD PNFPROFILE中的参数NFINSTANCEID取值相同，则该命令关联的ADD TNFINSIP下配置的所有IP，需要被ADD PNFPROFILE中配置的CHF的IP包含。
- 当命令中的SRVINSID为空时，判断命令中TNFI

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TNFINSINDEX | 目标NF实例索引 | local_planned | required | 无 | 整数类型，取值范围是0~2047。 |
| TNFTYPE | 目标NF类型 | global_planned | required | 无 | <br>- “CHF（CHF）”：CHF |
| TNFINSNAME | 目标NF实例名称 | global_planned | required | 无 | 字符串类型，输入长度范围是0~63。 |
| SRVNAME | 服务名称 | global_planned | optional | 无 | <br>- NrfNfm（NRF提供的Nnrf_NFManagement服务） |
| SRVINSID | 服务实例标识 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~50。 |
| SCHEMA | 协议模式 | global_planned | optional | 无 | <br>- “UriSchemeINVALID（SchemaInvalid）”：已废弃。 |
| FQDN | 域名 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~127。不区分大小写。 |
| NFDESCNAME | NF描述名称 | local_planned | optional | 无 | 字符串类型，输入长度范围是0~255。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD TNFINS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/增加目标NF实例（ADD TNFINS）_09652354.md)
    > - [**ADD TNFINSIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/增加目标NF实例IP地址（ADD TNFINSIP）_09654443.md)
    > - [**ADD TNFGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/增加目标NF组（ADD TNFGRP）_09651791.md)

**md：`WSFD-011206/配置CHF选择方式_92091086.md`**
- 数据规划表（该命令的参数行）：
  | **ADD TNFINS** | 目标NF实例索引（TNFINSINDEX） | - 1<br>- 2 | 本端规划 | 增加主备CHF实例。 |
  | **ADD TNFINS** | 目标NF类型（TNFTYPE） | - CHF<br>- CHF | 固定取值 | - |
  | **ADD TNFINS** | 协议模式（SCHEMA） | - http<br>- http | 全网规划 | - |
  | **ADD TNFINS** | 域名（FQDN） | - chf1.hw.com<br>- chf2.hw.com | 从对端获取 | 与PCF下发的FQDN名称保持一致。 |
- 任务示例脚本（该命令行）：
  `ADD TNFINS: TNFINSINDEX=1, TNFTYPE=CHF, TNFINSNAME="target_chf_0", SCHEMA=http;`
  `ADD TNFINS: TNFINSINDEX=2, TNFTYPE=CHF, TNFINSNAME="target_chf_1", SCHEMA=http;`
  `ADD TNFINS: TNFINSINDEX=1, TNFTYPE=CHF, TNFINSNAME="target_chf_0", SCHEMA=http;`
  `ADD TNFINS: TNFINSINDEX=2, TNFTYPE=CHF, TNFINSNAME="target_chf_1", SCHEMA=http;`
  `ADD TNFINS: TNFINSINDEX=1, TNFTYPE=CHF, TNFINSNAME="target_chf_0", SCHEMA=http, FQDN="chf1.hw.com";`
  `ADD TNFINS: TNFINSINDEX=2, TNFTYPE=CHF, TNFINSNAME="target_chf_1", SCHEMA=http, FQDN="chf2.hw.com";`
  `ADD TNFINS: TNFINSINDEX=1, TNFTYPE=CHF, TNFINSNAME="target_chf_0", SCHEMA=http;`
  `ADD TNFINS: TNFINSINDEX=2, TNFTYPE=CHF, TNFINSNAME="target_chf_1", SCHEMA=http;`
  `ADD TNFINS: TNFINSINDEX=1, TNFTYPE=CHF, TNFINSNAME="target_chf_0", SCHEMA=http;`
  `ADD TNFINS: TNFINSINDEX=2, TNFTYPE=CHF, TNFINSNAME="target_chf_1", SCHEMA=http;`
- 操作步骤上下文（±2 行原文）：
  L70:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 配置目标CHF实例。
    >       **ADD TNFINS**
    >     3. 配置目标CHF实例的IP地址信息。
    >       **ADD TNFINSIP**
  L78:
    >     2. 配置CHF Group。
    >           a. 配置目标CHF实例。
    >             **ADD TNFINS**
    >           b. 配置目标CHF实例的IP地址信息。
    >             **ADD TNFINSIP**
  L95:
    >     1. 配置CHF Group。
    >           a. 配置目标CHF实例。
    >             **ADD TNFINS**
    >           b. 配置目标CHF实例的IP地址信息。
    >             **ADD TNFINSIP**

## ④ 自动比对
- 命令真相参数（8）：['FQDN', 'NFDESCNAME', 'SCHEMA', 'SRVINSID', 'SRVNAME', 'TNFINSINDEX', 'TNFINSNAME', 'TNFTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '固定取值': 1, '全网规划': 1, '从对端获取': 1}（多值→atom 应考虑 decision_driven）
