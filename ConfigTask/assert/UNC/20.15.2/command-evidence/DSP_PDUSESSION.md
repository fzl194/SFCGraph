# 命令证据包：DSP PDUSESSION
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md`
> 用该命令的特性数：35

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询2G/3G/4G/5G的会话上下文信息。

如需查询QoS详细信息请参阅DSP SESSIONQOSINFO命令。

如需查询签约详细信息请参阅DSP SESSIONSUBDATA命令。
**notes（规格/上限→应投影 atom rule）**：
- - I-SMF/V-SMF不支持DSP PDUSESSION命令中指定地址（QUERYTYPE为IPV4ADDR或IPV6ADDR）查询会话信息。
- 使用SIMPLE（简约信息呈现）方式查询时，如果当前用户是2B2C漫游双DNN特性用户，且通用DNN会话是4G，专用DNN会话是5G场景，此时查询结果中，针对专用DNN会话的查询记录，EBI字段表示专用DNN会话的PDU Session ID，LB

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| QUERYTYPE | 查询方式 | local_planned | required | 无 | <br>- IMSI（用户IMSI号） |
| IMSI | IMSI | local_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。 |
| MSISDN | MSISDN | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~15。 |
| MEI | IMEI | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~16。 |
| DSPINFOTYPE | 信息呈现方式 | local_planned | conditional | SIMPLE | <br>- SIMPLE（简约信息呈现） |
| WLNETWKTYPE | 无线网络类型 | local_planned | conditional | 无 | <br>- NW2G3G4G（2/3/4G网络） |
| EBIORNSAPI | EBI或者NSAPI | local_planned | conditional | 无 | 整数类型，取值范围是1~15。 |
| PDUSESSIONID | PDU会话ID | local_planned | conditional | 无 | 整数类型，取值范围是1~255。 |
| QFI | QoS流ID | local_planned | conditional | 无 | 整数类型，取值范围是1~63。 |
| UEIPV4ADDR | 用户IPv4地址 | local_planned | conditional | 无 | IPv4地址类型。UE IPV4仅支持SIMPLE查询方式。 |
| UEIPV6ADDR | 用户IPv6地址 | local_planned | conditional | 无 | IPv6地址类型。UE IPV6仅支持SIMPLE查询方式。 |
| IPDOMAIN | 用户IP域 | local_planned | conditional | 无 | 字符串类型，输入长度范围是0~255。请根据运营商的规划，如果为IPv4类型的地址段划分了域，则需要 |
| ACCESSTYPE234G | 接入方式 | local_planned | conditional | 无 | <br>- AT_3GPP_ACCESS（3GPP_ACCESS） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-225003

**md：`WSFD-225003/调测5G LAN业务基本功能_38657599.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=SIMPLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 3. 查询用户的PDU会话信息确认会话是否符合预期。
    >   预期结果：UE的会话创建流程中，选择到IP地址为192.168.126.11的UPF插入了用户会话
    >   [**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)
    > 
    >   ```
  L33:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=SIMPLE;
    >   RETCODE = 0  操作成功  
    > 

### WSFD-225002

**md：`WSFD-225002/参考信息_58970872.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > - **[SET ADDRESSATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/全局地址分配属性配置/设置UE IP地址属性（SET ADDRESSATTR）_09653185.md)**
    > - **[ADD RESELECTUPCAUSE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UPF选择管理/故障原因值重选UPF/增加重选UPF的故障原因值（ADD RESELECTUPCAUSE）_06399908.md)**
    > - **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    > - **[LST ADDRESSATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/全局地址分配属性配置/查询UE IP地址属性（LST ADDRESSATTR）_09652481.md)**
    > - **[LST SECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址段管理/查询地址段（LST SECTION）_09651558.md)**

