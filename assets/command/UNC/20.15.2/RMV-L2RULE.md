---
id: UNC@20.15.2@MMLCommand@RMV L2RULE
type: MMLCommand
name: RMV L2RULE（删除层二规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: L2RULE
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
- 层二规则
status: active
---

# RMV L2RULE（删除层二规则）

## 功能

**适用NF：SMF**

该命令用于删除层二规则。

## 注意事项

- 该命令执行后只对新接入的会话生效。

- 如果存在引用了层二规则名称的层二规则绑定记录，则不允许删除层二规则。层二规则绑定记录通过LST L2RULEBINDGRP查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2RULENAME | 层二规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定层二规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/L2RULE]] · 层二规则（L2RULE）

## 使用实例

删除层二规则名称为“rule1”的层二规则：

```
RMV L2RULE: L2RULENAME="rule1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除层二规则（RMV-L2RULE）_70462597.md`
