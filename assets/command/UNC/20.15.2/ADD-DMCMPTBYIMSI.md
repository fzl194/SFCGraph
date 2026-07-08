---
id: UNC@20.15.2@MMLCommand@ADD DMCMPTBYIMSI
type: MMLCommand
name: ADD DMCMPTBYIMSI（增加IMSI对应的Diameter兼容性）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DMCMPTBYIMSI
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter协议接口兼容性IMSI号段配置
status: active
---

# ADD DMCMPTBYIMSI（增加IMSI对应的Diameter兼容性）

## 功能

**适用网元：SGSN、MME**

该命令用于设置Diameter兼容性参数，用于保证网元间支持信元的兼容性。

该命令支持针对外网用户、本网用户、IMSI号段来配置兼容性参数。

## 注意事项

- 该命令最大记录数为8192。
- 该命令执行后立即生效。
- 该命令与[**SET DMCMPT**](../Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)命令均可对Diameter兼容性参数进行配置。系统会首先匹配本命令的配置记录，若发现系统中不存在或不匹配本命令的配置记录才会匹配[**SET DMCMPT**](../Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)命令的配置记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter兼容性参数策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>配置原则：<br>- Diameter参数策略优先级从高到低为：“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 当用户为MNO用户时，该参数需要配置为“0”或128～254之间的值，该取值必须和[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)配置的“MNOID”参数取值相同。<br>- 当用户为MVNO用户时，该参数需要配置为1～64之间的值，该取值必须和[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置的“MVNOID”参数取值相同。<br>说明：- 对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。<br>- 对于本网用户，该参数是为该用户归属的MNO/MVNO运营商标识。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～15位十进制数字字符串。<br>默认值：无<br>说明：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| UESRVCC | 是否支持UE-SRVCC-Capability信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S6a接口是否支持携带UE SRVCC Capability信元。<br>数据来源：本端规划<br>取值范围：<br>- “SUPPORT(支持)”<br>- “NOT_SUPPORT(不支持)”<br>默认值：<br>“SUPPORT(支持)”<br>配置原则：当HSS不识别UE SRVCC Capability信元时，设置为<br>“NOT_SUPPORT(不支持)”<br>。 |
| SF | 特性列表 | 可选必选说明：可选参数<br>参数含义：该参数表示MME给HSS发送的Update Location Request消息中的Supported-Features信元中设置的比特位，每个比特位表示MME支持的一种功能(目前仅支持设置Feature-List-ID 1中的第26比特<br>“UE可达通知”<br>功能和第28比特<br>“状态/位置信息重获取”<br>功能)。详细说明请参照3GPP 29.272。<br>数据来源：全网规划<br>取值范围：<br>- “UE_REACHABILITY_NOTIFICATION(UE可达通知)”<br>- “STATE_INFORMATION_RETRIEVAL(状态/位置信息重获取)”<br>默认值：无<br>配置原则：请根据特性需要，设置相应的比特位。相应比特位为1时表示支持该功能，为0时表示不支持该功能。 |
| SF2 | 特性列表2 | 可选必选说明：可选参数<br>参数含义：该参数表示MME给HSS发送的消息中的Supported-Features信元中设置的比特位，每个比特位表示MME支持的一种功能，详细说明请参照3GPP 29.272。<br>数据来源：全网规划<br>取值范围：<br>- “FLSTID2_BIT16(P-CSCF Restoration)”，本参数与“WSFD-201205 基于HSS/UDM的P-CSCF故障恢复”特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。<br>- “FLSTID2_BIT19（Monitor Event）”<br>- “FLSTID2_BIT20（Dedicated Core Networks）”，本参数与“WSFD-208001DECOR基础功能”、“WSFD-208002DECOR”特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。<br>- “FLSTID2_BIT21(Non-IP PDN Type APNs)”，本参数与“WSFD-215103Non-IP数据传输”特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。<br>- “FLSTID2_BIT24(Emergency Service Continuity)”<br>- “FLSTID2_BIT27(NR as Secondary RAT)”<br>默认值：无<br>配置原则：请根据特性需要，设置相应的比特位。相应比特位为1时表示支持该功能，为0时表示不支持该功能。 |
| PGWIDTYPE | P-GW ID类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置MME给HSS发送的Notify Request消息中PDN GW Identity的类型优先级。<br>数据来源：全网规划<br>取值范围：<br>- “FQDN(MIP-Home-Agent-Host)”<br>- “IP_ADDRESS(MIP-Home-Agent-Address)”<br>默认值：<br>“FQDN(MIP-Home-Agent-Host)”<br>配置原则：<br>- 需要与UE在Non-3GPP接入时通过AAA Server向HSS注册的P-GW Identity的类型保持一致。<br>- 推荐使用“FQDN(MIP-Home-Agent-Host)”。<br>- 在全网规划时，必须确保“WSFD-104505LTE和WiFi网络之间的切换”特性和“WSFD-104504CDMA与LTE的非优化切换”特性中使用的P-GW Identity的类型一致。 |
| UPDATEPGWID | 切换后P-GW ID更新策略 | 可选必选说明：可选参数<br>参数含义：该参数用于设置UE从GPRS/UMTS切换到LTE之后，是否将切换的PDN承载的P-GW ID信息通知HSS。<br>数据来源：全网规划<br>取值范围：<br>- “NOUPDATE(不更新)”<br>- “UPDATE(更新)”<br>默认值：<br>“NOUPDATE(不更新)”<br>配置原则：如果存在以下场景，则需要将本参数设置为<br>“UPDATE(更新)”<br>：UE在GPRS/UMTS网络上建立承载，然后切换到LTE网络，再切换到WiFi网络。如果不存在这种场景，则可以将本参数设置为<br>“NOUPDATE(不更新)”<br>。 |
| NORPARA | NOR消息更新参数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在S6a/S6d接口上是否可以通过Notify Request消息向HSS更新相关参数。<br>数据来源：全网规划<br>取值范围：<br>- “IMS_VOPS(IMS VoPS参数)”<br>默认值：无<br>配置原则：<br>- “IMS_VOPS(IMS VoPS参数)”：IMS VoPS参数包括Homogenous Support of IMS Voice over PS Sessions和UE SRVCC Capability。系统需要向HSS更新IMS VoPS参数，同时业务流程中不需要发送Update Location Request消息的场景下，如果该选项被勾选，在业务流程结束后，系统会通过Notify Request消息进行更新IMS VoPS参数；否则，系统通过Update Location Request消息进行更新IMS VoPS参数。Notify Request消息对HSS的性能消耗远小于Update Location Request消息，因此当对端HSS支持MME/SGSN通过Notify Request消息更新IMS VoPS参数时，建议勾选。 |
| S6AS6DIND | S6a/S6d-Indicator | 可选必选说明：可选参数<br>参数含义：该参数用于控制Notify Request消息中的NOR-Flags信元S6a/S6d-Indicator比特的置位方式。该比特用于向HSS指示Notify Request消息修改的是SGSN还是MME的Homogeneous Support of IMS Voice Over PS Sessions参数。<br>数据来源：全网规划<br>取值范围：<br>- “NOT_SUPPORT(不支持)”<br>- “SUPPORT(支持)”<br>- “COMBINED(融合SGSN/MME支持)”<br>默认值：<br>“COMBINED(融合SGSN/MME支持)”<br>配置原则：<br>UNC<br>作为MME在S6a接口上发送Notify Request消息修改MME的Homogeneous Support of IMS Voice Over PS Sessions参数时，系统根据该参数配置的值，对NOR-Flags信元S6a/S6d-Indicator比特做不同的处理：<br>- “NOT_SUPPORT(不支持)”：S6a/S6d-Indicator比特置0。与不支持该比特的HSS对接时，建议选择该取值。<br>- “SUPPORT(支持)”：S6a/S6d-Indicator比特置1。与支持该比特的HSS对接时，建议选择该取值。<br>- “COMBINED(融合SGSN/MME支持)”：如果UNC已经为用户在HSS上进行了双注册，即已经分别作为SGSN通过S6d接口和作为MME通过S6a接口向HSS注册过用户的位置信息，该比特置1；单注册时，该比特置0。如果HSS仅针对双注册用户识别该比特，建议选择该取值。用户单注册时，待修改参数一定与已注册的这个CN节点相关，HSS可以不使用该比特进行区分。<br>说明：3GPP协议引入该S6a/S6d-Indicator比特前，MME和SGSN向HSS发送的Notify Request消息中，该比特作为保留比特都是置0的。3GPP协议引入该比特后，MME应该将该比特置1，SGSN应该将该比特置0。<br>UNC<br>作为MME与不同3GPP协议版本的HSS对接时，需要根据HSS的能力设置该参数以避免可能的协议兼容性问题。 |
| HSIMSVOPS | Homogeneous Support of IMS VoPS信元 | 可选必选说明：可选参数<br>参数含义：该参数用于控制S6a/S6d接口的Update Location Request和Notify Request消息是否携带Homogeneous Support of IMS Voice Over PS Sessions信元。该信元用于指示HSS，一个MME或SGSN服务的所有TA/RA都支持或都不支持IMS VoPS业务。<br>数据来源：全网规划<br>取值范围：<br>- “NOT_CARRY(不携带)”<br>- “BY_SYS_CAP(按照设备能力携带)”<br>- “BY_UE_CAP(按照用户能力携带)”<br>默认值：<br>“BY_SYS_CAP(按照设备能力携带)”<br>配置原则：<br>- “NOT_CARRY(不携带)”：系统不携带Homogeneous Support of IMS Voice Over PS Sessions信元。当HSS不支持或不使用Homogeneous Support of IMS Voice Over PS Sessions信元时建议选择该取值。<br>- “BY_SYS_CAP(按照设备能力携带)”<br>：系统根据RAN的IMS VoPS能力决定是否携带Homogeneous Support of IMS Voice Over PS Sessions信元，以及该信元的取值。RAN的IMS VoPS能力可以通过<br>[**SET IMSVOPS**](../../../网络管理/VoPS管理/设置VoPS配置(SET IMSVOPS)_72345711.md)<br>命令的<br>“MMEHOMO(MME侧全部支持PS域IMS语音)”<br>参数进行设置。--NOT_SUPPORT(不支持)，该信元取值为NOT_SUPPORT。--SUPPORT(支持)，该信元取值为SUPPORT。--UNSPECIFIED（未指定），不携带该信元。当HSS把Homogeneous Support of IMS Voice Over PS Sessions信元作为MME/SGSN整系统能力时建议选择该取值。<br>- “BY_UE_CAP(按照用户能力携带)”<br>：系统根据RAN的IMS VoPS能力和单用户的IMS VoPS能力决定是否携带Homogeneous Support of IMS Voice Over PS Sessions信元，以及该信元的取值。与<br>“BY_SYS_CAP(按照设备能力携带)”<br>不同之处在于，当<br>[**SET IMSVOPS**](../../../网络管理/VoPS管理/设置VoPS配置(SET IMSVOPS)_72345711.md)<br>命令的<br>“MMEHOMO(MME侧全部支持PS域IMS语音)”<br>参数的取值为<br>“SUPPORT(支持)”<br>时：对允许使用IMS VoPS业务的用户，该信元取值为SUPPORT；对不允许使用IMS VoPS业务的用户，系统按照<br>“NOIMSVOPS（不允许IMS VoPS的用户处理）”<br>参数的取值进行处理。系统根据<br>“UECAPMATCH（用户能力匹配模式）”<br>参数判断允许用户使用的IMS VoPS业务匹配模式。当HSS把Homogeneous Support of IMS Voice Over PS Sessions信元作为单用户在一个MME/SGSN下的能力时建议选择该取值。 |
| UECAPMATCH | 用户能力匹配模式 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定在S6a/S6d接口上按照用户能力携带Homogeneous Support of IMS Voice Over PS Sessions信元时，系统允许用户使用的IMS VoPS业务的匹配模式。<br>前提条件：该参数在<br>“HSIMSVOPS(Homogeneous Support of IMS VoPS信元)”<br>参数设置为<br>“BY_UE_CAP(按照用户能力携带)”<br>后生效。<br>数据来源：全网规划<br>取值范围：<br>- “FAST(快速匹配)”<br>- “EXACT(精确匹配)”<br>系统初始设置值：<br>“FAST(快速匹配)”<br>配置原则：<br>- “FAST(快速匹配)”：系统不根据用户的签约数据进行判断。主要用于以下两种场景：1、网络中未部署<br>“WSFD-201002用户群语音策略控制”<br>特性。2、网络中虽然部署了<br>“WSFD-201002用户群语音策略控制”<br>特性，但是策略中无需考虑用户签约数据因素。<br>- “EXACT(精确匹配)”：系统综合用户的签约数据进行判断。主要用于网络中部署了“WSFD-201002用户群语音策略控制”特性，并且相关策略需要考虑用户签约数据因素。 |
| NOIMSVOPS | 不允许IMS VoPS的用户处理 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制系统针对不允许使用IMS VoPS业务的用户，S6a/S6d接口的Update Location Request和Notify Request消息的Homogeneous Support of IMS Voice Over PS Sessions信元处理。<br>前提条件：该参数在<br>“HSIMSVOPS(Homogeneous Support of IMS VoPS信元)”<br>参数设置为<br>“BY_UE_CAP(按照用户能力携带)”<br>后生效。<br>数据来源：全网规划<br>取值范围：<br>- “NOT_CARRY(不携带)”<br>- “NOT_SUPPORT(携带NOT SUPPORT)”<br>默认值：<br>“NOT_SUPPORT(携带NOT SUPPORT)”<br>配置原则：<br>- “NOT_CARRY(不携带)”：系统不携带Homogeneous Support of IMS Voice Over PS Sessions信元。<br>- “NOT_SUPPORT(携带NOT SUPPORT)”：系统携带Homogeneous Support of IMS Voice Over PS Sessions信元，该信元取值为NOT_SUPPORT。 |
| TADSIMSPDN | T-ADS查询结果与IMS PDN连接状态相关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制系统向HSS返回T-ADS查询结果中的IMS Voice over PS Sessions Supported信元时，是否考虑用户的IMS PDN连接状态。<br>数据来源：全网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- “NO(否)”：系统只根据是否允许UE使用IMS VoPS业务，决定向HSS返回的IMS Voice over PS Sessions Supported信元取值，不考虑UE是否已经建立了IMS PDN连接：系统允许UE使用IMS VoPS业务，取值为SUPPORT；否则为NOT_SUPPORT。<br>- “YES(是)”：系统不仅根据是否允许UE使用IMS VoPS业务，还根据UE是否已经建立了IMS PDN连接以及考虑UE在IMS PDN连接建立情况下是否开启S-GW/P-GW故障下的业务恢复特性（特性编号：WSFD-201203，license部件编码：LKV2SRGF01），决定向HSS返回的IMS Voice over PS Sessions Supported信元取值：系统允许UE使用IMS VoPS业务，并且UE已经建立了IMS PDN连接，当S-GW/P-GW故障下的业务恢复特性未开启，或在S-GW/P-GW故障下的业务恢复特性开启的情况下，UE仅注册到MME（未注册到SGSN）且当有语音PDN故障时，取值为SUPPORT；否则为NOT_SUPPORT。<br>说明：- 使用了IMS APN激活的PDN连接被系统识别为IMS PDN连接。系统默认使用GSMA IR.92标准推荐的“IMS”作为IMS APN。如果激活了“WSFD-201002用户群语音策略控制”特性，可以通过[**ADD VOICEDEPLOY**](../../../业务安全管理/语音业务管理/增加语音部署配置(ADD VOICEDEPLOY)_72345361.md)命令配置特殊的IMS APN。 |
| NBIOTRAT | 是否支持NBIoT RAT | 可选必选说明：可选参数<br>参数含义：该参数用于指定S6a接口是否支持携带NBIOT RAT。当HSS不识别NBIOT RAT时，设置为<br>“NOT_SUPPORT（不支持）”<br>。<br>数据来源：全网规划<br>取值范围：<br>- “NOT_SUPPORT（不支持）”<br>- “SUPPORT（支持）”<br>默认值：<br>“NOT_SUPPORT（不支持）”<br>说明：- “HSS免升级”特性（特性编号：WSFD-215301，license部件编码：LKV2HUNN01）的相关license授权并开启后，该参数配置生效。 |
| NBIOTSTAT | 支持上报的状态列表 | 可选必选说明：可选参数<br>参数含义：该参数表示MME给HSS发送的ULR（Update Location Request）或IDA（Insert Subscriber Data Answer）消息中Supported-Services信元中设置的比特位，每个比特位表示一种可上报的NB-IoT状态，详细说明请参照3GPP 29.272。<br>数据来源：本端规划<br>取值范围：<br>- “UEREACH(UE可达)”<br>- “UELOC(UE位置信息)”<br>- “UELOSTCONN(UE连接丢失)”<br>- “UECOMMFAIL(UE通信失败)”<br>- “AVAILAFTDDNFAIL(DDN失败后可用)”<br>默认值：无<br>配置原则：<br>- NB-IoT状态上报功能受本命令“特性列表2”“FLSTID2_BIT19（Monitor Event）”控制，当“FLSTID2_BIT19（Monitor Event）”不选中时，本参数配置不生效。 |
| T6SF | T6接口特性列表 | 可选必选说明：可选参数<br>参数含义：该参数表示MME给SCEF发送的Reporting Information Request消息中的Supported-Features信元设置的比特位，每个比特位表示MME支持的一种功能。详细说明请参照3GPP 29.128。<br>数据来源：本端规划<br>取值范围：<br>- “T6FLID_BIT0(Monitor Event)”<br>默认值：无<br>配置原则：无 |
| NODCNR | 未签约DCNR是否允许DCNR | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持DCNR接入。<br>数据来源：全网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：无<br>说明：本参数受License控制（对应License的部件编码是LKV2UNCACC01），请在设置参数前使用<br>[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)<br>命令确认对应license是否得到授权，执行<br>[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)<br>命令确认对应License的开关状态为“ENABLE(打开)”。 |
| NORRAT | 是否支持NOR消息上报RAT TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于指定针对NSA用户，在Notify request消息是否支持携带RAT TYPE。当对端HSS不支持Notify request消息中携带RAT TYPE时，设置为“NOT_SUPPORT(不支持)”。<br>数据来源：本端规划<br>取值范围：枚举类型。该功能属于定制功能，开启前需要确认对端HSS为华为设备，且支持Notify request消息中携带RAT TYPE。<br>- NOT_SUPPORT(不支持)。<br>- SUPPORT(支持)。<br>系统初始设置值：NOT_SUPPORT(不支持)<br>说明：- 软参BYTE_EX_B34 BIT5用于控制MME是否支持通知HSS当前用户是否为NSA用户，软参优先级高于该参数。当软参BYTE_EX_B34 BIT5设置为1时，该参数功能不生效<br>- 在将软参BYTE_EX_B34 BIT5从“1”设置为“0”前，若需控制MME支持通知HSS当前用户是否为NSA用户，配置该参数值为SUPPORT |
| RATTYPELTEM | 是否支持LTE-M类型的RAT TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于指定针对LTE-M类型用户，在以下消息中是否支持携带LTE-M类型的RAT TYPE。<br>数据来源：整网规划<br>取值范围：<br>- ULR（Update Location Request）。<br>- NOR（Notify Request）<br>默认值：无<br>说明：- 针对LTE-M类型的用户，UNC向HSS发送Update Location Request消息或者Notify Request消息时，如果对应位域被选中，消息中的RAT TYPE信元会设置为LTE-M；否则消息中的RAT TYPE信元会设置为EUTRAN。<br>- Notify Request消息中携带RAT TYPE信元属于定制功能，开启前需要确认对端HSS为华为设备，且支持Notify Request消息中携带RAT TYPE。 |
| EPSFBUPDPGWID | EPS FB后P-GW ID更新策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制UE从5GC切换到EPS后，是否将切换的PDN承载的P-GW Identity信息通知HSS。<br>数据来源：整网规划<br>取值范围：<br>- NOUPDATE（不更新）<br>- UPDATE（更新）<br>系统初始设置值：NOUPDATE（不更新）<br>配置原则：如果存在UE在5GC网络上建立承载后切换到LTE网络，再需要切换到WiFi网络的场景时，则需要将本参数设置为“UPDATE(更新)”<br>；<br>如果不存在<br>该<br>场景，则可以将本参数设置为“NOUPDATE(不更新)”。 |
| UEDCNRCAP | 是否支持UE-DCNR-Capability信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S6a接口在ULR消息中是否支持携带UE DCNR Capability信元。<br>数据来源：本端规划<br>取值范围：<br>- NOT_SUPPORT(不支持)。<br>- SUPPORT(支持)。<br>系统初始设置值：NOT_SUPPORT(不支持)<br>配置原则：<br>- 该功能为华为的私有功能，对接异厂商HSS、同厂商但非配套版本的HSS时，建议配置“NOT_SUPPORT(不支持)”，否则可能会导致业务失败。只建议对本网用户且选择的HSS为华为设备的用户开启。<br>- 需要和华为HSS同时开启该功能。 |
| AMFID | 是否支持AMF Instance ID信元 | 可选必选说明：可选参数<br>参数含义：该参数用于MME发送给GMLC的Subscriber Location Report消息中是否支持携带AMF Instance ID信元。<br>数据来源：本端规划<br>取值范围：<br>- “NOT_SUPPORT（不支持）”<br>- “SUPPORT（支持）”<br>系统初始设置值：<br>“NOT_SUPPORT（不支持）”<br>配置原则：当GMLC不识别AMF Instance ID信元时，设置为<br>“NOT_SUPPORT（不支持）”<br>。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMCMPTBYIMSI]] · IMSI对应的Diameter兼容性（DMCMPTBYIMSI）

## 使用实例

- 对IMSI前缀为12303的用户配置为支持携带UE SRVCC Capability信元，支持P-CSCF故障时的语音恢复功能，“P-GW ID类型”为“FQDN(MIP-Home-Agent-Host)”，“切换后P-GW ID更新策略”为“NOUPDATE(不更新)”，“NOR消息更新参数”为“IMS_VOPS(IMS VoPS参数)”，“S6a/S6d-Indicator”为“COMBINED(融合SGSN/MME支持)”，“Homogeneous Support of IMS VoPS信元”为“BY_SYS_CAP(按照设备能力携带)”，“T-ADS查询结果与IMS PDN连接状态相关”为“NO(否)”时，运行以下命令：
  ADD DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", UESRVCC=SUPPORT, SF2=FLSTID2_BIT16-1, PGWIDTYPE=FQDN, UPDATEPGWID=NOUPDATE, NORPARA=IMS_VOPS-1, S6AS6DIND=COMBINED, HSIMSVOPS=BY_SYS_CAP, TADSIMSPDN=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DMCMPTBYIMSI.md`
