---
id: UNC@20.15.2@MMLCommand@ADD S1USRSECPARA
type: MMLCommand
name: ADD S1USRSECPARA（增加S1模式用户安全配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: S1USRSECPARA
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- S1模式用户安全参数
status: active
---

# ADD S1USRSECPARA（增加S1模式用户安全配置）

## 功能

![](增加S1模式用户安全配置(ADD S1USRSECPARA)_26305460.assets/notice_3.0-zh-cn_2.png)

不开启鉴权功能将导致身份未被鉴别的UE接入系统，引发系统内UE发生串号，计费错误等问题。

**适用网元：MME**

此命令用于增加指定号段的用户的鉴权、加密、完整性保护等安全配置。

## 注意事项

- 此命令对于当前系统内已存在签约数据的用户不立即生效，在用户签约数据被删除后再次进行附着时开始生效。
- 指定号段的用户群采用对应的安全配置参数，未指定的用户群采用默认的安全配置参数。
- 此命令最大记录数为128。
- 系统中缺省生成一条记录用于控制所有用户的安全策略。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>数据来源：整网规划<br>取值范围：5~15位十进制数字或<br>“DEFAULT”<br>默认值：无<br>配置原则：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。<br>说明：- 当IMSIPRE为字符串“DEFAULT”时，可以对“SUBRANGE（用户范围）”为“ALL_USER（所有用户）”的记录进行修改。 |
| SECPLC | 安全策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的安全策略，是否执行鉴权、安全协商流程。<br>数据来源：整网规划<br>取值范围：<br>- “NEVER(不鉴权不保护)”<br>- “AUTHONLY(只鉴权)”<br>- “AUTHANDPROTECTED(鉴权并保护)”<br>默认值：<br>“AUTHANDPROTECTED(鉴权并保护)”<br>配置原则：<br>- “NEVER(不鉴权不保护)”：在关闭安全功能的配置场景下选择。<br>- “AUTHONLY(只鉴权)”：在只执行鉴权不进行安全协商的配置场景下选择。<br>- “AUTHANDPROTECTED(鉴权并保护)”：在执行鉴权且进行安全协商的配置场景下选择。<br>- 建议值为“AUTHANDPROTECTED(鉴权并保护)”，“NEVER(不鉴权不保护)”和“AUTHONLY(只鉴权)”仅用于测试场景，不建议在实际场景中使用。 |
| SUPTINTAGTH | 完整性算法 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定配置系统支持的完整性算法。<br>前提条件：<br>- 该参数在“安全策略”设置为“AUTHANDPROTECTED(鉴权并保护)”时生效。<br>- 取值“EIA1(采用SNOW 3G完整性算法)”受License控制，在激活相应License项NAS Encryption and Integrity Protection (SNOW 3G)后，配置的EIA1算法才能生效。<br>- 取值“EIA2(采用AES完整性算法)”受License控制，在激活相应License项NAS Encryption and Integrity Protection(AES)后，配置的EIA2算法才能生效。<br>数据来源：整网规划<br>取值范围：<br>- “EIA0(采用空完整性算法)”<br>- “EIA1(采用SNOW 3G完整性算法)”<br>- “EIA2(采用AES完整性算法)”<br>- “EIA3(采用ZUC完整性算法)”<br>默认值：<br>“EIA0”<br>、<br>“EIA1”<br>、<br>“EIA2”<br>、<br>“EIA3”<br>配置原则：建议配置所有完整性算法，以兼容更多UE。<br>说明：- 系统根据[**ADD S1ALGPRIORITY**](增加S1模式加密和完整性算法优先级配置信息(ADD S1ALGPRIORITY)_26305462.md)配置的完整性算法的算法优先级，在UE和MME同时支持此算法的前提下，选择优先级最高的算法发送给UE。如果不配置[**ADD S1ALGPRIORITY**](增加S1模式加密和完整性算法优先级配置信息(ADD S1ALGPRIORITY)_26305462.md)命令，默认算法优先级从高到低分别为EIA2、EIA1、EIA3、EIA0，系统会按此优先级协商出和UE最终采用的完整性算法。<br>- 当参数设置为“EIA2(采用AES完整性算法)”时，“NAS信令加密与完整性保护”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-010303，License部件编码：LKV2AES02）。<br>- 当参数设置为“EIA1(采用SNOW 3G完整性算法)”时，“NAS信令加密与完整性保护”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-010303，License部件编码：LKV2SNOW3G02）。 |
| SUPTCIPHAGTH | 加密算法 | 可选必选说明：条件可选参数<br>参数含义：该参数用于配置系统支持的加密算法。<br>前提条件：<br>- 该参数在“安全策略”设置为“AUTHANDPROTECTED(鉴权并保护)”时生效。<br>- 取值“EEA1(采用SNOW 3G加密算法)”受License控制，在激活相应License项NAS Encryption and Integrity Protection(SNOW 3G)后，配置的EEA1算法才能生效。<br>- 取值“EEA2(采用AES加密算法)”受License控制，激活相应License项NAS Encryption and Integrity Protection(AES)后，配置的EEA2算法才能生效。<br>数据来源：整网规划<br>取值范围：<br>- “EEA0(采用空加密算法)”<br>- “EEA1(采用SNOW 3G加密算法)”<br>- “EEA2(采用AES加密算法)”<br>- “EEA3(采用ZUC加密算法)”<br>默认值：<br>“EEA0”<br>、<br>“EEA1”<br>、<br>“EEA2”<br>、<br>“EEA3”<br>配置原则：建议配置所有加密算法，以兼容更多UE。<br>说明：- 系统根据[**ADD S1ALGPRIORITY**](增加S1模式加密和完整性算法优先级配置信息(ADD S1ALGPRIORITY)_26305462.md)配置的加密算法的算法优先级，在UE和MME同时支持此算法的前提下，选择优先级最高的算法发送给UE。如果不配置[**ADD S1ALGPRIORITY**](增加S1模式加密和完整性算法优先级配置信息(ADD S1ALGPRIORITY)_26305462.md)命令，默认算法优先级从高到低分别为EEA2、EEA1、EEA3、EEA0，系统会按此优先级协商出和UE最终采用的加密算法。<br>- 当参数设置为“EEA2(采用AES加密算法)”时，“NAS信令加密与完整性保护”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-010303，License部件编码：LKV2AES02）。<br>- 当参数设置为“EEA1(采用SNOW 3G加密算法)”时，“NAS信令加密与完整性保护”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-010303，License部件编码：LKV2SNOW3G02）。 |
| OPTIONAL | 高级选项 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定是否使用鉴权事件、鉴权周期、鉴权事件上限、获取鉴权集数量和预取鉴权集等高级功能。<br>前提条件：该参数在<br>“安全策略”<br>设置为<br>“AUTHONLY(只鉴权)”<br>或<br>“AUTHANDPROTECTED(鉴权并保护)”<br>时生效。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>默认值：<br>“NO(否)” |
| AUTHEVENT | 鉴权事件 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定设置哪些流程属于灵活鉴权事件。<br>前提条件：该参数在<br>“高级选项”<br>设置为<br>“YES(是)”<br>时生效。<br>数据来源：本端规划<br>取值范围：<br>- “ATTACH(附着)”<br>- “INTRA_TAU(INTRA TAU)”<br>- “INTER_TAU(INTER TAU)”<br>- “DETACH(分离)”<br>- “SERVICE_REQUEST(服务请求)”<br>- “PROD_TAU（周期性TAU）”<br>- “SYSTEM_CHANGE_INTRA_TAU（系统间切换类型的INTRA TAU）”<br>- “INTRA_TAU_AFTER_HANDOVER（INTRA切换流程后的位置更新）”<br>- “INTER_TAU_AFTER_HANDOVER（INTER切换流程后的位置更新）”<br>默认值：<br>“ATTACH-1”<br>、<br>“INTER_TAU-1”<br>、<br>“SYSTEM_CHANGE_INTRA_TAU-1”<br>说明：- “ATTACH-1”：表示此流程属于灵活鉴权事件，其他参数取值相同。<br>- “ATTACH-0”：表示此流程不属于灵活鉴权事件，其他参数取值相同。<br>- “SERVICE_REQUEST”：同时控制Service Request和Control Plane Service Request流程的鉴权策略。<br>- “INTRA_TAU_AFTER_HANDOVER（INTRA切换流程后的位置更新）”和“INTER_TAU_AFTER_HANDOVER（INTER切换流程后的位置更新）”：在进行网络规划时，建议不要选择该参数，否则对Handover流程后TAU流程进行鉴权将导致整个切换流程时延增大。 |
| AUTHPERIOD | 鉴权周期 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户在基本流程（Attach/TAU/Detach/Service request）中发起周期鉴权。<br>前提条件：<br>- 该参数需要在“高级选项”设置为“YES(是)”时生效。<br>- 该参数配置受License控制，在激活相应License项(基于用户群的灵活鉴权)后，配置才能生效。<br>数据来源：本端规划<br>取值范围：0~24小时<br>默认值：24<br>配置原则：若取值为<br>“0”<br>，表示不启用周期鉴权功能。 |
| AUTHEVENTTHRESHOLD | 鉴权事件上限 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置无需鉴权的上限次数。当<br>“鉴权事件”<br>中指定的需要灵活鉴权的所有流程累积计数达到该上限时，将在当前对应的流程中进行一次鉴权。<br>前提条件：<br>- 该参数在“高级选项”设置为“YES(是)”时生效。<br>- 该参数配置受License控制，在激活相应License项(基于用户群的灵活鉴权)后，配置才能生效。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：1023<br>配置原则：<br>- 取值为“0”，表示不启用该项功能，所有的可选鉴权流程都不触发。<br>- 取值为“1”，表示每次“鉴权事件”中配置的可选鉴权事件发生都会触发鉴权流程。 |
| AUTHSETSNUMBER | 鉴权集数量 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定设置发送鉴权集请求时，从HSS获得的鉴权集数量。<br>前提条件：该参数在<br>“高级选项”<br>设置为<br>“YES(是)”<br>时生效。<br>数据来源：本端规划<br>取值范围：1~5<br>默认值：1 |
| PREGETAUTHSETS | 是否预取鉴权集 | 可选必选说明：条件可选参数<br>参数含义：该参数用于决定在鉴权流程前，MME是否预先从HSS中获得鉴权集。<br>前提条件：该参数在<br>“高级选项”<br>设置为<br>“YES(是)”<br>方时生效。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1USRSECPARA]] · S1模式用户安全配置（S1USRSECPARA）

