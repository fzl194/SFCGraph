# 命令证据包：SET CTXSTARTRATING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置给OCS_CHF发送的消息初始携带的计费属性（SET CTXSTARTRATING）_09897210.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置上下文激活时的给OCS/CHF发送的消息的计费属性。配置该命令后，用户激活时，UNC与在线计费服务器交互的消息中将携带指定的费率组，在线计费服务器会给该费率组下发相应的配额。当用户从离线计费自动恢复成在线计费时，UNC根据该命令的配置决定是否在发送的消息中为该用户使用过的业务重新申请配额。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为5000。
- 配置此命令需要通过ADD URRGROUP添加计费属性。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USERPROFILENAME | 用户模板名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| CTXRURRGRPNAME1 | 初始请求URR组名称1 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME2 | 初始请求URR组名称2 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME3 | 初始请求URR组名称3 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME4 | 初始请求URR组名称4 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME5 | 初始请求URR组名称5 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME6 | 初始请求URR组名称6 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME7 | 初始请求URR组名称7 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME8 | 初始请求URR组名称8 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME9 | 初始请求URR组名称9 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |
| CTXRURRGRPNAME10 | 初始请求URR组名称10 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L32:
    > - [**ADD PDUTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/增加PDU会话级的trigger参数（ADD PDUTRIGGER）_09653225.md)
    > - [**ADD RGTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/增加RG级的trigger参数（ADD RGTRIGGER）_09653787.md)
    > - [**SET CTXSTARTRATING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置给OCS_CHF发送的消息初始携带的计费属性（SET CTXSTARTRATING）_09897210.md)
    > - [**SET FAILHANDLING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)
    > - [**SET N40MSGSTG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md)

**md：`WSFD-011206/计费会话创建流程_01_10001.md`**
- 操作步骤上下文（±2 行原文）：
  L68:
    >     e. SMF通过NRF发现CHF。该方式下不支持3GPP 29510协议中规定的通过主备方式选择CHF，仅支持通过优先级和权重选择CHF。
    >     f. SMF根据本地配置**ADD SELECTCHFGBYCC**命令选择CHF，即基于本地配置的CC选择CHF。
    > 9. SMF发送[Nchf_ConvergedCharging_ChargingDataCreate Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_30f76786/Nchf_ConvergedCharging_ChargingDataCreate Request_23690012.md)消息到CHF，申请授权业务使用以及申请配额。消息中携带用户标识、PDU会话信息等标识信息，以及可能的一个或多个配额申请信息，每个配额申请对应一个费率组RG，携带的配额申请信息通过UNC上的**SET CTXSTARTRATING**命令配置。Nchf_ConvergedCharging_Create Request请求消息中携带的信元举例如下所示：
    >   ```
    >   ......

**md：`WSFD-011206/配置SMF与CHF交互的条件和内容_93420840.md`**
- 数据规划表（该命令的参数行）：
  | **SET CTXSTARTRATING** | 用户模板名称（USERPROFILENAME） | up_test | 已配置数据中获取 | 使用<br>**ADD USERPROFILE**<br>命令定义的<br>“USERPROFILENAME”<br>。 |
  | **SET CTXSTARTRATING** | 初始请求URR组名称1（CTXRTCHGPRONAME1） | urrgroup_test | 已配置数据中获取 | 使用<br>**ADD URRGROUP**<br>命令定义的<br>“URRGROUPNAME”<br>。 |
- 任务示例脚本（该命令行）：
  `SET CTXSTARTRATING: USERPROFILENAME="up_test", CTXRURRGRPNAME1="urrgroup_test";`
- 操作步骤上下文（±2 行原文）：
  L80:
    >       **ADD USERPROFILE**
    >     c. 绑定UserProfile与URR组，从而使SMF在与CHF建立计费会话时，为该用户模板的用户携带相应的URR组中的RG。
    >       **SET CTXSTARTRATING**
    > 3. **可选：** 配置Session级/RG级Trigger。
    >     a. 配置Session级Trigger。
  L117:
    > ADD URRGROUP: URRGROUPNAME="urrgroup_test", UPURRNAME1="urr_test", DOWNURRNAME1="urr_test";
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
    > SET CTXSTARTRATING: USERPROFILENAME="up_test", CTXRURRGRPNAME1="urrgroup_test";
    > ```
    > 

