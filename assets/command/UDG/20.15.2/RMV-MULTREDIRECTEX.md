---
id: UDG@20.15.2@MMLCommand@RMV MULTREDIRECTEX
type: MMLCommand
name: RMV MULTREDIRECTEX（删除扩展的多级重定向密码）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MULTREDIRECTEX
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 多级重定向控制
- 多级重定向密码扩展
status: active
---

# RMV MULTREDIRECTEX（删除扩展的多级重定向密码）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除多级重定向字段加密的密码。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MULTREDIRECTEX]] · 扩展的多级重定向密码（MULTREDIRECTEX）

## 使用实例

假如运营商想要删除加密密码，配置如下：

```
RMV MULTREDIRECTEX:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-MULTREDIRECTEX.md`
