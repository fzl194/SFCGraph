---
id: UDG@20.15.2@MMLCommand@RMV CFPROFBINDCFT
type: MMLCommand
name: RMV CFPROFBINDCFT（删除内容过滤策略绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CFPROFBINDCFT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤策略绑定配置
status: active
---

# RMV CFPROFBINDCFT（删除内容过滤策略绑定关系）

## 功能

**适用NF：PGW-U、UPF**

![](删除内容过滤策略绑定关系（RMV CFPROFBINDCFT）_39239150.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除内容过滤模板与内容过滤策略间指定或所有的绑定关系，可能影响url过滤结果，请谨慎使用。

该命令用于将配置的内容过滤策略从内容过滤模板中删除。

## 注意事项

该命令执行后只对之后发生承载更新的用户或者新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFTEMPLATENAME | 内容过滤模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容过滤模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CFTEMPLATE命令配置生成。 |
| CFPROFILENAME | 内容过滤策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CFPROFILE命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFPROFBINDCFT]] · 内容过滤策略绑定关系（CFPROFBINDCFT）

## 使用实例

将配置的内容过滤策略从内容过滤模板中删除：

```
RMV CFPROFBINDCFT: CFTEMPLATENAME="test", CFPROFILENAME="testprofile";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除内容过滤策略绑定关系（RMV-CFPROFBINDCFT）_39239150.md`