### WSFD-109001

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 任务示例脚本（该命令行）：
  `SET CTXSTARTRATING:USERPROFILENAME="up-test",CTXRURRGRPNAME1="urrgroup1";`
- 操作步骤上下文（±2 行原文）：
  L96:
    >             **ADD URRGROUP**
    >     3. 配置在线计费用户激活时CCR-I消息中携带指定的费率标识。
    >       **SET CTXSTARTRATING**
    >       > **说明**
    >       > 此命令只对内容计费用户生效，PDP级别计费用户不适用该命令。PDP级别计费用户CCR-Initial中携带UserProfile下或者全局下配置的默认计费属性，其中UserProfile优先。如果UserProfile下没有配置CCR-Initial的计费属性，则使用配置在全局下的CCR-Initial的计费属性。如果全局下没有配置CCR-Initial的计费属性，则CCR-Initial不携带计费属性。
  L99:
    >       > **说明**
    >       > 此命令只对内容计费用户生效，PDP级别计费用户不适用该命令。PDP级别计费用户CCR-Initial中携带UserProfile下或者全局下配置的默认计费属性，其中UserProfile优先。如果UserProfile下没有配置CCR-Initial的计费属性，则使用配置在全局下的CCR-Initial的计费属性。如果全局下没有配置CCR-Initial的计费属性，则CCR-Initial不携带计费属性。
    >       **ADD DCCTEMPLATE** 命令配置CCR-I消息中允许携带的RG的最大个数时要与 **SET CTXSTARTRATING** 命令配合使用。如果在 **SET CTXSTARTRATING** 命令中指定了N个RG，则 **ADD DCCTEMPLATE** 命令配置CCR-I消息中允许携带的RG的最大个数至少要配置为N，才能使得上述N个RG都能被CCR-I消息带上申请配额。
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923545)
  L138:
    > 
    > ```
    > SET CTXSTARTRATING:USERPROFILENAME="up-test",CTXRURRGRPNAME1="urrgroup1";
    > ```
    > 

### WSFD-109007

**md：`WSFD-109007/实现原理（适用于Nchf_N40接口的融合计费用户）_74112318.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > 1：用户发起PDU会话建立请求。
    > 
    > 2：GGSN-C/PGW-C/SMF向CHF发送Charging Data Request[Initial]消息，请求建立计费会话。该消息可携带预申请的事件计费配额（通过 [**SET CTXSTARTRATING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置给OCS_CHF发送的消息初始携带的计费属性（SET CTXSTARTRATING）_09897210.md) 命令配置），预申请的事件计费配额数 **由 [ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** 命令中的 “EVENTRSUVALUE” 参数决定，并通过serviceSpecificUnits字段携带给CHF。
    > 
    > 3：CHF向GGSN-C/PGW-C/SMF返回Charging Data Response[Initial]消息。如果GGSN-C/PGW-C/SMF预申请了事件计费配额，事件计费配额和阈值会通过serviceSpecificUnits字段和unitQuotaThreshold字段携带给GGSN-C/PGW-C/SMF。

## ④ 自动比对
- 命令真相参数（11）：['CTXRURRGRPNAME1', 'CTXRURRGRPNAME10', 'CTXRURRGRPNAME2', 'CTXRURRGRPNAME3', 'CTXRURRGRPNAME4', 'CTXRURRGRPNAME5', 'CTXRURRGRPNAME6', 'CTXRURRGRPNAME7', 'CTXRURRGRPNAME8', 'CTXRURRGRPNAME9', 'USERPROFILENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 2}（多值→atom 应考虑 decision_driven）
