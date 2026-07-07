# 命令证据包：SET LICENSESWITCH
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md`
> 用该命令的特性数：213

## ② 命令真相（mml_commands.jsonl）
**功能**：该命令用于设置License项的配置开关。当License文件中含有某功能的许可时，通过此命令可以设置该功能是否开通。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 当license文件未激活时，无法设置任何license项，激活后只能设置已购买且支持配置开关的license项。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| LICITEM | SWITCH |
| --- | --- |
| LKV4W9B

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| LICITEM | License项 | local_planned | required | 无。 | 字符串类型，输入长度范围是0~255。 |
| SWITCH | 开关 | local_planned | required | 无。 | <br>- “ENABLE（开）”：开启License控制项 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-225002

**md：`WSFD-225002/参考信息_58970872.md`**
- 操作步骤上下文（±2 行原文）：
  L9:
    > 本特性相关的MML命令如下：
    > 
    > - **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > - **[SET ADDRESSATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/全局地址分配属性配置/设置UE IP地址属性（SET ADDRESSATTR）_09653185.md)**
    > - **[ADD RESELECTUPCAUSE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UPF选择管理/故障原因值重选UPF/增加重选UPF的故障原因值（ADD RESELECTUPCAUSE）_06399908.md)**

**md：`WSFD-225002/激活5G LAN跨SMF群组管理_09652117.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CUFMN01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 
    > 1. 打开本特性的License配置开关。对应的License控制项为"82209930 LKV2CUFMN01 CU FullMesh组网"。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 2. 配置地址分配方式。
    >   **[SET ADDRESSATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/全局地址分配属性配置/设置UE IP地址属性（SET ADDRESSATTR）_09653185.md)**
  L53:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CUFMN01",SWITCH=ENABLE;
    > ```
    > 

### WSFD-216001

**md：`WSFD-216001/激活eMTC终端省电PSM模式_77396101.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2M2MS02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L56:
    >       [**MOD M2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/修改M2M策略参数(MOD M2MPLCY)_72345365.md)
    > 3. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277396101)
  L75:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2M2MS02", SWITCH=ENABLE;
    > ```

### WSFD-216002

**md：`WSFD-216002/激活eMTC eDRX模式（适用于MME）_77396103.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EDRX02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L67:
    >   > “宽带S1模式寻呼时间窗口时长” 设置时，建议WBPTW的值至少为DefaultPagingDRX值的2倍，这样eNodeB在WBPTW窗口内可以有多次机会寻呼用户。Default Paging DRX值是eNodeB在S1 Setup Request消息中携带给MME的。
    > 5. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 6. **可选：**如果eMTC终端需要添加RAT Type为LTE-M类型时，需要执行此步骤。
    >     a. 将RAT Type为LTE-M的消息传递给SGW-C。
  L109:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EDRX02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-216002/激活eMTC eDRX模式（适用于SGW-C）_78638572.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WMTDRX11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0278638572)
  L43:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WMTDRX11",SWITCH=ENABLE;
    > ```

**md：`WSFD-216002/调测eMTC eDRX模式（适用于SGW-C）_78638573.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    >   [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3WMTDRX11";
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0278638573__step2)。
    >     - 如果“SWITCH”为“DISABLE”，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 在OM Portal上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择GTPC、UP DATA和DOWN DATA消息类型。
    > 4. 测试终端使用“test”APN接入网络，并进行下行数据业务。激活用户，并跟踪该用户消息。

### WSFD-216101

**md：`WSFD-216101/激活eMTC基于延迟定时器的信令拥塞控制（适用于MME）_77897410.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LTCC02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本功能的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 设置低优先级APN流控。
    >     a. 增加APNNI组。
  L79:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LTCC02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-216101/调测eMTC基于延迟定时器的信令拥塞控制（适用于MME）_77897411.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 查询 基于延迟定时器的信令拥塞控制 对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0277897411__cmd7195778175821)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 2. 执行 **[LST LOWPRIAPNFC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/操作维护/设备管理/流控管理/业务流控管理/低优先级APN流控管理/查询低优先级APN流控参数（LST LOWPRIAPNFC）_26146158.md)** 命令查看低优先级APN流控功能开关是否打开。
    >     - 如果参数配置为ON，请执行[3](#ZH-CN_OPI_0277897411__step17368152112206)。

**md：`WSFD-216101/激活eMTC基于延迟定时器的信令拥塞控制（适用于PGW-C）_77897405.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WMTSBT11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 设置全局Back-Off时长。
    >   **[SET GBACKOFFTIME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/流控管理/全局Back-off Time信息/设置全局Back-off Time信息（SET GBACKOFFTIME）_76686936.md)**
  L53:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WMTSBT11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-216101/调测eMTC基于延迟定时器的信令拥塞控制（适用于PGW-C）_77897406.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 查询 基于延迟定时器的信令拥塞控制 对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0277897406__step877713597511)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 2. 构造PGW-C系统过载。
    > 3. 调测终端开机，并进行业务访问试图建立PDN连接。观察PGW-C返回的失败响应消息。

### WSFD-216102

**md：`WSFD-216102/激活eMTC基于eNodeB覆盖等级的寻呼_77396885.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CELP02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    >   [**SET S1CMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md)
    > 4. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277396885)
  L64:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CELP02", SWITCH=ENABLE;
    > ```

**md：`WSFD-216102/调测eMTC基于eNodeB覆盖等级的寻呼_77528849.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2CELP01 | 本端规划 | 确认license已经打开 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 确认license已经打开 |

### WSFD-216103

**md：`WSFD-216103/激活eMTC低优先级接入控制_77396886.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LPAC02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L42:
    >   [**SET LOWPRIOFC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/操作维护/设备管理/流控管理/业务流控管理/低优先级接入流控管理/设置低优先级流控参数(SET LOWPRIOFC)_72345759.md)
    > 3. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277396886)
  L61:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LPAC02", SWITCH=ENABLE;
    > ```

### WSFD-216104

**md：`WSFD-216104/激活基于APN的eMTC终端接入速率控制_77396887.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3WMTARC11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITC**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 开启基于APN的APN速率控制功能。
    >   [**SET APNRATECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md)
  L58:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3WMTARC11",SWITCH=ENABLE;
    > ```
    > 

### WSFD-216105

**md：`WSFD-216105/激活基于服务PLMN的eMTC终端接入速率控制_77396889.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WMTPRC11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 开启Serving PLMN速率控制功能。
    >     - 开启基于APN的Serving PLMN速率控制功能。
  L59:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WMTPRC11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-216105/调测基于服务PLMN的eMTC终端接入速率控制_77396890.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查看回显中是否允许使用基于服务PLMN的eMTC终端接入速率控制功能。
    >     - 如果“ 开关”为“使能”，请执行[步骤 3](#ZH-CN_OPI_0277396890__step2)。
    >     - 如果“ 开关”为“不使能”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关
    > 3. 执行 [**LST APNPLMNRATECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/查询APN Serving PLMN速率控制配置（LST APNPLMNRATECTRL）_64343876.md) 命令查看基于APN的Serving PLMN速率控制功能是否开启。
    >   ```

### WSFD-104001

**md：`WSFD-104001/激活IPv6承载上下文特性（AMF_SMF）_48043375.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2IPV6AM01",SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2IPV6SM01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开IPv6承载上下文特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0248043375)
  L43:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPV6AM01",SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IPV6SM01",SWITCH=ENABLE;
    > ```
  L44:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPV6AM01",SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IPV6SM01",SWITCH=ENABLE;
    > ```

**md：`WSFD-104001/调测IPv6承载上下文特性（AMF_SMF）_48043361.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询IPv6承载上下文对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，流程结束。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 测试终端接入网络，指示用户IP地址类型为IPv6。
    > 4. 执行 [**DSP PDUSESSION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过IMSI查看测试终端承载信息。

**md：`WSFD-104001/激活IPv6承载上下文特性（适用于MME、SGW-C_PGW-C）_48043351.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开IPv6承载上下文特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0248043351)
  L41:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;
    > ```
  L42:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;
    > ```

**md：`WSFD-104001/调测IPv6承载上下文特性（适用于MME、SGW-C_PGW-C）_48043381.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询IPV6承载上下文对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，流程结束。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。

**md：`WSFD-104001/激活IPv6承载上下文特性（SGSN_GGSN）_48043366.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开IPv6承载上下文特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0248043366)
  L41:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;
    > ```
  L42:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;
    > ```

**md：`WSFD-104001/调测IPv6承载上下文特性（SGSN_GGSN）_48043374.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询IPv6承载上下文对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，流程结束。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。

### WSFD-104002

**md：`WSFD-104002/激活IPv4v6双栈接入特性（适用于PGW-C）_48043380.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2IPDSSM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开IPv6承载上下文特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0248043380)
  L45:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPDSSM01", SWITCH=ENABLE;
    > ```

**md：`WSFD-104002/激活IPv4v6双栈接入特性（适用于SGSN_MME）_48043379.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DUSA02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L52:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开IPv4v6双栈接入特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 开启IPv4v6双栈接入功能。
    >   [**SET SMFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md)
  L75:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DUSA02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104002/调测IPv4v6双栈接入特性（适用于SGSN_MME）_48043346.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询本特性对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤3](#ZH-CN_OPI_0248043346__cmd9774172517215)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 测试终端接入网络，指示用户IP地址类型为IPv4v6。
    > 4. 执行 [**DSP SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/系统管理/用户数据库管理/显示承载上下文(DSP SMCTX)_72226033.md) 命令，通过IMSI查看测试终端承载信息。

**md：`WSFD-104002/调测支持静态IPv4v6双栈地址功能（适用于PGW-C）_48043387.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询本特性对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0248043387__step1677352512218)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 测试终端接入网络，指示用户IP地址类型为IPv4v6。
    > 4. 执行 [**DSP SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/系统管理/用户数据库管理/显示承载上下文(DSP SMCTX)_72226033.md) 命令，通过IMSI查看测试终端承载信息。

**md：`WSFD-104002/WSFD-104002 IPv4v6双栈接入（5G）参考信息_48043365.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**DSP PDUSESSION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)
    > 

**md：`WSFD-104002/激活IPv4v6双栈接入特性_48043372.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2IPDSAM01",SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2IPDSSM01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开IPv4v6双栈接入特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0248043372)
  L46:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPDSAM01",SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IPDSSM01",SWITCH=ENABLE;
    > ```
  L47:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IPDSAM01",SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IPDSSM01",SWITCH=ENABLE;
    > ```

**md：`WSFD-104002/调测IPv4v6双栈接入特性_48043390.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > 
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令，查询本特性对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0248043390__step1677352512218)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
  L37:
    > 2. 执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令，查询本特性对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0248043390__step1677352512218)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 测试终端接入网络，指示用户IP地址类型为IPv4v6。
    > 4. 执行 [**DSP PDUSESSION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过IMSI查看测试终端承载信息。

### WSFD-108002

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2PCLBO01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2PCLBO01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2PCLBO01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L97:
    >   [**SET SMFFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)
    > 5. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0228860590)
  L142:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PCLBO01", SWITCH=ENABLE;
    > ```
    > 
  L164:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PCLBO01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-108004

**md：`WSFD-108004/配置“ULCL UPF+辅锚点UPF双主负荷分担模式”_10379148.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DMECFP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L180:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DMECFP01", SWITCH=ENABLE;
    > ```

**md：`WSFD-108004/配置“主锚点UPF双主负荷分担部署模式”_28860593.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DMECFP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L52:
    >       **[SET DEACTIVERATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活PDP速率/设置去激活用户承载的速率（SET DEACTIVERATE）_09652156.md)**
    > 3. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0228860593)
  L85:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DMECFP01", SWITCH=ENABLE;
    > ```

**md：`WSFD-108004/配置“园区内UPF和园区外UPF冗余模式”_10539042.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DMECFP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L207:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DMECFP01", SWITCH=ENABLE;
    > ```

### WSFD-108005

**md：`WSFD-108005/激活MEC单点模式故障保护_30792896.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SMECFP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L44:
    >   **[SET UPFAULTOPERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/本地分流管理/辅锚点故障迁移/设置UP故障处理系统参数（SET UPFAULTOPERPARA）_30518084.md)**
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0230792896)
  L69:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SMECFP01", SWITCH=ENABLE;
    > ```

### WSFD-011601

**md：`WSFD-011601/激活NB-IoT终端标准接入（适用于MME）_76669503.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NBPS01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2NBFQ01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2NBFQ02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置S6a接口兼容性策略。
    >   [**SET DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)
  L50:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NBPS01", SWITCH=ENABLE;
    > ```
    > 
  L56:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NBFQ01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-011601/激活NB-IoT终端标准接入（适用于S_PGW-C）_57752888.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV3WPNBPS11 | 本端规划 | 用于配置License控制项开关。 |
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 用于配置License控制项开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3WPNBPS11", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3WNBSL111", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001257752888)
  L46:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3WPNBPS11", SWITCH=ENABLE;
    > ```
    > 
  L52:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3WNBSL111", SWITCH=ENABLE;
    > ```

### WSFD-215001

**md：`WSFD-215001/激活终端省电PSM模式_76015635.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2M2MS01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2M2MS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    >   > 对于处于PSM态的终端，当有下行短消息时，MME会通知上游网元终端不可达。当终端进入连接态后，HSS给短消息中心发送Alert Service Request消息触发短消息重发流程，此时由于短消息中心向EPC核心网下发的短消息存在延时，可能出现短消息下发至终端时，终端又再一次进入PSM态，导致短消息一直发送失败。因此若存在下行短消息的场景，参数 “ACTIVETIMER” 时长的设置需要和短消息中心协商。
    > 3. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276015635)
  L85:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2M2MS01", SWITCH=ENABLE;
    > ```
    > 
  L111:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2M2MS01", SWITCH=ENABLE;
    > ```

### WSFD-215101

**md：`WSFD-215101/激活基于信令面的数据传输（MME）_76015637.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DNAS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L58:
    >   系统支持通过命令 [**SET CHRCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/CHR管理/CHR配置/设置CHR配置（SET CHRCFG）_72225295.md) 和 [**SET CHRLOWPERFSVRSUB**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/低性能CHR服务器的单据订阅条件/设置低性能CHR服务器的单据订阅条件（SET CHRLOWPERFSVRSUB）_72345083.md) 配置在Control Plane Service Request流程成功或失败时是否上报CHR单据，配置过程参见 [激活CHR功能](../../../操作维护功能/WSFD-202001 CHR功能/WSFD-202001 CHR功能（适用于SGSN_MME_AMF）/激活CHR功能_50287962.md) 。
    > 5. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276015637)
  L83:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DNAS01", SWITCH=ENABLE;
    > ```

**md：`WSFD-215101/激活基于信令面的数据传输（SGW-C）_77260996.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WPSDTO11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L34:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置话单中是否携带CP CIoT EPS Optimisation Indicator、UNI PDU CP Only Flag字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
  L49:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WPSDTO11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215101/调测基于信令面的数据传输（SGW-C）_77260997.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    >   [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3WPSDTO01";
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0277260997__cmd1831301046184705)。
    >     - 如果“SWITCH”为“DISABLE”，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 在OM Portal上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择GTPC、UP DATA和DOWN DATA消息类型。
    > 4. 激活用户，并跟踪该用户消息。

### WSFD-215102

**md：`WSFD-215102/激活NB-IoT用户面传输通道保活_76015638.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2UPTH01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L54:
    >       [**MOD TAICIOT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/CIoT能力配置/修改CIoT能力配置(MOD TAICIOT)_26145782.md)
    > 4. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276015638)
  L79:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2UPTH01", SWITCH=ENABLE;
    > ```

### WSFD-215103

**md：`WSFD-215103/激活Non-IP数据传输_76015639.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NOIP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L57:
    >   [**ADD MMECHARACT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md)
    > 6. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276015639)
  L94:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NOIP01", SWITCH=ENABLE;
    > ```

**md：`WSFD-215103/激活Non-IP数据传输（S_PGW-C）_77449667.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WNBNIP11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L44:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 使能全局的Non-IP功能开关。
    >   [**SET NONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/全局Non-IP配置/设置Non-IP功能配置（SET NONIPFUNC）_28567659.md)
  L72:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WNBNIP11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215103/调测Non-IP数据传输（S_PGW-C）_77449668.md`**
- 操作步骤上下文（±2 行原文）：
  L41:
    >   [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3WNBNIP11";
    >     - 如果“ 开关”为“使能”，请执行[3](#ZH-CN_OPI_0277449668__cmd1236500464184705)。
    >     - 如果“ 开关”为“不使能”，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 执行 [**LST NONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/全局Non-IP配置/查询Non-IP功能配置（LST NONIPFUNC）_28567650.md) 命令，检查全局Non-IP功能是否开启。
    >     - 如果 “Non-IP功能开关” 为 “使能” ， [4](#ZH-CN_OPI_0277449668__cmd1583218602184705) 。

### WSFD-215104

**md：`WSFD-215104/激活NB-IoT基于SGs接口的短消息_76015640.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2GSDT01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L45:
    >       [**MOD M2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/修改M2M策略参数(MOD M2MPLCY)_72345365.md)
    > 3. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276015640)
  L64:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2GSDT01", SWITCH=ENABLE;
    > ```

### WSFD-215201

**md：`WSFD-215201/激活基于延迟定时器的信令拥塞控制（MME）_75415670.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LTCC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本功能的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 设置低优先级APN流控。
    >     a. 增加APNNI组。
  L79:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LTCC01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215201/调测基于延迟定时器的信令拥塞控制（MME）_75514399.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 查询 基于延时定时器的信令拥塞控制 对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0275514399__cmd7195778175821)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 2. 执行 **[LST LOWPRIAPNFC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/操作维护/设备管理/流控管理/业务流控管理/低优先级APN流控管理/查询低优先级APN流控参数（LST LOWPRIAPNFC）_26146158.md)** 命令查看低优先级APN流控功能开关是否打开。
    >     - 如果参数配置为ON，请执行[3](#ZH-CN_OPI_0275514399__step17368152112206)。

**md：`WSFD-215201/激活基于延迟定时器的信令拥塞控制（PGW-C）_75071709.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 设置全局Back-Off时长。
    >   **[SET GBACKOFFTIME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/流控管理/全局Back-off Time信息/设置全局Back-off Time信息（SET GBACKOFFTIME）_76686936.md)**
  L53:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="
    > LKV3WPSSBT11
    > ",SWITCH=ENABLE;

**md：`WSFD-215201/调测基于延迟定时器的信令拥塞控制（PGW-C）_75791001.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 查询 基于延时定时器的信令拥塞控制 对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0275791001__step877713597511)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 2. 构造PGW-C系统过载。
    > 3. 调测终端开机，并进行业务访问试图建立PDN连接。观察PGW-C返回的失败响应消息。

### WSFD-215202

**md：`WSFD-215202/激活基于eNodeB覆盖等级的寻呼_76015642.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CELP01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2CELP01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2PRPG02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L40:
    >   [**SET S1CMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md)
    > 4. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276015642)
  L69:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CELP01", SWITCH=ENABLE;
    > ```
    > 
  L101:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CELP01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215202/调测基于eNodeB覆盖等级的寻呼_76928326.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2CELP01 | 本端规划 | 确认license已经打开 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 确认license已经打开 |
- 操作步骤上下文（±2 行原文）：
  L47:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 配置MME使用CP CIoT方式。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) : LICITEM="LKV2CELP01", SWITCH=ENABLE;
    >     3. 在 UNC 上创建用户跟踪，假设终端的IMSI为“123036901000001”。
    >     4. 设置重发寻呼的最大次数 “N3413” 为 “1” 。

