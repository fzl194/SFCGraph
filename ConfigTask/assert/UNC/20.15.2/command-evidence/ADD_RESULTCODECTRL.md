# 命令证据包：ADD RESULTCODECTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用来配置当UNC收到指定结果码信息后执行何种操作。例如关闭动态PCC功能、执行缺省动作、执行宕机备份等。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为2100。
- 对于Gx接口的回滚策略，当SET FHBYPASS的GXERRRC参数配置为ENABLE时，SET FHBYPASS命令优先级高于此命令。
- 直连组网模式下，当DirectInitAct、DirectUpdAct、DirectTerminAct配置为Invalid时，则取InitAction、UpdateAction、Termin

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCCTEMPLATE | PCC模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。 |
| INTFTYPE | 接口类型 | 对端协商 | required | 无 | 枚举类型。 |
| N7RESULTCODEVAL | N7返回码 | 对端协商 | conditional | 无 | 字符串类型，输入长度范围为1～3。300-599或者3xx-5xx，不区分大小写。其中xx代表一个范 |
| VENDORID | 设备提供商标识 | global_planned | conditional | 无 | 整数类型，取值范围为0～65535。 |
| GXRESULTCODEVAL | Gx返回码 | 对端协商 | conditional | 无 | 字符串类型，输入长度范围为1～4。1000-9999，1xxx-9xxx，不区分大小写。其中xxxx |
| INITACTION | Initial流程处理动作 | local_planned | optional | 无 | 枚举类型。 |
| INITHOLDTMSW | Initial流程回滚后使能Holding-Time | local_planned | conditional | DISABLE | 枚举类型。 |
| UPDATEACTION | Update流程处理动作 | local_planned | optional | 无 | 枚举类型。 |
| UPDHOLDTMSW | Update流程回滚后使能Holding-Time | local_planned | conditional | DISABLE | 枚举类型。 |
| TERMINACTION | Terminate流程处理动作 | local_planned | optional | 无 | 枚举类型。 |
| DIRECTINITACT | 直连对端Initial流程处理动作 | local_planned | optional | INVALID | 枚举类型。 |
| DIRECTUPDACT | 直连对端Update流程处理动作 | local_planned | optional | INVALID | 枚举类型。 |
| DIRECTTERMINACT | 直连对端Terminate流程处理动作 | local_planned | optional | INVALID | 枚举类型。 |
| DIRECTINITHTSW | 直连对端Initial流程回滚后使能Holding-Time | local_planned | conditional | DISABLE | 枚举类型。 |
| DIRECTUPDHTSW | 直连对端Update流程回滚后使能Holding-Time | local_planned | conditional | DISABLE | 枚举类型。 |
| REACTREQ | 重新激活请求 | local_planned | conditional | DEFAULT | 枚举类型。 |
| DIRECTREACTREQ | 直连对端重激活请求 | local_planned | conditional | DEFAULT | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > - [**ADD PCRFGRPBNDAPN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
    > - [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)
    > - [**ADD RESULTCODECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
    > - [**SET FHBYPASS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)

**md：`WSFD-109101/实现原理_29056158.md`**
- 操作步骤上下文（±2 行原文）：
  L127:
    > | N4接口响应超时或返回异常返回码 | UNC<br>发送PFCP Session Modification Request消息给GGSN-U/PGW-U，GGSN-U/PGW-U响应超时或者返回异常响应，或者GGSN-U/PGW-U发送PFCP Session Report Request消息给<br>UNC<br>，响应超时或者返回异常响应。 | 如果<br>UNC<br>发起消息，GGSN-U/PGW-U无响应或返回异常返回码，则<br>UNC<br>通过PFCP Session Deletion Request消息向GGSN-U/PGW-U发起去活请求。<br>如果GGSN-U/PGW-U发起消息，<br>UNC<br>无响应或返回异常返回码，则GGSN-U/PGW-U通过PFCP Session Report Request消息向<br>UNC<br>发起去活请求。 |
    > 
    > 在等待PCRF响应超时、Gx接口链路故障、CCA消息中携带异常返回码故障场景下， UNC 支持根据 [**SET FHBYPASS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md) 的配置改变异常处理策略。该命令仅用于故障场景下的紧急处理，优先级高于 [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 、 [**ADD RESULTCODECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) 的配置。由于该命令的配置将影响用户的控制策略，只有在获得了客户的书面认可后方可使用。
    > 
    > > **说明**

**md：`WSFD-109101/配置异常场景数据_31422947.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | 设备提供商标识（VENDORID） | 0 | 全网规划 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | 接口类型（INTFTYPE） | INTFTYPE_GX | 对端协商 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | Gx返回码（GXRESULTCODEVAL） | 3xxx | 本端规划 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | PCC模板名称（PCCTEMPLATE） | templatetest | 本端规划 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | Intial流程处理动作（INITACTION） | FAILOVER | 本端规划 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | Update流程处理动作（UPDATEACTION） | FAILOVER | 本端规划 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | Terminate流程处理动作（TERMINACTION） | FAILOVER | 本端规划 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | 直连对端Initial流程处理动作（DIRECTINITACT） | FAILOVER | 本端规划 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | 直连对端Update流程处理动作（DIRECTUPDACT） | FAILOVER | 本端规划 | 配置UNC收到异常返回码后执行何种操作。 |
  | [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) | 直连对端Terminate流程处理动作（DIRECTTERMINACT） | FAILOVER | 本端规划 | 配置UNC收到异常返回码后执行何种操作。 |
- 任务示例脚本（该命令行）：
  `ADD RESULTCODECTRL: PCCTEMPLATE="templatetest", INTFTYPE=INTFTYPE_GX, VENDORID=0, GXRESULTCODEVAL="3xxx", INITACTION=FAILOVER, UPDATEACTION=FAILOVER, TERMINACTION=FAILOVER;`
  `ADD RESULTCODECTRL: PCCTEMPLATE="templatetest", INTFTYPE=INTFTYPE_GX, VENDORID=0, GXRESULTCODEVAL="3xxx", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, DIRECTTERMINACT=FAILOVER;`
- 操作步骤上下文（±2 行原文）：
  L84:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 根据运营商规划配置GGSN/PGW-C收到各种结果码后执行何种操作。若不配置，GGSN/PGW-C使用系统默认处理方式。
    >       [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
    >     3. **可选：**配置GGSN/PGW-C收到直连对端返回码后执行何种操作。
    >       [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
  L86:
    >       [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
    >     3. **可选：**配置GGSN/PGW-C收到直连对端返回码后执行何种操作。
    >       [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
    >     4. **可选：**如果设置GGSN/PGW-C收到直连对端返回码后执行FAILOVERALL动作，可配置FAILOVERALL的持续时长，缺省使用默认值。
    >       [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
  L94:
    >   [**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)
    >   > **说明**
    >   > - 本命令优先级高于[**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)和[**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)。
    >   > - 由于配置[**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)将影响用户的控制策略，只有在取得了客户的书面认可后方可使用。
    >   > - GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L138:
    > **[LST UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/查询用户模板组和用户模板的绑定关系（LST UPBINDUPG）_09897232.md)**
    > 
    > **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**
    > 
    > **[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 已配置数据中获取 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 接口类型（INTFTYPE） | INTFTYPE_GX | 与对端协商 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 设备提供商标识（VENDORID） | 0 | 全网规划 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Gx返回码（GXRESULTCODEVAL） | 3004<br>3002<br>5012 | 与对端协商 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Initial流程处理动作（DIRECTINITACT） | FAILOVER | 本端规划 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Update流程处理动作（DIRECTUPDACT） | FAILOVER | 本端规划 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
- 任务示例脚本（该命令行）：
  `ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3004";`
  `ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3002";`
  `ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="5012";`
  `ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3004";`
  `ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3002";`
  `ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="5012";`
- 操作步骤上下文（±2 行原文）：
  L264:
    >       > **说明**
    >       > 具体结果码需要与对端PCRF/DRA确认。
    >       **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)** / **[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)**
    >       **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)**
    >     e. 增加PCC故障场景维持BYPASS状态码配置。
  L406:
    >           - 策略接口为Gx接口，直连组网
    >             ```
    >             ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3004";
    >             ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3002";
    >             ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="5012";
  L407:
    >             ```
    >             ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3004";
    >             ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3002";
    >             ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="5012";
    >             ```

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 已配置数据中获取 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 接口类型（INTFTYPE） | INTFTYPE_N7 | 与对端协商 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | N7返回码（N7RESULTCODEVAL） | 500<br>400<br>504 | 与对端协商 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 设备提供商标识（VENDORID） | 0 | 全网规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Initial流程处理动作（INITACTION） | FAILOVER<br>LOCALPCC | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Initial流程回滚后使能Holding-Time（INITHOLDTMSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Update流程处理动作（UPDATEACTION） | FAILOVER<br>INHERIT_PCC | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Update流程回滚后使能Holding-Time（UPDHOLDTMSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Initial流程处理动作（DIRECTINITACT） | FAILOVER | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Update流程处理动作（DIRECTUPDACT） | FAILOVER | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Initial流程回滚后使能Holding-Time（DIRECTINITHTSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Update流程回滚后使能Holding-Time（DIRECTUPDHTSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
  | **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Update流程回滚后使能Holding-Time（DIRECTUPDHTSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
- 任务示例脚本（该命令行）：
  `ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;`
  `ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;`
  `ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;`
  `ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;`
  `ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;`
  `ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;`
- 操作步骤上下文（±2 行原文）：
  L287:
    >       > **说明**
    >       > 具体结果码需要与对端PCF/SCP确认。
    >       **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)** / **[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)**
    >     g. **可选：**配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。
    >       > **说明**
  L445:
    > 
    >             ```
    >             ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;
    >             ```
    >             //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。
  L497:
    > 
    >             ```
    >             ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;
    >             ```
    >             //配置对端SCP回复指定结果码后SMF/PGW-C的处理操作。

## ④ 自动比对
- 命令真相参数（17）：['DIRECTINITACT', 'DIRECTINITHTSW', 'DIRECTREACTREQ', 'DIRECTTERMINACT', 'DIRECTUPDACT', 'DIRECTUPDHTSW', 'GXRESULTCODEVAL', 'INITACTION', 'INITHOLDTMSW', 'INTFTYPE', 'N7RESULTCODEVAL', 'PCCTEMPLATE', 'REACTREQ', 'TERMINACTION', 'UPDATEACTION', 'UPDHOLDTMSW', 'VENDORID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 3, '对端协商': 1, '本端规划': 19, '已配置数据中获取': 2, '与对端协商': 4}（多值→atom 应考虑 decision_driven）
