---
id: UDG@20.15.2@MMLCommand@ADD CFPROFBINDCFT
type: MMLCommand
name: ADD CFPROFBINDCFT（增加内容过滤策略绑定关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CFPROFBINDCFT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤策略绑定配置
status: active
---

# ADD CFPROFBINDCFT（增加内容过滤策略绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于将预先配置的内容过滤策略绑定到内容过滤模板中。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1000。
- 每个模板最大可以绑定10个策略。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFTEMPLATENAME | 内容过滤模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CFTEMPLATE命令配置生成。 |
| CFPROFILENAME | 内容过滤策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CFPROFILE命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [内容过滤策略绑定关系（CFPROFBINDCFT）](configobject/UDG/20.15.2/CFPROFBINDCFT.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00255]]

## 使用实例

将预先配置的内容过滤策略绑定到内容过滤模板中：

```
ADD CFPROFBINDCFT: CFTEMPLATENAME="test", CFPROFILENAME="testprofile";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加内容过滤策略绑定关系（ADD-CFPROFBINDCFT）_43236707.md`
