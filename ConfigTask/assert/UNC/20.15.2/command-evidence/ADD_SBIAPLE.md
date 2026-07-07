# 命令证据包：ADD SBIAPLE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：该命令用于增加本端服务化接口接入点信息，即本端服务化接口实体，供基于服务化接口的业务使用。当本端NF需要和目的NF之间建立服务化连接时，需要添加本配置。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 本端服务化接口实体（SBIAPLE）引用的HTTP本端实体组（HTTPLEGRP）内必须存在一个作为Server端的HTTP本端实体和一个作为Client端的HTTP本端实体。
- 如果不配置对端NF信息（目的NF类型、目的NF服务、CHF的目的NF类型），则只能配置一个服务化接口实体。
- 如果配置对端NF信息（目的NF类型、目的NF服务、CHF的目的NF类型）

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| INDEX | 索引 | local_planned | required | 无 | 整数类型，取值范围是1~128。 |
| HTTPLEGRPIDX | HTTP本端实体组标识 | local_planned | required | 无 | 整数类型，取值范围是1~64。 |
| NFTYPE | 本端NF类型 | global_planned | required | 无 | <br>- “INVALID（INVALID）”：无效值 |
| PEERNFTYPE | 目的NF类型 | global_planned | conditional | 无 | 仅支持配置目的NF为Nchf。 |
| CHFPEERNFTYPE | CHF的目的NF类型 | local_planned | conditional | 无 | 仅支持配置目的NF为Nnrf和Nocs |
| PEERSERVICE | 目的NF服务 | global_planned | conditional | 无 | 仅支持配置目的NF服务为Nchf_ConvCharg服务。 |
| DESCRIPTION | 描述 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~255。 |
| CHFPEERNFINSTID | CHF的目的NF实例ID | local_planned | conditional | 无 | 字符串类型，输入长度范围是0~255。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010308

**md：`WSFD-010308/WSFD-010308 SBI接口加密参考信息_70185217.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - [**修改HTTP本端实体(MOD HTTPLE)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/修改HTTP本端实体（MOD HTTPLE）_28971845.md)
    > - [**查询HTTP本端实体(LST HTTPLE)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/查询HTTP本端实体（LST HTTPLE）_29291769.md)
    > - [**增加本端实例端点(ADD SBIAPLE)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)
    > - [**删除本端实例端点(RMV SBIAPLE)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/删除服务化接口本端实体（RMV SBIAPLE）_84132108.md)
    > - [**修改本端实例端点(MOD SBIAPLE)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/修改服务化接口本端实体（MOD SBIAPLE）_83813638.md)

**md：`WSFD-010308/激活SBI接口加密特性(CERT)_70185215.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md) | 索引 | AMF：1<br>NRF：2 | 全网规划 | - |
  | [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md) | HttpLEGRP索引 | AMF：1<br>NRF：2 | 全网规划 | - |
  | [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md) | 本端NF类型 | AMF：NFTypeAMF<br>NRF：NFTypeNRF | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=1, NFTYPE=NFTypeAMF, DESCRIPTION="AMF";`
  `ADD SBIAPLE: INDEX=2, HTTPLEGRPIDX=2, NFTYPE=NFTypeNRF, DESCRIPTION="NRF";`
- 操作步骤上下文（±2 行原文）：
  L96:
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     h. 增加AMF服务化接口的接入点信息。
    >       [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)
    >     i. 设置对接的NRF实例支持TLS。
    >           - 新增NRF实例场景：参考[配置和NRF的对接](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置AMF/配置SBI接口/配置和NRF的对接_29346409.md)，其中[**ADD NRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NRF管理/NRF配置管理/NRF实例配置管理/增加NRF信息（ADD NRF）_09652106.md)的“TLS”参数配置为“true”。
  L115:
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     h. 增加NRF服务化接口的接入点信息。
    >       [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0170185215)
  L174:
    > 
    > ```
    > ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=1, NFTYPE=NFTypeAMF, DESCRIPTION="AMF";
    > ```
    > 

**md：`WSFD-010308/激活SBI接口加密特性(PSK)_57783838.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md) | 索引(INDEX) | AMF：1<br>NRF：2 | 全网规划 | - |
  | [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md) | HTTP本端实体组标识(HTTPLEGRPIDX) | AMF：1<br>NRF：2 | 全网规划 | - |
  | [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md) | 本端NF类型(NFTYPE) | AMF：NFTypeAMF<br>NRF：NFTypeNRF | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=1, NFTYPE=NFTypeAMF, DESCRIPTION="AMF";`
- 操作步骤上下文（±2 行原文）：
  L83:
    >       [**ADD HTTPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)
    >     k. 增加AMF服务化接口的接入点信息。
    >       [**ADD SBIAPLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)
    >     l. 设置对接的NRF实例支持TLS。
    >           - 新增NRF实例场景：参考[配置和NRF的对接](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置AMF/配置SBI接口/配置和NRF的对接_29346409.md)，其中[**ADD NRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NRF管理/NRF配置管理/NRF实例配置管理/增加NRF信息（ADD NRF）_09652106.md)的“TLS”参数配置为“true”。
  L157:
    > 
    > ```
    > ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=1, NFTYPE=NFTypeAMF, DESCRIPTION="AMF";
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/配置QoS能力开放功能_48518810.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD SBIAPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)** | 索引（INDEX） | 1 | 本端规划 | 增加服务化接口本端实体 |
  | **[ADD SBIAPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)** | HttpLEGRP索引（HTTPLEGRPIDX） | 3 | 本端规划 | 增加服务化接口本端实体 |
  | **[ADD SBIAPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)** | 本端NF类型（NFTYPE） | NFTypeBSF | 全网规划 | 增加服务化接口本端实体 |
  | **[ADD SBIAPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)** | 描述（DESCRIPTION） | BSF | 全网规划 | 增加服务化接口本端实体 |
- 任务示例脚本（该命令行）：
  `ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=3, NFTYPE=NFTypeBSF, DESCRIPTION="BSF";`
- 操作步骤上下文（±2 行原文）：
  L76:
    >   **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)**
    > 7. 配置服务化接口本端实体。
    >   **[ADD SBIAPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)**
    > 8. 使能HTTP1.1开关。
    >   **[SET HTTPCONF](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**
  L142:
    > 5. 配置服务化接口本端实体。
    >   ```
    >   ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=3, NFTYPE=NFTypeBSF, DESCRIPTION="BSF";
    >   ```
    > 6.

## ④ 自动比对
- 命令真相参数（8）：['CHFPEERNFINSTID', 'CHFPEERNFTYPE', 'DESCRIPTION', 'HTTPLEGRPIDX', 'INDEX', 'NFTYPE', 'PEERNFTYPE', 'PEERSERVICE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 8, '本端规划': 2}（多值→atom 应考虑 decision_driven）
