---
id: UNC@20.15.2@MMLCommand@MOD APNDNS
type: MMLCommand
name: MOD APNDNS（修改APN DNS域名策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNDNS
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
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- APN DNS域名策略
status: active
---

# MOD APNDNS（修改APN DNS域名策略）

## 功能

**适用网元：SGSN、MME**

该命令用于修改APN DNS域名策略。

当选择上游网元GGSN/PGW时，需要根据APNNI和UE允许的接入能力确定使用.gprs后缀还是.org后缀组装APN域名。同时，DNS查询时，根据APNNI域名类型选择最多8个IP地址组成备选列表，进行负荷分担。当可用的IP地址权重少于阈值时，选择低优先级IP地址进行补充。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：参见命令<br>[**ADD APNDNS**](增加APN DNS域名策略(ADD APNDNS)_26145932.md)<br>。<br>说明：“APNNI”<br>和<br>“UEACCCAP”<br>作为索引查找记录，不能修改。 |
| UEACCCAP | UE接入能力 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE接入2/3/4G网络的能力。<br>数据来源：整网规划<br>取值范围：<br>- “GERAN/UTRAN_UE（GERAN/UTRAN UE）”<br>- “EUTRAN_UE(EUTRAN UE)”<br>- “GERAN/UTRAN/EUTRAN_UE(GERAN/UTRAN/EUTRAN UE)”<br>- “ALL_UE(ALL UE)”<br>默认值：无<br>说明：“APNNI”<br>和<br>“UEACCCAP”<br>作为索引查找记录，不能修改。 |
| DNSPOLICY | DNS域名策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定使用的DNS后缀模式。.gprs或者.org。<br>数据来源：整网规划<br>取值范围：<br>“GPRS(GPRS)”<br>，<br>“ORG(ORG)”<br>默认值：无<br>配置原则：<br>- 如果用户使用的APN和UE能力匹配记录的前两个参数，则该参数决定域名所使用的后缀类型。<br>- GPRS（.gprs）：该参数用来指定使用的DNS后缀模式为.gprs。格式如：HUAWEI11.MNC003.MCC123.GPRS<br>- ORG（.org）：该参数用来指定NRI域名格式为.org。格式如：HUAWEI1.COM.APN.EPC.MNC003.MCC123.3GPPNETWORK.ORG |
| SELPOLICY | 根据UE接入能力选择 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GGSN/P-GW选择策略。<br>数据来源：整网规划<br>取值范围：<br>- “NO(NO)”<br>- “YES(YES)”<br>配置原则：参见命令<br>[**ADD APNDNS**](增加APN DNS域名策略(ADD APNDNS)_26145932.md)<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNDNS]] · APN DNS域名策略（APNDNS）

## 使用实例

修改 “APN网络标识” 为“huawei.com”， “根据UE接入能力选择” 为 “EUTRAN_UE(EUTRAN UE)” 的UE， “ DNS域名策略 ” “GPRS(GPRS)”

**MOD APNDNS: APNNI="huawei.com", UEACCCAP=EUTRAN_UE, DNSPOLICY=GPRS;**

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN-DNS域名策略(MOD-APNDNS)_26305742.md`
