# 激活HTTP3.0 Host识别

- [操作场景](#ZH-CN_OPI_0000001456786521__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001456786521__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001456786521__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001456786521__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001456786521)

在 UDG 上激活HTTP3.0 Host识别功能。当用户访问的业务采用HTTP3.0协议承载时，需要部署HTTP3.0 Host识别特性，对业务实施计费与策略控制。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0000001456786521)

前提条件

- 请仔细阅读[特性概述](特性概述_06826690.md)。
- UDG完成与周边网元的对接。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET SACOMMONPARA**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/SA公共参数/设置SA业务公共参数（SET SACOMMONPARA）_82837416.md) | QUIC协议识别功能增强开关 | ENABLE | 固定取值 | - |
| [**ADD URR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md) | 使用量上报规则名称（URRNAME） | urr_red | 本端规划 | 使用量上报规则信息，要求<br>UDG<br>和CG两端的URRID取值要一致。 |
| [**ADD URR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md) | URR标识（URRID） | 12001 | 全网规划 | 使用量上报规则信息，要求<br>UDG<br>和CG两端的URRID取值要一致。 |
| [**ADD URR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md) | 使用量上报模式（USAGERPTMODE） | OFFLINE | 全网规划 | 使用量上报规则信息，要求<br>UDG<br>和CG两端的URRID取值要一致。 |
| [**ADD URRGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md) | 使用量上报规则组名称（URRGROUPNAME） | cp_red | 本端规划 | - |
| [**ADD URRGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md) | 上行发起URR名称1（UPURRNAME1） | urr_red | 从已配置数据中获取 | 已在该配置任务中通过命令<br>[**ADD URR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md)<br>配置。 |
| [**ADD URRGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md) | 下行发起URR名称1（DOWNURRNAME1） | urr_red | 从已配置数据中获取 | 已在该配置任务中通过命令<br>[**ADD URR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md)<br>配置。 |
| [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md) | PCC策略组名称（PCCPOLICYGRPNM） | cg_red | 本端规划 | PCC策略组。 |
| [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md) | URR组名称(URRGROUPNAME) | cp_red | 从已配置数据中获取 | PCC策略组绑定的URR组，已通过<br>[**ADD URRGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md)<br>命令配置完成。 |
| [**ADD FLOWFILTER**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md) | 流过滤器名称（FLOWFILTERNAME） | fg_red | 本端规划 | 流过滤器。 |
| [**ADD PROTBINDFLOWF**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的协议绑定/增加流过滤器协议绑定关系（ADD PROTBINDFLOWF）_82837370.md) | 流过滤器名称（FLOWFILTERNAME） | fg_red | 从已配置数据中获取 | 流过滤器名称已通过<br>[**ADD FLOWFILTER**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md)<br>命令配置。 |
| [**ADD PROTBINDFLOWF**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的协议绑定/增加流过滤器协议绑定关系（ADD PROTBINDFLOWF）_82837370.md) | 协议名称（PROTOCOLNAME） | icloudprivaterelay | 本端规划 | 绑定的七层协议。 |
| [**ADD RULE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 规则名称（RULENAME） | rule_red | 本端规划 | 使用的内容计费规则。 |
| [**ADD RULE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 流过滤器或流过滤器组选择(FILTERINGMODE) | FLOWFILTER | 本端规划 | - |
| [**ADD RULE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 流过滤器名称（FLOWFILTERNAME） | fg_red | 从已配置数据中获取 | 绑定的FlowFilter已通过<br>[**ADD FLOWFILTER**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md)<br>命令配置。 |
| [**ADD RULE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - |
| [**ADD RULE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 策略名称（POLICYNAME） | cg_red | 本端规划 | 绑定的PCC策略组已通过<br>[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md)<br>命令配置。 |
| [**ADD USERPROFILE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/用户模板/增加用户模板（ADD USERPROFILE）_82837279.md) | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | - |
| [**ADD RULEBINDING**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_82837272.md) | 规则名称（RULENAME） | rule_red | 从已配置数据中获取 | UserProfile绑定的业务规则，已通过<br>[**ADD RULE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md)<br>命令配置完成。 |

## [操作步骤](#ZH-CN_OPI_0000001456786521)

1. 打开QUIC协议识别功能增强开关
  [**SET SACOMMONPARA**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/SA公共参数/设置SA业务公共参数（SET SACOMMONPARA）_82837416.md)
    - 如果“开关”为“ENABLE”，请执行[3](#ZH-CN_OPI_0000001456786521__cmd72501694814)。
    - 如果“开关”为“DISABLE”，则执行[**SET SACOMMONPARA**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/SA公共参数/设置SA业务公共参数（SET SACOMMONPARA）_82837416.md)命令打开本特性对应的License配置开关。
2. 配置内容计费使用的URR和URR Group。
    a. 配置URR。
      [**ADD URR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md)
    b. 配置上行和下行发起的业务对应的URR。
      [**ADD URRGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md)
3. 配置内容计费使用的PCC策略组。
  [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md)
4. 配置过滤条件。
    a. 配置流过滤器。
      [**ADD FLOWFILTER**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md)
    b. 绑定七层过滤条件。
      [**ADD PROTBINDFLOWF**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的协议绑定/增加流过滤器协议绑定关系（ADD PROTBINDFLOWF）_82837370.md)
5. 配置内容计费使用的规则。
  [**ADD RULE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md)
6. 配置内容计费规则绑定用户模板。
    a. 创建UserProfile实例。
      [**ADD USERPROFILE**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/用户模板/增加用户模板（ADD USERPROFILE）_82837279.md)
    b. 将已配置的内容计费规则绑定到UserProfile。
      [**ADD RULEBINDING**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_82837272.md)

## [任务示例](#ZH-CN_OPI_0000001456786521)

任务描述

开启 UDG 的HTTP3.0识别功能， UDG 将访问HTTP3.0承载类业务，例如PrivateRelay用户业务，报文记入使用量上报规则名称urr_red，进行离线计费。

脚本

//打开QUIC协议识别功能增强开关。

```
SET SACOMMONPARA: QUICIDENFUNCEN=ENABLE;
```

//配置离线计费的费率标识。

```
ADD URR:URRNAME="urr_red",URRID=12001,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="cp_red",UPURRNAME1="urr_red",DOWNURRNAME1="urr_red";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="cg_red",URRGROUPNAME="cp_red";
```

//配置七层信息。

```
ADD FLOWFILTER:FLOWFILTERNAME="fg_red";
ADD PROTBINDFLOWF:FLOWFILTERNAME="fg_red",PROTOCOLNAME="icloudprivaterelay";
```

//配置内容计费规则。

```
ADD RULE:RULENAME="rule_red",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="fg_red",POLICYNAME="cg_red";
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
```

//配置内容计费规则绑定用户模板。

```
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_red";
```
