---
id: UNC@20.15.2@MMLCommand@RMV QOSCAPBY5QI
type: MMLCommand
name: RMV QOSCAPBY5QI（删除基于5QI的QosFlow QoS限制配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSCAPBY5QI
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 基于IMSI号段的QoS管理
- 基于5QI的Qos Flow QoS限制配置
status: active
---

# RMV QOSCAPBY5QI（删除基于5QI的QosFlow QoS限制配置）

## 功能

**适用NF：SMF**

该命令用于删除基于5QI的QosFlow QoS限制的相关配置参数。

## 注意事项

命令执行后只对新接入用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数表示用于QosFlow QoS限制配置的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- INVALIDSUBRANGE（无效的用户范围）<br>- IMSI_PREFIX（指定IMSI前缀的用户）<br>- VISITING（拜访用户）<br>- ROAMING（漫游用户）<br>- HOME_USER（本网用户）<br>- ALL_USER（所有用户）<br>- HOME_NOLOCAL_USER（本网非本省用户）<br>默认值：无<br>配置原则：<br>“SUBRANGE（用户范围）”的优先级从高到低为：“IMSI_PREFIX（指定IMSI前缀）”，"HOME_NOLOCAL_USER"（本网非本省用户），“HOME_USER（本网用户）”或“ROAMING（漫游用户）”或“VISITING（拜访用户）”，“ALL_USER（所有用户）”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于系统根据对用户的IMSI前缀进行匹配，从而区分不同的用户群。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| QOS5QI | 标准5QI | 可选必选说明：必选参数<br>参数含义：该参数用于指定系统对用户QosFlow的5QI限制。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSCAPBY5QI]] · 基于5QI的QosFlow QoS限制配置。（QOSCAPBY5QI）

## 使用实例

删除“用户范围”为“IMSI_PREFIX”，“IMSI前缀”为“308010700”，“QOS5QI”为“9”的基于5QI的QosFlow QoS限制配置：

```
RMV QOSCAPBY5QI:SUBRANGE=IMSI_PREFIX,IMSIPRE="308010700",QOS5QI=9;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除基于5QI的QosFlow-QoS限制配置（RMV-QOSCAPBY5QI）_76079624.md`
