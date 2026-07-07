# 命令证据包：SET N40APIVER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/N40 API版本/设置N40接口协议版本和需要使用的FeatureList（SET N40APIVER）_31773565.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：![](设置N40接口协议版本和需要使用的FeatureList（SET N40APIVER）_31773565.assets/notice_3.0-zh-cn_2.png)

此操作会修改N40接口的功能和信元携带能力，如果CHF不支持对应的功能或信元，将无法正常处理SMF发送的消息。

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置N40接口协议版本、需要使用的Feature
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| APIVER | FEATURE |
| --- | --- |
| F30 | NODEFUNC-1 |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APIVER | API接口版本 | global_planned | required | 无。 | <br>- “F30（F30）”：遵循3GPP TS 32291 F30定义的Nchf_Conver |
| FEATURE | 特性 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40A | <br>- “NODEFUNC（NODEFUNC）”：N40接口Serving/Local Node |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET N40APIVER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/N40 API版本/设置N40接口协议版本和需要使用的FeatureList（SET N40APIVER）_31773565.md)
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)

**md：`WSFD-011206/配置N40接口的API版本和增强的功能集_31702747.md`**
- 数据规划表（该命令的参数行）：
  | ****SET N40APIVER**** | API接口版本（APIVER） | F30 | 全网规划 | 配置N40接口支持的API版本，需和CHF使用相同的协议版本。 |
  | ****SET N40APIVER**** | 特性（FEATURE） | NBIOTCHG-1&LTEMCHG-1 | 全网规划 | 配置N40接口增强的功能，需和CHF使用相同的接口能力。<br>该参数类型为位域类型，支持取值叠加进行选择，功能使能时参数后携带-1，不使能时参数后携带-0，如果不修改对应功能，无需携带对应参数，详细可参考任务示例。 |
- 任务示例脚本（该命令行）：
  `SET N40APIVER: APIVER=F30, FEATURE=NODEFUNC-1;`
  `SET N40APIVER: APIVER=F30, FEATURE=NBIOTCHG-1&LTEMCHG-1;`
  `SET N40APIVER: APIVER=F30, FEATURE=UTRANCHG3GPP-1;`
  `SET N40APIVER: APIVER=F30, FEATURE=TRIGGER23G-1;`
  `SET N40APIVER: APIVER=F30, FEATURE=GERANCHG-1;`
  `SET N40APIVER: APIVER=F30, FEATURE=WLANCHG-1;`
  `SET N40APIVER: APIVER=F30, FEATURE=NODEFUNC-1&GERANCHG-1&WLANCHG-1;`
- 操作步骤上下文（±2 行原文）：
  L37:
    > - 进入 “MML命令行-UNC” 窗口。
    > - 配置N40接口支持的API版本及增强功能集。
    >   **SET N40APIVER**
    > - 配置N40消息属性模板，控制N40消息中是否携带对应字段。
    >   **ADD N40MSGTEMP**
  L58:
    > 
    > ```
    > SET N40APIVER: APIVER=F30, FEATURE=NODEFUNC-1;
    > ```
    > 
  L64:
    > 
    > ```
    > SET N40APIVER: APIVER=F30, FEATURE=NBIOTCHG-1&LTEMCHG-1;
    > ADD N40MSGTEMP: TEMPLATENAME="n40attr", NBEXTENDATTR=ENABLE;
    > ```

## ④ 自动比对
- 命令真相参数（2）：['APIVER', 'FEATURE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 2}（多值→atom 应考虑 decision_driven）
