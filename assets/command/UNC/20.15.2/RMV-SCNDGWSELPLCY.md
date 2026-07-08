---
id: UNC@20.15.2@MMLCommand@RMV SCNDGWSELPLCY
type: MMLCommand
name: RMV SCNDGWSELPLCY（删除相同APN建立多个PDP/PDN连接的网关选择策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCNDGWSELPLCY
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- GGSN_P-GW选择
status: active
---

# RMV SCNDGWSELPLCY（删除相同APN建立多个PDP/PDN连接的网关选择策略）

## 功能

**适用网元：SGSN、MME**

该命令用于删除指定用户使用相同APN建立多个PDP/PDN连接场景下，系统选择GGSN/P-GW的策略。

## 注意事项

- 该命令执行后只对新激活PDN生效。

## 权限

manage-ug; system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | 接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用以指定网关地址选择策略的适用用户的接入方式。<br>数据来源：整网规划<br>取值范围：<br>- “LTE(LTE)”：指定的接入类型是LTE。<br>- “GPRS_UMTS(GPRS&UMTS)”：指定的接入类型是GPRS或者UMTS。<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用以指定网关地址选择策略的适用用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有指定接入类型的用户。<br>- “HOME_USER（本网用户）”：所有指定接入类型的本网用户。<br>- “FOREIGN_USER（外网用户）”：所有指定接入类型的外网用户。<br>- “IMSI_PREFIX（指定IMSI前缀）”：所有指定接入类型且指定IMSI前缀的用户。<br>默认值：无<br>配置原则：如果一个用户在多个用户范围内，该参数生效的优先级从高到低：<br>“IMSI_PREFIX（指定IMSI前缀）”<br>，<br>“HOME_USER（本网用户）”<br>或<br>“FOREIGN_USER（外网用户）”<br>，<br>“ALL_USER（所有用户）”<br>。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用以指定网关地址选择策略的适用用户IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“指定IMSI前缀”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~15位数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCNDGWSELPLCY]] · 相同APN建立多个PDP/PDN连接的网关选择策略（SCNDGWSELPLCY）

## 使用实例

删除LTE接入类型的所有外网用户使用相同APN建立多个PDN连接的网关选择策略配置： “接入类型” 设置成 “LTE” ， “用户范围” 设置成 “FOREIGN_USER（外网用户）” ：

RMV SCNDGWSELPLCY: RATTYPE=LTE, SUBRANGE=FOREIGN_USER;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SCNDGWSELPLCY.md`
