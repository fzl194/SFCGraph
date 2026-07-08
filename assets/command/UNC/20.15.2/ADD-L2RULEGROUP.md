---
id: UNC@20.15.2@MMLCommand@ADD L2RULEGROUP
type: MMLCommand
name: ADD L2RULEGROUP（增加层二规则组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: L2RULEGROUP
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 层二规则组
status: active
---

# ADD L2RULEGROUP（增加层二规则组）

## 功能

**适用NF：SMF**

该命令用于添加层二规则组。可使用该层二规则组绑定多个层二规则。

## 注意事项

- 该命令执行后只对新接入的会话生效。

- 最多可输入10000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2RULEGROUPNAME | 层二规则组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定层二规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [层二规则组（L2RULEGROUP）](configobject/UNC/20.15.2/L2RULEGROUP.md)

## 使用实例

增加一个层二规则组名称为“rulegrp1”：

```
ADD L2RULEGROUP: L2RULEGROUPNAME="rulegrp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加层二规则组（ADD-L2RULEGROUP）_70382285.md`
