---
id: UNC@20.15.2@MMLCommand@RMV UFCSFB
type: MMLCommand
name: RMV UFCSFB（删除预留功能策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UFCSFB
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 预留功能策略管理
status: active
---

# RMV UFCSFB（删除预留功能策略）

## 功能

**适用网元：MME**

该命令用于删除预留功能策略。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “HOME_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：此参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [预留功能策略（UFCSFB）](configobject/UNC/20.15.2/UFCSFB.md)

## 使用实例

运营商删除外网用户的预留功能策略：

RMV UFCSFB: SUBRANGE=FOREIGN_USER, NOID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除预留功能策略(RMV-UFCSFB)_26305258.md`
