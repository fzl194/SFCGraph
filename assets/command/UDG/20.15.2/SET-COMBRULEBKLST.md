---
id: UDG@20.15.2@MMLCommand@SET COMBRULEBKLST
type: MMLCommand
name: SET COMBRULEBKLST（设置组合规则黑名单）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: COMBRULEBKLST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- CombRuleBkLst
status: active
---

# SET COMBRULEBKLST（设置组合规则黑名单）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置如果同时存在组合rule和拆分rule，组合rule type中未配置，且组合rule优先级低，则网关当做是的blacklist的策略类型。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | BLPOLICYTYPE |
| --- | --- |
| 初始值 | NULL |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BLPOLICYTYPE | 黑名单策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用来设置组合rule中未配置的策略作为黑名单策略处理的策略类型。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- SMARTREDIRECT：指定url重定向策略在组合rule中未配置时作为黑名单策略。<br>- ADC：指定ADC策略在组合rule中未配置时作为黑名单策略。<br>- QOS：指定Qos策略在组合rule中未配置时作为黑名单策略。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [组合规则黑名单（COMBRULEBKLST）](configobject/UDG/20.15.2/COMBRULEBKLST.md)

## 使用实例

设置组合规则黑名单为ADC：

```
SET COMBRULEBKLST: BLPOLICYTYPE=SMARTREDIRECT-0&ADC-1&QOS-0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置组合规则黑名单（SET-COMBRULEBKLST）_86530161.md`
