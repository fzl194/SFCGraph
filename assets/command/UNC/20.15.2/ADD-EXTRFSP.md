---
id: UNC@20.15.2@MMLCommand@ADD EXTRFSP
type: MMLCommand
name: ADD EXTRFSP（增加扩展RFSP策略组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: EXTRFSP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 2049
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- RFSP管理
- 扩展RFSP策略管理
status: active
---

# ADD EXTRFSP（增加扩展RFSP策略组成员）

## 功能

**适用网元：SGSN、MME**

该命令用于为扩展RFSP策略组增加一条策略。使用扩展RFSP策略就是根据终端移动行为等更精细化地为用户指定不同的RFSP ID。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2049。
- 只允许添加一条“ARETYPE（区域类型）”为“TAGP(跟踪区群组)”的记录。
- 当“ARETYPE（区域类型）”为“ENBGP(eNodeB Group)”时只允许添加“类型”为“INSIDE(内部)”类型的eNodeB群组。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该扩展RFSP策略的类型。<br>数据来源：整网规划<br>取值范围：<br>- “SPEC_MOVE_SUB(指定的移动用户)”<br>默认值：无<br>说明：SPEC_MOVE_SUB(指定的移动用户)：该扩展RFSP策略适用于从指定跟踪区范围移出的用户。指定的跟踪区范围通过“TAGPID（跟踪区群组标识）”参数配置。 |
| ARETYPE | 区域类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定扩展RFSP策略控制区域范围类型。<br>前提条件：该参数在“TYPE（类型）”参数配置为“SPEC_MOVE_SUB(指定的移动用户)”后生效。<br>数据来源：整网规划<br>取值范围：<br>- “TAGP(跟踪区群组)”<br>- “ENBGP(eNodeB群组)”<br>默认值：TAGP(跟踪区群组)<br>配置原则：<br>- TAGP(跟踪区群组)：用来配置用户从指定跟踪区范围移出时的扩展RFSP策略；<br>- ENBGP(eNodeB群组)：用来配置用户在指定eNodeB覆盖范围内长时间驻留时的扩展RFSP策略。 |
| TAGPID | 跟踪区群组标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>前提条件：该参数在<br>“ARETYPE（区域类型）”<br>参数配置为<br>“TAGP(跟踪区群组)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无<br>配置原则：<br>- 该参数需要已经通过[**ADD TAGP**](../../跟踪区管理/跟踪区群组管理/增加TA群组(ADD TAGP)_26145580.md)配置。 |
| ENBGPID | eNodeB群组标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>前提条件: 该参数在<br>“ARETYPE（区域类型）”<br>参数配置为<br>“ENBGP(eNodeB群组)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无<br>配置原则：<br>- 该参数需要已经通过[**ADD ENBGP**](../../eNodeB管理/eNodeB群组管理/增加eNodeB群组(ADD ENBGP)_26145606.md)配置。 |
| TRFSP | 目标RFSP | 可选必选说明：必选参数<br>参数含义：该参数用于指定目标RFSP ID。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无<br>配置原则：<br>- 1~128为运营商自定义值。<br>- 129~256为协议(3GPP TS 36.300)指定值，其中256表示的优先级从高到低为：E-UTRAN，UTRAN，GERAN。255表示的优先级从高到低为：UTRAN，GERAN，E-UTRAN。254表示的优先级从高到低为：GERAN，UTRAN，E-UTRAN。<br>说明：目标RFSP的用途，详见<br>[表1](#ZH-CN_MMLREF_0000001126145536__tab1)<br>。 |
| RFSPRC | 目标RFSP重发次数 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定重复下发目标RFSP ID的次数。<br>前提条件：该参数在<br>“ARETYPE（区域类型）”<br>参数配置为<br>“TAGP(跟踪区群组)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~10<br>默认值：2<br>配置原则：<br>- 当用户通过TAU流程从指定的跟踪区群组覆盖的区域移出导致MME向eNodeB下发“TRFSP（目标RFSP）”后，如果UE在此区域外从IDLE态通过Service Request或TAU流程进入到Connect态时，终端自动清除之前从eNodeB接收到的“TRFSP（目标RFSP）”对应的专有优先级信息；为了避免上述问题，需要设置此参数来实现在后续流程中的重发“TRFSP（目标RFSP）”。<br>说明：MME将会在TAU和Service Request流程中重发<br>“TRFSP（目标RFSP）”<br>；当重发时，MME将不考虑UE当前是否处于该跟踪区群组覆盖范围。 |
| SEND_CTRL | 目标RFSP发送抑制 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置在低速检测区是否针对目标RFSP的下发次数进行抑制。<br>前提条件：该参数在<br>“ARETYPE（区域类型）”<br>参数配置为<br>“ENBGP(eNodeB群组)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：NO(否)<br>说明：当需要抑制迁出RFSP下发次数，从而减少用户频繁在检测区和周边网络切换时，将该参数设置为<br>“YES(是)”<br>。 |
| CTRL_PERIOD | 抑制周期 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置控制目标RFSP发送次数时间周期。<br>前提条件：该参数在<br>“SEND_CTRL(目标RFSP发送抑制)”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：本端规划<br>取值范围：10min~120min<br>默认值：无 |
| RFSPSNDCUNT | 抑制周期内目标RFSP重发次数 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置在“抑制周期”设定的时间内最大下发迁出RFSP次数。<br>前提条件：该参数在<br>“SEND_CTRL(目标RFSP发送抑制)”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~10<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EXTRFSP]] · 扩展RFSP策略组成员（EXTRFSP）

## 使用实例

运营商定义扩展RFSP策略组策略：希望针对指定的移动用户，从跟踪区群组“1”所在的跟踪区移出时，为该用户下发RFSP ID为“2”对应的频点优先级，指示用户按下发的频点优先级重新接入。

ADD EXTRFSP: TYPE=SPEC_MOVE_SUB, TAGPID=1, TRFSP=2;

运营商定义扩展RFSP策略组策略：希望针对指定的移动用户，在低速区域eNodeB群组“2”驻留时长超过阈值时，为该用户下发RFSP ID为“3”对应的频点优先级，指示用户迁出低速区域eNodeB群组。

ADD EXTRFSP: TYPE=SPEC_MOVE_SUB, ARETYPE=ENBGP, ENBGPID=2, TRFSP=3;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-EXTRFSP.md`
