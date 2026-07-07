# 命令证据包：SET STGTRIGGER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置融合计费消息缓存期间融合计费消息生成的trigger（SET STGTRIGGER）_34667406.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF**

该命令用于设置融合计费消息缓存期间融合计费消息生成的trigger。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TIMELIMIT | PDUTIMELIMIT | VOLUMELIMIT | PDUVOLUMELIMIT | RATCHG | SRVNDCHG | QOSCHG | ULCHG |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMM

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TIMELIMIT | 时间阈值 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGT | <br>- NONREPORT（不上报） |
| PDUTIMELIMIT | PDU时长阈值(分钟) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGT | 整数类型，取值范围是0~1440，单位是分钟。 |
| VOLUMELIMIT | 流量阈值 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGT | <br>- NONREPORT（不上报） |
| PDUVOLUMELIMIT | PDU流量阈值(MB) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGT | 整数类型，取值范围是0~2147483647，单位是兆字节。 |
| RATCHG | RAT更新 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGT | <br>- NONREPORT（不上报） |
| SRVNDCHG | 服务节点更新 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGT | <br>- NONREPORT（不上报） |
| QOSCHG | QoS更新 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGT | <br>- NONREPORT（不上报） |
| ULCHG | 用户位置更新 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGT | <br>- NONREPORT（不上报） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > - [**SET FAILHANDLING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)
    > - [**SET N40MSGSTG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md)
    > - [**SET STGTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置融合计费消息缓存期间融合计费消息生成的trigger（SET STGTRIGGER）_34667406.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0174013176)

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 数据规划表（该命令的参数行）：
  | **SET STGTRIGGER** | VOLUMELIMIT（流量阈值） | IMMEDIATE | 本端规划 | 融合计费消息缓存期间的trigger，全局配置。 |
  | **SET STGTRIGGER** | PDUVOLUMELIMIT（PDU流量阈值(MB)） | 500 | 本端规划 | 融合计费消息缓存期间的trigger，全局配置。 |
- 任务示例脚本（该命令行）：
  `SET STGTRIGGER: VOLUMELIMIT=IMMEDIATE, PDUVOLUMELIMIT=500;`
- 操作步骤上下文（±2 行原文）：
  L61:
    >   **SET N40MSGSTG**
    > - 配置计费消息缓存期间的trigger。
    >   **SET STGTRIGGER**
    > - 配置由SMF生成ChargingDataRef。
    >   **SET CNVRGDCHGPARA**
  L106:
    > 
    > ```
    > SET STGTRIGGER: VOLUMELIMIT=IMMEDIATE, PDUVOLUMELIMIT=500;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（8）：['PDUTIMELIMIT', 'PDUVOLUMELIMIT', 'QOSCHG', 'RATCHG', 'SRVNDCHG', 'TIMELIMIT', 'ULCHG', 'VOLUMELIMIT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 2}（多值→atom 应考虑 decision_driven）
