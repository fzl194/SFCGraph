---
id: UNC@20.15.2@MMLCommand@RMV IMSICHAR
type: MMLCommand
name: RMV IMSICHAR（删除IMSI号段属性配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSICHAR
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
- 网络管理
- 归属网络运营商管理
- IMSI号段属性配置表
status: active
---

# RMV IMSICHAR（删除IMSI号段属性配置）

## 功能

**适用网元：SGSN、MME**

该命令用于删除IMSI号段对应的属性配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后会造成该运营商的相应配置失效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1～15位十进制数字<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行删除。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>取值范围：1～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [IMSI号段属性配置（IMSICHAR）](configobject/UNC/20.15.2/IMSICHAR.md)

## 使用实例

删除 “IMSI前缀” 为 “123456” 的属性配置记录：

RMV IMSICHAR: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMSI号段属性配置(RMV-IMSICHAR)_26305860.md`
