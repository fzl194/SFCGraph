---
id: UNC@20.15.2@MMLCommand@MOD QOSMONTRULE
type: MMLCommand
name: MOD QOSMONTRULE（修改QoS监测规则）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: QOSMONTRULE
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- QoS监测管理
- QoS监测规则管理
status: active
---

# MOD QOSMONTRULE（修改QoS监测规则）

## 功能

**适用NF：SMF**

该命令用于修改QoS监测规则。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MATCHMODE | 匹配类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示匹配类型。<br>数据来源：本端规划<br>取值范围：<br>- MSISDN（MSISDN）<br>- IMSI（IMSI）<br>- MULTIPARA（多参数）<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"MATCHMODE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"MATCHMODE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定切片业务类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定切片细分标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定DNN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| ARP | ARP数值 | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定ARP。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无<br>配置原则：无 |
| FIVEQI | 5QI | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定5QI。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| MONTSWITCH | QoS监测开关 | 可选必选说明：该参数在"MATCHMODE"配置为"MSISDN"、"IMSI"、"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定QoS监测开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| MONTPERIOD | QoS监测周期(分钟) | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定QoS监测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是60~5256000。<br>默认值：无<br>配置原则：无 |
| RESOURCENUM | 规划资源数 | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定规划资源数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~99999999。<br>默认值：无<br>配置原则：无 |
| MONTRATIO | QoS监测比例(%) | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定QoS监测比例。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100，单位是百分比。<br>默认值：无<br>配置原则：无 |
| REQQOSMONT | 时延监测方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE和UPF(PSA)之间数据包时延监测方向。<br>数据来源：本端规划<br>取值范围：<br>- “DL（下行监测）”：测量UPF(PSA)到UE的下行数据包时延。<br>- “UL（上行监测）”：测量UE到UPF(PSA)的上行数据包时延。<br>- “RP（往返监测）”：测量UE和UPF(PSA)之间的往返数据包时延。<br>默认值：无<br>配置原则：<br>该参数至少需要勾选一个有效值。 |
| REPORTFREQ | 上报频率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定时延监测上报频率。<br>数据来源：本端规划<br>取值范围：<br>- “EVETT（事件触发）”：事件触发上报时延。<br>- “PERIO（周期性触发）”：周期性上报时延。<br>- “SESRL（会话释放触发）”：会话释放触发上报时延。<br>默认值：无<br>配置原则：<br>该参数至少需要勾选一个有效值。 |
| DLPCKTDLAYTHRES | 下行时延阈值(毫秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要上报下行数据包时延的阈值取值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295，单位是毫秒。<br>默认值：无<br>配置原则：<br>该参数在“REQQOSMONT”勾选“DL”，且REPORTFREQ勾选“EVETT”时需配置，且仅在该场景下生效。 |
| ULPCKTDLAYTHRES | 上行时延阈值(毫秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要上报上行数据包时延的阈值取值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295，单位是毫秒。<br>默认值：无<br>配置原则：<br>该参数在“REQQOSMONT”勾选“UL”，且REPORTFREQ勾选“EVETT”时需配置，且仅在该场景下生效。 |
| RPPCKTDLAYTHRES | 往返时延阈值(毫秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要上报往返数据包时延的阈值取值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295，单位是毫秒。<br>默认值：无<br>配置原则：<br>该参数在“REQQOSMONT”勾选“RP”，且REPORTFREQ勾选“EVETT”时需配置，且仅在该场景下生效。 |
| MINWAITTIME | 等待最小值时间(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定两次连续时延监测报告之间的最小等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295，单位是秒。<br>默认值：无<br>配置原则：<br>该参数在REPORTFREQ勾选“EVETT”时需配置，且仅在该场景下生效。 |
| MEASPERIOD | 测量周期(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定生成时延监测报告的周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295，单位是秒。<br>默认值：无<br>配置原则：<br>该参数在REPORTFREQ勾选“PERIO”时需配置，且仅在该场景下生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSMONTRULE]] · QoS监测规则（QOSMONTRULE）

## 使用实例

修改IMSI为"460030123456789"QoS监测规则的监测开关为ENABLE：

```
MOD QOSMONTRULE:MATCHMODE=IMSI,IMSI="460030123456789",MONTSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-QOSMONTRULE.md`
