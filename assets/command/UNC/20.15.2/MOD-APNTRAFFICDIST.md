---
id: UNC@20.15.2@MMLCommand@MOD APNTRAFFICDIST
type: MMLCommand
name: MOD APNTRAFFICDIST（修改漫游地动态签约分流控制）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNTRAFFICDIST
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- 漫游地动态签约分流控制
status: active
---

# MOD APNTRAFFICDIST（修改漫游地动态签约分流控制）

## 功能

**适用NF：SMF**

该命令用于修改指定的Selected DNN的漫游地动态签约分流控制。改变SMF发给CHF的消息中的Sponsor Identity、访地策略对应的计费用户模板名称，控制是否需要上报辅锚点UPF的用量以及控制园区内主锚点流量是否进行计费。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SELECTEDDNN | Selected DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定基于漫游地动态签约的分流策略控制特性的AMF带给SMF的Selected DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| SPONSORID | Sponsor Identity | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF发给CHF的消息中的Sponsor Identity。该参数配置为有效值时，SMF会在给CHF发的消息中指示免流，并在上报用量时携带Sponsor Identity。CHF收到免流指示时不上报话单给归属地，转为离线计费，话单本地指定目录存储。运营商的计费营帐系统会从CHF指定目录取话单，根据Sponsor Identity识别商城，与商城进行费用结算。该参数配置为有效值时，为了计费准确性，5G在商城区域内已触发分流、发生5G到4G的互操作时发起会话重建。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>输入单空格与不输入效果相同，此时SPONSORID为空。 |
| AUXUSAGEREPORT | 辅锚点UPF上报用量开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否需要上报辅锚点UPF的用量。<br>数据来源：全网规划<br>取值范围：选择ENABLE（使能）或DISABLE（不使能）。<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| PSACHARGE | 在园区内主锚点流量是否计费 | 可选必选说明：可选参数<br>参数含义：该参数用于控制园区内主锚点流量是否进行计费。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定访地策略对应的计费用户模板名称。该参数已经通过ADD USERPROFILE命令中的USERPROFILENAME参数配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNTRAFFICDIST]] · 漫游地动态签约分流控制（APNTRAFFICDIST）

## 使用实例

修改Selected DNN名为“mall1”的漫游地动态签约分流控制，使主辅锚点均需要上报辅锚点UPF的用量，打开“辅锚点UPF上报用量开关”，用户模板名称为“testuserprofilename”，园区主锚点流量进行计费。

```
MOD APNTRAFFICDIST: SELECTEDDNN = "mall1", AUXUSAGEREPORT = ENABLE, 
PSACHARGE = ENABLE, USERPROFILENAME = "testuserprofilename";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-APNTRAFFICDIST.md`