### WSFD-215203

**md：`WSFD-215203/激活低优先级接入控制_76015643.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LPAC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L43:
    >   [**SET LOWPRIOFC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/操作维护/设备管理/流控管理/业务流控管理/低优先级接入流控管理/设置低优先级流控参数(SET LOWPRIOFC)_72345759.md)
    > 3. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 4. **可选：**设置信令优先级指示。
    >   [**SET M2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M控制参数/设置M2M控制参数(SET M2MCTRL)_72345369.md)
  L64:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LPAC01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-215501

**md：`WSFD-215501/激活支持Category NB2接入（S_PGW-C）_77673142.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WSNBAC21",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 打开本特性的软参配置开关。
    >   [**SET SMFSOFTPARA**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)
  L45:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WSNBAC21",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215501/调测支持Category NB2接入（S_PGW-C）_77673143.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询license中是否允许使用Category NB2 接入功能。
    >     - 如果 “SWITCH” 为 “ENABLE” ，请执行 [3](#ZH-CN_OPI_0277673143__cmd901522578184706) 。
    >     - 如果 “SWITCH” 为 “DISABLE” ，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 打开接入侧/PDN侧镜像接口上的抓包工具，准备抓取 测试终端 的出入报文。
    > 4. 测试终端 使用“apn-test”APN接入网络，并开始使用NB-IoT业务。

### WSFD-215502

**md：`WSFD-215502/WSFD-215502 支持2 HARQ终端接入参考信息_75820852.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关命令如下：
    > 
    > [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0275820852)

**md：`WSFD-215502/激活支持2 HARQ终端接入_08484252.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2HARQ01 | 本端规划 | 用于配置License控制项开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 用于配置License控制项开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HARQ01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001308484252)
  L46:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HARQ01", SWITCH=ENABLE;
    > ```

### WSFD-990005

**md：`WSFD-990005/激活RedCap eDRX功能（DDN寻呼流程）_00958549.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2RCEDRXSM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L47:
    >   [**SET PFCPCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP接口兼容性/设置PFCP接口兼容性参数（SET PFCPCMPT）_96243192.md)
    > 5. 打开本功能的License配置开关：
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001600958549)
  L73:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2RCEDRXSM01", SWITCH=ENABLE;
    > ```

**md：`WSFD-990005/调测RedCap eDRX功能（DDN寻呼流程）_01173309.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    >   [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV2RCEDRXSM01";
    >     - 如果“ 开关”为“使能”，请执行[步骤 3](#ZH-CN_OPI_0000001601173309__step16421957519)。
    >     - 如果“ 开关”为“不使能”，则执行 [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上创建用户跟踪。
    > 4. 测试终端接入网络，并进行下行数据业务。激活用户，并跟踪该用户消息。

### WSFD-011603

**md：`WSFD-011603/WSFD-011603 NB-IoT UE状态上报功能参考信息_45290656.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**RMV MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/删除MME属性配置信息（RMV MMECHARACT）_72345557.md)
    > - [**LST MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/查询MME属性配置信息（LST MMECHARACT）_72225637.md)
    > - [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - **[LST LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
    > - [**SET M2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M控制参数/设置M2M控制参数(SET M2MCTRL)_72345369.md)

**md：`WSFD-011603/激活NB-IoT UE状态上报功能_44810844.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2USRF01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L71:
    >   [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) : RANGE=对端设备范围, IPTYPE=IP地址类型, IPV4=MME IPv4信令面地址, MASKV4=IPv4掩码, MNTREVTINFO=NB-IoT状态上报订阅信息;
    > 3. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) : LICITEM="LKV2USRF01", SWITCH=ENABLE;
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001444810844)
  L108:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2USRF01", SWITCH=ENABLE;
    > ```

### WSFD-215002

**md：`WSFD-215002/激活NB-IoT eDRX模式（MME）_76015636.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EDRX01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L61:
    >   > “窄带S1模式寻呼时间窗口时长” 设置时，建议NBPTW的值至少为NB-IoT Default Paging DRX值的2倍，这样eNodeB在NBPTW窗口内可以有多次机会寻呼用户。NB-IoT Default Paging DRX值是eNodeB在S1 Setup Request消息中携带给MME的。
    > 5. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276015636)
  L92:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EDRX01", SWITCH=ENABLE;
    > ```

**md：`WSFD-215002/激活NB-IoT eDRX模式（SGW-C）_77194597.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WNBDRX11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置下行数据到达S-GW时，全局的NB-IoT用户下行报文缓存时长。
    >   [**SET SMFGLBDLBUFTIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/GTP会话协议参数管理/下行报文缓存时长/设置全局下行报文缓存时长（SET SMFGLBDLBUFTIME）_96805509.md)
  L54:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WNBDRX11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215002/调测NB-IoT eDRX模式（SGW-C）_77194598.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    >   [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3WNBDRX11";
    >     - 如果“ 开关”为“使能”，请执行[3](#ZH-CN_OPI_0277194598__cmd1126127540184705)。
    >     - 如果“ 开关”为“不使能”，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 在OM Portal上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择GTPC、UP DATA和DOWN DATA消息类型。 [4](#ZH-CN_OPI_0277194598__step3)
    > 4. 测试终端使用“test”APN接入网络，并进行下行数据业务。激活用户，并跟踪该用户消息。

### WSFD-215204

**md：`WSFD-215204/激活基于APN的NB-IoT终端接入速率控制（MME）_76026859.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2AARC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    >   [**SET SMFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md)
    > 3. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276026859)
  L55:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2AARC01", SWITCH=ENABLE;
    > ```

**md：`WSFD-215204/激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WNBARC11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 开启基于APN的APN速率控制功能。
    >   [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md)
  L58:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WNBARC11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215204/调测基于APN的NB-IoT终端接入速率控制（PGW-C）_77673130.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查看回显中是否允许使用APN速率控制功能。
    >     - 如果“ 开关”为“使能”，请执行[3](#ZH-CN_OPI_0277673130__cmd610952254184706)。
    >     - 如果“ 开关”为“不使能”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 执行 [**LST APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/查询APN速率控制配置（LST APNRATECTRL）_64343877.md) 命令查看基于APN的NB-IoT速率控制功能是否开启。
    >   ```

### WSFD-215205

**md：`WSFD-215205/激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WNBPRC11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 开启Serving PLMN速率控制功能。
    >     - 开启基于APN的Serving PLMN速率控制功能。
  L60:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WNBPRC11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215205/调测基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673137.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查看回显中是否允许使用基于服务PLMN的NB-IoT终端接入速率控制功能。
    >     - 如果“ 开关”为“使能”，请执行[3](#ZH-CN_OPI_0277673137__cmd722063597184706)。
    >     - 如果“ 开关”为“不使能”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 执行 [**LST APNPLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/查询APN Serving PLMN速率控制配置（LST APNPLMNRATECTRL）_64343876.md) 命令查看基于APN的Serving PLMN速率控制功能是否开启。
    >   ```

**md：`WSFD-215205/激活基于服务PLMN的NB-IoT终端接入速率控制（MME）_76026860.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SARC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L53:
    >   [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md)
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276026860)
  L79:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SARC01", SWITCH=ENABLE;
    > ```

### WSFD-215301

**md：`WSFD-215301/激活HSS免升级_76026861.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HUNN01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L43:
    >   > 当 “SUPAPNNI” 选为 “SPECIAL_APNNI” 时，需要先通过 [**ADD APNNIGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/APNNI信息管理/APNNI组管理/增加APNNI组(ADD APNNIGROUP)_26305508.md) 和 [**ADD APNNI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/APNNI信息管理/APNNI管理/增加APNNI(ADD APNNI)_26305506.md) 来绑定APNNI组。
    > 4. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276026861)
  L68:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HUNN01", SWITCH=ENABLE;
    > ```

### WSFD-215302

**md：`WSFD-215302/激活PCRF免升级_76026862.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WNPUNN11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置开启PCRF免升级功能。
    >   [**SET NBIOTRATVALUE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）_09896820.md)
  L45:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WNPUNN11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-215302/调测PCRF免升级_76026863.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >   [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3WNPUNN11";
    >     - 如果“ 开关”为“使能”，请执行[步骤 2](#ZH-CN_OPI_0276026863__step2_new)。
    >     - 如果“ 开关”为“不使能”，则执行 [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 2. 执行 [**LST NBIOTRATVALUE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/NB-IoT用户RAT值/查询NB-IoT终端配置的RAT值（LST NBIOTRATVALUE）_09896821.md) 命令，查看 PCRF免升级 功能是否开启。
    >   ```

### WSFD-215401

**md：`WSFD-215401/激活NB-IoT终端异常信令与流量管理_76026864.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2PTST01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2PTST01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L72:
    >   [**ADD M2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md)
    > 3. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276026864)
  L121:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PTST01", SWITCH=ENABLE;
    > ```
    > 
  L143:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PTST01", SWITCH=ENABLE;
    > ```

### WSFD-104601

**md：`WSFD-104601/激活支持基于终端能力选择用户面_93971023.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2UNCUP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L76:
    >       [**ADD DNSN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md)
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0193971023)
  L121:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2UNCUP01", SWITCH=ENABLE;
    > ```

### WSFD-104602

**md：`WSFD-104602/激活NSA用户业务连续性保障_93971028.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2UNCUP02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L84:
    >       [**ADD DNSN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md)
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0193971028)
  L133:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2UNCUP02", SWITCH=ENABLE;
    > ```

### WSFD-010701

**md：`WSFD-010701/激活QoS与流量管理（适用于PGW-C）_86476700.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;`
  `SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L101:
    > 
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
    >   ```
    >   //配置整机使能用户的上下行Remark功能。
  L117:
    > 
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
    >   ```
    >   //配置整机使能用户的上下行Remark功能。

### WSFD-105103

**md：`WSFD-105103/激活基于用户等级的QCI扩展_70933935.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2QCIE02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L42:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. （可选）设置扩展QCI到标准QCI的转换关系。
    >   [**ADD QCICONV**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/扩展QCI转换关系/增加扩展QCI转换关系(ADD QCICONV)_26306024.md)
  L59:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2QCIE02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-109202

**md：`WSFD-109202/激活会话类QOS保证（适用于GGSN）_28258187.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L69:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置全局的QoS信息。
    >   [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md)
  L118:
    > - 打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
    >   ```
    > - 配置基于全局的GPRS/UMTS QoS信息。

**md：`WSFD-109202/激活会话类QOS保证（适用于SGW-C_PGW-C）_28344569.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;`
  `SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;`
  `SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;`
  `SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;`
  `SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L90:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) [设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置全局的QoS信息。
    >   [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md)
  L141:
    > 
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
    >   ```
    >   ```
  L150:
    > 
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
    >   ```
    >   ```

### WSFD-105001

**md：`WSFD-105001/激活QoS覆盖_93181073.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2QOSOW02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L45:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置QoS覆盖规则数据。
    >   [**ADD QOSTRANS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/签约QoS转换/增加签约QoS转换配置(ADD QOSTRANS)_72345831.md)
  L61:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2QOSOW02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-105002

**md：`WSFD-105002/激活漫游用户QoS限制_93181079.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2RSQR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L40:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置本网本地用户所归属的HLR号码列表，用于进一步判断本网用户是本网本地用户还是本网异地用户。
    >   [**ADD LOCALHLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/LOCALHLR管理/增加本地HLR(ADD LOCALHLR)_72225755.md)
  L66:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2RSQR01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-105004

**md：`WSFD-105004/激活逻辑接口DSCP配置_70933933.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LIDC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L55:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. **可选：**配置输出IP报文的DSCP值。
    >   > **说明**
  L86:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LIDC01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-105101

**md：`WSFD-105101/激活PFC（仅用于Gb 模式）_93928738.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2PFC02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 修改信令实体，打开PFC开关。
    >   [**MOD NSE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/信令实体管理/修改信令实体(MOD NSE)_26305838.md)
  L52:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PFC02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-105102

**md：`WSFD-105102/激活提供会话类QoS等级业务承载_93181084.md`**
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

### WSFD-105104

**md：`WSFD-105104/激活基于IMSI号段的QoS控制（适用于MME）_70933937.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2IMSIQOS02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L67:
    >           - “开关”=“关闭”，执行[步骤 2.b](#ZH-CN_OPI_0170933937__SET_LICCTRL)。
    >     b. 打开本特性的License配置开关。
    >       **[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 添加基于IMSI号段的QoS控制记录。
    >   [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)
  L86:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IMSIQOS02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-105104/激活基于IMSI号段的QoS控制（适用于SGSN）_92954483.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2IMSIQOS02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L75:
    >           - “开关”=“关闭”，执行[2.b](#ZH-CN_OPI_0192954483__SET_LICCTRL)。
    >     b. 打开本特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 增加IMSI前缀所在号段用户的SM属性配置。
    >   [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md)
  L93:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IMSIQOS02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-105104/激活基于IMSI号段的QoS控制（适用于SMF）_84864432.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2QCBISM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L62:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. （可选）针对使用语音业务的用户，如果这些用户不受基于IMSI号段的QoS控制，可将其加入白名单。
    >   **[**ADD QOSCAPWHITEAPNS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/5GC QoS配置/基于IMSI号段的QoS管理/不受SMFQOSCAP配置控制的APN白名单列表/增加不受SMFQOSCAP配置控制的APN白名单列表。（ADD QOSCAPWHITEAPNS）_26639421.md)**
  L81:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2QCBISM01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-105104/激活漫入用户的QoS控制（适用于SMF）_14101265.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2QCBISM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L59:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. （可选）针对使用语音业务的用户，如果这些用户不受基于漫入用户的QoS控制，可将其加入白名单。
    >   **[**ADD QOSCAPWHITEAPNS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/5GC QoS配置/基于IMSI号段的QoS管理/不受SMFQOSCAP配置控制的APN白名单列表/增加不受SMFQOSCAP配置控制的APN白名单列表。（ADD QOSCAPWHITEAPNS）_26639421.md)**
  L80:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2QCBISM01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-105105

**md：`WSFD-105105/激活PCC模式的本地QoS策略控制（适用于MME）_70933939.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NQOS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L75:
    >           - “开关”=“关闭”，执行[步骤 2.b](#ZH-CN_OPI_0170933939__SET_LICCTRL)。
    >     b. 打开本特性的License配置开关。
    >       **[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 检查Non-GBR承载的配置。
    >     a. 查询Non-GBR承载的配置记录。
  L102:
    > ```
    > LST LICENSESWITCH: LICITEM="LKV2NQOS01";
    > SET LICENSESWITCH: LICITEM="LKV2NQOS01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-105105/激活PCC模式的本地QoS策略控制（适用于SGSN）_92954490.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NQOS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L52:
    >           - “开关”=“关闭”，执行[步骤 2.b](#ZH-CN_OPI_0192954490__SET_LICCTRL)。
    >     b. 打开本特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 增加IMSI前缀所在号段用户的SM属性配置。
    >   [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md)
  L71:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NQOS01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-109203

**md：`WSFD-109203/激活本地QOS控制（适用于GGSN）_28258572.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | LICITEM | LKV3W9LQOS12 | 本端规划 | 配置License配置开关 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | SWITCH | ENABLE | 本端规划 | 配置License配置开关 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9LQOS12",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L73:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置GPRS/UMTS缺省QoS参数（用于纠错）。
    >   [**SET DEFPRER8QOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/全局PreR8 QoS纠错/设置缺省的Pre-R8 QoS参数（SET DEFPRER8QOS）_09654401.md)
  L101:
    > - 打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9LQOS12",SWITCH=ENABLE;
    >   ```
    > - 配置基于全局的GPRS/UMTS QoS缺省QoS参数（用于纠错）。

**md：`WSFD-109203/激活本地QOS控制（适用于SGW-C_PGW-C）_28258573.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)<br>[设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | LICITEM | LKV3W9LQOS12 | 本端规划 | 配置License配置开关 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)<br>[设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | SWITCH | ENABLE | 本端规划 | 配置License配置开关 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9LQOS12",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L78:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >   [设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选** ：配置EPC网络中的QoS参数和R99，R98 QoS参数的映射规则。缺省使用默认值
  L79:
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >   [设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选** ：配置EPC网络中的QoS参数和R99，R98 QoS参数的映射规则。缺省使用默认值
    >   [**SET EPSQCI2PRER8**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/EPS QCI映射到PreR8/设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）_09651491.md)
  L110:
    > - 打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9LQOS12",SWITCH=ENABLE;
    >   ```
    > - **可选**：配置EPC网络中的QoS参数和R99，R98 QoS参数的映射规则。缺省使用默认值。

### WSFD-109204

**md：`WSFD-109204/激活QCI扩展_10505693.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2UNCQCI1", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L76:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    >   > **说明**
    >   > SGW-C和PGW-C分离场景，可能存在PGW-C有扩展QCI的license但是SGW-C无扩展QCI的license的情况。此情况下SGW-C收到携带扩展QCI的专有承载创建请求时的处理受软参控制：
  L127:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2UNCQCI1", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-109204/调测QCI扩展_10505694.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 
    >   - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0310505694__step1567118364012)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在OM Portal上创建用户跟踪任务，查看用户跟踪任务结果。
    >     - 预期结果如[图1](#ZH-CN_OPI_0310505694__fig891205813386)、[图2](#ZH-CN_OPI_0310505694__fig777334083912)用户跟踪所示，检查消息跟踪中向UE侧发送的消息中的扩展QCI是否按照数据配置将扩展QCI值64转换为标准QCI值8。如果是正确携带，则调测完成。

### WSFD-104510

**md：`WSFD-104510/调测5G SA到LTE网络间重选_90799284.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >   [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) :LICITEM="LKV2NRBL5";
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0190799284__cmd105004011261)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 验证UE从5G网络向LTE网络重选可实现。
    >     a. 在MME的OM Portal上创建用户跟踪任务。

**md：`WSFD-104510/调测LTE到5G SA网络间重选_90799286.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >   [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) :LICITEM="LKV2NRBL5";
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0190799286__cmd1098161310282)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 验证UE从EPS移动到5GS网络重选可实现。
    >     a. 在AMF的OM Portal上创建用户跟踪任务。

### WSFD-104511

**md：`WSFD-104511/调测5G SA到LTE网络间切换_90799285.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >   [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) :LICITEM="LKV2PHBL5";
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0190799285__cmd105004011261)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 验证UE从5G网络向LTE网络切换可实现。
    >     a. 在AMF的OM Portal上创建用户跟踪任务。

**md：`WSFD-104511/调测LTE到5G SA网络间切换_90799283.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >   [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) :LICITEM="LKV2PHBL5";
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0190799283__cmd1098161310282)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 验证终端从LTE网络向5G网络切换可实现。
    >     a. 在MME、AMF的OM Portal上创建用户跟踪任务。

### WSFD-104501

**md：`WSFD-104501/激活LTE和UMTS网络之间的重选_91285430.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2AUUL02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L78:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置GUTI和PTMSI/RAI的识别模式，需要分别配置掩码模式、区段模式和域名回退模式下的RNC ID。
    >     - [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md)
  L112:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2AUUL02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104502

**md：`WSFD-104502/激活LTE和GSM网络之间的重选_93948992.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2AUGL02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L76:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置GUTI和PTMSI/RAI的识别模式，需要分别配置掩码模式、区段模式和域名回退模式下的RNC ID。
    >     - [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md)
  L110:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2AUGL02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104503

**md：`WSFD-104503/激活LTE和UMTS PS网络之间的切换_91285433.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HOLU02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L75:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. （可选）配置在切换流程中是否使用RNC ID域名进行查询。如果不使用RNC ID域名，系统会组装RAI域名进行查询。
    >   [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md) 命令主要适用于重选流程，仅仅“使用RNC ID域名”参数对切换流程域名组装有影响。
  L109:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HOLU02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104504

**md：`WSFD-104504/激活CDMA与LTE的非优化切换_76144609.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NOHC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**设置PDN GW Identity的类型参数。
    >   根据3GPP 23.402要求：Notify Request只能携带Hostname和IP地址其中一种。由于不能确保所有厂商的网元都按协议要求来填写，如存在PDN GW Identity不一致时，可能会导致后续业务流程失败。因此 UNC 可通过该配置，来选择给HSS上报的是FQDN或者是IP地址。
  L57:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NOHC01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104505

**md：`WSFD-104505/激活LTE和WiFi网络之间的普通切换_76144615.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2WIFI01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置PGW-C Identity的类型参数。
    >   根据3GPP 23402要求：Notify Request只能携带Hostname和IP地址其中一种。由于不能确保所有厂商的网元都按协议要求来填写，如存在PGW-C Identity不一致时，可能会导致后续业务流程失败。因此 UNC 可通过该配置，来选择给HSS上报的是FQDN或者是IP地址。
  L50:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2WIFI01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104505/激活LTE和WiFi网络之间的紧急呼叫切换_76869184.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2WIFI01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L34:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置PGW-C Identity的类型参数。
    >   根据3GPP 23402要求：Notify Request只能携带Hostname和IP地址其中一种。由于不能确保所有厂商的网元都按协议要求来填写，如存在PGW-C Identity不一致时，可能会导致后续业务流程失败。因此 UNC 可通过该配置，来选择给HSS上报的是FQDN或者是IP地址。
  L56:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2WIFI01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104507

**md：`WSFD-104507/激活切换策略控制_75042561.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SRVHD02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L43:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 启用业务切换策略功能。
    >   [**SET COMPATIBILITY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/QoS兼容性配置/设置QoS兼容性配置(SET COMPATIBILITY)_72345835.md)
  L76:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SRVHD02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-106207

**md：`WSFD-106207/激活基于SPID的UE驻留和切换策略管理_68358239.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SPID01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2SPID01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L78:
    >       **场景二：假设不信赖HSS中的用户签约信息（例如对于漫游用户），或在HSS签约未规划或HSS不支持该功能。为了实现自定义的驻留优先级控制， UNC 可以在本地针对用户进行RFSP策略的配置：**
    > 
    >       - [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >           - [**ADD RFSP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/RFSP管理/RFSP策略管理/RFSP参数配置/增加RFSP配置(ADD RFSP)_26305350.md)
    >             > **说明**
  L97:
    >       **场景三：假设运营商需要某号段的用户优先使用签约的RFSP ID对应的频点优先级进行驻留控制，如果没有签约RFSP ID，才按照配置对应的频点优先级进行驻留控制：**
    > 
    >       - [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >           - [**ADD RFSP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/RFSP管理/RFSP策略管理/RFSP参数配置/增加RFSP配置(ADD RFSP)_26305350.md)
    >           - 由于现网BSC可能存在老版本，为了兼容性，2G场景需要打开“是否支持SPID”开关。
  L131:
    >   //开启基于SPID的UE驻留和切换策略管理功能开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2SPID01", SWITCH=ENABLE;
    >   ```
    >   //需要对如下几类用户进行驻留控制的规划：对于30808号段的用户，按照RFSP为1对应的频点优先级进行驻留控制；对于NOID为1对应的漫游用户，按照RFSP为2对应的频点优先级进行驻留控制；对于除30808号段和NOID为1的漫游用户之外的其他用户，按照RFSP为3对应的频点优先级进行驻留控制。

**md：`WSFD-106207/调测基于SPID的UE驻留和切换策略管理_68358240.md`**
- 操作步骤上下文（±2 行原文）：
  L32:
    >     2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >           - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0168358240__cmd51101620141416)。
    >           - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    >     3. 检查是否激活基于SPID的UE驻留和切换策略管理。
    >       [**DSP LICENSE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md) :;

### WSFD-201301

**md：`WSFD-201301/激活E-UTRAN和WLAN互操作_76948724.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WPHOLW11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L53:
    >       [**ADD APNWIFILTEHO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/E-UTRAN和WLAN互操作控制/基于APN的E-UTRAN和WLAN互操作控制/增加基于APN的E-UTRAN和WLAN互操作控制属性（ADD APNWIFILTEHO）_82122523.md)
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > 以下步骤在AMF上执行
  L87:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WPHOLW11",SWITCH=ENABLE;
    > ```
    > 

### WSFD-106004

**md：`WSFD-106004/激活请求信息纠正功能_81812385.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV2DNNC01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开license配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置切片纠正信息。
  L38:
    > 2. 打开license配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置切片纠正信息。
    >   **[ADD LOCALNSDNN](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/网络切片和DNN纠正管理/增加网络切片或DNN纠正配置（ADD LOCALNSDNN）_09652139.md)**
  L65:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV2DNNC01",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106004/激活请求信息纠正功能_81164518.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2RINCOR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**根据IMSI、PDP Type配置Local APNNI。
    >   [**ADD PDPAPN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/本地APNNI管理/增加本地APN NI配置(ADD PDPAPN)_72345275.md)
  L86:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2RINCOR02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-106203

**md：`WSFD-106203/激活别名APN_34797880.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV2AAPN01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L65:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :
    > 3. 配置真实APN。
    >   [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
  L94:
    > 1. 开启别名APN功能License。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV2AAPN01",SWITCH=ENABLE;
    >   ```
    > 2. 配置真实APN并配置APN的上报属性。

**md：`WSFD-106203/调测别名APN_34797881.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > 2. 查询UNC上虚拟APN对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行 [3](#ZH-CN_OPI_0234797881__step2) 。
    >     - 如果“SWITCH”为“DISABLE”，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 测试终端8613812345678分别使用不同的APN“apn1”和“apn2”接入网络。
    >     - 如果测试终端成功接入网络，请执行[4](#ZH-CN_OPI_0234797881__step1748715326214)。

**md：`WSFD-106203/激活别名APN_68358227.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ALIASAPN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 添加别名映射表的记录。
    >   > **说明**
  L54:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ALIASAPN02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106203/调测别名APN_68358228.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358228__cmd51101620141416)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 用户发起初始附着，携带APN为“example.com”、PDN类型与缺省APN的子集。
    >   预期结果：用户附着成功。

### WSFD-106006

**md：`WSFD-106006/激活网络侧二次激活特性_43382681.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NSPDP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L38:
    > 1. 打开本特性的License配置开关。
    >   进入 “MML命令行-UNC” 窗口。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0243382681)
  L51:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NSPDP01", SWITCH=ENABLE;
    > ```

### WSFD-106205

**md：`WSFD-106205/激活主动分离未激活用户_85273669.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2DTUSR02 | 本端规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DTUSR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L52:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置主动分离未激活用户特性参数。
    >     - 设置GSM模式下相关参数。
  L80:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DTUSR02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-106206

**md：`WSFD-106206/激活去激活空闲PDP上下文_84683746.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2DAPDP02 | 全网规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DAPDP02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 为相应计费属性的PDP上下文配置去激活空闲PDP上下文的时长。
    >   [**ADD CHGBEHA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费行为参数配置/增加计费行为参数(ADD CHGBEHA)_26145366.md)
  L56:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DAPDP02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-205102

**md：`WSFD-205102/WSFD-205102 虚拟APN参考信息_29376297.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)

**md：`WSFD-205102/激活虚拟APN_70437186.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9VAPN12",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L67:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :
    > 3. 配置APN，开启虚拟APN功能。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
  L80:
    >   >
    >   > - 当配置虚拟APN映射方式为**PCO**时，还需要通过[**SET DOMAINSEPARATOR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/域名分隔符/设置域名前后缀分隔符（SET DOMAINSEPARATOR）_09654169.md)设置前缀分隔符或后缀分隔符，将从PCO信元中解析出的域名作为真实的APN。
    >   > - 当配置虚拟APN映射方式为**LAC_GROUP**、**TAC_GROUP**、**RAC_GROUP**或者 **SERVING_GROUP**时，需要使用[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)开启基于位置的业务管理特性相关License，并预先配置[**ADD LACGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于LAC位置的虚拟APN映射管理/虚拟APN映射的LAC组/增加LAC组（ADD LACGROUP）_09654412.md)、[**ADD LACID**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于LAC位置的虚拟APN映射管理/LAC组的LAC段/增加LAC组内绑定的LAC号段（ADD LACID）_09651398.md)、[**ADD TACGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于TAC位置的虚拟APN映射管理/虚拟APN映射的TAC组/增加TAC组（ADD TACGROUP）_09651749.md)、[**ADD S1TACID**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于TAC位置的虚拟APN映射管理/TAC组的S1 TAC段/增加TAC组内绑定的S1TAC号段（ADD S1TACID）_09651757.md)、[**ADD N2TACID**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于TAC位置的虚拟APN映射管理/TAC组的N2 TAC段/增加TAC组内绑定的N2TAC号段（ADD N2TACID）_09653669.md)、[**ADD RACGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于RAC位置的虚拟APN映射管理/虚拟APN映射的RAC组/增加RAC组（ADD RACGROUP）_09652702.md)、[**ADD RACID**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于RAC位置的虚拟APN映射管理/RAC组的RAC段/增加RAC组内绑定的RAC号段（ADD RACID）_09652984.md)、[**ADD SRVNODEGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于对接IP地址的虚拟APN映射管理/虚拟APN映射的服务节点组/增加服务节点组（ADD SRVNODEGROUP）_09651376.md)、[**ADD SRVNODEIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/基于对接IP地址的虚拟APN映射管理/服务节点组的服务节点IP段/增加服务节点IP（ADD SRVNODEIP）_09654166.md)，否则命令配置失败。
    >   > - 当配置虚拟APN映射方式为**PLMN**时，获取用户的PLMN来和配置的PLMN进行匹配获取真实APN，可参考[WSFD-011310 PLMN标识获取](../../漫游管理功能/WSFD-011310 PLMN标识获取_75602852.md)。
    >   >     - GGSN用户通过ULI (User Location Identifier)属性或者RAI (Routing Area Identifier)属性、SGSN/MME的IP地址映射出PLMN的方式获取用户的PLMN标识。
  L99:
    > 1. 开启虚拟APN功能License。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9VAPN12",SWITCH=ENABLE;
    >   ```
    > 2. 新增虚拟APN“example.com”，使能Virtual APN功能。

### WSFD-205105

**md：`WSFD-205105/激活上下文回收管理_27434204.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2RCON01",SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2RCON01",SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2RCON01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L61:
    >   **[DEA SMCTX](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md)**
    > 7. 打开上下文回收管理特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0227434204)
  L80:
    >   //打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2RCON01",SWITCH=ENABLE;
    >   ```
    > - 脚本二：
  L89:
    >   //打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2RCON01",SWITCH=ENABLE;
    >   ```
    > - 脚本三：

### WSFD-106001

**md：`WSFD-106001/激活终端侧二次PDP上下文激活特性_43355960.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SPCA01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0243355960)
  L45:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SPCA01", SWITCH=ENABLE;
    > ```

### WSFD-205104

**md：`WSFD-205104/激活支持用户发起的二次激活_39947740.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3W9SACT11", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 打开UE发起二次激活开关。
    >   [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
  L45:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3W9SACT11", SWITCH=ENABLE;
    > ```
    > 

### WSFD-106401

**md：`WSFD-106401/WSFD-106401 位置定位服务（LCS）（适用于MME）参考信息_91808332.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**ADD GMLCAU**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC权限配置/增加GMLC权限配置(ADD GMLCAU)_26145794.md)
    > - [**RMV GMLCAU**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC权限配置/删除GMLC权限配置(RMV GMLCAU)_72225473.md)

**md：`WSFD-106401/激活位置定位服务（LCS）（适用于MME）_91808319.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LCS02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2LCS02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2LCR01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2LCS02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L47:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**在未部署E-SMLC网元的LCS组网场景下，打开依赖特性“WSFD-110520 小区位置信息上报功能（S11接口）”的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
  L49:
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**在未部署E-SMLC网元的LCS组网场景下，打开依赖特性“WSFD-110520 小区位置信息上报功能（S11接口）”的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 4. 增加发起定位请求的GMLC的权限。
    >   [**ADD GMLCAU**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC权限配置/增加GMLC权限配置(ADD GMLCAU)_26145794.md)
  L74:
    >   //打开位置定位服务（LCS）的License配置开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2LCS02", SWITCH=ENABLE;
    >   ```
    >   //增加一条 “GMLC 标识” 为 “1” ， “支持的客户端类型” 为 “VALUE_ADDED_SERVICES（增值业务）” ， “支持的LCS业务类型” 为 “3” 的GMLC配置记录。

**md：`WSFD-106401/调测位置定位服务（LCS）（适用于MME）_91808303.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    >     2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >           - 如果“SWITCH”为“ENABLE”，请执行后续步骤。
    >           - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > - **3GPP协议定义的标准LCS组网场景下的调测步骤**
    >     1. 创建用户跟踪。

**md：`WSFD-106401/WSFD-106401 位置定位服务（LCS）（适用于SGSN）参考信息_68358259.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**SET LCSPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS软件参数表/设置LCS参数表记录(SET LCSPARA)_72225477.md)
    > - [**LST LCSPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS软件参数表/查询LCS参数表记录(LST LCSPARA)_26305608.md)

