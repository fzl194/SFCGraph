---
id: UNC@20.15.2@MMLCommand@RMV QOSCAPBYQCI
type: MMLCommand
name: RMV QOSCAPBYQCI（删除基于QCI的Non-GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSCAPBYQCI
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- QoS限制配置
- 基于QCI的承载级QoS限制
status: active
---

# RMV QOSCAPBYQCI（删除基于QCI的Non-GBR承载QoS限制配置）

## 功能

**适用网元：MME**

该命令用于根据用户范围及承载的QCI删除Non-GBR承载QoS限制配置记录。

## 注意事项

- 该命令执行后对于新接入的EPS承载立即生效。如果当前用户已经激活了EPS承载，该命令的限制会在用户下一次会话管理业务流程中生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数表示使用QoS限制的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：指网络中的所有用户。<br>- “IMSI_PREFIX(指定IMSI前缀)：指网络中与指定的IMSI前缀匹配的用户。”<br>- “HOME_USER(本网用户)：指网络中的本网签约用户。”<br>- “FOREIGN_USER(外网用户)：指网络中的漫游用户。”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~15位数字。<br>默认值：无 |
| QCI | QCI | 可选必选说明：必选参数<br>参数含义：该参数表示使用QoS限制的用户签约的承载的QCI。<br>数据来源：整网规划<br>取值范围：1~9<br>默认值：无 |

## 操作的配置对象

- [基于QCI的Non-GBR承载QoS限制配置（QOSCAPBYQCI）](configobject/UNC/20.15.2/QOSCAPBYQCI.md)

## 使用实例

运营商规划网络，删除IMSI前缀为3080107000，QCI为5的用户QoS限制配置：

RMV QOSCAPBYQCI: SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000", QCI=5;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除基于QCI的Non-GBR承载QoS限制配置(RMV-QOSCAPBYQCI)_26146222.md`
