---
id: UDG@20.15.2@MMLCommand@ADD PWDBLACKLIST
type: MMLCommand
name: ADD PWDBLACKLIST（增加密码禁用词）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: PWDBLACKLIST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 用户管理
- 密码黑名单
status: active
---

# ADD PWDBLACKLIST（增加密码禁用词）

## 功能

该命令用于增加密码禁用词。配置密码禁用词后，所有包含密码禁用词的字符串（不区分大小写）都不能被配置成本地用户的密码。可以通过执行查询本地用户（ [**LST OP**](../用户/查询本地用户（LST OP）_59036769.md) ）命令查看本地用户的信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为32。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FORBIDDENWORD | 密码禁用词 | 可选必选说明：必选参数<br>参数含义：密码禁用词。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。不区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PWDBLACKLIST]] · 密码禁用词（PWDBLACKLIST）

## 使用实例

设置字符a为密码禁用词：

```
ADD PWDBLACKLIST:FORBIDDENWORD="a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加密码禁用词（ADD-PWDBLACKLIST）_59036534.md`