**md：`WSFD-106401/激活位置定位服务（LCS）（适用于SGSN）_68358257.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LCS02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L64:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 打开LCS开关。
    >     - 打开用户归属PLMN的LCS功能允许开关。
  L113:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LCS02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-223002

**md：`WSFD-223002/激活公私网协同访问（含共享UPF选择）_15100009.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SUPFS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L72:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. SMF本端配置共享UPF。
    >   **[ADD PNFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)**
  L120:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SUPFS01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104404

**md：`WSFD-104404/激活基于权重_优先级的Diameter负荷分担_66313822.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DMLS01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2DMLS01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2DMLS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L45:
    > 
    > 1. 打开本特性的License配置开关。 进入 “MML命令行-UNC” 窗口。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 配置到HSS的Diameter路由基于权重/优先级负荷分担
    >   配置步骤参考 [配置到HSS的数据](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置MME/配置到HSS的数据_29306465.md) ，其中配置Diameter主机路由和Diameter域路由时，采用的选路模式为优先级权重，如下。
  L76:
    >   ```
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2DMLS01", SWITCH=ENABLE;
    >   ```
    >   //配置主机路由索引0和1，选路模式为优先级权重，优先级为0，权重分别是1和2。
  L96:
    >   //打开License配置开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2DMLS01", SWITCH=ENABLE;
    >   ```
    >   //配置同一域路由索引中配置两个peer，选路模式为优先级权重，优先级分别是0和1，权重为1。

**md：`WSFD-104404/调测基于权重_优先级的Diameter负荷分担_66313823.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0166313823__cmd19480755172748)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 检查不同用户附着后，是否按照配置规划接入到不同HSS。
    >     - [**LST DMRT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter路由/查询Diameter域路由配置(LST DMRT)_72225969.md) :;查询Diameter域路由数据。

### WSFD-213002

**md：`WSFD-213002/激活 N7接口PCF Group_13564475.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NFSRA01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L38:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 配置SMF选择PCF的负荷分担参数。
    >   **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
  L63:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NFSRA01",SWITCH=ENABLE;
    > ```
    > 

### WSFD-106003

**md：`WSFD-106003/激活用户接入控制功能特性（适用于SGSN、MME）_64082494.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ARD02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L44:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置用户接入控制功能的控制策略。
    >     - 增加控制用户接入GERAN网络的接入限制参数。
  L74:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ARD02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106003/调测用户接入控制功能特性（适用于SGSN、MME）_68358180.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358180__cmd1820420181437)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 维护台创建用户跟踪任务。
    > 4. 用户A和用户B开机发起附着。

### WSFD-106012

**md：`WSFD-106012/WSFD-106012 支持Null-MSISDN参考信息_68358211.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > [**设置License配置开关(SET LICENSESWITCH)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > #### [告警](#ZH-CN_CONCEPT_0168358211)

**md：`WSFD-106012/激活支持Null-MSISDN（适用SMF_GGSN_SGW-C_PGW-C）_76486798.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9NUMD02",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 
    > 1. 以下命令在 “MML命令行-UNC” 窗口上执行。打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 使能Null-MSISDN功能。
    >   > **说明**
  L52:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3W9NUMD02",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106012/激活支持Null-MSISDN（适用于SGSN_MME）_68358209.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NOISDN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 打开本特性的License配置开关。
    >   进入 “MML命令行-UNC” 窗口。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0168358209)
  L46:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NOISDN02", SWITCH=ENABLE;
    > ```

**md：`WSFD-106012/调测支持Null-MSISDN_68358210.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    >     2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令查询License配置开关是否已打开。
    >           - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358210__p1432111826180642)。
    >           - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    >     3. 创建用户跟踪。
    >       参数选择如下：

### WSFD-106005

**md：`WSFD-106005/激活支持ODB特性_64082507.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ODB02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 开启 SGSN 支持ODB功能开关。
    >   [**SET SDCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/签约数据管理/签约数据信息/设置签约数据配置(SET SDCFG)_72225433.md)
  L55:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ODB02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106005/调测支持ODB特性_68358186.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358186__cmd1843084452313)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 检查SGSN上的功能流程信息。
    >   [**LST SDCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/签约数据管理/签约数据信息/查询签约数据配置（LST SDCFG）_26305564.md) :;

### WSFD-106008

**md：`WSFD-106008/激活一号多卡功能特性_64082510.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MIMSI02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 打开本特性的License配置开关。
    >   进入 “MML命令行-UNC” 窗口。 在 “MML命令行-UNC” 窗口上执行命令
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0164082510)
  L45:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MIMSI02", SWITCH=ENABLE;
    > ```

**md：`WSFD-106008/调测一号多卡功能特性_68358192.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358192__cmd13362183012362)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 用户A的IMSI1、IMSI2同时执行附着流程。
    >   预期结果：执行附着流程成功。

### WSFD-106009

**md：`WSFD-106009/WSFD-106009 多时区业务参考信息_68527100.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - [**查询GGSN属性配置信息(LST GGSNCHARACT)**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/查询GGSN属性配置信息(LST GGSNCHARACT)_26145936.md)
    > - [**删除GGSN属性配置信息(RMV GGSNCHARACT)**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/删除GGSN属性配置信息(RMV GGSNCHARACT)_26305744.md)
    > - [**设置License项开关(SET LICENSESWITCH)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**设置5G移动性管理功能(SET NGMMFUNC)**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)
    > - [**增加区域编码(ADD AREACODE)**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/通用区域编码管理/增加区域编码（ADD AREACODE）_44006351.md)

**md：`WSFD-106009/激活多时区业务特性（适用于SGSN_MME）_64082513.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2TZSV01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L55:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. （可选）配置 UNC 是否可以向UE发送网络信息。
    >   [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)
  L102:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2TZSV01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106009/调测多时区业务特性_68358198.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358198__cmd51101620141416)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建待验证GPRS/UMTS/EPC用户的用户跟踪任务。
    > 4. 用户开机，发起Attach请求。

### WSFD-201302

**md：`WSFD-201302/激活支持WLAN与GSM_UMTS_LTE双流并发_77853913.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WPWLAN11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277853913)
  L45:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WPWLAN11",SWITCH=ENABLE;
    > ```

### WSFD-010303

