---
id: UNC@20.15.2@MMLCommand@MOD ACLGROUP6
type: MMLCommand
name: MOD ACLGROUP6（修改IPv6 ACL规则组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ACLGROUP6
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- IPv6 ACL规则组
status: active
---

# MOD ACLGROUP6（修改IPv6 ACL规则组）

## 功能

该命令用于修改IPv6 ACL规则组的配置，可以修改规则组的步长，以及规则组描述信息。

## 注意事项

- 该命令执行后立即生效。
- IPv6 ACL创建之后，ACLTYPE不可修改，修改的话会报错。
- 执行该命令前，需要提前配置ADD ACLGROUP命令添加ACL规则组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | IPv6 ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6 ACL规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是2000～2999（基本IPv6 ACL），3000～3999（高级IPv6 ACL）。<br>默认值：无 |
| ACLSTEP | 规则组步长 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则组规则步长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20。<br>默认值：无 |
| ACLMATCHORDER | 规则的匹配顺序 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则的匹配顺序是深度优先还是配置优先。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Config：配置优先。<br>- Auto：深度优先。<br>默认值：无 |
| ACLDESCRIPTION | 规则组描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则组描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 建议取有实际意义的名称，以方便识别。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACLGROUP6]] · IPv6 ACL规则匹配计数（ACLGROUP6）

## 使用实例

为了便于维护，可以修改IPv6 ACL规则组2005的描述信息为"aclgroup"：

```
MOD ACLGROUP6: ACLNAME="2005",ACLDESCRIPTION="aclgroup";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IPv6-ACL规则组（MOD-ACLGROUP6）_50120866.md`
