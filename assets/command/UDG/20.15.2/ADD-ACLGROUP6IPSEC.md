---
id: UDG@20.15.2@MMLCommand@ADD ACLGROUP6IPSEC
type: MMLCommand
name: ADD ACLGROUP6IPSEC（增加IPv6 ACL规则组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ACLGROUP6IPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- ACL管理
- IPv6 ACL规则组
status: active
---

# ADD ACLGROUP6IPSEC（增加IPv6 ACL规则组）

## 功能

该命令用于增加ACL规则组。

> **说明**
> - 该命令执行后立即生效。
>
> - 当参数ACLNAME为非数字时，ACLTYPE参数默认为高级ACL。
>
> - 最多可输入65535条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | 规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是3000～3999（高级ACL），但兼容CE版本，允许配置其他数值但不会生效。<br>默认值：无<br>配置原则：无 |
| ACLSTEP | 规则组步长 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则组规则步长，仅当不指定规则ID时生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~20。<br>默认值：5<br>配置原则：无 |
| ACLTYPE | 规则组类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则组类型。如果不输入该参数，当参数ACLNAME为非数字时，该参数默认为高级ACL。<br>数据来源：本端规划<br>取值范围：<br>- Basic（基本ACL）<br>- Advance（高级ACL）<br>默认值：无<br>配置原则：无 |
| ACLMATCHORDER | 规则的匹配顺序 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则的匹配顺序是深度优先还是配置优先。<br>数据来源：本端规划<br>取值范围：<br>- “Config（规则组下的规则按照配置优先排序）”：配置优先。<br>- “Auto（规则组下的规则按照深度优先自动排序）”：深度优先。<br>默认值：Config<br>配置原则：无 |
| ACLDESCRIPTION | 规则组描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ACL规则组描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~127。支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>建议取有实际意义的名称，以方便识别。 |

## 操作的配置对象

- [IPv6 ACL规则组（ACLGROUP6IPSEC）](configobject/UDG/20.15.2/ACLGROUP6IPSEC.md)

## 使用实例

用户想通过流分类进行报文过滤或重定向，需要绑定ACL规则组，可以创建编号为3005的ACL规则组：

```
ADD ACLGROUP6IPSEC: ACLNAME="3005";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加IPv6-ACL规则组（ADD-ACLGROUP6IPSEC）_21521202.md`
