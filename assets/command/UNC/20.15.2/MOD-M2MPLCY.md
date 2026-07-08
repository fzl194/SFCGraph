---
id: UNC@20.15.2@MMLCommand@MOD M2MPLCY
type: MMLCommand
name: MOD M2MPLCY（修改M2M策略参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: M2MPLCY
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
- 业务安全管理
- M2M管理
- M2M策略参数配置
status: active
---

# MOD M2MPLCY（修改M2M策略参数）

## 功能

**适用网元：SGSN、MME**

该命令用于修改M2M的策略参数。

## 注意事项

该命令执行后对已经附着的用户不立即生效。用户下次RAU/TAU流程再生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待修改M2M策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>说明：当存在多条记录时，首先匹配<br>“IMSI_PREFIX（指定IMSI前缀）”<br>的记录，其次匹配<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>的记录，最后匹配<br>“ALL_USER（所有用户）”<br>的记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无<br>说明：当该参数配置生效时，按照IMSI最长匹配进行查询，如果有<br>“APNNI（APNNI）”<br>匹配的记录，使用该记录的配置；如果没有<br>“APNNI（APNNI）”<br>匹配的记录，则查找IMSI次长匹配的记录。 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：全网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 符号“*”表示通配符，即不限制APNNI。 如果APNNI为“*”，表示该记录适用于所有的APNNI，否则该记录适用于指定的APNNI记录。<br>- 相同IMSI前缀的不同记录中“APNNI（APNNI）”配置不能相同。<br>- 当系统识别到UE支持“长周期RAU定时器”时，使用用户签约的“APNNI”进行匹配，若签约的“APNNI”匹配到多条记录，随机选择其中一条记录；若没有匹配到记录，使用“APNNI”为“*”的记录。<br>- 当系统识别到UE支持“长周期TAU定时器”、“PSM”、“eDRX”或者“NBIOT(CP优化)”时，使用用户实际使用的“APNNI”进行匹配，若用户为多PDN场景且使用的“APNNI”匹配到多条记录，随机选择其中一条记录；若没有匹配到记录，使用“APNNI”为“*”的记录<br>- 不支持输入*和其他字符组合。 |
| RAUTAUTMRSRC | 长周期RAU或TAU定时器来源 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在Attach /TAU /RAU流程中使用的长周期RAU或TAU定时器来源。<br>数据来源：全网规划<br>取值范围：<br>- “USE_CONFIG（使用配置）”：表示使用“长周期RAU或TAU定时器时长（小时）”参数配置值。<br>- “UE_REQUEST_PREFER（UE请求优先）”：表示优先使用Attach Request/TAU Request/RAU Request中携带的T3412 extended value，如果未携带该信元，使用“长周期RAU或TAU定时器时长（小时）”参数配置值。<br>默认值：无 |
| LONGRAUTAUTMR | 长周期RAU或TAU定时器时长（小时） | 可选必选说明：可选参数<br>参数含义：该参数用于指定长周期RAU/TAU定时器时长。<br>数据来源：全网规划<br>取值范围：0～10000<br>默认值：无<br>说明：- 该参数配置为0，且“长周期RAU或TAU定时器来源”参数配置为USE_CONFIG表示长周期性定时器不生效。<br>- 该参数配置为0，且“长周期RAU或TAU定时器来源”参数配置为UE_REQUEST_PREFER，UE未在Attach Request/TAU Request/RAU Request消息中携带T3412 extended value时，长周期性定时器不生效。<br>- 终端在Attach Request/TAU Request/RAU Request消息中通过MS network feature support IE的extended periodic timer bit位指示支持长周期定时器，MME/SGSN在Attach Accept/TAU Accept/RAU Accept消息中携带extended periodic timer。<br>- extended periodic timer主要用于M2M领域，可节省终端电池消耗，降低对网络的信令负荷。 |
| PSMSW | PSM开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启支持终端省电PSM模式。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”<br>- “ON （打开）”<br>默认值: 无<br>配置原则：<br>当运营商需要部署“WSFD-<br>215001<br>终端省电PSM模式”特性或“WSFD-<br>216001<br>eMTC终端省电PSM模式”特性时，需要将该参数设置为<br>“ON（打开）”<br>。<br>说明：- 此参数与“WSFD-215001终端省电PSM模式”特性License（部件编码：LKV2M2MS01）共同作用开启“WSFD-215001终端省电PSM模式”特性。<br>- 此参数与“WSFD-216001eMTC终端省电PSM模式”特性License（部件编码：LKV2M2MS02）共同作用开启“WSFD-216001eMTC终端省电PSM模式”特性。<br>当开关为<br>“ON （打开）”<br>时，请确保对应的license已经申请并激活，License控制开关已开启。 |
| ACTIVETIMERSRC | Active Timer来源 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定在Attach /TAU流程中使用的Active Timer取值来源。<br>前提条件：该参数在"PSM 开关"参数配置为"打开"后生效。<br>数据来源：全网规划<br>取值范围：<br>- “USE_CONFIG（使用配置）”：表示使用“Active Timer定时器时长(秒)”参数配置值。<br>- “USE_UE_REQUEST（使用UE请求）”：表示使用UE请求。<br>- “USE_MAXRSPTM（UE可达订阅优先）”：表示使用来自HSS的UE可达订阅请求消息携带的Maximum Response Time作为Active Timer时长。如果不存在，若软参DWORD_EX18 BIT8为1则使用来自HSS的Active-Time作为Active Timer时长；若Maximum Response Time和Active-Time均不存在或Maximum Response Time不存在且软参DWORD_EX18 BIT8为0，则使用“Active Timer定时器时长(秒)”参数配置值。<br>- “USE_MAXRSPTM_OR_UEREQ（UE可达订阅优先，UE请求次优）”：表示优先使用来自HSS的UE可达订阅请求消息携带的Maximum Response Time作为Active Timer时长；如果不存在，若软参DWORD_EX18 BIT8为1则使用来自HSS的Active-Time作为Active Timer时长；若Maximum Response Time和Active-Time均不存在或Maximum Response Time不存在且软参DWORD_EX18 BIT8为0，则使用Attach Request/TAU Request消息中携带的T3324信元值。<br>默认值: 无<br>说明：MME最终下发的Active Timer定时器时长不大于Periodic TAU Timer (T3412/T3412 extended)转化为秒之后的时长。 |
| ACTIVETIMER | Active Timer定时器时长（秒） | 可选必选说明：条件可选参数。<br>参数含义：该参数用于指定Active Timer定时器时长。<br>前提条件：该参数在"Active Timer来源"参数配置为"使用配置"或"UE可达订阅优先"后生效。<br>数据来源：全网规划<br>取值范围：0～11160<br>默认值: 无<br>配置原则：<br>- Active Timer定时器时长必须小于Periodic TAU Timer (T3412/T3412 extended)转化为秒之后的时长。<br>- Active timer表示M2M终端进入Idle模式后持续多长时间进入PSM(Power Saving Mode)状态。该时间越长，M2M终端越耗电。<br>说明：- 当参数取值为1的时候，在Attach Accept/Tau Accept消息中携带给UE的“Active Timer定时器”值为1，单位：2s。<br>- 当参数取值范围0,2～63：在Attach Accept/Tau Accept消息中携带给UE的“Active Timer定时器”是X/2向下取整，单位：2s。X即0，或2~63之间的取值。<br>- 当参数取值范围64~1919：在Attach Accept/Tau Accept消息中携带给UE的“Active Timer定时器”是X/60向下取整，单位：min。X即64~1919之间的取值。<br>- 当参数取值范围1920~11160：在Attach Accept/Tau Accept消息中携带给UE的“Active Timer定时器”是X/360向下取整，单位：6min。X即1920~11160之间的取值。<br>- M2M终端在Attach Request/TAU Request消息中携带T3324 value IE（Active timer）表示支持PSM功能，MME则在Attach Accept/TAU Accept消息中携带Active timer。<br>- Active timer主要用于M2M领域，可节省终端电池消耗，降低对网络的信令负荷。Active timer原理参见“WSFD-215001支持终端省电PSM模式”特性描述。 |
| DELAYSEND | 延迟发送 | 可选必选说明：条件可选参数。<br>参数含义：该参数用于指定当UE进入PSM状态后，在收到来自S-GW发送的Downlink Data Notification消息时，MME是否通过Downlink Data Notification Acknowledge消息携带DL Buffering Duration信元指示SGW缓存数据。<br>前提条件：该参数在"PSM 开关"参数配置为"打开"后生效。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：表示MME给SGW回复Downlink Data Notification Acknowledge消息携带原因值"Unable to page UE"，指示SGW丢弃数据。<br>- “YES（是）”：表示MME给SGW回复Downlink Data Notification Acknowledge消息携带DL Buffering Duration。<br>默认值: 无<br>说明：- 当软参DWORD_EX25 BIT25设置为1，且“PSM 开关”参数配置为“打开”情况下，该参数按照配置为“YES”生效。<br>- 当S-GW发送的Downlink Data Notification消息不携带EPS bearer ID信元且存在多个PDN连接时，此参数配置为“YES”不生效。 |
| EDRXSW | eDRX开关 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定是否开启支持终端省电eDRX模式。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON （打开）<br>默认值：无<br>配置原则：当运营商需要部署“WSFD-<br>215002<br>NB-IoT eDRX模式”特性或“WSFD-<br>216002<br>eMTC eDRX模式”特性时，需要将该参数设置为<br>“ON（打开）”<br>。<br>说明：- 此参数与“WSFD-215002NB-IoT eDRX模式”特性License（部件编码：LKV2EDRX01）共同作用开启“WSFD-215002NB-IoT eDRX模式”特性。<br>- 此参数与“WSFD-216002eMTC eDRX模式”特性License（部件编码：LKV2EDRX02）共同作用开启“WSFD-216002eMTC eDRX模式”特性。<br>当开关为<br>“ON （打开）”<br>时，请确保对应的license已经申请并激活，License控制开关已开启。 |
| NBECL | 窄带S1模式寻呼周期 | 可选必选说明：条件可选参数。<br>前提条件：该参数在"eDRX开关"参数配置为"打开"后生效。<br>参数含义：该参数用于指定窄带S1模式寻呼时间周期。<br>数据来源：全网规划<br>取值范围：<br>- USE_UE_REQUEST（使用UE请求值）：使用UE请求值。<br>- SECONDS_20_48（20.48秒）：20.48秒。<br>- SECONDS_40_96（40.96秒）：40.96秒。<br>- SECONDS_81_92（81.92秒）：81.92秒。<br>- SECONDS_163_84（163.84秒）：163.84秒。<br>- SECONDS_327_68（327.68秒）：327.68秒。<br>- SECONDS_655_36（655.36秒）：655.36秒。<br>- SECONDS_1310_72（1310.72秒）：1310.72秒。<br>- SECONDS_2621_44（2621.44秒）：2621.44秒。<br>- SECONDS_5242_88（5242.88秒）：5242.88秒。<br>- SECONDS_10485_76（10485.76秒）：10485.76秒。<br>默认值：无 |
| NBPTW | 窄带S1模式寻呼时间窗口时长 | 可选必选说明：条件可选参数。<br>前提条件：该参数在"eDRX开关"参数配置为"打开"后生效。<br>参数含义：该参数用于指定窄带S1模式寻呼时间窗口时长。<br>数据来源：全网规划<br>取值范围：<br>- USE_UE_REQUEST（使用UE请求值）：使用UE请求值。<br>- SECONDS_2_56（2.56秒）：2.56秒。<br>- SECONDS_5_12（5.12秒）：5.12秒。<br>- SECONDS_7_68（7.68秒）：7.68秒。<br>- SECONDS_10_24（10.24秒）：10.24秒。<br>- SECONDS_12_8（12.8秒）：12.8秒。<br>- SECONDS_15_36（15.36秒）：15.36秒。<br>- SECONDS_17_92（17.92秒）：17.92秒。<br>- SECONDS_20_48（20.48秒）：20.48秒。<br>- SECONDS_23_04（23.04秒）：23.04秒。<br>- SECONDS_25_6（25.6秒）：25.6秒。<br>- SECONDS_28_16（28.16秒）：28.16秒。<br>- SECONDS_30_72（30.72秒）：30.72秒。<br>- SECONDS_33_28（33.28秒）：33.28秒。<br>- SECONDS_35_84（35.84秒）：35.84秒。<br>- SECONDS_38_4（38.4秒）：38.4秒。<br>- SECONDS_40_96（40.96秒）：40.96秒。<br>默认值：无 |
| WBECL | 宽带S1模式寻呼周期 | 可选必选说明：条件可选参数。<br>前提条件：该参数在"eDRX开关"参数配置为"打开"后生效。<br>参数含义：该参数用于指定宽带S1模式寻呼时间周期。<br>数据来源：全网规划<br>取值范围：<br>- USE_UE_REQUEST（使用UE请求值）：使用UE请求值。<br>- SECONDS_5_12（5.12秒）：5.12秒。<br>- SECONDS_10_24（10.24秒）：10.24秒。<br>- SECONDS_20_48（20.48秒）：20.48秒。<br>- SECONDS_40_96（40.96秒）：40.96秒。<br>- SECONDS_61_44（61.44秒）：61.44秒。<br>- SECONDS_81_92（81.92秒）：81.92秒。<br>- SECONDS_102_4（102.4秒）：102.4秒。<br>- SECONDS_122_88（122.88秒）：122.88秒。<br>- SECONDS_143_36（143.36秒）：143.36秒。<br>- SECONDS_163_84（163.84秒）：163.84秒。<br>- SECONDS_327_68（327.68秒）：327.68秒。<br>- SECONDS_655_36（655.36秒）：655.36秒。<br>- SECONDS_1310_72（1310.72秒）：1310.72秒。<br>- SECONDS_2621_44（2621.44秒）：2621.44秒。<br>默认值：无 |
| WBPTW | 宽带S1模式寻呼时间窗口时长 | 可选必选说明：条件可选参数。<br>前提条件：该参数在"eDRX开关"参数配置为"打开"后生效。<br>参数含义：该参数用于指定宽带S1模式寻呼时间窗口时长。<br>数据来源：全网规划<br>取值范围：<br>- USE_UE_REQUEST（使用UE请求值）：使用UE请求值。<br>- SECONDS_1_28（1.28秒）：1.28秒。<br>- SECONDS_2_56（2.56秒）：2.56秒。<br>- SECONDS_3_84（3.84秒）：3.84秒。<br>- SECONDS_5_12（5.12秒）：5.12秒。<br>- SECONDS_6_4（6.4秒）：6.4秒。<br>- SECONDS_7_68（7.68秒）：7.68秒。<br>- SECONDS_8_96（8.96秒）：8.96秒。<br>- SECONDS_10_24（10.24秒：10.24秒）。<br>- SECONDS_11_52（11.52秒）：11.52秒。<br>- SECONDS_12_8（12.8秒）：12.8秒。<br>- SECONDS_14_08（14.08秒）：14.08秒。<br>- SECONDS_15_36（15.36秒）：15.36秒。<br>- SECONDS_16_64（16.64秒）：16.64秒。<br>- SECONDS_17_92（17.92秒）：17.92秒。<br>- SECONDS_19_2（19.2秒）：19.2秒。<br>- SECONDS_20_48（20.48秒）：20.48秒。<br>默认值：无 |
| PSMANDEDRX | PSM和eDRX优先级 | 可选必选说明：条件可选参数。<br>前提条件：该参数在"eDRX开关"参数配置为"打开"后生效。<br>参数含义：该参数用于指定终端省电PSM模式和终端省电eDRX模式使用策略。<br>数据来源：全网规划<br>取值范围：<br>- “PSM_AND_EDRX(PSM和eDRX同时生效)”：PSM和eDRX同时启用。<br>- “PSM_FIRST(PSM优先)”：MME启用PSM。<br>- “EDRX_FIRST(eDRX优先)”：MME启用eDRX。<br>默认值：无<br>说明：优先级的取值必须满足MME配置同时满足启用PSM和eDRX。 |
| CPOPSW | CP优化功能 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持Control-plane CIoT EPS optimization（CP CIoT）功能。<br>数据来源：全网规划<br>取值范围：<br>- “NOT_SUPPORT(不支持)”<br>- “SUPPORT(支持)”<br>默认值：无<br>配置原则：当运营商需要部署“WSFD-<br>215101<br>基于信令面的数据传输”（特性编号：WSFD-<br>215101<br>；部件编码： LKV2DNAS01）特性时，如果规划终端支持使用CP CIoT数据传输，将此参数配置为<br>“SUPPORT(支持)”<br>，并确认特性License是否申请并激活，且License控制开关开启。 |
| UPRATECTL | CP上行数据包数 | 可选必选说明：条件可选参数<br>参数含义：该参数用于配置启用Control-plane CIoT EPS optimization（CP CIoT）功能的UE每6分钟可以传输的最大上行数据包数。<br>前提条件：该参数在"CP优化功能"参数配置为"支持"后生效。<br>数据来源：全网规划<br>取值范围：0和10～65535<br>默认值：无<br>配置原则：<br>根据3GPP 23401协议规定，网络可以对支持CP CIoT功能的UE进行数据包传输限制，限制UE每6分钟上下行单向传输的数据包数不超过网络侧配置，且取值不小于10，用以满足UE最小数据传输需求。<br>说明：- 本参数不对NAS消息传输的SMS数据包进行限制。<br>- 该参数的可配置范围为0和10~65535，10~65535为正常取值范围，当配置为0时，表示网络侧不对支持CP CIoT功能的UE进行数据包传输限制。现网设备可以视网络设备的负荷来调整该参数，当NAS消息传输的数据包对网络设备的负荷影响较大时，可以适当下调该参数，以降低网络设备负荷。<br>- “基于服务PLMN的NB-IoT终端接入速率控制”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-215205，license部件编码：LKV2SARC01 ）。<br>- 该参数修改后不立即生效，UE发起Attach或TAU流程后才可生效。 |
| DOWNRATECTL | CP下行数据包数 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制MME在Control-plane CIoT EPS optimization（CP CIoT）传输方式下每6分钟可以传输的最大下行数据包数。<br>前提条件：该参数在"CP优化功能"参数配置为"支持"后生效。<br>数据来源：全网规划<br>取值范围：0和10～65535<br>默认值：无<br>配置原则：<br>根据3GPP 23401协议规定，网络可以对支持CP CIoT功能的UE进行数据包传输限制，限制UE每6分钟上下行单向传输的数据包数不超过网络侧配置，且取值不小于10，用以满足UE最小数据传输需求。<br>说明：- 本参数不对NAS消息传输的SMS数据包进行限制。<br>- 该参数的可配置范围为0和10~65535，10~65535为正常取值范围，当配置为0时，表示网络侧不对支持CP CIoT功能的UE进行数据包传输限制。现网设备可以视网络设备的负荷来调整该参数，当NAS消息传输的数据包对网络设备的负荷影响较大时，可以适当下调该参数，以降低网络设备负荷。<br>- “基于服务PLMN的NB-IoT终端接入速率控制”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-215205，license部件编码：LKV2SARC01 ）。<br>- 该参数修改后不立即生效，UE发起Attach或TAU流程后才可生效。 |
| S1UCAPA | S1-U能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NB-IoT用户使用S1-U进行数据传输的能力。<br>数据来源：全网规划<br>取值范围：<br>- “NOT_SUPPORT（不支持）”：不支持S1-U数据传输和UP CIoT。<br>- “SUPPORT_S1UDATA（支持S1-U数据传输）”：仅支持S1-U数据传输。<br>- “SUPPORT_S1UDATA_AND_UP（支持S1-U数据传输和UP CIoT）”：支持S1-U数据传输和UP CIoT<br>默认值： 无 |
| SGSSMSSW | SGs短信开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启非联合附着的SGs短信。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”<br>- “ON（打开）”<br>默认值：无<br>配置原则： 当运营商需要部署“NB-IoT基于SGs接口的短消息”特性时，需要将该参数设置为“ON（打开）”。该参数与该特性license共同完成特性的开启（特性编号：WSFD-<br>215104<br>，License部件编码：LKV2GSDT01）。<br>说明：该参数受软参DWORD_EX28 BIT16控制，如该软参设置为1，非联合附着条件下的基于SGs接口短消息业务功能直接生效。 |
| SIGCTRLSW | 信令控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启信令控制功能。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”<br>- “ON（打开）”<br>默认值：无 |
| SIGCTRLINDEX | 信令控制索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定M2M信令控制配置的索引。<br>前提条件：该参数在"信令控制开关"参数配置为"打开"后生效。<br>数据来源：本端规划<br>取值范围：0～31<br>默认值：无 |
| CP2UPBYPKGNUM | CP数传包个数过载门限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CP CIoT模式下用户的最大数传包传输个数。当CP CIoT模式下数传包个数大于参数值后，由MME发起CP CIoT到UP CIoT的切换流程。<br>数据来源：全网规划<br>取值范围：0～65535<br>默认值：无<br>说明：数传包包括UE和S-GW之间的所有数据报文。<br>以下任一条件满足时，MME就会发起CP CIoT到UP CIoT的切换流程：<br>- CP CIoT模式下数传包个数大于“CP数传包个数过载门限”<br>- CP CIoT模式下单次数传包长度大于“CP数传包大小过载门限” |
| CP2UPBYPKGLEN | CP数传包大小过载门限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CP CIoT模式下用户的最大数传包传输长度。当CP CIoT模式下单次数传包长度大于参数值后，由MME发起CP CIoT到UP CIoT的切换流程。<br>数据来源：全网规划<br>取值范围：0～2000<br>默认值：无<br>说明：数传包包括UE和S-GW之间的所有数据报文。<br>以下任一条件满足时，MME就会发起CP CIoT到UP CIoT的切换流程：<br>- CP CIoT模式下数传包个数大于“CP数传包个数过载门限”<br>- CP CIoT模式下单次数传包长度大于“CP数传包大小过载门限” |
| NBEDRXSUBPRI | 窄带EDRX寻呼周期签约优先 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示是否优先使用签约的eDRX-Cycle-Lenght-Value作为NB-IoT用户eDRX模式的寻呼周期<br>前提条件：该参数在<br>“eDRX开关”<br>参数配置为<br>“ON（打开）”<br>后生效<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：使用“窄带S1模式寻呼周期”配置值作为NB-IoT用户eDRX模式的寻呼周期。<br>- “YES（是）”：优先使用签约数据中的eDRX-Cycle-Lenght-Value作为eDRX模式的寻呼周期，签约数据中不存在eDRX-Cycle-Lenght-Value时，再使用“窄带S1模式寻呼周期”配置值作为NB-IoT用户eDRX模式的寻呼周期。<br>默认值：无 |
| WBEDRXSUBPRI | 宽带EDRX寻呼周期签约优先 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示是否优先使用签约的eDRX-Cycle-Lenght-Value作为WB用户eDRX模式的寻呼周期<br>前提条件：该参数在<br>“eDRX开关”<br>参数配置为<br>“ON（打开）”<br>后生效<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：使用“宽带S1模式寻呼周期”配置值作为WB用户eDRX模式的寻呼周期。<br>- “YES（是）”：优先使用签约数据中的eDRX-Cycle-Lenght-Value作为eDRX模式的寻呼周期，签约数据中不存在eDRX-Cycle-Lenght-Value时，再使用“宽带S1模式寻呼周期”配置值作为WB用户eDRX模式的寻呼周期。<br>默认值：无 |
| NBPTWSUBPRI | 窄带寻呼时间窗口时长签约优先 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示是否优先使用签约的Paging-Time-Window-Length作为NB-IoT用户eDRX模式的寻呼时间窗口时长。<br>前提条件：该参数在“eDRX开关”参数配置为“ON（打开）”后生效。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：使用“窄带S1模式寻呼时间窗口时长”配置值作为NB-IoT用户eDRX模式的寻呼时间窗口时长。<br>- “YES（是）”：优先使用签约数据中的Paging-Time-Window-Length作为eDRX模式的寻呼时间窗口时长，签约数据中不存在Paging-Time-Window-Length时，再使用“窄带S1模式寻呼时间窗口时长”配置值作为NB-IoT用户eDRX模式的寻呼时间窗口时长。<br>默认值：无 |
| WBPTWSUBPRI | 宽带寻呼时间窗口时长签约优先 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示是否优先使用签约的Paging-Time-Window-Length作为WB用户eDRX模式的寻呼时间窗口时长。<br>前提条件：该参数在“eDRX开关”参数配置为“ON（打开）”后生效。<br>数据来源：全网规划<br>取值范围：<br>“NO（否）”：使用“宽带S1模式寻呼时间窗口时长”配置值作为WB用户eDRX模式的寻呼时间窗口时长。<br>“YES（是）”：优先使用签约数据中的Paging-Time-Window-Length作为eDRX模式的寻呼时间窗口时长，签约数据中不存在Paging-Time-Window-Length时，再使用“宽带S1模式寻呼时间窗口时长”配置值作为WB用户eDRX模式的寻呼时间窗口时长。<br>默认值：无 |
| NBMODEDRX | NB-IoT用户支持NB-DRX | 可选必选说明：可选参数<br>参数含义：该参数表示MME是否对NB-IOT用户启用NB模式的DRX。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：<br>如果希望对NB-IOT用户使用Attach/TAU Req消息携带的“DRX parameter in NB-S1 mode”信元或者配置的DRX信元时，设置为“YES”。 |
| NBDRX | NB模式的DRX值 | 可选必选说明：条件可选参数。<br>前提条件：该参数在" NB-IoT用户支持NB-DRX "参数配置为"是"后生效。<br>参数含义：该参数用于指定NB模式的DRX值。<br>数据来源：全网规划<br>取值范围：<br>- “USE_UE_REQUEST（使用UE请求值）”<br>- “T_32（32）”<br>- “T_64 （54）”<br>- “T_128（128）”<br>- “T_256（256）”<br>- “T_512（512）”<br>- “T_1024（1024）”<br>默认值：无 |
| NBSGSSMSSUB | SGs短信签约判断 | 可选必选说明：可选参数<br>参数含义：该参数用于SGs短信功能开启时，在NB-IoT非联合附着/TAU流程中是否对签约Network Access Mode进行判断。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：<br>如果希望NB-IoT非联合附着/TAU的SGs短信功能生效，需要检查签约中Network Access Mode信元为PACKET_AND_CIRCUIT，设置为<br>“YES（是）”<br>。<br>说明：本参数在<br>“SGs短信开关”<br>参数设置为<br>“ON（打开）”<br>或者<br>[DWORD_EX28 BIT16](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/DWORD_EX28 BIT16 控制非联合附着条件下的基于SGs接口短消息业务功能是否直接生效_05450941.md)<br>软参设置为<br>“1”<br>时生效。 |
| NBITRTAUSUB | NB-IOT Inter TAU签约判断 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Inter场景下，NB-IoT联合TAU接入触发SGsAP-LOCATION-UPDATE-REQUEST时，是否对签约Network Access Mode进行判断。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：<br>如果希望NB-IoT Inter联合TAU接入触发SGsAP-LOCATION-UPDATE-REQUEST时，需要检查签约中Network Access Mode信元为PACKET_AND_CIRCUIT，设置为<br>“YES（是）”<br>。<br>说明：本参数在<br>“SGs短信开关”<br>参数设置为<br>“ON（打开）”<br>或者<br>[DWORD_EX28 BIT16](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/DWORD_EX28 BIT16 控制非联合附着条件下的基于SGs接口短消息业务功能是否直接生效_05450941.md)<br>软参设置为<br>“1”<br>时生效。 |

