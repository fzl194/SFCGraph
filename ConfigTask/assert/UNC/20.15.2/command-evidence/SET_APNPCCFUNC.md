# 命令证据包：SET APNPCCFUNC
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md`
> 用该命令的特性数：6

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用于使能或关闭指定APN/DNN用户的动态PCC功能。

PCC即策略和计费控制，当运营商需要通过动态PCC功能对计费策略和计费的粒度进行灵活控制，从而优化运营商的计费手段，提高收益时，可以通过此命令使能指定APN用户的动态PCC功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：HOMEPCCSWITCH=INHERIT,RoamPCCSwitch=INHERIT,VisitPCCSwitch=INHERIT,PCCTEMPLATE=NULL,PCFSelectMode=NULL。
- 当HOMEPCCSWIT

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| HOMEPCCSWITCH | 本地用户动态PCC功能 | 对端协商 | optional | 无 | 枚举类型。 |
| ROAMPCCSWITCH | 漫游用户动态PCC功能 | 对端协商 | optional | 无 | 枚举类型。 |
| VISITPCCSWITCH | 拜访用户动态PCC功能 | 对端协商 | optional | 无 | 枚举类型。 |
| PCCTEMPLATE | PCC模板名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63，不区分大小写。字符串中不能出现空格。 |
| PCFSELECTMODE | 选择PCF方式 | global_planned | optional | 无 | 位域类型。 |
| DISCCUSTOM | PCF状态过滤参数 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | apn-op | 已配置数据中获取 | 基于APN配置PCC本端主机名选择模式。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | PCC模板名称（PCCTEMPLATE） | pcctemplate_01 | 已配置数据中获取 | 基于APN配置PCC本端主机名选择模式。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC: APN="apn-op", PCCTEMPLATE="pcctemplate_01";`
- 操作步骤上下文（±2 行原文）：
  L169:
    >             [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >           b. 将PCC模板与APN绑定。
    >             [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >     - 基于全局设置PCC本端主机名选择方式。
    >       [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
  L337:
    >   ```
    >   ADD PCCTEMPLATE: PCCTEMPNAME="pcctemplate_01", LOCSLCTMODE=UPFGRP, UPFGLOCGBNDGNAME="test";
    >   SET APNPCCFUNC: APN="apn-op", PCCTEMPLATE="pcctemplate_01";
    >   ```

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | apn-test1<br>apn-test2 | 已配置数据中获取 | APN绑定的PCC开关。<br>“apn-test1”下的PCC开关为“ENABLE”，“apn-test2”下的PCC开关为“INHERIT”。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 本地用户PCC功能（HOMEPCCSWITCH） | ENABLE<br>INHERIT | 本端规划 | APN绑定的PCC开关。<br>“apn-test1”下的PCC开关为“ENABLE”，“apn-test2”下的PCC开关为“INHERIT”。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 漫游用户PCC功能（ROAMPCCSWITCH） | ENABLE<br>INHERIT | 本端规划 | APN绑定的PCC开关。<br>“apn-test1”下的PCC开关为“ENABLE”，“apn-test2”下的PCC开关为“INHERIT”。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 拜访用户PCC功能（VISITPCCSWITCH） | ENABLE<br>INHERIT | 本端规划 | APN绑定的PCC开关。<br>“apn-test1”下的PCC开关为“ENABLE”，“apn-test2”下的PCC开关为“INHERIT”。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="apn-test1",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;`
  `SET APNPCCFUNC:APN="apn-test2",HOMEPCCSWITCH=INHERIT,ROAMPCCSWITCH=INHERIT,VISITPCCSWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L127:
    >       [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >     c. 针对指定的APN配置PCC使能开关，并将PccTemplate绑定到APN下。
    >       [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > 8. **可选：**配置specific APN。
    >   [**ADD SPECIFICAPNVAL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md)
  L224:
    >   ```
    >   ```
    >   SET APNPCCFUNC:APN="apn-test1",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
    >   ```
    >   ```
  L227:
    >   ```
    >   ```
    >   SET APNPCCFUNC:APN="apn-test2",HOMEPCCSWITCH=INHERIT,ROAMPCCSWITCH=INHERIT,VISITPCCSWITCH=INHERIT;
    >   ```

**md：`WSFD-109101/配置异常场景数据_31422947.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | apn-test | 已配置数据中获取 | APN下的故障处理动作。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 本地用户PCC功能（HOMEPCCSWITCH） | ENABLE | 本端规划 | APN下的故障处理动作。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 漫游用户PCC功能（ROAMPCCSWITCH） | ENABLE | 本端规划 | APN下的故障处理动作。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 拜访用户PCC功能（VISITPCCSWITCH） | ENABLE | 本端规划 | APN下的故障处理动作。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | PCC模板名称（PCCTEMPLATE） | templatetest | 本端规划 | APN下的故障处理动作。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="apn-test",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,PCCTEMPLATE="templatetest";`
- 操作步骤上下文（±2 行原文）：
  L80:
    >       [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >     5. 当基于APN粒度设置GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式，需要将PCCTEMPLATE绑定到APN下。
    >       [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - CCA消息中携带异常返回码。
    >     1. 进入 “MML命令行-UNC” 窗口。
  L120:
    >   ```
    >   ```
    >   SET APNPCCFUNC:APN="apn-test",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,PCCTEMPLATE="templatetest";
    >   ```
    > 2. 配置GGSN/PGW-C收到PCRF返回的异常码时的处理动作。

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | apn1 | 已配置数据中获取 | 针对指定的APN配置本地PCC使能开关，绑定PCC模板。<br>APN粒度（<br>[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)<br>）的优先级高于全局粒度（<br>[**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>）。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 本地用户PCC功能（HOMEPCCSWITCH） | DISABLE | 对端协商 | 针对指定的APN配置本地PCC使能开关，绑定PCC模板。<br>APN粒度（<br>[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)<br>）的优先级高于全局粒度（<br>[**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>）。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 漫游用户PCC功能（ROAMPCCSWITCH） | DISABLE | 对端协商 | 针对指定的APN配置本地PCC使能开关，绑定PCC模板。<br>APN粒度（<br>[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)<br>）的优先级高于全局粒度（<br>[**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>）。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 拜访用户PCC功能（VISITPCCSWITCH） | DISABLE | 对端协商 | 针对指定的APN配置本地PCC使能开关，绑定PCC模板。<br>APN粒度（<br>[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)<br>）的优先级高于全局粒度（<br>[**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>）。 |
  | [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | PCC模板名称（PCCTEMPLATE） | pcctemplate | 已配置数据中获取 | 针对指定的APN配置本地PCC使能开关，绑定PCC模板。<br>APN粒度（<br>[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)<br>）的优先级高于全局粒度（<br>[**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>）。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="apn1",HOMEPCCSWITCH=DISABLE,ROAMPCCSWITCH=DISABLE,VISITPCCSWITCH=DISABLE,PCCTEMPLATE="pcctemplate";`
- 操作步骤上下文（±2 行原文）：
  L83:
    >       [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >     b. 针对指定的APN配置PCC使能开关和PCC模板。
    >       [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > 5. 配置PCC用户使用的业务规则。
    >     a. 配置QoS属性。
  L138:
    >   ```
    >   ```
    >   SET APNPCCFUNC:APN="apn1",HOMEPCCSWITCH=DISABLE,ROAMPCCSWITCH=DISABLE,VISITPCCSWITCH=DISABLE,PCCTEMPLATE="pcctemplate";
    >   ```
    > 4. 配置PCC业务规则。如配置的rule仅下发给辅锚点PGW-U，则需要将“RULERANGE”设置为“LOCAL”；仅下发给主锚点PGW-U则设置为“CENTRAL”。

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | - huawei.com<br>- apn-test1<br>- apn-test2<br>- apn-another | 全网规划 | 针对指定的DNN配置PCC使能开关，绑定PCC模板。<br>- ENABLE：开启APN级别的动态PCC功能。<br>- DISABLE：开启APN级别的本地PCC功能，不从PCRF/PCF获取策略。<br>- INHERIT：采用[**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)命令的设置值。 |
  | [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 本地用户动态PCC功能（HOMEPCCSWITCH） | - ENABLE<br>- ENABLE<br>- INHERIT<br>- DISABLE | 对端协商 | 针对指定的DNN配置PCC使能开关，绑定PCC模板。<br>- ENABLE：开启APN级别的动态PCC功能。<br>- DISABLE：开启APN级别的本地PCC功能，不从PCRF/PCF获取策略。<br>- INHERIT：采用[**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)命令的设置值。 |
  | [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 漫游用户动态PCC功能（ROAMPCCSWITCH） | - ENABLE<br>- ENABLE<br>- INHERIT<br>- DISABLE | 对端协商 | 针对指定的DNN配置PCC使能开关，绑定PCC模板。<br>- ENABLE：开启APN级别的动态PCC功能。<br>- DISABLE：开启APN级别的本地PCC功能，不从PCRF/PCF获取策略。<br>- INHERIT：采用[**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)命令的设置值。 |
  | [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 拜访用户动态PCC功能（VISITPCCSWITCH） | - ENABLE<br>- ENABLE<br>- INHERIT<br>- DISABLE | 对端协商 | 针对指定的DNN配置PCC使能开关，绑定PCC模板。<br>- ENABLE：开启APN级别的动态PCC功能。<br>- DISABLE：开启APN级别的本地PCC功能，不从PCRF/PCF获取策略。<br>- INHERIT：采用[**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)命令的设置值。 |
  | [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | 针对指定的DNN配置PCC使能开关，绑定PCC模板。<br>- ENABLE：开启APN级别的动态PCC功能。<br>- DISABLE：开启APN级别的本地PCC功能，不从PCRF/PCF获取策略。<br>- INHERIT：采用[**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)命令的设置值。 |
  | [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 选择PCF方式（PCFSELECTMODE） | DNN<br>SERVINGSCOPE | 全网规划 | 需要灵活选择PCF时，规划该参数。<br>例如，根据DNN和NFLOC选择PCF时，需要复选DNN和NFLOC；根据DNN和SUPI选择PCF时，需要复选DNN和SUPI；根据DNN和SERVINGSCOPE选择PCF时，需要复选DNN和SERVINGSCOPE。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="huawei.com",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,PCCTEMPLATE="pcctemplate";`
  `SET APNPCCFUNC:APN="apn-test1",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;`
  `SET APNPCCFUNC:APN="apn-test2",HOMEPCCSWITCH=INHERIT,ROAMPCCSWITCH=INHERIT,VISITPCCSWITCH=INHERIT;`
  `SET APNPCCFUNC:APN="apn-another",HOMEPCCSWITCH=DISABLE,ROAMPCCSWITCH=DISABLE,VISITPCCSWITCH=DISABLE;`
  `SET APNPCCFUNC:APN="apn-test1",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,PCCTEMPLATE="pcctemplate";`
  `SET APNPCCFUNC:APN="apn-test1",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,PCFSELECTMODE=DNN-1&SERVINGSCOPE-1;`
  `SET APNPCCFUNC:APN="apn-test2",HOMEPCCSWITCH=INHERIT,ROAMPCCSWITCH=INHERIT,VISITPCCSWITCH=INHERIT;`
  `SET APNPCCFUNC:APN="apn-another",HOMEPCCSWITCH=DISABLE,ROAMPCCSWITCH=DISABLE,VISITPCCSWITCH=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L167:
    >             [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    >           b. 针对指定的DNN配置PCC使能开关，绑定PCC模板。
    >             [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >           c. （可选）[**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)命令中的“选择PCF方式（PCFSELECTMODE）”包含“NFLOC”时，在SMF的NF概述信息中增加位置信息。
    >             [**MOD NFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)
  L168:
    >           b. 针对指定的DNN配置PCC使能开关，绑定PCC模板。
    >             [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >           c. （可选）[**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)命令中的“选择PCF方式（PCFSELECTMODE）”包含“NFLOC”时，在SMF的NF概述信息中增加位置信息。
    >             [**MOD NFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)
    >     11. **可选：**配置PCC策略组。用于动态PCC时PCF下发预定义规则，或本地PCC时的静态规则。
  L246:
    > ```
    > ADD PCCTEMPLATE:PCCTEMPNAME="pcctemplate",SELPEERFAILACT=DEFAULT,INITIALFAILACT=FORBIDDEN,UPDATEFAILACT=INHERIT,NTFRSRURI=ENABLE,N7FAILOVERSW=ENABLE,PCFLBPARA=GROUPID;
    > SET APNPCCFUNC:APN="huawei.com",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,PCCTEMPLATE="pcctemplate";
    > ```
    > 

**md：`WSFD-109101/相关概念_71770360.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > | SM策略（会话管理策略） | PCC规则 | 与一个或一组SDF相关的信息，如用于检测SDF的SDF模板及相应的QoS、时间/流量上报、计费方式等策略和计费参数。<br>说明：SDF（Service Data Flow，业务流）<br>指与用户使用的业务关联的一组IP流，比如用户浏览一个网页时，从该网站发送到UE的下行IP数据包流即为一个SDF。 | 用于进行SDF粒度的策略控制。 |
    > 
    > 在UNC上，可以通过 **[**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** 命令配置本地策略，还可以通过 **[**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** 配置指定DNN的本地策略。
    > 
    > #### [会话规则和PCC规则](#ZH-CN_CONCEPT_0171770360)

### WSFD-102001

**md：`WSFD-102001/激活VoLTE基础语音业务（适用于SGW-C_PGW-C）_67930995.md`**
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC: APN="ims", HOMEPCCSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L41:
    >   [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 4. 开启APN下的PCC开关。
    >   [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > 5. 将指定的PCRF分组及号段信息绑定到指定APN。
    >   [**ADD PCRFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
  L81:
    > 
    > ```
    > SET APNPCCFUNC: APN="ims", HOMEPCCSWITCH=ENABLE;
    > ```
    > 

### WSFD-102101

**md：`WSFD-102101/激活VoLTE紧急呼叫（适用于SGW-C_PGW-C）_30394882.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 本地用户PCC功能（HOMEPCCSWITCH） | ENABLE | 本端规划 | 使能紧急APN的PCC功能。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 漫游用户PCC功能（ROAMPCCSWITCH） | INHERIT | 本端规划 | 使能紧急APN的PCC功能。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 拜访用户PCC功能（VISITPCCSWITCH） | INHERIT | 本端规划 | 使能紧急APN的PCC功能。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="sos",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=INHERIT,VISITPCCSWITCH=INHERIT;`
- 操作步骤上下文（±2 行原文）：
  L55:
    >       > 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。
    >     c. 使能APN的PCC功能。
    >       [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > 4. 配置紧急呼叫结束后释放缺省承载。
    >   [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
  L84:
    >   //使能APN的PCC功能。
    >   ```
    >   SET APNPCCFUNC:APN="sos",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=INHERIT,VISITPCCSWITCH=INHERIT;
    >   ```
    > 3. 配置紧急呼叫结束后释放缺省承载。

### WSFD-102706

**md：`WSFD-102706/激活VoNR紧急呼叫_46685913.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | sos | 全网规划 | 使能紧急APN的PCC功能。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 本地用户PCC功能（HOMEPCCSWITCH） | ENABLE | 与对端协商 | 使能紧急APN的PCC功能。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 漫游用户PCC功能（ROAMPCCSWITCH） | ENABLE | 与对端协商 | 使能紧急APN的PCC功能。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 拜访用户PCC功能（VISITPCCSWITCH） | ENABLE | 与对端协商 | 使能紧急APN的PCC功能。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 选择PCF方式（PCFSELECTMODE） | DNN<br>SERVINGSCOPE | 全网规划 | 使能紧急APN的PCC功能。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="sos", HOMEPCCSWITCH=ENABLE, ROAMPCCSWITCH=ENABLE, VISITPCCSWITCH=ENABLE, PCFSELECTMODE=DNN-1&GPSI-0&IMSI-0&NFLOC-0&PLMN-0&SERVINGSCOPE-1&SNSSAIS-0;`
- 操作步骤上下文（±2 行原文）：
  L99:
    >   > 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。
    >   使能APN的PCC功能。
    >   [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >   配置APN的IMS属性。
    >   [**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)
  L137:
    > 
    > ```
    > SET APNPCCFUNC:APN="sos", HOMEPCCSWITCH=ENABLE, ROAMPCCSWITCH=ENABLE, VISITPCCSWITCH=ENABLE, PCFSELECTMODE=DNN-1&GPSI-0&IMSI-0&NFLOC-0&PLMN-0&SERVINGSCOPE-1&SNSSAIS-0;
    > ```
    > 

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L80:
    > **[LST PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/查询PCC模板（LST PCCTEMPLATE）_09897067.md)**
    > 
    > [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > 
    > **[LST APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/查询APN PCC功能（LST APNPCCFUNC）_09897035.md)**
  L190:
    > **[LST RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/查询配置MODELC_D组网的SCP原因码（LST RESULTCODESCP）_16808737.md)**
    > 
    > **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)**
    > 
    > **[LST APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/查询APN PCC功能（LST APNPCCFUNC）_09897035.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | ims | 全网规划 | （可选）针对指定的DNN绑定PCC模板。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | （可选）针对指定的DNN绑定PCC模板。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";`
- 操作步骤上下文（±2 行原文）：
  L275:
    >       **[MOD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/修改Diameter路由域名信息（MOD DIAMRTREALM）_09897304.md)**
    >     h. **可选：**为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。
    >       [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >     i. 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。
    >       [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
  L433:
    > 
    >       ```
    >       SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
    >       ```
    >       //设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。
  L547:
    > 
    >       ```
    >       SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
    >       ```
    >       //设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | APN名称（APN） | ims | 全网规划 | 为语音业务绑定PCC模板，配置PCF状态过滤参数。 |
  | **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | 为语音业务绑定PCC模板，配置PCF状态过滤参数。 |
  | **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | PCF状态过滤参数（DISCCUSTOM） | MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT | 本端规划 | 为语音业务绑定PCC模板，配置PCF状态过滤参数。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | ims | 全网规划 | （可选）针对指定的DNN绑定PCC模板。 |
  | [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | （可选）针对指定的DNN绑定PCC模板。 |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;`
  `SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";`
- 操作步骤上下文（±2 行原文）：
  L283:
    >       [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) / **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**
    >     e. 为语音业务绑定PCC模板，配置PCF状态过滤参数。
    >       [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >     f. 配置对端PCF/SCP回复指定结果码后SMF/PGW-C的处理操作。
    >       > **说明**
  L299:
    >       **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)**
    >     j. **可选：**为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。
    >       [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    >     k. 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。
    >       [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
  L437:
    > 
    >             ```
    >             SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;
    >             ```
    >             //配置对端PCF回复指定结果码后SMF/PGW-C的处理操作。

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > - **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
    > - **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)**
    > - **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)**
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - **[ADD PCRF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | APN名称（APN） | apn-test | 全网规划 | 已通过命令<br>**[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**<br>进行配置，可以使用命令<br>**[LST APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>查询。 |
  | **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | PCC模板名称（PCCTEMPLATE） | test_template | 已配置数据中获取 | - |
  | **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | 本地用户动态PCC功能（HOMEPCCSWITCH） | ENABLE | 与对端协商 | - |
  | **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | 漫游用户动态PCC功能（ROAMPCCSWITCH） | ENABLE | 与对端协商 | - |
  | **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | 拜访用户动态PCC功能（VISITPCCSWITCH） | ENABLE | 与对端协商 | - |
- 任务示例脚本（该命令行）：
  `SET APNPCCFUNC:APN="apn-test",PCCTEMPLATE="test_template",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;`
  `SET APNPCCFUNC:APN="apn-test",PCCTEMPLATE="test_template",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L177:
    >       > 同一个APN只能配置TCP/SCTP中的一种场景，不允许两种场景同时配置到同一APN下。
    >     c. 将PCC Template绑定到APN下。
    >       **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)**
    > 11. 开启全局缺省PCC开关并设置域名绑定。
    >     a. 配置IMSI或MSISDN号码段。
  L266:
    >   ```
    >   ```
    >   SET APNPCCFUNC:APN="apn-test",PCCTEMPLATE="test_template",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
    >   ```
    >   //配置全局缺省的PCC开关，将PCRF域pcrf.huawei.com和用户号段imsi_msisdn_segment_1绑定。
  L384:
    >   ```
    >   ```
    >   SET APNPCCFUNC:APN="apn-test",PCCTEMPLATE="test_template",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
    >   ```
    >   //配置全局缺省的PCC开关，将PCRF域pcrf.huawei.com和用户号段imsi_msisdn_segment_1绑定。

## ④ 自动比对
- 命令真相参数（7）：['APN', 'DISCCUSTOM', 'HOMEPCCSWITCH', 'PCCTEMPLATE', 'PCFSELECTMODE', 'ROAMPCCSWITCH', 'VISITPCCSWITCH']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 7, '本端规划': 15, '对端协商': 6, '全网规划': 8, '与对端协商': 6}（多值→atom 应考虑 decision_driven）
