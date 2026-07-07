# 命令证据包：ADD APNUSRPROFG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md`
> 用该命令的特性数：17

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

本命令用于将USRPROFGROUP绑定到APN下。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为10000。
- 每个APN只能绑定一个USRPROFGROUP。
- 要配置此命令，需要首先配置ADD APN和ADD USRPROFGROUP。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| USERPROFGNAME | 用户模板组名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-108002

**md：`WSFD-108002/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L23:
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > #### [告警](#ZH-CN_CONCEPT_0228860592)

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN） | Huawei.com | 全网规划 | 配置基于DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | 用户模板组名称（USERPROFGNAME） | ulcl_test | 本端规划 | 配置基于DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="Huawei.com",USERPROFGNAME="ulcl_test";`
- 操作步骤上下文（±2 行原文）：
  L93:
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     d. 将用户模板组绑定至指定APN。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 4. 配置IPv6会话场景下的分流策略。
    >   [**SET SMFFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)
  L134:
    > ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";
    > ADD UPBINDUPG:USERPROFGNAME="ulcl_test",UPBINDTYPE=ULCL,USERPROFILENAME="testuserprofilename";
    > ADD APNUSRPROFG:APN="Huawei.com",USERPROFGNAME="ulcl_test";
    > //配置IPv6会话场景下的分流策略。
    > SET SMFFUNC: IPV6LOCALUP=UlClPrefer;

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET SMFFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)
    > 

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN） | dnn-ar | 全网规划 | 配置基于专网业务DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
  | [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | 用户模板组名称（USERPROFGNAME） | ulcl_test | 本端规划 | 配置基于专网业务DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="dnn-ar",USERPROFGNAME="ulcl_test";`
- 操作步骤上下文（±2 行原文）：
  L69:
    >       [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     d. 将用户模板组绑定至专网DNN。
    >       [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 4. 配置IPv6会话场景下的分流策略。
    >   [**SET SMFFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)
  L108:
    > ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";
    > ADD UPBINDUPG:USERPROFGNAME="ulcl_test",UPBINDTYPE=ULCL,USERPROFILENAME="testuserprofilename";
    > ADD APNUSRPROFG:APN="dnn-ar",USERPROFGNAME="ulcl_test";
    > //配置IPv6会话场景下的分流策略。
    > SET SMFFUNC: IPV6LOCALUP=UlClPrefer;

### WSFD-223101

**md：`WSFD-223101/WSFD-223101 基于预定义规则的分流策略控制(4G)参考信息_11634944.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L23:
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0000001211634944)

### WSFD-109202

