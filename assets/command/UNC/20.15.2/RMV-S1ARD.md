---
id: UNC@20.15.2@MMLCommand@RMV S1ARD
type: MMLCommand
name: RMV S1ARD（删除S1模式接入限制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1ARD
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 接入限制管理
- S1模式接入限制参数
status: active
---

# RMV S1ARD（删除S1模式接入限制参数）

## 功能

**适用网元：MME**

该命令用于删除S1模式接入限制参数。该命令先根据IMSI号段将用户进行分类，再对每一类用户按照用户签约的ARD信息、签约的APN信息进行区分而控制用户接入E-UTRAN网络。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于清除指定用户范围的信息。<br>取值范围：<br>- “ALL_USER(所有用户)”：表示该指定用户范围为所有用户。<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”：表示该用户范围为指定IMSI前缀。<br>- “SPECIAL_IMSI_RANGE(指定IMSI范围)”：表示该用户范围为指定IMSI范围。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待清除用户的IMSI前缀的信息。使用时按照IMSI完全匹配进行查询。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>时生效。<br>取值范围：1～15位数字<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待清除用户的IMSI，对该IMSI所在号段进行删除。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时生效。<br>取值范围：1～15位数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1ARD]] · S1模式接入限制参数（S1ARD）

## 使用实例

1. 删除所有用户的S1模式接入限制记录：
  RMV S1ARD: SUBRANGE=ALL_USER;
2. 删除IMSI前缀为123456的S1模式接入限制记录：
  RMV S1ARD: SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="123456";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-S1ARD.md`
