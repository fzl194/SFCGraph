---
id: UNC@20.15.2@MMLCommand@RMV IUIMEICFG
type: MMLCommand
name: RMV IUIMEICFG（删除Iu模式IMEI配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IUIMEICFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 设备检查管理
- Iu模式IMEI配置
status: active
---

# RMV IUIMEICFG（删除Iu模式IMEI配置）

## 功能

**适用网元：SGSN**

该命令用于删除UTRAN指定号段用户的获取和检查IMEI的策略。

## 注意事项

- 该命令执行后立即生效。
- 只能删除指定号段用户的IMEI配置，而不能删除默认的IMEI配置。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>取值范围：1～15位十进制数字<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行删除。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>取值范围：1～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [Iu模式IMEI配置（IUIMEICFG）](configobject/UNC/20.15.2/IUIMEICFG.md)

## 使用实例

删除IMSI前缀为“123456”的UTRAN用户的IMEI配置：

RMV IUIMEICFG:SUBRANGE=IMSI_PREFIX, IMSIPRE="123456";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Iu模式IMEI配置（RMV-IUIMEICFG）_26305446.md`