**md：`WSFD-010303/激活NAS信令加密与完整性保护（适用于4G）_75704844.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2AES02 | 本端规划 | 以使用AES算法为例，打开对应的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 以使用AES算法为例，打开对应的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2AES02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L56:
    >   [**ADD S1ALGPRIORITY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/用户安全管理/S1模式用户安全参数/增加S1模式加密和完整性算法优先级配置信息(ADD S1ALGPRIORITY)_26305462.md)
    > 4. 打开License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0175704844)
  L88:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2AES02", SWITCH=ENABLE;
    > ```

### WSFD-103005

**md：`WSFD-103005/激活基于用户群的灵活鉴权_66313816.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2FLEXAUTH02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2FLEXAUTH02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L54:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置基于用户群的灵活鉴权策略。
    >     - Gb模式下增加指定用户群的灵活鉴权策略。
  L79:
    >   //开启基于用户群的灵活鉴权功能开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2FLEXAUTH02", SWITCH=ENABLE;
    >   ```
    >   //添加HOME PLMN的灵活鉴权参数。
  L93:
    >   //开启基于用户群的灵活鉴权功能开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2FLEXAUTH02", SWITCH=ENABLE;
    >   ```
    >   //Gb模式下，添加特定用户群的灵活鉴权参数。

**md：`WSFD-103005/调测基于用户群的灵活鉴权_66372437.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0166372437__cmd1917762794818)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 用户开机发起附着。
    >   预期结果：用户成功附着到网络后发起了鉴权流程，用户鉴权响应成功，继续完成附着流程。

### WSFD-103000

**md：`WSFD-103000/激活支持GPRS 加密功能：GEA-1_GEA-2_GEA-3（仅用于Gb 模式）_94029921.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2GEA102 | 本端规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2GEA102", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L47:
    >   > - 参数“SECPLC”（安全策略）选择“AUTHANDPROTECTED”。
    > 3. 打开GEA特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0194029921)
  L66:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2GEA102", SWITCH=ENABLE;
    > ```

### WSFD-103004

**md：`WSFD-103004/激活设备标识检查特性（适用于2G&3G）_42179843.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EIR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L44:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :
    > 3. 设置GERAN、UTRAN、E-UTRAN网络获取和检查IMEI的策略。
    >   [**MOD GBIMEICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/设备检查管理/Gb模式IMEI配置/修改Gb模式IMEI配置(MOD GBIMEICFG)_26305444.md)
  L68:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EIR02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-103004/调测设备标识检查特性（适用于2G&3G）_42179844.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0242179844__zh-cn_opi_0172585763_cmd22931240113215)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务。
    > 4. 用户开机发起附着请求。预期结果：附着过程MME向EIR发起设备标识检查流程，设备标识检查请求中携带用户的IMEI信息。EIR返回设备标识检查结果，该用户为白名单用户。用户附着成功。

**md：`WSFD-103004/激活设备标识检查特性（适用于4G）_63510668.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EIR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L44:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :
    > 3. 设置4G网络设备标识获取和检查策略。
    >   [**MOD S1IMEICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/设备检查管理/S1模式IMEI配置/修改S1模式IMEI配置(MOD S1IMEICFG)_26145638.md)
  L59:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EIR02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-103004/调测设备标识检查特性（适用于4G）_72585763.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0172585763__cmd22931240113215)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务。
    > 4. 用户开机发起附着请求。

**md：`WSFD-103004/激活设备标识检查特性（适用于5G）_31253420.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EIR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L47:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :
    > 3. 配置5G网络PEI获取和检查策略。
    >   [**ADD NGPEIPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/业务安全管理/PEI策略管理/增加5G PEI策略（ADD NGPEIPLCY）_09651346.md)
  L62:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EIR02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-103004/调测设备标识检查特性（适用于5G）_31413194.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0000001131413194__cmd22931240113215)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建 [HTTP接口跟踪](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建接口跟踪/HTTP接口跟踪_80502490.md) 。
    > 4. 用户开机发起初始注册请求。

### WSFD-103006

**md：`WSFD-103006/激活1_N设备标识检查（适用于2G&3G&4G）_66313818.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV21NIMEI01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 打开本特性的License配置开关。
    >   进入 “MML命令行-UNC” 窗口。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 配置IMEI检查上限，即指定当IMEI未改变时， UNC 每多少次Attach流程发起一次IMEI检查。
    >   Gb模式下： [**MOD GBIMEICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/设备检查管理/Gb模式IMEI配置/修改Gb模式IMEI配置(MOD GBIMEICFG)_26305444.md)
  L55:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV21NIMEI01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-103006/调测1_N设备标识检查（适用于2G&3G&4G）_66362855.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0166362855__cmd19480755172748)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建待验证用户的用户跟踪任务。
    > 4. 用户开机，发起第一次3G Attach请求。

**md：`WSFD-103006/激活1_N设备标识检查（适用于5G）_77332851.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV21NIMEI01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 打开本特性的License配置开关。
    >   进入 “MML命令行-UNC” 窗口。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 配置PEI检查上限。
    >   [**MOD NGPEIPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/业务安全管理/PEI策略管理/修改5G PEI策略（MOD NGPEIPLCY）_09652460.md)
  L52:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV21NIMEI01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-103006/调测1_N设备标识检查（适用于5G）_77252943.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](../../WSFD-103004 设备标识检查/设备标识检查（5G）/调测设备标识检查特性（适用于5G）_31413194.md#ZH-CN_OPI_0000001131413194__cmd22931240113215)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建 [HTTP接口跟踪](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建接口跟踪/HTTP接口跟踪_80502490.md) 。
    > 4. 用户开机发起初始注册请求。

### WSFD-219000

**md：`WSFD-219000/开启特性License开关_61379373.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | - LKV2MFDFUNC01<br>- LKV2MSFUNC01 | 本端规划 | 开启内生安全的特性License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 开启内生安全的特性License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MFDFUNC01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2MSFUNC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 开启内生安全的特性License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000002561379373)
  L45:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MFDFUNC01", SWITCH=ENABLE;
    > ```
    > 
  L51:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MSFUNC01", SWITCH=ENABLE;
    > ```

### WSFD-104301

**md：`WSFD-104301/激活AMF Pool特性_91611153.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2AMFPL01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2AMFPL01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2AMFPL01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0191611153)
  L48:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2AMFPL01", SWITCH=ENABLE;
    > ```
    > 
  L56:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2AMFPL01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-206101

**md：`WSFD-206101/激活UDM全故障业务保活特性_36886325.md`**
- 数据规划表（该命令的参数行）：
  | **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | License项（LICITEM） | LKV2UDMBPMM01 | 本端规划 | 在AMF侧开启UDM全故障业务保活特性的License开关。 |
  | **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | 开关（SWITCH） | ENABLE | 本端规划 | 在AMF侧开启UDM全故障业务保活特性的License开关。 |
  | **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | License项（LICITEM） | LKV2UDMBPSM01 | 本端规划 | 在SMF侧开启UDM全故障业务保活特性的License开关。 |
  | **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | 开关（SWITCH） | ENABLE | 本端规划 | 在SMF侧开启UDM全故障业务保活特性的License开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2UDMBPMM01",SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UDMBPSM01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L112:
    > - AMF侧配置
    >     1. 打开本特性的License配置开关。
    >       **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    >     2. 开启AMF的UDM全故障Bypass功能。
    >       **[SET AMFUDMBYPASS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF的UDM故障BYPASS功能/设置AMF的UDM故障BYPASS功能（SET AMFUDMBYPASS）_26366865.md)**
  L144:
    > - SMF侧配置
    >     1. 打开本特性的License配置开关。
    >       **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    >     2. 增加UDM Bypass后的用户签约QoS属性。
    >       **[ADD 5GCSUBQOS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/5GC QoS配置/本地5GC QoS/增加5GC签约QoS配置（ADD 5GCSUBQOS）_09652601.md)**
  L185:
    >   //开启AMF的UDM全故障特性license。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2UDMBPMM01",SWITCH=ENABLE;
    >   ```
    >   //开启AMF的UDM故障Bypass功能。

### WSFD-206102

**md：`WSFD-206102/激活HSS全故障业务保活特性_05594153.md`**
- 数据规划表（该命令的参数行）：
  | **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | License项（LICITEM） | LKV2HSSBP01 | 本端规划 | 开启HSS全故障业务保活特性的License开关。 |
  | **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | 开关（SWITCH） | ENABLE | 本端规划 | 开启HSS全故障业务保活特性的License开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HSSBP01",SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2HSSBP01",SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2HSSBP01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L74:
    > 
    > 1. 打开本特性的License配置开关。
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 2. 配置HSS Bypass功能开关和策略。
    >   [**SET HSSBYPASS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/可靠性管理/HSS故障BYPASS功能/设置HSS故障Bypass功能控制参数(SET HSSBYPASS)_62871280.md)
  L111:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HSSBP01",SWITCH=ENABLE;
    > ```
    > 
  L159:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HSSBP01",SWITCH=ENABLE;
    > ```
    > 

### WSFD-104202

**md：`WSFD-104202/激活MSC Pool内的用户迁移（Gs接口）特性_86818610.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MSCMG02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L41:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开本特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     3. **可选：**配置迁移第一阶段时长和迁移第二阶段迁移速度。
    >       [**SET VLROFFLOADINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移配置信息/设置VLR迁移配置信息(SET VLROFFLOADINF)_72345023.md)
  L66:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MSCMG02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104202/调测MSC Pool内的用户迁移（Gs接口）特性_86818611.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0186818611__cmd1660314278334)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 查询MSC/VLR迁移配置信息。
    >   [**LST VLROFFLOADINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移配置信息/查询VLR迁移配置信息(LST VLROFFLOADINF)_26145422.md) ;

### WSFD-104302

**md：`WSFD-104302/激活AMF Pool 用户迁移特性_10427846.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SMAP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L41:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > 配置迁移任务
  L78:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SMAP01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104302/调测AMF Pool 用户迁移特性_10427847.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    >   **LST LICENSESWITCH** :LICITEM="LKV2SMAP01";
    >     - 如果“SWITCH”为“ENABLE”，请执行步骤[步骤2](#ZH-CN_OPI_0210427847__cmd18584181415450)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 如下分别介绍协议标准流程的迁移类型以及针对类型为“IMSI(IMSI)”的单用户的迁移任务的调试方法。
    >     - 验证协议标准流程的迁移类型（迁移类型为：ALL/PART/RATE）工作是否正常。

### WSFD-110011

**md：`WSFD-110011/激活NSSF主备容灾_45188380.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ASNSSR01", SWITCH=DISABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2ASNSSR01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2ASNSSR01", SWITCH=DISABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2ASNSSR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    >   **[DSP DRINFO](../../../../../OM参考/命令/UNC MML命令/平台服务管理/CSDB功能管理/CSDB管理/容灾管理/查询容灾信息(DSP DRINFO)_51012929.md)**
    > 5. 在主、备NSSF上分别进行“关闭”和“打开”本特性的License配置开关，确保容灾功能成功激活。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 6. 复位NSSF。
    >   > **说明**
  L115:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ASNSSR01", SWITCH=DISABLE;
    > ```
    > 
  L121:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ASNSSR01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-110011/调测NSSF主备容灾_45188381.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询本特性对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请参考步骤3。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 执行 **[LST DRINST](../../../../../OM参考/命令/UNC MML命令/平台服务管理/CSDB功能管理/CSDB管理/容灾管理/查询容灾实例(LST DRINST)_51012924.md)** 命令，查询容灾实例信息是否配置成功。
    >   预期结果：以其中一个NSSF为例，查询结果显示本端容灾实例标识对应的容灾实例名称已经配置正确。

### WSFD-110012

**md：`WSFD-110012/激活NSSF双活容灾_50205683.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DLNSSR01", SWITCH=DISABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2DLNSSR01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2DLNSSR01", SWITCH=DISABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2DLNSSR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    >   **[DSP DRINFO](../../../../../OM参考/命令/UNC MML命令/平台服务管理/CSDB功能管理/CSDB管理/容灾管理/查询容灾信息(DSP DRINFO)_51012929.md)**
    > 5. 在双活NSSF上分别进行“关闭”和“打开”本特性的License配置开关，确保容灾功能成功激活。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 
    > 配置AMF
  L111:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DLNSSR01", SWITCH=DISABLE;
    > ```
    > 
  L117:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DLNSSR01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-110012/调测NSSF双活容灾_50205684.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询本特性对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请参考步骤3。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 执行 **[LST DRINST](../../../../../OM参考/命令/UNC MML命令/平台服务管理/CSDB功能管理/CSDB管理/容灾管理/查询容灾实例(LST DRINST)_51012924.md)** 命令，查询容灾实例信息是否配置成功。
    >   预期结果：以其中一个NSSF为例，查询结果显示本端容灾实例标识对应的容灾实例名称已经配置正确。

### WSFD-114001

**md：`WSFD-114001/激活NRF主备容灾特性_56656841.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ASNRR01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2ASNRR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L58:
    >       > 此命令针对每个NRF需要配置两次，分别为本端NRF实例通信地址信息和对端NRF实例通信地址信息，并且需要先配置本端NRF实例通信地址信息。
    > 2. NRF1和NRF2上的 [1](#ZH-CN_OPI_0000001756656841__cmd17947852202716) 都完成后，在NRF1和NRF2上分别打开主备容灾的License开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. **可选：**NRF1和NRF2上的 [2](#ZH-CN_OPI_0000001756656841__cmd2716193316285) 都完成后，在NRF1和NRF2上分别先关闭容灾通道开关，打开主备备份状态忽略开关。
    >   > **说明**
  L133:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ASNRR01", SWITCH=ENABLE;
    > ```
    > 
  L141:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ASNRR01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-114001/调测NRF主备容灾特性_08937148.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 **[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)** 查询NRF主备容灾功能对应的License配置开关是否打开（对应License项为：LKV2ASNRR01）。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0000001708937148__cmd145911132132411)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 3. 执行 **[LST DRCOMM](../../../../../OM参考/命令/UNC MML命令/平台服务管理/CSDB功能管理/CSDB管理/容灾管理/查询容灾实例地址(LST DRCOMM)_51012928.md)** 查询容灾通道地址是否和规划一致。
    >     - 如果是，请执行[4](#ZH-CN_OPI_0000001708937148__step1571118471453)。

**md：`WSFD-114001/异常处理：主备NRF回退到单机NRF_56696641.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM=" LKV2ASNRR01", SWITCH=DISABLE;`
  `SET LICENSESWITCH: LICITEM=" LKV2ASNRR01", SWITCH=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L34:
    >     a. 进入 “MML命令行-UNC” 窗口。
    >     b. 关闭主备NRF容灾特性的License配置开关。
    >       **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    >     c. 删除主备NRF容灾实例通信地址信息。
    >       **[RMV DRCOMM](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/CSDB功能管理/CSDB管理/容灾管理/删除容灾实例地址(RMV DRCOMM)_51012926.md)**
  L60:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM=" LKV2ASNRR01", SWITCH=DISABLE;
    > ```
    > 
  L95:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM=" LKV2ASNRR01", SWITCH=DISABLE;
    > ```
    > 

### WSFD-114002

**md：`WSFD-114002/激活NRF双活容灾特性_48424544.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DLNRR01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2DLNRR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L57:
    >       > 此命令针对每个NRF需要配置两次，分别为本端NRF实例通信地址信息和对端NRF实例通信地址信息，并且需要先配置本端NRF实例通信地址信息。
    > 2. NRF1和NRF2上的 [1](#ZH-CN_OPI_0248424544__cmd17947852202716) 都完成后，在NRF1和NRF2上分别打开双活容灾的License开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. **可选：**NRF1和NRF2上的 [2](#ZH-CN_OPI_0248424544__cmd2716193316285) 都完成后，在NRF1和NRF2上分别先关闭容灾通道开关，打开双活备份状态忽略开关。
    >   > **说明**
  L132:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DLNRR01", SWITCH=ENABLE;
    > ```
    > 
  L140:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DLNRR01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-114002/调测NRF双活容灾特性_48424546.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 **[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)** 查询NRF双活容灾功能对应的License配置开关是否打开（对应License项为：LKV2DLNRR01）。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0248424546__cmd145911132132411)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 3. 执行 **[LST DRCOMM](../../../../../OM参考/命令/UNC MML命令/平台服务管理/CSDB功能管理/CSDB管理/容灾管理/查询容灾实例地址(LST DRCOMM)_51012928.md)** 查询容灾通道地址是否和规划一致。
    >     - 如果是，请执行[4](#ZH-CN_OPI_0248424546__step1571118471453)。

**md：`WSFD-114002/异常处理：双活NRF回退到单机NRF_66718544.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM=" LKV2DLNRR01", SWITCH=DISABLE;`
  `SET LICENSESWITCH: LICITEM=" LKV2DLNRR01", SWITCH=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L34:
    >     a. 进入 “MML命令行-UNC” 窗口。
    >     b. 关闭双活NRF容灾特性的License配置开关。
    >       **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    >     c. 删除双活NRF容灾实例通信地址信息。
    >       **[RMV DRCOMM](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/CSDB功能管理/CSDB管理/容灾管理/删除容灾实例地址(RMV DRCOMM)_51012926.md)**
  L60:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM=" LKV2DLNRR01", SWITCH=DISABLE;
    > ```
    > 
  L95:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM=" LKV2DLNRR01", SWITCH=DISABLE;
    > ```
    > 

### WSFD-213001

**md：`WSFD-213001/激活CU Full Mesh组网（SMF）_05448882.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CUFMN01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L34:
    > 
    > 1. 打开本特性的License配置开关。
    >   **SET LICENSESWITCH**
    > 2. 配置地址分配方式。
    >   ****SET ADDRESSATTR****
  L63:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CUFMN01",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-213001/激活CU Full Mesh组网（UPF）_51809001.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3G5CUFM01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L28:
    > 
    > 1. 打开本特性的License配置开关。
    >   **SET LICENSESWITCH**
    > 2. 配置用户面支持分配F-TEID。
    >   **SET CPTEIDUALLOC**
  L43:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3G5CUFM01",SWITCH=ENABLE;
    > ```
    > 

### WSFD-213004

**md：`WSFD-213004/激活GW-U故障隔离_77561887.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3GWUISL01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3GWUISL01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L55:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 配置SGW-U和S11的绑定关系。
    >   **[ADD UPBINDS11](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UPF选择管理/UPF绑定S11接口/增加SGW-U与SGW-C侧S11接口的绑定关系（ADD UPBINDS11）_09653045.md)**
  L78:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3GWUISL01", SWITCH=ENABLE;
    > ```
    > 
  L93:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3GWUISL01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-106302

**md：`WSFD-106302/激活基于APN的接入速率控制_91285446.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ACIU01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L48:
    >       [**ADD APNCTRLPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/基于APN的信令控制参数/增加基于APN的信令控制参数(ADD APNCTRLPARA)_72345383.md)
    > 3. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >   > **说明**
    >   > 如果同一个APN在多个APN组中分别设置了信令控制门限，则只要一个APN组中的相关信令速率超过门限值便开始该APN下的用户的信令控制。
  L85:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ACIU01", SWITCH=ENABLE;
    > ```

### WSFD-106303

**md：`WSFD-106303/WSFD-106303 基于ARP的差异化服务参考信息（适用于GGSN、SGW-C、PGW-C）_40400505.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > - **[LST LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
    > - **[SET USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置用户ARP优先级配置（SET USERPRIORARP）_27933281.md)**

**md：`WSFD-106303/激活基于ARP的差异化服务（适用于GGSN、SGW-C、PGW-C）_88712956.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2DIFFSEC01 | 本端规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DIFFSEC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L54:
    > 
    > 1. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. **可选：**配置拜访或漫游用户的级别限制功能，以及限制级别。
    >   **[SET USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置用户ARP优先级配置（SET USERPRIORARP）_27933281.md)**
  L83:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DIFFSEC01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106303/WSFD-106303 基于ARP的差异化服务参考信息（适用于SGSN）_85249848.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - **[RMV ARPRANGE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/差异化服务配置/删除ARP策略范围配置(RMV ARPRANGE)_72225351.md)**
    > - **[LST ARPRANGE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/差异化服务配置/查询ARP策略范围配置(LST ARPRANGE)_72345269.md)**
    > - **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > - **[LST LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
    > 

**md：`WSFD-106303/激活基于ARP的差异化服务（适用于SGSN）_84683752.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2DAPDP02 | 全网规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DIFSRV02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > 场景一：根据用户的ARP，基于用户级别为用户配置差异化的网络服务。
  L119:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DIFSRV02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-106304

**md：`WSFD-106304/激活Super-Charger功能_84683755.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SUPCHG02 | 全网规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SUPCHG02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 开启Super-Charger功能开关。
    >   [**SET SDCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/签约数据管理/签约数据信息/设置签约数据配置(SET SDCFG)_72225433.md)
  L54:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SUPCHG02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-106305

**md：`WSFD-106305/激活IM类业务资源管控_84683758.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SUPCHG02 | 全网规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2RRMIM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L49:
    >   > 参数 “SPECSRV” （是否支持特殊业务类型）固定选择 “YES” （是）。
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0184683758)
  L69:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2RRMIM01", SWITCH=ENABLE;
    > ```

### WSFD-106306

**md：`WSFD-106306/激活快速移动用户业务保障_68358251.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SGHM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L102:
    > 
    > 8. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0168358251)
  L183:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SGHM01", SWITCH=ENABLE;
    > ```

**md：`WSFD-106306/调测快速移动用户业务保障_68358252.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    >     2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >           - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358252__cmd51101620141416)。
    >           - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    >     3. 创建用户跟踪。
    >     4. 用户在专用网络的某TA中开机附着，后续移动到专用网络以外的跟踪区，触发TAU流程。

