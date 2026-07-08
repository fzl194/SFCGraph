---
id: UNC@20.15.2@MMLCommand@ADD APNDNS
type: MMLCommand
name: ADD APNDNS（增加APN DNS域名策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNDNS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- APN DNS域名策略
status: active
---

# ADD APNDNS（增加APN DNS域名策略）

## 功能

**适用网元：SGSN、MME**

该命令用于增加一条APN DNS域名策略。

当选择上游网元GGSN/PGW时，需要根据APNNI和UE允许的接入能力确定使用.gprs后缀还是.org后缀组装APN域名。同时，DNS查询时，根据APNNI域名类型选择最多8个IP地址组成备选列表，进行负荷分担。当可用的IP地址权重少于阈值时，选择低优先级IP地址进行补充。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数256。
- 当UE的同时具备2/3/4G网络接入能力，但是系统中没有“APN网络标识”和“UE接入能力”匹配的记录时(包括“UE接入能力”设置为“ALL_UE(ALL UE)”的记录)，默认优选合建的GGSN/PGW。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- “*”表示通配符，即不限制APNNI。 如果APNNI为“*”，表示该记录适用于所有的APNNI。使用时先查找指定APN的记录，查找不到再使用“*”通配记录。 |
| UEACCCAP | UE接入能力 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE接入2/3/4G网络的能力。<br>数据来源：整网规划<br>取值范围：<br>- “GERAN/UTRAN_UE（GERAN/UTRAN UE）”<br>- “EUTRAN_UE(EUTRAN UE)”<br>- “GERAN/UTRAN/EUTRAN_UE(GERAN/UTRAN/EUTRAN UE)”<br>- “ALL_UE(ALL UE)”<br>默认值：无<br>配置原则：<br>- 相同“APNNI”的各条记录的UE接入能力不能重复。<br>- 如果配置了“ALL UE”的记录，则不能再配置“APNNI”相同的其它UE接入类型的记录。<br>说明：- 当“UE接入能力”设置为“ALL_UE(ALL UE)”时，系统不区分UE接入能力，仅进行“APN网络标识”匹配。 |
| DNSPOLICY | DNS域名策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定使用的DNS后缀模式。.gprs或者.org。<br>数据来源：整网规划<br>取值范围：<br>“GPRS(GPRS)”<br>，<br>“ORG(ORG)”<br>默认值：无<br>配置原则：<br>- 如果用户使用的APN和UE能力匹配记录的前两个参数，则该参数决定域名所使用的后缀类型。<br>- GPRS（.gprs）：该参数用来指定使用的DNS后缀模式为.gprs。格式如：EXAMPLE11.MNC.MCC.GPRS<br>- ORG（.org）：该参数用来指定DNS域名格式为.org。格式如：EXAMPLE1.COM.APN.EPC.MNC.MCC.3GPPNETWORK.ORG |
| SELPOLICY | 根据UE接入能力选择 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GGSN/P-GW选择策略，即MME是否根据UE能力优先选择GGSN/PGW合一网关。此参数在使用NAPTR方式查询时生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(NO)”<br>- “YES(YES)”<br>默认值：<br>“NO(NO)”<br>说明：- 针对不具备EUTRAN接入能力的UE优选GGSN，表示优先选择服务名称为x-3gpp-ggsn的Hostname，如果存在满足条件的Hostname，则这些Hostname的优先级最高，带有GnGp接口的PGW的Hostname优先级较低。<br>- 针对只具备EUTRAN接入能力的UE优选PGW，表示优先选择服务名称为x-3gpp-pgw并且不具备x-gn和x-gp接口能力的Hostname。如果存在满足条件的Hostname，则这些Hostname的优先级最高，带有GnGp接口的PGW的Hostname优先级较低。<br>- 针对同时具备GERAN、UTRAN和EUTRAN接入能力的UE优选合建的GGSN/PGW，表示优先选择服务名称为x-3gpp-pgw并且具备x-gn和x-gp接口能力的Hostname。如果存在满足条件的Hostname，则这些Hostname的优先级最高，独立的GGSN或独立的PGW的Hostname优先级较低。 |

## 操作的配置对象

- [APN DNS域名策略（APNDNS）](configobject/UNC/20.15.2/APNDNS.md)

## 使用实例

添加APN网络标识为“huawei.com”，根据UE接入能力选择为“EUTRAN_UE(EUTRAN UE)”，DNS域名策略为“GPRS(GPRS)”。

**ADD APNDNS: APNNI="huawei.com",UEACCCAP=EUTRAN_UE,DNSPOLICY=GPRS;**

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APN-DNS域名策略(ADD-APNDNS)_26145932.md`
