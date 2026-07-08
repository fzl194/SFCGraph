---
id: UDG@20.15.2@MMLCommand@RMV CFPROFILE
type: MMLCommand
name: RMV CFPROFILE（删除内容过滤策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CFPROFILE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤策略配置
status: active
---

# RMV CFPROFILE（删除内容过滤策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除内容过滤策略。

## 注意事项

- 该命令执行后立即生效。
- 如果CFPROFILE被CFPROFBINDCFT引用，则不允许被删除，需要先删除绑定关系。
- 如果CFPROFILE被CONTCATEGBIND引用，可以删除CFPROFILE，同时删除绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFPROFILENAME | 内容过滤策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [内容过滤策略（CFPROFILE）](configobject/UDG/20.15.2/CFPROFILE.md)

## 使用实例

删除指定名字的CFPROFILE：

```
RMV CFPROFILE: CFPROFILENAME="cfp1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除内容过滤策略（RMV-CFPROFILE）_39957524.md`
