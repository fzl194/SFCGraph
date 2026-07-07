# 命令证据包：SET CHGCHAR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用于设置某个计费属性的参数配置。
**notes（规格/上限→应投影 atom rule）**：
- - 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 只有[**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md)命令配置的CG，才能在此命令、[**ADD CHGBEHA**](../计费行为参数配置/增加计费行为参数(ADD CHGBEHA)_26145366.md)和[**ADD CHGPLMNCG**](../P

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CC | 计费属性 | 整网规划 | required |  | <br>- “NORMAL（普通计费）”：表示普通计费属性，按照此种方式计费的用户按照常规的方式支付 |
| MP | 生成M-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| MPCP | 周期生成M-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| MPL | M-CDR生成周期（min） | 整网规划 | optional |  | 1min～1440min |
| MLCP | 位置更新生成M-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| MLCL | M-CDR位置更新最大次数 | 整网规划 | optional |  | 1～10 |
| RPCMCDR | 精简M-CDR | 整网规划 | optional |  | <br>- “NO（否）”：表示不生成精简M-CDR。 |
| SP | 生成S-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| SPP | 周期生成S-CDR | 整网规划 | optional |  | <br>- “FORBID（不生成）”：表示不周期生成S-CDR。 |
| SPL | S-CDR生成周期（min） | 整网规划 | optional |  | 1min～1440min |
| SVP | 流量生成S-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| SVL | 生成S-CDR流量阈值（KB） | 整网规划 | optional |  | 1KB～1000000KB |
| SCCP | 计费条件变更生成S-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| SCCL | 最大计费条件变更次数 | 整网规划 | optional |  | 1～10 |
| SLCP | 位置更新生成S-CDR | 整网规划 | optional |  | <br>- “NO（不生成）”：不会导致inter RAU SGSN新侧不创建话单，只是位置更新时不 |
| PCC | PLMN变化生成特定原因值S-CDR | 整网规划 | optional |  | <br>“NO（不生成）” |
| RPCSCDR | 精简S-CDR | 整网规划 | optional |  | <br>- “NO（否）” |
| SMOP | 生成S-SMO-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| SMTP | 生成S-SMT-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| LCSMOP | 生成LCS-MO-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| LCSMTP | 生成LCS-MT-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| LCSNIP | 生成LCS-NI-CDR | 整网规划 | optional |  | <br>- “NO（不生成）” |
| SR | 计费限呼标志 | 整网规划 | optional |  | <br>- “UNRESTRICT（不限制业务）”：表示不限制业务，在缓存满时保证网上用户和新接入用 |
| CGIP | CG的IPv4地址 | 整网规划 | optional |  | 0.0.0.0～255.255.255.255 |
| CGIPV6 | CG的IPv6地址 | 整网规划 | optional |  | ::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF |
| TARIACCFLG | 费率变更允许的用户类型 | 整网规划 | optional |  | <br>- “HOME_USER（本地用户）” |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010501

**md：`WSFD-010501/WSFD-010501 会话管理特性概述（适用于2G&3G）_85436070.md`**
- 操作步骤上下文（±2 行原文）：
  L127:
    > 
    > > **说明**
    > > PDP上下文的修改一般都会包含QoS的改变，QoS改变后是否会重新生成话单是根据命令 [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) 的配置决定的。
    > 
    > #### [特性规格](#ZH-CN_CONCEPT_0185436070)

### WSFD-106202

**md：`WSFD-106202/WSFD-106202 SMS over GPRS_EDGE_WCDMA参考信息_85247549.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**增加本地PLMN(ADD HPLMN)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)
    > - [**增加互联PLMN(ADD CONNECTPLMN)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)
    > - [**设置计费属性参数(SET CHGCHAR)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)
    > - [**查询计费属性参数(LST CHGCHAR)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/查询计费属性参数(LST CHGCHAR)_72225049.md)
    > 

**md：`WSFD-106202/激活SMS over GPRS_EDGE_WCDMA_84683740.md`**
- 数据规划表（该命令的参数行）：
  | [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 计费属性（CC） | NORMAL | 全网规划 | 开启始发SMS和终止SMS计费功能。 |
  | [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 生成S-SMO-CDR（SMOP） | YES | 全网规划 | 开启始发SMS和终止SMS计费功能。 |
  | [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 生成S-SMT-CDR（SMTP） | YES | 全网规划 | 开启始发SMS和终止SMS计费功能。 |
  | [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | CG的IPv4地址（CGIP） | 10.10.171.9 | 全网规划 | 开启始发SMS和终止SMS计费功能。 |
- 任务示例脚本（该命令行）：
  `SET CHGCHAR: CC=NORMAL, SMOP=YES, SMTP=YES, CGIP="10.10.171.9";`
- 操作步骤上下文（±2 行原文）：
  L93:
    > 6. 配置短消息计费。
    >     a. 开启始发SMS和终止SMS计费功能。
    >       [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)
    >       > **说明**
    >       > - 参数“SMOP”（生成S-SMO-CDR）选择“YES”。
  L147:
    > 
    > ```
    > SET CHGCHAR: CC=NORMAL, SMOP=YES, SMTP=YES, CGIP="10.10.171.9";
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**SET CHGPLMNCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md)
    > - [**LST CHGPLMNCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/查询PLMN的计费属性参数(LST CHGPLMNCHAR)_72344991.md)
    > - [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)
    > - [**LST CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/查询计费属性参数(LST CHGCHAR)_72225049.md)
    > - [**ADD CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)

