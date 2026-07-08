---
id: UDG@20.15.2@MMLCommand@MOD ACLGROUPIPSEC
type: MMLCommand
name: MOD ACLGROUPIPSEC（修改ACL规则组）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: ACLGROUPIPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- ACL管理
- ACL规则组
status: active
---

# MOD ACLGROUPIPSEC（修改ACL规则组）

## 功能

该命令用于修改ACL规则组的配置，可以修改规则组的步长，以及规则组描述信息。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行该命令前，需要提前配置[**ADD ACLGROUPIPSEC**](增加ACL规则组（ADD ACLGROUPIPSEC）_26150747.md)命令添加ACL规则组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是3000～3999（高级ACL），但兼容CE版本，允许配置其他数值但不会生效。<br>默认值：无<br>配置原则：无 |
| ACLSTEP | 规则组步长 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则组规则步长，仅当不指定规则ID时生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~20。<br>默认值：无<br>配置原则：无 |
| ACLMATCHORDER | 规则的匹配顺序 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则的匹配顺序是深度优先还是配置优先。<br>数据来源：本端规划<br>取值范围：<br>- “Config（规则组下的规则按照配置优先排序）”：配置优先。<br>- “Auto（规则组下的规则按照深度优先自动排序）”：深度优先。<br>默认值：无<br>配置原则：无 |
| ACLDESCRIPTION | 规则组描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ACL规则组描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~127。支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>建议取有实际意义的名称，以方便识别。 |

## 操作的配置对象

- [ACL规则组（ACLGROUPIPSEC）](configobject/UDG/20.15.2/ACLGROUPIPSEC.md)

## 使用实例

为了便于维护，可以修改规则组3005的描述信息为"aclgroup"：

```
MOD ACLGROUPIPSEC: ACLNAME="3005",ACLDESCRIPTION="aclgroup";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改ACL规则组（MOD-ACLGROUPIPSEC）_26150757.md`
