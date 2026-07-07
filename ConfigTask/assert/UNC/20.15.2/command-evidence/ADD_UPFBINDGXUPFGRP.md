# 命令证据包：ADD UPFBINDGXUPFGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/UPF管理/关联UPF与Gx UPF组/增加UPF与Gx UPF组的关联关系（ADD UPFBINDGXUPFGRP）_29660166.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用于添加指定的UPF到Gx UPF组中。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为300。
- 单个Gx UPF组最多可以有300个UPF。
- 同一UPF可以绑定到不同的Gx UPF组下。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| UPFGRPNAME | Gx UPF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～32。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、 |
| UPFINSTANCEID | UPF实例标识 | global_planned | required | 无 | 字符串类型，输入长度范围是1~36。UpfHostName参数必须满足以下约束规则：1.如果输入为u |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPFBINDGXUPFGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/UPF管理/关联UPF与Gx UPF组/增加UPF与Gx UPF组的关联关系（ADD UPFBINDGXUPFGRP）_29660166.md) | Gx UPF组名称（UPFGRPNAME） | upfgrp_01<br>upfgrp_02 | 已配置数据中获取 | 将对接的UPF主机名添加到UPF组中。 |
  | [**ADD UPFBINDGXUPFGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/UPF管理/关联UPF与Gx UPF组/增加UPF与Gx UPF组的关联关系（ADD UPFBINDGXUPFGRP）_29660166.md) | UPF实例标识（UPFINSTANCEID） | upf_instance_01<br>upf_instance_02 | 与对端协商 | 将对接的UPF主机名添加到UPF组中。 |
- 任务示例脚本（该命令行）：
  `ADD UPFBINDGXUPFGRP: UPFGRPNAME="upfgrp_01", UPFINSTANCEID="upf_instance_01";`
  `ADD UPFBINDGXUPFGRP: UPFGRPNAME="upfgrp_02", UPFINSTANCEID="upf_instance_02";`
- 操作步骤上下文（±2 行原文）：
  L159:
    >   [**ADD GXUPFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/UPF管理/Gx UPF组/增加Gx UPF组（ADD GXUPFGROUP）_16858407.md)
    > 13. 添加UPF到UPF组中。
    >   [**ADD UPFBINDGXUPFGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/UPF管理/关联UPF与Gx UPF组/增加UPF与Gx UPF组的关联关系（ADD UPFBINDGXUPFGRP）_29660166.md)
    > 14. 配置UPF组与Diameter本端主机组的绑定关系组。
    >   [**ADD UPFGLOCGBNDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/UPF组与Diam本端主机组的绑定关系组/增加UPF组与Diameter本端主机组的绑定关系组（ADD UPFGLOCGBNDGRP）_29420948.md)
  L329:
    >   ADD GXUPFGROUP: UPFGRPNAME="upfgrp_01";
    >   ADD GXUPFGROUP: UPFGRPNAME="upfgrp_02";
    >   ADD UPFBINDGXUPFGRP: UPFGRPNAME="upfgrp_01", UPFINSTANCEID="upf_instance_01";
    >   ADD UPFBINDGXUPFGRP: UPFGRPNAME="upfgrp_02", UPFINSTANCEID="upf_instance_02";
    >   ADD UPFGLOCGBNDGRP: UPFGLOCGBNDGNAME="test";
  L330:
    >   ADD GXUPFGROUP: UPFGRPNAME="upfgrp_02";
    >   ADD UPFBINDGXUPFGRP: UPFGRPNAME="upfgrp_01", UPFINSTANCEID="upf_instance_01";
    >   ADD UPFBINDGXUPFGRP: UPFGRPNAME="upfgrp_02", UPFINSTANCEID="upf_instance_02";
    >   ADD UPFGLOCGBNDGRP: UPFGLOCGBNDGNAME="test";
    >   ADD UPFGBINDLOCG: UPFGLOCGBNDGNAME="test", UPFGRPNAME="upfgrp_01", DIAMLOCGRPNAME="pgwc_host_group_01", PRIORITY=10;

## ④ 自动比对
- 命令真相参数（2）：['UPFGRPNAME', 'UPFINSTANCEID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '与对端协商': 1}（多值→atom 应考虑 decision_driven）
