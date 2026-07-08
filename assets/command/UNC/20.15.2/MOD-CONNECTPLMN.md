---
id: UNC@20.15.2@MMLCommand@MOD CONNECTPLMN
type: MMLCommand
name: MOD CONNECTPLMN（修改互联PLMN）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CONNECTPLMN
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
- 网络管理
- 互联PLMN管理
status: active
---

# MOD CONNECTPLMN（修改互联PLMN）

## 功能

**适用网元：SGSN、MME**

此命令用于修改配置的互联PLMN信息。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待修改的互联PLMN的移动国家号码。<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待修改的互联PLMN的移动网号码。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| MATCHIMSI | 匹配IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定除了MCC和MNC外的IMSI的字段。<br>数据来源：整网规划<br>取值范围：长度不超过10的十进制数字<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>可选必选说明：可选参数<br>参数含义：与该互联PLMN签署了漫游协议的<br>UNC<br>设备运营商（MNO/MVNO），具体含义请参见<br>“专属互连PLMN（EXCLUSIVEPLMN）”<br>参数的说明。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| SM | 是否允许SM业务 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许这个PLMN用户使用会话管理业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：建议值为<br>“YES(允许)” |
| MAXSMNUM | 最大承载数 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定根据运营商业务规划对应的每个用户最多建立的承载个数。用户请求建立的承载个数不能超过该值，超过则会建立失败。<br>前提条件：该参数在<br>“是否允许SM业务”<br>参数设置为<br>“YES(允许)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1~11<br>默认值：无<br>配置原则：建议值为11 |
| SMS | 是否允许SMS业务 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许这个PLMN用户使用短消息业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：建议值为<br>“YES(允许)” |
| SMSCR | 是否允许纠正短消息中心 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定是否允许这个PLMN用户使用纠正短消息中心业务。<br>前提条件：该参数在<br>“是否允许SMS业务”<br>参数设置为<br>“YES(允许)”<br>时生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：建议值为<br>“NO(不允许)” |
| SMSCT | 纠正后的短消息中心 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定纠正后的短消息中心。<br>前提条件：该参数在<br>“是否允许纠正短消息中心”<br>参数设置为<br>“YES(允许)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1~15位十进制数字<br>默认值：无 |
| LCS | 是否允许LCS业务 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许这个PLMN用户使用2G/3G的LCS业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：建议值为<br>“YES(允许)” |
| S5S8TYPE | 协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商在S5/S8口使用的协议类型。<br>数据来源：整网规划<br>取值范围：<br>- “GTP(GTP)”：表示S5/S8口使用GTP协议。<br>- “PMIP(PMIP)”：表示S5/S8口使用PMIP协议。<br>默认值：无<br>配置原则：建议值为<br>“GTP(GTP)”<br>说明：- SGSN使用S4接口连接SGW或MME使用S11接口连接SGW时会使用S5/S8接口。<br>- S5接口是本网SGW与本网PGW之间的逻辑接口；S8接口是本网SGW与外网PGW之间的逻辑接口。 |
| COUNTRYORAREANAME | 运营商名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定互联PLMN的运营商名称。<br>数据来源：整网规划<br>取值范围：1~50位字符串<br>默认值：无 |
| EXCLUSIVEPLMN | 专属互连PLMN | 可选必选说明：可选参数<br>可选必选说明：可选参数<br>参数含义：该参数用于指定专属互连PLMN（仅和本运营商签署漫游协议的用户）。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- UNC系统被多个运营商（MNO/MVNO）共享使用时：- 如果互联PLMN只与其中一个共享运营商（MNO/MVNO）签署了漫游协议，建议配置为“YES(是)”，“运营商标识（NOID）”参数配置为该共享运营商的标识。UNC系统将限制该互联HPLMN用户只接入该共享运营商（MNO/MVNO）的网络，不允许接入其他共享运营商网络。<br>- 除上述情况，建议配置为“NO(否)”。UNC系统将允许该互联HPLMN用户使用所有共享运营商（MNO/MVNO）的网络接入。“运营商标识（NOID）”参数配置为系统优选的共享运营商的标识，如果UE未主动选择为其提供服务的运营商，UNC系统会选择该参数指定的运营商（MNO/MVNO）为UE提供服务。如果希望互联PLMN用户只使用部分共享运营商（MNO/MVNO）的网络接入，还需要激活“WSFD-105003区域漫游限制”特性，并通过配置禁止该互联PLMN用户接入部分共享运营商（MNO/MVNO）的位置区域。<br>- UNC系统只被一个运营商（MNO）使用时，“运营商标识”参数标识只能配置为该MNO的标识：- 如果UNC系统与其它运营商的SGSN/MME共享使用RAN，即MOCN组网，并且该互联PLMN只与该MNO签署了漫游协议，没有和那些共享RAN设备的其它运营商签署漫游协议，建议配置为“YES(是)”。这样，UE在CS域也只能选择该MNO的网络进行业务，RAN为该UE选择的PS域业务运营商和CS域业务运营商一定是相同的，因此UNC不触发RAN根据UE的IMSI信息进行CS/PS协调。否则，建议配置为“NO(否)”。这样，UNC触发RAN根据UE的IMSI信息进行CS/PS协调，以保证RAN为该UE选择的PS域业务运营商和CS域业务运营商是相同的。<br>- 非MOCN组网，该参数的取值不影响UNC系统的行为，取默认值“NO(否)”即可。 |
| EMCBS | 是否允许紧急呼叫业务 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许使用紧急呼叫业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：如果不支持VOLTE紧急呼叫业务，期望在CS域做紧急呼叫时，建议配置为<br>“NO（不允许）” |
| EMGCNUMSW | 紧急号码下发开关 | 可选必选说明：可选参数<br>参数含义：该参数用来控制系统在给漫游用户发送Attach Accept、TAU Accept、RAU Accept消息时，是否将紧急号码携带在消息中发送给UE。<br>数据来源：整网规划<br>取值范围：<br>- “ON(开启)”<br>- “OFF(关闭)”<br>默认值：无<br>配置原则：当本参数设置为<br>“ON(开启)”<br>时，系统将在Attach Accept、TAU Accept、RAU Accept消息中给漫游用户发送紧急号码列表。其中，紧急号码列表来源于ADD EMGCNUM中的配置，如果ADD EMGCNUM没有配置，则不下发紧急号码。<br>说明：紧急号码下发还受其它配置（SET MMFUNC中EMNUM参数、DWORD_EX6 BIT10、DWORD_EX6 BIT11、DWORD_EX33 BIT13、DWORD_EX33 BIT12）控制，共同决策是否下发紧急号码。 |

## 操作的配置对象

- [互联PLMN（CONNECTPLMN）](configobject/UNC/20.15.2/CONNECTPLMN.md)

## 使用实例

修改移动国家码为460，移动网号为00，附加的IMSI字段为1234的互联PLMN，专属互连PLMN修改为NO：

MOD CONNECTPLMN: MCC="460", MNC="00", MATCHIMSI="1234", EXCLUSIVEPLMN=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改互联PLMN(MOD-CONNECTPLMN)_26146044.md`
