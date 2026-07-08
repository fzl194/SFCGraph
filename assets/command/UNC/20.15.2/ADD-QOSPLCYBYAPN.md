---
id: UNC@20.15.2@MMLCommand@ADD QOSPLCYBYAPN
type: MMLCommand
name: ADD QOSPLCYBYAPN（增加基于APN的QoS策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QOSPLCYBYAPN
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
- 基于APN的QOS策略
status: active
---

# ADD QOSPLCYBYAPN（增加基于APN的QoS策略）

## 功能

**适用网元：MME**

该命令用于增加一条QoS策略配置，制定特定用户群基于APN的QoS策略。

## 注意事项

- 该命令执行后对于新接入的EPS承载立即生效。如果当前用户已经激活了EPS承载，该命令的限制会在用户下一次会话管理业务流程中生效。
- 本命令最大记录数为1024。
- 当“用户范围”设置为“IMSI_PREFIX（指定IMSI前缀）”，使用时按照IMSI最长匹配进行查询，相同IMSI前缀的“APNNI（APNNI）”配置不能相同。在IMSI最长匹配的记录中，如果有“APNNI（APNNI）”匹配的记录，使用该记录的配置；如果没有“APNNI（APNNI）”匹配的记录，则查找IMSI次长匹配的记录。如果IMSI和APNNI的组合同时匹配到多条记录，“IMSI前缀”长度不相等时，使用“IMSI前缀”最长匹配的记录；“IMSI前缀”长度相等时，使用“APNNI”非*的记录。例如用户123030000000001使用HUAWEI1.COM，在[表1 示例1](#ZH-CN_TOPIC_0000001388832402__tab2)所示场景下，匹配到记录2；在[表2 示例2](#ZH-CN_TOPIC_0000001388832402__tab3)所示场景下，匹配到记录1；在[表3 示例3](#ZH-CN_TOPIC_0000001388832402__table157452305619)所示场景下，匹配到记录2。
  *表1 示例1*

  | 记录 | 用户范围 | IMSI前缀 | APNNI | APNNI |
  | --- | --- | --- | --- | --- |
  | 记录1 | “IMSI_PREFIX（指定IMSI前缀）” | 12303 | HUAWEI1.COM | HUAWEI1.COM |
  | 记录2 | “IMSI_PREFIX（指定IMSI前缀）” | 123030000000001 | * | * |
  *表2 示例2*

  | 记录 | 用户范围 | IMSI前缀 | APNNI | APNNI |
  | --- | --- | --- | --- | --- |
  | 记录1 | “IMSI_PREFIX（指定IMSI前缀）” | 123030000000001 | HUAWEI1.COM | HUAWEI1.COM |
  | 记录2 | “IMSI_PREFIX（指定IMSI前缀）” | 123030000000001 | * | * |
  *表3 示例3*

  | 记录 | 用户范围 | IMSI前缀 | APNNI | APNNI |
  | --- | --- | --- | --- | --- |
  | 记录1 | “IMSI_PREFIX（指定IMSI前缀）” | 123030000000001 | HUAWEI2.COM | HUAWEI2.COM |
  | 记录2 | “IMSI_PREFIX（指定IMSI前缀）” | 12303 | HUAWEI1.COM | HUAWEI1.COM |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | RAT类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的接入类型，系统优先匹配与当前用户所处网络类型相同的配置数据，当相同RAT类型配置中不包含该用户时，再进行<br>“ALL”<br>类型的匹配。<br>数据来源：整网规划<br>取值范围：<br>- “ALL(ALL)”<br>- “GERAN(GERAN)”<br>- “UTRAN(UTRAN)”<br>- “E-UTRAN(E-UTRAN)”<br>- “NB-IoT(NB-IoT)”<br>默认值：<br>“E-UTRAN(E-UTRAN)” |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定基于APN的QoS策略配置的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX(指定IMSI前缀)”：指网络中与指定的IMSI前缀匹配的用户。<br>- “HOME_USER(本网用户)”：指网络中的本网签约用户。<br>- “FOREIGN_USER(外网用户)”：指网络中的漫游用户。<br>- “ALL_USER(所有用户)”：指网络中的所有用户。<br>默认值：<br>“IMSI_PREFIX(指定IMSI前缀)”<br>配置原则：<br>- “SUBRANGE（用户范围）”的优先级从高到低为：“IMSI_PREFIX（指定IMSI前缀）”，“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”，“ALL_USER（所有用户）”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>对于外网用户，该参数用于指定与互联PLMN签订漫游协议的本局运营商标识，对于本网用户，该参数是本网用户对应的运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254。<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定进行匹配的IMSI前缀。系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 符号“*”表示通配符，即不限制APNNI。 如果APNNI为“*”，表示该记录适用于所有的APNNI，否则该记录适用于指定的APNNI记录。 |
| NONGBRPLCY | NonGBR承载QOS是否受本地策略控制 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户QOS是否受<br>[**ADD QOSCAP**](../Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>配置控制。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)”<br>说明：运营商希望部分用户不受<br>[**ADD QOSCAP**](../Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>控制时，可以将该参数配置为<br>“NO（否）”<br>，例如对所有漫游用户QOS做限制，但是不希望对VoLTE的业务做限制。<br>[**ADD QOSCAP**](../Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>配置的<br>“UEAMBRULK”<br>和<br>“UEAMBRDLK”<br>不受此参数影响。 |
| QCIPLCY | 基于QCI的QOS是否受本地策略控制 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户QOS是否受<br>[**ADD QOSCAPBYQCI**](../基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md)<br>配置控制。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)”<br>说明：运营商希望部分用户不受<br>[**ADD QOSCAPBYQCI**](../基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md)<br>控制时，可以将该参数配置为<br>“NO（否）”<br>，例如对所有漫游用户QOS做限制，但是不希望对VoLTE的业务做限制。 |
| GBRPLCY | GBR承载QOS是否受本地策略控制 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户QOS是否受<br>[**ADD QOSCAPGBR**](../GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md)<br>配置控制。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)”<br>说明：运营商希望部分用户不受<br>[**ADD QOSCAPGBR**](../GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md)<br>控制时，可以将该参数配置为<br>“NO（否）”<br>，例如对所有漫游用户QOS做限制，但是不希望对VoLTE的业务做限制。 |
| REJSPECQCI | 是否控制特定QCI的专载建立 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户是否拒绝某一特定QCI的专载建立。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：运营商希望拒绝特定QCI（如QCI=2）的专载建立时，可以将该参数配置为<br>“YES(是)”<br>。<br>该参数仅用于测试场景，不建议现网使用。如需使用该功能，请联系华为技术支持。 |
| QCI | QCI值 | 可选必选说明：条件必选参数<br>参数含义：该参数表示用户请求或网关下发的GBR承载的QCI。<br>前提条件：该参数在<br>“REJSPECQCI（是否控制特定QCI的专载建立）”<br>配置为<br>“YES（是）”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~4<br>默认值：无 |
| GBRREJNASCAUSE | 拒绝GBR承载建立NAS原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数指定了系统因为QoS策略拒绝UE请求的GBR承载资源建立时使用的NAS原因值。<br>前提条件：该参数在<br>“REJSPECQCI（是否控制特定QCI的专载建立）”<br>配置为<br>“YES（是）”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~127<br>默认值：37<br>说明：系统作为MME，在发送给UE的Bearer Resource Allocation Reject消息的ESM Cause信元中携带该原因值，请参见3GPP TS 24.301。 |
| GBRGTPCREJCAUSE | 拒绝GBR承载建立GTPC原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数指定了系统因为QoS策略拒绝网络侧请求的GBR承载建立时使用的GTPC原因值。<br>前提条件：该参数在<br>“REJSPECQCI（是否控制特定QCI的专载建立）”<br>配置为<br>“YES（是）”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~255<br>默认值：88<br>说明：系统作为MME，在发送给S-GW/P-GW的Create Bearer Response消息的Cause信元中携带该原因值，请参见3GPP TS 29.274。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSPLCYBYAPN]] · 基于APN的QoS策略（QOSPLCYBYAPN）

## 使用实例

增加一条基于APN的QoS策略配置，对于 “RAT类型” 为 “E-UTRAN” ， “用户范围” 为 “IMSI_PREFIX” ， “IMSI前缀” 为 “3080107000” （即IMSI号范围在308010700000000~308010700099999内）， “APNNI” 为 “HUAWEI1.COM” 的用户，设置其QoS不受 [**ADD QOSCAP**](../Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) 、 [**ADD QOSCAPBYQCI**](../基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) 、 [**ADD QOSCAPGBR**](../GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) 的控制，且不允许建立 “QCI” 为 “2” 的专载。

```
ADD QOSPLCYBYAPN: RATTYPE=E-UTRAN, SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000", APNNI="HUAWEI1.COM", NONGBRPLCY=NO, QCIPLCY=NO, GBRPLCY=NO, REJSPECQCI=YES, QCI=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-QOSPLCYBYAPN.md`
