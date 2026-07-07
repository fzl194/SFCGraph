# 命令证据包：ADD CHGIMSICFG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用于配置基于 “IMSI前缀” 、 “APNNI” 、 “用户拜访类型” 和 “计费属性” 的计费配置信息，可以用该命令根据 “IMSI前缀” 、 “APNNI” 、 “用户拜访属性” 和 “计费属性” 配置生成话单的触发条件。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效，但该配置只对之后激活的用户有效。
- 此表最大记录数为2048。
- 当[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令的“PLMN ID控制策略（PLMNCTRL）”取值为“LOCINFO（位置信息）中的PLMN ID”时，相应选择[**ADD CHGPLMNCFG**](../PLMN计费配置/

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 | 整网规划 | required | 无 | <br>- “ALL_USER（所有用户）” |
| IMSIPRE | IMSI前缀 | 整网规划 | conditional | 无 | 5～15位十进制字符串 |
| VISITTYPE | 拜访类型 | 整网规划 | optional | <br>“ROAMING（使用归属地GGSN的漫游用户）&VISITING（使用 | <br>- “ROAMING（使用归属地GGSN的漫游用户）”：表示使用归属地GGSN的漫游用户。 |
| APNNI | APNNI | 整网规划 | required | 无 | 1～62位字符串 |
| CC | 计费属性 | 整网规划 | optional | HOT_BILLING(实时计费)&FLAT_RATE(包月制)&PREPAID | <br>- HOT_BILLING(实时计费) |
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
  | 支持<br>[**ADD CHGIMSICFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)<br>控制S-CDR话单生成的配置命令个数 | 2,048 |

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)
    > - [**LST CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/查询计费属性参数(LST CHGCHAR)_72225049.md)
    > - [**ADD CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)
    > - [**MOD CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/修改IMSI计费配置(MOD CHGIMSICFG)_26305200.md)
    > - [**RMV CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/删除IMSI计费配置(RMV CHGIMSICFG)_72225065.md)

**md：`WSFD-011201/离线计费话单（SGSN）_02556787.md`**
- 操作步骤上下文（±2 行原文）：
  L208:
    > 
    > - 基于PLMN和APN NI共同定制的S-CDR话单生成策略（通过命令**ADD CHGPLMNCFG**配置）。
    > - 基于IMSI前缀、APN NI、拜访类型、计费属性共同定制S-CDR话单生成策略（通过命令**ADD CHGIMSICFG**配置）。
    > - 全局S-CDR话单生成策略，即基于计费属性定制生成S-CDR话单的策略（通过命令**SET CHGCHAR**配置）。计费属性及计费属性选择机制详见：[计费属性](#ZH-CN_TOPIC_0302556787__section1423991923213)和[计费属性选择机制](#ZH-CN_TOPIC_0302556787__section846162403217)
    > 
  L230:
    > 1. 通过**SET CHGPLMNCHAR**完成全局配置策略。**SET CHGPLMNCHAR**:PLMN=VPLMN, SP=YES;
    > 2. 通过**SET CHGCDR**设置计费CDR参数。**SET CHGCDR**:PLMNCTRL=IMSI;
    > 3. 通过 **ADD CHGIMSICFG** 抑制外网某号段(12303前缀)且使用特定APN NI（huawei.com）的漫游用户生成S-CDR话单。
    >   **ADD CHGIMSICFG** :SUBRANGE=IMSI_PREFIX,IMSIPRE="12303",VISITTYPE=ROAMING-1,APNNI="huawei.com",SP=NO;
    > 
  L231:
    > 2. 通过**SET CHGCDR**设置计费CDR参数。**SET CHGCDR**:PLMNCTRL=IMSI;
    > 3. 通过 **ADD CHGIMSICFG** 抑制外网某号段(12303前缀)且使用特定APN NI（huawei.com）的漫游用户生成S-CDR话单。
    >   **ADD CHGIMSICFG** :SUBRANGE=IMSI_PREFIX,IMSIPRE="12303",VISITTYPE=ROAMING-1,APNNI="huawei.com",SP=NO;
    > 
    > > **说明**

**md：`WSFD-011201/配置离线计费参数（SGSN）_01731207.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHGIMSICFG** | 用户范围（SUBRANGE） | IMSI_PREFIX | 全网规划 | 抑制特定用户的S-CDR话单生成。 |
  | **ADD CHGIMSICFG** | IMSI前缀（IMSIPRE） | 12303 | 全网规划 | 抑制特定用户的S-CDR话单生成。 |
  | **ADD CHGIMSICFG** | 拜访类型 （VISITTYPE） | ROAMING-1 | 全网规划 | 抑制特定用户的S-CDR话单生成。 |
  | **ADD CHGIMSICFG** | APNNI（APNNI） | huawei.com | 全网规划 | 抑制特定用户的S-CDR话单生成。 |
  | **ADD CHGIMSICFG** | 计费属性（CC） | NORMAL_BILLING-1 | 全网规划 | 抑制特定用户的S-CDR话单生成。 |
  | **ADD CHGIMSICFG** | 生成S-CDR（SP） | NO | 全网规划 | 抑制特定用户的S-CDR话单生成。 |
- 任务示例脚本（该命令行）：
  `ADD CHGIMSICFG: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", VISITTYPE=ROAMING-1, APNNI="huawei.com", CC=NORMAL_BILLING-1, SP=NO;`
- 操作步骤上下文（±2 行原文）：
  L61:
    >   **SET CHGPLMNCHAR**
    > 5. 基于IMSI前缀、APN NI、漫游属性、计费属性共同配置生成S-CDR策略。
    >   **ADD CHGIMSICFG**
    >   > **说明**
    >   > - **SET CHGCDR**中的“PLMNCTRL”参数用于控制PLMN ID的获取来源。当PLMNCTRL=IMSI中的PLMNID，则话单生成策略为基于IMSI前缀、APN NI、拜访类型和计费属性共同配置的S-CDR话单生成策略；当PLMNCTRL=LOCINFO中的PLMNID，则话单生成策略为基于PLMN和APN NI共同配置的S-CDR话单生成策略。
  L104:
    >   > **说明**
    >   > - 如果**SET CHGPLMNCHAR**命令配置了禁止生成某种话单，则无论命令**SET CHGCHAR**配置何种类型的值，都不生成话单。
    >   > - 如果**SET CHGPLMNCHAR**命令配置了允许生成某种话单，则用户是否生成话单将由命令**ADD CHGIMSICFG**、**ADD CHGPLMNCFG**和**SET CHGCHAR**中的配置决定。
    > 
    > 可选：激活话单传输功能，具体内容请参考 **《UNC产品手册》：UNC初始配置与调测->2/3/4/5G融合组网对接配置->配置SGSN->配置到CG的数据。**
  L119:
    > 
    > ```
    > ADD CHGIMSICFG: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", VISITTYPE=ROAMING-1, APNNI="huawei.com", CC=NORMAL_BILLING-1, SP=NO;
    > ```

## ④ 自动比对
- 命令真相参数（13）：['APNNI', 'CC', 'IMSIPRE', 'SCCL', 'SCCP', 'SLCP', 'SP', 'SPL', 'SPP', 'SUBRANGE', 'SVL', 'SVP', 'VISITTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 6}（多值→atom 应考虑 decision_driven）
