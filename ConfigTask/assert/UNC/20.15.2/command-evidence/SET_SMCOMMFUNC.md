# 命令证据包：SET SMCOMMFUNC
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF、GGSN**

此命令用于设置通用会话管理扩展功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- GAGYCHGSW参数配置成不使能会导致GaGy计费功能不可用，请谨慎修改参数取值。
- PCRFQRYSW参数配置仅在RESTFULQRYSW参数配置开启时生效，如需支持通过Restful查询非异网漫游或非国漫场景下PCRF的地址，需先开启RESTFULQRYSW参数，再开启PCRFQRYSW。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：


**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| LOCREPORT | 位置上报 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- NotSupport（不支持） |
| RTBEHINDMSSW | 手机后路由功能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- DISABLE（不使能） |
| MULTIDNNSW | 2B2C漫游双DNN特性开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- NotSupport（不支持） |
| UDMDEREGINSID | 携带实例ID向UDM发起去注册 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- DISABLE（不使能） |
| PGWRNSSWITCH | PGW重定向功能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- DISABLE（不使能） |
| QOSANASW | QoS质差分析开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- NotSupport（不支持） |
| GAGYCHGSW | GaGy计费功能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- “ENABLE（使能）”：使能 |
| RESTFULQRYSW | Restful接口查询PCF/PCRF地址开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- NotSupport（不支持） |
| QOSEXPSW | 体验感知信息采集订阅开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- NotSupport（不支持） |
| LOCATIONCHSW | 位置变更订阅开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- NotSupport（不支持） |
| EXPOSURELOCRPT | 能力开放位置上报 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- NotSupport（不支持） |
| PCRFQRYSW | 查询PCRF地址开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCO | <br>- NotSupport（不支持） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置QoS能力开放功能_48518810.md`**
- 数据规划表（该命令的参数行）：
  | **[SET SMCOMMFUNC](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md)** | 查询PCRF地址开关（PCRFQRYSW） | ENABLE | 全网规划 | QoS能力开放功能 |
- 任务示例脚本（该命令行）：
  `SET SMCOMMFUNC: PCRFQRYSW=ENABLE`
- 操作步骤上下文（±2 行原文）：
  L80:
    >   **[SET HTTPCONF](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**
    > 9. 开启QoS能力开放功能开关。
    >   **[SET SMCOMMFUNC](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md)**
    > 
    > ## [任务示例](#ZH-CN_OPI_0000002048518810)
  L152:
    > 7. 开启QoS能力开放功能。
    >   ```
    >   SET SMCOMMFUNC: PCRFQRYSW=ENABLE
    >   ```

### WSFD-205101

**md：`WSFD-205101/WSFD-205101 支持Routing Behind MS参考信息_76359000.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET APNADDRESSATT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.md)
    > - **[SET SMCOMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md)**
    > - **[ADD ROUTINGBEHINDMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/手机后路由/增加本地配置的手机后路由信息（ADD ROUTINGBEHINDMS）_59000287.md)**
    > 

**md：`WSFD-205101/激活支持Routing Behind MS_76358998.md`**
- 数据规划表（该命令的参数行）：
  | **[SET SMCOMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md)** | 手机后路由功能开关（RTBEHINDMSSW） | ENABLE | 本端规划 | 支持从本地配置中获取后路由。 |
- 任务示例脚本（该命令行）：
  `SET SMCOMMFUNC: RTBEHINDMSSW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L47:
    >   > - 在功能开启前，需要在AAA Server上配置好分配给终端设备使用的IP地址段。
    > 4. 支持从本地配置中获取后路由。
    >   **[SET SMCOMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md)**
    > 5. 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。
    >   **[ADD ROUTINGBEHINDMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/手机后路由/增加本地配置的手机后路由信息（ADD ROUTINGBEHINDMS）_59000287.md)**
  L74:
    > 
    > ```
    > SET SMCOMMFUNC: RTBEHINDMSSW=ENABLE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（12）：['EXPOSURELOCRPT', 'GAGYCHGSW', 'LOCATIONCHSW', 'LOCREPORT', 'MULTIDNNSW', 'PCRFQRYSW', 'PGWRNSSWITCH', 'QOSANASW', 'QOSEXPSW', 'RESTFULQRYSW', 'RTBEHINDMSSW', 'UDMDEREGINSID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 1, '本端规划': 1}（多值→atom 应考虑 decision_driven）
