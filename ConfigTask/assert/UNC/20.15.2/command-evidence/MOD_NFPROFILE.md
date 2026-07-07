# 命令证据包：MOD NFPROFILE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于修改NF实例的概述信息。对于已向NRF注册过的NF实例，使用该命令修改NF实例的概述信息后，将会触发其向NRF发起更新流程。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 使用该命令修改NF实例的概述信息后，将会向NRF发起更新流程。
- NF状态不支持选择Suspend状态。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| NFINSTANCENAME | NF实例名称 | global_planned | required | 无 | 字符串类型，输入长度范围是0~50。 |
| NFSTATUS | NF状态 | global_planned | optional | 无 | <br>- “Invalid（Invalid）”：表示当前NF处于无效态，如果配置成该值，NF注册的 |
| HTTPLEIDX | http地址实例标识 | global_planned | optional | 无 | 整数类型，取值范围是0~255。 |
| FQDN | 域名 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~255。不区分大小写。 |
| INTERPLMNFQDN | PLMN间域名 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~255。不区分大小写。 |
| CAPACITY | 容量 | global_planned | optional | 无 | 整数类型，取值范围是0~65535。值越大表示容量越大。 |
| PRIORITY | 优先级 | global_planned | optional | 无 | 整数类型，取值范围是0~65535。值越小优先级越高。 |
| LOAD | 负载 | global_planned | optional | 无 | 整数类型，取值范围是0~100。 |
| LOCALITY | 位置信息 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~150。 |
| ALLOWEDNFTYPES | 支持的NF类型 | global_planned | optional | 无 | <br>- AllowNfINVALID（AllowNfINVALID） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-104302

**md：`WSFD-104302/WSFD-104302 AMF Pool用户迁移参考信息_10427848.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - **[**ADD NFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/增加NF实例概述信息（ADD NFPROFILE）_09654146.md)**
    > - **[**RMV NFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/删除NF实例概述信息（RMV NFPROFILE）_09651742.md)**
    > - **[**MOD NFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)**
    > - **[**LST NFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/查询NF实例概述信息（LST NFPROFILE）_09651589.md)**
    > - **[**STR OFFLOADAMF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AMF Pool 迁移控制/启动AMF迁移任务（STR OFFLOADAMF）_09653235.md)**

**md：`WSFD-104302/激活AMF Pool 用户迁移特性_10427846.md`**
- 数据规划表（该命令的参数行）：
  | **[**MOD NFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)** | NF实例名称（NFINSTANCENAME） | AMF_Instance_0 | 全网规划 | 用户迁移信息 |
  | **[**MOD NFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)** | 容量（CAPACITY） | 0 | 全网规划 | 用户迁移信息 |

### WSFD-109101

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**MOD NFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md) | NF实例名称（NFINSTANCENAME） | SMF_Instance_0 | - | 根据NFLOC选择PCF时需要规划。 |
  | [**MOD NFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md) | 位置信息（LOCALITY） | beijing | 全网规划 | 根据NFLOC选择PCF时需要规划。 |
- 操作步骤上下文（±2 行原文）：
  L169:
    >             [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >           c. （可选）[**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)命令中的“选择PCF方式（PCFSELECTMODE）”包含“NFLOC”时，在SMF的NF概述信息中增加位置信息。
    >             [**MOD NFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)
    >     11. **可选：**配置PCC策略组。用于动态PCC时PCF下发预定义规则，或本地PCC时的静态规则。
    >       [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)

### WSFD-205015

**md：`WSFD-205015/参考信息_22851145.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - **[DSP NFCACHE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF Cache管理/查询NF缓存信息（DSP NFCACHE）_09651365.md)**
    > - **[DSP REGNFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/显示网元概述信息（DSP REGNFPROFILE）_29286833.md)**
    > - **[MOD NFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)**
    > - **[ADD SMFINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/SMF/SMF信息管理/增加SMF信息（ADD SMFINFO）_09653991.md)**
    > - **[ADD NFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF TAI信息管理/增加NF TAI信息（ADD NFTAI）_09652077.md)**

**md：`WSFD-205015/激活SMF支持多服务区特性（适用于SMF）_22891113.md`**
- 数据规划表（该命令的参数行）：
  | **[MOD NFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)** | NFINSTANCENAME（NF实例名称） | smf1 | 本端规划 | 可使用“LST NFPROFILE”命令查看目前SMF实例的优先级，通过“MOD NFPROFILE”确保服务注册消息中smfInfo的priority值小于smfInfoList中smfInfo的priority值。 |
  | **[MOD NFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)** | PRIORITY（优先级） | 1 | 全网规划 | 可使用“LST NFPROFILE”命令查看目前SMF实例的优先级，通过“MOD NFPROFILE”确保服务注册消息中smfInfo的priority值小于smfInfoList中smfInfo的priority值。 |
  | **[MOD NFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)** | NFINSTANCENAME（NF实例名称） | smf2 | 本端规划 | 可使用“LST NFPROFILE”命令查看目前SMF实例的优先级，通过“MOD NFPROFILE”确保服务注册消息中smfInfo的priority值小于smfInfoList中smfInfo的优先级。 |
  | **[MOD NFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)** | PRIORITY（优先级） | 1 | 全网规划 | 可使用“LST NFPROFILE”命令查看目前SMF实例的优先级，通过“MOD NFPROFILE”确保服务注册消息中smfInfo的priority值小于smfInfoList中smfInfo的优先级。 |
- 任务示例脚本（该命令行）：
  `MOD NFPROFILE: NFINSTANCENAME="smf1", PRIORITY=1;`
  `MOD NFPROFILE: NFINSTANCENAME="smf2", PRIORITY=1;`
- 操作步骤上下文（±2 行原文）：
  L149:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 修改SMF实例概述信息。
    >   **[MOD NFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)**
    > 4. 配置SMF实例信息。
    >   **[ADD SMFINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/SMF/SMF信息管理/增加SMF信息（ADD SMFINFO）_09653991.md)**
  L197:
    > 
    > ```
    > MOD NFPROFILE: NFINSTANCENAME="smf1", PRIORITY=1;
    > ```
    > 
  L251:
    > 
    > ```
    > MOD NFPROFILE: NFINSTANCENAME="smf2", PRIORITY=1;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（10）：['ALLOWEDNFTYPES', 'CAPACITY', 'FQDN', 'HTTPLEIDX', 'INTERPLMNFQDN', 'LOAD', 'LOCALITY', 'NFINSTANCENAME', 'NFSTATUS', 'PRIORITY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 5, '-': 1, '本端规划': 2}（多值→atom 应考虑 decision_driven）
