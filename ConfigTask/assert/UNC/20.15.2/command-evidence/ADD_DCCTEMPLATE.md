# 命令证据包：ADD DCCTEMPLATE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md`
> 用该命令的特性数：10

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于新增DCC在线计费模板，用于配置在线计费相关属性。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为101。
- 该命令的CCRSPESMFLAG、EVENTCHGMOD、QHTEXPIREDRSU和BLKFREESRV参数只有在DCC模板的默认值名称为GLOBAL时生效。
- 该命令的SERIALCCR、LOCSLCTMODE、SERVICETRIGGER、BLKFREESRV和LOCALHOSTNAME参数值配置后只对新上线的用户生效。
- 

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| DCCTMPLTNAME | DCC模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。 |
| PRIOCSGRPNAME | 主OCS组名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| SECOCSGRPNAME | 备OCS组名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| SERVICECONTEXT | Service-Context-Id值 | 对端协商 | optional | 32251@3gpp.org | 字符串类型，输入长度范围为1～63。 |
| DICTNO | 字典序号 | local_planned | optional | 1 | 整数类型，取值范围为1～2。 |
| SPECIFICATION | DCCA规范 | local_planned | optional | INHERIT | 枚举类型。 |
| QCT | 配额空耗时间门限值（秒） | local_planned | optional | 4294967295 | 整数类型，取值范围为0，5～200，4294967295，单位是秒。 |
| QHT | 配额空闲时间门限值（秒） | local_planned | optional | 4294967295 | 整数类型，取值范围为0，5～3600，4294967295，单位是秒。 |
| VQT | 流量阈值触发百分比（%） | local_planned | optional | 4294967295 | 整数类型，取值范围为0～50，4294967295，单位是百分比。 |
| TQT | 时间阈值触发百分比（%） | local_planned | optional | 4294967295 | 整数类型，取值范围为0～50，4294967295，单位是百分比。 |
| UQT | 事件阈值触发百分比（%） | local_planned | optional | 4294967295 | 整数类型，取值范围为0～50，4294967295，单位是百分比。 |
| TRTIMER | Tr定时器时长（秒） | local_planned | optional | 4294967295 | 整数类型，取值范围为11～40，4294967295，单位是秒。 |
| CCRINITRGNUM | 指定CCR-I消息中携带RG的个数 | local_planned | optional | 4294967295 | 整数类型，取值范围为0～10，4294967295。 |
| MAXBTI | 最大BTI（秒） | local_planned | optional | 4294967295 | 整数类型，取值范围为0～3600，4294967295。 |
| VALIDTIME | 在线配额有效时长（分） | local_planned | optional | 4294967295 | 整数类型，取值范围为0，5～1440，4294967295，单位是分钟。 |
| CCRTARIFFSW | CCR携带费率切换点信元开关 | local_planned | optional | INHERIT | 枚举类型。 |
| CCFH | CCFH处理动作 | local_planned | optional | INHERIT | 枚举类型。 |
| RATTRIGGER | Rat变化触发使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| SGSNTRIGGER | SGSN变化触发使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| QOSTRIGGER | QoS变化触发使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| ULITRIGGER | ULI变化触发使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| MCCTRIGGER | MCC变化触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| MNCTRIGGER | MNC变化触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| LACTRIGGER | LAC变化触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| UETZTRIGGER | UE TimeZone改变触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| PRIVATEATTR | 私有属性使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| QUOTATOTAL | 是否携带累加流量信息 | local_planned | optional | INHERIT | 枚举类型。 |
| CCFHOFFLINE | CCFH离线标志位使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| AUTOFAILBACK | failback使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| RARNORGACTION | RAR消息RG上报方式 | local_planned | optional | INHERIT | 枚举类型。 |
| CCRPRECISIONTS | CCR携带高精度时间戳标记 | local_planned | optional | INHERIT | 枚举类型。 |
| MAXENVELOPE | 触发CCR的最大信封数 | local_planned | optional | 4294967295 | 整数类型，取值范围为0～10，4294967295。 |
| FAILOVERSUP | 支持failover使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| DDFH | DDFH处理动作 | local_planned | optional | INHERIT | 枚举类型。 |
| OCSCHANGECCAI | CCA-I触发OCS变化 | local_planned | optional | INHERIT | 枚举类型。 |
| OCSCHANGECCAU | CCA-U触发OCS变化 | local_planned | optional | INHERIT | 枚举类型。 |
| OCSCHANGERAR | RAR触发OCS变化 | local_planned | optional | INHERIT | 枚举类型。 |
| MSCCCARRYTYPE | MSCC携带方式 | local_planned | optional | INHERIT | 枚举类型。 |
| EVENTCHGMOD | 事件计费方式 | local_planned | optional | INHERIT | 枚举类型。 |
| CCRSPESMFLAG | CCR消息携带3GPP specific AVPs的M标志 | local_planned | optional | INHERIT | 枚举类型。 |
| EVENTCHGCCC | 事件计费信用控制关闭动作 | local_planned | optional | INHERIT | 枚举类型。 |
| FUATERMINATE | 最终配额动作指示终结方式 | local_planned | optional | INHERIT | 枚举类型。 |
| QHTEXPIREDRSU | QHT超时触发的CCR消息MSCC中是否携带RSU | local_planned | optional | INHERIT | 枚举类型。 |
| BLKFREESRV | Command层异常返回码动作为Block时阻塞免费业务 | local_planned | optional | PASS | 枚举类型。 |
| ONLCHGRECOVER | 在线计费自动恢复功能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| RECOVERINTERVAL | 在线计费自动恢复间隔 （分钟） | local_planned | conditional | 5 | 整数类型，取值范围为1～60，单位是分钟。 |
| TACTRIGGER | TA改变触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| ECGITRIGGER | ECGI改变触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| SERIALCCR | 串行发送CCR | global_planned | optional | INHERIT | 枚举类型。 |
| NOQUOTATRIGGER | 无配额更新开关 | local_planned | optional | INHERIT | 枚举类型。 |
| RACTRIGGER | RAC改变触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| CELLIDTRIGGER | CellID改变触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| LOCSLCTMODE | 在线计费本端主机名选择模式 | local_planned | optional | INHERIT | 枚举类型。 |
| LOCALHOSTNAME | 在线计费本端主机名 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～127。 |
| SERVICETRIGGER | 业务触发请求使能开关 | local_planned | optional | INHERIT | 枚举类型。 |
| ENBTRIGGER | eNodeB变化触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| SESSIONMODE | Gy会话模式 | global_planned | optional | INHERIT | 枚举类型。 |
| SPRATETRIGGER | 服务PLMN控制速率改变触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| APNRATETRIGGER | APN控制速率改变触发重授权开关 | local_planned | optional | INHERIT | 枚举类型。 |
| PDPTYPE4NONIP | None IP用户的PDP类型 | local_planned | optional | INHERIT | 枚举类型。 |
| BLOCKTIMER | 阻塞去活时间 | local_planned | optional | 0 | 整数类型，取值范围为0～1440，单位是分钟。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-216104

