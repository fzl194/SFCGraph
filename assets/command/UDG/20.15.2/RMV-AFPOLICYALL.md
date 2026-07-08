---
id: UDG@20.15.2@MMLCommand@RMV AFPOLICYALL
type: MMLCommand
name: RMV AFPOLICYALL（删除所有防欺诈策略配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AFPOLICYALL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈策略
status: active
---

# RMV AFPOLICYALL（删除所有防欺诈策略配置）

## 功能

**适用NF：PGW-U、UPF**

![](删除所有防欺诈策略配置（RMV AFPOLICYALL）_08772495.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除所有的防欺诈配置后，功能可能不正常，不要一次性删除所有的防欺诈配置。

该命令用于删除所有判断出欺诈行为后的处理策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFPOLICYALL]] · 所有防欺诈策略配置（AFPOLICYALL）

## 使用实例

如果运营商要删除所有在判断出欺诈行为后处理策略，则配置命令如下：

```
RMV AFPOLICYALL:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-AFPOLICYALL.md`
