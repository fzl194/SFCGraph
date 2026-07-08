---
id: UNC@20.15.2@MMLCommand@RMV NGACCAREALST
type: MMLCommand
name: RMV NGACCAREALST（删除5G接入限制区域列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGACCAREALST
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入限制
- 5G接入限制区域管理
status: active
---

# RMV NGACCAREALST（删除5G接入限制区域列表）

## 功能

**适用NF：AMF**

该命令用于删除5G接入限制区域信息配置。

## 注意事项

- 该命令执行后立即生效。

- 若指定的区域除一条非特殊用户的配置记录之外其他配置均为特殊用户配置，则该配置不能删除。若要删除，请先删除该区域的特殊用户配置记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREARANGE | 区域范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用接入限制的区域范围：所有区域或者指定区域。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_AREA（所有区域）”：所有区域<br>- “AREA_CODE（指定区域编码）”：指定区域编码<br>默认值：无<br>配置原则：无 |
| AREACODE | 区域编码 | 可选必选说明：该参数在"AREARANGE"配置为"AREA_CODE"时为条件必选参数。<br>参数含义：该参数用于指定应用接入限制的某个区域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该区域编码必须先通过ADD AREACODE进行添加；而区域内的跟踪区列表则通过ADD AREAMEM进行添加。<br>默认值：无<br>配置原则：无 |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用接入限制的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “USER_GROUP（用户群）”：用户群<br>- “SPECIAL_USER_RANGE（指定IMSI范围）”：指定IMSI范围。<br>- “MSISDN_PREFIX（MSISDN前缀）”：MSISDN前缀。<br>默认值：无<br>配置原则：<br>当前指定IMSI范围无法匹配IMSI长度为14的用户。<br>当配置多条记录的情况下，AMF按照“指定IMSI范围”、“用户群”、"MSISDN前缀"、“本网用户”或“外网用户”、“所有用户”由高到低的优先级进行匹配，其中“用户群”场景下又以匹配号段长短作为优先级判定依据。<br>当存在“用户范围”为“SPECIAL_USER_RANGE(指定IMSI范围)”或“USER_GROUP(用户群)”中任意一种的记录时，不建议再添加“MSISDN_PREFIX(MSISDN前缀)”的记录；当存在“MSISDN_PREFIX(MSISDN前缀)”的记录时，不建议再添加“用户范围”为“SPECIAL_USER_RANGE(指定IMSI范围)”或“USER_GROUP(用户群)”的记录。 |
| BEGINIMSI | 起始IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIAL_USER_RANGE"时为条件必选参数。<br>参数含义：该参数用于指定起始IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：<br>终止IMSI需大于等于起始IMSI。仅当终止IMSI与起始IMSI长度全为15位十进制数时，终止IMSI可以等于起始IMSI。<br>当输入值不足15位时，末尾补0处理。例如，BEGINIMSI输入12345，ENDIMSI输入123456，表示区间为[123450000000000,123456000000000]。<br>当BEGINIMSI未输入取值时，系统会为此参数赋无效值"NULL"。 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定用户的MSISDN前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G接入限制区域列表（NGACCAREALST）](configobject/UNC/20.15.2/NGACCAREALST.md)

## 使用实例

某5G试验网络完成商用前的测试，删除原本仅限VIP用户和试验用户接入的限制配置，执行如下命令：

```
RMV NGACCAREALST: AREARANGE=AREA_CODE, AREACODE="SH_5G_TRIAL_NETWORK", SUBRANGE=ALL_USER;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G接入限制区域列表（RMV-NGACCAREALST）_44007640.md`
