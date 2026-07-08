---
id: UNC@20.15.2@MMLCommand@ADD DMRT
type: MMLCommand
name: ADD DMRT（增加Diameter域路由配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DMRT
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter路由
status: active
---

# ADD DMRT（增加Diameter域路由配置）

## 功能

**适用网元：SGSN、MME**

该命令用于新增一条Diameter域路由。域路由是指通过域名来选择对端。建议在 UNC 和Diameter对端通过DRA（Diameter路由代理）连接时使用此命令。如果需要配置域路由和主机路由互为主备，可以通过命令 [**ADD DMRTGRP**](../Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) 将域路由和主机路由配到同一个Diameter路由组索引中，业务通过引用路由组配置进行选路。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数2048。
- 一个域路由下最多配置16个对端。
- 对于“选路模式”为“SELMODE_IMSI_PRIORITY(IMSI指定优选)”的域路由，若Diameter路由组中存在属于该Diameter域路由的“路由索引”，则配置才能生效。Diameter路由组信息请参考[**LST DMRTGRP**](../Diameter路由组/查询Diameter路由组(LST DMRTGRP)_26306104.md)命令。
- 对于“应用名称”为“S6A/S6D(S6a/S6d)”的非默认域路由， 需要该域路由的域名为epc.mnc<MNC>.mcc<MCC>格式或IMSIHSS配置了该域路由的“目的实体域名”才可以生效。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统范围内标识一条Diameter域路由。<br>数据来源：本端规划<br>取值范围：0~2047<br>默认值：无<br>配置原则：相同的“路由索引”必须“是否默认路由”、“应用名称”、“选路模式”、“目的实体域名”和“路由名称”相同而“对端实体索引”不同。 |
| APPNAM | 应用名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该条域路由对应的应用接口类型。<br>数据来源：整网规划<br>取值范围：<br>- “S6A/S6D(S6a/S6d)”<br>- “S13(S13)”<br>- “SLG(SLg)”<br>- “T6A/T6AI/T6B/T6BI(T6a/T6ai/T6b/T6bi)”<br>默认值：<br>“S6A/S6D(S6a/S6d)”<br>配置原则：<br>- “S6A/S6D(S6a/S6d)”表示该域路由用于S6a/S6d接口，在对端网元为HSS或者通过DRA转接到HSS时，选择该应用。<br>- “S13(S13)”表示该域路由用于S13接口，在对端网元为EIR或者通过DRA转接到EIR时，选择该应用；<br>- “SLG(SLg)”表示该域路由用于SLg接口，在对端网元为GMLC或者通过DRA转接到GMLC时，选择该应用。<br>- “T6A/T6AI/T6B/T6BI(T6a/T6ai/T6b/T6bi)”表示该域路由用于T6a/T6ai/T6b/T6bi接口。其中T6a为MME到SCEF的接口；T6ai为MME到IWK-SCEF的接口；T6b为SGSN到SCEF的接口；T6bi为SGSN到IWK-SCEF的接口。 |
| ISDEFAULT | 是否默认路由 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该条域路由是否是默认路由。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 一个应用接口只能配置一个默认路由，即满足“路由名称”相同，且“是否默认路由”为“YES(是)”的记录，其“路由索引”必须相同。<br>- “应用名称”相同的默认路由，其“路由索引”必须相同而“对端实体索引”必须不同。<br>说明：- 默认路由作用：当请求消息携带的对端域名和应用名称在DMRT表中匹配不到记录时使用默认路由选择对端。请求消息携带的对端域名填写规则请参考产品文档中**Diameter路由查找整体层****次**。<br>- 不建议将“选路模式”为“SELMODE_IMSI_PRIORITY(IMSI指定优选)”模式的域路由配置成默认路由。 |
| RSELMODE | 选路模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域路由选择对端的模式。<br>数据来源：本端规划<br>取值范围：<br>- “SELMODE_ROUND_ROBIN(轮选)”：表示存在多条链路集时，采用顺序选择的方式选取各条链路集。<br>- “SELMODE_MASTER_SLAVE(主从)”：表示1＋N备份模式。在这种模式中，域中仅有一个链路集处于激活状态，其余链路集则均处于备份状态。<br>- “SELMODE_ACTIVE(激活)”：表示使用上次使用的链路集。<br>- “SELMODE_PRIORITY_WEIGHT(优先级权重)”：表示存在多条链路集时，根据优先级和权重选取各条链路集。<br>- “SELMODE_IMSI_PRIORITY(IMSI指定优选)”：表示存在多条链路集时，根据路由组([**ADD DMRTGRP**](../Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md))指定的链路集和优先级选取各条链路集。<br>默认值：<br>“SELMODE_MASTER_SLAVE(主从)”<br>配置原则：<br>- 当选路模式为SELMODE_IMSI_PRIORITY(IMSI指定优选)时，需要将域路由索引和需要使用的对端索引配置到路由组中。<br>说明：- 当参数设置为“SELMODE_PRIORITY_WEIGHT(优先级权重)”时，“基于权重/优先级的Diameter负荷分担”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-104404，License项：LKV2DMLS01）。 |
| REALMNAME | 目的实体域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目的对端域名。<br>数据来源：整网规划<br>取值范围：0~127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”，不区分大小写。例如：epc.mnc123.mcc123.3gppnetwork.org。<br>说明：- 对于默认路由，该参数同时也作为目的域名指导转发，推荐配置为网络中不存在的域名，仅作为默认路由标识。建议配置域名为：“defaultRoute”。<br>- Diameter从请求消息中Destination-Realm AVP获取目的域名，与路由表配置的域名（通过ADD DMRT配置）做匹配 。匹配方式不需要全匹配，而是采取后向最大匹配法则——路由表的域名可以为Destination-Realm AVP字符串的后缀，相当于寻找Dest-Realm AVP的最长后缀子串，即AVP的域名长度要大于等于路由表的域名；比如现在消息的目的域名是www.abc.efg.hij，而路由表1的域名是efg.hij，路由表2的域名是abc.efg.hij，那么就会匹配到路由表2。 |
| PEERIDX | 对端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于标识目的对等端。<br>数据来源：整网规划<br>取值范围：0~639<br>默认值：无<br>配置原则：<br>- 一个路由索引最多可配置16个对端索引。<br>- 同一对端只能被一条选路模式为IMSI指定优选的域路由引用。<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMPE**](../Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)<br>设置此参数。 |
| ROUTENAM | 路由名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域路由的名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。<br>说明：- 一个域路由索引只有一个路由名称。<br>- 同一域路由索引下，添加多个对端实体时，如果路由名称不一致，使用最后配置的路由名称。 |
| PRIORITY | 优先级 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定域中对端的优先级。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：无<br>说明：- “SELMODE_MASTER_SLAVE(主从)”时，同一个域中不同对端的优先级不允许相同。<br>- 该参数只在“选路模式”设置为“SELMODE_MASTER_SLAVE(主从)”、“SELMODE_PRIORITY_WEIGHT(优先级权重)”或者“SELMODE_IMSI_PRIORITY(IMSI指定优选)”时有效。<br>- “选路模式”设置为“SELMODE_MASTER_SLAVE(主从)”时，如果该参数未配置，系统会按照如下规则配置：- 若表中配置了至少一条该“路由索引”的记录则取已配置的最大的优先级，之后加1作为本次新加“路由索引”的优先级，并要求其值不超过255。<br>- 若表中没有该“路由索引”的记录，则优先级为0。<br>- “选路模式”设置为“SELMODE_PRIORITY_WEIGHT(优先级权重)”或者“SELMODE_IMSI_PRIORITY(IMSI指定优选)”时，如果该参数未配置，则系统默认优先级为0。<br>- 数值越小，优先级越高。 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域中对端的权重。<br>数据来源：整网规划<br>取值范围：1~255<br>默认值：1<br>说明：该参数只在<br>“选路模式”<br>设置为<br>“SELMODE_PRIORITY_WEIGHT(优先级权重)”<br>时有效。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Diameter域路由中对等端的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMRT]] · Diameter域路由配置（DMRT）

## 使用实例

增加一个模式为轮选模式的本地缺省路由，其名字为diamt_route1目的域为example.com:

ADD DMRT: ROUTEIDX=1, RSELMODE=SELMODE_ROUND_ROBIN, REALMNAME="example.com", PEERIDX=0, ROUTENAM="diamt_route1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Diameter域路由配置(ADD-DMRT)_26306100.md`
