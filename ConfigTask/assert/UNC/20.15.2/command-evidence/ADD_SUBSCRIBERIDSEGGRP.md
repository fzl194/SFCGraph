# 命令证据包：ADD SUBSCRIBERIDSEGGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用来配置IMSI/MSISDN/IMEISV号码段组，用于根据号段组选择USERPROFILE作为本地策略、根据号段选择OCS、用户根据号段选择OCS组以及在线计费模板、根据号段选择CG组、根据号段选择SGW离线计费方式等。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 如果绑定多个IMSI/MSISDN/IMEISV号码段，需多次执行此命令。
- 系统最大支持配置128条IMSI/MSISDN/IMEISV号码段组。每条IMSI/MSISDN/IMEISV号码段组最大绑定12000条IMSI/MSISDN/IMEISV号码段，号段组单个UNC绑定规格为25000个。
- 配置SUBSCRIBERIDSEGGRP前，需要首先通过AD

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SEGGROUPNAME | IMSI/MSISDN/IMEISV号段组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| SEGMENTNAME | IMSI/MSISDN/IMEISV号段名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| SEGMENTTYPE | 号段类型 | local_planned | required | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD CGGRPBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组绑定/增加CG组绑定关系（ADD CGGRPBINDING）_09896884.md)
    > - [**ADD SGWSEGGCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW IMSI_MSISDN号段组计费方式/增加SGW IMSI_MSISDN Group Charge Method（ADD SGWSEGGCHGMETH）_09896995.md)

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SUBSCRIBERIDSEGGRP** | IMSI/MSISDN/IMEISV号段组名称（SEGGROUPNAME） | testmsisdngr1 | 本端规划 | 配置IMSI/MSISDN/IMEISV号码段组。 |
  | **ADD SUBSCRIBERIDSEGGRP** | IMSI/MSISDN/IMEISV号段名称（SEGMENTNAME） | testmsisdn1 | 已配置数据中获取 | 配置IMSI/MSISDN/IMEISV号码段组。 |
  | **ADD SUBSCRIBERIDSEGGRP** | 号段类型（SEGMENTTYPE） | IMSIMSISDN | 本端规划 | 配置IMSI/MSISDN/IMEISV号码段组。 |
- 任务示例脚本（该命令行）：
  `ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr1", SEGMENTNAME="testmsisdn1", SEGMENTTYPE=IMSIMSISDN;`
- 操作步骤上下文（±2 行原文）：
  L76:
    >       **ADD IMSIMSISDNSEG**
    >     b. 配置IMSI/MSISDN/IMEISV号码段组。
    >       **ADD SUBSCRIBERIDSEGGRP**
    >     c. 设置SGW-C基于号段组的计费方式。
    >       **ADD SGWSEGGCHGMETH**
  L128:
    > 
    > ```
    > ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr1", SEGMENTNAME="testmsisdn1", SEGMENTTYPE=IMSIMSISDN;
    > ```
    > 

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L48:
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD VIRTUALAPNRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/虚拟APN映射策略/增加虚拟APN映射策略配置（ADD VIRTUALAPNRULE）_09652380.md)
    > 

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L48:
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD VIRTUALAPNRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/虚拟APN映射策略/增加虚拟APN映射策略配置（ADD VIRTUALAPNRULE）_09652380.md)
    > - **[DSP SMPDPNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文数/查询会话管理的PDP上下文数（DSP SMPDPNUM）_09653799.md)**

**md：`WSFD-109001/配置OCS负荷分担_95923468.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SUBSCRIBERIDSEGGRP** | IMSI/MSISDN/IMEISV号段组名称（SEGGROUPNAME） | testmsisdngr1<br>testmsisdngr2 | 本端规划 | 配置IMSIMSISDN号码段组。 |
  | **ADD SUBSCRIBERIDSEGGRP** | IMSI/MSISDN/IMEISV号段名称（SEGMENTNAME） | testmsisdn1<br>testmsisdn2 | 已配置数据中获取 | 配置IMSIMSISDN号码段组。 |
  | **ADD SUBSCRIBERIDSEGGRP** | 号段类型（SEGMENTTYPE） | IMSIMSISDN | 已配置数据中获取 | 配置IMSIMSISDN号码段组。 |
- 任务示例脚本（该命令行）：
  `ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr1", SEGMENTNAME="testmsisdn1", SEGMENTTYPE=IMSIMSISDN;`
  `ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr2", SEGMENTNAME="testmsisdn2", SEGMENTTYPE=IMSIMSISDN;`
- 操作步骤上下文（±2 行原文）：
  L84:
    >       **ADD IMSIMSISDNSEG**
    >     c. 配置IMSI及MSISDN号码段组。
    >       **ADD SUBSCRIBERIDSEGGRP**
    >     d. 配置OCS组。重复执行本步骤可增加多个OCS组信息。
    >       **ADD OCSGROUP**
  L237:
    >   ```
    >   ```
    >   ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr1", SEGMENTNAME="testmsisdn1", SEGMENTTYPE=IMSIMSISDN;
    >   ```
    >   ```
  L243:
    >   ```
    >   ```
    >   ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr2", SEGMENTNAME="testmsisdn2", SEGMENTTYPE=IMSIMSISDN;
    >   ```
    >   //基于用户号段将OCS info绑定到OCS group，这样同一OCS group的用户会基于用户号段进行负荷分担。

**md：`WSFD-109001/配置基于CC+用户号段选择OCS_95923602.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SUBSCRIBERIDSEGGRP** | IMSI/MSISDN/IMEISV号段组名称（SEGGROUPNAME） | testmsisdngr1<br>testmsisdngr2 | 本端规划 | 配置IMSIMSISDN号码段组。 |
  | **ADD SUBSCRIBERIDSEGGRP** | IMSI/MSISDN/IMEISV号段名称（SEGMENTNAME） | testmsisdn1<br>testmsisdn2 | 已配置数据中获取 | 配置IMSIMSISDN号码段组。 |
  | **ADD SUBSCRIBERIDSEGGRP** | 号段类型（SEGMENTTYPE） | IMSIMSISDN | 已配置数据中获取 | 配置IMSIMSISDN号码段组。 |
- 任务示例脚本（该命令行）：
  `ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr1", SEGMENTNAME="testmsisdn1", SEGMENTTYPE=IMSIMSISDN;`
  `ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr2", SEGMENTNAME="testmsisdn2", SEGMENTTYPE=IMSIMSISDN;`
- 操作步骤上下文（±2 行原文）：
  L76:
    >       **ADD IMSIMSISDNSEG**
    >     c. 配置IMSI及MSISDN号码段组。
    >       **ADD SUBSCRIBERIDSEGGRP**
    >     d. 配置OCS组。
    >       **ADD OCSGROUP**
  L148:
    >   ```
    >   ```
    >   ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr1", SEGMENTNAME="testmsisdn1", SEGMENTTYPE=IMSIMSISDN;
    >   ```
    >   ```
  L154:
    >   ```
    >   ```
    >   ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="testmsisdngr2", SEGMENTNAME="testmsisdn2", SEGMENTTYPE=IMSIMSISDN;
    >   ```
    >   //基于用户号段将OCS info绑定到OCS group，这样同一OCS group的用户会基于用户号段进行负荷分担。

## ④ 自动比对
- 命令真相参数（3）：['SEGGROUPNAME', 'SEGMENTNAME', 'SEGMENTTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 4, '已配置数据中获取': 5}（多值→atom 应考虑 decision_driven）
