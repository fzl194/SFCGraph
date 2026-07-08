---
id: UNC@20.15.2@MMLCommand@ADD RNC
type: MMLCommand
name: ADD RNC（增加Iu接口RNC信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RNC
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu接口RNC信息
status: active
---

# ADD RNC（增加Iu接口RNC信息）

## 功能

**适用网元：SGSN**

该命令用于增加Iu接口RNC信息。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为512。
- 输入“NI”和“SPC”确定的信令点必须在SCCP目的信令点表中已经配置。SCCP目的信令点表请参考[**ADD SCCPDPC**](../../信令传输管理/SCCP管理/SCCP目的信令点/增加SCCP目的信令点(ADD SCCPDPC)_26306130.md)命令。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RNCX | RNC索引 | 可选必选说明：必选参数<br>参数含义：该参数用于设置RNC索引。<br>数据来源：整网规划<br>取值范围：0～511<br>默认值：无 |
| RNCN | RNC名 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RNC名称。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：无 |
| RNCMCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家代码，MCC + MNC = PLMN ID。<br>数据来源：整网规划<br>取值范围：3位十进制的数字<br>默认值：无 |
| RNCMNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号，MCC + MNC = PLMN ID。<br>数据来源：整网规划<br>取值范围：2或3位十进制的数字<br>默认值：无 |
| RNCID | RNC标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RNC标识，在一个PLMN中唯一标识一个RNC。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |
| NI | 网络指示语 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络指示语。<br>数据来源：整网规划<br>取值范围：<br>- “INT(国际网)”<br>- “INTB(国际备用网)”<br>- “NAT(国内网)”<br>- “NATB(国内备用网)”<br>默认值：无 |
| SPC | 信令点编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信令点编码，24bit或14bit信令点编码。<br>数据来源：整网规划<br>取值范围：1～8位十六进制的字符串<br>默认值：无 |
| TRLCTMR | 资源分配定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定重定位时资源分配定时器。<br>数据来源：整网规划<br>取值范围：0ms～65534ms<br>默认值：50000ms |
| TRLCCMP | 迁移完成定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定重定位完成定时器。<br>数据来源：整网规划<br>取值范围：0ms～65534ms<br>默认值：55000ms |
| TRABASSGT | RAB指配过程定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAB指配过程定时器。<br>数据来源：整网规划<br>取值范围：0ms～65534ms<br>默认值：15000ms |
| TIGOC | 忽略OVERLOAD定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定忽略OVERLOAD定时器。该定时器期间，忽略核心网侧收到的所有OVERLOAD消息和信令点拥塞通知。请参考3GPP TS 25.413。<br>数据来源：整网规划<br>取值范围：0s～65534s<br>默认值：60s<br>说明：“忽略OVERLOAD定时器(TIGOC)”<br>必须小于<br>“控制流量速率定时器(TINTC)”<br>。 |
| TINTC | 控制流量速率定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定控制流量速率定时器。该定时器期间，核心网禁止增加流量速率。请参考3GPP TS 25.413。<br>数据来源：整网规划<br>取值范围：0s～65534s<br>默认值：90s |
| TRAFR | 复位定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定复位定时器。在核心网侧配置的复位过程的最大时间。请参考3GPP TS 25.413。<br>数据来源：整网规划<br>取值范围：0s～~65534s<br>默认值：60s |
| TRATR | 复位保护定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定复位保护定时器。在发送复位确认消息之前，核心网侧的保护时间。请参考3GPP TS 25.413。<br>数据来源：整网规划<br>取值范围：0s～65534s<br>默认值：60s |
| CNMCC | 核心网移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定核心网移动国家码，MCC + MNC = PLMN ID。在Paging等流程中，需要把此项带给RNC，如果此项未配置，则使用<br>[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)<br>中相应参数配置的值。<br>数据来源：整网规划<br>取值范围：1～3位十进制数字字符串<br>默认值：无 |
| CNMNC | 核心网移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定核心网移动网号，MCC + MNC = PLMN ID。在Paging等流程中，需要把此项带给RNC，如果此项未配置，则使用<br>[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)<br>中相应参数配置的值。<br>数据来源：整网规划<br>取值范围：2～3位十进制数字字符串<br>默认值：无 |
| CNID | CN标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN标识，在一个PLMN中唯一标识一个SGSN。在Paging等流程中，需要把此项带给RNC，如果此项未配置，则使用<br>[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)<br>中相应参数配置的值。<br>数据来源：整网规划<br>取值范围：0～4095或65535<br>默认值：无<br>说明：当修改CNID为65535，CNID就设置为无效值，同时CNMCC，CNMNC参数也同步修改为无效值。 |
| IMS | RNC是否支持IMS | 可选必选说明：可选参数<br>参数含义：该参数用于指定RNC是否支持IMS。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)” |
| IU_FLEX | RNC是否支持IU-FLEX | 可选必选说明：可选参数<br>参数含义：该参数用于指定RNC是否支持IU-FLEX。如果支持IU-FLEX，表示该RNC对应的路由区在POOL区内。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)”<br>说明：当参数设置为<br>“YES(支持)”<br>时，“Iu-flex”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>104203<br>，License部件编码：LKV2IUFLEX02）。 |
| RANSHR | RNC是否支持RAN共享 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RNC是否支持RAN共享。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)” |
| UESBI | 保留参数 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)” |
| RNCVER | RNC的协议版本 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RNC的协议版本，与RNC保持一致。MME根据RNC的协议版本控制给RNC发送的信元，更高版本协议才会支持的信元不发送给RNC。<br>数据来源：对端协商<br>取值范围：<br>- “ R99(R99)”<br>- “R4(R4)”<br>- “R5(R5)”<br>- “R6(R6)”<br>- “R7(R7)”<br>- “R8(R8)”<br>- “R9+(R9+)”<br>默认值：<br>“R6(R6)” |
| SPID | RNC是否支持SPID | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定向RNC发送的消息中是否携带SPID。<br>前提条件：该参数在<br>“RNC的协议版本”<br>为<br>“R8(R8)”<br>或<br>“R9+(R9+)”<br>时配置。<br>数据来源：对端协商<br>取值范围：<br>- “NO(不支持)”：对端RNC不支持SPID，不希望核心网将SPID带给RNC时，关闭此开关。<br>- “YES(支持)”：对端RNC支持SPID，并希望核心网将SPID带给RNC时，打开此开关。<br>默认值：<br>“NO(不支持)”<br>说明：- 由于无线侧设备可能是低协议版本的设备，提供此功能开关避免启用SPID功能时对无线侧设备产生接口兼容性影响。<br>- SPID从R8版本开始引入，只有当“RNC的协议版本”配置为“R8(R8)”及以上的版本，才能打开SPID功能。 |
| OFUTRAN | RNC是否支持Out Of UTRAN | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定，如下场景中<br>UNC<br>发送给RNC的IU Release Command消息中是否携带Out of UTRAN信元：<br>- UNC作为旧侧GnGp SGSN，在IntraUNCUTRAN->EUTRAN TAU时向旧侧RNC发送Iu Release Command<br>该参数可以指令RNC立即释放RRC资源，不再等待UE的响应，减少因等待造成的RRC资源浪费(由于重选流程，是直接在新侧EUTRAN接入，因此不会再给RNC应答)。<br>前提条件：该参数在<br>“RNC的协议版本”<br>配置为<br>“R9+(R9+)”<br>后生效。<br>数据来源：对端协商<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)”<br>说明：- 受3GPP TS 23.060 GTPV1协议限制，UNC作为旧侧GnGp SGSN，不支持InterUNC场景下新侧RAT的判断，此场景下不会携带Out of UTRAN信元。<br>- Out of UTRAN从3GPP TS 25.413 R11开始引入，只有当"RNC的协议版本"配置为"R9+(R9+)"，才能配置Out of UTRAN功能。 |
| SENDRESET | 发送RESET消息最大次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定定时器超时后重发RESET消息的最大次数。<br>数据来源：整网规划<br>取值范围：1～50<br>默认值：3 |
| IPV6ATTR | RNC是否支持IPv6 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RNC是否支持IPV6。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)” |
| SNDOVERLOAD | 是否向RNC发送OVERLOAD消息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN在3G过载的情况下，是否向RNC发送Overload消息。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：为了防止发送Overload消息对对端网元造成不良影响，SGSN设计成可配置在过载情况下是否发送Overload消息，且缺省配置下不发送。 |
| OTS | RNC是否支持OneTunnel | 可选必选说明：可选参数<br>参数含义：该参数用于指定RNC是否支持OneTunnel。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)”<br>说明：当参数设置为<br>“YES(支持)”<br>时，“支持Direct Tunnel功能”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>104506<br>，License部件编码：LKV2DIRTUN02）。 |
| R7QOS | RNC是否支持R7 QoS | 可选必选说明：可选参数<br>参数含义：该参数用于指定RNC是否支持R7 QoS。<br>数据来源：整网规划<br>前提条件：该参数在<br>“RNCVER”<br>为<br>“R6”<br>或者<br>“R7”<br>时生效。<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)” |
| RABQOS | 协商RAB QoS | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAB指配是否协商QoS，即SGSN向RNC发送的RAB ASSIGNMENT REQUEST消息中是否携带Alternative RAB Parameter Values信元。请参见协议3GPP TS 25.413。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不支持)”<br>- “YES(支持)”<br>默认值：<br>“NO(不支持)” |
| ALTBRTYPE | 可选比特率类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAB指配协商QoS时的可选比特率类型，即SGSN向RNC发送的RAB ASSIGNMENT REQUEST消息中使用的可选比特率类型是未指定类型(Unspeicified)或值范围类型(Value Range)。请参见协议3GPP TS 25.413。<br>数据来源：整网规划<br>取值范围：<br>- “UNSPECIFIED(未指定类型)”<br>- “VALUERANGE(值范围类型)”<br>默认值：<br>“UNSPECIFIED(未指定类型)” |
| CHGSYMTOASYMBI | 更改RAB双向对称为非对称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否将RAB指配中RAB上下行方向类型由Symmetric bidirectional改为Asymmetric Bidirectional。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不支持)”：要求核心网和无线侧的速率相同。<br>- “YES(支持)”：核心网和无线侧的速率可以不同。<br>默认值：<br>“YES(支持)” |
| SGSNBUF | 是否SGSN缓存3G下行数据包 | 可选必选说明：可选参数<br>参数含义：此参数指示Iu模式RAU流程中是否由SGSN缓存下行数据。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：- YES表示在UE处于PMM_CONNECTED状态时，从该RNC迁移到其它RAN节点的RAU过程中，SGSN直接对UE的下行数据进行缓存，并通过新侧RAN节点所在的网络转发给UE。当RNC不支持下行数据缓存和转发功能时建议配置为YES。<br>- NO表示在UE处于PMM_CONNECTED状态时，从该RNC迁移到其它RAN节点的RAU过程中，SGSN不对UE的下行数据进行缓存，而是仍然下发给旧侧RNC，由旧侧RNC对UE的下行数据进行缓存。然后由旧侧RNC导回给SGSN，再由SGSN通过新侧RAN节点所在的网络转发给UE。当RNC遵守3GPP协议支持下行数据缓存和转发功能时建议配置为NO。 |
| IPPLC | Iu-U地址处理策略 | 可选必选说明：可选参数<br>参数含义：如果Iu-U地址为IPv4v6双栈，控制发送给RNC消息中transportLayerAddress信元的地址填写策略和控制从RNC收到消息中transportLayerAddress信元的读取策略。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4IPV6(先IPv4后IPv6)”<br>- “IPV6IPV4(先IPv6后IPv4)”<br>- “Iu-C(与Iu-C相同)”<br>- “IPV4(仅使用IPv4地址)”<br>- “IPV6(仅使用IPv6地址)”<br>默认值：<br>“IPV4IPV6(先IPv4后IPv6)”<br>配置原则：<br>- 仅IPv4向IPv6组网改造过程中的IPv4IPv6双栈组网时需要配置。<br>- 需要和对端RNC对接后确认RNC填写和读取transportLayerAddress信元的规则后配置。默认配置为IPv4在前IPv6在后。<br>- 取值为“Iu-C(与Iu-C相同)”时，当前只支持IPv4。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RNC]] · Iu接口RNC信息（RNC）

## 使用实例

增加一个RNC，索引为1，RNC名称为TEST，移动国家代码为460，移动网号为00，RNC的标识为1，网络指示语为国内网，信令点编码是0x123，其余参数采用缺省值：

ADD RNC: RNCX=1, RNCN="TEST", RNCMCC="460", RNCMNC="00", RNCID=1, NI=NATB, SPC="123";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Iu接口RNC信息(ADD-RNC)_26146040.md`
