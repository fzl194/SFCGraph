---
id: UNC@20.15.2@MMLCommand@ADD TACSHAREPLMN
type: MMLCommand
name: ADD TACSHAREPLMN（增加基于区域的PLMN管理）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TACSHAREPLMN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 延迟生效
is_dangerous: false
max_records: 20000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 基于区域MME共享管理
- 基于区域PLMN管理
status: active
---

# ADD TACSHAREPLMN（增加基于区域的PLMN管理）

## 功能

**适用网元：MME**

在 **[MOCN](../../../../../../../../../网络部署/特性部署/UNC特性指南/网络共享功能/WSFD-207003 基于LTE的网络共享（MOCN）_68260814.md)** 组网下的两网融合项目中，基于区域逐步融合，需要配置基于特定区域PLMN的使用策略。该命令用于增加基于区域的PLMN管理。

## 注意事项

- 此命令最大记录数为20000。
- 此命令执行后60秒内生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>说明：跟踪区域码不允许重复。 |
| PLMNGPID | PLMN群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PLMN群组标识。<br>数据来源：本端规划<br>取值范围：1～31<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TACSHAREPLMN]] · 基于区域的PLMN管理（TACSHAREPLMN）

## 使用实例

增加一条： “跟踪区域码” 为 “0x5800” ， “PLMN群组标识” 为 “1” ，的记录。

ADD TACSHAREPLMN: TAC="0x5800", PLMNGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TACSHAREPLMN.md`
