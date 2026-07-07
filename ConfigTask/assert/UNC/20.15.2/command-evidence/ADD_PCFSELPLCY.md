# 命令证据包：ADD PCFSELPLCY
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF**

该命令用于对指定的用户群增加PCF的选择策略。通过本配置，AMF可以对不同用户群使用差异化的条件选择到不同的PCF，以满足运营商灵活部署网络的要求。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SUBRANGE | USRGRPID | IMSIPRE | CTRLMODE | TGTPLMNSW | SUPISW | GPSISW | NSSW | RETRYSW | REDIRECTSW | SSSW | CROSSPROVSW |
| --- | --- | --- | --- | --- 

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 | global_planned | required | 无 | <br>- “ALL_USER（所有用户）”：所有用户 |
| USRGRPID | 用户群组标识 | global_planned | conditional | 无 | 整数类型，取值范围是0~4294967294。该用户群标识必须已经通过ADD NGUSRGRP命令添 |
| IMSIPRE | IMSI前缀 | local_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。 |
| CTRLMODE | 控制模式 | global_planned | conditional | 无 | <br>- “WHITELIST（白名单）”：白名单 |
| TGTPLMNSW | 是否使用目标PLMN | global_planned | optional | YES | <br>- “YES（是）”：是 |
| SUPISW | 是否使用SUPI | global_planned | optional | YES | <br>- “YES（是）”：是 |
| GPSISW | 是否使用GPSI | global_planned | optional | NO | <br>- “YES（是）”：是 |
| NSSW | 是否使用网络切片 | global_planned | optional | NO | <br>- “YES（是）”：是 |
| RETRYSW | 是否重选PCF | global_planned | optional | YES | <br>- “YES（是）”：是 |
| REDIRECTSW | 是否支持PCF重定向 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| SSSW | 是否携带Serving Scope | global_planned | conditional | 无 | 当运营商期望能为指定的用户群选择到为特定的区域提供服务的PCF时，启用本开关。 |
| SERVINGSCOPE | 服务范围 | global_planned | conditional | 无 | 字符串类型，输入长度范围是0~64。如果输入多个服务范围，那么使用“:”作为分隔符，比如“pudon |
| CROSSPROVSW | 是否区分跨省漫游 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| NBEGIN | 区域标识起始位置 | global_planned | conditional | 无 | 整数类型，取值范围是1~12。 |
| NEND | 区域标识终止位置 | global_planned | conditional | 无 | 整数类型，取值范围是1~12。 |
| DESC | 描述信息 | local_planned | optional | 无 | 字符串类型，输入长度范围是0~32。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - **[ADD NGUSRGRPMEM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组成员管理/增加5G用户群成员（ADD NGUSRGRPMEM）_44006476.md)**
    > - **[ADD AMUEPLCYCTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)**
    > - **[ADD PCFSELPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)**
    > - **[ADD ALLOWDNN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/本地分流管理/增加允许本地专网分流的DNN（ADD ALLOWDNN）_42502264.md)**
    > 

**md：`WSFD-223003/PDU会话创建使能专网业务流程_85233681.md`**
- 操作步骤上下文（±2 行原文）：
  L10:
    > 
    > 1. UE发起PDU会话创建流程，携带TAI、SUPI以及Requesteddnn信息。
    > 2. AMF根据用户信息及本地配置（**ADD PCFSELPLCY**命令中的“SERVINGSCOPE”参数）就近选择AM-PCF。
    > 3. AMF向AM-PCF发送Npcf_AMPolicyControl_Create Request消息，携带用户TAI位置信息以及SUPI等信息。AM-PCF根据用户对专网业务的签约状态，以及用户当前所处位置的TAI信息决策是否下发专网DNN。
    >     - 若条件满足则将标识专网业务预定义UL CL分流规则的UserProfileName以selectedDnn（"smfSelInfo.dnn" = "dnn-ar"）的形式通过Npcf_AMPolicyControl_Create Response消息下发给AMF。

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（AMF）_82619543.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD PCFSELPLCY](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)** | SUBRANGE（用户范围） | USER_GROUP | 全网规划 | 配置AM-PCF的选择策略。USRGRPID参数需要通过命令<br>**[ADD NGUSRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)**<br>预先配置好。 |
  | **[ADD PCFSELPLCY](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)** | USRGRPID（用户群组标识） | 20 | 全网规划 | 配置AM-PCF的选择策略。USRGRPID参数需要通过命令<br>**[ADD NGUSRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)**<br>预先配置好。 |
  | **[ADD PCFSELPLCY](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)** | CTRLMODE（控制模式） | WHITELIST | 全网规划 | 配置AM-PCF的选择策略。USRGRPID参数需要通过命令<br>**[ADD NGUSRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)**<br>预先配置好。 |
  | **[ADD PCFSELPLCY](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)** | SSSW（是否携带Serving Scope） | YES | 全网规划 | 配置AM-PCF的选择策略。USRGRPID参数需要通过命令<br>**[ADD NGUSRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)**<br>预先配置好。 |
  | **[ADD PCFSELPLCY](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)** | SERVINGSCOPE（服务范围） | YES | 全网规划 | 配置AM-PCF的选择策略。USRGRPID参数需要通过命令<br>**[ADD NGUSRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)**<br>预先配置好。 |
  | **[ADD PCFSELPLCY](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)** | DESC（描述信息） | for roaming user | 本端规划 | 配置AM-PCF的选择策略。USRGRPID参数需要通过命令<br>**[ADD NGUSRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)**<br>预先配置好。 |
