---
id: UNC@20.15.2@MMLCommand@RMV MPACIPV6RULE
type: MMLCommand
name: RMV MPACIPV6RULE（删除IPv6 MPAC策略规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MPACIPV6RULE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- IPv6策略规则
status: active
---

# RMV MPACIPV6RULE（删除IPv6 MPAC策略规则）

## 功能

该命令用于删除某策略下的某规则。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定创建规则的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |
| RULENAME | 规则名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPACIPV6RULE]] · IPv6 MPAC策略规则（MPACIPV6RULE）

## 使用实例

删除某策略下的某规则：

```
RMV MPACIPV6RULE:POLICYNAME="policyV6",RULENAME="name-test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MPACIPV6RULE.md`
