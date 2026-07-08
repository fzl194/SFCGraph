---
id: UNC@20.15.2@MMLCommand@ADD L2RULEBINDGRP
type: MMLCommand
name: ADD L2RULEBINDGRP（增加层二规则与层二规则组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: L2RULEBINDGRP
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
- 层二规则绑定
status: active
---

# ADD L2RULEBINDGRP（增加层二规则与层二规则组的绑定关系）

## 功能

**适用NF：SMF**

该命令用于增加层二规则与层二规则组的绑定关系。

## 注意事项

- 该命令执行后只对新接入的会话生效。

- 同一个层二规则组下最多可绑定16个层二规则。

- 最多可输入10000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2RULEGROUPNAME | 层二规则组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定层二规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD L2RULEGROUP命令配置生成。 |
| L2RULENAME | 层二规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定层二规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD L2RULE命令配置生成。 |

## 操作的配置对象

- [层二规则与层二规则组的绑定关系（L2RULEBINDGRP）](configobject/UNC/20.15.2/L2RULEBINDGRP.md)

## 使用实例

如果运营商需要将层二规则“rule1”与层二规则组"rulegrp1"绑定：

```
ADD L2RULEBINDGRP: L2RULEGROUPNAME="rulegrp1", L2RULENAME="rule1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加层二规则与层二规则组的绑定关系（ADD-L2RULEBINDGRP）_70462509.md`
