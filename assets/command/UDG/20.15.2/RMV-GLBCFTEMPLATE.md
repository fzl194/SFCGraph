---
id: UDG@20.15.2@MMLCommand@RMV GLBCFTEMPLATE
type: MMLCommand
name: RMV GLBCFTEMPLATE（删除全局内容过滤模板）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: GLBCFTEMPLATE
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
- 全局内容过滤模板绑定配置
status: active
---

# RMV GLBCFTEMPLATE（删除全局内容过滤模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除全局的内容过滤模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBCFTEMPLATE]] · 全局内容过滤模板（GLBCFTEMPLATE）

## 使用实例

删除全局的内容过滤模板：

```
RMV GLBCFTEMPLATE:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除全局内容过滤模板（RMV-GLBCFTEMPLATE）_51429108.md`
