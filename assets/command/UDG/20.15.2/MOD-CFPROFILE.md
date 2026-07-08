---
id: UDG@20.15.2@MMLCommand@MOD CFPROFILE
type: MMLCommand
name: MOD CFPROFILE（修改内容过滤策略）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: CFPROFILE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤策略配置
status: active
---

# MOD CFPROFILE（修改内容过滤策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改内容过滤策略。

## 注意事项

该命令执行后只对之后发生承载更新的用户或者新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFPROFILENAME | 内容过滤策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于设置优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~65535。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CFPROFILE]] · 内容过滤策略（CFPROFILE）

## 使用实例

配置CFPROFILE，优先级修改成2：

```
MOD CFPROFILE: CFPROFILENAME="cfp1", PRIORITY=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-CFPROFILE.md`
