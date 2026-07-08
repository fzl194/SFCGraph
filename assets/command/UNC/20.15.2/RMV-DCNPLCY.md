---
id: UNC@20.15.2@MMLCommand@RMV DCNPLCY
type: MMLCommand
name: RMV DCNPLCY（删除DCN配置策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DCNPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN配置策略
status: active
---

# RMV DCNPLCY（删除DCN配置策略）

## 功能

**适用网元：MME**

该命令用于删除指定用户范围DCN的配置策略参数。删除后，MME将不再为该范围的用户提供DCN服务。

## 注意事项

该命令执行后只对新接入用户生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DCN策略的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PRE(指定IMSI前缀)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>配置为<br>“IMSI_PRE(指定IMSI前缀)”<br>后生效。<br>数据来源：本端规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [DCN配置策略（DCNPLCY）](configobject/UNC/20.15.2/DCNPLCY.md)

## 使用实例

运营商删除 “IMSIPRE” 为 “123003” 的用户的DCN的配置策略，不再为其提供DCN服务：

RMV DCNPLCY: SUBRANGE=IMSI_PRE, IMSIPRE="123003";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DCN配置策略(RMV-DCNPLCY)_72345433.md`
