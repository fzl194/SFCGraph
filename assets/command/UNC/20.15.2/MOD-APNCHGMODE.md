---
id: UNC@20.15.2@MMLCommand@MOD APNCHGMODE
type: MMLCommand
name: MOD APNCHGMODE（修改基于APN的计费接口选择方式）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNCHGMODE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- APN计费模式
status: active
---

# MOD APNCHGMODE（修改基于APN的计费接口选择方式）

## 功能

![](修改基于APN的计费接口选择方式（MOD APNCHGMODE）_72001549.assets/notice_3.0-zh-cn_2.png)

修改基于APN的计费接口选择方式不当可能选错计费策略接口，相应计费策略接口未配置时会导致计费相关流程失败，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于修改不同的APN在不同类型终端接入不同网络时所选择的计费接口。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| TMACCTYPE | 指定终端和接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定终端和接入类型。<br>数据来源：本端规划<br>取值范围：<br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。<br>- “UE5G_RAT5G（5G终端5G接入）”：5G终端5G接入是指在5G接入的PDU激活流程。<br>- “UENON5G_RAT4G（非5G终端4G接入）”：非5G终端4G接入是指在4G接入的PDN激活流程。<br>- “RAT2G（2G接入）”：2G接入是指在2G接入的一次PDP激活流程。<br>- “RATNBIOT（NB-IoT接入）”：NB-IoT接入是指NB-IoT用户接入。<br>- “NON_3GPP（非3GPP接入）”：非3GPP接入是指用户从非3GPP网络接入。<br>- “RATLTEM（LTE-M接入）”：LTE-M接入是指LTE-M用户接入。<br>- “RAT3G（3G接入）”：3G接入是指在3G接入的PDP一次激活流程。<br>默认值：无<br>配置原则：无 |
| BY5GSIWKI | 按5GS互操作指示选择计费接口 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于配置是否按5GS互操作标识的取值来选择计费接口。“5GS互操作标识”是指S11、SS5/S8、S2b接口的“5GS Interworking Indication”参数。<br>数据来源：本端规划<br>取值范围：<br>- False（否）<br>- True（是）<br>默认值：无<br>配置原则：<br>本参数为TRUE时，当对端携带“5GS Interworking Indication”参数为1时，选择Nchf接口；当对端携带“5GS Interworking Indication”参数为0，或者对端未携带“5GS Interworking Indication”参数时，选择GaGy接口。<br>本参数为FALSE且BY5GCNRI参数为FALSE时，根据FORCED参数选择计费接口，需要配置FORCED参数。 |
| FORCED | 指定的计费接口 | 可选必选说明：该参数在"TMACCTYPE"配置为"RAT2G"、"RATNBIOT"、"NON_3GPP"、"RATLTEM"、"RAT3G"时为条件必选参数。该参数在"TMACCTYPE"配置为"UE5G_RAT5G"、"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于指定计费接口。<br>数据来源：本端规划<br>取值范围：<br>- “GaGyMode（GaGy模式）”：GaGy模式<br>- “NchfMode（Nchf模式）”：Nchf模式<br>- “INVALID（无效值）”：无效计费模式<br>默认值：无<br>配置原则：<br>当前版本取值为INVALID，将会选择Nchf模式。 |
| FORSGWONLY | 作为SGW计费模式 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：作为SGW时的计费模式。<br>数据来源：本端规划<br>取值范围：<br>- GaGyMode（GaGy模式）<br>- NchfMode（Nchf模式）<br>- Inherit（继承其他选项）<br>默认值：无<br>配置原则：<br>当前版本取值为Inherit，将会选择GaGy模式。 |
| FORVSMFONLY | 作为V-SMF计费模式 | 可选必选说明：该参数在"TMACCTYPE"配置为"UE5G_RAT5G"时为条件可选参数。<br>参数含义：该参数用于作为V-SMF时的计费模式。<br>数据来源：全网规划<br>取值范围：<br>- “GaGyMode（GaGy模式）”：GaGy模式<br>- “NchfMode（Nchf模式）”：Nchf模式<br>默认值：无<br>配置原则：无 |
| ISMFCHGSW | I-SMF是否支持计费 | 可选必选说明：该参数在"TMACCTYPE"配置为"UE5G_RAT5G"时为条件可选参数。<br>参数含义：I-SMF是否支持计费。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| BY5GCNRI | 按5GC无限制接入标识选择计费接口 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于配置是否按5GC无限制接入标识的取值来选择计费接口。“5GC无限制接入标识”是指S11、S5/S8、S2b接口的“5GC Not Restricted Indication Selection”参数。<br>数据来源：本端规划<br>取值范围：<br>- False（否）<br>- True（是）<br>默认值：无<br>配置原则：<br>本参数为TRUE时，当对端携带“5GC Not Restricted Indication Selection”参数为1时，选择Nchf接口；当对端携带“5GC Not Restricted Indication Selection”参数为0，或者对端未携带“5GC Not Restricted Indication Selection”参数时，选择GaGy接口。<br>本参数为FALSE且BY5GSIWKI参数为FALSE时，根据FORCED参数选择计费接口，需要配置FORCED参数。 |

## 操作的配置对象

- [基于APN的计费接口选择方式（APNCHGMODE）](configobject/UNC/20.15.2/APNCHGMODE.md)

## 使用实例

修改基于APN的计费接口选择方式，“APN名称”为“huawei.com”，指定5G终端4G接入的计费接口为Nchf。

```
MOD APNCHGMODE:APN="huawei.com", TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=False, FORCED=NchfMode;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于APN的计费接口选择方式（MOD-APNCHGMODE）_72001549.md`
