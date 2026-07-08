---
id: UDG@20.15.2@MMLCommand@RMV MULTREDIRECT
type: MMLCommand
name: RMV MULTREDIRECT（删除多级重定向密码）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MULTREDIRECT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 多级重定向控制
- 多级重定向密码
status: active
---

# RMV MULTREDIRECT（删除多级重定向密码）

## 功能

**适用NF：PGW-U、UPF**

![](删除多级重定向密码（RMV MULTREDIRECT）_06232192.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除多级重定向字段加密的密码可能会影响用户多级重定向字段加密业务，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除多级重定向字段加密的密码。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/MULTREDIRECT]] · 多级重定向密码（MULTREDIRECT）

## 使用实例

假如运营商想要删除加密密码，配置如下：

```
RMV MULTREDIRECT:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除多级重定向密码（RMV-MULTREDIRECT）_06232192.md`
