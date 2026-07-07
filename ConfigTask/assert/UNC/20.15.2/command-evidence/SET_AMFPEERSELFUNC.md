# 命令证据包：SET AMFPEERSELFUNC
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF**

该命令用于控制不同场景下AMF选择对端的功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SCPSEPPRESEL | NFLOCATION | SCPRESELEN | AUSFRESELEN |
| --- | --- | --- | --- |
| OFF | UDM-1&SMF-1 | OFF | ON |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SCPSEPPRESEL | SCP/SEPP重选开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “OFF（关闭）”：关闭 |
| NFLOCATION | 支持使用Location的对端NF类型 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- UDM（UDM） |
| SCPRESELEN | SCP重选增强开关 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “OFF（关闭）”：关闭 |
| AUSFRESELEN | AUSF重选增强开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “OFF（关闭）”：关闭 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-206101

**md：`WSFD-206101/WSFD-206101 UDM全故障业务保活参考信息_89886362.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    > - **[LST NSDNN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/网络切片内DNN管理/查询网络切片支持的DNN（LST NSDNN）_09652609.md)**
    > - **[MOD NSDNN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/网络切片内DNN管理/修改网络切片支持的DNN（MOD NSDNN）_96242642.md)**
    > - **[SET AMFPEERSELFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**
    > - **[LST AMFPEERSELFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/查询AMF对端选择功能控制参数（LST AMFPEERSELFUNC）_18717536.md)**
    > 

**md：`WSFD-206101/实现原理_36726335.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 4. AMF与主AUSF/SCP交互，通过[表1](#ZH-CN_TOPIC_0000001236726335__table929334110412)中的机制判断主AUSF/SCP是否故障。
    >   > **说明**
    >   > 对端AUSF返回5xx错误码时，AMF在对ProblemDetails校验失败后是否重选AUSF以及重选后的AUSF响应消息携带ProblemDetails再次校验失败是否进入UDM Bypass状态根据命令 **[SET AMFPEERSELFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)** 的 “AUSF重选增强开关” 参数配置进行处理。
    >     - 存在网元实例标识为主AUSF的**[ADD BYPASSFAULTCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/Bypass故障状态码管理/增加BYPASS故障状态码（ADD BYPASSFAULTCODE）_58840347.md)**配置记录。
    >           a. 存在网元实例标识为主AUSF， 故障码配置为*，并且错误信息与主AUSF响应的故障码相同的**[ADD BYPASSFAULTCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/Bypass故障状态码管理/增加BYPASS故障状态码（ADD BYPASSFAULTCODE）_58840347.md)**配置记录，则AMF执行[6](#ZH-CN_TOPIC_0000001236726335__li199276572289)。
  L49:
    > 5. AMF重选AUSF/SCP。
    >   > **说明**
    >   > 对端AUSF返回5xx错误码时，AMF在对ProblemDetails校验失败后是否重选AUSF以及重选后的AUSF响应消息携带ProblemDetails再次校验失败是否进入UDM Bypass状态根据命令 **[SET AMFPEERSELFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)** 的 “AUSF重选增强开关” 参数配置进行处理。
    >     - 服务发现备用AUSF失败，或者与备用AUSF/SCP交互后，备用AUSF/SCP返回的故障码大于等于500，则AMF执行[6](#ZH-CN_TOPIC_0000001236726335__li199276572289)。
    >     - 重选AUSF返回的故障码不符合3GPP协议标准时，AMF按照软参**[DWORD68 BIT5](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（AMF）/移动性管理/DWORD68 BIT5 控制AMF与AUSF或UDM交互时是否使用对端原始响应信息_07524626.md)**和**[DWORD17 BIT21](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（AMF）/移动性管理/DWORD17 BIT21 控制AMF对AUSF返回状态码不符合3GPP协议标准时的处理策略_14164683.md)**的值进行处理。

**md：`WSFD-206101/激活UDM全故障业务保活特性_36886325.md`**
- 数据规划表（该命令的参数行）：
  | **[SET AMFPEERSELFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)** | AUSF重选增强开关（AUSFRESELEN） | ON | 本端规划 | 配置对端AUSF返回5xx错误码时，AMF在对ProblemDetails校验失败后是否重选AUSF以及重选后的AUSF响应消息携带ProblemDetails再次校验失败是否进入UDM Bypass状态。<br>此处以参数值为<br>“ON”<br>举例。 |
- 任务示例脚本（该命令行）：
  `SET AMFPEERSELFUNC:AUSFRESELEN=ON;`
- 操作步骤上下文（±2 行原文）：
  L133:
    >       > - 基于具体UDM/AUSF网元实例、具体的故障码和错误信息组合：“网元实例标识”配置为具体的某些网元实例，“自定义故障码”配置为具体的故障码，不配置“错误信息”或者配置具体的“错误信息”。
    >     7. 配置对端AUSF返回5xx错误码时，AMF在对ProblemDetails校验失败后是否重选AUSF以及重选后的AUSF响应消息携带ProblemDetails再次校验失败是否进入UDM Bypass状态。
    >       **[SET AMFPEERSELFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**
    >     8. 通过软参DWORD65 BIT17配置AMF未服务发现到可用的AUSF或UDM时用户是否进入UDM Bypass状态。
    >       **[SET AMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置AMF软件参数比特位（SET AMFSOFTPARAOFBIT）_09651487.md)**
  L206:
    > 
    >   ```
    >   SET AMFPEERSELFUNC:AUSFRESELEN=ON;
    >   ```
    >   //配置AMF未服务发现到可用的AUSF或UDM时用户是否进入UDM Bypass状态。

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > - [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    > - **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0172466541)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)** | 支持使用Location的对端NF类型（NFLOCATION） | PCF | 全网规划 | 配置AMF支持使用PCF通过Location信元携带的地址进行通信。 |
- 任务示例脚本（该命令行）：
  `SET AMFPEERSELFUNC: NFLOCATION=PCF-1;`
  `SET AMFPEERSELFUNC: NFLOCATION=PCF-1;`
- 操作步骤上下文（±2 行原文）：
  L134:
    >       [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    >     8. 配置AMF支持使用PCF通过Location信元携带的地址进行通信。
    >       **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**
    > - 配置SMF的PCC功能。
    >     1. 进入 “MML命令行-UNC” 窗口。
  L310:
    > 
    > ```
    > SET AMFPEERSELFUNC: NFLOCATION=PCF-1;
    > ```
    > 
  L364:
    > 
    > ```
    > SET AMFPEERSELFUNC: NFLOCATION=PCF-1;
    > ```

### WSFD-130001

**md：`WSFD-130001/WSFD-130001 短消息业务参考信息_46109052.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > [**SET NGMMFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)
    > 
    > **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**
    > 
    > #### [告警](#ZH-CN_CONCEPT_0246109052)

**md：`WSFD-130001/激活短消息业务_41956073.md`**
- 数据规划表（该命令的参数行）：
  | **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)** | 支持使用Location的对端NF类型（NFLOCATION） | SMSF | 全网规划 | 对端NF支持使用多个IP地址跟AMF对接场景下，且对端NF类型属于该参数配置的范围，AMF支持使用该NF通过Location信元携带的地址进行后续消息交互。 |
- 任务示例脚本（该命令行）：
  `SET AMFPEERSELFUNC: NFLOCATION=SMSF-1;`
- 操作步骤上下文（±2 行原文）：
  L38:
    >   **[SET NGMMFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
    > 3. 配置AMF支持使用SMSF通过Location信元携带的地址进行后续消息交互。
    >   **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**
    > 4. 打开获取IMEISV开关。如果需要获取用户设备标识，建议配置GETPEIPLCY参数为GETIMEISV(获取IMEISV)，这样AMF可直接向UE获取IMEISV，减少信令消耗。
    >   **[ADD NGPEIPLCY](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/业务安全管理/PEI策略管理/增加5G PEI策略（ADD NGPEIPLCY）_09651346.md)**
  L61:
    > 
    > ```
    > SET AMFPEERSELFUNC: NFLOCATION=SMSF-1;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（4）：['AUSFRESELEN', 'NFLOCATION', 'SCPRESELEN', 'SCPSEPPRESEL']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '全网规划': 2}（多值→atom 应考虑 decision_driven）
