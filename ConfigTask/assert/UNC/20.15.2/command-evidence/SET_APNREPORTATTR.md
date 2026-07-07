# 命令证据包：SET APNREPORTATTR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于修改SMF与PCRF/PCF交互的消息使用的APN类型、性能统计使用的APN类型、CG话单使用的APN类型、与AAA交互的鉴权消息和计费消息使用APN类型、以及与OCS/CHF交互使用的APN类型。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 每个APN支持一条配置。
- 当系统未配置时，使用该命令增加性能统计及和各网元交互使用的APN类型配置，当系统存在该配置时，使用该命令修改配置。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：CONGESTIONRPT：DISABLE，INTELLIGENTSEL：DISABLE，LOCATIONREPORT：

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无。 | 字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字 |
| CONGESTIONRPT | 拥塞控制 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- DISABLE（不使能） |
| INTELLIGENTSEL | 智能网关选择 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- DISABLE（不使能） |
| LOCATIONREPORT | 实时位置 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- DISABLE（不使能） |
| MAPTRANSDATA | 通过本地配置获取VLR ID/Global Title | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- DISABLE（不使能） |
| AAAACCT | 上报给AAA计费的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |
| AAAAUTH | 上报给AAA鉴权的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |
| CG | 上报给CG的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |
| DIAMETERAAA | 上报给Diameter AAA的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |
| OCS | 上报给OCS的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |
| CHF | 上报给CHF的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |
| PCRF | 上报给PCRF的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |
| PCF | 上报给PCF的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |
| PERFORMANCE | 上报给话统的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | 当配置使用的APN类型为REQUESTED时：如果用户激活请求里的APN是别名APN，则对于性能统计 |
| UPF | 上报给用户面的APN名 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNR | <br>- REQUESTED（请求的） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-106203

**md：`WSFD-106203/激活别名APN_34797880.md`**
- 数据规划表（该命令的参数行）：
  | **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** | 上报给PCF的APN名（PCF） | SERVICE | 本端规划 | 在每次执行<br>[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>时会自动增加对应的<br>**[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**<br>配置记录，需要将真实APN的<br>“PCF”<br>和<br>“CHF”<br>配置为<br>“SERVICE”<br>。 |
  | **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** | 上报给CHF的APN名（CHF） | SERVICE | 本端规划 | 在每次执行<br>[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>时会自动增加对应的<br>**[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**<br>配置记录，需要将真实APN的<br>“PCF”<br>和<br>“CHF”<br>配置为<br>“SERVICE”<br>。 |
- 任务示例脚本（该命令行）：
  `SET APNREPORTATTR: APN="apn5", PCF=SERVICE, CHF=SERVICE;`
- 操作步骤上下文（±2 行原文）：
  L68:
    > 3. 配置真实APN。
    >   [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 4. 配置APN的上报属性。在每次执行 [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 时会自动增加对应的 **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** 配置记录，需要将真实APN的 “PCF” 和 “CHF” 配置为 “SERVICE” 。
    >   **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**
    > 5. 配置别名APN和转换APN。
  L69:
    >   [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 4. 配置APN的上报属性。在每次执行 [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 时会自动增加对应的 **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** 配置记录，需要将真实APN的 “PCF” 和 “CHF” 配置为 “SERVICE” 。
    >   **[SET APNREPORTATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**
    > 5. 配置别名APN和转换APN。
    >   [**ADD APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/增加APN别名配置（ADD APNALIAS）_28567622.md)
  L99:
    >   ```
    >   ADD APN: APN="apn5";
    >   SET APNREPORTATTR: APN="apn5", PCF=SERVICE, CHF=SERVICE;
    >   ```
    > 3. 别名APN名称为“apn1”和“apn2”，配置真实APN为 “apn5”。

### WSFD-211101

**md：`WSFD-211101/WSFD-211101 基于小区负荷上报的无线资源优化参考信息_34615790.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD APNREPORTATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0000001134615790)

**md：`WSFD-211101/激活基于小区负荷上报的无线资源优化_80495435.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNREPORTATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md) | APN（APN） | apn1 | 全网规划 | 使能基于APN的小区拥塞上报功能。 |
  | [**SET APNREPORTATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md) | 拥塞控制（CONGESTIONRPT） | ENABLE | 全网规划 | 使能基于APN的小区拥塞上报功能。 |
- 任务示例脚本（该命令行）：
  `SET APNREPORTATTR: APN="apn1", CONGESTIONRPT=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L38:
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 使能基于APN的小区拥塞上报功能。
    >   [**SET APNREPORTATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001180495435)
  L57:
    > 
    > ```
    > SET APNREPORTATTR: APN="apn1", CONGESTIONRPT=ENABLE;
    > ```
    > 

**md：`WSFD-211101/调测基于小区负荷上报的无线资源优化_34456008.md`**
- 操作步骤上下文（±2 行原文）：
  L77:
    >   ```
    >     - 是，请执行[步骤 11](#ZH-CN_OPI_0000001134456008__step114691314193316)。
    >     - 否，请执行[**SET APNREPORTATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)，将指定APN下的“CONGESTIONRPT”设置为“ENABLE”，然后重新执行[步骤 3](#ZH-CN_OPI_0000001134456008__step9780829144815)。
    > 11. 请联系华为技术支持工程师。
    >     a. 重新执行上述步骤并保存报文。

### WSFD-102203

**md：`WSFD-102203/WSFD-102203 基于PCRF_PCF的VoLTE业务快速恢复参考信息_89991355.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > - [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)
    > - **[SET APNREPORTATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0000001189991355)

**md：`WSFD-102203/激活基于PCRF_PCF的VoLTE业务快速恢复_43991630.md`**
- 数据规划表（该命令的参数行）：
  | **[SET APNREPORTATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** | APN名称（APN） | ims.real | 本端规划 | 将真实使用的APN与终端上报的APN配置映射关系。 |
  | **[SET APNREPORTATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** | 上报给PCRF的APN名<br>（PCRF） | REQUESTED | 本端规划 | 将真实使用的APN与终端上报的APN配置映射关系。 |
- 任务示例脚本（该命令行）：
  `SET APNREPORTATTR: APN="ims.real", PCRF=REQUESTED;`
- 操作步骤上下文（±2 行原文）：
  L38:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 将真实使用的APN与终端上报的APN配置映射关系。
    >   **[SET APNREPORTATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**
    > 3. 配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。
    >   **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**
  L55:
    > 
    > ```
    > SET APNREPORTATTR: APN="ims.real", PCRF=REQUESTED;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（15）：['AAAACCT', 'AAAAUTH', 'APN', 'CG', 'CHF', 'CONGESTIONRPT', 'DIAMETERAAA', 'INTELLIGENTSEL', 'LOCATIONREPORT', 'MAPTRANSDATA', 'OCS', 'PCF', 'PCRF', 'PERFORMANCE', 'UPF']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 4, '全网规划': 2}（多值→atom 应考虑 decision_driven）
