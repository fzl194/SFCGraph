# 命令证据包：ADD QOSPROP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令主要用于配置PCC预定义规则的QoS参数，可以通过ADD PCCPOLICYGRP的QOSPROPNAME参数将QoS参数关联到PCC Rule，PCC动态规则只能是L3/4层，所以PCC动态规则的QoS-information只能作用于L3/4层规则。

该命令可以配置PCC预定义规则的L3/4层规则的QoS，也可以配置PCC预定义规则的L7层规则的
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为500。
- 一个ADD PCCPOLICYGRP可以绑定一个QOSPROP，一个ADD L2RULE可以绑定一个QOSPROP。
- 预定义规则中配置的ADD QOSPROP与PCC动态规则的QoS-information作用相同，只有数据流匹配到预定义规则，才会执行预定义规则中的ADD QOSPROP。
- 如果同时配置了BWM Rule和绑定

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| QOSPROPNAME | QoS属性名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| QCIVALUE | QoS等级标识 | local_planned | conditional | 无 | 整数类型，取值范围为1～255。 |
| ARPVALUE | 分配保留优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～15。 |
| EMPCAP | QoS抢占能力 | local_planned | optional | DISABLE | 枚举类型。 |
| EMPVUL | QoS被抢占设置 | local_planned | optional | ENABLE | 枚举类型。 |
| GBRUPLKVALUE | 保证的上行比特率 | local_planned | optional | 无 | 整数类型，取值范围为0～20000000，单位是千比特每秒。 |
| GBRDNLKVALUE | 保证的下行比特率 | local_planned | optional | 无 | 整数类型，取值范围为0～20000000，单位是千比特每秒。 |
| MBRUPLKVALUE | 最大上行比特率 | local_planned | optional | 无 | 整数类型，取值范围为0～20000000，单位是千比特每秒。 |
| MBRDNLKVALUE | 最大下行比特率 | local_planned | optional | 无 | 整数类型，取值范围为0～20000000，单位是千比特每秒。 |
| QOSTYPE | QoS属性类型 | local_planned | required | 无 | 枚举类型。 |
| FQI | 5G QoS标识 | local_planned | conditional | 无 | 整数类型，取值范围为1～255。 |
| RQI | 反射QoS指示 | local_planned | conditional | 无 | 枚举类型。 |
| QOSURRNAME | QoS使用量上报规则名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD QOSPROP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性名称（QOSPROPNAME） | qos_property1 | 本端规划 | 配置QoS类型的PCC策略。 |
  | [**ADD QOSPROP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性类型（QOSTYPE） | QOS_BEARER_PARA | 本端规划 | 配置QoS类型的PCC策略。 |
- 任务示例脚本（该命令行）：
  `ADD QOSPROP:QOSPROPNAME="qos_property1", QOSTYPE=QOS_BEARER_PARA;`
- 操作步骤上下文（±2 行原文）：
  L86:
    > 5. 配置PCC用户使用的业务规则。
    >     a. 配置QoS属性。
    >       [**ADD QOSPROP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    >     b. 配置PCC策略。
    >       [**ADD PCCPOLICYGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
  L142:
    > 4. 配置PCC业务规则。如配置的rule仅下发给辅锚点PGW-U，则需要将“RULERANGE”设置为“LOCAL”；仅下发给主锚点PGW-U则设置为“CENTRAL”。
    >   ```
    >   ADD QOSPROP:QOSPROPNAME="qos_property1", QOSTYPE=QOS_BEARER_PARA;
    >   ```
    >   ```

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QOSPROPNAME（QoS属性名称） | qosprop_501 | 本端规划 | 存在多条记录时，不能重复。<br>以5G用户使用的QoSProp名称为qosprop_501；2/3/4G用户使用的名称为qosprop_401为例。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | EMPCAP（QoS抢占能力） | DISABLE | 本端规划 | 该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以不抢占为例。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | EMPVUL（QoS被抢占设置） | ENABLE | 本端规划 | 其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以被抢占为例。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | GBRUPLKVALUE（保证的上行比特率） | 600 | 本端规划 | 此处数据仅为举例，请根据业务模型进行规划。<br>创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | GBRDNLKVALUE（保证的下行比特率） | 6000 | 本端规划 | 此处数据仅为举例，请根据业务模型进行规划。<br>创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | MBRUPLKVALUE（最大上行比特率） | 1000 | 本端规划 | 此处数据仅为举例，请根据业务模型进行规划。<br>创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | MBRDNLKVALUE（最大下行比特率） | 10000 | 本端规划 | 此处数据仅为举例，请根据业务模型进行规划。<br>创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QOSTYPE（QoS属性类型） | QOS_FLOW_PARA | 本端规划 | 5G用户使用QOS_FLOW_PARA，2/3/4G用户使用QOS_BEARER_PARA。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QCIVALUE（QoS等级标识） | 66 | 全网规划 | “QOSTYPE”<br>为<br>“QOS_BEARER_PARA”<br>时需要规划。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | ARPVALUE（分配保留优先级） | 5 | 本端规划 | 值越小优先级越高。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | FQI（5G QoS标识） | 2 | 本端规划 | “QOSTYPE”<br>为<br>“QOS_FLOW_PARA”<br>时需要规划。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QOSURRNAME（QoS使用量上报规则名称） | URR_qos_01 | 已配置数据中获取 | 使用<br>[**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)<br>定义的URRNAME。 |
- 任务示例脚本（该命令行）：
  `ADD QOSPROP: QOSPROPNAME="qosprop_501", GBRUPLKVALUE=600, GBRDNLKVALUE=6000, MBRUPLKVALUE=1000, MBRDNLKVALUE=10000, QOSTYPE=QOS_FLOW_PARA, ARPVALUE=5, FQI=2, QOSURRNAME="URR_qos_01";`
  `ADD QOSPROP: QOSPROPNAME="qosprop_401", GBRUPLKVALUE=600, GBRDNLKVALUE=6000, MBRUPLKVALUE=1000, MBRDNLKVALUE=10000, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=66, ARPVALUE=5, QOSURRNAME="URR_qos_01";`
- 操作步骤上下文（±2 行原文）：
  L74:
    >   [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > 3. 配置QoS属性。
    >   [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > 4. 规则通过PCC策略组绑定QoS属性时，配置PCC策略组。规则直接绑定QoS属性时，请跳过本步骤。
    >   [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
  L80:
    >   [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     - 规则通过PCC策略组绑定QoS属性时，“POLICYTYPE”设置为“PCC”，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)命令配置的“PCCPOLICYGRPNM”参数值。
    >     - 规则直接绑定QoS属性时，“POLICYTYPE”设置为“QOS”“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)命令配置的“QOSPROPNAME”参数值。
    >     - PCC类型的“RULENAME”值与QOS类型的“RULENAME”值不能相同。
    > 6. 配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。
  L127:
    > 
    > ```
    > ADD QOSPROP: QOSPROPNAME="qosprop_501", GBRUPLKVALUE=600, GBRDNLKVALUE=6000, MBRUPLKVALUE=1000, MBRDNLKVALUE=10000, QOSTYPE=QOS_FLOW_PARA, ARPVALUE=5, FQI=2, QOSURRNAME="URR_qos_01";
    > ```
    > 

### WSFD-102602

**md：`WSFD-102602/WSFD-102602 LTE一键通参考信息（适用于PGW-C_SGW-C）_10282627.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)
    > - [**SET QOSGLOBAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md)
    > - [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > - [**SET APNQOSATTR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
    > 

**md：`WSFD-102602/激活LTE一键通（适用于PGW-C_SGW-C）_10282625.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QOSPROPNAME（QoS属性名称） | qos3 | 本端规划 | 配置PCC预定义规则的QoS参数。 |
  | [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QCIVALUE（QoS等级标识） | 65<br>66<br>69<br>70 | 本端规划 | 配置PCC预定义规则的QoS参数。 |
  | [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QOSTYPE（QoS属性类型） | QOS_BEARER_PARA | 本端规划 | 配置PCC预定义规则的QoS参数。 |
  | [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | EMPCAP（QoS抢占能力） | ENABLE | 本端规划 | 配置PCC预定义规则的QoS参数。 |
- 操作步骤上下文（±2 行原文）：
  L124:
    >       [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)
    >     i. （可选）配置PCC预定义规则的QoS参数。
    >       [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > 4. 基于APN的一键通业务配置：
    >     a. 查询PTT业务QCI是否已经配置为标准QCI。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > **[LST URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/查询URR组（LST URRGROUP）_09897196.md)**
    > 
    > [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > 
    > **[RMV QOSPROP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/删除QoS属性（RMV QOSPROP）_09897165.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性名称（QOSPROPNAME） | qosprop_voice | 本端规划 | 配置静态PCC策略的QoS参数。存在多条记录时，QoS属性名称不能重复。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS抢占能力（EMPCAP） | ENABLE | 本端规划 | 该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以抢占为例。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS被抢占设置（EMPVUL） | DISABLE | 本端规划 | 其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以不被抢占为例。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 保证的上行比特率（GBRUPLKVALUE） | 64 | 固定取值 | PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 保证的下行比特率（GBRDNLKVALUE） | 64 | 固定取值 | PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 最大上行比特率（MBRUPLKVALUE） | 64 | 固定取值 | PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 最大下行比特率（MBRDNLKVALUE） | 64 | 固定取值 | PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性类型（QOSTYPE） | QOS_BEARER_PARA | 本端规划 | 5G用户使用QOS_FLOW_PARA，2/3/4G用户使用QOS_BEARER_PARA。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS等级标识（QCIVALUE） | 1 | 本端规划 | “QOSTYPE”<br>为<br>“QOS_BEARER_PARA”<br>时需要规划。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS使用量上报规则名称（QOSURRNAME） | urr_qos_01 | 已配置数据中获取 | 使用<br>[**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)<br>定义的URRNAME。 |
- 任务示例脚本（该命令行）：
  `ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=1, QOSURRNAME="urr_qos_01";`
  `ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=1, QOSURRNAME="urr_qos_01";`
- 操作步骤上下文（±2 行原文）：
  L227:
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    >     c. 配置静态PCC策略的QoS参数。
    >       [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    >     d. 配置PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
  L364:
    > 
    >       ```
    >       ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=1, QOSURRNAME="urr_qos_01";
    >       ```
    >       //配置PCC策略组。
  L478:
    > 
    >       ```
    >       ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=1, QOSURRNAME="urr_qos_01";
    >       ```
    >       //配置PCC策略组。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性名称（QOSPROPNAME） | qosprop_voice | 本端规划 | 配置静态PCC策略的QoS参数。存在多条记录时，QoS属性名称不能重复。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS抢占能力（EMPCAP） | ENABLE | 本端规划 | 该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以抢占为例。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS被抢占设置（EMPVUL） | DISABLE | 本端规划 | 其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以不被抢占为例。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 保证的上行比特率（GBRUPLKVALUE） | 64 | 固定取值 | PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCF Bypass期间，创建专有QoSFlow/专有承载时，使用SMF/PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 保证的下行比特率（GBRDNLKVALUE） | 64 | 固定取值 | PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCF Bypass期间，创建专有QoSFlow/专有承载时，使用SMF/PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 最大上行比特率（MBRUPLKVALUE） | 64 | 固定取值 | PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCF Bypass期间，创建专有QoSFlow/专有承载时，使用SMF/PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 最大下行比特率（MBRDNLKVALUE） | 64 | 固定取值 | PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCF Bypass期间，创建专有QoSFlow/专有承载时，使用SMF/PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性类型（QOSTYPE） | QOS_FLOW_PARA | 本端规划 | 5G用户使用QOS_FLOW_PARA，2/3/4G用户使用QOS_BEARER_PARA。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 分配保留优先级（ARPVALUE） | 2 | 本端规划 | 值越小优先级越高。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 5G QoS标识（FQI） | 1 | 本端规划 | “QOSTYPE”<br>为<br>“QOS_FLOW_PARA”<br>时需要规划。 |
  | [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS使用量上报规则名称（QOSURRNAME） | urr_qos_01 | 已配置数据中获取 | 使用<br>[**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)<br>定义的URRNAME。 |
- 任务示例脚本（该命令行）：
  `ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_FLOW_PARA, FQI=1, ARPVALUE=2, QOSURRNAME="urr_qos_01";`
  `ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_FLOW_PARA, FQI=1, ARPVALUE=2, QOSURRNAME="urr_qos_01";`
- 操作步骤上下文（±2 行原文）：
  L246:
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    >     c. 配置静态PCC策略的QoS参数。
    >       [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    >     d. 配置PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
  L392:
    > 
    >       ```
    >       ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_FLOW_PARA, FQI=1, ARPVALUE=2, QOSURRNAME="urr_qos_01";
    >       ```
    >       //配置PCC策略组。
  L644:
    > 
    >       ```
    >       ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_FLOW_PARA, FQI=1, ARPVALUE=2, QOSURRNAME="urr_qos_01";
    >       ```
    >       //配置PCC策略组。

## ④ 自动比对
- 命令真相参数（13）：['ARPVALUE', 'EMPCAP', 'EMPVUL', 'FQI', 'GBRDNLKVALUE', 'GBRUPLKVALUE', 'MBRDNLKVALUE', 'MBRUPLKVALUE', 'QCIVALUE', 'QOSPROPNAME', 'QOSTYPE', 'QOSURRNAME', 'RQI']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 27, '全网规划': 1, '已配置数据中获取': 3, '固定取值': 8}（多值→atom 应考虑 decision_driven）
