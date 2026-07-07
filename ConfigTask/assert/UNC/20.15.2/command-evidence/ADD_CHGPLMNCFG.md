# 命令证据包：ADD CHGPLMNCFG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用于根据PLMN配置话单生成策略。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效，但该配置只对配置生效之后激活的用户有效。
- 该表最大记录数为1500。
- 该命令和[**ADD CHGIMSICFG**](../IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)中各字段默认值都为无效值。若需要使用该命令或[**ADD CHGIMSICFG**](../IMSI计费配置/增加IMSI计费配置(ADD CH

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 | 整网规划 | required | 无 | <br>- “ALL_USER（所有用户）” |
| MCC | 移动国家码 | 整网规划 | conditional | 无 | 位数为3的十进制数字 |
| MNC | 移动网号 | 整网规划 | conditional | 无 | 位数为2或3的十进制数字 |
| APNNI | APNNI | 整网规划 | required | 无 | 1～62位字符串 |
| SP | 生成S-CDR | 整网规划 | optional | <br>“DFT(缺省策略)” | <br>- “NO(不生成)” |
| SPP | 周期生成S-CDR | 整网规划 | optional | <br>“DFT(缺省策略)” | <br>- “FORBID(不生成)”：表示不周期生成S-CDR。 |
| SPL | S-CDR生成周期（min） | 整网规划 | optional | 0min | 0min～1440min |
| SVP | 流量生成S-CDR | 整网规划 | optional | <br>“DFT(缺省策略)” | <br>- “NO(不生成)” |
| SVL | 生成S-CDR流量阈值（KB） | 整网规划 | optional | 0KB | 0KB～1000000KB |
| SCCP | 计费条件变更生成S-CDR | 整网规划 | optional | <br>“DFT(缺省策略)” | <br>- “NO(不生成)” |
| SCCL | 最大计费条件变更次数 | 整网规划 | optional | 0 | 0～10 |
| SLCP | 位置更新生成S-CDR | 整网规划 | optional | <br>“DFT(缺省策略)” | <br>- “NO(不生成)”：不会导致inter RAU SGSN新侧不创建话单，只是位置更新时不 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/特性概述_25745814.md`**
- 数据规划表（该命令的参数行）：
  | 支持<br>[**ADD CHGPLMNCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)<br>控制S-CDR话单生成的配置命令个数 | 1,500 |

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**RMV CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/删除IMSI计费配置(RMV CHGIMSICFG)_72225065.md)
    > - [**LST CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/查询IMSI计费配置(LST CHGIMSICFG)_72344987.md)
    > - [**ADD CHGPLMNCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)
    > - [**MOD CHGPLMNCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/修改PLMN计费配置(MOD CHGPLMNCFG)_72344993.md)
    > - [**RMV CHGPLMNCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/删除PLMN计费配置(RMV CHGPLMNCFG)_26305206.md)

**md：`WSFD-011201/离线计费话单（SGSN）_02556787.md`**
- 操作步骤上下文（±2 行原文）：
  L207:
    > UNC 提供了三种生成S-CDR话单策略，可针对不同的用户灵活定制S-CDR的生成周期、流量阈值等参数：
    > 
    > - 基于PLMN和APN NI共同定制的S-CDR话单生成策略（通过命令**ADD CHGPLMNCFG**配置）。
    > - 基于IMSI前缀、APN NI、拜访类型、计费属性共同定制S-CDR话单生成策略（通过命令**ADD CHGIMSICFG**配置）。
    > - 全局S-CDR话单生成策略，即基于计费属性定制生成S-CDR话单的策略（通过命令**SET CHGCHAR**配置）。计费属性及计费属性选择机制详见：[计费属性](#ZH-CN_TOPIC_0302556787__section1423991923213)和[计费属性选择机制](#ZH-CN_TOPIC_0302556787__section846162403217)

**md：`WSFD-011201/配置离线计费参数（SGSN）_01731207.md`**
- 操作步骤上下文（±2 行原文）：
  L54:
    >   **SET CHGPLMNCHAR**
    > 3. 基于PLMN和APN NI共同配置生成S-CDR策略。
    >   **ADD CHGPLMNCFG**
    > 
    > 可选：基于IMSI前缀、APN NI、漫游属性、计费属性来共同定制S-CDR话单生成策略。
  L104:
    >   > **说明**
    >   > - 如果**SET CHGPLMNCHAR**命令配置了禁止生成某种话单，则无论命令**SET CHGCHAR**配置何种类型的值，都不生成话单。
    >   > - 如果**SET CHGPLMNCHAR**命令配置了允许生成某种话单，则用户是否生成话单将由命令**ADD CHGIMSICFG**、**ADD CHGPLMNCFG**和**SET CHGCHAR**中的配置决定。
    > 
    > 可选：激活话单传输功能，具体内容请参考 **《UNC产品手册》：UNC初始配置与调测->2/3/4/5G融合组网对接配置->配置SGSN->配置到CG的数据。**

## ④ 自动比对
- 命令真相参数（12）：['APNNI', 'MCC', 'MNC', 'SCCL', 'SCCP', 'SLCP', 'SP', 'SPL', 'SPP', 'SUBRANGE', 'SVL', 'SVP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
