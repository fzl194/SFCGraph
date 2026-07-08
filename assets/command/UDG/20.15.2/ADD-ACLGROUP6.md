---
id: UDG@20.15.2@MMLCommand@ADD ACLGROUP6
type: MMLCommand
name: ADD ACLGROUP6（增加IPv6 ACL规则组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ACLGROUP6
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- IPv6 ACL规则组
status: active
---

# ADD ACLGROUP6（增加IPv6 ACL规则组）

## 功能

该命令用于增加IPv6 ACL规则组。ACL是一种IP包过滤技术，通过对IPv6报文的源地址/通配位、报文目的地址/通配位、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有作用）等信息对照ACL规则进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，其动作包括允许（Permit）、拒绝（Deny）等。使用ACL技术时，需要先配置ACL规则组。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 当参数ACLNAME为非数字时，ACLTYPE参数默认为高级ACL。
- 单个ACL规则组下最多支持16384条ACL规则。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | IPv6 ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6 ACL规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是2000～2999（基本IPv6 ACL），3000～3999（高级IPv6 ACL）。<br>默认值：无 |
| ACLSTEP | 规则组步长 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则组规则步长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20。<br>默认值：5 |
| ACLTYPE | 规则组类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则组类型。如果不输入该参数，当参数ACLNAME为非数字时，该参数默认为高级ACL。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Basic：基本IPv6 ACL规则。<br>- Advance：高级IPv6 ACL规则。<br>默认值：无 |
| ACLMATCHORDER | 规则的匹配顺序 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则的匹配顺序是深度优先还是配置优先。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Config：配置优先。<br>- Auto：深度优先。<br>默认值：Config |
| ACLDESCRIPTION | 规则组描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则组描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。支持空格，区分大小写。<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACLGROUP6]] · IPv6 ACL规则匹配计数（ACLGROUP6）

## 关联任务

- [[UDG@20.15.2@Task@0-00209]]

## 使用实例

- 用户想通过流分类进行报文过滤或重定向，需要绑定IPv6 ACL规则组，可以创建名称为"group_basic"的IPv6 ACL规则组：
  ```
  ADD ACLGROUP6: ACLNAME="group_basic",ACLTYPE=Basic;
  ```
- 用户想通过流分类进行报文过滤或重定向，需要绑定IPv6 ACL规则组，可以创建编号为2000的IPv6 ACL规则组：
  ```
  ADD ACLGROUP6: ACLNAME="2000";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加IPv6-ACL规则组（ADD-ACLGROUP6）_50281822.md`
