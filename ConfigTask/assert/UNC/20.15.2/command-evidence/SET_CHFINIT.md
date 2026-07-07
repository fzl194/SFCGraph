# 命令证据包：SET CHFINIT
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置融合计费模板（Converged Charging Template）中用户激活相关参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令的CCTMPLTNAME参数使用ADD CCT命令配置生成。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCTMPLTNAME | CHFINIT | CCRINITRGNUM | WAITCHFRESP | RGSOURCE |
| --- | --- | --- | --- | --- |
| global | SENDRE

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | local_planned | required | 无。 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| CHFINIT | CHF交互使能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- SENDREQ（激活发送） |
| CCRINITRGNUM | 初始RG个数 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | 整数类型，取值范围是0~10。 |
| WAITCHFRESP | CHF交互等待CHF响应开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- DISABLE（不使能） |
| RGSOURCE | RG来源 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查 | <br>- “DEFAULT（缺省配置）”：该参数仅对PCC用户生效，使用PCF下发的规则向CHF预 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/计费会话创建流程_01_10001.md`**
- 操作步骤上下文（±2 行原文）：
  L160:
    >   | "notifyUri":"http://192.168.16.10:31000/nchf-convergedcharging/notify/v2/chargingdata/0890b418120f089410120a001a00b00006ffffffff" | 代表接收CHF的notify消息的SMF的Uri地址。 |
    >   > **说明**
    >   > - Nchf_ConvergedCharging_Create Request消息默认在PDU会话建立时触发，也可以在业务使用时触发，触发方式可通过UNC上的**SET CHFINIT**命令中的“CHFINIT”参数配置。
    >   > - 是否申请配额取决于当前RG的Charging method是否是online类型，只有online的RG才需要申请配额，会在Multiple Unit Usage中携带Rating Group信元。
    > 10. CHF检查该用户账户余额是否能满足配额预留，如果该用户账户有足够余额，CHF执行相应预留动作并开启CDR话单。CHF会生成一张CDR原始话单，同时转换生成CDR最终话单，存储到最终话单临时文件中。当最终话单临时文件达到转正阈值（默认1M大小或半小时），则转正为最终话单文件。

**md：`WSFD-011206/使用全局CCT模板进行融合计费实例_93029782.md`**
- 数据规划表（该命令的参数行）：
  | **SET CHFINIT** | CCTMPLTNAME（融合计费模板名称） | cct-test | 本端规划 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。 |
  | **SET CHFINIT** | CHFINIT（CHF交互使能开关） | SENDREQ | 本端规划 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。 |
  | **SET CHFINIT** | CCRINITRGNUM（初始RG个数） | 10 | 本端规划 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。 |
- 任务示例脚本（该命令行）：
  `SET CHFINIT: CCTMPLTNAME="global", CHFINIT=SENDREQ, CCRINITRGNUM=10;`
- 操作步骤上下文（±2 行原文）：
  L83:
    > 
    > ```
    > SET CHFINIT: CCTMPLTNAME="global", CHFINIT=SENDREQ, CCRINITRGNUM=10;
    > ```
    > 

**md：`WSFD-011206/配置SMF与CHF交互的条件和内容_93420840.md`**
- 数据规划表（该命令的参数行）：
  | **SET CHFINIT** | 融合计费模板名称（CCTMPLTNAME） | cct_test | 已配置数据中获取 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **SET CHFINIT** | CHF交互使能开关（CHFINIT） | SENDREQ | 本端规划 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
  | **SET CHFINIT** | 初始RG个数（CCRINITRGNUM） | 5 | 本端规划 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。<br>CCT模板的配置请参见<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>。 |
- 任务示例脚本（该命令行）：
  `SET CHFINIT: CCTMPLTNAME="cct_test", CHFINIT=SENDREQ, CCRINITRGNUM=5;`
- 操作步骤上下文（±2 行原文）：
  L72:
    > 
    > 1. **可选：** 配置建立PDU会话时是否发送ChargingDataRequest与CHF交互。
    >   **SET CHFINIT**
    > 2. **可选：** 配置SMF在建立计费会话的ChargingDataRequest中携带的为哪些RG申请预配额。
    >     a. 配置URR组合URR，指定需预申请配额的RG。
  L108:
    > 
    > ```
    > SET CHFINIT: CCTMPLTNAME="cct_test", CHFINIT=SENDREQ, CCRINITRGNUM=5;
    > ```
    > 

**md：`WSFD-011206/调测融合计费的计费会话创建功能_89257219.md`**
- 操作步骤上下文（±2 行原文）：
  L59:
    >           - 如果是“激活发送”，请执行[步骤 9](#ZH-CN_OPI_0289257219__step581732155615)。
    >           - 如果是“激活不发送”，请执行[步骤 8.b](#ZH-CN_OPI_0289257219__substep13518171125516)。
    >     b. 执行与当前用户所使用的融合计费模板对应的 [**SET CHFINIT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md) 命令，配置 “CHFINIT” 参数为 “SENDREQ” ，请再次执行 [步骤 3](#ZH-CN_OPI_0289257219__step2585105420194) 。
    > 9. 检查用户激活时是否有可用的CHF。
    >     a. 执行 [**LST GLBDFTCHFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/查询全局默认CHF组（LST GLBDFTCHFGROUP）_09651740.md) 、 [**LST SELECTCHFGBYCC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/查询基于CC选择CHF处理（LST SELECTCHFGBYCC）_09653040.md) 命令，查询当前用户是否有可选择的CHF。

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET CHFINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**SET CHFINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md) | CCTMPLTNAME（融合计费模板名称） | cct-test | 本端规划 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。 |
  | [**SET CHFINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md) | CHFINIT（CHF交互使能开关） | SENDREQ | 本端规划 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。 |
  | [**SET CHFINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md) | CCRINITRGNUM（初始RG个数） | 10 | 本端规划 | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。 |
- 任务示例脚本（该命令行）：
  `SET CHFINIT: CCTMPLTNAME="cct-test", CHFINIT=SENDREQ, CCRINITRGNUM=10;`
- 操作步骤上下文（±2 行原文）：
  L73:
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互建立计费会话。
    >   [**SET CHFINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md)
    > 4. **可选：**配置事件计费使用的计费属性。
    >     a. 配置事件计费的RG使用的URR组及相应URR。
  L123:
    > 
    > ```
    > SET CHFINIT: CCTMPLTNAME="cct-test", CHFINIT=SENDREQ, CCRINITRGNUM=10;
    > ```
    > 

### WSFD-224103

**md：`WSFD-224103/特性概述_62528507.md`**
- 操作步骤上下文（±2 行原文）：
  L71:
    > 2. 当UNC作为V-SMF和H-SMF形态时，QBC计费不支持使用GaGy接口计费。
    > 3. 用户激活场景，使用QBC计费时，不支持SMF不与CHF交互，即用户激活时SMF必须发送计费会话创建请求消息和CHF进行协商RoamingChargingProfile。
    > 4. 漫游切换场景，当**[**SET CHFINIT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md)**命令配置用户激活不与CHF交互，本地用户切换成漫游用户时，不会触发计费会话创建请求消息与CHF协商RoamingCharingProfile，直接使用SMF本地配置生成RoamingChargingProfile。
    > 5. CHF故障恢复后，用户在线恢复重新与CHF创建计费会话时，不支持重新进行RoamingChargingProfile协商。
    > 6. V-SMF切换场景，旧的V-SMF不支持向新的V-SMF返回CHF地址信息，新的V-SMF也不支持使用旧的V-SMF返回的CHF。

## ④ 自动比对
- 命令真相参数（5）：['CCRINITRGNUM', 'CCTMPLTNAME', 'CHFINIT', 'RGSOURCE', 'WAITCHFRESP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 8, '已配置数据中获取': 1}（多值→atom 应考虑 decision_driven）
