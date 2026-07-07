# 命令证据包：SET CHGPLMNCHAR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用于设置某个PLMN类型的用户计费属性的参数配置。
**notes（规格/上限→应投影 atom rule）**：
- - 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 如果该命令配置了禁止生成某种话单，不管[**ADD CHGPLMNCFG**](../PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)、[**ADD CHGIMSICFG**](../IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.m

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PLMN | PLMN 类型 | 整网规划 | required |  | <br>- “HPLMN（本地 PLMN）”：表示本网用户。 |
| MP | 生成M-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| SP | 生成S-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| SMOP | 生成S-SMO-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| SMTP | 生成S-SMT-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| LCSMOP | 生成LCS-MO-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| LCSMTP | 生成LCS-MT-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| LCSNIP | 生成LCS-NI-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011001

**md：`WSFD-011001/WSFD-011001 漫游控制参考信息_70014634.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**MOD NGCONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/互联PLMN管理/修改5G Connect PLMN（MOD NGCONNECTPLMN）_09651707.md)
    > - [**LST NGCONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/互联PLMN管理/查询5G Connect PLMN（LST NGCONNECTPLMN）_09653790.md)
    > - [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md)
    > - [**LST CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/查询PLMN的计费属性参数(LST CHGPLMNCHAR)_72344991.md)
    > - [**SET NGMMPROCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM流程管理/5G移动性管理流程控制参数/设置5G移动性管理流程控制参数（SET NGMMPROCTRL）_09652386.md)

**md：`WSFD-011001/激活漫游控制特性(适用于SGSN_MME)_62950136.md`**
- 数据规划表（该命令的参数行）：
  | [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) | PLMN（PLMN类型） | VPLMN | 全网规划 | 漫游PLMN用户的计费属性参数 |
  | [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) | MP（生成M-CDR） | YES | 全网规划 | 漫游PLMN用户的计费属性参数 |
  | [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) | SP（生成S-CDR） | YES | 全网规划 | 漫游PLMN用户的计费属性参数 |
  | [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) | SMOP（生成S-SMO-CDR） | YES | 全网规划 | 漫游PLMN用户的计费属性参数 |
  | [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) | SMTP（生成S-SMT-CDR） | YES | 全网规划 | 漫游PLMN用户的计费属性参数 |
  | [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) | LCSMOP（生成LCS-MO-CDR） | YES | 全网规划 | 漫游PLMN用户的计费属性参数 |
  | [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) | LCSMTP（生成LCS-MT-CDR） | YES | 全网规划 | 漫游PLMN用户的计费属性参数 |
  | [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) | LCSNIP（生成LCS-NI-CDR） | YES | 全网规划 | 漫游PLMN用户的计费属性参数 |
- 任务示例脚本（该命令行）：
  `SET CHGPLMNCHAR: PLMN=VPLMN, LCSNIP=NO;`
- 操作步骤上下文（±2 行原文）：
  L63:
    >   [**ADD CONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)
    > 3. 设置漫游PLMN用户的计费属性参数。
    >   [**SET CHGPLMNCHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md)
    >   > **说明**
    >   > 参数 “PLMN” （PLMN类型）选择 “VPLMN” （拜访PLMN）。
  L84:
    > 
    > ```
    > SET CHGPLMNCHAR: PLMN=VPLMN, LCSNIP=NO;
    > ```

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**DSP CHGCDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/显示强制生成用户话单的结果信息(DSP CHGCDR)_26305188.md)
    > - [**TST CHGCDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/模拟SGSN话单(TST CHGCDR)_72344975.md)
    > - [**SET CHGPLMNCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md)
    > - [**LST CHGPLMNCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/查询PLMN的计费属性参数(LST CHGPLMNCHAR)_72344991.md)
    > - [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)

**md：`WSFD-011201/离线计费话单（SGSN）_02556787.md`**
- 操作步骤上下文（±2 行原文）：
  L223:
    > ![](离线计费话单（SGSN）_02556787.assets/zh-cn_image_0302611111_2.png)
    > 
    > - 当全局配置策略（通过命令**SET CHGPLMNCHAR**配置）中设置生成S-CDR时，以上三种S-CDR话单生成策略才会生效。
    > - **SET CHGCDR**中的PLMNCTRL参数用于控制PLMN ID的获取来源。当PLMN ID控制策略“PLMNCTRL”=IMSI，则话单生成策略为基于IMSI前缀、APN NI、拜访类型和计费属性共同配置的S-CDR话单生成策略；当PLMN ID控制策略“PLMNCTRL”=LOCINFO，则话单生成策略为基于PLMN和APN NI共同配置的S-CDR话单生成策略。
    > 
  L228:
    > 举例场景：外网PLMN生成S-CDR话单，仅抑制其中某号段且使用特定APN NI的漫游用户生成S-CDR话单的场景，主要步骤及涉及命令的关键参数配置如下：
    > 
    > 1. 通过**SET CHGPLMNCHAR**完成全局配置策略。**SET CHGPLMNCHAR**:PLMN=VPLMN, SP=YES;
    > 2. 通过**SET CHGCDR**设置计费CDR参数。**SET CHGCDR**:PLMNCTRL=IMSI;
    > 3. 通过 **ADD CHGIMSICFG** 抑制外网某号段(12303前缀)且使用特定APN NI（huawei.com）的漫游用户生成S-CDR话单。

**md：`WSFD-011201/配置离线计费参数（SGSN）_01731207.md`**
- 操作步骤上下文（±2 行原文）：
  L52:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 配置生成S-CDR话单。
    >   **SET CHGPLMNCHAR**
    > 3. 基于PLMN和APN NI共同配置生成S-CDR策略。
    >   **ADD CHGPLMNCFG**
  L59:
    > 
    > 4. 配置生成S-CDR话单。
    >   **SET CHGPLMNCHAR**
    > 5. 基于IMSI前缀、APN NI、漫游属性、计费属性共同配置生成S-CDR策略。
    >   **ADD CHGIMSICFG**
  L101:
    > 
    > 11. 配置特定PLMN的计费属性参数。
    >   **SET CHGPLMNCHAR**
    >   > **说明**
    >   > - 如果**SET CHGPLMNCHAR**命令配置了禁止生成某种话单，则无论命令**SET CHGCHAR**配置何种类型的值，都不生成话单。

## ④ 自动比对
- 命令真相参数（8）：['LCSMOP', 'LCSMTP', 'LCSNIP', 'MP', 'PLMN', 'SMOP', 'SMTP', 'SP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 8}（多值→atom 应考虑 decision_driven）
