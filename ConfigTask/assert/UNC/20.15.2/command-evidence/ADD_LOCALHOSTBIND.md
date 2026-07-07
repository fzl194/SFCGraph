# 命令证据包：ADD LOCALHOSTBIND
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组绑定/增加Diameter本端主机与Diameter本端主机组的关联关系（ADD LOCALHOSTBIND）_17057495.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用于添加指定的Diameter本端主机到本端主机分组中。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 单个Diameter本端主机分组内最多可以有64个本端主机。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| LOCGRPNAME | Diameter本端信息组名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| LOCHOSTNAME | Diameter本端主机名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOCALHOSTBIND**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组绑定/增加Diameter本端主机与Diameter本端主机组的关联关系（ADD LOCALHOSTBIND）_17057495.md) | Diameter本端信息组名（LOCGRPNAME） | pgwc_host_group_01<br>pgwc_host_group_02 | 已配置数据中获取 | 将Diameter本端主机添加到Diameter本端主机组中。 |
  | [**ADD LOCALHOSTBIND**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组绑定/增加Diameter本端主机与Diameter本端主机组的关联关系（ADD LOCALHOSTBIND）_17057495.md) | Diameter本端主机名（LOCHOSTNAME） | pgwc_1<br>pgwc_2 | 已配置数据中获取 | 将Diameter本端主机添加到Diameter本端主机组中。 |
- 任务示例脚本（该命令行）：
  `ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_01", LOCHOSTNAME="pgwc_1";`
  `ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_02", LOCHOSTNAME="pgwc_2";`
- 操作步骤上下文（±2 行原文）：
  L155:
    >   [**ADD LOCALHOSTGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组/增加Diameter本端主机组（ADD LOCALHOSTGRP）_16858413.md)
    > 11. 配置Diameter本端主机与Diameter本端主机组的关联关系。
    >   [**ADD LOCALHOSTBIND**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组绑定/增加Diameter本端主机与Diameter本端主机组的关联关系（ADD LOCALHOSTBIND）_17057495.md)
    > 12. 配置UPF组。
    >   [**ADD GXUPFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/UPF管理/Gx UPF组/增加Gx UPF组（ADD GXUPFGROUP）_16858407.md)
  L325:
    >   ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_01";
    >   ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_02";
    >   ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_01", LOCHOSTNAME="pgwc_1";
    >   ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_02", LOCHOSTNAME="pgwc_2";
    >   ADD GXUPFGROUP: UPFGRPNAME="upfgrp_01";
  L326:
    >   ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_02";
    >   ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_01", LOCHOSTNAME="pgwc_1";
    >   ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_02", LOCHOSTNAME="pgwc_2";
    >   ADD GXUPFGROUP: UPFGRPNAME="upfgrp_01";
    >   ADD GXUPFGROUP: UPFGRPNAME="upfgrp_02";

## ④ 自动比对
- 命令真相参数（2）：['LOCGRPNAME', 'LOCHOSTNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 2}（多值→atom 应考虑 decision_driven）
