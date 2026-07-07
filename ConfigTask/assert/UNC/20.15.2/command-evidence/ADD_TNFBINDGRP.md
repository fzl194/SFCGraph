# 命令证据包：ADD TNFBINDGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/增加目标NF实例绑定组（ADD TNFBINDGRP）_09651533.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、NCG、SMSF**

该命令用于增加目标NF实例绑定目标NF组的配置。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入4096条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TNFGRPINDEX | 目标NF组索引 | local_planned | required | 无 | 整数类型，取值范围是0~511。 |
| TNFINSINDEX | 目标NF实例索引 | local_planned | required | 无 | 整数类型，取值范围是0~2047。 |
| PRIORITY | 优先级 | global_planned | optional | 10 | 整数类型，取值范围是1~255。值越小优先级越高。 |
| WEIGHT | 权重 | global_planned | optional | 无 | 整数类型，取值范围是1~65535。值越大表示权重越大。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD TNFINSIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/增加目标NF实例IP地址（ADD TNFINSIP）_09654443.md)
    > - [**ADD TNFGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/增加目标NF组（ADD TNFGRP）_09651791.md)
    > - [**ADD TNFBINDGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/增加目标NF实例绑定组（ADD TNFBINDGRP）_09651533.md)
    > - [**ADD SELECTCHFGBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/增加基于CC选择CHF处理（ADD SELECTCHFGBYCC）_09652118.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**

**md：`WSFD-011206/配置CHF选择方式_92091086.md`**
- 数据规划表（该命令的参数行）：
  | **ADD TNFBINDGRP** | 目标NF组索引（TNFGRPINDEX） | - 1<br>- 2 | 已配置数据中获取 | 将CHF实例绑定到CHF组上。 |
  | **ADD TNFBINDGRP** | 目标NF实例索引（TNFINSINDEX） | - 1<br>- 2 | 已配置数据中获取 | 将CHF实例绑定到CHF组上。 |
- 任务示例脚本（该命令行）：
  `ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;`
  `ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;`
  `ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;`
  `ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;`
  `ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;`
  `ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;`
  `ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;`
  `ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;`
- 操作步骤上下文（±2 行原文）：
  L84:
    >             **ADD TNFGRP**
    >           d. 将目标CHF绑定到CHF组。
    >             **ADD TNFBINDGRP**
    >     3. 配置基于CC选择CHF组。
    >       **ADD SELECTCHFGBYCC**
  L101:
    >             **ADD TNFGRP**
    >           d. 将目标CHF绑定到CHF组。
    >             **ADD TNFBINDGRP**
    >     2. 配置基于全局默认的CHF组选择CHF。
    >       **SET GLBDFTCHFGROUP**
  L132:
    > ADD TNFGRP: TNFGRPINDEX=1, TNFTYPE=CHF, TNFGRPNAME="ChfGroup1";
    > ADD TNFGRP: TNFGRPINDEX=2, TNFTYPE=CHF, TNFGRPNAME="ChfGroup2";
    > ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;
    > ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;
    > ADD SELCHFGBYIMSI: IMSI="123456789012345", PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";

## ④ 自动比对
- 命令真相参数（4）：['PRIORITY', 'TNFGRPINDEX', 'TNFINSINDEX', 'WEIGHT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 2}（多值→atom 应考虑 decision_driven）
