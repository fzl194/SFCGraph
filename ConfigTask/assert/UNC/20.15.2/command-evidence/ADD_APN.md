# 命令证据包：ADD APN
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md`
> 用该命令的特性数：44

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于添加一个新的APN实例。在运营商需要接入外部包交换网络，配置APN和绑定VPN时使用此命令进行配置。2/3/4/5G核心网中采用APN来标识UNC，同时APN定义了UNC可以接入的外部包交换网络。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 当前版本不支持此命令的APPLAYERVOLUME、QCHATSWITCH、PSEUDOACTSWITCH参数。
- VIRTUALAPN开关开启前必须通过ADD VIRTUALAPNRULE配置规划的虚拟APN映射规则，否则会导致该APN下的用户激活失败。

- 最多可输入20000条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| VIRTUALAPN | 虚拟APN | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| HASVPN | 绑定VPN | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| VPNINSTANCE | VPN实例名 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~31。 |
| HASVPNIPV6 | 绑定IPv6 VPN | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| VPNINSTANCEIPV6 | IPv6 VPN实例名 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~31。 |
| SERVINGNODEPLMN | 根据SGSN/SGW映射PLMN | local_planned | optional | ENABLE | <br>- ENABLE（使能） |
| SERVINGNODERAT | 根据SGSN/SGW映射RAT | local_planned | optional | ENABLE | <br>- ENABLE（使能） |
| APPLAYERVOLUME | 仅统计应用层流量 | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| QCHATSWITCH | Qchat功能开关 | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| EMERGENCYSWITCH | 支持紧急呼叫 | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| PSEUDOACTSWITCH | 支持假激活用户开关 | local_planned | optional | INHERIT | <br>- ENABLE（使能） |
| NTSRSWITCH | 网络侧触发业务恢复功能开关 | local_planned | optional | INHERIT | <br>- ENABLE（使能） |
| RESTORPGWSWITCH | 故障重启业务恢复功能PGW开关 | local_planned | optional | INHERIT | <br>- ENABLE（使能） |
| PDTNSWITCH | PDTN功能开关 | local_planned | conditional | DISABLE | <br>- ENABLE（使能） |
| REACWITHDEL | 去活消息携带reactivation-request开关 | local_planned | optional | DISABLE | <br>- DISABLE（不使能） |
| SCENELIST | 场景列表 | local_planned | conditional | 无 | <br>- GX_RET_CODE_5002（Gx接口返回5002错误码） |
| USRINTSECACTSW | 用户发起的二次激活开关 | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| CHARGEPROFILE | 计费策略 | local_planned | optional | NULL | <br>- NULL（NULL） |
| PPDSWITCH | Ppd功能开关 | local_planned | optional | INHERIT | <br>- INHERIT（继承全局） |
| ULCLFUNC | ULCL功能开关 | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| LADN | 局域数据网络 | global_planned | optional | NotSupport | <br>- Support（支持） |
| REACTTRANS | 透明传输reactivation-request开关 | global_planned | optional | ENABLE | 枚举类型。 |
| RELEASESKIPIND | 携带skipInd信元开关 | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| S6BEMERGCYSERVICE | S6b Emergency Service 标识 | local_planned | conditional | DISABLE | <br>- ENABLE（使能） |
| PPISWITCH | PPI 功能开关 | local_planned | optional | INHERIT | <br>- INHERIT（继承全局） |
| LOCREPORT | 位置上报 | local_planned | optional | INHERIT | <br>- INHERIT（继承全局） |
| PARKINGAPN | Parking APN | global_planned | optional | DISABLE | <br>- ENABLE（使能） |
| TRAFFICDIST | 支持基于漫游地动态签约的分流策略控制 | global_planned | optional | DISABLE | <br>- ENABLE（使能） |
| ALWAYSPSAULCLSW | 主锚点Always分流开关 | global_planned | optional | DISABLE | <br>- ENABLE（使能） |
| CALLINGNUMTYPE | 主叫号码类型 | global_planned | optional | MSISDN | <br>- “MSISDN（移动用户的ISDN号码）”：表示主叫号码类型为MSISDN |
| NGHRVIRTUALAPN | 5G HR漫游场景H-SMF虚拟APN映射功能开关 | local_planned | optional | DISABLE | <br>- ENABLE（使能） |
| INTELLSERSELUPF | 智能业务UPF选择开关 | global_planned | optional | DISABLE | <br>- ENABLE（使能） |
| EXPOSURELOCRPT | 能力开放位置上报 | local_planned | optional | INHERIT | <br>- INHERIT（继承全局） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-108002

**md：`WSFD-108002/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md)
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | Huawei.com | 全网规划 | 配置使能SMF上的ULCL功能 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | ULCL功能开关（ULCLFUNC） | ENABLE | 本端规划 | 配置使能SMF上的ULCL功能 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="Huawei.com", ULCLFUNC=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L87:
    > 3. 配置基于DNN的分流，将DNN绑定至UL CL分流规则中。
    >     a. 配置使能SMF上的ULCL功能。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     b. 配置用户模板组。
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
  L116:
    > 
    > ```
    > ADD APN:APN="Huawei.com", ULCLFUNC=ENABLE; 
    > ```
    > 

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-223003/PDU会话创建使能专网业务流程_85233681.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > 5. AMF通过Nsmf_PDUSession_CreateSMContext request消息将UE激活请求带上来的Requesteddnn和AM-PCF指定的selectedDnn（dnn-ar）携带给SMF。
    >   > **说明**
    >   > SMF从AMF收到selectedDnn（dnn-ar）后会基于本地配置（ **ADD APN** 中的 “TRAFFICDIST” ）以及License判定，如果匹配则继续会话创建流程，否则直接拒绝流程。
    > 6. 会话注册。
    > 7. SMF选择SM-PCF。

**md：`WSFD-223003/PDU会话重建使能专网业务流程_37553658.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > 6. AMF通过Nsmf_PDUSession_CreateSMContext request向SMF发起PDU会话创建请求，消息中携带UE激活请求携带的Requesteddnn和AM-PCF指定的selectedDnn（dnn-ar）给SMF。
    >   > **说明**
    >   > SMF从AMF收到selectedDnn（dnn-ar）后会基于本地配置（ **ADD APN** 中的 “TRAFFICDIST” ）以及License判定，如果匹配则继续会话创建流程，否则直接拒绝流程。
    > 7. 会话注册。
    > 8. SMF选择SM-PCF。

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | dnn-ar | 全网规划 | 配置使能专网DNN的ULCL功能 |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | ULCL功能开关（ULCLFUNC） | ENABLE | 本端规划 | 配置使能专网DNN的ULCL功能 |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 支持基于漫游地动态签约的分流策略控制（TRAFFICDIST） | ENABLE | 全网规划 | 配置使能专网DNN的ULCL功能 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="dnn-ar", ULCLFUNC=ENABLE,TRAFFICDIST=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L63:
    > 3. 配置基于DNN的分流，将专网DNN绑定至UL CL分流规则中。
    >     a. 配置使能SMF上的ULCL功能。
    >       [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     b. 配置用户模板组。
    >       [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
  L84:
    > 
    > ```
    > ADD APN:APN="dnn-ar", ULCLFUNC=ENABLE,TRAFFICDIST=ENABLE; 
    > ```
    > 

### WSFD-223101

**md：`WSFD-223101/WSFD-223101 基于预定义规则的分流策略控制(4G)参考信息_11634944.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md)
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)

### WSFD-228001

