---
id: UNC@20.15.2@MMLCommand@MOD SMFPRESELBYIMSI
type: MMLCommand
name: MOD SMFPRESELBYIMSI（修改基于IMSI优选指定SMF配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SMFPRESELBYIMSI
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMF优选策略管理
status: active
---

# MOD SMFPRESELBYIMSI（修改基于IMSI优选指定SMF配置）

## 功能

**适用NF：AMF**

该命令用于修改基于IMSI优选指定SMF配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定进行优选指定SMF的用户IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。<br>默认值：无<br>配置原则：无 |
| SMFINSTANCEID | SMF实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定优选SMF的实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFPRESELBYIMSI]] · 基于IMSI优选指定SMF配置（SMFPRESELBYIMSI）

## 使用实例

针对IMSI为“123456789012345”的用户修改优选SMF实例ID为“a6a61c6f-0d3a-4221-b1da-424eda3ccf66”配置，执行如下命令：

```
MOD SMFPRESELBYIMSI:IMSI="123456789012345",SMFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf66";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SMFPRESELBYIMSI.md`