### WSFD-106101

**md：`WSFD-106101/信令面下发跟踪任务（5G）_50118325.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ESTAM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3ESTSM02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2ESTAM03", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L22:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置AMF是否向UDM查询或者订阅TraceData。
    >   [**SET NGMMFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)
  L39:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 关闭SMSF向UDM单独获取和订阅Trace Data的软参开关（软参值设置为0）。
    >   [**SET COMMONSOFTPARAOFBIT**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置公共软件参数比特位（SET COMMONSOFTPARAOFBIT）_26494601.md)
  L64:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ESTAM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3ESTSM02", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2ESTAM03", SWITCH=ENABLE;

**md：`WSFD-106101/管理面_信令面下发跟踪任务（4G）_99103732.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ESTAM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3ESTSM02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 
    > 1. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 打开SGs、Sv接口消息跟踪控制开关。
    >   [**SET E2ETRCCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/跟踪配置管理/端到端用户跟踪管理/设置端到端用户跟踪参数(SET E2ETRCCFG)_26305220.md)
  L51:
    > ```
    > //打开License配置开关。
    > SET LICENSESWITCH: LICITEM="LKV2ESTAM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3ESTSM02", SWITCH=ENABLE;
    > ```
  L52:
    > //打开License配置开关。
    > SET LICENSESWITCH: LICITEM="LKV2ESTAM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3ESTSM02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106101/管理面下发跟踪任务（5G）_97000418.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ESTAM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3ESTSM02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2ESTAM03", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L20:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. （可选）配置跟踪消息上报速率控制（建议使用默认值。如果修改，请联系华为技术支持）。
    >   [**SET FWSOFTPARABITS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软参配置管理/设置软件参数比特位（SET FWSOFTPARABITS）_37580503.md)
  L35:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ESTAM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3ESTSM02", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2ESTAM03", SWITCH=ENABLE;
  L36:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ESTAM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3ESTSM02", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2ESTAM03", SWITCH=ENABLE;
    > ```

### WSFD-202001

**md：`WSFD-202001/调测CHR功能_50287963.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询CHR功能的License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行步骤[3](#ZH-CN_OPI_0250287963__cmd1820420181437)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    >   > **说明**
    >   > CHR License仅控制整系统的正常流程CHR单据。

**md：`WSFD-202001/激活CHR功能_93162716.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CHR04", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L98:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的CHR功能License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >   > **说明**
    >   > CHR License仅控制整系统的正常流程CHR单据。
  L164:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CHR04", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-202001/激活CHR功能_50287962.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CHR03", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2CHR03", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L100:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的CHR功能License配置开关。
    >   **[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    >   > **说明**
    >   > CHR License仅控制整系统的正常流程CHR单据。
  L173:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CHR03", SWITCH=ENABLE;
    > ```
    > 
  L239:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CHR03", SWITCH=ENABLE;
    > ```
    > 

### WSFD-202002

**md：`WSFD-202002/激活支持HTTP头压缩字典_75848137.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HTTPCMPHD01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3HTTPCMPHD02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置HTTP动态头域压缩字典上报功能，以及上报周期。
    >   [**SET HTTPINFORPT**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP CHR上报管理/设置HTTP连接信息上报参数（SET HTTPINFORPT）_29213293.md)
  L48:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HTTPCMPHD01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3HTTPCMPHD02", SWITCH=ENABLE;
    > ```
  L49:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HTTPCMPHD01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3HTTPCMPHD02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-202002/调测支持HTTP头压缩字典_75848138.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行步骤[3](#ZH-CN_OPI_0275848138__substep3797227164518)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. UNC 已与CHR服务器完成对接正常后，在CHR客户端上观察信息上报。
    >   预期结果：在 动态 头压缩 字典 更新时，CHR客户端上可以观察更新的HTTP的索引字段。

### WSFD-109101

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L94:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置IMSI或MSISDN号码段。
    >   [**ADD IMSIMSISDNSEG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
  L165:
    > 1. 打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;
    >   ```
    > 2. 配置MSISDN号段。

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L76:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 关闭全局粒度的动态PCC功能。关闭后，开启的是全局粒度的本地PCC功能。
    >   [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
  L127:
    > 1. 打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;
    >   ```
    > 2. 关闭全局粒度的动态PCC开关。关闭后，开启的是全局粒度的本地PCC功能。

**md：`WSFD-109101/调测PCC业务_31422956.md`**
- 操作步骤上下文（±2 行原文）：
  L50:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0231422956__step1618175015812)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 在OM Portal上建立用户跟踪消息。
    > 3. 激活用户，并跟踪该用户消息。

**md：`WSFD-109101/调测到PCRF的数据_31422954.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0231422954__stp1)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 执行 [**DSP PCRFSTATUS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md) 命令，查看PCRF的状态是否正常。
    >   ```

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2PCCBF01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W9SPCC11", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2PCCBF01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W9SPCC11", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2PCCBF01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W9SPCC11", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L113:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     3. 配置AMF选择PCF的策略信息。已存在正确的选择PCF的策略信息时，请跳过本步骤。
    >       [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
  L138:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     3. 使能SMF上的全局用户的PCC功能。
    >       [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
  L232:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PCCBF01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3W9SPCC11", SWITCH=ENABLE;
    > ```

### WSFD-109102

**md：`WSFD-109102/激活ADC基本功能_92582136.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L46:
    > 
    > 1. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :LICITEM="LKV2BADCF01",SWITCH=ENABLE;
    > 2. PCRF/PCF要下发应用Start和Stop的两个Event Trigger，当PCRF/PCF通过动态规则下发appid时，请执行本步骤。
    >     a. 配置ADC业务使用的appid。
  L74:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-109102/调测ADC基本功能_92582137.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0292582137__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务，消息类型选择N4、Gx和N7。
    >   如下以SMF与PCF之间是N7接口为例进行描述，如实际使用的是Gx接口，触发器为APPLICATION_START和APPLICATION_STOP，交互消息为CCR和CCA。

### WSFD-109103

**md：`WSFD-109103/调测IPv6 SA_78881327.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询IPv6 SA的特性开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0278881327__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务，消息类型选择N4、Gx和N7。
    > 4. 测试终端使用“apn-test”接入网络，观测PGW-C/SMF是否向UPF正确传递预定义规则名称/预定义规则组名称。

### WSFD-109104

**md：`WSFD-109104/激活基于累计流量的策略控制_29056190.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9PCBT12",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置累计流量的上报方式。
    >   [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
  L59:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3W9PCBT12",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-109104/调测基于累计流量的策略控制_29056191.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0229056191__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务，消息类型选择N4、Gx和N7。
    > 4. 测试终端使用“apn-test”接入网络，用户访问业务，并进行在线视频或者FTP电影下载。

### WSFD-109105

**md：`WSFD-109105/激活基于位置的业务管理_79067181.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3WPLBSM11", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L60:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :
    >   > **说明**
    >   > [步骤 3](#ZH-CN_OPI_0279067181__step15536230103518) ～ [步骤 6](#ZH-CN_OPI_0279067181__step1638043213516) 几个步骤之间相互独立，可以单个参数作为位置信息，也可以多个参数的组合作为位置信息。请根据实际规划配置。
  L100:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3WPLBSM11", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-109105/调测基于位置的业务管理_79067182.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0279067182__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务，消息类型选择N4。
    > 4. 测试终端使用“example.com”发起接入网络请求。

### WSFD-109107

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9STQE11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L70:
    > 
    > 1. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 配置QoS URR。
    >   [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
  L115:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3W9STQE11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-109107/调测业务触发的QoS保证_85397059.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0285397059__step578242664311)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 在OM Portal上创建 [用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 任务。
    > 3. 测试终端使用 “apn1” APN接入网络。

### WSFD-109108

**md：`WSFD-109108/调测基于接入点策略控制_79943605.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0279943605__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务，消息类型选择N4、Gx和N7。
    > 4. 测试终端使用APN“huawei.com”发起接入网络请求。

### WSFD-109301

**md：`WSFD-109301/WSFD-109301 网络侧发起专有PDP_承载建立参考信息_27915146.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0227915146)

**md：`WSFD-109301/激活网络侧发起专有PDP_承载建立_27915144.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

**md：`WSFD-109301/调测网络侧发起专有PDP_承载建立_27915145.md`**
- 操作步骤上下文（±2 行原文）：
  L31:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0227915145__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建N4接口跟踪、Gx接口跟踪和S11接口跟踪。
    > 4. 激活“apn-ims”APN下两个用户（UE A和UE B）。UE A呼叫UE B。

### WSFD-211001

**md：`WSFD-211001/WSFD-211001 基于初始接入位置的策略控制参考信息_27915140.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**ADD USRLOCATION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/用户位置/增加用户位置（ADD USRLOCATION）_09897143.md)
    > - [**ADD USRLOCATIONGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/用户位置组/增加用户位置组（ADD USRLOCATIONGRP）_09897148.md)

**md：`WSFD-211001/激活基于初始接入位置的策略控制_27915138.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV2PCIAL01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L53:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置用户位置信息。
    >   [**ADD USRLOCATION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/用户位置/增加用户位置（ADD USRLOCATION）_09897143.md)
  L83:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV2PCIAL01",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-211001/调测基于初始接入位置的策略控制_27915139.md`**
- 操作步骤上下文（±2 行原文）：
  L31:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0227915139__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建N4接口跟踪和Gx接口跟踪。
    >   此处以Gx接口为例，N7接口调测步骤与Gx接口类似。

### WSFD-211005

**md：`WSFD-211005/调测基于业务感知的带宽控制_79619227.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0279619227__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务，消息类型选择N4/Gx/N7。
    > 4. 测试终端使用“huawei.com”发起接入网络请求。

### WSFD-211009

**md：`WSFD-211009/激活基于业务累计流量的策略控制_27915156.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L49:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置Monitoring-Key的解析方式。
    >   [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
  L75:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-211009/调测基于业务累计流量的策略控制_27915157.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0227915157__step080520399015)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建用户跟踪任务，消息类型选择N4、Gx和N7。
    > 4. 测试终端使用“apn-test”接入网络，用户访问P2P业务。

### WSFD-211101

**md：`WSFD-211101/激活基于小区负荷上报的无线资源优化_80495435.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9WOCR11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 
    > 1. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 使能基于APN的小区拥塞上报功能。
    >   [**SET APNREPORTATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)
  L51:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3W9WOCR11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-211101/调测基于小区负荷上报的无线资源优化_34456008.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0000001134456008__step578242664311)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 在OM Portal上创建 [用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 任务。
    > 3. 测试终端使用 “apn1” APN接入网络。

### WSFD-106403

**md：`WSFD-106403/去激活小区位置信息上报功能（S11接口）_49840880.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LCR01", SWITCH=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 关闭本特性的License配置开关。
    >   在“MML命令行-UNC”窗口上执行：
    >   [**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) : LICITEM="LKV2LCR01"，SWITCH=DISABLE；
    > 2. 配置特定的GGSN/P-GW不允许使用该功能。
    >   在“MML命令行-UNC”窗口上执行：
  L50:
    > ```
    > //关闭License配置开关。
    > SET LICENSESWITCH: LICITEM="LKV2LCR01", SWITCH=DISABLE;
    > 
    > //配置特定的GGSN/P-GW不允许使用该功能。

**md：`WSFD-106403/激活小区位置信息上报功能（S11接口）_85120025.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LCR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L48:
    > 1. 打开本特性的License配置开关。
    >   在 “MML命令行-UNC” ：
    >   [**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) : LICITEM="LKV2LCR01"，SWITCH=ENABLE；
    > 2. 配置特定的GGSN/P-GW允许使用该功能。
    >   在“MML命令行-UNC”窗口上执行：
  L87:
    > ```
    > //打开小区位置信息上报功能。
    > SET LICENSESWITCH: LICITEM="LKV2LCR01", SWITCH=ENABLE;
    > 
    > //配置特定的GGSN/P-GW允许使用该功能。

### WSFD-206002

**md：`WSFD-206002/激活LTE UE信令控制_88625070.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LUSC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L70:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置识别终端类型的数据库。
    >     a. 查询S1模式IMEI配置。
  L121:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LUSC01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-206002/调测LTE UE信令控制_88625014.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0188625014__cmd1821627242180641)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 检查IMEI数据库配置信息。
    >   [**LST IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/查询IMEI库记录（LST IMEILIB）_26305544.md)

### WSFD-206003

**md：`WSFD-206003/WSFD-206003 基于APN的信令拥塞控制参考信息_88625082.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**ADD APNCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/基于APN的MM拥塞控制_流控_寻呼优化配置/增加APN控制参数配置(ADD APNCTRL)_26145470.md)
    > - [**MOD APNCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/基于APN的MM拥塞控制_流控_寻呼优化配置/修改APN控制参数配置(MOD APNCTRL)_26305282.md)

**md：`WSFD-206003/激活基于APN的信令拥塞控制_88625063.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ASCC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置APN拥塞控制参数。
    >   [**ADD APNCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/基于APN的MM拥塞控制_流控_寻呼优化配置/增加APN控制参数配置(ADD APNCTRL)_26145470.md)
  L54:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ASCC01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-206003/调测基于APN的信令拥塞控制_88625071.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0188625071__cmd1430237208180641)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > - 检查APN拥塞控制功能配置。
    >   进入 “MML命令行-UNC” 窗口。

### WSFD-206008

**md：`WSFD-206008/激活5G UE信令控制_72052700.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SAUSC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L88:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. **可选：**开启用户异常信令抑制功能。
    >   **[SET NGSMARTPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/异常信令抑制参数/设置5G信令抑制参数（SET NGSMARTPARA）_25121211.md)**
  L119:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SAUSC01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-206008/调测5G UE信令控制_72052701.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0272052701__step7311192619543)。
    >     - 如果“SWITCH”为“DISABLE”，请执行**[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 3. 检查用户异常信令抑制功能是否开启。
    >   **[LST NGSMARTPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/异常信令抑制参数/查询5G信令抑制参数（LST NGSMARTPARA）_25120889.md)**

### WSFD-104102

**md：`WSFD-104102/激活MME过载控制特性_63529674.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2POOLOC02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置过载级别与eNodeB控制策略的关系。
    >   [**SET S1OVERLOAD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口过载控制/设置S1过载控制信息(SET S1OVERLOAD)_72345849.md)
  L65:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2POOLOC02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104102/调测MME过载控制特性_72585764.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0172585764__cmd1443233354713)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上建立S1接口跟踪，用户跟踪。
    > 

### WSFD-206001

**md：`WSFD-206001/激活精准寻呼（LTE）_88625065.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2PRPG02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L70:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 打开eNodeB学习邻接关系和寻呼范围开关。
    >   [**SET S1PAGINGCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼策略管理/设置S1寻呼策略控制表(SET S1PAGINGCTRL)_72345845.md)
  L104:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PRPG02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-206001/调测精准寻呼（LTE）_88625019.md`**
- 操作步骤上下文（±2 行原文）：
  L96:
    >             异常结果处理：参考 [激活LTE精准寻呼](激活精准寻呼（LTE）_88625065.md) 并重新配置。
    >     3. 可选：检查eNodeB邻接关系。
    >       当 [**ADD S1PAGINGRULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼规则管理/增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md) 命令中配置的寻呼动作组合中包含邻接eNodeB，且 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令中 “邻接eNodeB开关” 已开启时，需要检查此项，否则可以跳过。
    >       [**DSP ENBNEIBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/eNodeB邻接关系管理/显示eNodeB邻接关系(DSP ENBNEIBS)_26146258.md)
    >           - 预期结果：能够查询到指定中心eNodeB的邻接eNodeB列表，eNodeB已经学习到邻接关系。

**md：`WSFD-206001/激活精准寻呼（5G）_58600013.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2PRPG02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L100:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置寻呼规则，包括用户类型、业务类型和寻呼范围组合。
    >   [**ADD NGPAGINGRULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/N2接口管理/NGAP接口寻呼管理/NG寻呼规则管理/增加5G寻呼规则（ADD NGPAGINGRULE）_09652969.md)
  L149:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PRPG02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-206001/调测精准寻呼（5G）_58600014.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > 
    >   - 如果“SWITCH”为“ENABLE”，请执行[步骤2](#ZH-CN_OPI_0258600014__step767223614014)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 在OM Portal上创建用户跟踪任务，在“参数配置”栏输入用户IMSI，其他参数：选择默认值。
    > 3. 创建用户所在最近gNodeB以及预计用户会移动到的gNodeB的N2接口跟踪。

### WSFD-206004

**md：`WSFD-206004/激活固定终端寻呼优化特性_85511003.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2POFT01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 1. 打开本特性的License配置开关。
    >   进入 “MML命令行-UNC” 窗口。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 配置需要优化的签约APN及READY定时器时长。
    >   进入 “MML命令行-UNC” 窗口。
  L57:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2POFT01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-206005