## 操作的配置对象

- [M2M策略参数（M2MPLCY）](configobject/UNC/20.15.2/M2MPLCY.md)

## 使用实例

修改M2M策略参数，配置 “用户范围” 为 “所有用户” ， “APNNI” 为 “HUAWEI1.com” ， “长周期RAU或TAU定时器来源” 为 “USE_CONFIG” ， “长周期RAU或TAU定时器时长（小时）” 为 “22” ， “PSM开关” 为 “打开” ， “Active Timer来源” 为 “USE_CONFIG” ， “Active Timer定时器时长(秒)” 为 “60” ， “延迟发送” 为 “YES” ， “CP优化功能” 为 “不支持” ， “S1UCAPA” 为 “NOT_SUPPORT（不支持）” ， “SGs短信开关” 为 “ON（打开）” ：

MOD M2MPLCY: SUBRANGE=ALL_USER, APNNI="HUAWEI1.COM", RAUTAUTMRSRC=USE_CONFIG, LONGRAUTAUTMR=22, PSMSW=ON, ACTIVETIMERSRC=USE_CONFIG, ACTIVETIMER=60, DELAYSEND=YES, CPOPSW=NOT_SUPPORT, S1UCAPA=NOT_SUPPORT, SGSSMSSW=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改M2M策略参数(MOD-M2MPLCY)_72345365.md`
