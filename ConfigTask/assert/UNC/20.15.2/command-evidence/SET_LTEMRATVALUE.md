# 命令证据包：SET LTEMRATVALUE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/LTE-M用户RAT值/设置LTE-M用户的RAT值（SET LTEMRATVALUE）_04284725.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SGW-C、SMF**

该命令用于设置终端通过LTE-M接入方式时UNC给周边网元发送消息时RAT信元中携带的值。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| OCS | CHF | CG | AAAACCT | AAAAUTH | PCRF | PCF | PGW | UPF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTE_M | LTE_M | LTE_M | LTE_M 

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| OCS | 和OCS交互使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |
| CHF | 和CHF交互使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |
| CG | 和CG交互使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |
| AAAACCT | 和AAA计费服务器交互使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |
| AAAAUTH | 和AAA鉴权服务器交互使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |
| PCRF | 和PCRF交互使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |
| PCF | 和PCF交互使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |
| PGW | UNC作为SGW-C发送给PGW-C时使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |
| UPF | 和UPF交互使用的RAT值 | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEM | <br>- EUTRAN（EUTRAN） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 操作步骤上下文（±2 行原文）：
  L177:
    >     - 对接PCRF/PCF不支持**EUTRAN-NB-IoT**类型时，“PCRF”/“PCF”设置为“EUTRAN”，PGW-C向PCRF/PCF发送NB-IoT用户的相关消息时，RAT信元值为“EUTRAN”。“PCRF”设置为“EUTRAN”时，还需要开启PCRF免升级License，详细操作请参见[激活PCRF免升级](../../../../NB-IoT业务功能/WSFD-215302 PCRF免升级/激活PCRF免升级_76026862.md)。
    > 18. **可选：**LTE-M用户接入场景，设置PGW-C向PCRF/PCF发送消息时的RAT信元值。
    >   [**SET LTEMRATVALUE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/LTE-M用户RAT值/设置LTE-M用户的RAT值（SET LTEMRATVALUE）_04284725.md) : PCRF=LTE_M, PCF=LTE_M;
    >     - 对接PCRF/PCF支持**LTE-M**类型时，“PCRF”/“PCF”设置为“LTE_M”，PGW-C向PCRF/PCF发送LTE-M用户的相关消息时，RAT信元值为“LTE-M”。系统初始值为“LTE_M”。
    >     - 对接PCRF/PCF不支持**LTE-M**类型时，“PCRF”/“PCF”设置为“EUTRAN”，PGW-C向PCRF/PCF发送LTE-M用户的相关消息时，RAT信元值为“EUTRAN”。

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L159:
    >       NB-IoT用户接入场景，还支持设置SMF向CHF/UPF等网元发送消息时的RAT信元值。
    >     9. （可选）LTE-M用户接入场景，设置SMF向PCF发送消息时的RAT信元值。
    >       [**SET LTEMRATVALUE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/LTE-M用户RAT值/设置LTE-M用户的RAT值（SET LTEMRATVALUE）_04284725.md) : PCF=LTE_M;
    >           - 对接PCF支持**LTE-M**类型时，“PCF”设置为“LTE_M”，SMF向PCF发送LTE-M用户的相关消息时，RAT信元值为“LTE-M”。系统初始值为“LTE_M”。
    >           - 对接PCF不支持**LTE-M**类型时，“PCF”设置为“EUTRAN”，SMF向PCF发送LTE-M用户的相关消息时，RAT信元值为“EUTRAN”。

## ④ 自动比对
- 命令真相参数（9）：['AAAACCT', 'AAAAUTH', 'CG', 'CHF', 'OCS', 'PCF', 'PCRF', 'PGW', 'UPF']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
