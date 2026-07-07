# 命令证据包：ADD CGGRPBINDING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组绑定/增加CG组绑定关系（ADD CGGRPBINDING）_09896884.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来增加离线计费模板和CG组绑定关系。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为2000。
- 该命令引用了IMSI/MSISDN号段，可能导致匹配不到号段，在全局范围内选择CG发送话单。
- 一个离线模板下最大可配置32个CG组。
- 一个离线模板下未配置IMSI/MSISDN号段组的CG组最多只能配置一个。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| OFCTEMPLATENAME | 离线计费模板名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| CGGRPID | CG组ID | local_planned | required | 无 | 整数类型，取值范围为1～32。 |
| SEGGROUPNAME | Imsi/Msisdn号码段组名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格。 |
| IMSIPRIORITY | Imsi/Msisdn号码段组优先级 | local_planned | optional | 无 | 整数类型，取值范围为1～65535。值越小优先级越高，优先级唯一。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD CGGRPBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组绑定/增加CG组绑定关系（ADD CGGRPBINDING）_09896884.md)
    > - [**ADD SGWSEGGCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW IMSI_MSISDN号段组计费方式/增加SGW IMSI_MSISDN Group Charge Method（ADD SGWSEGGCHGMETH）_09896995.md)
    > - [**ADD GLBOFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/全局离线计费模板/增加全局离线计费模板（ADD GLBOFCTEMPLATE）_09896916.md)

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 操作步骤上下文（±2 行原文）：
  L88:
    >       **ADD CGBINDING**
    >     e. **可选：**配置CG组绑定关系。
    >       **ADD CGGRPBINDING**
    >     f. 配置CG的负荷分担算法。
    >       **SET CDRTRANSFER**

## ④ 自动比对
- 命令真相参数（4）：['CGGRPID', 'IMSIPRIORITY', 'OFCTEMPLATENAME', 'SEGGROUPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
