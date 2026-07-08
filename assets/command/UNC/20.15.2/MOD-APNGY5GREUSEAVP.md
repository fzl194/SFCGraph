---
id: UNC@20.15.2@MMLCommand@MOD APNGY5GREUSEAVP
type: MMLCommand
name: MOD APNGY5GREUSEAVP（修改基于apn的Gy接口重用字段的填写方式）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNGY5GREUSEAVP
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 话单字段控制
- 5G用户话单重用字段控制
status: active
---

# MOD APNGY5GREUSEAVP（修改基于apn的Gy接口重用字段的填写方式）

## 功能

**适用NF：PGW-C**

该命令用于修改指定APN 5G用户接入时，Gy接口重用字段的填写方式。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”；该参数取值应与ADD APN命令中参数“APN”保持一致，使用该前需通过ADD APN添加一组记录。 |
| RAT | 无线接入技术 | 可选必选说明：可选参数<br>参数含义：该参数用于控制用户RAT为NR时，Gy接口是否通过支持通过3GPP-RAT-Type字段携带用户真实的RAT。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不携带用户信息<br>- “ENABLE（使能）”：携带用户真实信息(EUTRAN)<br>默认值：无<br>配置原则：无 |
| ULI | 用户位置信息 | 可选必选说明：可选参数<br>参数含义：该参数用于控制用户RAT为NR时，Gy接口是否支持通过3GPP-User-Location-Info字段携带用户真实的位置信息。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不携带用户信息<br>- “ENABLE（使能）”：携带转换后的用户4G位置信息<br>默认值：无<br>配置原则：无 |
| SERVINGNODETYPE | 服务节点类型 | 可选必选说明：可选参数<br>参数含义：该参数用于控制用户RAT为NR时，Gy接口是否支持通过Serving-Node-Type字段携带用户真实的服务节点类型。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不携带用户信息<br>- “ENABLE（使能）”：携带用户真实服务节点类型(MME)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNGY5GREUSEAVP]] · 基于apn的Gy接口重用字段的填写方式（APNGY5GREUSEAVP）

## 使用实例

对指定APN的5G用户，当需要修改其Gy接口重用字段的填写方式时，使用该命令。

```
MOD APNGY5GREUSEAVP: APN="APNGY", RAT=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-APNGY5GREUSEAVP.md`
