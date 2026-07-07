# 命令证据包：ADD SGWSEGGCHGMETH
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW IMSI_MSISDN号段组计费方式/增加SGW IMSI_MSISDN Group Charge Method（ADD SGWSEGGCHGMETH）_09896995.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C**

该命令用于设置SGW基于号段组的计费方式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SEGGROUPNAME | IMSI/MSISDN号段组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格。 |
| PRIORITY | IMSI/MSISDN号段组优先级 | local_planned | required | 无 | 整数类型，取值范围为1～65535。值越小优先级越高，优先级唯一。 |
| OFFLINEFLAG | IMSI/MSISDN号段组离线计费开关 | local_planned | required | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L29:
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD CGGRPBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组绑定/增加CG组绑定关系（ADD CGGRPBINDING）_09896884.md)
    > - [**ADD SGWSEGGCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW IMSI_MSISDN号段组计费方式/增加SGW IMSI_MSISDN Group Charge Method（ADD SGWSEGGCHGMETH）_09896995.md)
    > - [**ADD GLBOFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/全局离线计费模板/增加全局离线计费模板（ADD GLBOFCTEMPLATE）_09896916.md)
    > - [**ADD FESTIVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SGWSEGGCHGMETH** | IMSI/MSISDN号段组名称（SEGGROUPNAME） | testmsisdngr1 | 已配置数据中获取 | 设置SGW-C基于号段组的计费方式。 |
  | **ADD SGWSEGGCHGMETH** | IMSI/MSISDN号段组优先级（PRIORITY） | 2 | 本端规划 | 设置SGW-C基于号段组的计费方式。 |
  | **ADD SGWSEGGCHGMETH** | IMSI/MSISDN号段组离线计费开关（OFFLINEFLAG） | ENABLE | 本端规划 | 设置SGW-C基于号段组的计费方式。 |
- 任务示例脚本（该命令行）：
  `ADD SGWSEGGCHGMETH:SEGGROUPNAME="testmsisdngr1", PRIORITY=2, OFFLINEFLAG=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L78:
    >       **ADD SUBSCRIBERIDSEGGRP**
    >     c. 设置SGW-C基于号段组的计费方式。
    >       **ADD SGWSEGGCHGMETH**
    > 5. **可选** ：配置SP合一用户产生SGW话单。
    >   **SET OFCCDRPARA**
  L132:
    > 
    > ```
    > ADD SGWSEGGCHGMETH:SEGGROUPNAME="testmsisdngr1", PRIORITY=2, OFFLINEFLAG=ENABLE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（3）：['OFFLINEFLAG', 'PRIORITY', 'SEGGROUPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '本端规划': 2}（多值→atom 应考虑 decision_driven）
