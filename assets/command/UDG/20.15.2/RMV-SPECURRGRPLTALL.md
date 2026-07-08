---
id: UDG@20.15.2@MMLCommand@RMV SPECURRGRPLTALL
type: MMLCommand
name: RMV SPECURRGRPLTALL（删除所有特殊URR组列表）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SPECURRGRPLTALL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 特殊使用率上报规则组列表
status: active
---

# RMV SPECURRGRPLTALL（删除所有特殊URR组列表）

## 功能

**适用NF：PGW-U、UPF**

![](删除所有特殊URR组列表（RMV SPECURRGRPLTALL）_05776418.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除所有特殊URR组列表可能会影响业务匹配结果，导致用户业务受损，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除所有特殊URR组列表配置。

## 注意事项

- 该命令执行后立即生效。
- 当配置量较大时单次执行可能无法删除全部记录，需要执行多次。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [所有特殊URR组列表（SPECURRGRPLTALL）](configobject/UDG/20.15.2/SPECURRGRPLTALL.md)

## 使用实例

删除所有配置的特殊URR组列表：

```
RMV SPECURRGRPLTALL:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除所有特殊URR组列表（RMV-SPECURRGRPLTALL）_05776418.md`
