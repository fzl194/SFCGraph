---
id: UNC@20.15.2@MMLCommand@MOD RULE
type: MMLCommand
name: MOD RULE（修改规则）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: RULE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 规则
status: active
---

# MOD RULE（修改规则）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改规则，其中包含策略信息以及优先级。只有已经添加成功的规则才能够修改。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| POLICYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置策略类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- PCC：计费与策略控制，代表该规则可以配置PCC策略，用于实现计费和策略控制功能。<br>- BWM：带宽管理，代表该规则可以配置带宽管理分类策略，其分类结果可以用于带宽管理的策略匹配功能。<br>- HEADEN：头增强，代表该规则可以配置头增强策略，可以基于配置的头增强策略向HTTP/RTSP请求报文头域中插入字段。<br>- WEBPROXY：Web Proxy，代表该规则可以配置WebProxy的IPFarm对象名称，用于设置WebProxy选择的服务器地址池。<br>- IPREDIR：IP重定向，代表该规则可以配置IP重定向的目标IP地址，支持IPv4和IPv6两种类型的IP地址。<br>- SMARTREDIRECT：Captive Portal智能重定向，代表该规则可以配置Captive Portal的IPFarm对象名称，用于设置Captive Portal选择的服务器地址池。<br>- REMARK_FPI：Remark或者FPI，代表该规则可以配置IP报文的DSCP重标记值或FPI策略。<br>- SRV_TRIGGER：Service Trigger Radius，代表该规则可以配置业务触发Radius消息交互功能标识，并配置Radius交互过程中报文处理方式。<br>- TRAFFICCLASS：Traffic Classifier，代表该规则可以配置Service Chain对象名称，用于实现业务链功能。<br>- LBO：Local Break Out，代表该规则可以用于本地业务分流。<br>- FIREWALL：防火墙，代表该规则可以配置防火墙策略。<br>- ULCL：ULCL，代表该规则可以配置ULCL策略。<br>- ADC：代表该规则用于应用检测与控制功能。<br>- QOS：代表该规则可以配置QoS策略，可以基于配置的QoS策略进行业务级QoS处理。<br>- FUP：公平使用策略，代表该规则可以配置公平使用策略。<br>- NON_SPECIFIC_TYPE：不指定具体的类型。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |
| PRIORITY | 全局优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置全局优先级，仅对PCC用户生效。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～4294967295。值越小优先级越高。<br>默认值：无<br>配置原则：设置的PRIORITY仅对PCC用户生效。为了避免后续规划的规则与已配置规则的优先级冲突，建议规划优先级时按照10的倍数来定义，以便于后续插入任意优先级的新规则。 |
| POLICYNAME | 策略名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“POLICYTYPE”配置为“PCC”、“ULCL” 或 “QOS”时为可选参数。<br>参数含义：该参数用于设置策略名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 设置的POLICYNAME必须是本策略类型所属的系统已经存在的策略名称。根据策略类型的取值不同，所对应的策略定义对象不同，其代表的对象名也做相应的调整。- PCC：计费与策略控制，代表该策略名称为PCC策略组的名称。<br>- ULCL: 过滤器规则，代表策略名称为ULCL过滤器规则的名称。<br>- QOS：QOS动作策略，代表该策略名称为QOS业务的名称，使用ADD QOSPROP配置命令生成。 |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“POLICYTYPE”配置为“ULCL”时为可选参数。<br>参数含义：该参数用于设置rule的流过滤器名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RULERANGE | 规则生效范围 | 可选必选说明：条件可选参数<br>前提条件：该参数在“POLICYTYPE”配置为“PCC” 或 “QOS”时为可选参数。<br>参数含义：该参数用于设置规则生效范围。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- ALL：表示对中心和边缘UPF（主锚点UPF和辅锚点UPF）均生效。<br>- CENTRAL：表示对中心UPF（主锚点）生效。<br>- LOCAL：表示对边缘UPF（辅锚点）生效。<br>默认值：无<br>配置原则：对于已添加的规则，修改生效范围时，需检查Rule的生效范围与其绑定的UserProfile生效范围是否冲突；只对新用户生效业务生效。 |
| NWDAFEVENTS | NWDAF数据分析事件 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则对应的分析事件类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NULL：表示该规则非NWDAF智能规则。<br>- QOS_ANALYSIS：表示该规则对应的NWDAF事件分析类型为QOS分析。<br>- QOS_EXP_ANALYSIS：表示该规则对应的NWDAF事件分析类型为体验感知信息分析。<br>默认值：无<br>配置原则：无 |
| IPERULEDELYSW | 智能规则传递开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“NWDAFEVENTS”配置为“QOS_ANALYSIS” 或 “QOS_EXP_ANALYSIS”时为可选参数。<br>参数含义：该参数用于设置是否传递智能规则。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：当希望该规则仅用于智能双N7会话特性时，将该开关设置为DISABLE；否则，将该开关设置为ENABLE。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RULE]] · 规则（RULE）

## 使用实例

假如运营商需要定义一个规则，要求规则类型为PCC，基于名称为TESTPCCPOLICYGRPNM的PCC策略组进行计费和策略控制，优先级为50。修改优先级为60：

```
MOD RULE:RULENAME="TESTRULE",POLICYTYPE=PCC,PRIORITY=60,POLICYNAME="TESTPCCPOLICYGRPNM";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改规则（MOD-RULE）_09897202.md`