**md：`WSFD-228001/WSFD-228001 跨域业务访问参考信息_55954935.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - **[ADD DNAIINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/DNAI管理/DNAI信息管理/增加DNAI信息（ADD DNAIINFO）_10605246.md)**
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - **[ADD APNUPFINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/APN UPF信息管理/增加指定APN的UPF节点信息（ADD APNUPFINFO）_96241630.md)**
    > - **[MOD UPNODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP节点管理/修改UPF节点（MOD UPNODE）_09652705.md)**

**md：`WSFD-228001/部署跨域业务漫游访问（反向分流）（SMF）_58568777.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | Huawei.com | 全网规划 | 配置专用DNN Always的分流功能 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 主锚点Always分流开关（ALWAYSPSAULCLSW） | ENABLE | 全网规划 | 配置专用DNN Always的分流功能 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="Huawei.com", ALWAYSPSAULCLSW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L49:
    >   **[ADD DNAIINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/DNAI管理/DNAI信息管理/增加DNAI信息（ADD DNAIINFO）_10605246.md)**
    > 4. 配置专用DNN Always的分流功能。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 5. 配置专用DNN下UPF位置特征。
    >   **[ADD APNUPFINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/APN UPF信息管理/增加指定APN的UPF节点信息（ADD APNUPFINFO）_96241630.md)**
  L73:
    > ADD DNAIINFO: DNAI="testdnai", SHUNTDIRECT=REVERSE, SHUNTLOC=HOME, ALWAYSSHUNTSW=ENABLE
    > //配置专用DNN Always的分流功能。
    > ADD APN: APN="Huawei.com", ALWAYSPSAULCLSW=ENABLE;
    > //配置专用DNN下UPF位置特征。
    > ADD APNUPFINFO: APN="Huawei.com", UPFINSTANCEID=UPF_INSTANCE0, LOCATION=INHERIT, PSACOMBINEULCL=ENABLE;

**md：`WSFD-228001/部署跨域业务漫游访问（正向分流）（SMF）_11634940.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | Huawei.com | 全网规划 | 配置专用DNN Always的分流功能 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 主锚点Always分流开关（ALWAYSPSAULCLSW） | ENABLE | 全网规划 | 配置专用DNN Always的分流功能 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="Huawei.com", ALWAYSPSAULCLSW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L49:
    >   **[ADD DNAIINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/DNAI管理/DNAI信息管理/增加DNAI信息（ADD DNAIINFO）_10605246.md)**
    > 4. 配置专用DNN Always的分流功能。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 5. 配置专用DNN下UPF位置特征。
    >   **[ADD APNUPFINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/APN UPF信息管理/增加指定APN的UPF节点信息（ADD APNUPFINFO）_96241630.md)**
  L73:
    > ADD DNAIINFO: DNAI="testdnai", SHUNTDIRECT=NORMAL, SHUNTLOC=HOME, ALWAYSSHUNTSW=ENABLE;
    > //配置专用DNN Always的分流功能。
    > ADD APN: APN="Huawei.com", ALWAYSPSAULCLSW=ENABLE;
    > //配置专用DNN下UPF位置特征。
    > ADD APNUPFINFO: APN="Huawei.com", UPFINSTANCEID=UPF_INSTANCE0, LOCATION=INHERIT, PSACOMBINEULCL=ENABLE;

### WSFD-011521

**md：`WSFD-011521/激活NSA用户QoS管理_27675786.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > 
    > - 请仔细阅读[WSFD-011521 NSA 用户QoS管理特性概述](特性概述_27675785.md)。
    > - 完成配置普通APN[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)。
    > 
    > 数据

### WSFD-010701

**md：`WSFD-010701/WSFD-010701 QoS与流量管理参考信息_30180384.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md)
    > - [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
    > - [**ADD 5GCSUBQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/5GC QoS配置/本地5GC QoS/增加5GC签约QoS配置（ADD 5GCSUBQOS）_09652601.md)

**md：`WSFD-010701/激活QoS与流量管理（适用于GGSN）_29724911.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn | 本端规划 | 配置指定APN实例。 |
- 操作步骤上下文（±2 行原文）：
  L78:
    >       [**ADD PRER8REMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/PreR8 Qos映射ToS_DSCP/增加Pre-R8 QoS到TOS_DSCP的映射规则（ADD PRER8REMARK）_09654400.md)
    >     5. 配置指定AP实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     6. 为该APN实例绑定QOSPROFILE。
    > - 置基于APN的3GPP QoS到DSCP/ToS的映射关系。
  L89:
    >       **[ADD 5GCREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/5GC QoS配置/5GC Qos映射ToS_DSCP/增加5GC QoS到TOS_DSCP的映射规则（ADD 5GCREMARK）_09653051.md)**
    >     5. 配置指定APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     6. 为该APN实例绑定QOSPROFILE。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)

**md：`WSFD-010701/激活QoS与流量管理（适用于PGW-C）_86476700.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn | 本端规划 | 配置指定APN实例。 |
- 操作步骤上下文（±2 行原文）：
  L75:
    >       **[**ADD EPSREMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)**
    >     5. 配置指定AP实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     6. 为该APN实例绑定QOSPROFILE。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)

**md：`WSFD-010701/激活QoS与流量管理（适用于SMF）_86476699.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn | 本端规划 | 配置指定APN实例。 |
- 操作步骤上下文（±2 行原文）：
  L76:
    >       **[**ADD 5GCREMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/5GC QoS配置/5GC Qos映射ToS_DSCP/增加5GC QoS到TOS_DSCP的映射规则（ADD 5GCREMARK）_09653051.md)**
    >     5. 配置指定APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     6. 为该APN实例绑定QOSPROFILE。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)

### WSFD-109202

**md：`WSFD-109202/WSFD-109202 会话类QOS保证参考信息_28258189.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**ADD PRER8QOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/PreR8 QoS控制动作/增加Pre-R8 QoS控制动作配置（ADD PRER8QOSACTION）_09652510.md)
    > - [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >   [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
    > - [**SET QOSREMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局DSCP_ToS映射功能/设置全局QoS到TOS_DSCP的映射规则（SET QOSREMARK）_09653840.md)

**md：`WSFD-109202/激活会话类QOS保证（适用于GGSN）_28258187.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN（APN名称） | apn1 | 本端规划 | 指定APN实例。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn1";`
  `ADD APN:APN="apn1";`