**md：`WSFD-109202/WSFD-109202 会话类QOS保证参考信息_28258189.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET QOSCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS控制功能/设置QoS控制配置（SET QOSCTRL）_09653269.md)
    > 

**md：`WSFD-109202/激活会话类QOS保证（适用于GGSN）_28258187.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN名称） | apn1 | 全网规划 | 将UserProfile Group绑定到APN。 |
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | USERPROFGNAME（用户模板组名称） | usrg | 全网规划 | 将UserProfile Group绑定到APN。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="usrg";`
- 操作步骤上下文（±2 行原文）：
  L98:
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 将UserProfile Group绑定到APN。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    >     - 为APN实例绑定QoS profile。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
  L177:
    >   //将UserProfile Group绑定到APN。
    >   ```
    >   ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="usrg";
    >   ```
    >   //为该APN实例绑定QosProfile。

**md：`WSFD-109202/激活会话类QOS保证（适用于SGW-C_PGW-C）_28344569.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN (APN名称) | apn1 | 全网规划 | 将UserProfile Group绑定到APN |
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | USERPROFGNAME（用户模板组名称） | usrg | 全网规划 | 将UserProfile Group绑定到APN |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="usrg";`
- 操作步骤上下文（±2 行原文）：
  L119:
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     - 将UserProfile Group绑定到APN。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    >     - 为APN实例绑定QoS profile。
    >       [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
  L214:
    >   //将UserProfile Group绑定到APN。
    >   ```
    >   ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="usrg";
    >   ```
    >   //为该APN实例绑定QosProfile。

### WSFD-109203

**md：`WSFD-109203/WSFD-109203 本地QOS控制参考信息_28258574.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
    > - [**SET QOSCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS控制功能/设置QoS控制配置（SET QOSCTRL）_09653269.md)

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L29:
    > - [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD PCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN） | apn1 | 全网规划 | 将UserProfile Group绑定到APN。 |
  | [**ADD APNUSRPROFG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 全网规划 | 将UserProfile Group绑定到APN。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L113:
    >       > - [**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令配置后，common policy仍使用[**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)中配置的匹配条件的UserProfile中的策略。
    >     g. 将UserProfile Group绑定到APN。
    >       [**ADD APNUSRPROFG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    >       > **说明**
    >       > 业务策略组合和APN建立绑定关系后，对该APN已经存在的用户无效，只对后续新激活的用户生效。
  L164:
    >   ```
    >   ```
    >   ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="upg_test";
    >   ```

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD GUAMI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/AMF/AMF全局标识符管理/增加AMF全局标识（ADD GUAMI）_09653726.md)
    > - [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN） | huawei.com | 全网规划 | 将UserProfile Group绑定到DNN。 |
  | [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 全网规划 | 将UserProfile Group绑定到DNN。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L189:
    >             [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >           c. 将UserProfile Group绑定到DNN。
    >             [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - 配置GGSN-C/PGW-C/SMF与PCF之间的接口模式。
    >   5G终端在5G接入是使用Npcf接口，用户在3G接入时使用Gx接口。其他指定终端和接入类型时，例如对于2G/4G用户，按照如下描述选择策略接口（优先级顺序：基于PCF实例标识的策略接口类型>基于APN的策略接口类型>全局的策略接口类型）：
  L263:
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";
    > ```
    > 

### WSFD-109102

**md：`WSFD-109102/WSFD-109102 ADC基本功能参考信息_92582138.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0292582138)

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    > - [**SET DFTIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认空闲上下文定时器配置（SET DFTIDLETIME）_09654414.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN） | huawei.com | 全网规划 | 将UserProfile Group绑定到DNN。 |
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 全网规划 | 将UserProfile Group绑定到DNN。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L93:
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     c. 将UserProfile Group绑定到DNN。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 8. **可选：**系统初始值不符合要求时，修改指定APN级别的专有QoS Flow级别的空闲定时器时长。
    >   [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
  L161:
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";
    > ```
    > 

### WSFD-211001

**md：`WSFD-211001/WSFD-211001 基于初始接入位置的策略控制参考信息_27915140.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**MOD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/修改用户模板组和用户模板的绑定关系（MOD UPBINDUPG）_09897230.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0227915140)

**md：`WSFD-211001/激活基于初始接入位置的策略控制_27915138.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN） | apn-test | 已配置数据中获取 | 使用<br>[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令中定义的APN名称。 |
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | 用户模板组名称（USERPROFGNAME） | upg_test1 | 已配置数据中获取 | 使用<br>[**MOD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/修改用户模板组和用户模板的绑定关系（MOD UPBINDUPG）_09897230.md)<br>命令中绑定的用户模板组名称。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg_test1";`
- 操作步骤上下文（±2 行原文）：
  L66:
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > 6. 将用户模板组和APN/DNN绑定。
    >   [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0227915138)
  L111:
    > 
    > ```
    > ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg_test1";
    > ```

### WSFD-211005

**md：`WSFD-211005/WSFD-211005 基于业务感知的带宽控制参考信息_79619228.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0279619228)

**md：`WSFD-211005/激活基于业务感知的带宽控制_79619226.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN） | huawei.com | 全网规划 | 将UserProfile Group绑定到DNN。 |
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 全网规划 | 将UserProfile Group绑定到DNN。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L59:
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     c. UserProfile Group绑定到DNN。如已配置，请跳过本步骤。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0279619226)
  L82:
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";
    > ```

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L49:
    > - **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - **[TST AAA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS维护/服务器检测/测试AAA服务器（TST AAA）_09896762.md)**
    > - **[**DSP ROUTE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由基础/IPv4路由表/显示IPv4路由表（DSP ROUTE）_00441129.md)**

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN名称（APN） | apn-test | 已配置数据中获取 | 将User Profile Group绑定到指定APN下。<br>已通过<br>[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>配置，可以使用<br>**[**LST APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>命令进行查询。 |
  | [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 已配置数据中获取 | 已经通过<br>**[ADD USRPROFGROUP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**<br>命令配置完成，可以使用<br>**[LST USRPROFGROUP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/查询用户模板组（LST USRPROFGROUP）_09897222.md)**<br>查询。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L70:
    >       [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     e. 将UsrProfGroup绑定到指定APN。
    >       [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    >       > **说明**
    >       > 业务策略组合和APN建立绑定关系后，对该APN已经存在的用户无效，只对后续激活的用户生效。
  L106:
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="up_test";
    > ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";
    > ```

### WSFD-011201

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 操作步骤上下文（±2 行原文）：
  L99:
    >       **ADD UPBINDUPG**
    >     e. 将UserProfileGroup绑定到APN实例下。
    >       **ADD APNUSRPROFG**
    > 3. 配置OFCTemplate模板绑定APN对象。
    >     a. 配置APN。如已配置APN，请跳过该步骤。

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APNUSRPROFG** | APN名称（APN） | apn-test | 已配置数据中获取 | 将UserProfile组绑定到APN上。 |
  | **ADD APNUSRPROFG** | 用户模板组名称（USERPROFGNAME） | upg-tes | 已配置数据中获取 | 将UserProfile组绑定到APN上。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";`
  `ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L82:
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >   > **说明**
    >   > 没有绑定rule的UserProfile下的用户数据包不会创建五元组，不会占用五元组资源，并且这种方式能够使不同APN的不同UserProfile下的用户使用不同的费率标识进行用户级的离线计费。而方式一全局粒度配置时GGSN/SGW-C/PGW-C中的用户使用相同的费率标识进行用户级的离线计费。
  L111:
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    > 
    > ## [任务示例](#ZH-CN_OPI_0298555879)
  L144:
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    >   ADD APN:APN="apn-test";
    >   ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
    >   ```
    > 3. 任务三：配置内容计费的费率标识，具体内容为：上下行均使用离线计费，费率标识（RG，SID）=（10,20）。

### WSFD-011206

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APNUSRPROFG** | APN（APN） | apn-test | 全网规划 | 将UserProfile绑定到DNN实例。<br>基于UserProfile粒度需要规划。 |
  | **ADD APNUSRPROFG** | 用户模板组名称（USERPROFGNAME） | upg_test | 已配置数据中获取 | 将UserProfile绑定到DNN实例。<br>基于UserProfile粒度需要规划。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L100:
    >           b. 配置DNN实例，将UserProifle组绑定到DNN实例。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >             每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行 **ADD UPBINDUPG** 命令，将UserProfile绑定到UserProfile组即可。
    > 
  L155:
    > ```
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";
    > ```

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APNUSRPROFG** | APN（APN） | apn-test | 已配置数据中获取 | 使用<br>**ADD APN**<br>命令定义的<br>“APN”<br>。 |
  | **ADD APNUSRPROFG** | 用户模板组名称（USERPROFGNAME） | upg_test | 已配置数据中获取 | 使用<br>**ADD USRPROFGROUP**<br>命令定义的<br>“USERPROFGNAME”<br>。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L110:
    >           b. 配置DNN实例，将UserProifle组绑定到DNN实例。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >             每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行 **ADD UPBINDUPG** 命令，将UserProfile绑定到UserProfile组即可。
    >     5. **可选：** 配置在线RG配额耗尽后的默认动作。
  L211:
    > ```
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";
    > ```

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

**md：`WSFD-109001/配置在线计费模板_95923574.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APNUSRPROFG** | APN（APN） | apn-test | 已配置数据中获取 | UsrProfGroup绑定到APN。 |
  | **ADD APNUSRPROFG** | 用户模板组名称（USERPROFGNAME） | upg-test | 已配置数据中获取 | UsrProfGroup绑定到APN。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L93:
    >       **ADD UPBINDUPG**
    >     e. 将UserProfileGroup绑定到APN实例下。
    >       **ADD APNUSRPROFG**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923574)
  L162:
    > 
    > ```
    > ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
    > ```

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APNUSRPROFG** | APN名称（APN） | apn-test | 已配置数据中获取 | 将UserProfile组绑定到APN上。 |
  | **ADD APNUSRPROFG** | 用户模板组名称（USERPROFGNAME） | upg-tes | 已配置数据中获取 | 将UserProfile组绑定到APN上。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";`
  `ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L86:
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >   > **说明**
    >   > 没有绑定rule的UserProfile下的用户数据包不会创建五元组，不会占用五元组资源，并且这种方式能够使不同APN的不同UserProfile下的用户使用不同的费率标识进行用户级的在线计费。而方式一全局粒度配置时GGSN/PGW-C中的用户使用相同的费率标识进行用户级的在线计费。
  L115:
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923388)
  L148:
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    >   ADD APN:APN="apn-test";
    >   ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
    >   ```
    > 3. 任务三：配置内容计费的费率标识，具体内容为：上下行均使用在线计费，费率标识（RG，SID）=（10,20）。

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L158:
    > 
    > ```
    > ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
    > ```

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0274112323)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN（APN名称） | apn-test | 全网规划 | 将UserProfile组绑定到DNN上。 |
  | [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | USERPROFGNAME（用户模板组名称） | upg-test | 全网规划 | 将UserProfile组绑定到DNN上。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L100:
    >     b. 配置DNN，将UserProfile组绑定到指定DNN实例上。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0274112321)
  L162:
    > ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    > ADD APN:APN="apn-test";
    > ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
    > ```
    > 

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L122:
    > **[LST USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/查询用户模板组（LST USRPROFGROUP）_09897222.md)**
    > 
    > [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 
    > **[MOD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/修改APN用户模板组绑定关系（MOD APNUSRPROFG）_09897225.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | APN（APN） | ims | 全网规划 | （可选）为APN绑定用户模板组。 |
  | **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）为APN绑定用户模板组。 |
  | **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | APN（APN） | ims | 全网规划 | （可选）为APN绑定用户模板组。 |
  | **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）为APN绑定用户模板组。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="ims", USERPROFGNAME="upg_ims";`
- 操作步骤上下文（±2 行原文）：
  L218:
    >       > **说明**
    >       > 如果APN ims已绑定了用户模板组，则跳过本步骤。
    >       **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)**
    > 2.
    >   配置语音缺省承载静态PCC策略。
  L249:
    >       > **说明**
    >       > 如果APN ims已绑定了用户模板组，则跳过本步骤。
    >       **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)**
    > 3.
    >   配置PCRF Bypass条件。
  L346:
    > 
    >       ```
    >       ADD APNUSRPROFG:APN="ims", USERPROFGNAME="upg_ims";
    >       ```
    >     2. 配置语音专有承载静态PCC策略。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | APN（APN） | ims | 全网规划 | （可选）为APN绑定用户模板组。 |
  | **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）为APN绑定用户模板组。 |
  | **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | APN（APN） | ims | 全网规划 | （可选）为APN绑定用户模板组。 |
  | **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）为APN绑定用户模板组。 |
- 任务示例脚本（该命令行）：
  `ADD APNUSRPROFG:APN="ims", USERPROFGNAME="upg_ims";`
- 操作步骤上下文（±2 行原文）：
  L237:
    >       > **说明**
    >       > 如果APN ims已绑定了用户模板组，则跳过本步骤。
    >       **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)**
    > 2.
    >   配置语音专有QoS Flow/缺省承载静态PCC策略。
  L268:
    >       > **说明**
    >       > 如果APN ims已绑定了用户模板组，则跳过本步骤。
    >       **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)**
    > 3.
    >   配置PCF Bypass条件。
  L374:
    > 
    >       ```
    >       ADD APNUSRPROFG:APN="ims", USERPROFGNAME="upg_ims";
    >       ```
    >     2. 配置语音专有QoS Flow/专有承载静态PCC策略。

## ④ 自动比对
- 命令真相参数（2）：['APN', 'USERPROFGNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 25, '本端规划': 2, '已配置数据中获取': 13}（多值→atom 应考虑 decision_driven）
