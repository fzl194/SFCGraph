---
id: UNC@20.15.2@MMLCommand@RMV ACLGROUP
type: MMLCommand
name: RMV ACLGROUP（删除ACL规则组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ACLGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- ACL规则组
status: active
---

# RMV ACLGROUP（删除ACL规则组）

## 功能

该命令用于删除ACL规则组。

## 注意事项

- 该命令执行后立即生效。
- 如果规则组下配置了规则，则所有规则会一并删除。
- 如果有业务已经引用了规则组，不可以删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是1000～1999（接口ACL），2000～2999（基本ACL），3000～3999（高级ACL），4000～4999（以太ACL）。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACLGROUP]] · ACL规则匹配计数（ACLGROUP）

## 使用实例

用户不再使用ACL进行报文过滤，可以将规则组2005删除：

```
RMV ACLGROUP: ACLNAME="2005";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ACLGROUP.md`