- 操作步骤上下文（±2 行原文）：
  L20:
    > 
    > - 请仔细阅读 [WSFD-109202 会话类QoS保证特性概述](WSFD-109202 会话类QOS保证特性概述_28258186.md) 。
    > - 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
    > - 完成加载License。
    > 
  L81:
    >       [**ADD PRER8QOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/PreR8 QoS控制动作/增加Pre-R8 QoS控制动作配置（ADD PRER8QOSACTION）_09652510.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 为APN实例绑定QoS profile。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
  L96:
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 将UserProfile Group绑定到APN。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-109202/激活会话类QOS保证（适用于SGW-C_PGW-C）_28344569.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN (APN名称) | apn1 | 本端规划 | 指定APN实例。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn1";`
  `ADD APN:APN="apn1";`
- 操作步骤上下文（±2 行原文）：
  L20:
    > 
    > - 请仔细阅读 [WSFD-109202 会话类QoS保证特性概述](WSFD-109202 会话类QOS保证特性概述_28258186.md) 。
    > - 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
    > - 完成加载License。
    > 
  L102:
    >       [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 为APN实例绑定QoS profile。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
  L117:
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 将UserProfile Group绑定到APN。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-109202/调测会话类QOS保证_28258188.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - 完成[激活会话类QoS保证（适用于GGSN）](激活会话类QOS保证（适用于GGSN）_28258187.md)。
    > - 完成[激活会话类QoS保证（适用于SGW-C/PGW-C）](激活会话类QOS保证（适用于SGW-C_PGW-C）_28344569.md)。
    > - 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
    > 
    > 数据

### WSFD-109203

**md：`WSFD-109203/WSFD-109203 本地QOS控制参考信息_28258574.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)

**md：`WSFD-109203/激活本地QOS控制（SMF）_77795473.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn | 本端规划 | 配置指定APN实例。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn1";`
- 操作步骤上下文（±2 行原文）：
  L21:
    > 
    > - 请仔细阅读 [WSFD-109203 本地QOS控制特性概述](特性概述_28258571.md) 。
    > - 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
    > 
    > 数据
  L92:
    >       [**ADD 5GCQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/5GC QoS配置/5GC QoS控制动作/增加5GC QoS控制动作配置（ADD 5GCQOSACTION）_09652342.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 为APN实例绑定QoS profile。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
  L131:
    >   //进入指定APN实例。
    >   ```
    >   ADD APN:APN="apn1";
    >   ```
    >   //为该APN实例绑定QosProfile。

**md：`WSFD-109203/激活本地QOS控制（适用于GGSN）_28258572.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN（APN名称） | apn1 | 本端规划 | 指定APN实例。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn1";`
- 操作步骤上下文（±2 行原文）：
  L21:
    > 
    > - 请仔细阅读 [WSFD-109203 本地QOS控制特性概述](特性概述_28258571.md) 。
    > - 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
    > - 完成加载License。
    > 
  L87:
    >       [**ADD PRER8QOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/PreR8 QoS控制动作/增加Pre-R8 QoS控制动作配置（ADD PRER8QOSACTION）_09652510.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 为APN实例绑定QoS profile。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
  L127:
    >   //进入指定APN实例。
    >   ```
    >   ADD APN:APN="apn1";
    >   ```
    >   //为该APN实例绑定QosProfile。

**md：`WSFD-109203/激活本地QOS控制（适用于SGW-C_PGW-C）_28258573.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN（APN名称） | apn1 | 本端规划 | 指定APN实例。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn1";`
- 操作步骤上下文（±2 行原文）：
  L21:
    > 
    > - 请仔细阅读 [WSFD-109203 本地QOS控制特性概述](特性概述_28258571.md) 。
    > - 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
    > - 完成加载License。
    > 
  L96:
    >       [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 为APN实例绑定QoS profile。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
  L144:
    >   //进入指定APN实例。
    >   ```
    >   ADD APN:APN="apn1";
    >   ```
    >   //为该APN实例绑定QosProfile。

**md：`WSFD-109203/特性概述_28258571.md`**
- 操作步骤上下文（±2 行原文）：
  L82:
    > 
    > - 基于APN的QoS
    >   通过 [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) 命令配置指定APN实例下的QosProfile，通过 [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 配置APN实例，并通过 [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) [设置指定APN的QoS属性配置信息（SET APNQOSATTR）](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) 为APN实例绑定QoS profile。
    >     - 若配置了别名APN，则不使用本地QoS策略，使用签约的QoS策略。
    >     - 若配置了虚拟APN，则使用虚拟APN配置的本地QoS策略。

**md：`WSFD-109203/调测本地QOS控制_29670144.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - 完成[激活本地QOS控制（适用于SGW-C/PGW-C）](激活本地QOS控制（适用于SGW-C_PGW-C）_28258573.md)。
    > - 完成[激活本地QOS控制（SMF）](激活本地QOS控制（SMF）_77795473.md)。
    > - 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
    > 
    > 数据

### WSFD-106203

**md：`WSFD-106203/WSFD-106203 别名APN参考信息（适用于GGSN_PGW-C_SMF）_34797882.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/增加APN别名配置（ADD APNALIAS）_28567622.md)
    > - [**LCK APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/锁定APN别名配置（LCK APNALIAS）_28567625.md)

**md：`WSFD-106203/激活别名APN_34797880.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn5 | 本端规划 | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>中的APN名称不能与<br>[**ADD APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/增加APN别名配置（ADD APNALIAS）_28567622.md)<br>中的别名APN重复。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn5";`
- 操作步骤上下文（±2 行原文）：
  L27:
    > 
    > - 请仔细阅读 [WSFD-106203 别名APN特性概述（适应于GGSN/PGW-C/SMF）](WSFD-106203 别名APN特性概述（适应于GGSN_PGW-C_SMF）_34797879.md)。
    > - 完成配置APN[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)。
    > - 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
    > 
  L67:
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :
    > 3. 配置真实APN。
    >   [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 4. 配置APN的上报属性。在每次执行 [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 时会自动增加对应的 **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** 配置记录，需要将真实APN的 “PCF” 和 “CHF” 配置为 “SERVICE” 。
    >   **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**
  L68:
    > 3. 配置真实APN。
    >   [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 4. 配置APN的上报属性。在每次执行 [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 时会自动增加对应的 **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** 配置记录，需要将真实APN的 “PCF” 和 “CHF” 配置为 “SERVICE” 。
    >   **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**
    > 5. 配置别名APN和转换APN。

### WSFD-010504

**md：`WSFD-010504/WSFD-010504 控制面地址分配方式参考信息_77813716.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 

### WSFD-104005

**md：`WSFD-104005/WSFD-104005 DHCPv6地址分配参考信息_61255173.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD DHCPSERVER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/DHCP服务器/增加DHCP服务器（ADD DHCPSERVER）_86984444.md)
    > - [**ADD DHCPBINDPOOLGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/DHCP服务器绑定/增加DHCP服务器组与地址池组绑定关系（ADD DHCPBINDPOOLGRP）_32382543.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.md)
    > - [**SET IPALLOCRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址分配规则配置/设置全局地址分配规则（SET IPALLOCRULE）_49644937.md)

### WSFD-104413

**md：`WSFD-104413/WSFD-104413 DHCP功能参考信息_61065989.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD DHCPSERVER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/DHCP服务器/增加DHCP服务器（ADD DHCPSERVER）_86984444.md)
    > - [**ADD DHCPBINDPOOLGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/DHCP服务器绑定/增加DHCP服务器组与地址池组绑定关系（ADD DHCPBINDPOOLGRP）_32382543.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.md)
    > - [**SET IPALLOCRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址分配规则配置/设置全局地址分配规则（SET IPALLOCRULE）_49644937.md)

### WSFD-205102

**md：`WSFD-205102/WSFD-205102 虚拟APN参考信息_29376297.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 
    > [**ADD VIRTUALAPNRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/虚拟APN映射策略/增加虚拟APN映射策略配置（ADD VIRTUALAPNRULE）_09652380.md)

**md：`WSFD-205102/激活虚拟APN_70437186.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | example.com | 本端规划 | 开启虚拟APN功能。 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 虚拟APN（VIRTUALAPN） | ENABLE | 本端规划 | 开启虚拟APN功能。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="example.com",VIRTUALAPN=ENABLE;`
  `ADD APN:APN="email",VIRTUALAPN=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L26:
    > 
    > - 请仔细阅读 [WSFD-205102 虚拟APN](../WSFD-205102 虚拟APN_66765163.md)。
    > - 完成配置APN[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)或别名APN配置，别名APN参考[别名APN（适用于GGSN/PGW-C/SMF）](../WSFD-106203 别名APN/别名APN（适用于GGSN_PGW-C_SMF）_34797878.md)。
    > - 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
    > 
  L69:
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :
    > 3. 配置APN，开启虚拟APN功能。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 4. （可选）配置APN纠错。
    >   [**SET ANONYMOUSAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/匿名APN/设置匿名APN配置（SET ANONYMOUSAPN）_09651574.md)
  L103:
    > 2. 新增虚拟APN“example.com”，使能Virtual APN功能。
    >   ```
    >   ADD APN:APN="example.com",VIRTUALAPN=ENABLE;
    >   ```
    > 3.

### WSFD-205104

**md：`WSFD-205104/WSFD-205104 支持用户发起的二次激活参考信息_85401023.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0000001185401023)

**md：`WSFD-205104/激活支持用户发起的二次激活_39947740.md`**
- 任务示例脚本（该命令行）：
  `ADD APN: APN="huawei.com", USRINTSECACTSW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 打开UE发起二次激活开关。
    >   [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001139947740)
  L51:
    > 
    > ```
    > ADD APN: APN="huawei.com", USRINTSECACTSW=ENABLE;
    > ```

### WSFD-109101

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn-test1<br>apn-test2 | 全网规划 | 配置APN。可通过<br>[**LST APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>命令查询已经配置的APN。 |

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn1 | 本端规划 | 配置APN。可通过<br>[**LST APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>命令查询已经配置的APN。 |

### WSFD-109105

**md：`WSFD-109105/WSFD-109105 基于位置的业务管理参考信息_79067183.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD SRVNODEGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于对接IP地址的虚拟APN映射管理/虚拟APN映射的服务节点组/增加服务节点组（ADD SRVNODEGROUP）_09651376.md)
    > - [**ADD SRVNODEIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于对接IP地址的虚拟APN映射管理/服务节点组的服务节点IP段/增加服务节点IP（ADD SRVNODEIP）_09654166.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD VIRTUALAPNRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/虚拟APN映射策略/增加虚拟APN映射策略配置（ADD VIRTUALAPNRULE）_09652380.md)
    > 

**md：`WSFD-109105/激活基于位置的业务管理_79067181.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | example.com | 本端规划 | 规划虚拟APN。 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 虚拟APN（VIRTUALAPN） | ENABLE | 本端规划 | 规划虚拟APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="example.com", VIRTUALAPN=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L85:
    >       [**ADD SRVNODEIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于对接IP地址的虚拟APN映射管理/服务节点组的服务节点IP段/增加服务节点IP（ADD SRVNODEIP）_09654166.md)
    > 7. 配置APN，开启虚拟APN功能。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 8. 配置虚拟APN与真实APN的映射规则。
    >   [**ADD VIRTUALAPNRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/虚拟APN映射策略/增加虚拟APN映射策略配置（ADD VIRTUALAPNRULE）_09652380.md)
  L138:
    > 
    > ```
    > ADD APN: APN="example.com", VIRTUALAPN=ENABLE;
    > ```
    > 

### WSFD-011310

**md：`WSFD-011310/WSFD-011310 PLMN标识获取参考信息_72291446.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET SGWPLMNORIGIN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取PLMN管理/S_P合一的SGW PLMN获取策略/设置S-GW PLMN ID来源（SET SGWPLMNORIGIN）_09651723.md)
    > - [**SET PLMNPRIORITY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取PLMN管理/获取PLMN方式的优先级/设置获取PLMN优先级（SET PLMNPRIORITY）_09653827.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD SRVNODEPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取PLMN管理/服务节点PLMN/增加SGSN_SGW_PGW地址段和PLMN标识之间的映射关系（ADD SRVNODEPLMN）_09652097.md)
    > 

**md：`WSFD-011310/激活PLMN标识获取_66289935.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn-test | 本端规划 | APN实例名称 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 根据SGSN/SGW-C映射PLMN（SERVINGNODEPLMN） | ENABLE | 本端规划 | PLMN标识映射开关 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test",SERVINGNODEPLMN=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L59:
    > 5. 配置允许指定APN下的用户通过SGW-C IP映射获取SGW-C的PLMN标识的方式来获取PLMN标识。
    >     a. 指定APN实例名称时，设置允许此APN下的用户通过SGW-C IP映射方式来获取PLMN标识的开关。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     b. 配置SGW-C IP与PLMN标识间的映射关系表。
    >       [**ADD SRVNODEPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取PLMN管理/服务节点PLMN/增加SGSN_SGW_PGW地址段和PLMN标识之间的映射关系（ADD SRVNODEPLMN）_09652097.md)
  L96:
    > 
    > ```
    > ADD APN:APN="apn-test",SERVINGNODEPLMN=ENABLE;
    > ```
    > 

### WSFD-205107

**md：`WSFD-205107/WSFD-205107 GGSN_P-GW信令代理参考信息_87913145.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD PRIMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/GGSN和P-GW Proxy/代理选择的IMSI_MSISDN号段/增加代理IMSI_MSISDN号段（ADD PRIMSIMSISDNSEG）_42853258.md)
    > - [**MOD PRIMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/GGSN和P-GW Proxy/代理选择的IMSI_MSISDN号段/修改代理IMSI_MSISDN号段（MOD PRIMSIMSISDNSEG）_88613385.md)

**md：`WSFD-205107/激活GGSN_P-GW信令代理_38987364.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN实例名（APN） | apn-test | 从已配置数据中获取 | APN实例名称 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L105:
    > 2. 如需开启指定APN的Proxy 功能，配置基于APN控制是否打开网关Proxy功能。
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    >   ```

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - **[ADD APNRDSCLIENTIP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)**
    > - **[ADD APNRDSSVRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/APN Radius服务器/设置APN Radius服务器组（ADD APNRDSSVRGRP）_09896735.md)**

**md：`WSFD-011306/配置RADIUS功能_32909765.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - 请仔细阅读[WSFD-011306 Radius功能特性概述](../特性概述_31467848.md)
    > - 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
    > - 完成[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)。
    > 
    > 数据

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn-test | 全网规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L22:
    > - 请仔细阅读[WSFD-011306 Radius功能特性概述](../特性概述_31467848.md)。
    > - UNC与周边网元的互通配置已经完成。
    > - 完成[增加APN配置](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)。
    > - **该功能需要与UPF/PGW-U共同完成配置**。配置该功能前，需要确保已在UPF/PGW-U上配置完成使用的过滤器和绑定的流过滤器、规则等业务感知信息。
    > - 已通过[**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)配置完成逻辑接口使用到的逻辑IP。
  L53:
    > 2. 配置业务触发RADIUS功能。
    >     a. 配置APN。
    >       [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     b. 使能业务触发RADIUS功能。
    >       **[SET APNRDSACCTCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS计费管理/APN计费控制/设置APN RADIUS计费控制参数（SET APNRDSACCTCTRL）_09896770.md)**
  L89:
    > 
    > ```
    > ADD APN: APN="apn-test";
    > SET APNRDSACCTCTRL: APN="apn-test",SRVTRIGGER=ENABLE;
    > ```

**md：`WSFD-011306/配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn1 | 全网规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | VPN实例名（VPNINSTANCE） | vpn_pdn | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定IPv6 VPN（HASVPNIPV6） | DISABLE | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | INHERIT | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn1", HASVPN=ENABLE, VPNINSTANCE="vpn_pdn", HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT, REACWITHDEL=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L112:
    >       > 步骤b-e中，执行该命令多次，可以配置多个计费/鉴权AAA服务器。
    >     f. 配置APN。
    >       [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     g. 配置APN下的Client-IP。
    >       **[ADD APNRDSCLIENTIP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)**
  L192:
    > 
    > ```
    > ADD APN: APN="apn1", HASVPN=ENABLE, VPNINSTANCE="vpn_pdn", HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT, REACWITHDEL=DISABLE;
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）_31879931.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn1 | 全网规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | VPN实例名（VPNINSTANCE） | vpn_pdn | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定IPv6 VPN（HASVPNIPV6） | DISABLE | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | INHERIT | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn1", HASVPN=ENABLE, VPNINSTANCE="vpn_pdn", HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT, REACWITHDEL=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L114:
    >       > 步骤b-e中，执行该命令多次，可以配置多个计费/鉴权AAA服务器。
    >     f. 配置APN。
    >       [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     g. 配置APN下的Client-IP。
    >       **[ADD APNRDSCLIENTIP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)**
  L188:
    > 
    > ```
    > ADD APN: APN="apn1", HASVPN=ENABLE, VPNINSTANCE="vpn_pdn", HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT, REACWITHDEL=DISABLE;
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn1 | 全网规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | VPN实例名（VPNINSTANCE） | vpn_enterprise | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定IPv6 VPN（HASVPNIPV6） | DISABLE | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | INHERIT | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn1",HASVPN=ENABLE,VPNINSTANCE="vpn_enterprise";`
- 操作步骤上下文（±2 行原文）：
  L144:
    >       > 步骤b-e中，执行该命令多次，可以配置多个计费/鉴权AAA服务器。
    >     f. 配置APN。
    >       [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     g. 配置APN下的Client-IP。
    >       **[ADD APNRDSCLIENTIP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)**
  L255:
    > 
    > ```
    > ADD APN: APN="apn1",HASVPN=ENABLE,VPNINSTANCE="vpn_enterprise";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn1 | 全网规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | VPN实例名（VPNINSTANCE） | vpn_enterprise | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定IPv6 VPN（HASVPNIPV6） | DISABLE | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | INHERIT | 本端规划 | - |
  | [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn1",HASVPN=ENABLE,VPNINSTANCE="vpn_enterprise";`
- 操作步骤上下文（±2 行原文）：
  L144:
    >       > 步骤b-e中，执行该命令多次，可以配置多个计费/鉴权AAA服务器。
    >     f. 配置APN。
    >       [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     g. 配置APN下的Client-IP。
    >       **[ADD APNRDSCLIENTIP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)**
  L275:
    > 
    > ```
    > ADD APN: APN="apn1",HASVPN=ENABLE,VPNINSTANCE="vpn_enterprise";
    > ```
    > 

### WSFD-104004

**md：`WSFD-104004/WSFD-104004 IPv6前缀代理参考信息_76459529.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**MOD ADDRPOOL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/修改地址池（MOD ADDRPOOL）_64343893.md)
    > - [**LST ADDRPOOL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/查询地址池（LST ADDRPOOL）_09652305.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**MOD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/修改APN配置（MOD APN）_09653164.md)
    > - [**RMV APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/删除APN配置（RMV APN）_09653148.md)

**md：`WSFD-104004/激活IPv6前缀代理_76459527.md`**
- 任务示例脚本（该命令行）：
  `ADD APN`
- 操作步骤上下文（±2 行原文）：
  L62:
    > 5. 配置APN下的地址分配属性。根据规划配置为本地或Radius分配IPv6代理前缀。
    >     a. 指定APN名称。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     b. 配置地址分配属性。为本地或Radius分配IPv6代理前缀。
    >       [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.md)
  L102:
    > 
    > ```
    > ADD APN
    > : APN="huawei.com";
    > 

### WSFD-011307

**md：`WSFD-011307/激活支持RADIUS抄送功能_33769357.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn-test | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L22:
    > - 请仔细阅读[WSFD-011307 支持Radius抄送功能特性概述](特性概述_33741340.md)。
    > - 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
    > - 完成[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)。
    > - 完成[激活RADIUS功能](../WSFD-011306 Radius功能/激活RADIUS功能_15542173.md)。
    > 
  L64:
    >   > 如需配置多个服务器，则需要执行该命令多次。
    > 6. 配置APN下绑定AAA服务器组。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >   **[ADD APNRDSSVRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/APN Radius服务器/设置APN Radius服务器组（ADD APNRDSSVRGRP）_09896735.md)**
    > 
  L106:
    > 
    > ```
    > ADD APN: APN="apn-test";
    > ADD APNRDSSVRGRP: APN="apn-test",RDSSVRGRPNAME="isprg";
    > ```

### WSFD-011308

**md：`WSFD-011308/激活AAA负荷分担_14758812.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - 请仔细阅读[WSFD-011308 AAA负荷分担特性概述](特性概述_14758811.md)。
    > - 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
    > - 完成[增加APN配置](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)。
    > 
    > 数据

### WSFD-011201

**md：`WSFD-011201/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
  `ADD APN: APN="apn-test";`
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L144:
    > 
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    > 
  L180:
    > 
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    > 
  L216:
    > 
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    > 

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN，可以使用命令<br>**LST APN**<br>查询。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L102:
    > 3. 配置OFCTemplate模板绑定APN对象。
    >     a. 配置APN。如已配置APN，请跳过该步骤。
    >       **ADD APN**
    >     b. 配置APN实例绑定OFCTemplate模板。
    >       **SET APNCHARGECTRL**
  L157:
    > 3. 任务二：配置APN实例 **apn-test** 的离线计费参数。
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    >   ```

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L100:
    > 
    > ```
    > ADD APN: APN="apn-test";
    > ```
    > 

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 本端规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test";`
  `ADD APN:APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L81:
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >   > **说明**
  L110:
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    > 
  L143:
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    >   ADD APN:APN="apn-test";
    >   ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
    >   ```

**md：`WSFD-011201/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L68:
    > 3. 配置APN下的费率切换组。
    >     a. 配置APN。如已配置APN，请跳过该步骤。
    >       **ADD APN**
    >     b. 配置APN实例下的费率切换组。
    >       **SET APNCHARGECTRL**
  L145:
    > 3. 任务二：基于APN **apn-test** 配置费率切换组。
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    >   ```

**md：`WSFD-011201/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L69:
    >       **ADD CHARGECHAR**
    >     2. 配置APN。如已配置APN，请跳过该步骤。
    >       **ADD APN**
    >     3. 将CC绑定到APN上。
    >       **SET APNCHARGECTRL** :
  L105:
    > 
    > ```
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > ```
    > 

**md：`WSFD-011201/配置话单字段（GGSN_SGW-C_PGW-C）_95923364.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 本端规划 | 配置APN，可以使用命令<br>**LST APN**<br>查询。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L101:
    > 3. 配置APN实例的话单字段模板。
    >     a. 配置APN实例。如已配置APN，请跳过该步骤。
    >       **ADD APN**
    >     b. 配置APN实例绑定话单字段模板。
    >       **SET APNCHARGECTRL**
  L132:
    > 
    > ```
    > ADD APN: APN="apn-test";
    > ```
    > 

**md：`WSFD-011201/调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。 |

### WSFD-011202

**md：`WSFD-011202/激活支持热计费功能_28072077.md`**
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L77:
    > 
    > ```
    > ADD APN:APN="apn-test";
    > ```
    > 

### WSFD-011206

**md：`WSFD-011206/使能融合计费功能_77691175.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置DNN。可通过<br>**LST APN**<br>命令查询已经配置的DNN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L99:
    > 
    > ```
    > ADD APN: APN="apn-test";
    > ```
    > 

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 基于DNN粒度，将CCT绑定到特定DNN下。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;`
  `ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L83:
    >       **ADD CCT**
    >     2. 配置DNN。
    >       **ADD APN**
    >     3. 配置CCT模板绑定DNN。
    >       **SET APNCHARGECTRL**
  L99:
    >             **ADD UPBINDUPG**
    >           b. 配置DNN实例，将UserProifle组绑定到DNN实例。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >             每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行 **ADD UPBINDUPG** 命令，将UserProfile绑定到UserProfile组即可。
  L133:
    > 
    > ```
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > SET APNCHARGECTRL: APN="apn-test", CCTEMPLATE="cct_test";
    > ```

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L109:
    >             **ADD UPBINDUPG**
    >           b. 配置DNN实例，将UserProifle组绑定到DNN实例。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >             每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行 **ADD UPBINDUPG** 命令，将UserProfile绑定到UserProfile组即可。
  L210:
    > 
    > ```
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";
    > ```

**md：`WSFD-011206/配置计费属性CC_90776700.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置DNN。可通过<br>**LST APN**<br>命令查询已经配置的DNN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L67:
    >       **ADD CHARGECHAR**
    >     3. 配置DNN。如已配置DNN，请跳过该步骤。
    >       **ADD APN**
    >     4. 将CC绑定到DNN上。
    >       **SET APNCHARGECTRL**
  L101:
    > ```
    > ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > SET APNCHARGECTRL: APN="apn-test", CCNAME="testchgcha";
    > ```

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置DNN。可通过<br>**LST APN**<br>命令查询已经配置的DNN。 |

### WSFD-011309

**md：`WSFD-011309/激活支持用户属性反射_28361026.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 根据SGSN/SGW映射RAT（SERVINGNODERAT） | ENABLE | 本端规划 | 配置使用SGSN/S-GW IP映射方式来获取RAT类型的开关。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test",SERVINGNODERAT=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    >   [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. 配置APN实例，设置是否允许此APN下的用户通过SGSN/S-GW-IP映射方式来获取RAT Type。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 7. 配置APN实例绑定话单字段模板。
    >   [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
  L89:
    > 
    > ```
    > ADD APN:APN="apn-test",SERVINGNODERAT=ENABLE;
    > ```
    > 

### WSFD-109001

**md：`WSFD-109001/配置在线计费模板_95923574.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 本端规划 | 配置APN，可以使用<br>**LST APN**<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L132:
    > 
    > ```
    > ADD APN: APN="apn-test";
    > ```
    > 

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 本端规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test";`
  `ADD APN:APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L85:
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >   > **说明**
  L114:
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    > 
  L147:
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    >   ADD APN:APN="apn-test";
    >   ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
    >   ```

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |

**md：`WSFD-109001/配置离线_在线计费方式（GGSN_PGW-C）_15408914.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test";`
  `ADD APN: APN="apn-test";`
  `ADD APN: APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L144:
    > 
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    > 
  L180:
    > 
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    > 
  L216:
    > 
    >   ```
    >   ADD APN: APN="apn-test";
    >   ```
    > 

**md：`WSFD-109001/配置计费属性CC（GGSN_SGW-C_PGW-C）_15408915.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。可通过<br>**LST APN**<br>命令查询已经配置的APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L69:
    >       **ADD CHARGECHAR**
    >     2. 配置APN。如已配置APN，请跳过该步骤。
    >       **ADD APN**
    >     3. 将CC绑定到APN上。
    >       **SET APNCHARGECTRL** :
  L105:
    > 
    > ```
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > ```
    > 

**md：`WSFD-109001/配置基于CC+用户号段选择OCS_95923602.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn1 | 本端规划 | 虚拟APN。 |
  | **ADD APN** | 虚拟APN（VIRTUALAPN） | ENABLE | 本端规划 | 虚拟APN。 |
  | **ADD APN** | APN名称（APN） | apn2<br>apn3 | 本端规划 | 配置APN，可以使用命令<br>**LST APN**<br>查询。 |
  | **ADD APN** | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | INHERIT | 本端规划 | 配置APN，可以使用命令<br>**LST APN**<br>查询。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn2",RESTORPGWSWITCH=INHERIT;`
  `ADD APN:APN="apn3",RESTORPGWSWITCH=INHERIT;`
  `ADD APN:APN="apn1",VIRTUALAPN=ENABLE,RESTORPGWSWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L85:
    > 4. 配置虚拟APN。
    >     a. 使能虚拟APN功能。
    >       **ADD APN**
    >     b. 配置虚拟APN映射规则。
    >       **ADD VIRTUALAPNRULE**
  L90:
    > 5. 配置真实APN。
    >     a. 配置真实APN实例。
    >       **ADD APN**
    >     b. 绑定DCC模板。
    >       **SET APNCHARGECTRL**
  L184:
    > 4. 配置真实APN。
    >   ```
    >   ADD APN:APN="apn2",RESTORPGWSWITCH=INHERIT;
    >   ```
    >   ```

**md：`WSFD-109001/配置CCR消息中携带的参数_95923469.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 本端规划 | 配置APN，可以使用命令<br>**LST APN**<br>查询。 |

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APN** | APN名称（APN） | apn-test | 本端规划 | 配置APN，可以使用<br>**LST APN**<br>命令进行查询。 |

### WSFD-109005

**md：`WSFD-109005/激活支持CoA功能_10243675.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn-test | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L56:
    > 2. 配置COA功能使能开关。
    >     a. 指定APN实例名称。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     b. 配置CoA功能使能开关。
    >       [**SET APNAUTHATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN鉴权属性/设置APN鉴权属性配置（SET APNAUTHATTR）_28567656.md)
  L88:
    > 
    > ```
    > ADD APN:APN="apn-test";
    > SET APNAUTHATTR:APN="apn-test",COASWITCH=ENABLE;
    > ```

### WSFD-109007

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN（APN名称） | apn-test | 全网规划 | 将UserProfile组绑定到DNN上。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L99:
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     b. 配置DNN，将UserProfile组绑定到指定DNN实例上。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
  L161:
    > ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    > ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    > ADD APN:APN="apn-test";
    > ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
    > ```

### WSFD-102001

**md：`WSFD-102001/配置与P-CSCF的对接数据（适用于SGW-C_PGW-C）_74289879.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | ims | 全网规划 | 配置APN实例。 |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="ims";`
- 操作步骤上下文（±2 行原文）：
  L49:
    >   > 比如说有A、B、C、D四台服务器，主备Group都需要配置四台服务器，主Group的顺序为A、B、C、D，备Group的顺序为B、A、D、C。
    > 4. 指定APN实例。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 5. 将指定的主备P-CSCF分组绑定到APN下。
    >   [**ADD PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/增加APN和P-CSCF组关联关系（ADD PCSCFGRPBNDAPN）_09653091.md)
  L110:
    > 
    > ```
    > ADD APN: APN="ims";
    > ```
    > 

### WSFD-102004

**md：`WSFD-102004/激活基于VoLTE的优先语音服务（适用于SGW-C_PGW-C）_51416105.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | ims | 已配置数据中获取 | - |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | Ppd功能开关（PPDSWITCH） | ENABLE | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="ims",PPDSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L40:
    >   [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md)
    > 3. 打开PPD功能开关。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0251416105)
  L61:
    > 
    > ```
    > ADD APN:APN="ims",PPDSWITCH=ENABLE;
    > ```

### WSFD-102101

**md：`WSFD-102101/激活VoLTE紧急呼叫（适用于SGW-C_PGW-C）_30394882.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | sos | 全网规划 | 使能紧急呼叫功能。 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | 使能紧急呼叫功能。 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | VPN实例名（VPNINSTANCE） | vpn1 | 已配置数据中获取 | 使能紧急呼叫功能。 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 支持紧急呼叫（EMERGENCYSWITCH） | ENABLE | 本端规划 | 使能紧急呼叫功能。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="sos",HASVPN=ENABLE,VPNINSTANCE="vpn1",EMERGENCYSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L51:
    >       [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    >     b. 创建APN实例，使能紧急呼叫功能。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >       > **说明**
    >       > 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。
  L80:
    >   //创建APN实例，使能紧急呼叫功能。
    >   ```
    >   ADD APN:APN="sos",HASVPN=ENABLE,VPNINSTANCE="vpn1",EMERGENCYSWITCH=ENABLE;
    >   ```
    >   //使能APN的PCC功能。

**md：`WSFD-102101/激活VoWIFI紧急呼叫_95090215.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | sos | 已配置数据中获取 | 规划使能紧急呼叫功能的APN实例。 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 支持紧急呼叫（EMERGENCYSWITCH） | ENABLE | 已配置数据中获取 | 是否使能VoWiFi紧急呼叫功能，默认值为<br>“DISABLE”<br>。 |
  | [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | S6b Emergency Service 标识（S6BEMERGCYSERVICE） | ENABLE | 本端规划 | 该参数仅在EMERGENCYSWITCH开启才能生效 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="sos",EMERGENCYSWITCH=ENABLE,S6BEMERGCYSERVICE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L12:
    > 在 UNC 上激活VoWiFi紧急呼叫功能，将紧急呼叫的用户接入WIFI网络。
    > 
    > 目前 UNC 支持VoWiFi紧急呼叫功能，可以通过 [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 的 “EMERGENCYSWITCH” 和 “S6BEMERGCYSERVICE” 参数分别配置开关和AAR消息是否携带Emergency Service标识。在Wi-Fi覆盖范围内且UE支持的情况下，针对VoWiFi紧急呼叫业务的处理方式是： 在3GPP网络覆盖下 ，UE发起紧急呼叫时优先回落CS域进行处理。
    > 
    > > **说明**
  L38:
    >   使能VoWiFi紧急呼叫功能。
    >   在 “MML命令行-UNC” 窗口上执行命令
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >   > **说明**
    >   > 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。
  L57:
    > 
    > ```
    > ADD APN:APN="sos",EMERGENCYSWITCH=ENABLE,S6BEMERGCYSERVICE=ENABLE;
    > ```

**md：`WSFD-102101/特性概述_70014691.md`**
- 操作步骤上下文（±2 行原文）：
  L126:
    > **VoWiF紧急呼叫**
    > 
    > 目前 UNC 支持VoWiFi紧急呼叫功能，可以通过 [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 的 “EMERGENCYSWITCH” 和 “S6BEMERGCYSERVICE” 参数分别配置开关和AAR消息是否携带Emergency Service标识。在Wi-Fi覆盖范围内且UE支持的情况下，针对VoWiFi紧急呼叫业务的处理方式是： 在3GPP网络覆盖下 ，UE发起紧急呼叫时优先回落CS域进行处理。
    > 
    > #### [计费与话单](#ZH-CN_TOPIC_0170014691)

### WSFD-102203

**md：`WSFD-102203/激活基于PCRF_PCF的VoLTE业务快速恢复_43991630.md`**
- 操作步骤上下文（±2 行原文）：
  L52:
    > // 进入 “MML命令行-UNC” 窗口。
    > 
    > //将真实使用的APN与终端上报的APN配置映射关系。 参数 APN使用 **[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** 命令配置生成。执行该命令前请先通过 **[**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)** 查询当前是否已添加该APN配置。 根据查询结果，选择是否配置该参数。
    > 
    > ```

### WSFD-102701

**md：`WSFD-102701/激活VoNR基础语音业务_58365277.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** | APN名称（APN） | ims | 全网规划<br>- | 配置IMS网络的APN |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="ims";`
- 操作步骤上下文（±2 行原文）：
  L75:
    > 4. 进入 “MML命令行-UNC” 窗口。
    > 5. 配置IMS网络APN。
    >   **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
    > 6. 修改APN参数。
    >   **[SET APNIMSATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)**
  L120:
    > 
    > ```
    > ADD APN: APN="ims";
    > ```
    > 

### WSFD-102702

**md：`WSFD-102702/激活EPS Fallback_76175590.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** | APN名称（APN） | ims | 全网规划<br>- | 配置IMS网络的APN |
- 任务示例脚本（该命令行）：
  `ADD APN: APN="ims";`
- 操作步骤上下文（±2 行原文）：
  L69:
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 7. 配置IMS网络APN。
    >   **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
    > 8. 修改APN参数。
    >   **[SET APNIMSATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)**
  L109:
    > 
    > ```
    > ADD APN: APN="ims";
    > ```
    > 

### WSFD-102705

**md：`WSFD-102705/WSFD-102705 基于VoNR的优先语音服务参考信息_78254456.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
    > - **[SET SMFFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)**
    > 

**md：`WSFD-102705/激活基于VoNR的优先语音服务_23535627.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** | APN名称（APN） | ims | 本端规划 | 开启PPI（寻呼策略指示）功能。 |
  | **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** | PPISWITCH（PPI 功能开关） | ENABLE | 本端规划 | 开启PPI（寻呼策略指示）功能。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="ims", PPISWITCH=ENABLE;`
  `ADD APN:APN="ims", PPISWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. **可选：**通过 **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** 命令开启PPI功能。
    > 3. 通过 **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** 命令中继承 **[SET SMFFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)** 命令中的全局配置开启PPI功能。
    > 
  L34:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. **可选：**通过 **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** 命令开启PPI功能。
    > 3. 通过 **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** 命令中继承 **[SET SMFFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)** 命令中的全局配置开启PPI功能。
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001223535627)
  L47:
    > 
    > ```
    > ADD APN:APN="ims", PPISWITCH=ENABLE;
    > ```
    > 

### WSFD-102602

**md：`WSFD-102602/激活LTE一键通（适用于PGW-C_SGW-C）_10282625.md`**
- 任务示例脚本（该命令行）：
  `ADD APN: APN="apn1";`
- 操作步骤上下文（±2 行原文）：
  L162:
    > 
    > ```
    > ADD APN: APN="apn1";
    > ```
    > 

### WSFD-102706

**md：`WSFD-102706/WSFD-102706 VoNR紧急呼叫参考信息_91548842.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**MOD SMFEMGCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/紧急呼叫会话配置/修改运营商紧急呼叫会话功能配置（MOD SMFEMGCFG）_37903905.md)
    > - **[**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**RMV APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/删除APN配置（RMV APN）_09653148.md)
    > - [**MOD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/修改APN配置（MOD APN）_09653164.md)

**md：`WSFD-102706/激活VoNR紧急呼叫_46685913.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** | APN名称（APN） | sos | 本端规划 | 添加一个新的APN实例。 |
  | **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** | 支持紧急呼叫（EMERGENCYSWITCH） | ENABLE | 本端规划 | 添加一个新的APN实例。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="sos",EMERGENCYSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L95:
    > 8. 配置APN参数，并将APN下的某指定号段绑定到P-CSCF组，使能紧急呼叫功能。
    >   创建APN实例。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >   > **说明**
    >   > 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。
  L131:
    > 
    > ```
    > ADD APN:APN="sos",EMERGENCYSWITCH=ENABLE;
    > ```
    > 

### WSFD-107019

**md：`WSFD-107019/WSFD-107019 P-CSCF选择参考信息_62638766.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
    > - **[MOD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/修改APN配置（MOD APN）_09653164.md)**
    > - **[RMV APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/删除APN配置（RMV APN）_09653148.md)**

**md：`WSFD-107019/激活P-CSCF选择_62638684.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** | APN名称（APN） | huawei.com | 本端规划 | 配置虚拟APN。 |
  | **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** | 虚拟APN（VIRTUALAPN） | ENABLE | 本端规划 | 配置虚拟APN。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="huawei.com", VIRTUALAPN=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L58:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 配置虚拟APN。
    >   **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
    > 3. **可选：**配置TAC组，在TAC组绑定TAC号段。
    >     a. 配置TAC组。
  L95:
    > 
    > ```
    > ADD APN:APN="huawei.com", VIRTUALAPN=ENABLE;
    > ```
    > 

### WSFD-201204

**md：`WSFD-201204/配置MME故障或重启场景_49797715.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN（APN） | ims | 已配置数据中获取 | APN下的网络侧触发业务恢复功能开关。<br>说明：可通过命令<br>[**LST APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>查询。 |
  | [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 网络侧触发业务恢复功能开关（NTSRSWITCH） | ENABLE | 本端规划 | APN下的网络侧触发业务恢复功能开关。<br>说明：可通过命令<br>[**LST APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>查询。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="ims",NTSRSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L59:
    >   > 当NTSRSWITCH参数配置为开启的情况下可通过软参 [BIT769](../../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/会话管理/BIT769 控制MME故障恢复时在DDN消息中是否携带TAI信元_10873890.md) 配置在MME故障场景发送的DDN消息中是否使用私有扩展信元携带用户的TAI。
    > 7. 配置指定APN的NTSR功能。
    >   [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >   > **说明**
    >   > - 推荐普通语音APN和紧急语音APN下配置该步骤，数据APN下不推荐配置。
  L111:
    > 
    > ```
    > ADD APN:APN="ims",NTSRSWITCH=ENABLE;
    > ```

**md：`WSFD-201204/配置SGW-C故障或重启场景_49797716.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN（APN） | ims | 已配置数据中获取 | APN下的网络侧触发业务恢复功能开关。<br>说明：可通过命令<br>[**LST APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>查询。 |
  | [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | ENABLE | 本端规划 | APN下的网络侧触发业务恢复功能开关。<br>说明：可通过命令<br>[**LST APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>查询。 |
  | [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | PDTN功能开关（PDTNSWITCH） | ENABLE | 本端规划 | APN下的网络侧触发业务恢复功能开关。<br>说明：可通过命令<br>[**LST APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>查询。 |
- 任务示例脚本（该命令行）：
  `ADD APN:APN="ims",RESTORPGWSWITCH=ENABLE,PDTNSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L54:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 设置基于APN的承载具备支持SGW RESTORATION的能力。
    >       [**ADD APN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     3. 配置基于整机的防闪断定时器时长和留承载时长。
    >       [**SET FASTRECOVERY**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/网络管理/业务快速恢复/全局参数/设置全局业务快速恢复配置（SET FASTRECOVERY）_31453525.md)
  L94:
    >   //设置基于APN的承载具备支持SGW RESTORATION的能力。
    >   ```
    >   ADD APN:APN="ims",RESTORPGWSWITCH=ENABLE,PDTNSWITCH=ENABLE;
    >   ```
    >   //基于整机的防闪断定时器时长为120秒，保留承载时长为59分钟。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L194:
    > **[LST APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/查询APN PCC功能（LST APNPCCFUNC）_09897035.md)**
    > 
    > **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
    > 
    > **[MOD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/修改APN配置（MOD APN）_09653164.md)**

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L29:
    > - **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)**
    > - **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)**
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - **[ADD PCRF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    > - **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test";`
  `ADD APN:APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L173:
    >       **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**
    >     b. 配置APN。
    >       **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
    >       > **说明**
    >       > 同一个APN只能配置TCP/SCTP中的一种场景，不允许两种场景同时配置到同一APN下。
  L263:
    >   ```
    >   ```
    >   ADD APN:APN="apn-test";
    >   ```
    >   ```
  L381:
    >   ```
    >   ```
    >   ADD APN:APN="apn-test";
    >   ```
    >   ```

### WSFD-011133

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 任务示例脚本（该命令行）：
  `ADD APN:APN="apn-test";`
  `ADD APN:APN="apn-test";`
  `ADD APN:APN="apn-test";`
  `ADD APN:APN="apn-test";`
- 操作步骤上下文（±2 行原文）：
  L273:
    >   ADD DIAMRTREALM:REALMNAME="ocs.huawei.com",APPLICATION=GY,SELECTMODE=MASTER_SLAVE;
    >   ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host1.example.com",SEQUENCE=1;
    >   ADD APN:APN="apn-test";
    >   ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host2.example.com",SEQUENCE=2;
    >   ADD APN:APN="apn-test";
  L275:
    >   ADD APN:APN="apn-test";
    >   ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host2.example.com",SEQUENCE=2;
    >   ADD APN:APN="apn-test";
    >   ADD REALMBINDAPN:APN="apn-test",APPLICATION=GY,CONSTBYIMSISW=DISABLE,REALMNAME="ocs.huawei.com";
    >   ```
  L369:
    >   ADD DIAMRTREALM:REALMNAME="ocs.huawei.com",APPLICATION=GY,SELECTMODE=MASTER_SLAVE;
    >   ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host1.example.com",SEQUENCE=1;
    >   ADD APN:APN="apn-test";
    >   ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host2.example.com",SEQUENCE=2;
    >   ADD APN:APN="apn-test";

### WSFD-011134

**md：`WSFD-011134/激活S6b over DRA（静态路由+BFD组网）_75821602.md`**
- 任务示例脚本（该命令行）：
  `ADD APN:APN="ims";`
  `ADD APN:APN="ims";`
- 操作步骤上下文（±2 行原文）：
  L245:
    >   ```
    >   ```
    >   ADD APN:APN="ims";
    >   ```
    >   ```
  L369:
    >   ```
    >   ```
    >   ADD APN:APN="ims";
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（34）：['ALWAYSPSAULCLSW', 'APN', 'APPLAYERVOLUME', 'CALLINGNUMTYPE', 'CHARGEPROFILE', 'EMERGENCYSWITCH', 'EXPOSURELOCRPT', 'HASVPN', 'HASVPNIPV6', 'INTELLSERSELUPF', 'LADN', 'LOCREPORT', 'NGHRVIRTUALAPN', 'NTSRSWITCH', 'PARKINGAPN', 'PDTNSWITCH', 'PPDSWITCH', 'PPISWITCH', 'PSEUDOACTSWITCH', 'QCHATSWITCH', 'REACTTRANS', 'REACWITHDEL', 'RELEASESKIPIND', 'RESTORPGWSWITCH', 'S6BEMERGCYSERVICE', 'SCENELIST', 'SERVINGNODEPLMN', 'SERVINGNODERAT', 'TRAFFICDIST', 'ULCLFUNC', 'USRINTSECACTSW', 'VIRTUALAPN', 'VPNINSTANCE', 'VPNINSTANCEIPV6']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 31, '本端规划': 61, '从已配置数据中获取': 1, '已配置数据中获取': 10, '全网规划<br>-': 2}（多值→atom 应考虑 decision_driven）
