# 命令证据包：SET FHBYPASS
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

![](设置失败旁路处理（SET FHBYPASS）_09896714.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该命令仅用于紧急情况下的故障恢复，执行该命令可能会导致一定的计费误差，请谨慎使用。执行该命令将改变失败处理的原则，请确认已经进行了必要的预检查，并已获得了执行该命令的权限。

该命令用来配置当
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 当设置Radius鉴权使能时，用户鉴权失败仍然可以激活，需要保证本地配置的地址分配方式不能是Radius分配，且本地有可用的地址池资源，否则会导致用户激活失败。
- 当设置在线计费使能时，需要根据计费中心的能力确认是否使能话单中记录failureHandlingContinue标识，否则可能导致计费损失。
- 当设置策略与计费控制使能时，

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| ONLCHARGE | 在线计费 | local_planned | optional | 无 | 枚举类型。 |
| GYERRRC | Gy异常结果码 | local_planned | conditional | 无 | 枚举类型。 |
| CCFHOFFLINE | 话单中记录failureHandlingContinue标识 | local_planned | conditional | 无 | 枚举类型。 |
| PCC | 策略与计费控制 | local_planned | optional | 无 | 枚举类型。 |
| GXERRRC | Gx异常结果码 | local_planned | conditional | 无 | 枚举类型。 |
| RDSAUTH | Radius鉴权 | local_planned | optional | 无 | 枚举类型。 |
| RDSACCT | Radius计费 | local_planned | optional | 无 | 枚举类型。 |
| HOLDINGTIME | 用户保持时长（分钟） | local_planned | optional | 无 | 整数类型，取值范围为0～1440，单位是分钟。 |
| RANGETIME | 用户保持调整时长（分钟） | local_planned | optional | 无 | 整数类型，取值范围为1～60，单位是分钟。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > - [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)
    > - [**ADD RESULTCODECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
    > - [**SET FHBYPASS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > - [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)

**md：`WSFD-109101/实现原理_29056158.md`**
- 操作步骤上下文（±2 行原文）：
  L127:
    > | N4接口响应超时或返回异常返回码 | UNC<br>发送PFCP Session Modification Request消息给GGSN-U/PGW-U，GGSN-U/PGW-U响应超时或者返回异常响应，或者GGSN-U/PGW-U发送PFCP Session Report Request消息给<br>UNC<br>，响应超时或者返回异常响应。 | 如果<br>UNC<br>发起消息，GGSN-U/PGW-U无响应或返回异常返回码，则<br>UNC<br>通过PFCP Session Deletion Request消息向GGSN-U/PGW-U发起去活请求。<br>如果GGSN-U/PGW-U发起消息，<br>UNC<br>无响应或返回异常返回码，则GGSN-U/PGW-U通过PFCP Session Report Request消息向<br>UNC<br>发起去活请求。 |
    > 
    > 在等待PCRF响应超时、Gx接口链路故障、CCA消息中携带异常返回码故障场景下， UNC 支持根据 [**SET FHBYPASS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md) 的配置改变异常处理策略。该命令仅用于故障场景下的紧急处理，优先级高于 [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 、 [**ADD RESULTCODECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md) 的配置。由于该命令的配置将影响用户的控制策略，只有在获得了客户的书面认可后方可使用。
    > 
    > > **说明**

**md：`WSFD-109101/配置异常场景数据_31422947.md`**
- 操作步骤上下文（±2 行原文）：
  L92:
    >       > GGSN/PGW-C根据指定返回码对所有用户执行failover动作后，已在线和新激活的用户使用备PCRF进行交互。当Failover All-sessions定时器到达后，如果主PCRF可用，新激活用户将使用主PCRF进行交互，已在线用户仍使用备PCRF进行交互，否则均使用备PCRF进行交互。
    > - 进入 “MML命令行-UNC” 窗口。 故障场景紧急处理：配置等待PCRF响应超时、Gx接口链路故障、CCA消息中携带异常返回码时的一键放通功能。
    >   [**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)
    >   > **说明**
    >   > - 本命令优先级高于[**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)和[**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)。
  L95:
    >   > **说明**
    >   > - 本命令优先级高于[**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)和[**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)。
    >   > - 由于配置[**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)将影响用户的控制策略，只有在取得了客户的书面认可后方可使用。
    >   > - GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。
    >   >     - 方式1：通过[**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)“HOLDINGTIME”控制对放通用户的后续处理。
  L97:
    >   > - 由于配置[**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)将影响用户的控制策略，只有在取得了客户的书面认可后方可使用。
    >   > - GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。
    >   >     - 方式1：通过[**SET FHBYPASS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)“HOLDINGTIME”控制对放通用户的后续处理。
    >   >     - 方式2：通过[**DSP CPPDPCHGINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费维护/用户计费信息/查询计费上下文信息（DSP CPPDPCHGINFO）_09897010.md)查询被放通用户的归属信息。
    > 

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - **[SET APNAUTHATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN鉴权属性/设置APN鉴权属性配置（SET APNAUTHATTR）_28567656.md)**
    > - **[SET APNRDSACCTCTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS计费管理/APN计费控制/设置APN RADIUS计费控制参数（SET APNRDSACCTCTRL）_09896770.md)**
    > - **[SET FHBYPASS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)**
    > - **[SET RDSRSPADDRCHK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/RADIUS响应消息地址检查/设置全局RADIUS响应消息源IP_端口检查配置（SET RDSRSPADDRCHK）_09896744.md)**
    > - [**ADD UPLIST4RDS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)

**md：`WSFD-011306/配置RADIUS功能_32909765.md`**
- 操作步骤上下文（±2 行原文）：
  L135:
    >       > - 域名做为后缀时，用户名+后缀分隔符+域名（后缀分隔符由**[**SET DOMAINSEPARATOR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/域名分隔符/设置域名前后缀分隔符（SET DOMAINSEPARATOR）_09654169.md)**命令配置）。
    > 7. **可选：****故障场景紧急处理：** 配置RADIUS鉴权超时无响应或计费AAA服务器无响应时的一键放通功能。
    >   **[SET FHBYPASS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)**
    >   > **说明**
    >   > - 本命令优先级高于**[SET APNAUTHATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN鉴权属性/设置APN鉴权属性配置（SET APNAUTHATTR）_28567656.md)**的**“AAANORSPCTRL”**和**[SET APNRDSACCTCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS计费管理/APN计费控制/设置APN RADIUS计费控制参数（SET APNRDSACCTCTRL）_09896770.md)**的**“****DEACTIVE”**。
  L138:
    >   > **说明**
    >   > - 本命令优先级高于**[SET APNAUTHATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN鉴权属性/设置APN鉴权属性配置（SET APNAUTHATTR）_28567656.md)**的**“AAANORSPCTRL”**和**[SET APNRDSACCTCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS计费管理/APN计费控制/设置APN RADIUS计费控制参数（SET APNRDSACCTCTRL）_09896770.md)**的**“****DEACTIVE”**。
    >   > - 由于配置**[SET FHBYPASS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)**将影响用户的激活状态，只有在取得了客户的书面认可后方可使用。
    >   > - 通过**[SET FHBYPASS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)**“HOLDINGTIME”控制故障恢复后对放通用户的后续处理，即永久在线或去激活。
    > 8. **可选：** 配置Specific APN。
  L139:
    >   > - 本命令优先级高于**[SET APNAUTHATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN鉴权属性/设置APN鉴权属性配置（SET APNAUTHATTR）_28567656.md)**的**“AAANORSPCTRL”**和**[SET APNRDSACCTCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS计费管理/APN计费控制/设置APN RADIUS计费控制参数（SET APNRDSACCTCTRL）_09896770.md)**的**“****DEACTIVE”**。
    >   > - 由于配置**[SET FHBYPASS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)**将影响用户的激活状态，只有在取得了客户的书面认可后方可使用。
    >   > - 通过**[SET FHBYPASS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)**“HOLDINGTIME”控制故障恢复后对放通用户的后续处理，即永久在线或去激活。
    > 8. **可选：** 配置Specific APN。
    >   [**ADD SPECIFICAPNVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md)

### WSFD-109001

**md：`WSFD-109001/配置DCC处理动作_95923447.md`**
- 任务示例脚本（该命令行）：
  `SET FHBYPASS: ONLCHARGE=ENABLE, GYERRRC=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L133:
    >   **SET TWTIMER**
    > - 故障场景紧急处理：配置OCS故障（非异常结果码场景）或收到command层异常结果码时的Gy接口的一键放通功能。
    >   **SET FHBYPASS**
    >   > **说明**
    >   > - 由于配置**SET FHBYPASS**将影响用户的计费方式，只有在取得了客户的书面认可后方可使用。
  L135:
    >   **SET FHBYPASS**
    >   > **说明**
    >   > - 由于配置**SET FHBYPASS**将影响用户的计费方式，只有在取得了客户的书面认可后方可使用。
    >   > - **SET FHBYPASS**优先级高于DCC全局模板或DCC模板下的**SET OCSDOWNACTION**、**SET CMDLEVDFTBEH**、**ADD CMDRCACT**。
    >   > - GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。
  L136:
    >   > **说明**
    >   > - 由于配置**SET FHBYPASS**将影响用户的计费方式，只有在取得了客户的书面认可后方可使用。
    >   > - **SET FHBYPASS**优先级高于DCC全局模板或DCC模板下的**SET OCSDOWNACTION**、**SET CMDLEVDFTBEH**、**ADD CMDRCACT**。
    >   > - GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。
    >   >     - 方式1：通过**SET FHBYPASS**命令“HOLDINGTIME”控制对放通用户的后续处理，即是否转离线。

## ④ 自动比对
- 命令真相参数（9）：['CCFHOFFLINE', 'GXERRRC', 'GYERRRC', 'HOLDINGTIME', 'ONLCHARGE', 'PCC', 'RANGETIME', 'RDSACCT', 'RDSAUTH']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
