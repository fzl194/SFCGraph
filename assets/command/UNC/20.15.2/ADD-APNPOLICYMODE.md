---
id: UNC@20.15.2@MMLCommand@ADD APNPOLICYMODE
type: MMLCommand
name: ADD APNPOLICYMODE（增加基于APN的策略接口的选择方式）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNPOLICYMODE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 基于APN的策略接口选择方式配置
status: active
---

# ADD APNPOLICYMODE（增加基于APN的策略接口的选择方式）

## 功能

![](增加基于APN的策略接口的选择方式（ADD APNPOLICYMODE）_72001541.assets/notice_3.0-zh-cn_2.png)

配置基于APN的策略接口的选择方式不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加基于APN的策略接口的选择方式。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 当需要使用本命令配置2G和3G接入使用Npcf接口时，需要提前和对端PCF确认是否支持。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| TMACCTYPE | 指定终端和接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定终端和接入类型。<br>数据来源：本端规划<br>取值范围：<br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。<br>- “UENON5G_RAT4G（非5G终端4G接入）”：非5G终端4G接入是指在4G接入的PDN激活流程。<br>- “RAT2G（2G接入）”：2G接入是指在2G接入的PDP激活流程。<br>- “RATNBIOT（NB-IoT接入）”：NB-IoT接入是指NB-IoT用户接入。<br>- “NON_3GPP（非3GPP接入）”：非3GPP接入是指用户从非3GPP网络接入。<br>- “RATLTEM（LTE-M接入）”：LTE-M接入是指LTE-M用户接入。<br>- “RAT3G（3G接入）”：3G接入是指在3G接入的PDP激活流程。<br>默认值：无<br>配置原则：无 |
| BY5GSIWKI | 按5GS互操作指示选择策略接口开关 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于配置是否按5GS互操作指示的取值来选择策略接口。"5GS互操作指示"指示S11、S5/S8、S2b接口的“5GS Interworking Indication”参数。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：DISABLE<br>配置原则：<br>本参数为ENABLE时，当对端携带“5GS Interworking Indication”参数为1时，选择Npcf接口；当对端携带“5GS Interworking Indication”参数为0，或者对端未携带“5GS Interworking Indication”参数时，选择Gx接口。<br>本参数为DISABLE且BY5GCNRI参数为DISABLE时，根据FORCED参数选择策略接口，需要配置FORCED参数。 |
| FORCED | 指定策略接口 | 可选必选说明：该参数在"TMACCTYPE"配置为"RAT2G"、"RATNBIOT"、"NON_3GPP"、"RATLTEM"、"RAT3G"时为条件必选参数。该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于指定策略接口。在参数BY5GSIWKI取值为DISABLE时，按本参数的配置确定策略接口。在参数TMACCTYPE配置为RAT2G、RAT3G、RATNBIOT、RATLTEM或者NON_3GPP时，按本参数的配置确定策略接口。<br>数据来源：本端规划<br>取值范围：<br>- “Npcf（Npcf接口）”：使用Npcf接口。<br>- “Gx（Gx接口）”：使用Gx接口<br>默认值：无<br>配置原则：无 |
| PCFRESELBYPCFID | 是否基于PCF实例标识决策策略接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于控制当基于用户的终端和接入类型决策出策略接口类型为“Gx（Gx接口）”时，是否再基于PCF实例标识重新决策最终策略接口类型。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>该参数仅在Gx模式下生效。 |
| BY5GCNRI | 按5GC无限制接入标识选择策略接口开关 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于配置是否按5GC无限制接入标识的取值来选择计费接口。“5GC无限制接入标识”是指S11、S5/S8、S2b接口的“5GC Not Restricted Indication”参数。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：DISABLE<br>配置原则：<br>本参数为ENABLE时，当对端携带“5GC Not Restricted Indication”参数为1时，选择Npcf接口；当对端携带“5GC Not Restricted Indication”参数为0，或者对端未携带“5GC Not Restricted Indication”参数时，选择Gx接口。<br>本参数为DISABLE且BY5GSIWKI参数为DISABLE时，根据FORCED参数选择策略接口，需要配置FORCED参数。 |

## 操作的配置对象

- [基于APN的策略接口的选择方式（APNPOLICYMODE）](configobject/UNC/20.15.2/APNPOLICYMODE.md)

## 关联任务

- [[UNC@20.15.2@Task@0-00007]]

## 使用实例

增加基于APN的策略接口的选择方式，“APN名称”为“HUAWEI.COM”，指定5G终端4G接入的策略接口为Npcf。

```
ADD APNPOLICYMODE: APN="HUAWEI.COM",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Npcf;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于APN的策略接口的选择方式（ADD-APNPOLICYMODE）_72001541.md`
