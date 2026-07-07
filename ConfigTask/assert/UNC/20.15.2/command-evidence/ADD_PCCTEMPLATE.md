# 命令证据包：ADD PCCTEMPLATE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加一个PCC模板配置。

当部署PCC业务时，希望不同的APN有不同的PCC配置，则可以通过该命令配置不同的PCC模板，以便于绑定到APN下，使得不同的APN可以有不同的PCC配置属性。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为100。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCCTEMPNAME | PCC模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写，不允许命名为“global”。 |
| REPORTLEVEL | 缺省上报级别 | 对端协商 | optional | RG | 枚举类型。 |
| METERMETHOD | 缺省离线计费统计方式 | 对端协商 | optional | VOLUME | 枚举类型。 |
| ORGHOSTCCAI | 基于CCA-I Origin-Host AVP触发PCRF重选 | 对端协商 | optional | DISABLE | 枚举类型。 |
| ORGHOSTCCAU | 基于CCA-U Origin-Host AVP触发PCRF重选 | 对端协商 | optional | DISABLE | 枚举类型。 |
| ORGHOSTRAR | 基于RAR Origin-Host AVP触发PCRF重选 | 对端协商 | optional | DISABLE | 枚举类型。 |
| SELPEERFAILACT | 选择PCF/PCRF失败动作 | local_planned | optional | INHERIT | 枚举类型。 |
| SELPEERLOCPCC | 选择PCF/PCRF失败回滚为Local PCC用户类型 | local_planned | conditional | LOCAL_PCC | 枚举类型。 |
| SELPEERRDSPCC | 选择PCF/PCRF失败回滚为RADIUS PCC用户类型 | local_planned | conditional | LOCAL_PCC | 枚举类型。 |
| INITIALFAILACT | Initial流程故障处理动作 | local_planned | optional | INHERIT | 枚举类型。 |
| INITFAILLOCPCC | Initial流程故障回滚为Local PCC用户类型 | local_planned | conditional | LOCAL_PCC | 枚举类型。 |
| INITFAILRDSPCC | Initial流程故障回滚为RADIUS PCC用户类型 | local_planned | conditional | LOCAL_PCC | 枚举类型。 |
| UPDATEFAILACT | Update流程故障处理动作 | local_planned | optional | INHERIT | 枚举类型。 |
| UPDFAILLOCPCC | Update流程故障回滚为Local PCC用户类型 | local_planned | conditional | LOCAL_PCC | 枚举类型。 |
| HOLDINGTIME | 用户回滚后在线保持时长（分钟） | local_planned | optional | 65535 | 整数类型，取值范围为0～1440，65535，单位是分钟。 |
| ADJUSTRANGE | 随机延迟范围（分钟） | local_planned | optional | 无 | 整数类型，取值范围为0～60，单位是分钟。 |
| LOCSLCTMODE | 本端主机名选择模式 | local_planned | optional | INHERIT | 枚举类型。 |
| LOCALHOSTNAME | 本端主机名 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～127。 |
| NTFRSRURI | 基于Notify消息ResourceURI触发PCF重选 | local_planned | optional | INHERIT | 枚举类型。 |
| N7FAILOVERSW | N7 Failover功能开关 | 对端协商 | optional | INHERIT | 枚举类型。 |
| PCFLBPARA | PCF负荷分担参数 | 对端协商 | optional | INHERIT | 枚举类型。 |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| USEN15PCFSW | 优先使用N15 PCF开关 | global_planned | optional | INHERIT | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**SET PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    > - [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 操作步骤上下文（±2 行原文）：
  L10:
    > ## [操作场景](#ZH-CN_OPI_0231422950)
    > 
    > 当用户初始激活或进行业务时，GGSN/PGW-C发送CCR请求消息给PCRF，在指定消息重传时间间隔时间内未收到PCRF的响应消息，即可判断PCRF服务器状态异常。如果 [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) 命令中 “FAILOVERSW” 参数值为 “ENABLE” ，则进行failover处理；否则按照 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令设置的动作进行处理。
    > 
    > GGSN/PGW-C向备PCRF重发消息，如果备PCRF也没有响应或者备PCRF因状态异常、消息发送速率超过wal值等导致不可用，可以根据 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令配置情况去活用户或者转为非PCC用户/本地PCC用户继续进行业务。
  L12:
    > 当用户初始激活或进行业务时，GGSN/PGW-C发送CCR请求消息给PCRF，在指定消息重传时间间隔时间内未收到PCRF的响应消息，即可判断PCRF服务器状态异常。如果 [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) 命令中 “FAILOVERSW” 参数值为 “ENABLE” ，则进行failover处理；否则按照 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令设置的动作进行处理。
    > 
    > GGSN/PGW-C向备PCRF重发消息，如果备PCRF也没有响应或者备PCRF因状态异常、消息发送速率超过wal值等导致不可用，可以根据 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令配置情况去活用户或者转为非PCC用户/本地PCC用户继续进行业务。
    > 
    > 实现failover功能需要具备以下几个条件：

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | PCC模板名称（PCCTEMPNAME） | pcctemplate_01 | 本端规划 | 基于APN配置PCC本端主机名选择模式。 |
  | [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | 本端主机名选择模式（LOCSLCTMODE） | UPFGRP | 固定取值 | 基于APN配置PCC本端主机名选择模式。 |
  | [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | UPF组与Diameter本端主机组的绑定关系组名称（UPFGLOCGBNDGNAME） | test | 已配置数据中获取 | 基于APN配置PCC本端主机名选择模式。 |
- 任务示例脚本（该命令行）：
  `ADD PCCTEMPLATE: PCCTEMPNAME="pcctemplate_01", LOCSLCTMODE=UPFGRP, UPFGLOCGBNDGNAME="test";`
- 操作步骤上下文（±2 行原文）：
  L167:
    >     - 基于APN设置PCC本端主机名选择模式。
    >           a. 增加PCC模板。
    >             [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >           b. 将PCC模板与APN绑定。
    >             [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
  L336:
    >   ```
    >   ```
    >   ADD PCCTEMPLATE: PCCTEMPNAME="pcctemplate_01", LOCSLCTMODE=UPFGRP, UPFGLOCGBNDGNAME="test";
    >   SET APNPCCFUNC: APN="apn-op", PCCTEMPLATE="pcctemplate_01";
    >   ```

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 操作步骤上下文（±2 行原文）：
  L125:
    >       > 号段信息为可选配置。APN下只允许配置一个不带号段信息的PcrfGroup。
    >     b. **可选：**添加PCC模板，配置在激活过程中根据PCRF返回的重定向指示重选PCRF；配置缺省REPORTLEVEL和缺省METERMETHOD，缺省使用默认值。
    >       [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >     c. 针对指定的APN配置PCC使能开关，并将PccTemplate绑定到APN下。
    >       [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)

**md：`WSFD-109101/配置异常场景数据_31422947.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | PCC模板名称（PCCTEMPNAME） | pcctemplate | 本端规划 | 基于APN控制GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式。 |
- 任务示例脚本（该命令行）：
  `ADD PCCTEMPLATE:PCCTEMPNAME="templatetest",SELPEERFAILACT=DEFAULT,INITIALFAILACT=ROLLBACK,INITFAILRDSPCC=LOCAL_PCC,UPDATEFAILACT=ROLLBACK,UPDFAILLOCPCC=LOCAL_PCC;`
- 操作步骤上下文（±2 行原文）：
  L78:
    >       [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    >     4. 配置PCC Template中GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式以及PCC用户回滚后的在线保持时长。若不配置，GGSN/PGW-C默认继承全局配置。
    >       [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >     5. 当基于APN粒度设置GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式，需要将PCCTEMPLATE绑定到APN下。
    >       [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
  L117:
    >   ```
    >   ```
    >   ADD PCCTEMPLATE:PCCTEMPNAME="templatetest",SELPEERFAILACT=DEFAULT,INITIALFAILACT=ROLLBACK,INITFAILRDSPCC=LOCAL_PCC,UPDATEFAILACT=ROLLBACK,UPDFAILLOCPCC=LOCAL_PCC;
    >   ```
    >   ```

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | PCC模板名称（PCCTEMPNAME） | pcctemplate | 本端规划 | 配置PCC模板，将PCC模板配置为本地PCC。 |
  | [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | Initial流程故障处理动作（INITIALFAILACT） | FORBIDDEN | 本端规划 | 配置PCC模板，将PCC模板配置为本地PCC。 |
  | [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | Update流程故障处理动作（UPDATEFAILACT） | INHERIT | 本端规划 | 配置PCC模板，将PCC模板配置为本地PCC。 |
- 任务示例脚本（该命令行）：
  `ADD PCCTEMPLATE:PCCTEMPNAME="pcctemplate",INITIALFAILACT=FORBIDDEN,UPDATEFAILACT=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L81:
    > 4. 开启APN下的PCC开关。
    >     a. 配置PCC模板。
    >       [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >     b. 针对指定的APN配置PCC使能开关和PCC模板。
    >       [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
  L135:
    > 3. 配置指定APN的PCC开关。
    >   ```
    >   ADD PCCTEMPLATE:PCCTEMPNAME="pcctemplate",INITIALFAILACT=FORBIDDEN,UPDATEFAILACT=INHERIT;
    >   ```
    >   ```

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | PCC模板名称（PCCTEMPNAME） | pcctemplate | 本端规划 | 配置PCC模板，将PCC模板配置为本地PCC或动态PCC。 |
  | [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | 选择PCRF/PCF失败动作（SELPEERFAILACT） | DEFAULT | 本端规划 | 配置PCC模板，将PCC模板配置为本地PCC或动态PCC。 |
  | [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | Initial流程故障处理动作（INITIALFAILACT） | FORBIDDEN | 本端规划 | 配置PCC模板，将PCC模板配置为本地PCC或动态PCC。 |
  | [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | Update流程故障处理动作（UPDATEFAILACT） | INHERIT | 本端规划 | 配置PCC模板，将PCC模板配置为本地PCC或动态PCC。 |
  | [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | NTFRSRURI（基于Notify消息ResourceURI触发PCF重选） | ENABLE | 与对端协商 | PCF1故障，PCF2通过原来的会话向SMF发送携带PCF2的ResourceURI的UpdateNotify/TerminateNotify消息，期望SMF后续将会话消息发送给PCF2的容灾场景，需要将该参数设置为<br>“ENABLE”<br>。设置为ENABLE后，SMF收到UpdateNotify/TerminateNotify携带的ResourceURI时，SMF将会话的后续消息向ResourceURI对应的PCF发送。<br>该开关支持APN粒度（<br>[**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>）和全局粒度（<br>[**SET N7RCVATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/N7接收分发控制/设置N7接收信元处理控制（SET N7RCVATTRCTRL）_09653677.md)<br>），请根据实际PCF能力规划。 |
  | [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | N7FAILOVERSW（N7 Failover功能开关） | ENABLE | 与对端协商 | PCF采用主备容灾组网时，设置为<br>“ENABLE”<br>。PCF故障，如没有可用的备PCF时，设置为<br>“DISABLE”<br>。<br>该开关支持APN粒度（<br>[**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>）和全局粒度（<br>[**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>），请根据实际PCF能力规划。 |
  | [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) | PCF负荷分担参数（PCFLBPARA） | GROUPID | 与对端协商 | 此处以基于GROUPID实现负荷分担为例。<br>- 支持PCF主备容灾且“PCF负荷分担参数（PCFLBPARA）”取值为“GROUPID”时，SMF要求主备PCF的GroupID必须相同。<br>- 支持PCF主备容灾且“PCF负荷分担参数（PCFLBPARA）”取值为“PRIORITY”时，SMF要求主备PCF的PRIORITY必须不同。 |
- 任务示例脚本（该命令行）：
  `ADD PCCTEMPLATE:PCCTEMPNAME="pcctemplate",SELPEERFAILACT=DEFAULT,INITIALFAILACT=FORBIDDEN,UPDATEFAILACT=INHERIT,NTFRSRURI=ENABLE,N7FAILOVERSW=ENABLE,PCFLBPARA=GROUPID;`
  `ADD PCCTEMPLATE:PCCTEMPNAME="pcctemplate",SELPEERFAILACT=DEFAULT,INITIALFAILACT=FORBIDDEN,UPDATEFAILACT=INHERIT,NTFRSRURI=ENABLE,N7FAILOVERSW=ENABLE,PCFLBPARA=PRIORITY;`
- 操作步骤上下文（±2 行原文）：
  L165:
    >     10. 开启DNN下的PCC开关，将PCC模板绑定到DNN上。如果有多个DNN，则可以多次执行本步配置。
    >           a. 配置PCC模板，将PCC模板配置为本地PCC或动态PCC。
    >             [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >           b. 针对指定的DNN配置PCC使能开关，绑定PCC模板。
    >             [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
  L245:
    > 
    > ```
    > ADD PCCTEMPLATE:PCCTEMPNAME="pcctemplate",SELPEERFAILACT=DEFAULT,INITIALFAILACT=FORBIDDEN,UPDATEFAILACT=INHERIT,NTFRSRURI=ENABLE,N7FAILOVERSW=ENABLE,PCFLBPARA=GROUPID;
    > SET APNPCCFUNC:APN="huawei.com",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,PCCTEMPLATE="pcctemplate";
    > ```
  L349:
    > 
    > ```
    > ADD PCCTEMPLATE:PCCTEMPNAME="pcctemplate",SELPEERFAILACT=DEFAULT,INITIALFAILACT=FORBIDDEN,UPDATEFAILACT=INHERIT,NTFRSRURI=ENABLE,N7FAILOVERSW=ENABLE,PCFLBPARA=PRIORITY;
    > SET APNPCCFUNC:APN="apn-test1",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,PCCTEMPLATE="pcctemplate";
    > ```

**md：`WSFD-109101/相关概念_71770360.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > | SM策略（会话管理策略） | PCC规则 | 与一个或一组SDF相关的信息，如用于检测SDF的SDF模板及相应的QoS、时间/流量上报、计费方式等策略和计费参数。<br>说明：SDF（Service Data Flow，业务流）<br>指与用户使用的业务关联的一组IP流，比如用户浏览一个网页时，从该网站发送到UE的下行IP数据包流即为一个SDF。 | 用于进行SDF粒度的策略控制。 |
    > 
    > 在UNC上，可以通过 **[**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** 命令配置本地策略，还可以通过 **[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** 配置指定DNN的本地策略。
    > 
    > #### [会话规则和PCC规则](#ZH-CN_CONCEPT_0171770360)

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L72:
    > **[RST PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/复位PCC定时器/复位PCC定时器（RST PCCTIMER）_09897075.md)**
    > 
    > [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > 
    > **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**

**md：`WSFD-201207/实现原理（N7接口）_85304236.md`**
- 操作步骤上下文（±2 行原文）：
  L76:
    >   | 备SCP回复如下结果码和Protocol or application Error组合：<br>- 500 NF_SERVICE_FAILOVER<br>- 504 TARGET_NF_NOT_REACHABLE<br>- 502 NF_DISCOVERY_ERROR<br>- 502 MAX_SCP_HOPS_REACHED | - **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**命令对应N7返回码的“Initial流程处理动作（INITACTION）”参数值为“FAILOVER”<br>- 用户使用的PCC模板（**[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**）中的“N7 Failover功能开关（N7FAILOVERSW）”参数值为“ENABLE” | 会话回滚为本地PCC会话，使用本地配置的规则，进入PCF Bypass状态。<br>如果<br>**[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**<br>或者<br>**[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**<br>配置了Holding Time参数，SMF根据软参<br>[DWORD519 Bit9](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD519 Bit9控制激活流程查询PCF失败发生回滚时，HoldingTime功能是否生效_97903713.md)<br>配置决定是否启动Holding Time定时器。 |
    >   | 备SCP回复其它异常结果码 | - **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)**命令对应的N7返回码和故障码对应的Protocol or application Error信息组合的“Initial流程处理动作（INITACTION）”参数值为“FAILOVER”<br>- **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**命令的“SCP故障重选开关（SCPFAILOVERSW）”参数值为“SCP_FAILOVER”<br>- **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)**命令的“无语音专载时的故障非预期Bypass场景的异常处理动作（ACTNODEDBEARER）”参数值为“TERMINATE” | 会话激活失败。 |
    >   **步骤** **7** ：如果SMF将用户回滚为本地PCC用户，标识用户进入PCF Bypass状态。如果 **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** 或者 **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** 配置了Holding Time参数，SMF根据软参 [DWORD519 Bit9](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD519 Bit9控制激活流程查询PCF失败发生回滚时，HoldingTime功能是否生效_97903713.md) 配置决定是否启动Holding Time定时器。
    >   **步骤** **8** ：SMF选择UPF。
    >   **步骤** **9-10** ：SMF给UPF发送PFCP Session Establishment Request消息请求建立新的PFCP会话上下文，提供用于该PDU会话的数据监测，CN隧道信息，用于语音专有QoS Flow\专有承载创建的静态PCC策略等。
  L124:
    >   | 备SCP回复如下结果码和Protocol or application Error组合：<br>- 500 NF_SERVICE_FAILOVER<br>- 504 TARGET_NF_NOT_REACHABLE<br>- 502 NF_DISCOVERY_ERROR<br>- 502 MAX_SCP_HOPS_REACHED | **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)**<br>命令对应的N7返回码和故障码对应的Protocol or application Error信息组合的<br>“Update流程处理动作（UPDATEACTION）”<br>参数值为<br>“INHERIT_PCC”<br>，并且<br>“Update流程回滚后使能Holding-Time（UPDHOLDTMSW）”<br>参数值为<br>“ENABLE” | 会话回滚为本地PCC会话，继续使用PCF下发的规则，会话进入PCF Bypass状态。<br>如果<br>**[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**<br>或者<br>**[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**<br>配置了Holding Time参数，SMF启动Holding Time定时器。 |
    >   | 备SCP回复其它异常结果码 | - **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)**命令对应的N7返回码和故障码对应的Protocol or application Error信息组合的“Update流程处理动作（UPDATEACTION）”参数值为“FAILOVER”<br>- **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**命令的“SCP故障重选开关（SCPFAILOVERSW）”参数值为“SCP_FAILOVER”<br>- **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)**命令的“无语音专载时的故障非预期Bypass场景的异常处理动作（ACTNODEDBEARER）”参数值为“TERMINATE”，“存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作（ACTWITDEDBEARER）”参数值为“FASTROLLBACK”，并且“存在语音专载时更新流程故障回滚为Local PCC用户类型（FAILLOCPCC）”参数值为“INHERIT_PCC” | 当用户存在语音会话时，当前会话回滚为本地PCC会话，继续使用PCF下发的规则，会话进入PCF Bypass状态。<br>如果<br>**[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**<br>配置了用户快速回滚后在线保持时长参数，SMF启动Holding Time定时器。<br>当用户不存在语音会话时，去激活当前会话。 |
    >   **步骤** **4** ：如果SMF将用户回滚为本地PCC用户，标识用户进入PCF Bypass状态。如果 **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** 或者 **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** 配置了Holding Time参数，启动Holding Time定时器。
    >   **步骤** **5** ：SMF发送Nsmf_PDUSession_UpdateSmContext Response给AMF。
    >   **步骤** **6** ：（可选）QoS改变需要通知(R)AN侧时，进行该流程，(R)AN侧接受策略修改。
  L127:
    >   **步骤** **5** ：SMF发送Nsmf_PDUSession_UpdateSmContext Response给AMF。
    >   **步骤** **6** ：（可选）QoS改变需要通知(R)AN侧时，进行该流程，(R)AN侧接受策略修改。
    >   **步骤** **7-8** ：（可选）QoS参数修改涉及UPF侧修改时，SMF将更新的QoS信息通知UPF，根据 **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** 和 **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** 中 “Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC）” 参数值决定是否使用激活时安装的PCC策略：值为 “LOCAL_PCC” 时，通知UPF删除激活时安装的动态PCC策略，安装本地配置的静态PCC策略（用于语音专有QoS Flow\专有承载创建的静态PCC策略）；值为 “INHERIT_PCC” 时，继续使用激活时安装的PCC策略。
    >   **步骤** **9** ：（可选）QoS改变需要通知UE侧时，进行该流程，UE侧接受策略修改。
    > 

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | PCC模板名称（PCCTEMPNAME） | pcctemplate | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | INHERIT_PCC | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 用户回滚后在线保持时长（分钟）（HOLDINGTIME） | 30 | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 随机延迟范围（分钟）（ADJUSTRANGE） | 10 | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
- 操作步骤上下文（±2 行原文）：
  L259:
    >     c. 基于PCC模板配置故障处理动作、failover开关和Holding Time。
    >       > **说明**
    >       > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。
    >       [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) / **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**
    >     d. 配置对端PCRF/DRA回复指定结果码后PGW-C的处理操作。
  L260:
    >       > **说明**
    >       > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。
    >       [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) / **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**
    >     d. 配置对端PCRF/DRA回复指定结果码后PGW-C的处理操作。
    >       > **说明**
  L395:
    > 
    >       > **说明**
    >       > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。
    > 
    >       ```

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | PCC模板名称（PCCTEMPNAME） | pcctemplate | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | INHERIT_PCC | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 用户回滚后在线保持时长（分钟）（HOLDINGTIME） | 30 | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 随机延迟范围（分钟）（ADJUSTRANGE） | 10 | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
  | [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | N7 Failover功能开关（N7FAILOVERSW） | ENABLE | 与对端协商 | 策略接口使用N7接口且PCF采用主备容灾组网时，设置为<br>“ENABLE”<br>。<br>该开关支持APN粒度（<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>）和全局粒度（<br>[**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>），请根据实际PCF能力规划。 |
- 操作步骤上下文（±2 行原文）：
  L280:
    >     d. 基于PCC模板配置故障处理动作、failover开关和Holding Time。
    >       > **说明**
    >       > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。
    >       [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) / **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**
    >     e. 为语音业务绑定PCC模板，配置PCF状态过滤参数。
  L281:
    >       > **说明**
    >       > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。
    >       [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) / **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**
    >     e. 为语音业务绑定PCC模板，配置PCF状态过滤参数。
    >       [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
  L429:
    > 
    >             > **说明**
    >             > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。
    > 
    >             ```

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)**
    > - **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
    > - **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**
    > - **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
    > - **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** | PCC模板名称（PCCTEMPNAME） | test_template | 本端规划 | 配置由DRA或PCRF触发的PCRF重选和PCRF倒换。 |
  | **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** | 基于CCA-I Origin-Host AVP触发PCRF重选（ORGHOSTCCAI） | ENABLE | 全网规划 | 配置由DRA或PCRF触发的PCRF重选和PCRF倒换。 |
  | **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** | 基于CCA-U Origin-Host AVP触发PCRF重选（ORGHOSTCCAU） | ENABLE | 全网规划 | 配置由DRA或PCRF触发的PCRF重选和PCRF倒换。 |
  | **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** | 基于RAR Origin-Host AVP触发PCRF重选（ORGHOSTRAR） | ENABLE | 全网规划 | 配置由DRA或PCRF触发的PCRF重选和PCRF倒换。 |
- 任务示例脚本（该命令行）：
  `ADD PCCTEMPLATE:PCCTEMPNAME="test_template",ORGHOSTCCAI=ENABLE,ORGHOSTCCAU=ENABLE,ORGHOSTRAR=ENABLE;`
  `ADD PCCTEMPLATE:PCCTEMPNAME="test_template",ORGHOSTCCAI=ENABLE,ORGHOSTCCAU=ENABLE,ORGHOSTRAR=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L171:
    > 10. 配置激活和更新流程中，网关是否支持由DRA或PCRF触发的PCRF重选和PCRF倒换，并将PCC Template绑定到APN下。
    >     a. 配置PCC模板。
    >       **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**
    >     b. 配置APN。
    >       **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
  L260:
    >   //配置激活和更新流程中，网关支持由DRA或PCRF触发的PCRF重选和PCRF倒换，并将PCC Template绑定到APN下。
    >   ```
    >   ADD PCCTEMPLATE:PCCTEMPNAME="test_template",ORGHOSTCCAI=ENABLE,ORGHOSTCCAU=ENABLE,ORGHOSTRAR=ENABLE;
    >   ```
    >   ```
  L378:
    >   //配置激活和更新流程中，网关支持由DRA或PCRF触发的PCRF重选和PCRF倒换，并将PCC Template绑定到APN下。
    >   ```
    >   ADD PCCTEMPLATE:PCCTEMPNAME="test_template",ORGHOSTCCAI=ENABLE,ORGHOSTCCAU=ENABLE,ORGHOSTRAR=ENABLE;
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（23）：['ADJUSTRANGE', 'HOLDINGTIME', 'INITFAILLOCPCC', 'INITFAILRDSPCC', 'INITIALFAILACT', 'LOCALHOSTNAME', 'LOCSLCTMODE', 'METERMETHOD', 'N7FAILOVERSW', 'NTFRSRURI', 'ORGHOSTCCAI', 'ORGHOSTCCAU', 'ORGHOSTRAR', 'PCCTEMPNAME', 'PCFLBPARA', 'REPORTLEVEL', 'SELPEERFAILACT', 'SELPEERLOCPCC', 'SELPEERRDSPCC', 'UPDATEFAILACT', 'UPDFAILLOCPCC', 'UPFGLOCGBNDGNAME', 'USEN15PCFSW']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 24, '固定取值': 1, '已配置数据中获取': 1, '与对端协商': 4, '全网规划': 3}（多值→atom 应考虑 decision_driven）
