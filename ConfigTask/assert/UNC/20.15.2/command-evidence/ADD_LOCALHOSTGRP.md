# 命令证据包：ADD LOCALHOSTGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组/增加Diameter本端主机组（ADD LOCALHOSTGRP）_16858413.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于添加Diameter本端主机组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| LOCGRPNAME | Diameter本端信息组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOCALHOSTGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组/增加Diameter本端主机组（ADD LOCALHOSTGRP）_16858413.md) | Diameter本端信息组名称（LOCGRPNAME） | pgwc_host_group_01<br>pgwc_host_group_02 | 本端规划 | Diameter本端主机组。 |
- 任务示例脚本（该命令行）：
  `ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_01";`
  `ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_02";`
- 操作步骤上下文（±2 行原文）：
  L153:
    >   **同一PGW-C对接多个PGW-U，且不同PGW-U下的用户IP存在相同时，必须执行 [步骤 10](#ZH-CN_OPI_0230805096__step38911553714) ~ [步骤 16](#ZH-CN_OPI_0230805096__step3536110122512) ；IP地址不同时，可不配置 [步骤 10](#ZH-CN_OPI_0230805096__step38911553714) ~ [步骤 16](#ZH-CN_OPI_0230805096__step3536110122512) 。**
    > 10. 配置Diameter本端主机组。
    >   [**ADD LOCALHOSTGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组/增加Diameter本端主机组（ADD LOCALHOSTGRP）_16858413.md)
    > 11. 配置Diameter本端主机与Diameter本端主机组的关联关系。
    >   [**ADD LOCALHOSTBIND**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diamter本端主机组绑定/增加Diameter本端主机与Diameter本端主机组的关联关系（ADD LOCALHOSTBIND）_17057495.md)
  L323:
    >   ```
    >   ```
    >   ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_01";
    >   ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_02";
    >   ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_01", LOCHOSTNAME="pgwc_1";
  L324:
    >   ```
    >   ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_01";
    >   ADD LOCALHOSTGRP: LOCGRPNAME="pgwc_host_group_02";
    >   ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_01", LOCHOSTNAME="pgwc_1";
    >   ADD LOCALHOSTBIND: LOCGRPNAME="pgwc_host_group_02", LOCHOSTNAME="pgwc_2";

## ④ 自动比对
- 命令真相参数（1）：['LOCGRPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1}（多值→atom 应考虑 decision_driven）
