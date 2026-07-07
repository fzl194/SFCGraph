# 命令证据包：ADD N40MSGTEMP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/N40消息属性模板/增加N40消息属性模板（ADD N40MSGTEMP）_48957459.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加N40消息属性模板，用于控制N40消息中是否携带对应字段。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入101条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TEMPLATENAME | SECRATUSAGE | NBEXTENDATTR | QFIDOWNLINK | HOMECHGID | HWQBCIDCT | APPSVCPROVID | RCP |
| --- | --- | --- | --- | --- |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TEMPLATENAME | N40消息属性模板名 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| SECRATUSAGE | RANSecondaryRATUsageReport | local_planned | optional | ENABLE | <br>- ENABLE（携带该字段） |
| NBEXTENDATTR | NB扩展属性 | local_planned | optional | ENABLE | <br>- ENABLE（携带该字段） |
| QFIDOWNLINK | QFI容器中的DownLinkVolume | local_planned | optional | ENABLE | <br>- ENABLE（携带该字段） |
| HOMECHGID | HomeProvidedChargingID | local_planned | optional | ENABLE | <br>- ENABLE（携带该字段） |
| HWQBCIDCT | huaweiQBCIndication | global_planned | optional | DISABLE | <br>- DISABLE（不携带该字段） |
| APPSVCPROVID | applicationserviceProviderIdentity | global_planned | optional | DISABLE | <br>- ENABLE（携带该字段） |
| RCP | 是否支持携带roamingChargingProfile | local_planned | optional | ENABLE | <br>- ENABLE（携带该字段） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/配置N40接口的API版本和增强的功能集_31702747.md`**
- 数据规划表（该命令的参数行）：
  | ****ADD N40MSGTEMP**** | N40消息属性模板名（TEMPLATENAME） | n40attr | 本端规划 | 指定N40消息字段模板名。 |
  | ****ADD N40MSGTEMP**** | NB扩展属性（NBEXTENDATTR） | ENABLE | 本端规划 | 控制NB-IOT、LTEM接入时是否携带扩展属性信息，包括APN Rate Control、Serving PLMN Rate Control、CP only indication和PtP隧道。 |
- 任务示例脚本（该命令行）：
  `ADD N40MSGTEMP: TEMPLATENAME="n40attr", NBEXTENDATTR=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L39:
    >   **SET N40APIVER**
    > - 配置N40消息属性模板，控制N40消息中是否携带对应字段。
    >   **ADD N40MSGTEMP**
    > 
    > ## [任务示例](#ZH-CN_OPI_0231702747)
  L65:
    > ```
    > SET N40APIVER: APIVER=F30, FEATURE=NBIOTCHG-1&LTEMCHG-1;
    > ADD N40MSGTEMP: TEMPLATENAME="n40attr", NBEXTENDATTR=ENABLE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（8）：['APPSVCPROVID', 'HOMECHGID', 'HWQBCIDCT', 'NBEXTENDATTR', 'QFIDOWNLINK', 'RCP', 'SECRATUSAGE', 'TEMPLATENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 2}（多值→atom 应考虑 decision_driven）
