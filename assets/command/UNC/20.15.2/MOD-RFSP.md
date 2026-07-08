---
id: UNC@20.15.2@MMLCommand@MOD RFSP
type: MMLCommand
name: MOD RFSP（修改RFSP配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: RFSP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- RFSP管理
- RFSP策略管理
- RFSP参数配置
status: active
---

# MOD RFSP（修改RFSP配置）

## 功能

**适用网元：SGSN、MME**

此命令用于修改RFSP ID的配置。

## 注意事项

- 此命令执行后立即生效。
- 此配置涉及基于SPID的UE驻留和切换策略管理特性（特性编号：WSFD-106207，license部件编码：LKV2SPID01），执行命令请使用[**LST LICENSESWITCH**](../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置RFSP ID的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_IMSI(所有用户)”<br>- “SPECIAL_IMSI(指定用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>默认值：无<br>配置原则：<br>“SUBRANGE（用户范围）”<br>的优先级从高到低为：<br>“SPECIAL_IMSI(指定用户)”<br>，<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>，<br>“ALL_IMSI(所有用户)”<br>。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户群的IMSI前缀。<br>前提条件：此参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“SPECIAL_IMSI(指定用户)”<br>时有效。<br>数据来源：整网规划<br>取值范围：5～15位数字<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：<br>该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 当用户为MNO用户时，该参数需要配置为0或128～254之间的值，该取值必须和[**ADD MNO**](../../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置的“MNOID”参数取值相同。<br>- 当用户为MVNO用户时，该参数需要配置为1～64之间的值，该取值必须和[**ADD MVNO**](../../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置的“MVNOID”参数取值相同。<br>说明：对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。对于本网用户，该参数是为该用户归属的MNO/MVNO运营商标识。 |
| RFSPSOURCE | RFSP来源 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统所使用的RFSP ID的数据来源，即使用签约数据或本地配置的“目标RFSP”。<br>数据来源：整网规划<br>取值范围：<br>- “USE_CFG(配置优先)”<br>- “SUB_FIRST(签约优先)”<br>默认值：无<br>配置原则：<br>- 本参数取值为“USE_CFG（配置优先）”时，表示无论用户是否签约RFSP ID，均使用本命令指定的RFSP ID。<br>- 本参数取值为“SUB_FIRST（签约优先）”时，表示如果用户签约RFSP ID，使用用户签约的RFSP ID，如果用户未签约RFSP ID，使用本命令指定的RFSP ID。 |
| TRFSP | 目标RFSP | 可选必选说明：必选参数<br>参数含义：该参数用于指定目标RFSP ID。<br>数据来源：整网规划<br>取值范围：0~256，65535<br>默认值：无<br>配置原则：<br>- 如果配置的目标RFSP ID值为0，则表示直接使用签约的RFSP ID值。<br>- 1~128为运营商自定义值。<br>- 129~256为协议(3GPP TS 36.300)指定值，其中256表示的优先级从高到低为：E-UTRAN，UTRAN，GERAN。255表示的优先级从高到低为：UTRAN，GERAN，E-UTRAN。254表示的优先级从高到低为：GERAN，UTRAN，E-UTRAN。<br>- 65535表示无效，即系统不为该用户使用RFSP。如果针对高速移动用户仅希望使用扩展RFSP策略，不使用其他基于RFSP的驻留和切换策略，则需要配置“Target RFSP”参数为65535。 |
| EXTPLCY | 使用扩展RFSP策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用扩展RFSP策略。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>如果需要使用扩展RFSP策略，请配置为“YES（是）”。扩展策略请通过ADD EXTRFSP命令添加。使用扩展RFSP策略，可以根据终端移动行为等更精细化地为用户指定不同的RFSP ID。<br>该参数配置为“YES（是）”：如果系统为用户匹配到了扩展RFSP策略，则使用扩展RFSP策略中指定的RFSP ID；否则，系统会使用“TRFSP（目标RFSP）”参数配置的RFSP ID。 |

## 操作的配置对象

- [RFSP配置（RFSP）](configobject/UNC/20.15.2/RFSP.md)

## 使用实例

场景参见 [**ADD RFSP**](增加RFSP配置(ADD RFSP)_26305350.md) 的命令使用实例。

1. 修改30808号段的用户RFSP ID，使该号段的用户按照RFSP ID为4对应的频点优先级进行驻留控制：
  MOD RFSP: SUBRANGE=SPECIAL_IMSI, IMSIPRE="30808", TRFSP=4;
2. 修改30808号段的用户优先使用签约的RFSP ID对应的频点优先级进行驻留控制，如果用户未签约RFSP ID，使用RFSP ID为2对应的频点优先级进行驻留控制:
  MOD RFSP: SUBRANGE=SPECIAL_IMSI, IMSIPRE="30808", RFSPSOURCE=SUB_FIRST, TRFSP=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改RFSP配置(MOD-RFSP)_26145540.md`
