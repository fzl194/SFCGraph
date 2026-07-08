---
id: UNC@20.15.2@MMLCommand@ADD QOSCAPGBR
type: MMLCommand
name: ADD QOSCAPGBR（增加GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QOSCAPGBR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- QoS限制配置
- GBR承载QoS限制
status: active
---

# ADD QOSCAPGBR（增加GBR承载QoS限制配置）

## 功能

**适用网元：MME**

该命令用于增加一条GBR承载QoS限制配置记录，限制特定用户群GBR承载的EPS QoS。

当运营商希望对漫游用户等特殊群体的GBR承载应用特殊的QoS策略时，可以使用该命令对指定用户的GBR承载EPS QoS进行限制。

## 注意事项

- 本表最大记录数为1024。
- 该命令执行后对于新接入的EPS承载立即生效。如果当前用户已经激活了EPS承载，该命令的限制会在用户下一次会话管理业务流程中生效。
- 同一运营商的EPS网络内，建议所有MME/SGSN的QoS限制配置数据保持一致。
- 如果想取消对某一参数的限制，需要执行[**MOD QOSCAPGBR**](修改GBR承载QoS限制配置(MOD QOSCAPGBR)_26306028.md)命令将相应QoS参数修改为无效值。
- 该命令中关于GBR承载的QoS控制，涉及“PCC模式的本地QoS策略控制”特性（特性编号：WSFD-105105，License部件编码：LKV2NQOS01），执行命令请使用[**DSP LICENSE**](../../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的接入类型，系统优先匹配与当前用户所处网络类型相同的配置数据，当相同RAT类型配置中不包含该用户时，再进行“ALL”类型的匹配。<br>数据来源：整网规划<br>取值范围：<br>- “ALL(ALL)”<br>- “GERAN(GERAN)”<br>- “UTRAN(UTRAN)”<br>- “E-UTRAN(E-UTRAN)”<br>- “NB-IoT(NB-IoT)”<br>默认值：ALL(ALL) |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待增加GBR承载QoS限制配置的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX(IMSI前缀)”<br>- “HOME_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “ALL_USER(所有用户)”<br>默认值：IMSI_PREFIX(IMSI前缀)<br>说明：该功能为预留功能，暂未实现。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254。<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。说明：该功能为预留功能，暂未实现。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据对用户的IMSI进行匹配，从而区分不同的用户群。<br>数据来源：整网规划<br>取值范围：5~15位数字<br>默认值：无<br>配置原则：<br>- IMSI前缀取决于需要使用本条QoS限制的IMSI范围。<br>- 确定IMSI前缀时应遵循最大匹配原则。例如，对于IMSI号在308010700000000~308010700099999范围内的用户都需要将QoS信息限制为某一组数值，则应配置一条IMSI前缀为“3080107000”的记录。<br>- 当IMSI符合多条QoS限制配置的IMSI前缀时，采用匹配位数最多的记录。例如：用户IMSI号为308010700000001，有2条QoS限制配置的IMSI前缀分别为“30801”和“3080107”，则采用“3080107”的记录。 |
| GBRQCI | QCI（GBR承载） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的QCI限制。<br>数据来源：整网规划<br>取值范围：1~4<br>默认值：无<br>说明：如果网络下发扩展QCI，系统按照网络侧提升了QoS处理，即按照<br>“网络提升GBR承载QoS”<br>的取值来处理。 |
| GBRMBRULK | 上行最大速率 （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的上行最大速率限制。<br>数据来源：整网规划<br>取值范围：1~65000000<br>默认值：无<br>说明：如果同时配置了<br>“上行最大速率（kbps）”<br>和<br>“上行保证速率（kbps）”<br>，<br>“上行最大速率（kbps）”<br>应该大于等于<br>“上行保证速率 （kbps）”<br>。 |
| GBRMBRDLK | 下行最大速率 （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的下行最大速率限制。<br>数据来源：整网规划<br>取值范围：1~65000000<br>默认值：无<br>说明：如果同时配置了“下行最大速率 （kbps）”和“下行保证速率 （kbps）”，“下行最大速率 （kbps）”应该大于等于“下行保证速率 （kbps）”。 |
| GBRGBRULK | 上行保证速率 （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的上行保证速率限制。<br>数据来源：整网规划<br>取值范围：1~65000000<br>默认值：无<br>说明：如果同时配置了“上行最大速率 （kbps）”和“上行保证速率 （kbps）”，“上行最大速率 （kbps）”应该大于等于“上行保证速率 （kbps）”。 |
| GBRGBRDLK | 下行保证速率 （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的下行保证速率限制。<br>数据来源：整网规划<br>取值范围：1~65000000<br>默认值：无<br>说明：如果同时配置了“下行最大速率 （kbps）”和“下行保证速率 （kbps）”，“下行最大速率 (kbps)”应该大于等于“下行保证速率 （kbps）”。 |
| GBRARPPRL | ARP的优先级别（GBR承载） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的ARP优先级别限制。<br>数据来源：整网规划<br>取值范围：1~15<br>默认值：无<br>说明：取值越小，优先级越高。 |
| GBRARPPCI | ARP的抢占能力（GBR承载） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的ARP抢占能力限制。<br>数据来源：整网规划<br>取值范围：<br>- “ENABLE（启用）：允许该承载抢占其他ARP的优先级别较低的承载的资源。”<br>- “DISABLE（未启用）：不允许该承载抢占其他ARP的优先级别较低的承载的资源。”<br>默认值：无 |
| GBRARPPVI | ARP的被抢占能力（GBR承载） | 可选必选说明：可选参数<br>参数含义：ARP的被抢占能力(GBR承载)。该参数用于指定系统对用户GBR承载的ARP被抢占能力限制。<br>数据来源：整网规划<br>取值范围：<br>- “ENABLE（启用）：允许其他优先级别较高的承载抢占该承载的资源。”<br>- “DISABLE（未启用）：不允许其他优先级别较高的承载抢占该承载的资源。”<br>默认值：无 |
| GBRCTRLNWQOS | 网络提升GBR承载QoS | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>UNC<br>接收到网络下发的GBR承载QoS参数超出限制时的处理方法。<br>数据来源：整网规划<br>取值范围：<br>- “RESTRICT（限制QoS）：使用限制后的QoS进行相应的流程。”<br>- “REJECT（拒绝）：拒绝相关的业务流程。”<br>默认值：RESTRICT（限制QoS） |
| GBRREJNASCAUSE | 拒绝GBR承载建立/修改NAS原因值 | 可选必选说明：可选参数<br>参数含义：该参数指定了系统因为QoS限制拒绝UE请求的GBR承载资源建立/修改时使用的NAS原因值。<br>前提条件：该参数在<br>“网络提升GBR承载QoS”<br>参数设置为<br>“REJECT（拒绝）”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1~127<br>默认值：37<br>说明：- 系统作为MME，在发送给UE的Bearer Resource Allocatio/Modification Reject消息的ESM Cause信元中携带该原因值，请参见3GPP TS 24.301。 |
| GBRGTPCREJCAUSE | 拒绝GBR承载建立/修改GTPC原因值 | 可选必选说明：可选参数<br>参数含义：该参数指定了系统因为QoS限制拒绝网络侧请求的GBR承载建立/修改时使用的GTPC原因值。<br>前提条件：该参数在<br>“网络提升GBR承载QoS”<br>参数设置为<br>“REJECT（拒绝）”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1~255<br>默认值：88<br>说明：系统作为MME/SGSN，在发送给S-GW/P-GW的Create/Update Bearer Response消息的Cause信元中携带该原因值，请参见3GPP TS 29.274。 |
| MNNAME | 移动网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网络名称。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSCAPGBR]] · GBR承载QoS限制配置（QOSCAPGBR）

## 使用实例

增加一条GBR承载QoS限制配置，对于RAT类型为ALL、IMSI前缀为3080107000（即IMSI号范围在308010700000000~308010700099999内）的用户，将GBRQCI限制为3，上行最大速率限制为10000kbps，下行最大速率限制为20000kbps，上行保证速率限制为5000kbps，下行保证速率限制为10000kbps，ARP的优先级别（GBR承载）限制为10，ARP的抢占能力（GBR承载）限制为DISABLE，ARP的被抢占能力（GBR承载）限制为ENABLE，网络提升GBR承载QoS设置为RESTRICT（限制QoS），移动网络名称设置为MobileNet1。

ADD QOSCAPGBR: RATTYPE=ALL, IMSIPRE="3080107000", GBRQCI=3, GBRMBRULK=10000, GBRMBRDLK=20000, GBRGBRULK=5000, GBRGBRDLK=10000, GBRARPPRL=10, GBRARPPCI=DISABLE, GBRARPPVI=ENABLE, GBRCTRLNWQOS=RESTRICT, MNNAME="MobileNet1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GBR承载QoS限制配置(ADD-QOSCAPGBR)_26146216.md`
