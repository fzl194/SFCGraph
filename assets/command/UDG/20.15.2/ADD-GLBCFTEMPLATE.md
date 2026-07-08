---
id: UDG@20.15.2@MMLCommand@ADD GLBCFTEMPLATE
type: MMLCommand
name: ADD GLBCFTEMPLATE（增加全局内容过滤模板）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: GLBCFTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 全局内容过滤模板绑定配置
status: active
---

# ADD GLBCFTEMPLATE（增加全局内容过滤模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置全局的内容过滤模板。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFTEMPLATENAME | 内容过滤模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤模板名称。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：该参数使用ADD CFTEMPLATE命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBCFTEMPLATE]] · 全局内容过滤模板（GLBCFTEMPLATE）

## 使用实例

配置全局的内容过滤模板：

```
ADD GLBCFTEMPLATE: CFTEMPLATENAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-GLBCFTEMPLATE.md`
