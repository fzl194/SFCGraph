---
id: UNC@20.15.2@MMLCommand@RMV L2RULEGROUP
type: MMLCommand
name: RMV L2RULEGROUP（删除层二规则组）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV L2RULEGROUP（删除层二规则组）

## 功能

**适用NF：SMF**

该命令用于删除层二规则组。

## 注意事项

- 该命令执行后只对新接入的会话生效。

- 删除一个层二规则组的同时会删除此层二规则组下所有的与层二规则之间的绑定关系。
- 如果层二规则组名称已经被ADD L2RULEGRPBIND命令引用，则不允许删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2RULEGROUPNAME | 层二规则组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定层二规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [层二规则组（L2RULEGROUP）](configobject/UNC/20.15.2/L2RULEGROUP.md)

## 使用实例

删除层二规则组名称为“rulegrp1”的层二规则组：

```
RMV L2RULEGROUP: L2RULEGROUPNAME="rulegrp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除层二规则组（RMV-L2RULEGROUP）_23782814.md`