**md：`WSFD-225002/调测5G LAN跨SMF群组管理_58813376.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 
    > 1. 测试终端使用“data”DNN发起接入网络请求。
    > 2. 执行 ****DSP PDUSESSION**** 命令，通过测试终端的IMSI查看测试终端是否成功激活。
    >     - 如果测试终端激活成功，且使用的“IPv4 PDP address”与规划值一致，测试终端接入成功，调测结束。
    >     - 如果测试终端激活成功，但使用的“IPv4 PDP address”与规划值不一致，执行 [步骤 3](#ZH-CN_OPI_0000001558813376__step177831404618) 。

### WSFD-104001

**md：`WSFD-104001/调测IPv6承载上下文特性（AMF_SMF）_48043361.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 测试终端接入网络，指示用户IP地址类型为IPv6。
    > 4. 执行 [**DSP PDUSESSION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过IMSI查看测试终端承载信息。
    >     - 如果用户的缺省承载上下文动态信息中有一个IPv6地址，调测结束。
    >     - 如果用户的缺省承载上下文动态信息中没有IPv6地址，请参考[激活IPv6承载上下文特性（AMF/SMF）](激活IPv6承载上下文特性（AMF_SMF）_48043375.md)重新配置。

### WSFD-104002

**md：`WSFD-104002/WSFD-104002 IPv4v6双栈接入（5G）参考信息_48043365.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**DSP PDUSESSION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)
    > 
    > #### [告警](#ZH-CN_CONCEPT_0248043365)

**md：`WSFD-104002/调测IPv4v6双栈接入特性_48043390.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 测试终端接入网络，指示用户IP地址类型为IPv4v6。
    > 4. 执行 [**DSP PDUSESSION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过IMSI查看测试终端承载信息。
    >     - 如果用户的缺省承载上下文动态信息中“实际使用的PDN类型”为“IPv4v6”，调测结束。
    >     - 如果用户的缺省承载上下文动态信息中“实际使用的PDN类型”不为“IPv4v6”，请参考[激活IPv4v6双栈接入特性](激活IPv4v6双栈接入特性_48043372.md)重新配置。

### WSFD-108002

**md：`WSFD-108002/调测基于预定义规则的分流策略控制_28860591.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：UE的会话创建流程中，选择到IP地址为192.168.126.11的ULCL UPF插入了用户会话。
    > 
  L36:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

### WSFD-108004

**md：`WSFD-108004/调测MEC冗余模式故障保护_28860594.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L31:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：选择到IP地址为192.168.126.11的 **ULCL UPF+辅锚点UPF1** 。
    > 
  L35:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 
  L53:
    > 4. 构造故障场景：断开SMF和 **ULCL UPF+辅锚点UPF1** 的连接。
    > 5. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：选择到IP地址为192.168.126.12的 **ULCL UPF+辅锚点UPF2** 。
    > 

### WSFD-108005

**md：`WSFD-108005/调测MEC单点模式故障保护_30792897.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：选择到IP地址为192.168.126.12的 **ULCL UPF+辅锚点UPF1** 。
    > 
  L39:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 
  L57:
    > 4. 构造故障场景：断开SMF和 **ULCL UPF+辅锚点UPF1** 的连接。
    > 5. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：选择到IP地址为192.168.126.11的 **UPF PSA1** 。
    > 

### WSFD-223001

**md：`WSFD-223001/调测基于位置信息的分流策略控制（SMF）_07996028.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：UE的会话创建流程中，选择到IP地址为192.168.126.11的ULCL UPF插入了用户会话。
    > 
  L36:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

### WSFD-223003

**md：`WSFD-223003/调测基于漫游地动态签约的分流策略控制（SMF）_82779461.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L31:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：UE的会话创建流程中，选择到IP地址为192.168.126.11的ULCL UPF插入了用户会话。
    > 
  L35:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

### WSFD-223004

**md：`WSFD-223004/WSFD-223004 基于动态规则的分流策略控制参考信息_47837467.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0000001147837467)

**md：`WSFD-223004/调测基于动态规则的分流策略控制_01437552.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：UE的会话创建流程中，选择到IP地址为192.168.126.11的ULCL UPF插入了用户会话。
    > 
  L36:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

### WSFD-223006

**md：`WSFD-223006/调测基于DNN插入I-UPF_86651124.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户1的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：会话创建成功，且选择到IP地址为192.168.126.11的支持园区1专用DNN的UPF。
    > 4. 用户1移动，出园区1覆盖区域，再发起PDU会话创建流程。
  L41:
    > 4. 用户1移动，出园区1覆盖区域，再发起PDU会话创建流程。
    > 5. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：PDU会话创建失败，且失败原因是“特定切片和DNN的资源不足”。
    > 6. 用户2进入其园区2覆盖区域，发起PDU会话建立流程。
  L46:
    > 7. 进入 “MML命令行-UNC” 窗口。
    > 8. 查询用户2的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：会话创建成功，且选择到IP地址为192.168.126.21的支持园区2专用DNN的UPF。
    > 9. 用户2移动，出园区2覆盖区域，再发起PDU会话创建流程。

### WSFD-010502

**md：`WSFD-010502/调测静态地址分配IPv4地址功能_67401513.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 
    > 1. 测试终端使用“apn-test”APN发起接入网络请求，创建PDU会话标识为1的PDU会话。
    > 2. 进入 “MML命令行-UNC” 窗口。 执行 **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否成功激活。
    >     - 如果测试终端激活成功，且使用的 “用户IP地址” 与 “UP的PFCP IPv4地址” 与规划值一致，测试终端接入成功，调测结束。
    >     - 如果测试终端激活成功，但使用的 “用户IP地址” 或 “UP的PFCP IPv4地址” 与规划值不一致，执行 [3](#ZH-CN_OPI_0167401513__step6105132822616) 。

### WSFD-107021

**md：`WSFD-107021/调测静态地址用户路由冗余_76652608.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 测试终端使用“apn-test”APN发起接入网络请求，创建PDU会话标识为5的PDU会话。
    > 2. 进入 “MML命令行-UNC” 窗口。
    >   执行 **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否成功激活。
    >     - 如果测试终端激活成功，且使用的 “用户IP地址” 与 “UP的PFCP IPv4地址” 与 **主用UP** **F** 规划值一致，测试终端接入成功，调测结束。
    >     - 如果测试终端激活成功，但使用的 “用户IP地址” 或 “UP的PFCP IPv4地址” 与主用UPF规划值不一致，执行 [6](#ZH-CN_OPI_0276652608__cmd1105112822613) 。
  L43:
    > 4. 测试终端使用“apn-test”APN重新发起接入网络请求，创建PDU会话标识为5的PDU会话。
    > 5. 进入 “MML命令行-UNC” 窗口。
    >   执行 **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否成功激活。
    >     - 如果测试终端激活成功，且使用的 “用户IP地址” 与 “UP的PFCP IPv4地址” 与 **备用UPF** 规划值一致，测试终端接入成功，调测结束。
    >     - 如果测试终端激活成功，但使用的 “用户IP地址” 或 “UP的PFCP IPv4地址” 与备用UPF规划值不一致，执行 [6](#ZH-CN_OPI_0276652608__cmd1105112822613) 。

### WSFD-107020

**md：`WSFD-107020/调测支持基于UPF位置的DNS选择_76304919.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=SIMPLE;`
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=SIMPLE;`
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户PDU会话的会话ID。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：查询到PDU会话ID作为后续详细查询的PDU会话输入参数。
    >   ```
  L36:
    >   预期结果：查询到PDU会话ID作为后续详细查询的PDU会话输入参数。
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=SIMPLE;
    >   RETCODE = 0  操作成功  
    > 
  L49:
    >   ```
    > 4. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：以激活支持基于UPF位置的DNS选择的任务示例为例，PDU会话信息中的UPF是为终端选择的IP地址为"10.2.2.2"的UPF，IP地址为"10.1.1.1"的主DNS服务器，IP地址为"10.12.12.12"的备DNS服务器。
    > 

### WSFD-223002

**md：`WSFD-223002/调测公私网协同访问（含共享UPF选择）_15100010.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=SIMPLE;`
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户PDU会话的会话ID。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：查询到PDU会话ID作为后续详细查询的PDU会话输入参数。
    >   ```
  L35:
    >   预期结果：查询到PDU会话ID作为后续详细查询的PDU会话输入参数。
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=SIMPLE;
    >   RETCODE = 0  操作成功  
    > 
  L48:
    >   ```
    > 4. 查询用户PDU会话的用户面信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：PDU会话信息中的用户面地址是预期为用户选择的共享UPF地址。
    >   ```

### WSFD-213001

**md：`WSFD-213001/WSFD-213001 CU FullMesh组网参考信息_72288618.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - **[**RMV UPIPDOMAIN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UPF IP Domain管理/删除当前UPF绑定的IP域（RMV UPIPDOMAIN）_09652498.md)**
    > - **[**LST UPIPDOMAIN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UPF IP Domain管理/查询当前UPF绑定的IP域（LST UPIPDOMAIN）_09651493.md)**
    > - **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    > - **[**ADD SECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址段管理/增加地址段（ADD SECTION）_09651691.md)**
    > - **[**RMV SECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址段管理/删除地址段（RMV SECTION）_09654197.md)**

**md：`WSFD-213001/调测CU FullMesh组网（SMF）_51528857.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 
    > 1. 测试终端使用“data”DNN发起接入网络请求。
    > 2. 执行 ****DSP PDUSESSION**** 命令，通过测试终端的IMSI查看测试终端是否成功激活。
    >     - 如果测试终端激活成功，且使用的“IPv4 PDP address”与规划值一致，测试终端接入成功，调测结束。
    >     - 如果测试终端激活成功，但使用的“IPv4 PDP address”与规划值不一致，执行 [步骤 3](#ZH-CN_OPI_0000001151528857__step177831404618) 。

### WSFD-217001

**md：`WSFD-217001/WSFD-217001 用户面业务通道保活参考信息_04444264.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - **[SET PFCPPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP路径管理/PFCP路径参数管理/设置PFCP参数（SET PFCPPARA）_09652597.md)**
    > - **[LST PFCPPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP路径管理/PFCP路径参数管理/查询PFCP参数（LST PFCPPARA）_09651492.md)**
    > - **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    > - **[DSP PFCPPATHINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP路径管理/PFCP路径查询/显示PFCP链路相关数据（DSP PFCPPATHINFO）_10290311.md)**
    > 

**md：`WSFD-217001/实现原理_07860300.md`**
- 操作步骤上下文（±2 行原文）：
  L93:
    > - 进入惯性运行的用户状态查询：
    >     - 通过命令“**[DSP NGMMCTX](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/用户数据库管理/显示5G移动性管理上下文（DSP NGMMCTX）_09651524.md)**”在AMF上基于IMSI/MSISDN查询用户是否进入惯性运行状态以及进入惯性运行状态的开始时间。
    >     - 通过命令“**[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**”在SMF上基于IMSI/MSISDN查询用户是否进入惯性运行状态以及进入惯性运行状态的开始时间。

**md：`WSFD-217001/调测用户面业务通道保活（SMF）_07860926.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > 
    > 1. 在SMF上创建一个用户跟踪，参数 “IMSI” 填写被跟踪的园区用户A的IMSI。
    > 2. 用户A正常入网，进行业务。使用“ **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** ”命令查询用户上下文信息。
    > 3. 构造N2接口和N4接口同时故障的场景。
    > 4. N4故障检测期间，使用命令“ **[DSP SESSIONIOINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询会话惯性运行信息/显示会话惯性运行信息（DSP SESSIONIOINFO）_80169068.md)** ”查询用户A的某会话是否进入预惯性运行状态。
  L42:
    >     - UPF已进入惯性运行状态，执行[5](#ZH-CN_OPI_0307860926__step6348735172417)。
    >     - UPF未进入惯性运行状态，请参考[激活用户面业务通道保活（SMF）](激活用户面业务通道保活（SMF）_07860925.md)进行相关配置，然后重新执行步骤1~4。
    > 6. 使用命令“ **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** ”查询用户A是否进入惯性运行状态。
    >     - 是，调测结束。
    >     - 否，请参考[激活用户面业务通道保活（SMF）](激活用户面业务通道保活（SMF）_07860925.md)进行相关配置，然后重新执行步骤1~4。

### WSFD-106303

**md：`WSFD-106303/WSFD-106303 基于ARP的差异化服务参考信息（适用于GGSN、SGW-C、PGW-C）_40400505.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > - **[SET APNACCESSCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md)**
    > - **[LST APNACCESSCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/查询APN访问控制参数（LST APNACCESSCTRL）_09652260.md)**
    > - **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0000001440400505)

**md：`WSFD-106303/调测基于ARP的差异化服务（适用于GGSN、SGW-C、PGW-C）_39200897.md`**
- 操作步骤上下文（±2 行原文）：
  L67:
    > 
    >       ![](调测基于ARP的差异化服务（适用于GGSN、SGW-C、PGW-C）_39200897.assets/zh-cn_image_0000001462783685_2.png)
    >     c. 执行**[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**命令，查询用户上下文信息。
    >       **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** : QUERYTYPE=IMSI, IMSI="123451234512345";
    >       预期结果：该用户上下文不存在，说明达到PDP数拒绝告警门限后成功拒绝该级别的用户接入，执行 [步骤 1.f.4](#ZH-CN_OPI_0000001439200897__li19486142795) 。
  L68:
    >       ![](调测基于ARP的差异化服务（适用于GGSN、SGW-C、PGW-C）_39200897.assets/zh-cn_image_0000001462783685_2.png)
    >     c. 执行**[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**命令，查询用户上下文信息。
    >       **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** : QUERYTYPE=IMSI, IMSI="123451234512345";
    >       预期结果：该用户上下文不存在，说明达到PDP数拒绝告警门限后成功拒绝该级别的用户接入，执行 [步骤 1.f.4](#ZH-CN_OPI_0000001439200897__li19486142795) 。
    >       异常结果：上下文存在，请执行 [步骤 1.g](#ZH-CN_OPI_0000001439200897__li149715254129) 。
  L72:
    >       异常结果：上下文存在，请执行 [步骤 1.g](#ZH-CN_OPI_0000001439200897__li149715254129) 。
    >     d. 改变用户接入优先级别为1（高优先级用户），再次激活。
    >     e. 执行**[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**命令，查询上下文。
    >       **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** : QUERYTYPE=IMSI, IMSI="123451234512345";
    >       预期结果：该用户上下文存在，说明高级别的用户可以成功接入，执行 [步骤 1.f.6](#ZH-CN_OPI_0000001439200897__li14830270915) 。

### WSFD-109304

**md：`WSFD-109304/调测缺省承载GBR保障_40491397.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    >   如下以PGW-C与PCRF之间是Gx接口为例进行描述。如实际使用的是N7接口，交互消息为Npcf_SMPolicyControl_Create request和Npcf_SMPolicyControl_Create response。
    > 3. 测试终端使用APN“apn-test”接入网络。
    > 4. 行 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否激活成功。
    >     - 是，请执行[步骤 5](#ZH-CN_OPI_0000001240491397__step03685065417)。
    >     - 否，请联系华为技术工程师确保用户激活成功后，重新执行[步骤 3](#ZH-CN_OPI_0000001240491397__step1816324655316)。

### WSFD-109101

**md：`WSFD-109101/调测PCC基本功能_45059543.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION: QUERYTYPE=IMSI, IMSI="460000123456789", DSPINFOTYPE=SIMPLE;`
  `DSP PDUSESSION: QUERYTYPE=IMSI, IMSI="460000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L55:
    >   ```
    > 5. 测试终端使用APN“apn-test”接入网络。
    > 6. 执行 **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否激活成功且APN正确。
    >   ```
    >   DSP PDUSESSION: QUERYTYPE=IMSI, IMSI="460000123456789", DSPINFOTYPE=SIMPLE;
  L57:
    > 6. 执行 **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否激活成功且APN正确。
    >   ```
    >   DSP PDUSESSION: QUERYTYPE=IMSI, IMSI="460000123456789", DSPINFOTYPE=SIMPLE;
    >   ```
    >     - 是，请执行[步骤 7](#ZH-CN_OPI_0000001245059543__step4630171816912)。
  L61:
    >     - 是，请执行[步骤 7](#ZH-CN_OPI_0000001245059543__step4630171816912)。
    >     - 否，请联系PCF工程师确保PCF状态正常后重新执行[步骤 5](#ZH-CN_OPI_0000001245059543__step1816324655316)。
    > 7. 执行 **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看PCF ID是否正确。
    >   本举例中， “PCF ID” 为 “testPcfInstanceID” ，表明PCF ID正确。
    >   // “PDUSESSIONID” 和 “QFI” 从 [步骤 6](#ZH-CN_OPI_0000001245059543__step435410517284) 的显示结果中获取，即 “PDU会话ID” 和 “QoSFlow 5QI优先级” 参数值。

### WSFD-109105

**md：`WSFD-109105/调测基于位置的业务管理_79067182.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    > 3. 创建用户跟踪任务，消息类型选择N4。
    > 4. 测试终端使用“example.com”发起接入网络请求。
    > 5. 执行 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否激活成功。
    >     - 激活成功且查询的用户IP地址与规划值一致，调测结束。
    >     - 激活成功但查询的用户IP地址与规划值不一致，请执行[步骤 6](#ZH-CN_OPI_0279067182__step4667203213400)。

### WSFD-109108

**md：`WSFD-109108/调测基于接入点策略控制_79943605.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 3. 创建用户跟踪任务，消息类型选择N4、Gx和N7。
    > 4. 测试终端使用APN“huawei.com”发起接入网络请求。
    > 5. 执行 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否激活成功。
    >     - 激活成功且“用户IP地址”与规划值一致，请记录用户IP（IP1），然后执行[步骤 6](#ZH-CN_OPI_0279943605__step4667203213400)。
    >     - 激活失败，请调测基本会话接入功能。

### WSFD-211005

**md：`WSFD-211005/调测基于业务感知的带宽控制_79619227.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 3. 创建用户跟踪任务，消息类型选择N4/Gx/N7。
    > 4. 测试终端使用“huawei.com”发起接入网络请求。
    > 5. 执行 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 命令，通过测试终端的IMSI查看测试终端是否激活成功。
    >     - 是，请执行[步骤 6](#ZH-CN_OPI_0279619227__step4667203213400)。
    >     - 否，请联系华为技术支持工程师调测基本会话接入功能。

### WSFD-011310

**md：`WSFD-011310/调测PLMN标识获取_66289936.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 终端携带192.168.1.24的地址激活用户。
    > 2. 测试终端访问业务，调测PLMN标识获取功能。
    > 3. 进入 “MML命令行-UNC” 窗口。 执行命令 **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 查询UE的会话信息。
    >     - 终端成功接入网络后，通过第三方抓包工具查看相关报文信息，报文信息与规划一致，则调试结束。
    >     - 终端成功接入网络后，通过第三方抓包工具查看相关报文信息，报文信息与规划不一致，查询结果与预期不一致，请参考 [激活PLMN标识获取重新配置](激活PLMN标识获取_66289935.md) 。

### WSFD-011305

**md：`WSFD-011305/调测Radius鉴权接入_50176280.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=1, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：用户接入成功。
    > 
  L41:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=1, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

**md：`WSFD-011305/调测本地鉴权接入_95351133.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
  L41:
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

**md：`WSFD-011305/调测透明接入_95351130.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
  L39:
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

**md：`WSFD-011305/调测透明鉴权接入_95351132.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L42:
    > 3. 进入 “MML命令行-UNC” 窗口。
    > 4. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
  L44:
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

**md：`WSFD-011305/调测非透明接入_95351131.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L42:
    > 3. 进入 “MML命令行-UNC” 窗口。
    > 4. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
  L44:
    >   **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

### WSFD-104509

**md：`WSFD-104509/调测SGSN的黑白名单_76495252.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW2G3G4G, PDUSESSIONID=5, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L38:
    > 2. 终端携带MME地址10.200.0.2接入网络。10.200.0.2不在SGSN/MME/SGW-C的黑名单地址段内。
    >   预期结果：终端激活成功。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：PDU会话信息中的CP的PFCP IPv4地址是不在SGSN/MME/SGW-C黑名单中的10.200.0.2。
    > 
  L42:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW2G3G4G, PDUSESSIONID=5, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

### WSFD-205015

**md：`WSFD-205015/调测SMF支持多服务区特性_76051542.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 4. 在AMF的命令执行窗口，针对SMF1和SMF2分别执行**[DSP NFCACHE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF Cache管理/查询NF缓存信息（DSP NFCACHE）_09651365.md)**，查询缓存的smfInfoList信息。
    >   预期结果：查询结果中NFProfile同时包含smfInfo和smfInfoList，其中smfInfo信息中包括该SMF优选支持的区域信息，smfInfoList信息中包括该SMF非优选支持的区域信息。SMF1的smfInfo信息中包括TAC1、TAC3、TAC11~TAC19，smfInfoList信息中包括TAC2、TAC4、TAC21~TAC29。SMF2的smfInfo信息中包括TAC2、TAC4、TAC21~TAC29，smfInfoList信息中包括TAC1、TAC3、TAC11~TAC19。
    > 5. 在SMF1的命令执行窗口，执行**[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**。
    >   预期结果：可查看到UE1的PDU会话信息。
    > 6. 让用户UE1移动，从TAC1移动到TAC2（345012000002）。
  L39:
    >   预期结果：可查看到UE1的PDU会话信息。
    > 6. 让用户UE1移动，从TAC1移动到TAC2（345012000002）。
    > 7. 在SMF1的命令执行窗口，执行**[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**。
    >   预期结果：可查看到UE1的PDU会话信息。
    > 8. 用户UE2接入网络，接入位置为TAC2（345012000002）。
  L44:
    > 9. 在AMF的命令执行窗口，执行**[DSP NFCACHE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF Cache管理/查询NF缓存信息（DSP NFCACHE）_09651365.md)**。
    >   预期结果：对于SMF1和SMF2，使用SMF实例ID查询出的TAI列表中都包含TAC2。
    > 10. 在SMF2的命令执行窗口，执行**[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**。
    >   预期结果：可查看到UE2的PDU会话信息。

### WSFD-102101

**md：`WSFD-102101/调测VoLTE紧急呼叫（适用于SGW-C_PGW-C）_95090216.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION`
- 操作步骤上下文（±2 行原文）：
  L61:
    >     - 如果“cause-result”值为“16”，如[图2](#ZH-CN_OPI_0295090216__fig4)所示，请执行[7](#ZH-CN_OPI_0295090216__cmd1833593302184656)。
    >     - 如果“cause-result”值不为“16”，请参考故障案例进行调测。
    > 7. 执行 [**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过 测试终端 的IMSI查看 测试终端 用户信息。
    >   ```
    >   DSP PDUSESSION
  L63:
    > 7. 执行 [**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过 测试终端 的IMSI查看 测试终端 用户信息。
    >   ```
    >   DSP PDUSESSION
    >   :QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW2G3G4G, EBIORNSAPI=5, ACCESSTYPE234G=AT_3GPP_ACCESS;
    >   ```

**md：`WSFD-102101/调测VoWIFI紧急呼叫_95090217.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION`
- 操作步骤上下文（±2 行原文）：
  L59:
    >     - 如果“cause-result”值为“16”，如[图2](#ZH-CN_OPI_0295090217__fig4)所示，请执行[7](调测VoLTE紧急呼叫（适用于SGW-C_PGW-C）_95090216.md#ZH-CN_OPI_0295090216__cmd1833593302184656)。
    >     - 如果“cause-result”值不为“16”，请参考故障案例进行调测。
    > 7. 执行 [**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过 测试终端 的IMSI查看 测试终端 用户信息。
    >   ```
    >   DSP PDUSESSION
  L61:
    > 7. 执行 [**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过 测试终端 的IMSI查看 测试终端 用户信息。
    >   ```
    >   DSP PDUSESSION
    >   :QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW2G3G4G, EBIORNSAPI=5, ACCESSTYPE234G=AT_UNTRUSTED_NON_3GPP_ACCESS;
    >   ```

### WSFD-102202

**md：`WSFD-102202/WSFD-102202 P-CSCF故障时IMS业务恢复参考信息_26216213.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[SET NGIMSVOPS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/设置VoPS配置（SET NGIMSVOPS）_09653214.md)**
    > - **[LST NGIMSVOPS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/查询VoPS配置（LST NGIMSVOPS）_09653054.md)**
    > - **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    > - [**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)
    > - **[LST APNQOSATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/查询指定APN的QoS属性配置信息（LST APNQOSATTR）_09651477.md)**

### WSFD-102701

**md：`WSFD-102701/WSFD-102701 VoNR基础语音业务参考信息_11685430.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[**SET NGIMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/设置VoPS配置（SET NGIMSVOPS）_09653214.md)**
    > - **[**LST NGIMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/查询VoPS配置（LST NGIMSVOPS）_09653054.md)**
    > - **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    > - **[**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)**
    > - **[**LST APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/查询APN的IMS属性（LST APNIMSATTR）_09653158.md)**

**md：`WSFD-102701/调测VoNR基础语音业务_11845318.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    >     a. 在AMF的OM Portal上创建用户跟踪任务。5G用户开机注册。
    >     b. 查询用户上下文的用户状态信息。
    >       进入 “MML命令行-UNC” 窗口。 执行命令 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 查询用户在5G网络下的PDU会话。如果为IMS的PDU会话，则 “APN” 为 “ ims” 。
    >       预期结果：用户在5G网络有数据PDU会话和IMS的PDU会话。
    >     c. 查看AMF上用户跟踪。
  L49:
    >             预期结果：NG RAN回复PDU Session Resource Modify Response携带成功建立QoS Flow的信息，同时通过Uplink NAS消息将UE返回的PDU Session Modification Complete消息透传给AMF。
    >     d. 语音业务执行成功。
    >       进入 “MML命令行-UNC” 窗口。 执行命令 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** ，查询用户在5G网络下的PDU会话。
    >       预期结果：用户在5G网络有VoNR语音专载，存在5QI=1的QoS Flow。
    >     e. 若涉及4G/5G互操作流程，切换流程调测参见 [调测5G SA到LTE网络间切换](../../../../业务专题/5G Core 4_5G互操作解决方案/调测指导/调测5G SA到LTE网络间切换_01_10043.md) 。

### WSFD-102702

**md：`WSFD-102702/WSFD-102702 EPS Fallback参考信息_82764866.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[**SET NGIMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/设置VoPS配置（SET NGIMSVOPS）_09653214.md)**
    > - **[**LST NGIMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/查询VoPS配置（LST NGIMSVOPS）_09653054.md)**
    > - **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    > - **[**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)**
    > - **[**LST APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/查询APN的IMS属性（LST APNIMSATTR）_09653158.md)**

**md：`WSFD-102702/调测EPS Fallback_82220358.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >     a. 在MME、AMF的OM Portal上创建用户跟踪任务。5G用户开机注册。
    >     b. 查询用户上下文的用户状态信息。
    >       进入 “MML命令行-UNC” 窗口。 执行命令 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 查询用户在5G网络下的PDU会话。如果为IMS的PDU会话，则 “APN或者DNN” 为 “ ims” 。
    >       预期结果：用户在5G网络有数据PDU会话和IMS的PDU会话。
    >     c. 查看AMF上用户跟踪。
  L58:
    >       预期结果：被叫响铃，接通被叫。
    >     f. 语音业务执行成功。
    >       进入 “MML命令行-UNC” 窗口。 执行命令 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** （参数DSPINFOTYPE为DETAILED，WLNETWKTYPE为NW2G3G4G），查询用户在4G网络下的PDN连接。
    >       预期结果：用户在4G网络有VoLTE语音专载。
    >     g. 如果 [2.b](#ZH-CN_OPI_0182220358__substep4123184655110) ~ [2.f](#ZH-CN_OPI_0182220358__substep71255433249) 查看非预期结果，先参考 [激活EPS Fallback](激活EPS Fallback_76175590.md) 排查配置是否正确，若配置正确则执行 [3](#ZH-CN_OPI_0182220358__step2091112885113) 。

### WSFD-102703

**md：`WSFD-102703/调测EPS Fallback紧急呼叫_26162694.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >   ![](调测EPS Fallback紧急呼叫_26162694.assets/zh-cn_image_0000001090925470_2.png)
    > 6. UE主动发起紧急呼叫语音业务，语音业务执行成功。
    >   进入 “MML命令行-UNC” 窗口。 执行命令 **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** （参数DSPINFOTYPE为DETAILED，WLNETWKTYPE为NW2G3G4G），查询用户在4G网络下的PDN连接。
    >   如果为IMS的PDU会话，则 “APN或者DNN” 为 “ims” 。
    >   预期结果：用户在4G网络有紧急呼叫的VoLTE语音专载，且有QCI=5的默认承载。

### WSFD-102706

**md：`WSFD-102706/调测VoNR紧急呼叫_46687733.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >     b. 5G用户开机注册。
    >     c. 查询用户上下文的用户状态信息。
    >       进入 “MML命令行-UNC” 窗口。 执行命令 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 查询用户在5G网络下的PDU会话。如果为IMS的PDU会话，则 “APN” 为 “ ims” 。
    >       预期结果：用户在5G网络有IMS的PDU会话。
    >     d. 查询用户环境APN配置情况。

### WSFD-107019

**md：`WSFD-107019/调测P-CSCF选择_62638765.md`**
- 任务示例脚本（该命令行）：
  `DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=1, QFI=1;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询用户的PDU会话信息。
    >   **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
    >   预期结果：PDU会话信息中的P-CSCF是根据用户位置信息为终端选择的IP地址为"10.130.228.70"的P-CSCF。
    > 
  L37:
    > 
    >   ```
    >   DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=1, QFI=1;
    >   RETCODE = 0  操作成功  
    > 

### WSFD-221005

**md：`WSFD-221005/调测SMF故障下的业务恢复_37390847.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > 3. UE开机、附着到网络，并建立IMS语音PDU会话。
    > 4. 执行下述命令，查询用户的IMS语音上下文信息。
    >   执行命令 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 查询用户在5G网络下的PDU会话。如果为IMS的PDU会话，则 “APN” 为 “ IMS” 。
    >   预期结果：用户在5G网络有数据PDU会话和IMS的PDU会话。
    > 5. 验证在SMF故障场景下，用户语音业务恢复功能。
  L45:
    >           b. 重启用户接入的SMF。
    >           c. 执行下述命令查询用户接入的SMF信息。
    >             **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** : QUERYTYPE=IMSI, IMSI="460031700100001", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >             预期结果：通过观察IMS语音PDU会话信息发现UE接入的SMF控制面IP地址（ “控制面接入连接右端IP” ）和 “用户激活时间” 均发生改变。
    >     - 验证当SMF故障，AMF启用数据业务请求恢复方式，SMF上“VOICEDNN”范围的语音用户有数据业务请求时，恢复语音业务。
  L52:
    >           c. 用户发起数据业务请求（用户主动发起Service Request，重选SMF）。
    >           d. 执行下述命令查询用户接入的SMF信息。
    >             **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** : QUERYTYPE=IMSI, IMSI="460031700100001", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
    >             预期结果：通过观察IMS语音PDU会话信息发现UE接入的SMF控制面IP地址（ “控制面接入连接右端IP” ）和 “用户激活时间” 均发生改变。

## ④ 自动比对
- 命令真相参数（13）：['ACCESSTYPE234G', 'DSPINFOTYPE', 'EBIORNSAPI', 'IMSI', 'IPDOMAIN', 'MEI', 'MSISDN', 'PDUSESSIONID', 'QFI', 'QUERYTYPE', 'UEIPV4ADDR', 'UEIPV6ADDR', 'WLNETWKTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
