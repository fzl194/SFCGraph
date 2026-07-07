# 命令证据包：MOD CHGIMSICFG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/修改IMSI计费配置(MOD CHGIMSICFG)_26305200.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用于修改基于 “IMSI前缀” 的计费配置信息。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效，但该配置只对之后激活的用户有效。
- 当[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令的“PLMN ID控制策略（PLMNCTRL）”取值为“LOCINFO（位置信息）中的PLMN ID”时，相应选择[**ADD CHGPLMNCFG**](../PLMN计费配置/增加PLMN计费配置(ADD C

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 | 整网规划 | required | 无 | <br>- “ALL_USER（所有用户）” |
| IMSIPRE | IMSI前缀 | 整网规划 | conditional | 无 | 5～15位十进制字符串 |
| VISITTYPE | 拜访类型 | 整网规划 | optional | 无 | <br>- “ROAMING（使用归属地GGSN的漫游用户）” |
| APNNI | APNNI | 整网规划 | required | 无 | 最大长度为62个字符 |
| CC | 计费属性 | 整网规划 | optional | 无 | <br>- HOT_BILLING(实时计费) |
| SP | 生成S-CDR | 整网规划 | optional | 无 | <br>- “NO(不生成)” |
| SPP | 周期生成S-CDR | 整网规划 | optional | 无 | <br>- “FORBID(不生成)”：表示不周期生成S-CDR。 |
| SPL | S-CDR生成周期（min） | 整网规划 | optional | 无 | 0min～1440min |
| SVP | 流量生成S-CDR | 整网规划 | optional | 无 | <br>- “NO(不生成)” |
| SVL | 生成S-CDR流量阈值（KB） | 整网规划 | optional | 无 | 0KB～1000000KB |
| SCCP | 计费条件变更生成S-CDR | 整网规划 | optional | 无 | <br>- “NO(不生成)” |
| SCCL | 最大计费条件变更次数 | 整网规划 | optional | 无 | 0～10 |
| SLCP | 位置更新生成S-CDR | 整网规划 | optional | 无 | <br>- “NO(不生成)”：不会导致inter RAU SGSN新侧不创建话单，只是位置更新时不 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**LST CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/查询计费属性参数(LST CHGCHAR)_72225049.md)
    > - [**ADD CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)
    > - [**MOD CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/修改IMSI计费配置(MOD CHGIMSICFG)_26305200.md)
    > - [**RMV CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/删除IMSI计费配置(RMV CHGIMSICFG)_72225065.md)
    > - [**LST CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/查询IMSI计费配置(LST CHGIMSICFG)_72344987.md)

## ④ 自动比对
- 命令真相参数（13）：['APNNI', 'CC', 'IMSIPRE', 'SCCL', 'SCCP', 'SLCP', 'SP', 'SPL', 'SPP', 'SUBRANGE', 'SVL', 'SVP', 'VISITTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
