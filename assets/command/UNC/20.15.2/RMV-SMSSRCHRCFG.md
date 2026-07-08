---
id: UNC@20.15.2@MMLCommand@RMV SMSSRCHRCFG
type: MMLCommand
name: RMV SMSSRCHRCFG（删除SMS小范围CHR上报规则配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMSSRCHRCFG
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHR管理
status: active
---

# RMV SMSSRCHRCFG（删除SMS小范围CHR上报规则配置）

## 功能

**适用NF：SMSF**

该命令用于删除SMS小范围CHR上报规则配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置小范围CHR的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “SPECIFIC_IMSI（指定用户IMSI）”：表示指定用户IMSI。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件必选参数。<br>参数含义：该参数用于指定IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SMS小范围CHR上报规则配置（SMSSRCHRCFG）](configobject/UNC/20.15.2/SMSSRCHRCFG.md)

## 使用实例

运营商希望删除“用户范围”为“指定用户IMSI”，“IMSI前缀”为“12303120010”的SMS小范围CHR上报规则配置，执行如下命令：

```
RMV SMSSRCHRCFG:SUBRANGE=SPECIFIC_IMSI, IMSIPRE="12303120010";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SMS小范围CHR上报规则配置（RMV-SMSSRCHRCFG）_04041277.md`
