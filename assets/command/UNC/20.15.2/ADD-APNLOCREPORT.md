---
id: UNC@20.15.2@MMLCommand@ADD APNLOCREPORT
type: MMLCommand
name: ADD APNLOCREPORT（增加基于APN的位置上报配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNLOCREPORT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置上报管理
- APN用户位置信息上报开关
status: active
---

# ADD APNLOCREPORT（增加基于APN的位置上报配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加基于APN的位置上报配置。实时位置上报特性可以采用PCF/PCRF下发位置trigger的方式来触发，也可以采用SMF/PGW-C/GGSN本地配置位置trigger的方式来触发。SMF/PGW-C/GGSN可以通过本命令来配置基于APN的本地位置trigger。本配置受到全局位置上报功能（SET SMCOMMFUNC）和APN位置上报功能（ADD APN）的控制，并且有优先级高于全局位置上报配置（SET LOCATIONREPORT）。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| ULITRIGGERFLG | 配置用户位置信息的trigger | 可选必选说明：可选参数<br>参数含义：该参数用来配置用户位置信息的trigger。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| RAITRIGGERFLG | 配置路由区的trigger | 可选必选说明：可选参数<br>参数含义：该参数用来配置路由区的trigger。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| TAITRIGGERFLG | 配置跟踪区的trigger | 可选必选说明：可选参数<br>参数含义：该参数用来配置跟踪区的trigger。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| ECGITRIGGERFLG | 配置演进的全球小区的trigger | 可选必选说明：可选参数<br>参数含义：该参数用来配置演进的全球小区的trigger。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| NCGITRIGGERFLG | 配置NR全球小区的trigger | 可选必选说明：可选参数<br>参数含义：该参数用来配置5G NR全球小区的trigger。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| ULITRIROAMING | 基于用户漫游属性控制ULI信息上报 | 可选必选说明：该参数在"ULITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户漫游属性控制ULI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- ROAMING（漫游用户）<br>- VISITING（拜访用户）<br>- HOME（本地用户）<br>默认值：无<br>配置原则：<br>该参数在"ULITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| RAITRIROAMING | 基于用户漫游属性控制RAI信息上报 | 可选必选说明：该参数在"RAITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户漫游属性控制RAI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- ROAMING（漫游用户）<br>- VISITING（拜访用户）<br>- HOME（本地用户）<br>默认值：无<br>配置原则：<br>该参数在"RAITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| TAITRIROAMING | 基于用户漫游属性控制TAI信息上报 | 可选必选说明：该参数在"TAITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户漫游属性控制TAI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- ROAMING（漫游用户）<br>- VISITING（拜访用户）<br>- HOME（本地用户）<br>默认值：无<br>配置原则：<br>该参数在"TAITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| ECGITRIROAMING | 基于用户漫游属性控制ECGI信息上报 | 可选必选说明：该参数在"ECGITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户漫游属性控制ECGI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- ROAMING（漫游用户）<br>- VISITING（拜访用户）<br>- HOME（本地用户）<br>默认值：无<br>配置原则：<br>该参数在"ECGITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| NCGITRIROAMING | 基于用户漫游属性控制NCGI信息上报 | 可选必选说明：该参数在"NCGITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户漫游属性控制NCGI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- ROAMING（漫游用户）<br>- VISITING（拜访用户）<br>- HOME（本地用户）<br>默认值：无<br>配置原则：<br>该参数在"NCGITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| ULITRIRAT | 基于用户RAT类型控制ULI信息上报 | 可选必选说明：该参数在"ULITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户RAT类型控制ULI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- UNKNOWN（未知）<br>- UTRAN（通用陆地无线接入网）<br>- GERAN（GSM/EDGE无线接入网）<br>- WLAN（无线局域网）<br>- GAN（通用访问网络）<br>- HSPA（高速分组接入）<br>- EUTRAN（演进型通用陆地无线接入网）<br>- EUTRAN_NB_IOT（窄带物联网）<br>- NGRAN（5G无线接入网）<br>默认值：无<br>配置原则：<br>该参数在"ULITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| RAITRIRAT | 基于用户RAT类型控制RAI信息上报 | 可选必选说明：该参数在"RAITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户RAT类型控制RAI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- UNKNOWN（未知）<br>- UTRAN（通用陆地无线接入网）<br>- GERAN（GSM/EDGE无线接入网）<br>- WLAN（无线局域网）<br>- GAN（通用访问网络）<br>- HSPA（高速分组接入）<br>- EUTRAN（演进型通用陆地无线接入网）<br>- EUTRAN_NB_IOT（窄带物联网）<br>- NGRAN（5G无线接入网）<br>默认值：无<br>配置原则：<br>该参数在"RAITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| TAITRIRAT | 基于用户RAT类型控制TAI信息上报 | 可选必选说明：该参数在"TAITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户RAT类型控制TAI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- UNKNOWN（未知）<br>- UTRAN（通用陆地无线接入网）<br>- GERAN（GSM/EDGE无线接入网）<br>- WLAN（无线局域网）<br>- GAN（通用访问网络）<br>- HSPA（高速分组接入）<br>- EUTRAN（演进型通用陆地无线接入网）<br>- EUTRAN_NB_IOT（窄带物联网）<br>- NGRAN（5G无线接入网）<br>默认值：无<br>配置原则：<br>该参数在"TAITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| ECGITRIRAT | 基于用户RAT类型控制ECGI信息上报 | 可选必选说明：该参数在"ECGITRIGGERFLG"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用来配置基于用户RAT类型控制ECGI信息上报。<br>数据来源：本端规划<br>取值范围：<br>- UNKNOWN（未知）<br>- UTRAN（通用陆地无线接入网）<br>- GERAN（GSM/EDGE无线接入网）<br>- WLAN（无线局域网）<br>- GAN（通用访问网络）<br>- HSPA（高速分组接入）<br>- EUTRAN（演进型通用陆地无线接入网）<br>- EUTRAN_NB_IOT（窄带物联网）<br>- NGRAN（5G无线接入网）<br>默认值：无<br>配置原则：<br>该参数在"ECGITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。 |
| MSINFOTIMER | 位置更新消息上报的迟滞控制时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用来配置位置更新消息上报的迟滞控制时长(秒)。为了避免单会话内频繁发生更新的Trigger上报，UNC引入了迟滞控制，即控制相邻两次动作之间的最小时间间隔，避免动作频繁导致系统负荷增长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~3600。<br>默认值：600<br>配置原则：<br>该参数仅适用于PGW-C。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNLOCREPORT]] · 基于APN的位置上报配置（APNLOCREPORT）

## 使用实例

增加APN为“HUAWEI.COM”的基于用户位置、跟踪区、全球演进小区、5G NR全球小区trigger的实时位置上报：

```
ADD APNLOCREPORT: APN="HUAWEI.COM",ULITRIGGERFLG=ENABLE,RAITRIGGERFLG=DISABLE,TAITRIGGERFLG=ENABLE,ECGITRIGGERFLG=ENABLE,NCGITRIGGERFLG=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNLOCREPORT.md`
