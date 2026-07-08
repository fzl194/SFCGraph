---
id: UDG@20.15.2@MMLCommand@ADD BLACKLISTRULE
type: MMLCommand
name: ADD BLACKLISTRULE（增加黑名单规则）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: BLACKLISTRULE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 8000
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 规则
status: active
---

# ADD BLACKLISTRULE（增加黑名单规则）

## 功能

**适用NF：PGW-U、UPF**

此命令用于在配置业务策略的时候增加指定策略类型的黑名单规则，用于实现相应策略类型的黑名单规则。通过的报文经过流过滤器或流过滤器组的匹配基于优先级选择相应策略类型中优先级最高的规则，命中黑名单规则的业务流无需执行相应策略类型的策略。

## 注意事项

- 该命令执行后立即生效。
- 当RULESPECTYPE参数不指定或者指定为DEFAULT时，该命令最大记录数为8000；当RULESPECTYPE参数指定为SPECIFICATION_LIMITED时，该命令最大记录数为100000。
- DEFAULT类型的UserProfile只能绑定DEFAULT类型的Rule。SPECIFICATION_LIMITED类型的UserProfile只能绑定SPECIFICATION_LIMITED类型的Rule。
- RULE命令与BLACKLISTRULE命令同属于Rule对象，共享配置记录空间、MOD RULE命令、RMV RULE命令和LST RULE命令。
- 对于同属于Rule对象的RULE命令和BLACKLISTRULE命令来说，规则名称和策略类型共同构成一条配置的唯一标识，由于共享配置记录空间，ADD RULE命令和ADD BLACKLISTRULE命令不能配置相同的规则名称和策略类型。
- BlackListRule的匹配原则与Rule是一致的，命中BlackListRule的业务流无需执行相应策略类型的策略。
- 在PCRF通过Gx接口下发Charging-Rule-Name激活本地规则时，可以同时激活多个规则名称相同但策略类型不同的BlackListRule配置。
- 如果BlackListRule没有配置生效时间，则默认一直生效。
- 不支持配置策略类型为PCC的黑名单规则。
- 当策略类型为IPREDIR或SRV_TRIGGER时，不允许配置绑定了七层协议和协议组的流过滤器。
- 当策略类型为IPREDIR或SRV_TRIGGER时，如果流过滤器组中含有绑定了七层协议或协议组的流过滤器，则不允许配置该流过滤器组。
- 如果流过滤器绑定了除DNS外的其他七层协议，则不能使用Web代理策略。
- worker类型的rule最多配置五种。
- worker类型的rule，通用Rule子策略名称不支持修改。
- 当前不支持本地业务分流和业务链两种策略类型。
- 该命令设定后的数据，需要通过LST RULE命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| POLICYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BWM：带宽管理，代表该规则可以配置带宽管理分类策略，其分类结果可以用于带宽管理的策略匹配功能。<br>- HEADEN：头增强，代表该规则可以配置头增强策略，可以基于配置的头增强策略向HTTP/RTSP请求报文头域中插入字段。<br>- WEBPROXY：Web Proxy，代表该规则可以配置WebProxy的IPFarm对象名称，用于设置WebProxy选择的服务器地址池。<br>- IPREDIR：IP重定向，代表该规则可以配置IP重定向的目标IP地址，支持IPv4和IPv6两种类型的IP地址。<br>- SMARTREDIRECT：智能重定向，代表该规则可以配置CaptivePortal业务对应的IPFarm的名称，http智能重定向的名称，dns重写动作的名称或者重定向的名称。<br>- REMARK_FPI：Remark或者FPI，代表该规则可以配置IP报文的DSCP重标记值或FPI策略。<br>- SRV_TRIGGER：Service Trigger Radius，代表该规则可以配置业务触发Radius消息交互功能标识，并配置Radius交互过程中报文处理方式。<br>- TRAFFICCLASS：Traffic Classifier，代表该规则可以配置Service Chain对象名称，用于实现业务链功能，此参数当前不支持。<br>- LBO：Local Break Out，代表该规则可以用于本地业务分流，此参数当前不支持。<br>- FIREWALL：防火墙，代表该规则可以配置防火墙策略。<br>- ADC：代表该规则用于应用检测与控制功能。<br>- QOS：代表该规则可以配置QoS策略，可以基于配置的QoS策略进行业务级QoS处理。<br>- WORKER：代表该规则用于通用Rule业务。<br>默认值：无<br>配置原则：黑名单规则不配置和执行任何策略。 |
| RULESPECTYPE | 规则规格类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则类型，当取值为SPECIFICATION_LIMITED时，表示规格受限规则，表示会话安装的规则数和被USERPROFILE绑定的规则数量均存在一定限制。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT：默认配置。<br>- SPECIFICATION_LIMITED：规格受限配置。<br>默认值：无<br>配置原则：<br>- 不配置此参数时值默认为Default。<br>- 该参数配置后不允许修改。 |
| FILTERINGMODE | 流过滤器或流过滤器组选择 | 可选必选说明：必选参数<br>参数含义：该参数用于设置流过滤器或流过滤器组选择。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FLOWFILTER：指定流过滤器作为过滤条件。<br>- FLOWFILTERGRP：指定流过滤器组作为过滤条件。<br>默认值：无<br>配置原则：<br>- 如果运营商希望基于流过滤器设置过滤条件，设置该参数为FLOWFILTER。<br>- 如果运营商希望基于流过滤器组设置过滤条件，设置该参数为FLOWFILTERGRP。 |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERINGMODE”配置为“FLOWFILTER”时为必选参数。<br>参数含义：该参数用于设置流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD FLOWFILTER命令配置生成。<br>- 设置的FLOWFILTERNAME必须是系统已经存在的流过滤器名称。 |
| FLWFLTRGRPNAME | 流过滤器组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERINGMODE”配置为“FLOWFILTERGRP”时为必选参数。<br>参数含义：该参数用于设置流过滤器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FLOWFILTERGRP命令配置生成。 |
| TIMERANGENAME | 时间段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置TimeRange名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD TIMERANGE命令配置生成。<br>- 如果运营商希望控制BlackListRule生效的时间段信息，则可以配置TimeRange对象名称，只有TimeRange定义的时间段内，BlackListRule才可以生效并参与匹配和策略处理。设置的TIMERANGENAME必须是系统已经存在的时间段名称。 |
| PRIORITY | 全局优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置全局优先级，仅对PCC用户生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。值越小优先级越高。<br>默认值：4294967295<br>配置原则：设置的PRIORITY仅对PCC用户生效。为了避免后续规划的规则与已配置规则的优先级冲突，建议规划优先级时按照10的倍数来定义，以便于后续插入任意优先级的新规则。 |
| BLWORKERNAME | 通用Rule子策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“POLICYTYPE”配置为“WORKER”时为必选参数。<br>参数含义：该参数用于设置通用Rule下子策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的子策略名称。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BLACKLISTRULE]] · 黑名单规则（BLACKLISTRULE）

## 使用实例

假如运营商需要定义一个头增强的黑名单规则，要求命中FlowFilter为TESTFLOWFILTER的业务不需要进行头增强操作，优先级为50：

```
ADD BLACKLISTRULE:RULENAME="TESTBLACKLISTRULE",POLICYTYPE=HEADEN,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="TESTFLOWFILTER",PRIORITY=50;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-BLACKLISTRULE.md`
