---
id: UDG@20.15.2@MMLCommand@RMV RULEALL
type: MMLCommand
name: RMV RULEALL（删除所有规则）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RULEALL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 规则
status: active
---

# RMV RULEALL（删除所有规则）

## 功能

**适用NF：PGW-U、UPF**

![](删除所有规则（RMV RULEALL）_06014580.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会删除规则下所有绑定关系，并且会导致正在使用此规则的用户出现规则匹配错误、计费错误等现象。

该命令用于删除所有规则。

## 注意事项

- 该命令执行后立即生效。
- 如果Rule被用户模板（UserProfile）绑定，删除Rule会自动解除与用户模板的绑定关系。
- 如果Rule正在被业务使用，则不允许删除。
- 对于SMF下发的rule，生效方式参见BIT1842。
- 如果Rule被IMSI/MSISDN号段组绑定，删除Rule会自动解除与IMSI/MSISDN号段组的绑定关系。
- 当配置量较大时单次执行可能无法删除全部记录，需要多次执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULESPECTYPE | 规则规格类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则类型，当取值为SPECIFICATION_LIMITED时，表示规格受限规则，表示会话安装的规则数和被USERPROFILE绑定的规则数量均存在一定限制。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT：默认配置。<br>- SPECIFICATION_LIMITED：规格受限配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [所有规则（RULEALL）](configobject/UDG/20.15.2/RULEALL.md)

## 使用实例

删除所有规则：

```
RMV RULEALL:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除所有规则（RMV-RULEALL）_06014580.md`
