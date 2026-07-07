# 命令证据包：SET CHGCDR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用于设置计费CDR参数的配置，包括各种话单内容配置选项、SGSN节点标识等。
**notes（规格/上限→应投影 atom rule）**：
- - 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 计费CDR参数配置由系统缺省增加。
- S-CDR中填写的计费属性按照如下的优先等级进行选择：
    1. 通过 [**LST CHGGNCCCFG**](../Gn接口计费属性选择策略配置/查询Gn接口计费属性选择策略(LST CHGGNCCCFG)_26305186.md) 查看按照用户的IMSI匹配上的 “SPEC

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| ML | M-CDR选项 | 整网规划 | optional |  | <br>- “SERVED_IMEI（SERVED_IMEI）”：手机用户的IMEI。 |
| SMOL | S-SMO-CDR选项 | 整网规划 | optional |  | <br>- “SERVED_IMEI（SERVED_IMEI）”：手机用户的IMEI。 |
| SMTL | S-SMT-CDR选项 | 整网规划 | optional |  | <br>- “SERVED_IMEI（SERVED_IMEI）”：手机用户的IMEI。 |
| SL | S-CDR选项 | 整网规划 | optional |  | <br>- “NETWORK_INITIATED_PDP（NETWORK_INITIATED_PDP |
| LCSMTL | LCS-MT-CDR选项 | 整网规划 | optional |  | <br>- “SERVED_MSISDN（SERVED_MSISDN）”：手机的MSISDN。 |
| LCSMOL | LCS-MO-CDR选项 | 整网规划 | optional |  | <br>- “SERVED_MSISDN(SERVED_MSISDN)”：手机的MSISDN。 |
| LCSNIL | LCS-NI-CDR选项 | 整网规划 | optional |  | <br>- “SGSN_ADDR(SGSN_ADDR)”：SGSN的IP地址。 |
| NODEID | SGSN节点标识 | 整网规划 | optional |  | 长度不超过19的字符串 |
| HCC | 本地用户缺省计费属性 | 整网规划 | optional |  | <br>- “NORMAL（普通计费）”：表示普通计费属性，按照此种方式计费的用户按照常规的方式支付 |
| VCC | 拜访用户缺省计费属性 | 整网规划 | optional |  | <br>- “NORMAL（普通计费）”：表示普通计费属性，按照此种方式计费的用户按照常规的方式支付 |
| RCC | 漫游用户缺省计费属性 | 整网规划 | optional |  | <br>- “NORMAL（普通计费）”：表示普通计费属性，按照此种方式计费的用户按照常规的方式支付 |
| VP | 缺省非本地用户类型 | 整网规划 | optional |  | <br>- “ROAMING（漫游用户）”：表示使用归属PLMN的GGSN的外网用户。 |
| LRSNP | 配置本地话单序列号 | 整网规划 | optional |  | <br>- “ABSENT（无）”：表示不生成。 |
| IGNOREFLG | 忽略签约计费属性 | 整网规划 | optional |  | <br>- “HOME_SUBSCRIBER（HOME_SUBSCRIBER）”：表示是否忽略本网用 |
| CRC | 话单关闭原因值 | 整网规划 | optional |  | <br>- “NORMAL（正常释放）”：表示话单关闭原因值为正常释放。 |
| PLMNCTRL | PLMN ID控制策略 | 整网规划 | optional |  | <br>- “LOCINFO（位置信息中的PLMN ID）” |
| EXTRANGE | PLMNCG范围扩展 | 整网规划 | optional |  | <br>- “YES（允许非PLMNCG）” |
| FRCGEN | 强制生成话单方式 | 整网规划 | optional |  | <br>- “SCDRONLY（只生成S-CDR）”：表示在特定时间点生成所有用户的S-CDR话单。 |
| FRCTIME | 强制生成话单时间 | 整网规划 | conditional |  | 00&00&00~23&59&59 |
| CRQOS | 保持请求QoS | 整网规划 | optional |  | <br>- “YES(是)”：表示保持Request QoS原始值。 |
| CDRPLMNSELECT | 话单填写PLMN ID选择策略 | 整网规划 | optional |  | <br>- “LOCINFO（位置信息中的PLMN ID）” |
| CGPLMNSELECT | 话单发送PLMN ID选择策略 | 整网规划 | optional |  | <br>- “LOCINFO（位置信息中的PLMN ID）” |
| NONSUPPUEPLMN | MOCN中Non-supporting UE的PLMN获取策略 | 整网规划 | optional |  | <br>- “COMMON_PLMN（公共PLMN）” |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-207001