**md：`WSFD-206005/激活SmartPhone控制基础功能_85152746.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SPCB02 | 全网规划 | 打开Smartphone控制功能的License开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开Smartphone控制功能的License开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SPCB02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2SPCB02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L65:
    >       > - 参数“SMARTSW”（是否启用SMART用户识别功能）固定选择“YES”。
    >     3. 打开基于信令行为的SmartPhone控制功能的License开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - 激活基于终端类型的Smartphone控制功能。
    >     1. 进入 “MML命令行-UNC” 窗口。
  L80:
    >       > 参数 “DTLIMIT” （DT限制开关）固定选择 “ON” 。
    >     4. 打开基于终端类型的Smartphone控制功能的License开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - 激活SmartPaging功能。
    >     1. 进入 “MML命令行-UNC” 窗口。
  L91:
    >       > - 参数“SMARTPAGING”（GGSN是否支持Smart Paging）选择“YES”（是）。
    >     4. 打开SmartPaging功能的License开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0185152746)

### WSFD-206006

**md：`WSFD-206006/激活Smartphone异常信令节省_85152750.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2DAPDP02 | 全网规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SPAS02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L94:
    >   > “特定原因值拒绝激活唤醒开关” 及 “Parking APN假激活唤醒开关” 默认设置为打开。
    > 7. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0185152750)
  L140:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SPAS02", SWITCH=ENABLE;
    > ```

### WSFD-206007

**md：`WSFD-206007/激活SmartPhone话务模型统计_85152755.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SPCB02 | 全网规划 | 打开Smartphone控制功能的License开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开Smartphone控制功能的License开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SPTM02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L44:
    >   > IMEI库和APN NI库两者可以同时配置，优先级从高到低依次为：签约APN，IMEI，请求APN。
    > 3. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0185152755)
  L66:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SPTM02", SWITCH=ENABLE;
    > ```

### WSFD-206009

**md：`WSFD-206009/激活网元间HTR流控_53482538.md`**
- 数据规划表（该命令的参数行）：
  | **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | License项（LICITEM） | LKV2SHFCUNC01 | 本端规划 | 开启HTR流控License项的配置开关。 |
  | **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | 开关（SWITCH） | ENABLE | 本端规划 | 开启HTR流控License项的配置开关。 |
  | **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | License项（LICITEM） | LKV2SHFCUNC01 | 本端规划 | 开启HTR流控License项的配置开关。 |
  | **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | 开关（SWITCH） | ENABLE | 本端规划 | 开启HTR流控License项的配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SHFCUNC01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2SHFCUNC01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2SHFCUNC01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2SHFCUNC01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2SHFCUNC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L157:
    > 
    > 1. 开启HTR流控License项的配置开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 2. **可选：**设置HTR流控全局配置。
    >   **[SET HTTPHTRCFG](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP流控管理/HTTP HTR流控管理/HTTP HTR全局配置管理/设置HTR流控全局配置（SET HTTPHTRCFG）_35071002.md)**
  L202:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SHFCUNC01", SWITCH=ENABLE;
    > ```
    > 
  L241:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SHFCUNC01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-206010

**md：`WSFD-206010/激活基于分组的智能寻呼_09151282.md`**
- 数据规划表（该命令的参数行）：
  | **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | License项（LICITEM） | LKV2SGPPG01 | 本端规划 | 开启License项配置开关。 |
  | **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)** | 开关（SWITCH） | ENABLE | 本端规划 | 开启License项配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SGPPG01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2SGPPG01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L47:
    > 
    > 1. 开启License项配置开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 2. 配置基于分组的智能寻呼策略。
    >   **[ADD NGPEIPSPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/N2接口管理/NGAP接口寻呼管理/智能寻呼策略/增加基于分组的智能寻呼策略（ADD NGPEIPSPLCY）_35319045.md)**
  L70:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SGPPG01", SWITCH=ENABLE;
    > ```
    > 
  L96:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SGPPG01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104512

**md：`WSFD-104512/调测跨区域移动性管理_51453008.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0251453008__li72721737103914)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上 [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 。
    > 4. 用户开机附着到网络，在area01激活数据业务的PDU会话连接。

### WSFD-105003

**md：`WSFD-105003/激活区域漫游限制特性（适用于AMF）_48669743.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2RRR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L63:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 开启本特性的功能控制开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 开启区域漫游限制功能增强开关，将“AREARSTENSW”设置为“ON”。
    >   **[SET NGMMFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
  L101:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2RRR02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-105003/激活区域漫游限制特性（适用于SGSN_MME）_68262110.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2RRR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L145:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 开启本特性的功能控制开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >   > **说明**
    >   > 根据用户签约ZC信息进行漫游限制不受该License控制。
  L333:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2RRR02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-205012

**md：`WSFD-205012/激活跨域互联互通_50091712.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2ASLSR01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2ASLSR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L34:
    > 1. 进入 “MML命令行-UNC” 窗口。 -AMF
    > 2. 打开本特性AMF的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置I-SMF选择策略。
    >   [**ADD SMFSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/SMF选择策略管理/增加SMF选择策略（ADD SMFSELPLCY）_09653765.md)
  L39:
    > 4. 进入 “MML命令行-UNC” 窗口。 -SMF
    > 5. 打开本特性SMF的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0250091712)
  L52:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2ASLSR01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205012/调测跨域互联互通_50091713.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0250091713__li72721737103914)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上 [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 。
    > 4. 用户开机附着到网络，在同一区域的AMF上进行数据业务的PDU会话建立。

### WSFD-205107

**md：`WSFD-205107/去激活GGSN_P-GW信令代理_83748155.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM=LKV3W9GPSP11,SWITCH=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L58:
    > 
    > 1. 以下命令在“MML命令行 - UNC”窗口上执行。关闭本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :LICITEM=LKV3W9GPSP11,SWITCH=DISABLE;
    > 2. 删除Home group与APN的绑定关系。[**RMV HOMEGRPBINDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/GGSN和P-GW Proxy/Home Group绑定APN/删除Home Group和APN的绑定关系（RMV HOMEGRPBINDAPN）_42853268.md):APN=APN，HOMEGROUPINDX=Home group的编号；
    > 3. 关闭网关的Proxy功能<br>[**SET GWPROXYFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/GGSN和P-GW Proxy/网关Proxy功能/设置网关Proxy功能（SET GWPROXYFUNC）_42853270.md):PROXYSW=网关Proxy开关；
  L106:
    > 1. 关闭本特性的License开关。
    >   ```
    >   SET LICENSESWITCH:LICITEM=LKV3W9GPSP11,SWITCH=DISABLE;
    >   ```
    > 2. 删除Home group与APN的绑定关系。

**md：`WSFD-205107/激活GGSN_P-GW信令代理_38987364.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9GPSP11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L62:
    > 
    > 1. 以下命令在“MML命令行 - UNC”窗口上执行。打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) :LICITEM=LKV3W9GPSP11,SWITCH=ENABLE;
    > 2. 如需开启指定APN的Proxy 功能，配置基于APN控制是否打开网关Proxy功能。[**ADD APNGWPROXYFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/GGSN和P-GW Proxy/APN网关Proxy功能/增加APN网关Proxy功能配置（ADD APNGWPROXYFUNC）_42853254.md):APN=APN，PROXYSW=基于APN控制的网关Proxy开关； 如果未配置本步骤，则会使用全局控制是否打开网关Proxy功能。
    > 3. 如需开启所有APN的Proxy 功能，配置基于全局控制是否打开网关Proxy功能。
  L101:
    > 1. 打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9GPSP11",SWITCH=ENABLE;
    >   ```
    > 2. 如需开启指定APN的Proxy 功能，配置基于APN控制是否打开网关Proxy功能。

### WSFD-104408

**md：`WSFD-104408/激活通过SGs接口实现短消息_66313828.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SMSGU02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L77:
    > 1. 打开本特性的License配置开关。
    >   进入 “MML命令行-UNC” 窗口。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 建立MME和MSC之间的设备间通信。
    >     a. 添加MME和MSC之间偶联路径的SCTP参数模板
  L114:
    > ```
    > //打开License配置开关。
    > SET LICENSESWITCH: LICITEM="LKV2SMSGU02", SWITCH=ENABLE;
    > 
    > //MME上的配置

**md：`WSFD-104408/调测通过SGs接口实现短消息_66313829.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0166313829__cmd19480755172748)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 验证基于SGs接口实现发送短消息。
    >     a. 在MME网元上创建这两个用户的用户消息跟踪和S1-MME、S6a、SGs、GTPC接口消息跟踪任务。

### WSFD-106201

**md：`WSFD-106201/激活小区广播服务_68358221.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CBS02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2PWSR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L31:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**EPC场景需要配置EMM information消息的下发策略。
    >   [**SET MMFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)
  L64:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CBS02", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2PWSR01", SWITCH=ENABLE;
    > ```
  L65:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CBS02", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2PWSR01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-106201/调测小区广播服务_68358222.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358222__cmd51101620141416)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 如果是EPC场景，在 UNC 上创建SBc接口跟踪；如果是5GC场景，在 UNC 上创建N50接口跟踪。
    > 4. 从CBC/CBCF发起小区服务广播服务。

### WSFD-106202

**md：`WSFD-106202/激活SMS over GPRS_EDGE_WCDMA_84683740.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SMS02 | 本端规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SMS02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L77:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 增加短消息PLMN配置信息。
    >     - 增加非漫游用户短信息归属PLMN配置信息。
  L116:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SMS02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104004

**md：`WSFD-104004/激活IPv6前缀代理_76459527.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9V6PD11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L45:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License开关。
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 配置IPv6 VPN。
    >     a. 创建VPN实例。
  L79:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3W9V6PD11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104004/调测IPv6 前缀代理_76459528.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License中是否允许使用支持IPv6 前缀代理。
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0276459528__step10476194711114)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 2. 在 OM Portal上建立用户跟踪，在 “参数配置” 栏输入用户IMSI 。
    > 3. 测试终端 使用“huawei.com”的 “APN” 接入网络。

### WSFD-104401

**md：`WSFD-104401/激活支持多HPLMN功能（适用于AMF）_70150790.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MHAM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License开关。
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 查询MNO信息， UNC 在初配过程中已使用 [**ADD MNO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md) 命令添加了一条缺省MNO记录，通过本步骤可获取该缺省MNO的相关参数信息。
    >   **[**LST NGMNO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/5G 移动网络运营商管理/查询5G模式移动网络运营商信息（LST NGMNO）_09652431.md)**
  L61:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MHAM01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104401/激活支持多HPLMN功能（适用于GGSN_SGW-C_PGW-C_SMF）_70150792.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MHSM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License控制开关。
    >   **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. **可选：**新增HPLMN信息。
    >   **[**ADD NGHPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/Home PLMN信息管理/增加5G Home PLMN（ADD NGHPLMN）_09651693.md)**
  L50:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MHSM01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104401/激活支持多HPLMN功能（适用于SGSN_MME）_70150791.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L86:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开本特性的License开关。
    >       **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    >     3. 增加运营商网络标识。
    >           a. 打开运营商网络名称下发开关，当4G终端接入时，系统允许将运营商网络名称携带给终端。
  L112:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开本特性的License开关。
    >       **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    >     3. 增加运营商网络标识。
    >           a. 打开运营商网络名称下发开关，当终端接入时，系统允许将运营商网络名称携带给终端。
  L171:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104401/调测支持多HPLMN功能_70933791.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0170933791__cmd19480755172748)。
    >     - 如果“SWITCH”为“DISABLE”，请执行
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 检查所配置的HPLMN数据是否正确。
    >   **[LST NGHPLMN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/Home PLMN信息管理/查询5G Home PLMN（LST NGHPLMN）_09653743.md)** （适用于AMF/SGW-C/PGW-C/SMF）

### WSFD-104402

**md：`WSFD-104402/激活 EN-DC SON信息传送功能_64014514.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SON02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L49:
    > 1. 进入 “MML命令行-UNC” 窗口。
    >   打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 执行 **SET S1CMPT** 命令打开EN-DC SON功能开关。
    >   **[SET S1CMPT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md)**
  L64:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SON02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104402/激活eNodeB SON信息传送功能_66313820.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    > 1. 打开本特性的License配置开关。
    >   进入 “MML命令行-UNC” 窗口。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

**md：`WSFD-104402/调测EN-DC SON信息传送功能_14694133.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0000001514694133__cmd12357205912417)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 执行 **[LST S1CMPT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/查询S1接口兼容性(LST S1CMPT)_26146238.md)** 命令查询EN-DC SON开关是否已经打开。
    >     - 如果“ENDCSON”为“SUPPORT”，请执行[4](#ZH-CN_OPI_0000001514694133__cmd18271414345)。

**md：`WSFD-104402/调测eNodeB SON信息传送功能_66313821.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0166313821__cmd19480755172748)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. Intra MME场景：
    >     a. 确认eNodeB2、eNodeB3配置在MME2下（使用[**DSP S1APLNK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1AP链路/显示S1AP连接状态(DSP S1APLNK)_26146252.md)命令确认），并且未配置X2接口；在MME2上打开eNodeB2、eNodeB3的接口跟踪。

### WSFD-205101

**md：`WSFD-205101/激活支持Routing Behind MS_76358998.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9RBMS12",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L40:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 使能该APN的Routing Behind MS功能。
    >   [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.md)
  L62:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3W9RBMS12",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205101/调测支持Routing Behind MS_76358999.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    > 1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License中是否允许使用支持Routing Behind MS。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0276358999__step10476194711114)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 在 OM Portal上建立N4接口跟踪，在 “参数配置” 栏输入用户IMSI 。
    > 3. 测试终端 使用“huawei.com”的 “APN” 接入网络。

### WSFD-104405

**md：`WSFD-104405/激活基于SGs和Sv接口的默认MSC选择_66313824.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DMSC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L56:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置基于Sv接口选择默认MSC。
    >     a. 配置默认MSC地址。
  L85:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DMSC01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104405/调测基于SGs和Sv接口的默认MSC选择_66313825.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0166313825__cmd19480755172748)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上创建用户跟踪。
    > 4. 用户附着，接入E-UTRAN网络。

### WSFD-104406

**md：`WSFD-104406/激活NACC_66313826.md`**
- 操作步骤上下文（±2 行原文）：
  L31:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 在GERAN网络下需打开RIM功能。
    >   如果NSE为静态配置，通过 [**MOD NSE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/信令实体管理/修改信令实体(MOD NSE)_26305838.md) 修改 “是否支持RIM” 参数打开RIM功能。

**md：`WSFD-104406/调测NACC_66313827.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0166313827__cmd19480755172748)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：
    >   > **说明**

### WSFD-104409

**md：`WSFD-104409/激活多信令点功能特性_85510498.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MUSP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L43:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MUSP01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-104506

**md：`WSFD-104506/激活支持Direct Tunnel功能_26375780.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DIRTUN02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W9DIRT11", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L125:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开Direct Tunnel特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置SGSN。
    >   SGSN的Direct Tunnel配置，除个别参数外，与Indirect Tunnel配置无异。相关配置请参考 “ UNC 产品文档 > 安装与调测 > 初始配置与调测 ” 。
  L184:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DIRTUN02", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3W9DIRT11", SWITCH=ENABLE;
    > ```
  L185:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DIRTUN02", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV3W9DIRT11", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104506/调测支持Direct Tunnel功能_26375781.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0226375781__step586775134816)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 执行ping命令，分别ping对应的RNC、GGSN的IP地址，查看是否可以ping通。
    >     - 如果是，请执行[4](#ZH-CN_OPI_0226375781__step11538312515)。

### WSFD-104508

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WPSCTP11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L80:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 创建VPN实例。
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
  L145:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WPSCTP11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WPSCTP11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L77:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 创建VPN实例。
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
  L138:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WPSCTP11",SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-104508/调测Gx over SCTP功能_30442392.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    >   **[LST LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0230442392__stp1)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 2. 执行 **[DSP PCRFSTATUS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md)** 命令，查看PCRF的状态是否正常。
    >   ```

**md：`WSFD-104508/调测Gy over SCTP功能_30602208.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    >   **[LST LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0230602208__stp1)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 2. 执行 **[DSP OCSSTATUS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS状态/查询OCS状态（DSP OCSSTATUS）_09896968.md)** 命令，查看OCS的状态是否正常。
    >   ```

### WSFD-104509

**md：`WSFD-104509/激活SGSN的黑白名单_76495251.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9SBWL11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 使能黑白名单控制开关并配置SGSN/MME/SGW-C接入控制名单类型。
    >   **[SET ACCESSLISTFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/黑白名单控制/设置接入控制名单功能（SET ACCESSLISTFUNC）_72373079.md)**
  L53:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3W9SBWL11",SWITCH=ENABLE;
    > ```
    > 

### WSFD-205001

**md：`WSFD-205001/激活网关路由选择功能特性_63535124.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2GGSNR02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L80:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置选择GGSN/P-GW策略功能。
    >   > **说明**
  L145:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2GGSNR02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205001/调测网关路由选择功能特性_72585766.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    > > - 用户在HLR/HSS中有签约数据。
    > > - 以下各场景的配置已成功。
    > > - 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令，确保本特性开关已开启，即“SWITCH”为“ENABLE”；如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 
    > - 场景一：验证对特定用户指定网关IP地址，不需要进行DNS解析的场景。

### WSFD-205003

**md：`WSFD-205003/激活基于位置区域选择网关特性_63535130.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LOCGSN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L104:
    >       [**ADD AREADNS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/位置域名管理/增加位置区域DNS域名(ADD AREADNS)_72345559.md)
    > 5. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0163535130)
  L196:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LOCGSN02", SWITCH=ENABLE;
    > ```

**md：`WSFD-205003/调测基于位置区域选择网关特性_72585767.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0172585767__substep158479363479)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上 [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 。
    > 4. 验证本特性工作是否正常。

### WSFD-205004

**md：`WSFD-205004/激活S-GW_P-GW拓扑选择特性_63535133.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SELGW03", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L66:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 打开S-GW/P-GW拓扑选择开关。
    >   [**SET SMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md)
  L101:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SELGW03", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205004/调测S-GW_P-GW拓扑选择特性_72585768.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0172585768__substep177171010141415)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 执行 [**LST SMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/查询会话管理扩展功能(LST SMFUNC)_72225363.md) 。
    >   预期结果： “Top Select Configure” 为 “YES” 。

### WSFD-205005

**md：`WSFD-205005/激活基于UE接入能力选择网关特性_63535136.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2GSUE02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L66:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 增加基于UE接入能力选择网关的策略。
    >   [**ADD GWSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN_P-GW选择/增加GGSN_P-GW选择策略（ADD GWSELPLCY）_26145944.md)
  L96:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2GSUE02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205005/调测基于UE接入能力选择网关特性_72585769.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0172585769__substep8404172342811)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 查询APN定制功能配置表记录。
    >   进入 “MML命令行-UNC” 窗口。 在 “MML命令行-UNC” 窗口上执行命令

### WSFD-205006

**md：`WSFD-205006/激活基于P-GW锚点选择S-GW特性_63535139.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SELGW04", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L61:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：** 在Inter USN 2/3G切换4G场景下，增加Hostfile文件的A解析记录。
    >   [**ADD IPV4DNSH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)
  L87:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SELGW04", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205006/调测基于P-GW锚点选择S-GW特性_72585770.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0172585770__substep14521219441)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 执行下述命令查询基于P-GW锚点选择S-GW配置表记录信息：
    >   进入 “MML命令行-UNC” 窗口。 在 “MML命令行-UNC” 窗口上执行命令

### WSFD-205007

**md：`WSFD-205007/激活本地P-GW的PDN重建特性_63535142.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2PRLP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L45:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置不同类型业务（APN）的本地P-GW重选策略。
    >     a. 针对IMS语音业务，配置根据承载状态进行本地P-GW的重选。即采用当UE没有QCI为1（语音）或2（视频）的EPS承载时，系统发起P-GW重选过程。
  L70:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PRLP01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205007/调测本地P-GW的PDN重建特性_72585771.md`**
- 操作步骤上下文（±2 行原文）：
  L48:
    > 2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0172585771__li420305912250)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上 [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 。
    > 4. 用户开机附着到网络，在同一区域的S-GW/P-GW上激活PS数据业务的PDN连接。

### WSFD-205009

**md：`WSFD-205009/激活基于HeNB GW的HeNB接入_66313832.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SHNA01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L38:
    >   [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0166313832)
  L57:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SHNA01", SWITCH=ENABLE;
    > ```

**md：`WSFD-205009/调测基于HeNB GW的HeNB接入_66313833.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0166313833__step811720172748)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 创建指定IMSI UE的用户跟踪。
    > 4. UE开机附着到eNodeB的小区，且除缺省承载外，未建立其他专用承载。

### WSFD-205002

**md：`WSFD-205002/激活基于计费属性选择网关_91473807.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2CCGSN02 | 本端规划 | 打开License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CCGSN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L60:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 增加基于计费属性选择网关的策略。
    >   [**ADD GWSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN_P-GW选择/增加GGSN_P-GW选择策略（ADD GWSELPLCY）_26145944.md)
  L84:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CCGSN02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205002/调测基于计费属性选择网关_92137771.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0192137771__zh-cn_opi_0130428893_li1799635241180641)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 查询APN定制功能配置表记录。
    >   [**LST GWSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN_P-GW选择/查询GGSN_P-GW选择策略（LST GWSELPLCY）_72345545.md) :;

