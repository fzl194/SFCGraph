# 命令证据包：ADD SELCHFGBIMSISEG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/增加IMSI号段与CHF组的绑定关系（ADD SELCHFGBIMSISEG）_05630193.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF、GGSN**

该命令用于增加IMSI号段与CHF组的绑定关系。SMF选择NCG/CHF时，可基于指定的IMSI号段选择CHF组，将不同IMSI号段的用户的计费信息送到不同NCG/CHF组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令仅支持本地配置SMF选择CHF组场景。
- SMF选择CHF的优先级从高到低依次是：基于IMSI选择CHF > 基于IMSI号段选择CHF > 基于PCF下发的信息选择CHF > 基于从UDM获取的签约CC选择CHF > 基于标准化服务发现选择CHF > 基于SMF本地配置的CC选择CHF。

- 最多可输入1024条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SEGSTART | 号段起始字符串 | local_planned | required | 无 | 字符串类型，输入长度范围是5~15。号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进 |
| SEGEND | 号段结束字符串 | local_planned | required | 无 | 字符串类型，输入长度范围是5~15。号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进 |
| PRIMARYCHFGRP | 主CHF组 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~63。 |
| SECONDARYCHFGRP | 备CHF组 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/配置CHF选择方式_92091086.md`**
- 数据规划表（该命令的参数行）：
  | ****ADD SELCHFGBIMSISEG**** | 号段起始字符串（SEGSTART） | 12345678901 | 本端规划 | 用于设置绑定的IMSI号段的起始字符串。 |
  | ****ADD SELCHFGBIMSISEG**** | 号段结束字符串（SEGEND） | 12345678905 | 本端规划 | 用于设置绑定的IMSI号段的结束字符串。 |
  | ****ADD SELCHFGBIMSISEG**** | 主CHF组（PRIMARYCHFGRP） | ChfGroup1 | 主CHF组 | 主CHF组，使用<br>**ADD TNFGRP**<br>命令配置生成。 |
  | ****ADD SELCHFGBIMSISEG**** | 备CHF组（SECONDARYCHFGRP） | ChfGroup2 | 全网规划 | 备CHF组，使用<br>**ADD TNFGRP**<br>命令配置生成。 |
- 任务示例脚本（该命令行）：
  `ADD SELCHFGBIMSISEG:SEGSTART="12345678901",SEGEND="12345678905",PRIMARYCHFGRP="ChfGroup1",SECONDARYCHFGRP="ChfGroup2";`
- 操作步骤上下文（±2 行原文）：
  L66:
    >   **ADD SELCHFGBYIMSI**
    > - 配置基于IMSI号段选择CHF。针对现网存在多个CHF主备组，为了避免CHF之间业务不均衡，通过将不同IMSI号段范围和CHF主备组的绑定将用户分流到不同CHF。
    >   ****ADD SELCHFGBIMSISEG****
    > - 配置基于PCF下发的FQDN查询CHF。
    >     1. 进入 “MML命令行-UNC” 窗口。
  L148:
    > ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;
    > ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;
    > ADD SELCHFGBIMSISEG:SEGSTART="12345678901",SEGEND="12345678905",PRIMARYCHFGRP="ChfGroup1",SECONDARYCHFGRP="ChfGroup2";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（4）：['PRIMARYCHFGRP', 'SECONDARYCHFGRP', 'SEGEND', 'SEGSTART']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 2, '主CHF组': 1, '全网规划': 1}（多值→atom 应考虑 decision_driven）
