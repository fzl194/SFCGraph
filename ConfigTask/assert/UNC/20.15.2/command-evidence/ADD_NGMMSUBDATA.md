# 命令证据包：ADD NGMMSUBDATA
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md`
> 用该命令的特性数：5

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF**

该命令用于针对指定的用户（群）配置移动性管理相关参数，如移动性接入限制、RFSP索引等。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入1024条记录。
- AMF本地配置的接入和移动性签约数据的优先级高于用户签约。
- 通过本命令配置的多条记录存在用户（群）重叠的情况下，AMF以号段最长匹配的记录为准。故当为指定的用户（群）配置某个特定的签约数据时，本命令中其它的参数也需要一并配置，防止参数默认值未被修改而引起误用。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 | local_planned | required | 无 | <br>- “ALL_USER（所有用户）”：所有用户 |
| IMSIPRE | IMSI前缀 | global_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。 |
| IMSI | IMSI | global_planned | conditional | 无 | 字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。 |
| RATRESTRICT | RAT限制 | global_planned | optional | 无 | 该参数的默认值为“全部灰化”，即表示未生效。 |
| CORERESTRICT | 核心网类型限制 | global_planned | optional | 无 | 该参数的默认值为“全部灰化”，即表示未生效。 |
| RFSPINDEX | RFSP索引 | local_planned | optional | 0 | 整数类型，取值范围是0~256。 |
| NIM | 3GPP接入方式下的网络切片包含模式 | global_planned | optional | MODE_C | <br>- “MODE_A（网络切片包含模式A）”：网络切片包含模式A |
| DRX | 寻呼DRX | global_planned | optional | 0 | 整数类型，取值范围是0，32，64，128，256。其中0表示无效的寻呼DRX。 |
| RFSPPRI | RFSP优先级 | global_planned | optional | CFG_FIRST | <br>- “CFG_FIRST（配置优先）”：表示无论用户是否签约RFSP ID，均优先使用本命令 |
| UEAMBRULK | 上行UE AMBR (kbps) | global_planned | optional | 无 | 整数类型，取值范围是0~4000000000，单位是千比特每秒。 |
| UEAMBRDLK | 下行UE AMBR (kbps) | global_planned | optional | 无 | 整数类型，取值范围是0~4000000000，单位是千比特每秒。 |
| EXRATRESTRICT | 扩展RAT限制 | global_planned | optional | 无 | <br>- NOT_SUPPORT（不支持） |
| PRIMRATRESTRICT | 主接入限制的RAT类型 | global_planned | conditional | 无 | <br>- “E-UTRA（E-UTRA）”：不允许E-UTRA作为主接入类型。 |
| SECRATRESTRICT | 辅助接入限制的RAT类型 | global_planned | conditional | 无 | <br>- “E-UTRA（E-UTRA）”：不允许E-UTRA作为主接入类型。 |
| MPSMCSPRI | MPSMCS优先级 | global_planned | conditional | CFG_FIRST | <br>- “CFG_FIRST（配置优先）”：表示无论用户是否签约，均优先使用本命令指定的配置。 |
| MPS | MPS | global_planned | conditional | NULL | <br>- “NOT_SUPPORT（不支持）”：不支持 |
| MCS | MCS | global_planned | conditional | NULL | <br>- “NOT_SUPPORT（不支持）”：不支持 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-106207

**md：`WSFD-106207/WSFD-106207 基于SPID的UE驻留和切换策略管理（适用于AMF）参考信息_52057823.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    > 
    > #### [告警](#ZH-CN_CONCEPT_0000001152057823)