### WSFD-205008

**md：`WSFD-205008/激活Category 6网关选择_66313830.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2C6GS01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2CCGSN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L96:
    >   [**ADD IPV4DNSH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)
    > 9. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0166313830)
  L172:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2C6GS01", SWITCH=ENABLE;
    > ```
    > 
  L178:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CCGSN02", SWITCH=ENABLE;
    > ```

**md：`WSFD-205008/调测Category 6网关选择_66313831.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0166313831__step811720172748)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上 [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 。
    > 4. 用户发起附着，观察配置的IMEI获取和DNS选择网关过程。

### WSFD-205010

**md：`WSFD-205010/激活基于服务区域的SMF选择特性_48998097.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SDSC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置相同策略的SMF选择的DNN。
    >   **[ADD DNNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/DNN群组标识管理/增加DNN群组（ADD DNNGRP）_64343822.md)**
  L77:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SDSC01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205010/调测基于服务区域的SMF选择特性_48998098.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > 2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0248998098__li72721737103914)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上创建 [HTTP接口跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建接口跟踪/HTTP接口跟踪_80502490.md) 。
    > 4. DNN为Huawei1的企业业务本网用户在A省接入并正常进行业务。

### WSFD-205011

**md：`WSFD-205011/激活本地PDU会话重建特性_48998103.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2AMFLS01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2SMFLS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L61:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置PDU会话重选策略。
    >   > **说明**
  L99:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2AMFLS01", SWITCH=ENABLE;
    > ```
    > 
  L119:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SMFLS01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-205011/调测本地PDU会话重建特性_48998104.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0248998104__li72721737103914)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上 [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 。
    > 4. 用户开机附着到网络，在同一区域的SMF上激活数据业务的PDU会话连接，执行**[DSP USRSESSIONCTX](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/用户数据库管理/显示指定用户的会话信息（DSP USRSESSIONCTX）_09653734.md)**命令查询SMF信息。
  L47:
    > 2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0248998104__li149951237122918)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 上 [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) 。
    > 4. 用户开机附着到网络，在同一区域的SMF上激活数据业务的PDU会话连接（只存在缺省QoSFlow）。

### WSFD-207003

**md：`WSFD-207003/激活基于LTE的网络共享（MOCN）_03670021.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MOCN03", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L34:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开基于LTE的网络共享（MOCN）功能开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0203670021)
  L47:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MOCN03", SWITCH=ENABLE;
    > ```

### WSFD-207004

**md：`WSFD-207004/激活基于LTE的网络共享（GWCN）_68260818.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2GWCN03", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开基于LTE的网络共享（GWCN）功能开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置“支持多HPLMN”，请参见 [激活支持多HPLMN功能（适用于SGSN/MME）](../../组网功能/WSFD-104401 支持多HPLMN功能/激活支持多HPLMN功能（适用于SGSN_MME）_70150791.md) 。
    >   > **说明**
  L67:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2GWCN03", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-207004/调测基于LTE的网络共享（GWCN）_68358162.md`**
- 操作步骤上下文（±2 行原文）：
  L29:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0168358162__substep5463194653617)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。创建用户跟踪。
    > 3. 指定的MNO用户开机发起IMSI附着。构造eNodeB正确选择服务运营商的PLMN，发送给MME的Initial UE消息TAI中PLMN携带的Select PLMN正确。
    >     - 预期结果：用户跟踪中观察用户成功附着到网络。MME向用户发送Attach Accept消息，分配给用户的GUTI正确指示了服务的运营商的PLMN。然后执行[步骤4](#ZH-CN_OPI_0168358162__cmd315161113158)。

### WSFD-207006

**md：`WSFD-207006/激活基于LTE的MVNO_68260841.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MVNO03", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2MVNO03", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L73:
    > - 未部署 **MVNO** 的情况下，部署 **基于LTE的MVNO**
    >     1. 打开 [WSFD-207006 基于LTE的MVNO](../WSFD-207006 基于LTE的MVNO_68260820.md) 特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     2. 增加运营商网络标识。
    >           a. 打开运营商网络名称下发开关，当4G终端接入时，系统允许将运营商网络名称携带给终端。
  L110:
    > - 已经部署 **MVNO** 的情况下，部署 **基于LTE的MVNO**
    >     1. 打开 [WSFD-207006 基于LTE的MVNO](../WSFD-207006 基于LTE的MVNO_68260820.md) 特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     2. 增加运营商网络标识。
    >           a. 打开运营商网络名称下发开关，当4G终端接入时，系统允许将运营商网络名称携带给终端。
  L172:
    >   //打开License配置开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2MVNO03", SWITCH=ENABLE;
    >   ```
    >   //打开运营商网络名称下发开关，当4G终端接入时，系统允许将运营商网络名称携带给终端。

**md：`WSFD-207006/调测基于LTE的MVNO_68358168.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > 2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358168__cmd179781338194911)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 在 UNC 维护台创建UE的用户跟踪。
    > 4. UE开机并发起附着。

### WSFD-207007

**md：`WSFD-207007/WSFD-207007 基于5G的网络共享（MOCN）参考信息_31553468.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0231553468)

**md：`WSFD-207007/激活基于5G的网络共享（MOCN）_29397151.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MOCN04", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L31:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开基于5G的网络共享（MOCN）功能开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0229397151)
  L44:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MOCN04", SWITCH=ENABLE;
    > ```

### WSFD-106204

**md：`WSFD-106204/激活基于无线区域的网络地址选择_68358233.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2RRR02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2NSBR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置应用本特性的无线区域。
    >   [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)
  L64:
    >   //打开License配置开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;
    >   ```
    >   //增加MNO信息。
  L84:
    >   //开启区域漫游限制功能开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2RRR02", SWITCH=ENABLE;
    >   ```
    >   //位置区域划分。

**md：`WSFD-106204/调测基于无线区域的网络地址选择_68358234.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    >     2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    >           - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358234__cmd51101620141416)。
    >           - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    >     3. 创建用户跟踪。
    >     4. MNO-A的用户在MNO-B的无线网络RAN-B开机附着。

### WSFD-207001

**md：`WSFD-207001/激活网络共享（MOCN）_85152759.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2MOCN02 | 全网规划 | 打开License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MOCN02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L59:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 设置License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 修改NSE信息。
    >     - 当NSE是静态配置或动态手工配置的时候，
  L104:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MOCN02", SWITCH=ENABLE;
    > ```
    > 
  L130:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;
    > ADD HPLMN: MCC="461", MNC="23", CC="86";
    > ```

### WSFD-207002

**md：`WSFD-207002/激活网络共享（GWCN）场景一：SGSN共享给MNO_85152763.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2GWCN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L54:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开GWCN功能开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置“支持多HPLMN”，请参见 [激活支持多HPLMN功能（适用于SGSN/MME）](../../../组网功能/WSFD-104401 支持多HPLMN功能/激活支持多HPLMN功能（适用于SGSN_MME）_70150791.md) 。
    > 4. **可选：**增加Gs接口配置，为每个PLMN（LAI）配置对应的VLR。
  L90:
    >   //打开License配置开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;
    >   ```
    >   //增加Operator B的MNO标识。
  L109:
    >   //打开License配置开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2GWCN02", SWITCH=ENABLE;
    >   ```
    >   //分别增加Operator A和Operator B的三个RNC，网络指示语为国内备网，信令点编码分别是0xb01、0xb02及0xb03，RNC协议版本为R6，其余参数采用缺省值。

**md：`WSFD-207002/激活网络共享（GWCN）场景二：SGSN共享给MVNO_85152764.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MVNO02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2GWCN02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L56:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开GWCN功能开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置 UNC 支持MVNO，请参见 [激活MVNO](../../WSFD-207005 MVNO/激活MVNO_85152767.md) 。
    > 4. **可选：**增加Gs接口配置，为每个PLMN（LAI）配置对应的VLR。
  L92:
    >   //打开MVNO的License开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2MVNO02", SWITCH=ENABLE;
    >   ```
    >   //增加MVNO标识。
  L113:
    >   //开启GWCN功能开关。
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV2GWCN02", SWITCH=ENABLE;
    >   ```
    >   //增加A、B和C三个RNC，MNC+MCC分别为12300和66000，RNC的标识分别为0、1、2，网络指示语为国内备网，信令点编码分别是0xb01、0xb02及0xb03，RNC协议版本为R6，其余参数采用缺省值。

### WSFD-207005

**md：`WSFD-207005/激活MVNO_85152767.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MVNO02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2MVNO02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L78:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开 [WSFD-210004 MVNO](../WSFD-207005 MVNO_85152766.md) 和 [WSFD-207006 基于LTE的MVNO](../WSFD-207006 基于LTE的MVNO_68260820.md) 特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     3. 增加运营商网络标识。
    >       > **说明**
  L118:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开 [WSFD-210004 MVNO](../WSFD-207005 MVNO_85152766.md) 特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     3. 增加运营商网络标识。
    >       > **说明**
  L158:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开 [WSFD-210004 MVNO](../WSFD-207005 MVNO_85152766.md) 特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     3. 增加MVNO资源配置信息。
    >       [**ADD MVNORES**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MVNO管理/MVNO资源配置表/增加MVNO资源配置信息(ADD MVNORES)_72345665.md)

### WSFD-011201

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3W9BCC12", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L89:
    >   > 配置内容计费费率标识不依赖于内容计费License，但内容计费费率标识需在打开内容计费License后生效。因此，仅在激活内容计费时，执行本步骤。
    >     1. 打开内容计费的License配置开关。
    >       **SET LICENSESWITCH**
    >     2. 配置内容计费使用的URR组及相应URR，从而配置相应的计费费率标识。
    >           a. 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
  L150:
    > 
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV3W9BCC12", SWITCH=ENABLE;
    >   ```
    >   //配置离线计费、且费率标识为（RG，SID）=（10,20）的URR，并将该URR作为上下行URR绑定到URR组上。

### WSFD-011202

**md：`WSFD-011202/激活支持热计费功能_84683735.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2HBILL02 | 本端规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2HBILL02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置计费属性为热计费，并配置相关参数。
    >   [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)
  L56:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2HBILL02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-011202/调测支持热计费功能_85008162.md`**
- 操作步骤上下文（±2 行原文）：
  L43:
    > 2. 执行[**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令查询License配置开关是否已打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0185008162__zh-cn_opi_0130429263_p817039323180642)。
    >     - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 3. 用户开机发起附着。
    >   预期结果：用户成功附着。

### WSFD-011206

**md：`WSFD-011206/调测融合计费的主备CHF的可靠性_89257222.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0289257222__step7889143419175)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开内容计费基本功能对应的License配置开关。
    > 2. 在OM Portal上创建用户跟踪任务。
    > 3. 测试终端使用 “apn-test” DNN接入网络。

**md：`WSFD-011206/调测融合计费的流量计费功能_89257221.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0289257221__step7889143419175)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开内容计费基本功能对应的License配置开关。
    > 2. 在OM Portal上创建用户跟踪任务。
    > 3. 测试终端使用 “apn-test” DNN接入网络。

**md：`WSFD-011206/调测融合计费的缓存消息回放功能_90005269.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0290005269__step1629145118345)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开内容计费基本功能对应的License配置开关。
    > 2. 开启计费缓存功能。
    >     - [**SET FAILHANDLING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)命令“FHACTION”参数配置为“CONTINUE”。

**md：`WSFD-011206/调测融合计费的计费Trigger上报功能_89257220.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0289257220__step7889143419175)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开内容计费基本功能对应的License配置开关。
    > 2. 在OM Portal上创建用户跟踪任务。
    > 3. 测试终端使用 “apn-test” DNN接入网络。

**md：`WSFD-011206/调测融合计费的计费会话创建功能_89257219.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    >   ```
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0289257219__step7889143419175)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开内容计费基本功能对应的License配置开关。
    > 2. 在OM Portal上创建用户跟踪任务。
    > 3. 测试终端使用 “apn-test” DNN接入网络。

### WSFD-109001

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3W9BCC12", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L93:
    >   > 配置内容计费费率标识不依赖于内容计费License，但内容计费费率标识需在打开内容计费License后生效。因此，仅在激活内容计费时，执行本步骤。
    >     1. 打开内容计费的License配置开关。
    >       **SET LICENSESWITCH**
    >     2. 配置内容计费使用的URR组及相应URR，从而配置相应的计费费率标识。
    >           a. 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
  L154:
    > 
    >   ```
    >   SET LICENSESWITCH: LICITEM="LKV3W9BCC12", SWITCH=ENABLE;
    >   ```
    >   //配置在线计费、且费率标识为（RG，SID）=（10,20）的URR，并将该URR作为上下行URR绑定到URR组上。

### WSFD-109002

**md：`WSFD-109002/激活内容计费_74013177.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > 
    > 1. 激活内容计费的License。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 参见 [配置在线计费的费率标识](../WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置在线计费的费率标识_95923388.md) 或 [配置融合计费费率标识](../WSFD-011206 支持融合计费/激活支持融合计费/配置融合计费费率标识_93360308.md) 。
    >   > **说明**

### WSFD-109003

