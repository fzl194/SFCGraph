# 命令证据包：ADD FLOWFILTER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md`
> 用该命令的特性数：6

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于添加流过滤器。主要有两个用途：

UL CL分流场景下，在会话相关流程中，SMF会将流过滤器下发给UPF，UPF基于流过滤器执行相应的数据转发动作。ADC场景下，用于匹配PCF下发的ADC规则中的AppId，若匹配成功则将该ADC规则下发给UPF，指示UPF进行应用检测（详情参见WSFD-109102 ADC基本功能）。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100000。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| FLOWFILTERNAME | 流过滤器名称 | 对端协商 | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-108002

**md：`WSFD-108002/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md) | 流过滤器名称（FLOWFILTERNAME） | ulcl | 与对端协商 | 配置App ID |
- 任务示例脚本（该命令行）：
  `ADD FLOWFILTER: FLOWFILTERNAME="ulcl";`
  `ADD FLOWFILTER: FLOWFILTERNAME="ulcl";`
  `ADD FLOWFILTER: FLOWFILTERNAME="ulcl";`
- 操作步骤上下文（±2 行原文）：
  L78:
    >       [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    >     b. 配置ULCL过滤器名称。
    >       [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    >     c. 配置ULCL分流策略rule。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L125:
    > ADD ULCLPROP: ULCLPROPNAME="testulclpropname", DNAI="testdnai"; 
    > //配置ULCL过滤器名称。
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > //配置ULCL分流策略rule。
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
  L151:
    > ADD ULCLPROP: ULCLPROPNAME="testulclpropname", DNAI="testdnai"; 
    > //配置ULCL过滤器名称。
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > //配置ULCL分流策略rule。
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 

### WSFD-223001

**md：`WSFD-223001/WSFD-223001 基于位置信息的分流策略控制参考信息_47717539.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD NGPRA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/网络开放管理/5G PRA管理/5G PRA标识管理/增加5G PRA（ADD NGPRA）_44006470.md)

**md：`WSFD-223001/部署基于位置信息的分流策略控制（SMF）_53995959.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md) | 流过滤器名称（FLOWFILTERNAME） | ulcl | 与对端协商 | 配置App ID |
- 任务示例脚本（该命令行）：
  `ADD FLOWFILTER: FLOWFILTERNAME="ulcl";`
- 操作步骤上下文（±2 行原文）：
  L51:
    > ADD ULCLPROP: ULCLPROPNAME="testulclpropname", DNAI="testdnai"; 
    > //配置ULCL过滤器名称。
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > //配置ULCL分流策略rule。
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > 
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD FLOWFILTER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md) | 流过滤器名称（FLOWFILTERNAME） | ulcl | 与对端协商 | 配置App ID |
- 任务示例脚本（该命令行）：
  `ADD FLOWFILTER: FLOWFILTERNAME="ulcl";`
- 操作步骤上下文（±2 行原文）：
  L54:
    >       [**ADD ULCLPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    >     b. 配置ULCL过滤器名称。
    >       [**ADD FLOWFILTER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    >     c. 配置ULCL分流策略rule。
    >       [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L99:
    > ADD ULCLPROP: ULCLPROPNAME="testulclpropname", DNAI="testdnai"; 
    > //配置ULCL过滤器名称。
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > //配置ULCL分流策略rule。
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 

### WSFD-223101

**md：`WSFD-223101/WSFD-223101 基于预定义规则的分流策略控制(4G)参考信息_11634944.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-223101/部署基于预定义规则的分流策略控制(4G)（SMF）_11155006.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md) | 流过滤器名称（FLOWFILTERNAME） | ulcl | 与对端协商 | 配置App ID |
- 任务示例脚本（该命令行）：
  `ADD FLOWFILTER: FLOWFILTERNAME="ulcl";`
- 操作步骤上下文（±2 行原文）：
  L58:
    >       [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    >     b. 配置ULCL过滤器名称。
    >       [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    >     c. 配置ULCL分流策略rule。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L100:
    > 
    > ```
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > ```
    > 

### WSFD-109102

**md：`WSFD-109102/激活ADC基本功能_92582136.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md) | 流过滤器名称（FLOWFILTERNAME） | flowfilter_ADC01 | 本端规划 | 不同流过滤器之间，该参数不能重复。<br>GGSN-C/PGW-C/SMF、PGW-U/UPF、PCRF/PCF三个网元上的该参数必须一致，否则无法正常上报。 |
- 任务示例脚本（该命令行）：
  `ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";`
- 操作步骤上下文（±2 行原文）：
  L49:
    > 2. PCRF/PCF要下发应用Start和Stop的两个Event Trigger，当PCRF/PCF通过动态规则下发appid时，请执行本步骤。
    >     a. 配置ADC业务使用的appid。
    >       [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    >     b. 配置ADC参数。
    >       [**ADD ADCPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/ADC/ADC参数/增加ADC参数（ADD ADCPARA）_65996998.md)
  L80:
    > 
    > ```
    > ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";
    > ```
    > 

### WSFD-011306

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD FLOWFILTER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md) | 流过滤器名称（FLOWFILTERNAME） | flowfilter_1 | 与对端协商 | 需要与UPF/PGW-U上规划的流过滤器保持一致。 |
- 操作步骤上下文（±2 行原文）：
  L57:
    >       **[SET APNRDSACCTCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS计费管理/APN计费控制/设置APN RADIUS计费控制参数（SET APNRDSACCTCTRL）_09896770.md)**
    > 3. 配置业务使用的流过滤器。
    >   **[**ADD FLOWFILTER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)**
    > 4. 配置业务规则。
    >   [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

## ④ 自动比对
- 命令真相参数（1）：['FLOWFILTERNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'与对端协商': 5, '本端规划': 1}（多值→atom 应考虑 decision_driven）