**md：`WSFD-106207/激活基于SPID的UE驻留和切换策略管理_52313549.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | 用户范围(SUBRANGE) | IMSI_PREFIX | 本端规划 | 用于指定RFSP下发的策略。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | IMSI前缀(IMSIPRE) | 30809 | 全网规划 | 用于指定RFSP下发的策略。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | RFSP索引(RFSPINDEX) | 1 | 本端规划 | 用于指定RFSP下发的策略。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | RFSP优先级(RFSPPRI) | CFG_FIRST | 全网规划 | 用于指定RFSP下发的策略。 |
- 任务示例脚本（该命令行）：
  `ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="30809", RFSPINDEX=1, RFSPPRI=CFG_FIRST;`
- 操作步骤上下文（±2 行原文）：
  L40:
    >     - **场景一：运营商规划完全信赖用户在UDM的签约信息，在UDM直接规划好RFSP ID， UNC 本地不做任何RFSP** **控制** **。**
    >     - **场景二：假设不信赖UDM中的用户签约信息（例如对于漫游用户），或在UDM签约未规划或UDM不支持该功能。为了实现自定义的驻留优先级控制， UNC 可以在本地针对用户进行RFSP策略的配置：**
    >       [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001152313549)
  L53:
    > 
    > ```
    > ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="30809", RFSPINDEX=1, RFSPPRI=CFG_FIRST;
    > ```

**md：`WSFD-106207/特性概述_51977111.md`**
- 操作步骤上下文（±2 行原文）：
  L86:
    >       将签约的RFSP保存在UsedRfspIndex中，后续AM策略偶联建立流程中，将签约的RFSP发送给PCF，如果PCF返回有效的RFSP，则将PCF返回的RFSP保存在UsedRfspIndex。
    >     - AMF本地配置了有效的RFSP
    >       [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) 中RFSP优先级为配置优先：将本地配置的RFSP保存在UsedRfspIndex中，后续AM策略偶联建立流程中，将本地配置的RFSP发送给PCF，如果PCF返回有效的RFSP，则将PCF返回的RFSP保存在UsedRfspIndex。
    >       [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) 中RFSP优先级为签约优先：将签约的RFSP保存在UsedRfspIndex中，后续AM策略偶联建立流程中，将签约的RFSP发送给PCF，如果PCF返回有效的RFSP，则将PCF返回的RFSP保存在UsedRfspIndex。
    > - 签约数据中没有有效的RFSP：
  L87:
    >     - AMF本地配置了有效的RFSP
    >       [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) 中RFSP优先级为配置优先：将本地配置的RFSP保存在UsedRfspIndex中，后续AM策略偶联建立流程中，将本地配置的RFSP发送给PCF，如果PCF返回有效的RFSP，则将PCF返回的RFSP保存在UsedRfspIndex。
    >       [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) 中RFSP优先级为签约优先：将签约的RFSP保存在UsedRfspIndex中，后续AM策略偶联建立流程中，将签约的RFSP发送给PCF，如果PCF返回有效的RFSP，则将PCF返回的RFSP保存在UsedRfspIndex。
    > - 签约数据中没有有效的RFSP：
    >   不和PCF交互，直接使用AMF本地配置的RFSP。
  L99:
    > 1. UE向AMF发起注册请求，注册场景包括初始注册、5GC内移动性注册更新、周期性注册更新以及EPS到5GC的移动性注册更新等流程（详细参见[实现原理](实现原理_05217924.md)表1流程）。
    > 2. AMF从UDM获取用户签约的RFSP信息。
    > 3. AMF向PCF发起AM策略（Access and Mobility Policy，接入和移动性策略）请求。如果AMF本地已配置RFSP信息，则根据配置[**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)的**RFSP优先级(RFSPPRI)**参数决定AMF将本地配置的RFSP信息发送给PCF，或者将UDM签约的RFSP信息发送给PCF。PCF对RFSP信息做出调整，发送Npcf_AMPolicyControl_Create Response消息给AMF，携带RFSP信息。
    > 4. 当AMF获取RFSP信息，对于处于连接态的UE，AMF会把RFSP信息再带给NG-RAN。
    > 

### WSFD-106003

**md：`WSFD-106003/WSFD-106003 用户接入控制功能（适用于AMF）参考信息_48552639.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    > - [**SET NGMMPROCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM流程管理/5G移动性管理流程控制参数/设置5G移动性管理流程控制参数（SET NGMMPROCTRL）_09652386.md)
    > 