## 使用实例

1. 配置IMSI前缀为3080101的用户群的安全策略参数。其中安全策略为鉴权且保护，完整性算法仅支持EIA2，加密算法同时支持EEA0、EEA2，配置扩展参数，鉴权事件为ATTACH和INTER_TAU，鉴权周期为23小时，鉴权事件上限为512，请求2组鉴权集，选择预取鉴权集：
  ADD S1USRSECPARA: IMSIPRE="3080101", SECPLC=AUTHANDPROTECTED, SUPTINTAGTH=EIA0-0&EIA1-0&EIA2-1, SUPTCIPHAGTH=EEA0-1&EEA1-0&EEA2-1, OPTIONAL=YES, AUTHEVENT=ATTACH-1&INTRA_TAU-0&INTER_TAU-1&DETACH-0&SERVICE_REQUEST-0, AUTHPERIOD=23, AUTHEVENTTHRESHOLD=512, AUTHSETSNUMBER=2, PREGETAUTHSETS=YES;
2. 配置IMSI前缀为3080102的用户群的安全策略参数。其中安全策略为鉴权且保护，完整性算法，加密算法支持选取默认值(即支持EIA0、EIA1、EIA2、EEA0、EEA1、EEA2)，不配置扩展参数：
  ADD S1USRSECPARA: IMSIPRE="3080102", SECPLC=AUTHANDPROTECTED;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-S1USRSECPARA.md`
