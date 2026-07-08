---
id: UNC@20.15.2@MMLCommand@RMV MMERESELPLCY
type: MMLCommand
name: RMV MMERESELPLCY（删除MME重选策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMERESELPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MME重选管理
- MME重选策略参数
status: active
---

# RMV MMERESELPLCY（删除MME重选策略）

## 功能

**适用网元：MME**

该命令用于删除指定用户范围用户的MME重选策略参数。删除记录后，MME将不再为该范围的用户提供重选服务。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待进行网元重选的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在"用户范围"参数配置为"指定IMSI前缀"后生效。<br>数据来源：整网规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MMERESELPLCY]] · MME重选策略（MMERESELPLCY）

## 使用实例

1. 删除一条用户范围为“ALL_USER(所有用户)”的记录
  RMV MMERESELPLCY: SUBRANGE=ALL_USER;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MMERESELPLCY.md`
