# 配置七层业务触发的QOS保证（PGW-U、UPF）

- [操作场景](#ZH-CN_OPI_0180361858__1.3.1)
- [必备事项](#ZH-CN_OPI_0180361858__1.3.2)
- [操作步骤](#ZH-CN_OPI_0180361858__1.3.3)
- [任务示例](#ZH-CN_OPI_0180361858__1.3.4)

## [操作场景](#ZH-CN_OPI_0180361858)

当运营商规划了为某类需要QoS保证的业务提供专有承载/专有QoS Flow时，需要在 UDG 上配置基于七层的业务触发的QoS保证数据。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0180361858)

前提条件

- 请仔细阅读 [GWFD-020358 业务触发的QoS保证](../../GWFD-020358 业务触发的QoS保证_67655191.md) 。
- 完成加载license（如果有需求，请联系华为技术支持工程师处理）。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/过滤器/增加过滤器（ADD FILTER）_82837348.md) | 过滤器名字 （FILTERNAME） | filter_test | 本端规划 | UDG<br>通过将用户上下行报文匹配Filter，实现三四层报文的分析，从而过滤出会触发的数据报文。 |
| [**ADD FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/过滤器/增加过滤器（ADD FILTER）_82837348.md) | 三四层IPv4协议输入类型（L34PROTTYPE） | STRING | 本端规划 | UDG<br>通过将用户上下行报文匹配Filter，实现三四层报文的分析，从而过滤出会触发的数据报文。 |
| [**ADD FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/过滤器/增加过滤器（ADD FILTER）_82837348.md) | 三四层协议类型（L34PROTOCOL） | ANY | 本端规划 | UDG<br>通过将用户上下行报文匹配Filter，实现三四层报文的分析，从而过滤出会触发的数据报文。 |
| [**ADD L7FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/七层过滤器/增加七层过滤器（ADD L7FILTER）_82837397.md) | 七层过滤器名称（L7FILTERNAME） | l7_test | 本端规划 | 七层过滤条件。 |
| [**ADD L7FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/七层过滤器/增加七层过滤器（ADD L7FILTER）_82837397.md) | 子七层过滤器名称（SUBL7FLTNAME） | subl7_test | 本端规划 | 七层过滤条件。 |
| [**ADD L7FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/七层过滤器/增加七层过滤器（ADD L7FILTER）_82837397.md) | URL（URL） | www.example.com*/* | 本端规划 | 七层过滤条件。 |
| [**ADD FLOWFILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md) | 流过滤器名称（FLOWFILTERNAME） | flowfilter_test1 | 本端规划 | 流过滤器。 |
| [**ADD FLTBINDFLOWF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的过滤器绑定/增加流过滤器的过滤器绑定关系（ADD FLTBINDFLOWF）_82837366.md) | 流过滤器名称（FLOWFILTERNAME） | flowfilter_test1 | 已配置数据中获取 | 已通过<br>[**ADD FLOWFILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md)<br>命令配置。 |
| [**ADD FLTBINDFLOWF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的过滤器绑定/增加流过滤器的过滤器绑定关系（ADD FLTBINDFLOWF）_82837366.md) | 过滤器名字 （FILTERNAME） | filter_test | 已配置数据中获取 | 绑定的三四层过滤条件已通过<br>[**ADD FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/过滤器/增加过滤器（ADD FILTER）_82837348.md)<br>命令配置，可以通过<br>[**LST FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/过滤器/查询过滤器（LST FILTER）_82837353.md)<br>命令查询。 |
| [**ADD PROTBINDFLOWF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的协议绑定/增加流过滤器协议绑定关系（ADD PROTBINDFLOWF）_82837370.md) | 流过滤器名称 （FLOWFILTERNAME） | flowfilter_test1 | 已配置数据中获取 | 已通过<br>[**ADD FLOWFILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md)<br>命令配置。 |
| [**ADD PROTBINDFLOWF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的协议绑定/增加流过滤器协议绑定关系（ADD PROTBINDFLOWF）_82837370.md) | 协议名称（PROTOCOLNAME） | http | 本端规划 | 绑定的七层协议。 |
| [**ADD PROTBINDFLOWF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的协议绑定/增加流过滤器协议绑定关系（ADD PROTBINDFLOWF）_82837370.md) | 七层过滤器名字（L7FILTERNAME） | l7_test | 已配置数据中获取 | 绑定的七层过滤条件已通过<br>[**ADD L7FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/七层过滤器/增加七层过滤器（ADD L7FILTER）_82837397.md)<br>命令配置，可以通过<br>[**LST L7FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/七层过滤器/查询七层过滤器（LST L7FILTER）_86526660.md)<br>命令查询。 |
| [**ADD URR**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md) | 使用量上报规则名称<br>（URRNAME） | urr_1 | 本端规划 | 增加用于QoS事件上报的规则。 |
| [**ADD URR**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md) | URR标识（URRID） | 1001 | 本端规划 | 增加用于QoS事件上报的规则。 |
| [**ADD URR**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md) | 使用量上报模式<br>（USAGERPTMODE） | QOS | 固定取值 | 增加用于QoS事件上报的规则。 |
| [**ADD URRGROUP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md) | 使用量上报规则组名称（URRGROUPNAME） | urrgroup1 | 本端规划 | - |
| [**ADD URRGROUP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md) | 上行发起URR名称1<br>（UPURRNAME1） | urr_2 | 已配置数据中获取 | 已通过命令<br>[**ADD URR**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md)<br>配置。 |
| [**ADD URRGROUP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md) | 下行发起URR名称1<br>（DOWNURRNAME1） | urr_2 | 已配置数据中获取 | 已通过命令<br>[**ADD URR**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md)<br>配置。 |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务质量属性/增加QoS属性（ADD QOSPROP）_82837649.md) | Qos属性名称（QOSPROPNAME） | qos-property1 | 本端规划 | - |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务质量属性/增加QoS属性（ADD QOSPROP）_82837649.md) | QoS使用量上报规则名称<br>（QOSURRNAME） | urr_1 | 本端规划 | - |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务质量属性/增加QoS属性（ADD QOSPROP）_82837649.md) | 保证的上行比特率（GBRUPLKVALUE） | 110 | 本端规划 | - |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务质量属性/增加QoS属性（ADD QOSPROP）_82837649.md) | 保证的下行比特率（GBRDNLKVALUE） | 110 | 本端规划 | - |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务质量属性/增加QoS属性（ADD QOSPROP）_82837649.md) | 最大上行比特率（MBRUPLKVALUE） | 220 | 本端规划 | - |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务质量属性/增加QoS属性（ADD QOSPROP）_82837649.md) | 最大下行比特率（MBRDNLKVALUE） | 220 | 本端规划 | - |
| [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md) | PCC策略组名称（PCCPOLICYGRPNM） | ppg1 | 本端规划 | PCC策略组。 |
| [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md) | Qos属性名称（QOSPROPNAME） | qos-property1 | 已配置数据中获取 | QoS参数，已通过<br>[**ADD QOSPROP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务质量属性/增加QoS属性（ADD QOSPROP）_82837649.md)<br>命令配置完成。 |
| [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md) | URR组名称<br>（URRGROUPNAME） | urrgroup1 | 已配置数据中获取 | PCC策略组绑定的URR组，已通过<br>[**ADD URRGROUP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则组/增加URR组（ADD URRGROUP）_82837634.md)<br>命令配置完成。 |
| [**ADD WELLKNOWNPORT**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/知名端口/增加知名端口（ADD WELLKNOWNPORT）_82837332.md) | 知名端口名称 （IDENPROTNAME） | http | 本端规划 | HTTP协议的默认端口是80。 |
| [**ADD WELLKNOWNPORT**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/知名端口/增加知名端口（ADD WELLKNOWNPORT）_82837332.md) | 协议名称（PROTOCOLNAME） | http | 本端规划 | HTTP协议的默认端口是80。 |
| [**ADD WELLKNOWNPORT**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/知名端口/增加知名端口（ADD WELLKNOWNPORT）_82837332.md) | 端口范围操作码（PORTOP） | EQUAL | 本端规划 | HTTP协议的默认端口是80。 |
| [**ADD WELLKNOWNPORT**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/知名端口/增加知名端口（ADD WELLKNOWNPORT）_82837332.md) | 起始端口号（STARTPORT） | 80 | 本端规划 | HTTP协议的默认端口是80。 |
| [**ADD WELLKNOWNPORT**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/知名端口/增加知名端口（ADD WELLKNOWNPORT）_82837332.md) | 优先级（PRIORITY） | 5 | 本端规划 | HTTP协议的默认端口是80。 |
| [**ADD SADEDICBEARER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务感知专有承载/增加业务感知专有承载配置（ADD SADEDICBEARER）_82837654.md) | 协议等级（PROTOCOLLEVEL） | PROTOCOL | 本端规划 | - |
| [**ADD SADEDICBEARER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务感知专有承载/增加业务感知专有承载配置（ADD SADEDICBEARER）_82837654.md) | 协议名称（PROTOCOLNAME） | http | 已配置数据中获取 | - |
| [**ADD SADEDICBEARER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务感知专有承载/增加业务感知专有承载配置（ADD SADEDICBEARER）_82837654.md) | 触发专有承载模式（TRIGGERMODE） | DOWNLINK_ONLY | 本端规划 | - |
| [**ADD RULE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 规则名称（RULENAME） | rule_test | 本端规划 | - |
| [**ADD RULE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - |
| [**ADD RULE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 流过滤器或流过滤器组选择(FILTERINGMODE) | FLOWFILTER | 本端规划 | - |
| [**ADD RULE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 流过滤器名称（FLOWFILTERNAME） | flowfilter_test1 | 已配置数据中获取 | 绑定的FlowFilter已通过<br>[**ADD FLOWFILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md)<br>命令配置，可以通过<br>[**LST FLOWFILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/查询流过滤器（LST FLOWFILTER）_82837364.md)<br>命令查询。 |
| [**ADD RULE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 策略名称（POLICYNAME） | ppg1 | 已配置数据中获取 | 绑定的PCC策略组已通过<br>[**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md)<br>命令配置，可以通过<br>[**LST PCCPOLICYGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/查询PCC策略组（LST PCCPOLICYGRP）_82837609.md)<br>命令查询。 |
| [**ADD RULE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md) | 全局优先级（PRIORITY） | 5 | 本端规划 | 指定rule的优先级。 |
| [**ADD USERPROFILE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/用户模板/增加用户模板（ADD USERPROFILE）_82837279.md) | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | - |
| [**ADD RULEBINDING**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_82837272.md) | 用户模板名称（USERPROFILENAME） | up_test | 已配置数据中获取 | 使用<br>[**ADD USERPROFILE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/用户模板/增加用户模板（ADD USERPROFILE）_82837279.md)<br>命令定义的用户模板名称。 |
| [**ADD RULEBINDING**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_82837272.md) | 规则名称（RULENAME） | rule_test | 已配置数据中获取 | UserProfile绑定的业务规则，已通过<br>[**ADD RULE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md)<br>命令配置完成。 |

## [操作步骤](#ZH-CN_OPI_0180361858)

1. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)
2. 配置三四层过滤条件。
  [**ADD FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/过滤器/增加过滤器（ADD FILTER）_82837348.md)
3. 配置七层过滤条件。
  [**ADD L7FILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/七层规则管理/七层过滤器/增加七层过滤器（ADD L7FILTER）_82837397.md)
4. 配置流过滤器，绑定三四层、七层过滤条件。
    a. 配置流过滤器。
      [**ADD FLOWFILTER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器/增加流过滤器（ADD FLOWFILTER）_82837361.md)
    b. 配置三四层过滤条件与流过滤器的绑定关系。
      [**ADD FLTBINDFLOWF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的过滤器绑定/增加流过滤器的过滤器绑定关系（ADD FLTBINDFLOWF）_82837366.md)
    c. 配置七层过滤条件与流过滤器的绑定关系。
      [**ADD PROTBINDFLOWF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器的协议绑定/增加流过滤器协议绑定关系（ADD PROTBINDFLOWF）_82837370.md)
    d. 将新配置的Filter置为生效。
      [**SET REFRESHSRV**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/业务刷新/业务刷新（SET REFRESHSRV）_82837355.md)
5. 配置QoS属性。
    a. 配置QoS类型URR。
      [**ADD URR**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/使用率上报规则/增加URR（ADD URR）_82837629.md)
    b. 配置QoS属性。
      [**ADD QOSPROP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务质量属性/增加QoS属性（ADD QOSPROP）_82837649.md)
6. 配置PCC策略组。
  [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md)
7. 配置协议识别数据。
  [**ADD WELLKNOWNPORT**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/知名端口/增加知名端口（ADD WELLKNOWNPORT）_82837332.md)
8. 使能协议或协议组支持基于业务感知能力触发专有承载创建，并配置触发专有承载创建的模式。
  [**ADD SADEDICBEARER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/用户QOS控制/业务QOS控制/业务感知专有承载/增加业务感知专有承载配置（ADD SADEDICBEARER）_82837654.md)
9. 配置业务规则。
  [**ADD RULE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则/增加规则（ADD RULE）_82837266.md)
  > **说明**
  > 如果运营商希望基于流过滤器组设置过滤条件时，配置 “流过滤器或流过滤器组选择(FILTERINGMODE)” 为 “FLOWFILTERGRP” ，并且使用 [**ADD FLOWFILTERGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/流过滤器管理/流过滤器组/增加流过滤器组（ADD FLOWFILTERGRP）_82837384.md) 命令配置流过滤器组。
10. 配置业务策略组合。
    a. 创建UserProfile。
      [**ADD USERPROFILE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/用户模板/增加用户模板（ADD USERPROFILE）_82837279.md)
    b. 将已配置的Rule绑定到UserProfile。
      [**ADD RULEBINDING**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_82837272.md)
11. 配置UPF上报Flow-Description信息的格式。
  **[SET UPGLBPMPARA](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/计费控制/全局的PM策略控制/设置全局策略管理参数（SET UPGLBPMPARA）_82837620.md)**

## [任务示例](#ZH-CN_OPI_0180361858)

任务描述

配置基于七层专有承载创建 ，并使能HTTP协议支持基于业务感知能力触发专有承载创建，触发专有承载创建的模式为DOWNLINK_ONLY 。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="
LKV3G5STQE01
",SWITCH=ENABLE;
```

//配置三四层过滤条件。

```
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
```

//配置七层过滤条件。

```
ADD L7FILTER:L7FILTERNAME="l7_test",SUBL7FLTNAME="subl7_test",URL="www.example.com*/*";
```

//配置流过滤器，绑定三四层、七层过滤条件。

```
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test1";
```

```
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1",FILTERNAME="filter_test";
```

```
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1",PROTOCOLNAME="http",L7FILTERNAME="l7_test";
```

```
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
```

//配置QoS属性。

```
ADD URR: URRNAME="urr_1", URRID=1001, USAGERPTMODE=QOS;
```

```
ADD QOSPROP:QOSPROPNAME="qos-property1", QOSURRNAME="urr_1", GBRUPLKVALUE=110, GBRDNLKVALUE=110, MBRUPLKVALUE=220, MBRDNLKVALUE=220;
```

//配置PCC策略组。

```
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="ppg1",URRGROUPNAME="urrgroup1",QOSPROPNAME="qos-property1";
```

//配置协议识别。

```
ADD WELLKNOWNPORT: IDENPROTNAME="http",PROTOCOLNAME="http",PORTOP=EQUAL,STARTPORT=80,PRIORITY=5;
```

//使能HTTP协议支持基于业务感知能力触发专有承载创建，触发专有承载创建的模式为DOWNLINK_ONLY。

```
ADD SADEDICBEARER:PROTOCOLLEVEL=PROTOCOL,PROTOCOLNAME="http",TRIGGERMODE=DOWNLINK_ONLY;
```

//配置业务规则。

```
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
FILTERINGMODE=FLOWFILTER,
 FLOWFILTERNAME="flowfilter_test1", POLICYNAME="ppg1",PRIORITY=10;
```

//配置业务策略组合。

```
ADD USERPROFILE:USERPROFILENAME="up_test";
```

```
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

//配置UPF上报Flow-Description信息的格式。

```
SET UPGLBPMPARA: FLOWDANYFMT=AnyFMT;
```
