---
id: UNC@20.15.2@MMLCommand@MOD NSE
type: MMLCommand
name: MOD NSE（修改信令实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NSE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- 信令实体管理
status: active
---

# MOD NSE（修改信令实体）

## 功能

**适用网元：SGSN**

该命令用于修改NSE网络服务实体参数。信令实体分别位于BSS侧和SGSN侧，用于提供GB接口操作所需的网络管理功能。请参考3GPP TS 48.016。

## 注意事项

- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。
- 执行本命令修改“PFC（是否支持PFC）”、“CBL（是否支持CBL）”、“INR（是否支持INR）”、“LCS（是否支持LCS）”、“RIM（是否支持RIM）”或者“MOCN（是否支持MOCN）”，SGSN会复位该SIGBVC信令实体；但是如果这些功能在BSC侧是关闭的，在SGSN侧是开启的，这种情况下在SGSN侧关闭这些功能，SGSN不会复位SIGBVC信令实体。
- 如果修改NSE的任意一个或多个如下参数（“PFC（是否支持PFC）”、“CBL（是否支持CBL）”、“INR（是否支持INR）”、“LCS（是否支持LCS）”、“RIM（是否支持RIM）”）的取值，会导致SGSN主动发起针对该NSE的BVC-RESET流程，导致该NSE下的小区重新上报，引起业务短暂中断。但是如果这些功能在BSC侧是关闭的，在SGSN侧是开启的，这种情况下在SGSN侧关闭这些功能，SGSN不会复位SIGBVC信令实体。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGSNINDEX | SGSN索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN索引。<br>数据来源：整网规划<br>取值范围：0<br>默认值：无 |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无<br>说明：和PCU侧取值保持一致，此标识符在SGSN范围内唯一，不能重复。 |
| BSSID | BSS编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BSS的编号。<br>数据来源：整网规划<br>取值范围：0～65534<br>默认值：无<br>说明：编号任意指定，但是同一个BSS编号下所有NSE的“是否支持Gb-Flex”属性配置必须一致。 |
| FLUSTHT | FLUSH监控定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定FLUSH监控定时器的时长，为SGSN发送FLUSH LL后等待FLUSH LL ACK的超时时长。<br>数据来源：整网规划<br>取值范围：50ms～2000ms<br>默认值：无<br>配置原则：建议值为50ms。<br>说明：- 为了保证用户体验，这个值不要设得太大，一般情况下使用默认参数50。<br>- 小区更新包括2G小区间切换和2G到3G小区间的切换，两种场景SGSN都会向原小区下发Flush LL。<br>- 如果Flush LL没有正常下发，2G无线侧则判断TBF建链失败。 |
| PFC | 是否支持PFC | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持PFC流程（Packet Flow Context procedure），参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“YES(是)”<br>。<br>说明：- 如果本端NSE支持PFC，并且BSC的NSE也支持PFC，则PFC流程才可以得到支持；如果BSC支持PFC，则本端SGSN的NSE配置必须要支持PFC；若BSC不支持PFC，则本端是否支持都可以。<br>- 当参数设置为“YES(是)”时，“PFC(仅用于Gb模式)”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-105101，License部件编码：LKV2PFC02）。 |
| CBL | 是否支持CBL | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持CBL功能（Current Bucket Level），参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“YES(是)”<br>。 |
| INR | 是否支持INR | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持INR功能（Inter-NSE re-routing），参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“YES(是)”<br>。 |
| LCS | 是否支持LCS | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持LCS功能（Location Services），参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“NO(否)”<br>。 |
| RIM | 是否支持RIM | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持RIM功能（RAN Information Management），参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“NO(否)”<br>。<br>说明：- 当参数设置为“YES(是)”时，“NACC”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-104406，License部件编码：LKV2NACC02）。<br>- 如果NSE此参数的取值发生了改变，除了以下场景外，SGSN都会主动发起针对该NSE的BVC-RESET流程且在给BSC的BVC-RESET PDU中携带该参数值告知BSC。BSC会根据SGSN侧NSE是否支持RIM功能来决定是否将该NSE的RIM消息转发给SGSN。 在以下场景即使此参数取值发生变化SGSN也不会主动发起BVC-RESET流程： BSC侧配置NSE不支持RIM功能，且SGSN侧将该参数的取值由“YES(是)”修改为“NO(否)”。 |
| OTHERNODE | NSE连接方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该NSE所连接的对端局点的名字。<br>数据来源：整网规划<br>长度范围：1～29位字符串<br>默认值：无 |
| ARP | 是否携带ARP信元 | 可选必选说明：条件可选参数<br>参数含义：该参数用于判断是否在CREATE-BSS-PFC消息中携带ARP（Allocation/Retention Priority）信元。<br>前提条件：该参数在参数<br>“是否支持PFC”<br>配置为<br>“YES（是）”<br>时生效。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“NO(否)”<br>。 |
| RACAP | 是否携带RA Capability信元 | 可选必选说明：条件可选参数<br>参数含义：该参数用于判断是否在CREATE-BSS-PFC消息中携带RACAP（RA Capability）信元。<br>前提条件：该参数在参数<br>“是否支持PFC”<br>配置为<br>“YES（是）”<br>时生效。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“NO(否)”<br>。 |
| GB_FLEX | 是否支持Gb-Flex | 可选必选说明：可选参数<br>参数含义：标识本网络服务实体是否支持Gb-Flex功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“NO(否)”<br>。<br>说明：当参数设置为<br>“YES(是)”<br>时，“Gb-flex”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>104204<br>，License部件编码：LKV2GBFLEX02）。 |
| SPECSRV | 是否支持特殊业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持特殊业务类型。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：建议值为<br>“NO(否)”<br>。<br>说明：在该开关打开的情况下，BSSGP协议层会增加一个信元service-class-indicator，如果对端不支持该信元则会出现无法解析或丢包的情况。 |
| BSSQOSVERSION | BSS支持的Qos版本 | 可选必选说明：可选参数<br>参数含义：该参数用于标识BSS支持的QoS版本。<br>数据来源：整网规划<br>取值范围：<br>- “R99(R99)”<br>- “R5(R5)”<br>默认值：无<br>配置原则：建议值为<br>“R99(R99)”<br>。<br>说明：BSSID编号相同记录的QoS要配置相同。 |
| MOCN | 是否支持MOCN | 可选必选说明：可选参数<br>参数含义：该参数用于标识手动配置NSE是否支持MOCN功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>说明：- 当参数设置为“YES(是)”时，“网络共享(MOCN)”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-207001，License部件编码：LKV2MOCN02）。<br>- 只有BSC、SGSN同时支持MOCN功能时，该功能才会生效。 |
| SPID | 是否支持SPID | 可选必选说明：可选参数<br>参数含义：该参数用于指定向BSS发送的消息中是否携带SPID。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>说明：- SPID信元，是在3GPP TS R8 48.018协议引入的，由于无线侧设备可能是低协议版本的设备，提供此功能开关避免启用SPID功能时对无线侧设备产生接口兼容性影响。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSE]] · 信令实体（NSE）

## 使用实例

修改NSEI为10的NSE，使BSSID为1，FLUSH监控定时器为1000，支持PFC，CBL，INR和MOCN，携带ARP信元、携带RACAP信元，支持特殊业务类型，BSS支持的QoS版本为R5：

MOD NSE: NSEI=10, BSSID=1, FLUSTHT=1000, PFC=YES, CBL=YES, INR=YES, ARP=YES, RACAP=YES, SPECSRV=YES, BSSQOSVERSION=R5, MOCN=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NSE.md`