**md：`WSFD-216104/WSFD-216104 基于APN的eMTC终端接入速率控制参考信息_75993426.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET APNRATECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md)
    > - [**LST APNRATECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/查询APN速率控制配置（LST APNRATECTRL）_64343877.md)
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**MOD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
    > - [**RMV DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)

**md：`WSFD-216104/激活基于APN的eMTC终端接入速率控制_77396887.md`**
- 操作步骤上下文（±2 行原文）：
  L41:
    >   [**SET APNRATECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md)
    > 4. **可选：**配置APN Rate Control改变时发送CCR消息。
    >   [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > 5. **可选：**配置CDR话单中携带APN Rate Control字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)

### WSFD-216105

**md：`WSFD-216105/WSFD-216105 基于服务PLMN的eMTC终端接入速率控制参考信息_75993431.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET APNPLMNRATECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/设置APN Serving PLMN速率控制配置（SET APNPLMNRATECTRL）_64343912.md)
    > - [**LST APNPLMNRATECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/查询APN Serving PLMN速率控制配置（LST APNPLMNRATECTRL）_64343876.md)
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**MOD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
    > - [**RMV DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)

**md：`WSFD-216105/激活基于服务PLMN的eMTC终端接入速率控制_77396889.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    >       [**SET PLMNRATECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/Serving PLMN速率控制配置/设置Serving PLMN速率控制配置（SET PLMNRATECTRL）_64343918.md)
    > 4. **可选：**配置Serving PLMN Rate Control改变时发送CCR消息。
    >   [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > 5. **可选：**配置CDR话单中携带Serving PLMN Rate Control字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)

### WSFD-215204

**md：`WSFD-215204/WSFD-215204 基于APN的NB-IoT终端接入速率控制参考信息（PGW-C）_77673131.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md)
    > - [**LST APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/查询APN速率控制配置（LST APNRATECTRL）_64343877.md)
    > - [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**MOD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
    > - [**RMV DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)

**md：`WSFD-215204/激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md`**
- 操作步骤上下文（±2 行原文）：
  L41:
    >   [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md)
    > 4. **可选：**配置APN Rate Control改变时发送CCR消息。
    >   [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > 5. **可选：**配置CDR话单中携带APN Rate Control字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)

### WSFD-215205

**md：`WSFD-215205/WSFD-215205 基于服务PLMN的NB-IoT终端接入速率控制参考信息（S_PGW-C）_77673138.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET APNPLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/设置APN Serving PLMN速率控制配置（SET APNPLMNRATECTRL）_64343912.md)
    > - [**LST APNPLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/查询APN Serving PLMN速率控制配置（LST APNPLMNRATECTRL）_64343876.md)
    > - [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**MOD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
    > - [**RMV DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)

**md：`WSFD-215205/激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md`**
- 操作步骤上下文（±2 行原文）：
  L43:
    >       [**SET PLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/Serving PLMN速率控制配置/设置Serving PLMN速率控制配置（SET PLMNRATECTRL）_64343918.md)
    > 4. **可选：**配置Serving PLMN Rate Control改变时发送CCR消息。
    >   [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > 5. **可选：**配置CDR话单中携带Serving PLMN Rate Control字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**SET OCSINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板OCS初始化（SET OCSINIT）_09896932.md)
    > - [**SET TXTIMER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板Tx定时器（SET TXTIMER）_09896927.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**SET OCSINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板OCS初始化（SET OCSINIT）_09896932.md)
    > - [**SET TXTIMER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板Tx定时器（SET TXTIMER）_09896927.md)

**md：`WSFD-109001/在线计费DCC会话业务流程_95110431.md`**
- 操作步骤上下文（±2 行原文）：
  L67:
    > #### [单RG单DCC会话功能](#ZH-CN_TOPIC_0295110431)
    > 
    > 当OCS不支持在一个Gy会话中处理多个RG时，则需要同一个EPS承载的不同RG与OCS通过不同的session-id进行交互。通过配置 ****ADD DCCTEMPLATE**** 命令的 “SESSIONMODE” 参数为 “MULTIPLE” ，即承载内每个RG使用独立DCC会话，使能单RG单DCC会话功能。以用户访问RG1和RG2业务为例进行激活、位置变更、去激活，具体流程如 [图4](#ZH-CN_TOPIC_0295110431__fig297115302443) 所示。
    > 
    > - 用户激活触发DCC会话创建场景：多个RG触发创建多个Session，不同的Session之间的session-id不同。

**md：`WSFD-109001/配置DCC处理动作_95923447.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcc-test | 已配置数据中获取 | RAR中没有RG时的处理动作。 |
  | **ADD DCCTEMPLATE** | RAR消息RG上报方式（RARNORGACTION） | REPORT_ALL_RG | 本端规划 | RAR中没有RG时的处理动作。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test", CCFH=CONTINUE, CCFHOFFLINE=ENABLE, RARNORGACTION=REPORT_ALL_RG, FAILOVERSUP=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L48:
    > 
    > - 配置GGSN/PGW-C收到OCS的请求消息RAR中没有携带RG的处理动作。
    >   **ADD DCCTEMPLATE**
    > - 配置用户激活后OCS Down的处理动作。
    >     1. 配置Tx定时器超时以后的处理方式。
  L51:
    > - 配置用户激活后OCS Down的处理动作。
    >     1. 配置Tx定时器超时以后的处理方式。
    >       **ADD DCCTEMPLATE**
    >       > **说明**
    >       > 参数 “CCFH” 用于其他方式下在线计费Tx定时器超时后的动作处理。
  L61:
    >       > - “CONTINUE”：表示GGSN/PGW-C会向备OCS重发一次请求消息，如果能收到响应，则与备OCS交互；如果Tx定时器超时仍然未得到响应，则转离线计费，继续进行业务。选择该种方式时，同上需要一方面部署主备OCS组，一方面主OCS组支持failover，即在CCA消息中CC-Session-Failover AVP支持failover，另一方面还需要在GGSN/PGW-C本地配置支持failover功能，即配置[步骤 2](#ZH-CN_OPI_0295923447__step4)，[步骤 7](#ZH-CN_OPI_0295923447__step5)，该动作才能生效。
    >     2. 配置在线计费是否支持failover，配置 “FAILOVERSUP” 参数为 “ENABLE” 。当Tx定时器超时后的处理方式为 “RETRY_AND_TERM” 或者 “CONTINUE” 时，需要配置该步骤。
    >       **ADD DCCTEMPLATE**
    >     3. **可选：**配置在线计费是否支持自动failback。
    >       **ADD DCCTEMPLATE**

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcc-test | 已配置数据中获取 | 配置主从OCS组。 |
  | **ADD DCCTEMPLATE** | 主OCS组名称（PRIOCSGRPNAME） | og-test1 | 本端规划 | 配置主从OCS组。 |
  | **ADD DCCTEMPLATE** | 备OCS组名称（SECOCSGRPNAME） | og-test2 | 本端规划 | 配置主从OCS组。 |
- 操作步骤上下文（±2 行原文）：
  L116:
    >       **MOD DCCTEMPLATE**
    >       DCC模板
    >       **ADD DCCTEMPLATE**
    > 8. **可选：**配置Diameter应用相关功能，即设置GGSN/PGW-C是否检查OCS返回的CEA消息中携带的Origin-Host AVP。
    >     a. 配置GGSN/PGW-C检查OCS返回的CEA消息中携带的OriginHost AVP与本地 **ADD OCS** 配置的host名称是否一致。

**md：`WSFD-109001/配置在线计费模板_95923574.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcc-test | 本端规划 | 新增DCC在线计费模板，用于配置在线计费相关属性。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test";`
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test";`
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test";`
- 操作步骤上下文（±2 行原文）：
  L74:
    >       **MOD DCCTEMPLATE**
    >     b. 配置DCC Template模板，以及触发CCR的各参数、CCR消息中携带的参数。
    >       **ADD DCCTEMPLATE**
    >     c. 配置各计费参数，请见在线计费章节的后面小节。
    >           - [配置CCR触发场景](配置在线计费模板/配置CCR触发场景_95923545.md)
  L118:
    > 
    > ```
    > ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test";
    > ```
    > 
  L128:
    > 
    > ```
    > ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test";
    > ```
    > 

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcc-test | 本端规划 | 新增DCC在线计费模板，用于配置在线计费相关属性。 |
  | **ADD DCCTEMPLATE** | 配额空耗时间门限值（秒）（QCT） | 0 | 本端规划 | 配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。 |
  | **ADD DCCTEMPLATE** | 配额空闲时间门限值（秒）（QHT） | 0 | 本端规划 | 配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。 |
  | **ADD DCCTEMPLATE** | 流量阈值触发百分比（%）（VQT） | 20 | 本端规划 | 标识业务剩余流量配额达到VQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。 |
  | **ADD DCCTEMPLATE** | 时间阈值触发百分比（%）（TQT） | 20 | 本端规划 | 标识业务剩余时长配额达到TQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。 |
  | **ADD DCCTEMPLATE** | 指定CCR-I消息中携带RG的个数（CCRINITRGNUM） | 5 | 本端规划 | 用户激活时发送的CCR-I消息中携带RG的个数。 |
  | **ADD DCCTEMPLATE** | 在线配额有效时长（分）（VALIDTIME） | 30 | 本端规划 | 标识配额有效时长，超时后触发GGSN/PGW-C上报CCR消息。 |
  | **ADD DCCTEMPLATE** | 业务触发请求使能开关（SERVICETRIGGER） | ENABLE | 本端规划 | 应用新业务是否发送CCR。 |
  | **ADD DCCTEMPLATE** | CCFH处理动作（CCFH） | TERMINATE | 本端规划 | Tx定时器超时后处理动作。 |
  | **ADD DCCTEMPLATE** | 主OCS组名称（PRIOCSGRPNAME） | ocs_host | 本端规划 | 配置主从OCS组。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE: DCCTMPLTNAME="dcc-test", QCT=0, QHT=0, VQT=20, TQT=20, CCRINITRGNUM=5, CCFH=TERMINATE, SGSNTRIGGER=ENABLE, SERVICETRIGGER=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L96:
    >       **MOD DCCTEMPLATE**
    >     b. DCC模板。
    >       **ADD DCCTEMPLATE**
    >   > **说明**
    >   > 配置全局DCC模板使用命令全局 **MOD DCCTEMPLATE** ，其他粒度（UserProfile、APN、计费属性Charging Characteristics）的DCC模板使用命令 **ADD DCCTEMPLATE** ，在模板下配置在线计费参数（如 [步骤 6](#ZH-CN_OPI_0295923459__step5) ~ [步骤 9](#ZH-CN_OPI_0295923459__step131731835194911) ），最后绑定不同的粒度范围。
  L98:
    >       **ADD DCCTEMPLATE**
    >   > **说明**
    >   > 配置全局DCC模板使用命令全局 **MOD DCCTEMPLATE** ，其他粒度（UserProfile、APN、计费属性Charging Characteristics）的DCC模板使用命令 **ADD DCCTEMPLATE** ，在模板下配置在线计费参数（如 [步骤 6](#ZH-CN_OPI_0295923459__step5) ~ [步骤 9](#ZH-CN_OPI_0295923459__step131731835194911) ），最后绑定不同的粒度范围。
    >   >
    >   > 由此可见，主要是粒度范围不一致，其他的计费参数命令类似。
  L110:
    >       **ADD OCSBINDING**
    >     d. 配置主从OCS组。
    >       **ADD DCCTEMPLATE**
    > 6. 配置配额门限（配额空耗时间QCT、配额空闲时间QHT、流量门限阈值VQT、时长门限阈值TQT）。
    >   **ADD DCCTEMPLATE**

**md：`WSFD-109001/配置OCS Failover功能_95923411.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcc-test | 已配置数据中获取 | 配置主从OCS组。 |
  | **ADD DCCTEMPLATE** | 主OCS组名称（PRIOCSGRPNAME） | ocs-gra | 本端规划 | 配置主从OCS组。 |
  | **ADD DCCTEMPLATE** | 备OCS组名称（SECOCSGRPNAME） | ocs-grb | 本端规划 | 配置主从OCS组。 |
  | **ADD DCCTEMPLATE** | 支持failover使能开关（FAILOVERSUP） | ENABLE | 本端规划 | 支持failover和failback。 |
  | **ADD DCCTEMPLATE** | CCFH处理动作（CCFH） | RETRY_AND_TERM | 本端规划 | 支持failover和failback。 |
  | **ADD DCCTEMPLATE** | failback使能开关（AUTOFAILBACK） | ENABLE | 本端规划 | 支持failover和failback。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE: DCCTMPLTNAME="dcc-test", PRIOCSGRPNAME="ocs-gra", SECOCSGRPNAME="ocs-grb", CCFH=RETRY_AND_TERM, AUTOFAILBACK=ENABLE, FAILOVERSUP=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L10:
    > ## [操作场景](#ZH-CN_OPI_0295923411)
    > 
    > 当用户激活后进行业务时，GGSN/PGW-C发送在线计费请求消息给OCS，同时启动Tx定时器，在指定的时间内未收到OCS的响应，即可判断OCS服务器状态异常，则执行CCFH进行failover处理。CCFH的动作设置请参见 **ADD DCCTEMPLATE** 命令，只有当动作设置为RETRY_AND_TERM或者CONTINUE时，才会执行failover动作。GGSN/PGW-C向备OCS组重发消息，如果备OCS组也没有响应或者备OCS因状态异常、消息发送速率超过wal值等导致不可用，可以根据情况配置阻塞用户业务或者转离线计费继续进行业务。
    > 
    > 实现OCS服务器failover需要具备以下几个条件：
  L68:
    >     a. 配置DCC模板。
    >           - 全局模板：**MOD DCCTEMPLATE**
    >           - DCC模板：**ADD DCCTEMPLATE**
    >     b. 配置DCC模板的主从OCS组。
    >       **ADD DCCTEMPLATE**
  L70:
    >           - DCC模板：**ADD DCCTEMPLATE**
    >     b. 配置DCC模板的主从OCS组。
    >       **ADD DCCTEMPLATE**
    >     c. 配置DCC模板的Tx定时器超时后的处理方式。
    >       **ADD DCCTEMPLATE**

**md：`WSFD-109001/配置OCS负荷分担_95923468.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcc-test | 本端规划 | 主从OCS组。 |
  | **ADD DCCTEMPLATE** | 主OCS组名称（PRIOCSGRPNAME） | ocs_gra | 已配置数据中获取 | 主从OCS组。 |
  | **ADD DCCTEMPLATE** | 备OCS组名称（SECOCSGRPNAME） | ocs_grb | 已配置数据中获取 | 主从OCS组。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test",PRIOCSGRPNAME="ocs_gra",SECOCSGRPNAME="ocs_grb";`
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test",PRIOCSGRPNAME="ocs_gra",SECOCSGRPNAME="ocs_grb";`
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test",PRIOCSGRPNAME="ocs_gra",SECOCSGRPNAME="ocs_grb";`
- 操作步骤上下文（±2 行原文）：
  L97:
    >       **ADD OCSBINDING**
    > 5. 配置主从OCS组。
    >   **ADD DCCTEMPLATE**
    > 
    > ## [任务示例1](#ZH-CN_OPI_0295923468)
  L185:
    > 3. 配置主从OCS组。
    >   ```
    >   ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test",PRIOCSGRPNAME="ocs_gra",SECOCSGRPNAME="ocs_grb";
    >   ```
    > 
  L266:
    > 3. 配置主从OCS组。
    >   ```
    >   ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test",PRIOCSGRPNAME="ocs_gra",SECOCSGRPNAME="ocs_grb";
    >   ```
    > 

**md：`WSFD-109001/配置基于CC+用户号段选择OCS_95923602.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcctemp01<br>dcctemp02 | 本端规划 | 主从OCS组。 |
  | **ADD DCCTEMPLATE** | 主OCS组名称（PRIOCSGRPNAME） | ocs_gra | 已配置数据中获取 | 主从OCS组。 |
  | **ADD DCCTEMPLATE** | 备OCS组名称（SECOCSGRPNAME） | ocs_grb | 已配置数据中获取 | 主从OCS组。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcctemp01",PRIOCSGRPNAME="ocs-gra",SECOCSGRPNAME="ocs-grb";`
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcctemp02",PRIOCSGRPNAME="ocs-grb",SECOCSGRPNAME="ocs-gra";`
- 操作步骤上下文（±2 行原文）：
  L82:
    >       **ADD OCSBINDING**
    > 3. 配置主从OCS组。
    >   **ADD DCCTEMPLATE**
    > 4. 配置虚拟APN。
    >     a. 使能虚拟APN功能。
  L177:
    > 3. 配置主从OCS组。
    >   ```
    >   ADD DCCTEMPLATE:DCCTMPLTNAME="dcctemp01",PRIOCSGRPNAME="ocs-gra",SECOCSGRPNAME="ocs-grb";
    >   ```
    >   ```
  L180:
    >   ```
    >   ```
    >   ADD DCCTEMPLATE:DCCTMPLTNAME="dcctemp02",PRIOCSGRPNAME="ocs-grb",SECOCSGRPNAME="ocs-gra";
    >   ```
    > 4. 配置真实APN。

**md：`WSFD-109001/配置CCR消息中携带的参数_95923469.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | 私有属性使能开关（PRIVATEATTR） | ENABLE | 本端规划 | CCR消息是否携带运营商的私有扩展属性。 |
  | **ADD DCCTEMPLATE** | CCR携带费率切换点信元开关（CCRTARIFFSW） | ENABLE | 本端规划 | CCR消息是否携带CCA下发的费率切换时间点。 |
  | **ADD DCCTEMPLATE** | 是否携带累加流量信息（QUOTATOTAL） | ENABLE | 本端规划 | Gy接口按照累加/增量方式上报计费信息。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test", CCRTARIFFSW=ENABLE, PRIVATEATTR=ENABLE, QUOTATOTAL=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L49:
    >       > 默认情况下是按照增量方式上报，上述开关打开后按照累加模式上报。
    >     4. 配置CCR消息中携带一个或多个Multiple-Service-Credit-Control(MSCC) AVP，配置参数 “MSCCCARRYTYPE” 。
    >   **ADD DCCTEMPLATE**
    > - 配置全局DCC模板中CCR消息中携带的参数。
    >     1. 配置CCR消息中是否携带Requested-Service-Unit (RSU) AVP，配置参数 “QHTEXPIREDRSU” 。
  L77:
    > 1. 配置DCC template模板（配置CCR消息中携带费率切换点、配置CCR消息中携带运营商私有扩展属性）。
    >   ```
    >   ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test", CCRTARIFFSW=ENABLE, PRIVATEATTR=ENABLE, QUOTATOTAL=ENABLE;
    >   ```
    > 2. 为APN实例apn-test绑定DCC template模板。

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcc-test | 本端规划 | 新增DCC在线计费模板，用于配置在线计费相关属性。 |
  | **ADD DCCTEMPLATE** | 配额空耗时间门限值（秒）（QCT） | 0 | 本端规划 | 配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。 |
  | **ADD DCCTEMPLATE** | 配额空闲时间门限值（秒）（QHT） | 0 | 本端规划 | 配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。<br>说明：如果OCS支持接收QHT超时触发的CCR消息，建议QHT不小于60秒。 |
  | **ADD DCCTEMPLATE** | 流量阈值触发百分比（%）（VQT） | 0 | 本端规划 | 标识业务剩余流量配额达到VQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。 |
  | **ADD DCCTEMPLATE** | 时间阈值触发百分比（%）（TQT） | 20 | 本端规划 | 标识业务剩余时长配额达到TQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。 |
  | **ADD DCCTEMPLATE** | 指定CCR-I消息中携带RG的个数（CCRINITRGNUM） | 5 | 本端规划 | 用户激活时发送的CCR-I消息中携带RG的个数。 |
  | **ADD DCCTEMPLATE** | 在线配额有效时长（分）（VALIDTIME） | 30 | 本端规划 | 标识配额有效时长，超时后触发GGSN/PGW-C上报CCR消息。 |
  | **ADD DCCTEMPLATE** | 业务触发请求使能开关（SERVICETRIGGER） | ENABLE | 本端规划 | 应用新业务是否发送CCR。 |
  | **ADD DCCTEMPLATE** | Rat变化触发使能开关（RATTRIGGER） | ENABLE | 本端规划 | RAT改变是否发送CCR。 |
  | **ADD DCCTEMPLATE** | SGSN变化触发使能开关（SGSNTRIGGER） | ENABLE | 本端规划 | SGSN/SGW地址改变是否发送CCR。 |
  | **ADD DCCTEMPLATE** | QoS变化触发使能开关（QOSTRIGGER） | ENABLE | 本端规划 | QoS改变是否发送CCR。 |
  | **ADD DCCTEMPLATE** | ULI变化触发使能开关（ULITRIGGER） | ENABLE | 本端规划 | ULI改变是否发送CCR。 |
  | **ADD DCCTEMPLATE** | MCC变化触发重授权开关（MCCTRIGGER） | ENABLE | 本端规划 | MCC改变是否发送CCR。 |
  | **ADD DCCTEMPLATE** | MNC变化触发重授权开关（MNCTRIGGER） | ENABLE | 本端规划 | MNC改变是否发送CCR. |
  | **ADD DCCTEMPLATE** | LAC变化触发重授权开关（LACTRIGGER） | ENABLE | 本端规划 | LAC改变是否发送CCR。 |
  | **ADD DCCTEMPLATE** | UE TimeZone改变触发重授权开关（UETZTRIGGER） | ENABLE | 本端规划 | 终端时区改变是否发送CCR。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test", QHT=0,  VQT=0, TQT=20, VALIDTIME=30, RATTRIGGER=ENABLE, SGSNTRIGGER=ENABLE, QOSTRIGGER=ENABLE, ULITRIGGER=ENABLE, SERVICETRIGGER=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L60:
    >   **MOD DCCTEMPLATE**
    > - 配置DCC模板。
    >   **ADD DCCTEMPLATE**
    >     1. 配置CCR-I消息中允许携带的RG的最大个数。配置参数 “CCRINITRGNUM”
    >     2. 配置剩余流量配额小于VQT后向OCS发起CCR。配置参数 “VQT”
  L99:
    >       > **说明**
    >       > 此命令只对内容计费用户生效，PDP级别计费用户不适用该命令。PDP级别计费用户CCR-Initial中携带UserProfile下或者全局下配置的默认计费属性，其中UserProfile优先。如果UserProfile下没有配置CCR-Initial的计费属性，则使用配置在全局下的CCR-Initial的计费属性。如果全局下没有配置CCR-Initial的计费属性，则CCR-Initial不携带计费属性。
    >       **ADD DCCTEMPLATE** 命令配置CCR-I消息中允许携带的RG的最大个数时要与 **SET CTXSTARTRATING** 命令配合使用。如果在 **SET CTXSTARTRATING** 命令中指定了N个RG，则 **ADD DCCTEMPLATE** 命令配置CCR-I消息中允许携带的RG的最大个数至少要配置为N，才能使得上述N个RG都能被CCR-I消息带上申请配额。
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923545)
  L112:
    > 
    > ```
    > ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test", QHT=0,  VQT=0, TQT=20, VALIDTIME=30, RATTRIGGER=ENABLE, SGSNTRIGGER=ENABLE, QOSTRIGGER=ENABLE, ULITRIGGER=ENABLE, SERVICETRIGGER=ENABLE;
    > ```
    > 

**md：`WSFD-109001/配置在线计费自动回切功能_95923555.md`**
- 数据规划表（该命令的参数行）：
  | **ADD DCCTEMPLATE** | DCC模板名称（DCCTMPLTNAME） | dcc-test | 本端规划 | 配置在线计费自动回切功能。<br>说明：用户转离线时如果配置了<br>**SET HOLDINGTIME**<br>命令的HOLDINGTIME，则GGSN/PGW-C在<br>*HOLDINGTIME*<br>超时前一直按照<br>**ADD DCCTEMPLATE**<br>命令配置的RECOVERINTERVAL值定期尝试恢复在线计费；若未配置HOLDINGTIME，则视作该值无限大。 |
  | **ADD DCCTEMPLATE** | 在线计费自动恢复功能开关（ONLCHGRECOVER） | ENABLE | 本端规划 | 配置在线计费自动回切功能。<br>说明：用户转离线时如果配置了<br>**SET HOLDINGTIME**<br>命令的HOLDINGTIME，则GGSN/PGW-C在<br>*HOLDINGTIME*<br>超时前一直按照<br>**ADD DCCTEMPLATE**<br>命令配置的RECOVERINTERVAL值定期尝试恢复在线计费；若未配置HOLDINGTIME，则视作该值无限大。 |
  | **ADD DCCTEMPLATE** | 在线计费自动恢复间隔 （分钟）（RECOVERINTERVAL） | 10 | 本端规划 | 配置在线计费自动回切功能。<br>说明：用户转离线时如果配置了<br>**SET HOLDINGTIME**<br>命令的HOLDINGTIME，则GGSN/PGW-C在<br>*HOLDINGTIME*<br>超时前一直按照<br>**ADD DCCTEMPLATE**<br>命令配置的RECOVERINTERVAL值定期尝试恢复在线计费；若未配置HOLDINGTIME，则视作该值无限大。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test",ONLCHGRECOVER=ENABLE,RECOVERINTERVAL=10;`
- 操作步骤上下文（±2 行原文）：
  L27:
    >   >
    >   > - **SET OCSDOWNACTION**:“OCSDNACTION”需配置为*permit。*
    >   > - **ADD DCCTEMPLATE**:“CCFH”。
    >   > - **ADD CMDRCACT**:“CMDRCACT”为*continue*。
    > - 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
  L42:
    > 
    > 1. 配置在线计费自动回切功能。
    >   **ADD DCCTEMPLATE**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923555)
  L55:
    > 
    > ```
    > ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test",ONLCHGRECOVER=ENABLE,RECOVERINTERVAL=10;
    > ```

**md：`WSFD-109001/调测在线计费自动回切功能_95923505.md`**
- 操作步骤上下文（±2 行原文）：
  L58:
    >     - 如果CCR-I消息发送成功，则在线计费回切功能可用，调测结束。
    >     - 如果CCR-I消息发送不成功，请执行[步骤 7](#ZH-CN_OPI_0295923505__step5)。
    > 7. 执行 **LST DCCTEMPLATE** 命令查询通过 **SET HOLDINGTIME** 命令配置的对应DCC模板的 “HOLDINGTIME” 值是否大于通过 **ADD DCCTEMPLATE** 命令配置的 “RECOVERINTERVAL” 尝试恢复间隔。
    >     - 如果满足条件，则表明在线计费自动回切功能异常，执行[步骤 8](#ZH-CN_OPI_0295923505__step172811121155818)。
    >     - 如果不满足条件，请参考[配置DCC处理动作](../激活Gy_Diameter在线计费/配置DCC处理动作_95923447.md)、[配置在线计费自动回切功能](../激活Gy_Diameter在线计费/配置在线计费模板/配置在线计费自动回切功能_95923555.md)重新配置满足条件的值后，再次执行[步骤 6](#ZH-CN_OPI_0295923505__step4)。

### WSFD-109003

**md：`WSFD-109003/WSFD-109003 基于业务时长的计费参考信息_74013180.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**MOD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
    > - [**RMV DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)

**md：`WSFD-109003/基于业务时长的计费（适用于在线计费）_66402114.md`**
- 操作步骤上下文（±2 行原文）：
  L11:
    > 支持2种类型的时长计费：连续时长计费、QCT（Quota-Consumption-Time）时长计费。每种方式统计时长的方法不一样。
    > 
    > 在线计费的时长计费方式可以通过本地配置 [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md) 中参数 “QCT” 选择默认的时长计费方式为连续时长计费或QCT计费，或接受OCS在 “ MSCC > GSU ” 中下发的时长计费方式，包括连续时长计费、QCT计费。OCS下发的时长计费方式优先级高于本地配置。
    > 
    > 从计费精细度方面而言，QCT方式精度最高，连续时长计费其次。

### WSFD-109004

**md：`WSFD-109004/WSFD-109004 基于业务流量的计费参考信息_74013203.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**MOD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
    > - [**RMV DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md) | DCCTMPLTNAME（融合计费模板名称） | dcc-test | 本端规划 | 配置在线计费的DCC模板。 |
- 任务示例脚本（该命令行）：
  `ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test";`
- 操作步骤上下文（±2 行原文）：
  L90:
    >       [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    >     - 配置在线计费模板。
    >       [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    >       [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > 7. 绑定该UserProfile使用的Rule。
  L151:
    > 
    > ```
    > ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test";
    > SET USRPROFCHARGE: USRPROFNAME="up-test", DCCTEMPLATE="dcc-test";
    > ```

### WSFD-011133

**md：`WSFD-011133/WSFD-011133 Gy over DRA参考信息_29725462.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - **[ADD OCSGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)**
    > - **[ADD OCSBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)**
    > - **[ADD DCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)**
    > - **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
    > - **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)**

**md：`WSFD-011133/实现原理_30001131.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > #### [DRA](#ZH-CN_CONCEPT_0230001131)
    > 
    > Diameter Routing Agent（3GPP简称DRA，RFC称Diameter Agent）是在Diameter客户端与服务器间转交Diameter消息的设备，支持Diameter消息的路由、转交以及Diameter服务器寻址功能。在本特性中，DRA负责维护 GGSN/PGW-C 与OCS之间的链路，可以根据链路状态进行OCS的重选， 通过向 GGSN/PGW-C 转交OCS发送的CCA消息通知发生OCS的切换， GGSN/PGW-C在后续的信令交互中携带DRA重选的OCS host。另外OCS可以发起更新流程， 通过RAR消息 通知 GGSN/PGW-C 发生OCS切换。 **[ADD DCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)** / **[MOD DCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)** 命令可以控制 GGSN/PGW-C 是否支持OCS重选和切换。 GGSN/PGW-C 根据统计周期内向DRA发送消息的成功率，动态调整向DRA发送消息的速率，实现DRA的过载保护。为加强 GGSN/PGW-C 与DR A之间交互的安全性，可以采用在Gy接口上应用IPSec的方式。
    > 
    > DRA有如下三种类型：
  L145:
    > Failover到备用OCS Group中的OCS或备用DRA后，如果主用OCS Group中的OCS或主用DRA恢复正常，且Auto-failback功能使能， GGSN/PGW-C 将切换回主用OCS或主用DRA。
    > 
    > - OCS的failback控制开关：**[ADD DCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)**/**[MOD DCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)****AUTOFAILBACK**
    > - DRA的failback控制开关：**[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md) /****[MOD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/修改Diameter路由域名信息（MOD DIAMRTREALM）_09897304.md)****AUTOFAILBACKSW**

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 操作步骤上下文（±2 行原文）：
  L135:
    >       **[ADD OCSGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)**
    >     c. **可选：** 配置DCC模板以及主从OCS组。
    >       **[ADD DCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)**
    > 8. 配置DRA相关信息。
    >     a. **可选：**配置SCTP端点信息。

## ④ 自动比对
- 命令真相参数（61）：['APNRATETRIGGER', 'AUTOFAILBACK', 'BLKFREESRV', 'BLOCKTIMER', 'CCFH', 'CCFHOFFLINE', 'CCRINITRGNUM', 'CCRPRECISIONTS', 'CCRSPESMFLAG', 'CCRTARIFFSW', 'CELLIDTRIGGER', 'DCCTMPLTNAME', 'DDFH', 'DICTNO', 'ECGITRIGGER', 'ENBTRIGGER', 'EVENTCHGCCC', 'EVENTCHGMOD', 'FAILOVERSUP', 'FUATERMINATE', 'LACTRIGGER', 'LOCALHOSTNAME', 'LOCSLCTMODE', 'MAXBTI', 'MAXENVELOPE', 'MCCTRIGGER', 'MNCTRIGGER', 'MSCCCARRYTYPE', 'NOQUOTATRIGGER', 'OCSCHANGECCAI', 'OCSCHANGECCAU', 'OCSCHANGERAR', 'ONLCHGRECOVER', 'PDPTYPE4NONIP', 'PRIOCSGRPNAME', 'PRIVATEATTR', 'QCT', 'QHT', 'QHTEXPIREDRSU', 'QOSTRIGGER', 'QUOTATOTAL', 'RACTRIGGER', 'RARNORGACTION', 'RATTRIGGER', 'RECOVERINTERVAL', 'SECOCSGRPNAME', 'SERIALCCR', 'SERVICECONTEXT', 'SERVICETRIGGER', 'SESSIONMODE', 'SGSNTRIGGER', 'SPECIFICATION', 'SPRATETRIGGER', 'TACTRIGGER', 'TQT', 'TRTIMER', 'UETZTRIGGER', 'ULITRIGGER', 'UQT', 'VALIDTIME', 'VQT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 7, '本端规划': 44}（多值→atom 应考虑 decision_driven）
