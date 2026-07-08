---
id: UDG@20.15.2@MMLCommand@RMV CFTEMPLATE
type: MMLCommand
name: RMV CFTEMPLATE（删除内容过滤模板）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CFTEMPLATE
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
- 内容过滤模板配置
status: active
---

# RMV CFTEMPLATE（删除内容过滤模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除一个内容过滤模板的配置。

## 注意事项

- 该命令执行后立即生效。
- 如果内容过滤模板绑定了内容过滤策略，则不允许删除，需要执行命令RMV CFPROFBINDCFT接触绑定关系后再删除。
- 如果内容过滤模板绑定了APN，则不允许删除，需要执行命令RMV APNCFTEMPLATE接触绑定关系后再删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFTEMPLATENAME | 内容过滤模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [内容过滤模板（CFTEMPLATE）](configobject/UDG/20.15.2/CFTEMPLATE.md)

## 使用实例

删除一个内容过滤模板的配置：

```
RMV CFTEMPLATE: CFTEMPLATENAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除内容过滤模板（RMV-CFTEMPLATE）_74191815.md`