**md：`WSFD-109003/激活基于业务时长的计费_74013179.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="`
- 操作步骤上下文（±2 行原文）：
  L56:
    > 
    > 1. 激活基于业务时长的计费的License。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 修改在线计费模板/离线计费模板/融合计费模板，配置基于业务时长的计费。
    >   [**MOD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
  L75:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="
    > LKV3W9TBCS12
    > ", SWITCH=ENABLE;

### WSFD-109004

**md：`WSFD-109004/激活基于业务流量的计费_74013202.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3WPVBCS11", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L43:
    > 
    > 1. 激活基于业务流量的计费的License。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 修改在线计费模板/融合计费模板，配置基于业务流量的计费。
    >   [**MOD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
  L61:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3WPVBCS11", SWITCH=ENABLE;
    > ```
    > 

### WSFD-109005

**md：`WSFD-109005/激活支持CoA功能_10243675.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2UNCCOA1", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L53:
    > 
    > 1. 打开本特性的License开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 配置COA功能使能开关。
    >     a. 指定APN实例名称。
  L82:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2UNCCOA1", SWITCH=ENABLE;
    > ```
    > 

### WSFD-109006

**md：`WSFD-109006/激活ASN漫游计费_01125477.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3W9ASNR11", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L45:
    > 
    > 1. 打开本特性的License开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 配置ASN功能开关属性。
    >   **[SET ASNFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/GTP-C接口配置管理/ASN功能管理/设置ASN功能（SET ASNFUNC）_35519283.md)**
  L66:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3W9ASNR11", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-109006/调测ASN漫游计费_48173747.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > ## [操作步骤](#ZH-CN_OPI_0000001148173747)
    > 
    > 1. 进入 “MML命令行-UNC” 窗口。 执行 [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令，查询License中是否允许使用ASN漫游计费功能。
    >     - 如果License的ASN漫游计费功能项为“DISABLE”，则设备不支持ASN漫游计费功能，请打开License开关后继续调测本功能。
    >     - 如果License的ASN漫游计费功能项为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0000001148173747__step676020446172)。

### WSFD-109007

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3W9EBCS12", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L71:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开事件计费的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互建立计费会话。
    >   [**SET CHFINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md)
  L115:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3W9EBCS12", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102001

**md：`WSFD-102001/激活VoLTE基础语音业务（适用于MME）_64009863.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VOLTE01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    >   [**ADD IPV4DNSH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)
    > 3. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 4. 配置系统支持VoLTE语音业务。
    >   [**SET IMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/VoPS管理/设置VoPS配置(SET IMSVOPS)_72345711.md)
  L66:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2VOLTE01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-102001/激活VoLTE基础语音业务（适用于SGW-C_PGW-C）_67930995.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3W9IMSA12", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > 3. 开启全局缺省PCC开关。
  L69:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3W9IMSA12", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102004

**md：`WSFD-102004/激活基于VoLTE的优先语音服务（适用于MME）_68230386.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EMPS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L50:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **推荐：** 部署语音寻呼优先业务。
    >   [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)
  L73:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EMPS01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102101

**md：`WSFD-102101/激活VoLTE紧急呼叫（适用于MME）_70014693.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VLEC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L51:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置紧急号码信息。
    >   ![](激活VoLTE紧急呼叫（适用于MME）_70014693.assets/notice_3.0-zh-cn_2.png)
  L171:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2VLEC01", SWITCH=ENABLE;
    > ```

**md：`WSFD-102101/激活VoLTE紧急呼叫（适用于SGW-C_PGW-C）_30394882.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3W9ECAL11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L46:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置APN参数。
    >     a. 配置APN所属的VPN实例。
  L71:
    > 1. 打开本特性的License配置开关。
    >   ```
    >   SET LICENSESWITCH:LICITEM="LKV3W9ECAL11",SWITCH=ENABLE;
    >   ```
    > 2. 使能紧急呼叫功能。

**md：`WSFD-102101/调测VoLTE紧急呼叫（适用于SGW-C_PGW-C）_95090216.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    >   [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3W9ECAL11";
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0295090216__cmd103264131184656)。
    >     - 如果“SWITCH”为“DISABLE”，则执行 [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 在OM Portal上 [用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在 “参数配置” 栏输入用户IMSI ，在 “消息类型” 栏选择GTPC消息类型。
    >   > **说明**

**md：`WSFD-102101/调测VoWIFI紧急呼叫_95090217.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    >   [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3W9ECAL11";
    >     - 如果“SWITCH”为“ENABLE”，请执行[3](调测VoLTE紧急呼叫（适用于SGW-C_PGW-C）_95090216.md#ZH-CN_OPI_0295090216__cmd103264131184656)。
    >     - 如果“SWITCH”为“DISABLE”，则执行 [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
    > 3. 在OM Portal上 [用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在 “参数配置” 栏输入用户IMSI ，在 “消息类型” 栏选择GTPC消息类型。
    >   > **说明**

### WSFD-102202

**md：`WSFD-102202/激活P-CSCF故障时IMS业务恢复_26216211.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3W9IMSR11", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L58:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开该功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 修改APN参数。
    >   [**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)
  L85:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3W9IMSR11", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-102202/调测P-CSCF故障时IMS业务恢复_26216212.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > 
    >   - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0226216212__step20209124118175)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 在LMT上启动用户跟踪，准备抓取用户信令报文。
    > 3. 用户进行IMS业务。

### WSFD-102203

**md：`WSFD-102203/WSFD-102203 基于PCRF_PCF的VoLTE业务快速恢复参考信息_89991355.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)
    > - **[SET APNREPORTATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**

### WSFD-102702

**md：`WSFD-102702/激活EPS Fallback_76175590.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EFBAM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2EFBSM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L57:
    > 1. 进入 “MML命令行-UNC” 窗口。 -AMF
    > 2. 打开AMF该功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置系统支持IMS Voice Over PS服务。
    >   **[SET NGIMSVOPS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/设置VoPS配置（SET NGIMSVOPS）_09653214.md)**
  L67:
    > 5. 进入 “MML命令行-UNC” 窗口。 -SMF
    > 6. 打开SMF该功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 7. 配置IMS网络APN。
    >   **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
  L96:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EFBAM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2EFBSM01", SWITCH=ENABLE;
    > ```

**md：`WSFD-102702/调测EPS Fallback_82220358.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > 1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 查询WSFD-102702 EPS Fallback功能对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0182220358__cmd1098161310282)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 验证UE语音EPS Fallback可实现。
    >     a. 在MME、AMF的OM Portal上创建用户跟踪任务。5G用户开机注册。

### WSFD-201203

**md：`WSFD-201203/WSFD-201203 S-GW_P-GW故障下的业务恢复参考信息_92137768.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**LST PGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/P-GW属性/查询P-GW特性对接配置（LST PGWCHARACT）_72225619.md)
    > - [**ADD GWRESTORAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/网关故障管理/增加网关容灾APN(ADD GWRESTORAPN)_72225761.md)
    > - [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0192137768)

**md：`WSFD-201203/激活S-GW_P-GW故障下的业务恢复_91473804.md`**
- 数据规划表（该命令的参数行）：
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SRGF01 | 本端规划 | 打开本特性的License配置开关。 |
  | [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开本特性的License配置开关。 |
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2SRGF01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L122:
    >             > - 如果S-GW和P-GW非合一，则本步骤需要执行[**ADD SGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md)和[**ADD PGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/P-GW属性/增加P-GW特性对接配置（ADD PGWCHARACT）_26305748.md)两个命令。
    > 5. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0191473804)
  L179:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2SRGF01", SWITCH=ENABLE;
    > ```

### WSFD-201205

**md：`WSFD-201205/激活基于HSS的P-CSCF故障恢复（适用于IMS PDN 重建）_90107949.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L43:
    >   命令 [**SET DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) 和 [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 中除 “用户范围” 、 “运营商标识” 以及 “IMSI前缀” 外的其余参数功能均相同，且若系统中同时存在这两条命令的配置，系统会优先匹配命令 [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 的配置。因此在配置 [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 前需先执行 [**LST DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/查询Diameter兼容配置(LST DMCMPT)_72345869.md) 查询系统中 [**SET DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) 的配置记录，确保命令 [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 的配置记录中所携带的参数默认值不影响系统已有配置。
    > 3. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 4. **可选：**清除HSS信息。
    >   [**CLR HSSINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Diameter应用协议/HSS管理/清除HSS信息(CLR HSSINFO)_72225137.md)
  L78:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-201205/激活基于HSS的P-CSCF故障恢复（适用于承载更新）_21873364.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L71:
    >   PCO-based optional extension功能同时受License和MML命令的控制，只有License和该步骤MML全部开启功能才生效。
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 5. **可选：**清除HSS信息。
    >   [**CLR HSSINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Diameter应用协议/HSS管理/清除HSS信息(CLR HSSINFO)_72225137.md)
  L129:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102003

**md：`WSFD-102003/激活SRVCC特性（适用于SGW-C_PGW-C）_30364774.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:LICITEM="LKV3WPRVCC11",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L27:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0230364774)
  L40:
    > 
    > ```
    > SET LICENSESWITCH:LICITEM="LKV3WPRVCC11",SWITCH=ENABLE;
    > ```

### WSFD-102102

**md：`WSFD-102102/激活VoLTE紧急呼叫的定位(NI-LR)_70014699.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NVEC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L105:
    >       > [**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) 与 [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 命令均可对Diameter兼容性参数进行配置。系统会首先匹配 [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 命令的配置记录，若发现系统中不存在或不匹配 [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 命令的配置记录，才会匹配 [**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) 命令的配置记录。
    > 7. 打开特性开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0170014699)
  L179:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NVEC01", SWITCH=ENABLE;
    > ```

### WSFD-102301

**md：`WSFD-102301/激活基于CSFB的语音业务_37661227.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFBGU02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFBGU02", SWITCH=ENABLE;
    > ```

### WSFD-102401

**md：`WSFD-102401/激活基于CSFB的USSD业务_66296851.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFBEP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置SGs和Sv接口合一选择MSC。
    >   > **说明**
  L69:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFBEP01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102402

**md：`WSFD-102402/激活基于CSFB的LCS业务_64009898.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFBEP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置SGs和Sv接口合一选择MSC。
    >   > **说明**
  L68:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFBEP01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102404

**md：`WSFD-102404/激活基于CSFB的LA快速选择_64009906.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFBEP01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L29:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置S1接口支持Register LAI信元。
    >   [**SET S1CMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md)
  L44:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFBEP01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102501

**md：`WSFD-102501/激活CSFB紧急呼叫_64009912.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFBEC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    >   [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0164009912)
  L58:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFBEC01", SWITCH=ENABLE;
    > ```

### WSFD-102502

**md：`WSFD-102502/激活基于CSFB的优先语音服务_37666597.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFB05", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFB05", SWITCH=ENABLE;
    > ```

### WSFD-102503

**md：`WSFD-102503/激活CSFB被叫恢复_37666598.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSCR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSCR01", SWITCH=ENABLE;
    > ```

### WSFD-102504

**md：`WSFD-102504/激活MSC Pool场景下的CSFB_64009924.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFBMP02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L79:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 建立MME和MSC之间的设备间通信。
    >     a. 添加MME和MSC之间偶联路径的SCTP参数模板。
  L125:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFBMP02", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102505

**md：`WSFD-102505/激活基于CSFB的Multi PLMN_64009927.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFB04", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L29:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置基于CSFB的Multi PLMN特性参数。
    >   **[ADD TAILAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)**
  L44:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFB04", SWITCH=ENABLE;
    > ```
    > 

### WSFD-102506

**md：`WSFD-102506/激活Flash CSFB with RIM_37666599.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2CSFB03", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2CSFB03", SWITCH=ENABLE;
    > ```

### WSFD-102601

**md：`WSFD-102601/激活LTE一键通基础功能（适用于MME）_64009969.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2PPTF01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开 LTE一键通基础功能 的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置PTT业务QCI和标准QCI的映射规则。
    >   [**ADD QCICONV**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/扩展QCI转换关系/增加扩展QCI转换关系(ADD QCICONV)_26306024.md)
  L50:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2PPTF01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-102601/WSFD-102601 LTE一键通基础功能参考信息（适用于PGW-C_SGW-C）_39305377.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)
    > 

**md：`WSFD-102601/激活WSFD-102601 LTE一键通基础功能（适用于PGW-C_SGW-C）_39305629.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV3WNPLTE11", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L31:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开 LTE一键通基础功能 的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001339305629)
  L46:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV3WNPLTE11", SWITCH=ENABLE;
    > ```

### WSFD-102602

**md：`WSFD-102602/激活LTE一键通（适用于MME）_64009972.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2QPPT01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L54:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开 LTE一键通 功能特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置PTT APN以及PTT业务寻呼优先级。
    >   [**ADD APNPAGINGPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/基于APN的寻呼策略配置/增加APN寻呼策略参数配置(ADD APNPAGINGPLCY)_72225389.md)
  L77:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2QPPT01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-102602/激活LTE一键通（适用于PGW-C_SGW-C）_10282625.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2QPPT02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L105:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开 LTE一键通 功能特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 基于全局的一键通业务配置：
    >     a. 查询PTT业务QCI是否已经配置为标准QCI。
  L150:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2QPPT02", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-102602/调测LTE一键通（适用于PGW-C_SGW-C）_10282626.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > 
    >   - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0310282626__step767223614014)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 在OM Portal上创建用户跟踪任务，在“参数配置”栏输入用户IMSI，其他参数：选择默认值。
    > 3. 测试终端使用“apn1”接入网络。

### WSFD-102703

**md：`WSFD-102703/激活EPS Fallback紧急呼叫_26162693.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EFEC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L38:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开该功能的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置是否允许紧急呼叫业务。
    >   **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
  L65:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EFEC01", SWITCH=ENABLE;
    > ```
    > 

**md：`WSFD-102703/调测EPS Fallback紧急呼叫_26162694.md`**
- 操作步骤上下文（±2 行原文）：
  L29:
    > 1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 查询WSFD-102703 EPS Fallback紧急呼叫功能对应的License配置开关是否打开。
    >     - 如果“SWITCH”为“ENABLE”，请执行[2](../../../../业务专题/5G Core 4_5G互操作解决方案/调测指导/调测LTE到5G SA网络间重选_01_10046.md#ZH-CN_OPI_0190799286__cmd1098161310282)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. UE接入5G网络。
    > 3. UE拨打紧急呼叫电话时，UE在Service Request消息中携带的service type值为emergency services fallback。

### WSFD-102706

**md：`WSFD-102706/激活VoNR紧急呼叫_46685913.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VONRECMM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2VONRECSM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L75:
    > 
    > 1. 打开本特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 2. 配置是否允许紧急呼叫业务。
    >   **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
  L92:
    > 
    > 7. 打开本特性的License配置开关。
    >   **[SET LICENSESWITCH](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 8. 配置APN参数，并将APN下的某指定号段绑定到P-CSCF组，使能紧急呼叫功能。
    >   创建APN实例。
  L122:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2VONRECMM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2VONRECSM01", SWITCH=ENABLE;
    > ```

**md：`WSFD-102706/调测VoNR紧急呼叫_46687733.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    >     a. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 查询本特性对应的AMF和SMF的License配置开关是否打开。
    >           - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0000001446687733__cmd648832471710)。
    >           - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 调测VoNR紧急呼叫功能。
    >     a. 在AMF的OM Portal上创建用户跟踪任务。

### WSFD-201001

**md：`WSFD-201001/激活基于SRVCC的数据语音双切换_70014705.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2DVSS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L33:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**设置切换流程资源释放定时器。
    >   [**SET EMM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM协议参数管理/S1模式MM协议参数/设置S1模式MM协议参数(SET EMM)_72225207.md)
  L50:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2DVSS01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-201002

**md：`WSFD-201002/激活用户群语音策略控制_64009940.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VPCU01", SWITCH=ENABLE`
- 操作步骤上下文（±2 行原文）：
  L55:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 打开本特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >       > **说明**
    >       > MME被共享的场景下，语音策略的配置过程和MME不被共享情况下的类似。 [步骤 4](#ZH-CN_OPI_0164009940__step2_Local) 到 [步骤 5](#ZH-CN_OPI_0164009940__step3_foreign) 为MME不被共享场景下的配置过程。
  L144:
    >       [**SET IMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/VoPS管理/设置VoPS配置(SET IMSVOPS)_72345711.md)
    >     8. 打开用户群语音策略控制特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0164009940)
  L176:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2VPCU01", SWITCH=ENABLE
    > ```
    > 

### WSFD-201003

**md：`WSFD-201003/激活网络语音业务信息上报功能_75538866.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2NVIR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L40:
    >   [**SET CHRLOWPERFSVRSUB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/低性能CHR服务器的单据订阅条件/设置低性能CHR服务器的单据订阅条件（SET CHRLOWPERFSVRSUB）_72345083.md)
    > 4. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0275538866)
  L65:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2NVIR01", SWITCH=ENABLE;
    > ```

### WSFD-201004

**md：`WSFD-201004/激活基于IMEI的语音策略控制_70014723.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VPCU01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2VPCI01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2VPCU01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2VPCI01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L40:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >   > **说明**
    >   > 本特性和“ [1.2-WSFD-201002 用户群语音策略控制](../WSFD-201002 用户群语音策略控制_70014708.md) ”特性交互部署存在以下方式，运营商可以根据实际情况选择：
  L70:
    >   a. 打开 **用户群语音策略控制** 特性的License配置开关。
    >       ```
    >       SET LICENSESWITCH: LICITEM="LKV2VPCU01", SWITCH=ENABLE;
    >       ```
    >     b. 配置用户群语音策略。
  L86:
    >   a. 打开 **基于IMEI的语音策略控制** 特性的License配置开关。
    >       ```
    >       SET LICENSESWITCH: LICITEM="LKV2VPCI01", SWITCH=ENABLE;
    >       ```
    >     b. 增加IMEI群组信息。

### WSFD-201005

**md：`WSFD-201005/激活基于区域的语音策略控制_64009949.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VPCL01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L49:
    >       [**SET IMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/VoPS管理/设置VoPS配置(SET IMSVOPS)_72345711.md)
    >     4. 打开本特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - 同时部署
    >   同时部署 [WSFD-102001 VoLTE基础语音业务](../WSFD-102001 VoLTE基础语音业务_67023607.md) 和本特性。例如在新建局点部署VoLTE语音业务，且MME覆盖区域仅有部分E-UTRAN支持VoLTE语音业务。
  L61:
    >       [**SET IMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/VoPS管理/设置VoPS配置(SET IMSVOPS)_72345711.md)
    >     4. 打开本特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     5. 打开VoLTE基础语音业务特性的License开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
  L63:
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    >     5. 打开VoLTE基础语音业务特性的License开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0164009949)

### WSFD-201007

**md：`WSFD-201007/激活SRVCC的MSC拓扑选择_70014741.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MTSS01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L46:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 配置基于Sv接口选择SGs/Sv合一的MSC。
    >   > **说明**
  L74:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MTSS01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-201101

**md：`WSFD-201101/激活VoLTE一号多卡_70014747.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MIVT01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L30:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**针对漫游用户，设置软参DWORD_EX13 Bit1值为1，使漫游用户的VoLTE一号多卡功能生效。
    >   [**SET SOFTPARAOFBIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/操作维护/软件参数管理/软件参数比特位/设置软件参数表比特位(SET SOFTPARAOFBIT)_72345783.md)
  L47:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MIVT01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-201102

**md：`WSFD-201102/激活语音业务的位置信息策略控制功能_72660317.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VLPC01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L31:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**设置MME支持位置信息查询。
    >     - 针对所有用户设置MME支持位置信息查询。
  L64:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2VLPC01", SWITCH=ENABLE;
    > ```
    > 

### WSFD-201103

**md：`WSFD-201103/激活IMS功能_91473678.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 设置特定GGSN支持R5及R5以上版本QoS。
    >   [**ADD GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md)

### WSFD-201201

**md：`WSFD-201201/激活MME链式备份_75538863.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2MCR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L100:
    >       [**MOD S1USRSECPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/用户安全管理/S1模式用户安全参数/修改S1模式用户安全配置(MOD S1USRSECPARA)_26145650.md)
    > 10. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0275538863)
  L138:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2MCR01", SWITCH=ENABLE;
    > ```

### WSFD-201202

**md：`WSFD-201202/激活本地VLR_76948720.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2LVLR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L38:
    >   > 为避免对HSS造成信令冲击，建议执行本步骤，将 “HSS注册策略（DULR）” 配置为 “DELAY” 。
    > 3. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0276948720)
  L57:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2LVLR01", SWITCH=ENABLE;
    > ```

### WSFD-201204

**md：`WSFD-201204/激活VoLTE承载故障快速恢复（适用于MME）_86652961.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VTBR01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0286652961)
  L48:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2VTBR01", SWITCH=ENABLE;
    > ```

### WSFD-201208

**md：`WSFD-201208/激活VoLTE承载延时保活_90437921.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2BHVT01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L37:
    >   **SET ESM**
    > 3. 打开本特性的License配置开关。
    >   **SET LICENSESWITCH**
    > 
    > ## [任务示例](#ZH-CN_OPI_0000002490437921)
  L56:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2BHVT01", SWITCH=ENABLE;
    > ```

### WSFD-221001

**md：`WSFD-221001/激活VoNR承载延时保活_11685432.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2VCHSM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L48:
    >   **[SET QOSFLOWFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/设置QoS Flow扩展功能（SET QOSFLOWFUNC）_38788439.md)**
    > 5. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001111685432)
  L81:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2VCHSM01", SWITCH=ENABLE;
    > ```

### WSFD-221002

**md：`WSFD-221002/激活基于UDM的VoNR语音故障恢复（适用于AMF）_28824215.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L34:
    >   **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
    > 3. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0228824215)
  L55:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;
    > ```

### WSFD-221003

**md：`WSFD-221003/参考信息_90263269.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)
    > 

**md：`WSFD-221003/激活基于PCF的VoNR业务快速恢复_90423111.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH:ITEM="LKV2FRVNRPCF01",SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L31:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001190423111)
  L46:
    > 
    > ```
    > SET LICENSESWITCH:ITEM="LKV2FRVNRPCF01",SWITCH=ENABLE;
    > ```

### WSFD-220002

**md：`WSFD-220002/激活SBI IMR信令上报_31537766.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2IMRSDRSM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2IMRSDRAM01", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L76:
    >       **[DSP VPROBELNKSTAT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/vProbe管理/vProbe服务器链路状态/显示vProbe链路状态（DSP VPROBELNKSTAT）_39242821.md)**
    >     e. vProbe部署完成，且链路正常后，打开本特性的License配置开关。
    >       [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000002131537766)
  L114:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IMRSDRSM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IMRSDRAM01", SWITCH=ENABLE;
    > ```
  L115:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2IMRSDRSM01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2IMRSDRAM01", SWITCH=ENABLE;
    > ```

### WSFD-106002

**md：`WSFD-106002/激活支持EDGE功能（仅用于Gb模式）_43355961.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2EDGE02", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L32:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 打开本特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0243355961)
  L45:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2EDGE02", SWITCH=ENABLE;
    > ```

### WSFD-210000

**md：`WSFD-210000/激活5G超高带宽基本功能及其高速承载接入_73712144.md`**
- 任务示例脚本（该命令行）：
  `SET LICENSESWITCH: LICITEM="LKV2UNCBASE01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UNCBAND01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UNCBASE02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UNCBAND02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UHBBAM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UHBAAM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UHBBF10G", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UHBA10G", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UHBBF20G", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UHBA20G", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W95UHB01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W95UBA01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W95UHB02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W95UBA02", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UHBBSM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV2UHBASM01", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W95UHB10", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W95UBA10", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W95UHB20", SWITCH=ENABLE;`
  `SET LICENSESWITCH: LICITEM="LKV3W95UBA20", SWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L35:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 重复执行如下命令，依次打开5G超高带宽基本功能（1Gbps）、5G超高带宽高速承载接入（1Gbps）、5G超高带宽基本功能（2Gbps）、5G超高带宽高速承载接入（2Gbps）、5G超高带宽基本功能（5Gbps）、5G超高带宽高速承载接入（5Gbps）、5G超高带宽基本功能（10Gbps）、5G超高带宽高速承载接入（10Gbps）、5G超高带宽基本功能（20Gbps）和5G超高带宽高速承载接入（20Gbps）的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0173712144)
  L50:
    > 
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2UNCBASE01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2UNCBAND01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2UNCBASE02", SWITCH=ENABLE;
  L51:
    > ```
    > SET LICENSESWITCH: LICITEM="LKV2UNCBASE01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2UNCBAND01", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2UNCBASE02", SWITCH=ENABLE;
    > SET LICENSESWITCH: LICITEM="LKV2UNCBAND02", SWITCH=ENABLE;

## ④ 自动比对
- 命令真相参数（2）：['LICITEM', 'SWITCH']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 42, '全网规划': 16}（多值→atom 应考虑 decision_driven）
