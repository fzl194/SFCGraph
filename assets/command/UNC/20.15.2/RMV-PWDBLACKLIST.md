---
id: UNC@20.15.2@MMLCommand@RMV PWDBLACKLIST
type: MMLCommand
name: RMV PWDBLACKLIST（删除密码禁用词）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PWDBLACKLIST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 用户管理
- 密码黑名单
status: active
---

# RMV PWDBLACKLIST（删除密码禁用词）

## 功能

该命令用于删除密码禁用词。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FORBIDDENWORD | 密码禁用词 | 可选必选说明：必选参数<br>参数含义：密码禁用词。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。不区分大小写。不能包含一些特殊字符，如问号和分号等。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PWDBLACKLIST]] · 密码禁用词（PWDBLACKLIST）

## 使用实例

删除密码禁用词a：

```
RMV PWDBLACKLIST:FORBIDDENWORD="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除密码禁用词（RMV-PWDBLACKLIST）_59036566.md`