- 任务示例脚本（该命令行）：
  `ADD PCFSELPLCY: SUBRANGE=USER_GROUP, USRGRPID=20,CTRLMODE=WHITELIST, SSSW=YES, SERVINGSCOPE="YES", DESC="for roaming user";`
- 操作步骤上下文（±2 行原文）：
  L63:
    > 
    > ```
    > ADD PCFSELPLCY: SUBRANGE=USER_GROUP, USRGRPID=20,CTRLMODE=WHITELIST, SSSW=YES, SERVINGSCOPE="YES", DESC="for roaming user";
    > ```
    > 

### WSFD-230001

**md：`WSFD-230001/WSFD-230001 动态UE Logo下发参考信息_45929684.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [ADD NGUSRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)
    > - [ADD NGUSRGRPMEM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组成员管理/增加5G用户群成员（ADD NGUSRGRPMEM）_44006476.md)
    > - [ADD PCFSELPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
    > - [ADD NITZPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NITZ管理/NITZ策略管理/增加NITZ策略（ADD NITZPLCY）_09652255.md)
    > - [ADD AMUEPLCYCTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD GUAMI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/AMF/AMF全局标识符管理/增加AMF全局标识（ADD GUAMI）_09653726.md)
    > - [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
    > - [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)
    > - [**MOD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/修改AM策略和UE策略控制参数（MOD AMUEPLCYCTRL）_09654427.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md) | 用户范围（SUBRANGE） | HOME_USER | 全网规划 | AMF为指定用户群增加PCF的选择策略。此处以所有用户按照SUPI为例，实际请以规划为准。 |
  | [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md) | 是否适用目标PLMN（TGTPLMNSW） | NO | 全网规划 | AMF为指定用户群增加PCF的选择策略。此处以所有用户按照SUPI为例，实际请以规划为准。 |
  | [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md) | 是否适用SUPI（SUPISW） | YES | 全网规划 | AMF为指定用户群增加PCF的选择策略。此处以所有用户按照SUPI为例，实际请以规划为准。 |
  | [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md) | 是否适用GPSI（GPSISW） | NO | 全网规划 | AMF为指定用户群增加PCF的选择策略。此处以所有用户按照SUPI为例，实际请以规划为准。 |
  | [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md) | 是否适用网络切片（NSSW） | NO | 全网规划 | AMF为指定用户群增加PCF的选择策略。此处以所有用户按照SUPI为例，实际请以规划为准。 |
  | [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md) | 是否重选PCF（RETRYSW） | YES | 全网规划 | AMF在收到初选PCF的5xx原因值后，是否重选PCF再次重试AM策略和UE策略偶联创建流程。 |
  | [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md) | 描述信息（DESC） | for home user | 全网规划 | 自定义，便于运维即可。 |
- 任务示例脚本（该命令行）：
  `ADD PCFSELPLCY: SUBRANGE=HOME_USER, TGTPLMNSW=NO, SUPISW=YES, GPSISW=NO, NSSW=NO,  RETRYSW=YES, DESC="for home user";`
  `ADD PCFSELPLCY: SUBRANGE=HOME_USER, TGTPLMNSW=NO, SUPISW=YES, GPSISW=NO, NSSW=NO,  RETRYSW=YES, DESC="for home user";`
- 操作步骤上下文（±2 行原文）：
  L115:
    >       [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     3. 配置AMF选择PCF的策略信息。已存在正确的选择PCF的策略信息时，请跳过本步骤。
    >       [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
    >     4. 配置应用网络侧规划的AM策略/UE策略的用户群。默认不使用网络侧规划的AM策略/UE策略。
    >       [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)
  L278:
    > 
    > ```
    > ADD PCFSELPLCY: SUBRANGE=HOME_USER, TGTPLMNSW=NO, SUPISW=YES, GPSISW=NO, NSSW=NO,  RETRYSW=YES, DESC="for home user";
    > ```
    > 
  L325:
    > 
    > ```
    > ADD PCFSELPLCY: SUBRANGE=HOME_USER, TGTPLMNSW=NO, SUPISW=YES, GPSISW=NO, NSSW=NO,  RETRYSW=YES, DESC="for home user";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（16）：['CROSSPROVSW', 'CTRLMODE', 'DESC', 'GPSISW', 'IMSIPRE', 'NBEGIN', 'NEND', 'NSSW', 'REDIRECTSW', 'RETRYSW', 'SERVINGSCOPE', 'SSSW', 'SUBRANGE', 'SUPISW', 'TGTPLMNSW', 'USRGRPID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 12, '本端规划': 1}（多值→atom 应考虑 decision_driven）
