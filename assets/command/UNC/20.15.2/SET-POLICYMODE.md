---
id: UNC@20.15.2@MMLCommand@SET POLICYMODE
type: MMLCommand
name: SET POLICYMODE（设置策略接口的选择方式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: POLICYMODE
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
- 策略模式选择
status: active
---

# SET POLICYMODE（设置策略接口的选择方式）

## 功能

![](设置策略接口的选择方式（SET POLICYMODE）_09653658.assets/notice_3.0-zh-cn_2.png)

配置策略接口的选择方式不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置策略接口的选择方式。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 5G终端在5G接入时使用Npcf接口。
- 4G/5G互操作流程的策略接口不变。2/3/4G互操作流程的策略接口不变。
- 当需要使用本命令配置2G和3G接入使用Npcf接口时，需要提前和对端PCF确认是否支持。
- 当非5G终端4G接入时，若通过该命令修改参数“FORCED”的取值，则对应的参数“BYIWKUEN5GR4G”的取值会被同步修改成“DISABLE(不使能)”。
- 枚举项RAT3G默认初始记录的参数“FORCED”的值为Gx，参数“PCFRESELBYPCFID”的值为FALSE。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TMACCTYPE | BY5GSIWKI | BYIWKUEN5GR4G | FORCED | PCFRESELBYPCFID | BY5GCNRI |
| --- | --- | --- | --- | --- | --- |
| UE5G_RAT4G | ENABLE | DISABLE | INVALID | FALSE | DISABLE |
| UENON5G_RAT4G | DISABLE | DISABLE | Gx | FALSE | DISABLE |
| RAT2G | DISABLE | DISABLE | Gx | FALSE | DISABLE |
| RATNBIOT | DISABLE | DISABLE | Gx | FALSE | DISABLE |
| NON_3GPP | DISABLE | DISABLE | Gx | FALSE | DISABLE |
| RATLTEM | DISABLE | DISABLE | Gx | FALSE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMACCTYPE | 指定终端和接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定终端和接入类型。<br>数据来源：全网规划<br>取值范围：<br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。<br>- “UENON5G_RAT4G（非5G终端4G接入）”：非5G终端4G接入是指在4G接入的PDN激活流程。<br>- “RAT2G（2G接入）”：2G接入是指在2G接入的PDP激活流程。<br>- “RATNBIOT（NB-IoT接入）”：NB-IoT接入是指NB-IoT用户接入。<br>- “NON_3GPP（非3GPP接入）”：非3GPP接入是指用户从非3GPP网络接入。<br>- “RATLTEM（LTE-M接入）”：LTE-M接入是指LTE-M用户接入。<br>- “RAT3G（3G接入）”：3G接入是指在3G接入的PDP激活流程。<br>默认值：无。<br>配置原则：无 |
| BY5GSIWKI | 按5GS互操作指示选择策略接口开关 | 可选必选说明：该参数在"TMACCTYPE"配置为"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于配置是否按5GS互操作指示的取值来选择策略接口。"5GS互操作指示"指示S11、S5/S8、S2b接口的“5GS Interworking Indication”参数。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLICYMODE查询当前参数配置值。<br>配置原则：<br>本参数为ENABLE时，当对端携带“5GS Interworking Indication”参数为1时，选择Npcf接口；当对端携带“5GS Interworking Indication”参数为0，或者对端未携带“5GS Interworking Indication”参数时，选择Gx接口。<br>本参数为DISABLE且BY5GCNRI参数为DISABLE时，根据FORCED参数选择策略接口，需要配置FORCED参数。 |
| BYIWKUEN5GR4G | 非5G终端4G接入按5GS互操作指示选择策略接口开关 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于配置非5G终端4G接入时是否按5GS互操作指示的取值来选择策略接口。"5GS互操作指示"指示S5/S8接口的“5GS Interworking Indication”参数。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLICYMODE查询当前参数配置值。<br>配置原则：<br>本参数仅控制非5G终端4G接入场景，当本参数为ENABLE时，当对端携带“5GS Interworking Indication”参数为1时，选择Npcf接口；当对端携带“5GS Interworking Indication”参数为0，或者对端未携带“5GS Interworking Indication”参数时，选择Gx接口。<br>本参数为DISABLE且BY5GCNRI参数为DISABLE时，根据FORCED参数选择策略接口，需要配置FORCED参数。 |
| FORCED | 指定策略接口 | 可选必选说明：该参数在"TMACCTYPE"配置为"RAT2G"、"RATNBIOT"、"NON_3GPP"、"RATLTEM"、"RAT3G"时为条件必选参数。该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于指定策略接口。在参数BY5GSIWKI或者BYIWKUEN5GR4G取值为DISABLE时，按本参数的配置确定策略接口。在参数TMACCTYPE配置为RAT2G、RAT3G、RATNBIOT、RATLTEM或者NON_3GPP时，按本参数的配置确定策略接口。<br>数据来源：全网规划<br>取值范围：<br>- “Npcf（Npcf接口）”：使用Npcf接口。<br>- “Gx（Gx接口）”：使用Gx接口<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLICYMODE查询当前参数配置值。<br>配置原则：无 |
| PCFRESELBYPCFID | 是否基于PCF实例标识决策策略接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于控制当基于用户的终端和接入类型决策出策略接口类型为“Gx（Gx接口）”时，是否再基于PCF实例标识重新决策最终策略接口类型。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLICYMODE查询当前参数配置值。<br>配置原则：<br>该参数仅在Gx模式下生效。 |
| BY5GCNRI | 按5GC无限制接入标识选择策略接口开关 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。<br>参数含义：该参数用于配置是否按5GC无限制接入标识的取值来选择计费接口。“5GC无限制接入标识”是指S11、S5/S8、S2b接口的“5GC Not Restricted Indication”参数。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLICYMODE查询当前参数配置值。<br>配置原则：<br>本参数为ENABLE时，当对端携带“5GC Not Restricted Indication”参数为1时，选择Npcf接口；当对端携带“5GC Not Restricted Indication”参数为0，或者对端未携带“5GC Not Restricted Indication”参数时，选择Gx接口。<br>本参数为DISABLE且BY5GSIWKI参数或BYIWKUEN5GR4G参数或为DISABLE时，根据FORCED参数选择策略接口，需要配置FORCED参数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POLICYMODE]] · 策略接口的选择方式（POLICYMODE）

## 使用实例

设置5G终端4G接入的策略接口为Npcf。

```
SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Npcf;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-POLICYMODE.md`