**md：`WSFD-207001/激活网络共享（MOCN）_85152759.md`**
- 数据规划表（该命令的参数行）：
  | [**SET CHGCDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) | MOCN中Non-supporting UE的PLMN获取策略（NONSUPPUEPLMN） | SRV_PLMN | 全网规划 | 设置Non-supporting UE的PLMN获取策略。 |
- 任务示例脚本（该命令行）：
  `SET CHGCDR: NONSUPPUEPLMN=SRV_PLMN;`
- 操作步骤上下文（±2 行原文）：
  L77:
    >     a. 设置Non-supporting UE的PLMN获取策略。
    >           - 设置Gn接口上传输的或话单中使用的PLMN为Serving PLMN，然后执行 [b](#ZH-CN_OPI_0185152759__zh-cn_opi_0130429072_cmd297651773180641) 。
    >             [**SET CHGCDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)
    >           - 设置Gn接口上传输的或话单中使用的PLMN为COMMON PLMN。处理结束。
    >             [**SET CHGCDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)
  L79:
    >             [**SET CHGCDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)
    >           - 设置Gn接口上传输的或话单中使用的PLMN为COMMON PLMN。处理结束。
    >             [**SET CHGCDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)
    >     b. 为Non-supporting UE指定Serving PLMN。
    >       [**ADD HNOSRVPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络Serving PLMN管理/增加归属网络Serving PLMN信息(ADD HNOSRVPLMN)_72345655.md)
  L137:
    > 
    > ```
    > SET CHGCDR: NONSUPPUEPLMN=SRV_PLMN;
    > ```
    > 

**md：`WSFD-207001/特性概述_87065742.md`**
- 操作步骤上下文（±2 行原文）：
  L132:
    > - Non-supporting UE：Non-supporting UE不能解析广播系统信息中的网络共享信息，仅能获得Common PLMN。SGSN将Common PLMN作为Serving PLMN。
    > 
    > 如 [图3](#ZH-CN_CONCEPT_0187065742__zh-cn_concept_0130429052_fig_8) 所示，Operator A和Operator B共享RAN。RAN设置的Common PLMN为46123，和Operator B的PLMN不同，导致Billing Center B中存在无法识别的话单。 UNC 可以通过配置（ [**SET CHGCDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) 和 [**ADD HNOSRVPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络Serving PLMN管理/增加归属网络Serving PLMN信息(ADD HNOSRVPLMN)_72345655.md) ）将Common PLMN替换为配置的Serving PLMN填写入S-CDR/M-CDR话单中，解决此问题。
    > 
    > **图3** Common PLMN和Serving PLMN选择示意图

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**LST CHGGA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/查询计费Ga接口参数(LST CHGGA)_72225059.md)
    > - [**DSP CHGGA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/显示计费Ga接口参数状态(DSP CHGGA)_26305194.md)
    > - [**SET CHGCDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)
    > - [**LST CHGCDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/查询计费CDR参数（LST CHGCDR）_72225053.md)
    > - [**DSP CHGCDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/显示强制生成用户话单的结果信息(DSP CHGCDR)_26305188.md)

**md：`WSFD-011201/离线计费话单（SGSN）_02556787.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > #### [CDR内容的定制](#ZH-CN_TOPIC_0302556787)
    > 
    > SGSN可以对CDR的内容进行定制，CDR中可选字段的产生与否可以通过命令 **SET CHGCDR** 实现。以S-CDR为例， [表1](#ZH-CN_TOPIC_0302556787__zh-cn_concept_0130427386_tab4) 为R98、R99、R4、R5、R6，R7，R9七种协议类型的S-CDR话单结构。
    > 
    > *表1 R98、R99、R4、R5、R6，R7，R9七种协议类型的S-CDR话单结构*
  L224:
    > 
    > - 当全局配置策略（通过命令**SET CHGPLMNCHAR**配置）中设置生成S-CDR时，以上三种S-CDR话单生成策略才会生效。
    > - **SET CHGCDR**中的PLMNCTRL参数用于控制PLMN ID的获取来源。当PLMN ID控制策略“PLMNCTRL”=IMSI，则话单生成策略为基于IMSI前缀、APN NI、拜访类型和计费属性共同配置的S-CDR话单生成策略；当PLMN ID控制策略“PLMNCTRL”=LOCINFO，则话单生成策略为基于PLMN和APN NI共同配置的S-CDR话单生成策略。
    > 
    > 举例场景：外网PLMN生成S-CDR话单，仅抑制其中某号段且使用特定APN NI的漫游用户生成S-CDR话单的场景，主要步骤及涉及命令的关键参数配置如下：
  L229:
    > 
    > 1. 通过**SET CHGPLMNCHAR**完成全局配置策略。**SET CHGPLMNCHAR**:PLMN=VPLMN, SP=YES;
    > 2. 通过**SET CHGCDR**设置计费CDR参数。**SET CHGCDR**:PLMNCTRL=IMSI;
    > 3. 通过 **ADD CHGIMSICFG** 抑制外网某号段(12303前缀)且使用特定APN NI（huawei.com）的漫游用户生成S-CDR话单。
    >   **ADD CHGIMSICFG** :SUBRANGE=IMSI_PREFIX,IMSIPRE="12303",VISITTYPE=ROAMING-1,APNNI="huawei.com",SP=NO;

**md：`WSFD-011201/配置离线计费参数（SGSN）_01731207.md`**
- 操作步骤上下文（±2 行原文）：
  L63:
    >   **ADD CHGIMSICFG**
    >   > **说明**
    >   > - **SET CHGCDR**中的“PLMNCTRL”参数用于控制PLMN ID的获取来源。当PLMNCTRL=IMSI中的PLMNID，则话单生成策略为基于IMSI前缀、APN NI、拜访类型和计费属性共同配置的S-CDR话单生成策略；当PLMNCTRL=LOCINFO中的PLMNID，则话单生成策略为基于PLMN和APN NI共同配置的S-CDR话单生成策略。
    >   > - 基于IMSI前缀、APN和计费属性共同配置生成S-CDR话单策略默认优先级由高到低的顺序为：基于IMSI前缀和APN NI共同配置结合计费属性生成S-CDR话单策略、基于计费属性生成S-CDR话单策略。
    >   > - 基于PLMN和APN NI共同配置生成S-CDR话单策略默认优先级由高到低的顺序为：基于PLMN和APN NI共同配置生成S-CDR话单策略、基于计费属性S-CDR话单生成策略 。
  L70:
    > 
    > 6. 配置指定时间强制生成话单。
    >   **SET CHGCDR**
    > 
    > 可选：配置全局计费属性参数。
  L75:
    > 
    > 7. 配置全局计费属性参数。
    >   **SET CHGCDR**
    > 
    > 可选：配置特定计费属性的CDR参数。

**md：`WSFD-011201/配置话单可靠性保证（SGSN）_01731121.md`**
- 数据规划表（该命令的参数行）：
  | **SET CHGCDR** | 配置本地话单序列号（LRSNP） | PRESENT | 全网规划 | 本地话单序列号 |
- 任务示例脚本（该命令行）：
  `SET CHGCDR:LRSNP=PRESENT;`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 配置本地话单序列号。
    >   **SET CHGCDR**
    >   > **说明**
    >   > 参数 “LRSNP” （配置本地话单序列号）固定选择 “PRESENT” （有）。
  L55:
    > 
    > ```
    > SET CHGCDR:LRSNP=PRESENT;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（23）：['CDRPLMNSELECT', 'CGPLMNSELECT', 'CRC', 'CRQOS', 'EXTRANGE', 'FRCGEN', 'FRCTIME', 'HCC', 'IGNOREFLG', 'LCSMOL', 'LCSMTL', 'LCSNIL', 'LRSNP', 'ML', 'NODEID', 'NONSUPPUEPLMN', 'PLMNCTRL', 'RCC', 'SL', 'SMOL', 'SMTL', 'VCC', 'VP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 2}（多值→atom 应考虑 decision_driven）
