# 命令证据包：ADD UPFGBINDLOCG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/关联UPF组与Diameter本端主机组的关联关系/增加UPF组与Diameter本端主机组的关联关系（ADD UPFGBINDLOCG）_29660172.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用于添加指定的UPF组与指定的Diameter本端主机组的绑定关系。在用户根据PCRF或者DRA的相关配置选择对端主机后，可以根据此配置选择用户使用的本端主机。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为3000。
- 单个UPF组与Diameter本端主机组的绑定关系组内最多可以有64组绑定关系。
- 在同一个绑定关系组内，UPF组不允许重复。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| UPFGRPNAME | Gx UPF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、 |
| DIAMLOCGRPNAME | Diameter本端信息组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| PRIORITY | 优先级 | local_planned | required | 无 | 整数类型，取值范围为1～127。值越小优先级越高。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPFGBINDLOCG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/关联UPF组与Diameter本端主机组的关联关系/增加UPF组与Diameter本端主机组的关联关系（ADD UPFGBINDLOCG）_29660172.md) | UPF组与Diameter本端主机组的绑定关系组名称（UPFGLOCGBNDGNAME） | test | 已配置数据中获取 | 同一PGW-C对接多个PGW-U，不同PGW-U下的用户IP存在相同或重叠时，则同时满足上述2个条件的PGW-U对应的PGW-U组必须绑定不同的Diameter本端主机组。<br>例如，upf1和upf2满足上述条件，则upf1和upf2对应的Diameter本端主机名必须不同。 |
  | [**ADD UPFGBINDLOCG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/关联UPF组与Diameter本端主机组的关联关系/增加UPF组与Diameter本端主机组的关联关系（ADD UPFGBINDLOCG）_29660172.md) | Gx UPF组名称（UPFGRPNAME） | upfgrp_01<br>upfgrp_02 | 已配置数据中获取 | 同一PGW-C对接多个PGW-U，不同PGW-U下的用户IP存在相同或重叠时，则同时满足上述2个条件的PGW-U对应的PGW-U组必须绑定不同的Diameter本端主机组。<br>例如，upf1和upf2满足上述条件，则upf1和upf2对应的Diameter本端主机名必须不同。 |
  | [**ADD UPFGBINDLOCG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/关联UPF组与Diameter本端主机组的关联关系/增加UPF组与Diameter本端主机组的关联关系（ADD UPFGBINDLOCG）_29660172.md) | Diameter本端信息组名称（DIAMLOCGRPNAME） | pgwc_host_group_01<br>pgwc_host_group_02 | 已配置数据中获取 | 同一PGW-C对接多个PGW-U，不同PGW-U下的用户IP存在相同或重叠时，则同时满足上述2个条件的PGW-U对应的PGW-U组必须绑定不同的Diameter本端主机组。<br>例如，upf1和upf2满足上述条件，则upf1和upf2对应的Diameter本端主机名必须不同。 |
  | [**ADD UPFGBINDLOCG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/关联UPF组与Diameter本端主机组的关联关系/增加UPF组与Diameter本端主机组的关联关系（ADD UPFGBINDLOCG）_29660172.md) | 优先级（PRIORITY） | 10<br>15 | 本端规划 | 值越小，优先级越高。 |
- 任务示例脚本（该命令行）：
  `ADD UPFGBINDLOCG: UPFGLOCGBNDGNAME="test", UPFGRPNAME="upfgrp_01", DIAMLOCGRPNAME="pgwc_host_group_01", PRIORITY=10;`
  `ADD UPFGBINDLOCG: UPFGLOCGBNDGNAME="test", UPFGRPNAME="upfgrp_02", DIAMLOCGRPNAME="pgwc_host_group_02", PRIORITY=15;`
- 操作步骤上下文（±2 行原文）：
  L163:
    >   [**ADD UPFGLOCGBNDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/UPF组与Diam本端主机组的绑定关系组/增加UPF组与Diameter本端主机组的绑定关系组（ADD UPFGLOCGBNDGRP）_29420948.md)
    > 15. 配置UPF组与Diameter本端主机组的绑定关系。
    >   [**ADD UPFGBINDLOCG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/关联UPF组与Diameter本端主机组的关联关系/增加UPF组与Diameter本端主机组的关联关系（ADD UPFGBINDLOCG）_29660172.md)
    > 16. 设置PCC本端主机名选择模式。
    >     - 基于APN设置PCC本端主机名选择模式。
  L332:
    >   ADD UPFBINDGXUPFGRP: UPFGRPNAME="upfgrp_02", UPFINSTANCEID="upf_instance_02";
    >   ADD UPFGLOCGBNDGRP: UPFGLOCGBNDGNAME="test";
    >   ADD UPFGBINDLOCG: UPFGLOCGBNDGNAME="test", UPFGRPNAME="upfgrp_01", DIAMLOCGRPNAME="pgwc_host_group_01", PRIORITY=10;
    >   ADD UPFGBINDLOCG: UPFGLOCGBNDGNAME="test", UPFGRPNAME="upfgrp_02", DIAMLOCGRPNAME="pgwc_host_group_02", PRIORITY=15;
    >   ```
  L333:
    >   ADD UPFGLOCGBNDGRP: UPFGLOCGBNDGNAME="test";
    >   ADD UPFGBINDLOCG: UPFGLOCGBNDGNAME="test", UPFGRPNAME="upfgrp_01", DIAMLOCGRPNAME="pgwc_host_group_01", PRIORITY=10;
    >   ADD UPFGBINDLOCG: UPFGLOCGBNDGNAME="test", UPFGRPNAME="upfgrp_02", DIAMLOCGRPNAME="pgwc_host_group_02", PRIORITY=15;
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（4）：['DIAMLOCGRPNAME', 'PRIORITY', 'UPFGLOCGBNDGNAME', 'UPFGRPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 3, '本端规划': 1}（多值→atom 应考虑 decision_driven）
