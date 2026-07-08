---
id: UNC@20.15.2@MMLCommand@ADD NSE
type: MMLCommand
name: ADD NSE（增加信令实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NSE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- 信令实体管理
status: active
---

# ADD NSE（增加信令实体）

## 功能

**适用网元：SGSN**

该命令用于增加一个网络服务实体（Network service Entity，NSE），在PCU侧新增一个NSE时，在SGSN要增加相应的NSE。信令实体分别位于BSS侧和SGSN侧，用于提供Gb接口操作所需的网络管理功能。请参考3GPP TS 48.016。

## 注意事项

- 该命令执行后立即生效。
- 系统最大支持8192个静态NSE，每个进程最大可配置1024个静态NSE。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OTHERNODE | NSE连接方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该NSE所连接的对端局点的名字。<br>数据来源：整网规划<br>取值范围：1～29位字符串<br>默认值：无 |
| SGSNINDEX | SGSN索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN索引。<br>数据来源：整网规划<br>取值范围：0<br>默认值：0 |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无<br>说明：和PCU侧取值保持一致，此标识符在SGSN范围内唯一，不能重复。 |
| BSSID | BSS编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BSS的编号。<br>数据来源：整网规划<br>取值范围：0～65534<br>默认值：无<br>说明：编号任意指定，但是同一个BSS编号下所有NSE的“是否支持Gb-Flex”属性配置必须一致。 |
| FLUSTHT | FLUSH监控定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定FLUSH监控定时器的时长，为SGSN发送FLUSH LL后等待FLUSH LL ACK的超时时长。FLUSH流程是SGSN发现用户所在小区更新了，通知老小区刷新用户信息。<br>数据来源：整网规划<br>取值范围：50ms～2000ms<br>默认值：50<br>说明：- 为了保证用户体验，这个值不要设得太大，一般情况下使用默认参数50。<br>- 小区更新包括2G小区间切换和2G到3G小区间的切换，两种场景SGSN都会向原小区下发Flush LL。<br>- 如果Flush LL没有正常下发，2G无线侧则判断TBF建链失败。 |
| PFC | 是否支持PFC | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持PFC流程（Packet Flow Context procedure），PFC流程用于在BSS与SGSN协商QoS参数。参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)”<br>说明：- 如果本端NSE支持PFC，并且BSC的NSE也支持PFC，则PFC流程才可以得到支持；如果BSC支持PFC，则本端SGSN的NSE配置必须要支持PFC；若BSC不支持PFC，则本端是否支持都可以。<br>- 当参数设置为“YES(是)”时，“PFC(仅用于Gb模式)”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-105101，License部件编码：LKV2PFC02）。 |
| CBL | 是否支持CBL | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持CBL功能（Current Bucket Level），CBL功能用于调整漏桶当前占用率，与PCU协商。参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商，在双方都支持的情况下功能才可用。<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)” |
| INR | 是否支持INR | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持INR功能（Inter-NSE re-routing），INR功能是指在不同NSE之间的路由区更新。参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)” |
| LCS | 是否支持LCS | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持LCS功能（Location Services），LCS功能是指提供用户位置信息服务。参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| RIM | 是否支持RIM | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持RIM功能（RAN Information Management），RIM功能指无线侧信息管理，在进行小区重选之前，源侧小区所在的RAN侧设备将目标小区的无线系统信息传递给MS，令MS能够使用这些信息快速接入目标小区（省略了和目标侧小区的信息同步过程），从而优化小区重选过程，减少业务中断时间。参考协议3GPP TS 48.018。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：当参数设置为<br>“YES(是)”<br>时，“NACC”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>104406<br>，License部件编码：LKV2NACC02）。 |
| ARP | 是否携带ARP信元 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识是否在CREATE-BSS-PFC消息中携带ARP（Allocation/Retention Priority）信元。ARP是指定承载分配和保持的相对优先级。<br>前提条件：该参数在参数<br>“是否支持PFC”<br>配置为<br>“YES（是）”<br>时生效。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| RACAP | 是否携带RA Capability信元 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识是否在CREATE-BSS-PFC消息中携带RACAP（RA Capability）信元。RACAP是指无线接入能力。<br>前提条件：该参数在参数<br>“是否支持PFC”<br>配置为<br>“YES（是）”<br>时生效。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| GB_FLEX | 是否支持Gb-Flex | 可选必选说明：可选参数<br>参数含义：标识本网络服务实体是否支持Gb-Flex功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：当参数设置为<br>“YES(是)”<br>时，“Gb-flex”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>104204<br>，License部件编码：LKV2GBFLEX02）。 |
| SPECSRV | 是否支持特殊业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识本网络服务实体是否支持特殊业务类型。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：在该开关打开的情况下，BSSGP协议层会增加一个信元service-class-indicator（标识本网络服务实体是否支持特殊业务类型），如果对端不支持该信元则会出现无法解析或丢包的情况。 |
| BSSQOSVERSION | BSS支持的Qos版本 | 可选必选说明：可选参数<br>参数含义：该参数用于标识BSS支持的Qos版本。服务质量QoS体现了网络所能提供给用户的服务能力(带宽、延迟、丢包率)。使网络根据业务需求，依时间性、重要性进行数据传输，提供性能保证。<br>数据来源：整网规划<br>取值范围：<br>- “R99(R99)”<br>- “R5(R5)”<br>默认值：<br>“R99(R99)”<br>说明：- 业务使用R5(R5)是与BSS侧保持一致。<br>- BSSID编号相同记录的QoS要配置相同。 |
| MOCN | 是否支持MOCN | 可选必选说明：可选参数<br>参数含义：该参数用于标识手动配置NSE是否支持MOCN功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：- 当参数设置为“YES(是)”时，“网络共享(MOCN)”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-207001，License部件编码：LKV2MOCN02）。<br>- 只有BSC、SGSN同时支持MOCN功能时，该功能才会生效。 |
| SPID | 是否支持SPID | 可选必选说明：可选参数<br>参数含义：该参数用于指定向BSS发送的消息中是否携带SPID。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：- SPID信元，是在3GPP TS R8 48.018协议引入的，由于无线侧设备可能是低协议版本的设备，提供此功能开关避免启用SPID功能时对无线侧设备产生接口兼容性影响。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSE]] · 信令实体（NSE）

## 使用实例

增加一个NSE配置，连接方向为“ShangHai”，NSEI为10，BSSID为1，FLUSH监控定时器时长为500，不支持PFC、CBL、INR、LCS、RIM、PFC-FC和MOCN功能，不支持特殊业务类型，BSS支持的Qos版本为R99：

ADD NSE: OTHERNODE="ShangHai", NSEI=10, BSSID=1, FLUSTHT=500, PFC=NO, CBL=NO, INR=NO,SPECSRV=YES, BSSQOSVERSION=R99, MOCN=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NSE.md`