**md：`WSFD-106003/激活用户接入控制功能特性（适用于AMF）_48552637.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | IMSIPRE（IMSI前缀） | 123431234567890 | 本端规划 | AMF本地配置移动性接入限制信息。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | RATRESTRICT（RAT限制） | EUTRA-1 | 本端规划 | AMF本地配置移动性接入限制信息。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | CORERESTRICT（核心网类型限制） | FIFTHGC-1 | 本端规划 | AMF本地配置移动性接入限制信息。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | RFSPINDEX（RFSP索引） | 0 | 本端规划 | AMF本地配置移动性接入限制信息。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | SUBRANGE（用户范围） | IMSI_PREFIX | 本端规划 | AMF本地配置移动性接入限制信息。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | NIM（网络切片包含模式策略） | MODE_A（网络切片包含模式A） | 本端规划 | AMF本地配置移动性接入限制信息。 |
- 任务示例脚本（该命令行）：
  `ADD NGMMSUBDATA: SUBRANGE=ALL_USER, CORERESTRICT=FIFTHGC-1;`
  `ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="123431234567890", RATRESTRICT=NR-1;`
  `ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="123431234567891", RATRESTRICT=EUTRA-1;`
  `ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="123431234567892", CORERESTRICT=EPC-1;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. AMF本地配置用户移动性接入限制信息。
    >   [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    > 3. 配置拒绝用户接入的原因值。
    >   [**SET NGMMPROCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM流程管理/5G移动性管理流程控制参数/设置5G移动性管理流程控制参数（SET NGMMPROCTRL）_09652386.md)
  L59:
    >   //AMF本地配置用户移动性接入限制信息。
    >   ```
    >   ADD NGMMSUBDATA: SUBRANGE=ALL_USER, CORERESTRICT=FIFTHGC-1;
    >   ```
    >   //拒绝用户接入的原因值。
  L68:
    >   //AMF本地配置用户移动性接入限制信息。
    >   ```
    >   ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="123431234567890", RATRESTRICT=NR-1;
    >   ```
    >   //拒绝用户接入的原因值。

**md：`WSFD-106003/本地配置与签约数据的优先级_48748809.md`**
- 操作步骤上下文（±2 行原文）：
  L9:
    > - **AMF本地配置**
    >   为了在AMF上支持针对不同用户接入的灵活控制，AMF提供用户接入控制的本地策略配置，可配置本地策略适用的 **用户范围** 、指定限制的 **RAT类型** 和指定限制的 **核心网类型** 等。
    >   对于指定的用户（群），根据 [**ADD NGMMSUBDATA**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) 命令中“SUBRANGE”参数来匹配 **用户范围** ，优先级从高到低依次为：IMSI前缀（包括用户群组）>外网用户>本网用户>所有用户。如果其匹配成功，则按照本地配置的策略执行接入控制。
    > - **AMF本地配置****与****签约数据****的优先级**
    >   对于待接入的用户，同时存在签约信息和AMF本地配置的移动性接入限制信息，如果用户匹配了AMF本地配置的接入限制记录，则按照本地配置执行接入控制。只有当AMF本地未配置或者用户无任何匹配的接入限制记录时，AMF才根据签约数据检查接入控制。具体决策场景如 [表1](#ZH-CN_TOPIC_0248748809__table958362413522) 。

### WSFD-010110

**md：`WSFD-010110/初始注册流程_42250036.md`**
- 操作步骤上下文（±2 行原文）：
  L32:
    >   为实现此流程，AMF上的RedCap功能命令 [**SET AMFREDCAPFUNC**](../../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/RedCap功能管理/设置AMF RedCap功能（SET AMFREDCAPFUNC）_17306402.md) 的参数 **RATCMPTSW** 取值需要为"SMF"。
    > 3. **Step 9**：AMF向UDM发起Nudm_UECM_Registration进行注册，携带RatType取值为NR_REDCAP。
    > 4. **Step 10**：AMF通过Nudm_SDM_Get从UDM获取签约数据，包括ratRestrictions。若ratRestritions中包含NR_REDCAP，AMF拒绝用户接入。该限制可通过[**ADD NGMMSUBDATA**](../../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)的参数**RATRESTRICT**配置。
    >   为实现 **Step 9&10** ，AMF上需配置N8接口兼容性 **ADD AMFN8CMPTPLCY** 或配置RedCap功能命令 [**SET AMFREDCAPFUNC**](../../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/RedCap功能管理/设置AMF RedCap功能（SET AMFREDCAPFUNC）_17306402.md) 的参数 **RATCMPTSW** 取值为"UDM"。
    > 5. **Step 13**：若AMF开启AM策略控制，AMF向PCF发送 Npcf_AMPolicyControl_Create Request消息，建立AM（Access Management）策略控制关联，并携带RatType取值为NR_REDCAP。

**md：`WSFD-010110/移动性注册更新流程_93049793.md`**
- 操作步骤上下文（±2 行原文）：
  L80:
    >   为实现此流程，AMF上的RedCap功能命令 [**SET AMFREDCAPFUNC**](../../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/RedCap功能管理/设置AMF RedCap功能（SET AMFREDCAPFUNC）_17306402.md) 的参数 **RATCMPTSW** 取值需要为"SMF"。
    > 3. **Step 9**：AMF向UDM发起Nudm_UECM_Registration进行注册，携带RatType取值为NR_REDCAP。
    > 4. **Step 10**：AMF通过Nudm_SDM_Get从UDM获取签约数据，包括ratRestrictions。若ratRestritions中包含NR_REDCAP， AMF拒绝用户接入。该限制可通过[**ADD NGMMSUBDATA**](../../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)的参数**RATRESTRICT**配置。
    >   为实现 **Step 9&10** ，AMF上需配置N8接口兼容性 [**ADD AMFN8CMPTPLCY**](../../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/AMF N8接口兼容性参数管理/增加AMF N8接口兼容性策略（ADD AMFN8CMPTPLCY）_38983042.md) 或配置RedCap功能命令 [**SET AMFREDCAPFUNC**](../../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/RedCap功能管理/设置AMF RedCap功能（SET AMFREDCAPFUNC）_17306402.md) 的参数 **RATCMPTSW** 取值为"UDM"。
    > 5. **Step 13**：若AMF开启AM策略控制，AMF向PCF发送 Npcf_AMPolicyControl_Update Request消息，优先复用老侧的AM策略。若老侧没有，AMF则向PCF发送Npcf_AMPolicyControl_Create Request消息获取新的AM策略，可以将RatType取值为NR_REDCAP携带给PCF。

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md)
    > - [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md)
    > - [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > - [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | 用户范围（SUBRANGE） | HOME_USER | 全网规划 | 在AMF上配置哪些用户可使用本地RFSP索引。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | RAT限制（RATRESTRICT） | NR | 全网规划 | 此处以5G终端接入5G Core为例。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | 核心网类型限制（CORERESTRICT） | FIFTHGC | 全网规划 | 此处以5G终端接入5G Core为例。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | RFSP索引（RFSPINDEX） | 5 | 全网规划 | 取值非0时，此处是本地配置的RFSP索引。<br>取值为0时，标识未配置本地的RFSP索引。 |
  | [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md) | RFSP优先级（RFSPPRI） | CFG_FIRST | 全网规划 | - 设置为“CFG_FIRST”，无论用户是否签约RFSP ID，均使用本地配置的RFSP索引。该场景下本地的“RFSP索引”不能为“0”。<br>- 设置为“SUB_FIRST”时，优先使用用户签约的RFSP ID，如用户未签约RFSP ID，使用本地配置的RFSP索引。<br>AMF根据该配置，决策携带哪个RFSP索引 给PCF。后续处理为：<br>- PCF返回RFSP索引时，AMF将PCF返回的RFSP索引发送给无线侧。<br>- PCF未返回RFSP索引时，AMF将此处决策的RFSP索引发送给无线侧。 |
- 任务示例脚本（该命令行）：
  `ADD NGMMSUBDATA: SUBRANGE=HOME_USER, RATRESTRICT=EUTRA-0&NR-1, CORERESTRICT=FIFTHGC-1, RFSPPRI=CFG_FIRST, RFSPINDEX=5;`
  `ADD NGMMSUBDATA: SUBRANGE=HOME_USER, RATRESTRICT=EUTRA-0&NR-1, CORERESTRICT=FIFTHGC-1, RFSPPRI=CFG_FIRST, RFSPINDEX=5;`
- 操作步骤上下文（±2 行原文）：
  L132:
    >       > 对于UE策略，AMF只是透传PCF的消息给UE，故将 “UENOTIFYSW” 设置为 “YES” 前，须联系PCF工程师确认是否刷新UE策略。
    >     7. 配置本地的RFSP索引。用户未签约RFSP ID，或签约的RFSP ID不适用时需要配置。
    >       [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    >     8. 配置AMF支持使用PCF通过Location信元携带的地址进行通信。
    >       **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**
  L290:
    > 
    > ```
    > ADD NGMMSUBDATA: SUBRANGE=HOME_USER, RATRESTRICT=EUTRA-0&NR-1, CORERESTRICT=FIFTHGC-1, RFSPPRI=CFG_FIRST, RFSPINDEX=5;
    > ```
    > 
  L337:
    > 
    > ```
    > ADD NGMMSUBDATA: SUBRANGE=HOME_USER, RATRESTRICT=EUTRA-0&NR-1, CORERESTRICT=FIFTHGC-1, RFSPPRI=CFG_FIRST, RFSPINDEX=5;
    > ```
    > 

### WSFD-110005

**md：`WSFD-110005/WSFD-110005 支持网络切片模式下发参考信息_50497787.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[设置5G移动性管理功能（SET NGMMFUNC）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
    > - **[查询5G移动性管理功能（LST NGMMFUNC）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/查询5G移动性管理功能（LST NGMMFUNC）_09653016.md)**
    > - **[增加用户移动性管理参数（ADD NGMMSUBDATA）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)**
    > - **[删除用户移动性管理参数（RMV NGMMSUBDATA）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/删除用户移动性管理参数（RMV NGMMSUBDATA）_09652660.md)**
    > - **[修改用户移动性管理参数（MOD NGMMSUBDATA）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/修改用户移动性管理参数（MOD NGMMSUBDATA）_09652682.md)**

**md：`WSFD-110005/激活支持网络切片模式下发_45188374.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD NGMMSUBDATA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)** | 3GPP接入方式下的网络切片包含模式（NIM） | MODE_A | 本端规划 | AMF配置网络切片包含模式及下发NIM给UE的判断策略。 |
- 任务示例脚本（该命令行）：
  `ADD NGMMSUBDATA: SUBRANGE=HOME_USER, NIM=MODE_A;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 配置网络切片包含模式。
    >   **[ADD NGMMSUBDATA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)**
    > 3. 配置下发NIM给UE的判断策略。
    >   **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
  L50:
    > 
    > ```
    > ADD NGMMSUBDATA: SUBRANGE=HOME_USER, NIM=MODE_A;
    > ```
    > 

**md：`WSFD-110005/特性概述_45188372.md`**
- 操作步骤上下文（±2 行原文）：
  L66:
    > AMF应支持基于PLMN配置NSSAI Inclusion Mode，并在Registration Accept消息中将NSSAI inclusion mode发送给UE。
    > 
    > - AMF可以通过**[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**或**[ADD NGMMSUBDATA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)**命令配置NSSAI Inclusion mode参数，指定3GPP接入方式下的网络切片包含模式，可以根据运营商的要求控制UE在创建RRC连接时是否携带网络切片信息。有以下5种模式：
    >     - 不携带切片包含模式给UE（只有使用**[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**配置NSSAI Inclusion mode参数时才可配置此种模式）。
    >     - 模式A：初始注册、非UE能力变更触发的移动性注册更新场景下，UE在RRC连接建立时将携带Requested NSSAI给RAN；周期性注册更新、由于UE能力变更引起的移动性注册更新或者服务请求场景下，UE在RRC连接建立时将携带Allowed NSSAI给RAN。

## ④ 自动比对
- 命令真相参数（17）：['CORERESTRICT', 'DRX', 'EXRATRESTRICT', 'IMSI', 'IMSIPRE', 'MCS', 'MPS', 'MPSMCSPRI', 'NIM', 'PRIMRATRESTRICT', 'RATRESTRICT', 'RFSPINDEX', 'RFSPPRI', 'SECRATRESTRICT', 'SUBRANGE', 'UEAMBRDLK', 'UEAMBRULK']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 9, '全网规划': 7}（多值→atom 应考虑 decision_driven）
