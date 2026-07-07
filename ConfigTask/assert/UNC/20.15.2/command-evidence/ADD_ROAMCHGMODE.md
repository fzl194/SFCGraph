# 命令证据包：ADD ROAMCHGMODE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/漫游属性计费模式/增加基于漫游属性的计费接口选择方式（ADD ROAMCHGMODE）_23622918.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：![](增加基于漫游属性的计费接口选择方式（ADD ROAMCHGMODE）_23622918.assets/notice_3.0-zh-cn_2.png)

配置基于漫游属性选择计费接口选择方式不当可能选错计费策略接口，相应计费策略接口未配置时会导致计费相关流程失败，影响用户使用业务，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：PGW-C、GGSN、SMF、SGW-C**

该
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 最多可输入10000条记录。
- 4G/5G互操作流程的计费接口不变。2G/3G/4G互操作流程的计费接口不变。
- 当需要使用本命令配置2G接入使用Nchf接口时，需要提前和对端CHF确认是否支持。
- 当5G终端5G接入时，若该命令配置为gagy模式，需要开启特定License项，请提前联系华为技术支持确认。
- 选择计费接口时，该命令优先级高于SE

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TMACCTYPE | 指定终端和接入类型 | local_planned | required | 无 | <br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活 |
| CTRLTYPE | 控制类型 | global_planned | required | 无 | <br>- APN_LEVEL（APN级别） |
| APN | APN名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字 |
| ROAMINGTYPE | 漫游属性 | local_planned | required | 无 | <br>- ROAMING（漫游用户） |
| BY5GSIWKI | 按5GS互操作指示选择计费接口 | local_planned | conditional | 无 | <br>- False（否） |
| FORCED | 指定的计费接口 | local_planned | conditional | 无 | <br>- “GaGyMode（GaGy模式）”：GaGy模式 |
| FORSGWONLY | 作为SGW计费模式 | local_planned | conditional | 无 | <br>- GaGyMode（GaGy模式） |
| FORVSMFONLY | 作为V-SMF计费模式 | global_planned | conditional | 无 | <br>- “GaGyMode（GaGy模式）”：GaGy模式 |
| BY5GCNRI | 按5GC无限制接入标识选择计费 | local_planned | conditional | 无 | <br>- False（否） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_97906843.md`**
- 数据规划表（该命令的参数行）：
  | ****ADD ROAMCHGMODE**** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 本端规划 | 5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。 |
  | ****ADD ROAMCHGMODE**** | 漫游属性（ROAMINGTYPE） | ROAMING | 本端规划 | 配置是否通过漫游属性为用户下发对应的计费接口。 |
  | ****ADD ROAMCHGMODE**** | 按5GS互操作指示选择计费接口（BY5GSIWKI） | False | 全网规划 | 配置是否按5GS互操作标识的取值来选择计费接口。“5GS互操作标识”是指S5/S8接口的“5GS Interworking Indication”参数。 |
  | ****ADD ROAMCHGMODE**** | 指定的计费接口（FORCED） | NchfMode | 全网规划 | Nchf模式 |
  | ****ADD ROAMCHGMODE**** | 作为SGW计费模式（FORSGWONLY） | GaGyMode | 全网规划 | 可指定SGW发起计费会话时的计费接口。 |
  | ****ADD ROAMCHGMODE**** | 作为V-SMF计费模式（FORVSMFONLY） | GaGyMode | 全网规划 | 5G终端国漫场景下在漫游地接入5G核心网时可指定计费接口。 |
- 任务示例脚本（该命令行）：
  `ADD ROAMCHGMODE: ROAMINGTYPE="ROAMING",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=False, FORCED=GaGyMode;`
- 操作步骤上下文（±2 行原文）：
  L10:
    > ## [操作场景](#ZH-CN_OPI_0297906843)
    > 
    > UNC支持配置在不同类型终端接入不同网络时选择计费接口，计费接口选择有三种方式，优先级从高到低为：基于用户漫游属性选择计费接口 （对应指令为 **ADD ROAMCHGMODE** ）> 基于APN/DNN选择计费接口 （对应指令为 **ADD APNCHGMODE** ）> 全局配置计费接口（对应指令为 **SET CHGMODE** ）。 [图1](#ZH-CN_OPI_0297906843__fig97212421047) 绘制了不同类型终端接入不同网络时计费接口选择。
    > 
    > **图1** 不同类型终端接入不同网络时计费接口选择逻辑图
  L19:
    > 
    > > **说明**
    > > SGW独立部署的场景下，需要SGW发起计费会话。在这种场景下，通过设置SGW上 **ADD ROAMCHGMODE** / **ADD APNCHGMODE** / **SET CHGMODE** 指令中 **FORSGWONLY** 的值可以手动指定计费接口。
    > 
    > UNC支持配置在不同类型终端接入不同网络时选择策略接口，策略接口选择有两种方式，优先级从高到低为：基于APN/DNN选择策略接口 > 全局配置策略接口。 [图2](#ZH-CN_OPI_0297906843__fig12158133203715) 绘制了不同类型终端接入不同网络时策略接口选择。
  L83:
    >   **ADD APNCHGMODE**
    > 3. 配置不同漫游类型在不同类型终端接入不同网络时所选择的计费接口。
    >   ****ADD ROAMCHGMODE****
    > 4. 配置策略接口的选择方式。
    >   **SET POLICYMODE**

### WSFD-011206

**md：`WSFD-011206/配置计费和策略模式_77825710.md`**
- 数据规划表（该命令的参数行）：
  | ****ADD ROAMCHGMODE**** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 本端规划 | 5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。 |
  | ****ADD ROAMCHGMODE**** | 漫游属性（ROAMINGTYPE） | ROAMING | 本端规划 | 配置是否通过漫游属性为用户下发对应的计费接口。 |
  | ****ADD ROAMCHGMODE**** | 按5GS互操作指示选择计费接口（BY5GSIWKI） | False | 全网规划 | 配置是否按5GS互操作标识的取值来选择计费接口。“5GS互操作标识”是指S5/S8接口的“5GS Interworking Indication”参数。 |
  | ****ADD ROAMCHGMODE**** | 指定的计费接口（FORCED） | NchfMode | 全网规划 | Nchf模式 |
  | ****ADD ROAMCHGMODE**** | 作为SGW计费模式（FORSGWONLY） | GaGyMode | 全网规划 | 可指定SGW发起计费会话时的计费接口。 |
  | ****ADD ROAMCHGMODE**** | 作为V-SMF计费模式（FORVSMFONLY） | GaGyMode | 全网规划 | 5G终端国漫场景下在漫游地接入5G核心网时可指定计费接口。 |
- 任务示例脚本（该命令行）：
  `ADD ROAMCHGMODE: ROAMINGTYPE="ROAMING",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=False, FORCED=NchfMode;`
- 操作步骤上下文（±2 行原文）：
  L10:
    > ## [操作场景](#ZH-CN_OPI_0277825710)
    > 
    > UNC支持配置在不同类型终端接入不同网络时选择计费接口，计费接口选择有三种方式，优先级从高到低为：基于用户漫游属性选择计费接口 （对应指令为 **ADD ROAMCHGMODE** ）> 基于APN/DNN选择计费接口 （对应指令为 **ADD APNCHGMODE** ）> 全局配置计费接口（对应指令为 **SET CHGMODE** ）。 [图1](#ZH-CN_OPI_0277825710__fig3186737184017) 绘制了不同类型终端接入不同网络时计费接口选择。
    > 
    > **图1** 不同类型终端接入不同网络时计费接口选择逻辑图
  L19:
    > 
    > > **说明**
    > > SGW独立部署的场景下，需要SGW发起计费会话。在这种场景下，通过设置SGW上 **ADD ROAMCHGMODE** / **ADD APNCHGMODE** / **SET CHGMODE** 指令中 **FORSGWONLY** 的值可以手动指定计费接口。
    > 
    > UNC支持配置在不同类型终端接入不同网络时选择策略接口，策略接口选择有两种方式，优先级从高到低为：基于APN/DNN选择策略接口 > 全局配置策略接口。 [图2](#ZH-CN_OPI_0277825710__fig12158133203715) 绘制了不同类型终端接入不同网络时策略接口选择。
  L82:
    >   **ADD APNCHGMODE**
    > 3. 配置不同漫游类型在不同类型终端接入不同网络时所选择的计费接口。
    >   ****ADD ROAMCHGMODE****
    > 4. 配置策略接口的选择方式。
    >   **SET POLICYMODE**

### WSFD-109001

**md：`WSFD-109001/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_15408913.md`**
- 数据规划表（该命令的参数行）：
  | ****ADD ROAMCHGMODE**** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 本端规划 | 5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。 |
  | ****ADD ROAMCHGMODE**** | 漫游属性（ROAMINGTYPE） | ROAMING | 本端规划 | 配置是否通过漫游属性为用户下发对应的计费接口。 |
  | ****ADD ROAMCHGMODE**** | 按5GS互操作指示选择计费接口（BY5GSIWKI） | False | 全网规划 | 配置是否按5GS互操作标识的取值来选择计费接口。“5GS互操作标识”是指S5/S8接口的“5GS Interworking Indication”参数。 |
  | ****ADD ROAMCHGMODE**** | 指定的计费接口（FORCED） | NchfMode | 全网规划 | Nchf模式 |
  | ****ADD ROAMCHGMODE**** | 作为SGW计费模式（FORSGWONLY） | GaGyMode | 全网规划 | 可指定SGW发起计费会话时的计费接口。 |
  | ****ADD ROAMCHGMODE**** | 作为V-SMF计费模式（FORVSMFONLY） | GaGyMode | 全网规划 | 5G终端国漫场景下在漫游地接入5G核心网时可指定计费接口。 |
- 任务示例脚本（该命令行）：
  `ADD ROAMCHGMODE: ROAMINGTYPE="ROAMING",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=False, FORCED=GaGyMode;`
- 操作步骤上下文（±2 行原文）：
  L10:
    > ## [操作场景](#ZH-CN_OPI_0315408913)
    > 
    > UNC支持配置在不同类型终端接入不同网络时选择计费接口，计费接口选择有三种方式，优先级从高到低为：基于用户漫游属性选择计费接口 （对应指令为 **ADD ROAMCHGMODE** ）> 基于APN/DNN选择计费接口 （对应指令为 **ADD APNCHGMODE** ）> 全局配置计费接口（对应指令为 **SET CHGMODE** ）。 [图1](#ZH-CN_OPI_0315408913__zh-cn_opi_0297906843_fig97212421047) 绘制了不同类型终端接入不同网络时计费接口选择。
    > 
    > **图1** 不同类型终端接入不同网络时计费接口选择逻辑图
  L19:
    > 
    > > **说明**
    > > SGW独立部署的场景下，需要SGW发起计费会话。在这种场景下，通过设置SGW上 **ADD ROAMCHGMODE** / **ADD APNCHGMODE** / **SET CHGMODE** 指令中 **FORSGWONLY** 的值可以手动指定计费接口。
    > 
    > UNC支持配置在不同类型终端接入不同网络时选择策略接口，策略接口选择有两种方式，优先级从高到低为：基于APN/DNN选择策略接口 > 全局配置策略接口。 [图2](#ZH-CN_OPI_0315408913__zh-cn_opi_0297906843_fig12158133203715) 绘制了不同类型终端接入不同网络时策略接口选择。
  L83:
    >   **ADD APNCHGMODE**
    > 3. 配置不同漫游类型在不同类型终端接入不同网络时所选择的计费接口。
    >   ****ADD ROAMCHGMODE****
    > 4. 配置策略接口的选择方式。
    >   **SET POLICYMODE**

## ④ 自动比对
- 命令真相参数（9）：['APN', 'BY5GCNRI', 'BY5GSIWKI', 'CTRLTYPE', 'FORCED', 'FORSGWONLY', 'FORVSMFONLY', 'ROAMINGTYPE', 'TMACCTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 6, '全网规划': 12}（多值→atom 应考虑 decision_driven）
