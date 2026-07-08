---
id: UNC@20.15.2@MMLCommand@RMV ACLRULEADV4
type: MMLCommand
name: RMV ACLRULEADV4（删除高级ACL规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ACLRULEADV4
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- 高级ACL规则
status: active
---

# RMV ACLRULEADV4（删除高级ACL规则）

## 功能

该命令用于删除高级ACL规则。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则属于哪个规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是3000～3999。<br>默认值：无 |
| ACLRULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACLRULEADV4]] · 高级ACL规则（ACLRULEADV4）

## 使用实例

删除高级ACL规则组3000下的规则名称为"rule_6"的规则：

```
RMV ACLRULEADV4: ACLNAME="3000",ACLRULENAME="rule_6";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ACLRULEADV4.md`