**md：`WSFD-011201/离线计费话单（SGSN）_02556787.md`**
- 操作步骤上下文（±2 行原文）：
  L209:
    > - 基于PLMN和APN NI共同定制的S-CDR话单生成策略（通过命令**ADD CHGPLMNCFG**配置）。
    > - 基于IMSI前缀、APN NI、拜访类型、计费属性共同定制S-CDR话单生成策略（通过命令**ADD CHGIMSICFG**配置）。
    > - 全局S-CDR话单生成策略，即基于计费属性定制生成S-CDR话单的策略（通过命令**SET CHGCHAR**配置）。计费属性及计费属性选择机制详见：[计费属性](#ZH-CN_TOPIC_0302556787__section1423991923213)和[计费属性选择机制](#ZH-CN_TOPIC_0302556787__section846162403217)
    > 
    > > **说明**

**md：`WSFD-011201/配置离线计费参数（SGSN）_01731207.md`**
- 操作步骤上下文（±2 行原文）：
  L80:
    > 
    > 8. 配置特定计费属性的CDR参数。
    >   **SET CHGCHAR**
    >   > **说明**
    >   > - 只有**ADD CHGCG**命令配置的CG，才能在**SET CHGCHAR**命令中生效。
  L82:
    >   **SET CHGCHAR**
    >   > **说明**
    >   > - 只有**ADD CHGCG**命令配置的CG，才能在**SET CHGCHAR**命令中生效。
    >   > - 根据实际场景的不同选择性配置计费属性功能。用户计费属性的优先级由低到高的顺序如下：
    >   >     - **SET CHGCDR**命令配置的计费属性。
  L85:
    >   > - 根据实际场景的不同选择性配置计费属性功能。用户计费属性的优先级由低到高的顺序如下：
    >   >     - **SET CHGCDR**命令配置的计费属性。
    >   >     - **SET CHGCHAR**命令配置的计费属性。
    >   >     - 用户在HLR中签约的计费属性。
    > 

**md：`WSFD-011201/调测费率切换功能（SGSN）_95923436.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > > - 设置计费属性（CC）为NORMAL的用户生成S-CDR，将最大计费条件变更次数（SCCL）设置为3次。
    > >   在 “MML命令行-UNC” 窗口上执行命令
    > >   **SET CHGCHAR** :CC=NORMAL,SP=YES,SCCL=3;
    > > - 确保SGSN与CG话单版本一致，连接正常。
    > 

### WSFD-011202

**md：`WSFD-011202/WSFD-011202 支持热计费功能（适用于SGSN）参考信息_85142303.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)
    > - [**LST CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/查询计费属性参数(LST CHGCHAR)_72225049.md)
    > 

**md：`WSFD-011202/激活支持热计费功能_84683735.md`**
- 数据规划表（该命令的参数行）：
  | [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 计费属性（CC） | HOTBILLING | 全网规划 | 设置计费属性为热计费，并配置相关参数。 |
  | [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 生成S-CDR（SP） | YES | 全网规划 | 设置计费属性为热计费，并配置相关参数。 |
  | [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 周期生成S-CDR（SPP） | PERMIT | 全网规划 | 设置计费属性为热计费，并配置相关参数。 |
  | [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | S-CDR生成周期（min）（SPL） | 2 | 全网规划 | 设置计费属性为热计费，并配置相关参数。 |
- 任务示例脚本（该命令行）：
  `SET CHGCHAR: CC=HOTBILLING, SP=YES, SPP=PERMIT, SPL=2;`
- 操作步骤上下文（±2 行原文）：
  L41:
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置计费属性为热计费，并配置相关参数。
    >   [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)
    >   > **说明**
    >   > 参数 “CC” （计费属性）选择 “HOTBILLING” (实时计费)。
  L62:
    > 
    > ```
    > SET CHGCHAR: CC=HOTBILLING, SP=YES, SPP=PERMIT, SPL=2;
    > ```

## ④ 自动比对
- 命令真相参数（26）：['CC', 'CGIP', 'CGIPV6', 'LCSMOP', 'LCSMTP', 'LCSNIP', 'MLCL', 'MLCP', 'MP', 'MPCP', 'MPL', 'PCC', 'RPCMCDR', 'RPCSCDR', 'SCCL', 'SCCP', 'SLCP', 'SMOP', 'SMTP', 'SP', 'SPL', 'SPP', 'SR', 'SVL', 'SVP', 'TARIACCFLG']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 8}（多值→atom 应考虑 decision_driven）
