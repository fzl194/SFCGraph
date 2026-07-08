---
id: UDG@20.15.2@MMLCommand@RMV AFPROXYSRVALL
type: MMLCommand
name: RMV AFPROXYSRVALL（删除所有防欺诈可信代理服务器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AFPROXYSRVALL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈可信代理服务器
status: active
---

# RMV AFPROXYSRVALL（删除所有防欺诈可信代理服务器）

## 功能

**适用NF：PGW-U、UPF**

![](删除所有防欺诈可信代理服务器（RMV AFPROXYSRVALL）_08935041.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除所有可信代理服务器可能会改变业务匹配结果，导致用户业务受损，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除所有配置的可信代理服务器IP。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AFPROXYSRVALL]] · 所有防欺诈可信代理服务器（AFPROXYSRVALL）

## 使用实例

删除所有配置的可信代理服务器地址：

```
RMV AFPROXYSRVALL:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-AFPROXYSRVALL.md`
