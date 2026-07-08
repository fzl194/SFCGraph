---
id: UNC@20.15.2@MMLCommand@RMV QOSCAP
type: MMLCommand
name: RMV QOSCAP（删除Non-GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSCAP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- QoS限制配置
- Non-GBR承载QoS限制
status: active
---

# RMV QOSCAP（删除Non-GBR承载QoS限制配置）

## 功能

**适用网元：MME**

该命令用于删除一条或多条QoS限制配置。

## 注意事项

- 该命令执行后立即生效。
- 同一网络内，所有MME/SGSN中的QoS限制配置数据应保持一致。
- 当UNC作为MME/SGSN网元时，对应用户群的QoS信息将会被配置中的QoS信息限制。
- 配置记录删除时，如果当前用户正在进行业务流程，配置限制不会实时生效，在当前流程结束后才会生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | RAT类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的接入类型，系统优先匹配与当前用户所处网络类型相同的配置数据，当相同RAT类型配置中不包含该用户时，再进行<br>“ALL”<br>类型的匹配。<br>数据来源：整网规划<br>取值范围：<br>- “ALL(ALL)”<br>- “GERAN(GERAN)”<br>- “UTRAN(UTRAN)”<br>- “E-UTRAN(E-UTRAN)”<br>- “NB-IoT(NB-IoT)”<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加Non-GBR承载QoS限制配置的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “HOME_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数必须先由<br>[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数必须先由<br>[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>命令定义，才能在此处引用。<br>取值范围：5～15位数字<br>默认值：无<br>说明：- IMSI前缀取决于需要使用本条QoS限制的IMSI范围。<br>- 确定IMSI前缀时应遵循最大匹配原则。例如，需要限制所有IMSI号在308010700000000~308010700099999范围内用户的QoS信息，则应配置一条IMSI前缀为“3080107000”的记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSCAP]] · Non-GBR承载QoS限制配置（QOSCAP）

## 使用实例

删除 “RAT类型” 为 “ALL” ， “用户范围” 类型为 “IMSI_PREFIX” ， “IMSI前缀” 为 “3080107000” 的QoS限制配置。

RMV QOSCAP: RATTYPE=ALL,SUBRANGE=IMSI_PREFIX,IMSIPRE="3080107000";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-QOSCAP.md`
