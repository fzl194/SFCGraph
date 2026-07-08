---
id: UDG@20.15.2@MMLCommand@RMV AFDNSCHKTPALL
type: MMLCommand
name: RMV AFDNSCHKTPALL（删除所有需要进行防欺诈检查的DNS报文类型）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AFDNSCHKTPALL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务防欺诈
- 根据报文类型进行的DNS防欺诈检测
status: active
---

# RMV AFDNSCHKTPALL（删除所有需要进行防欺诈检查的DNS报文类型）

## 功能

**适用NF：PGW-U、UPF**

![](删除所有需要进行防欺诈检查的DNS报文类型（RMV AFDNSCHKTPALL）_05543948.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除所有AfDnsCheckType可能会影响用户的业务，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除所有进行DNS防欺诈检查的DNS报文类型值。

## 注意事项

该命令执行后对新数据流生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [所有需要进行防欺诈检查的DNS报文类型（AFDNSCHKTPALL）](configobject/UDG/20.15.2/AFDNSCHKTPALL.md)

## 使用实例

如果运营商要删除所有进行DNS防欺诈检查的DNS报文类型值，则配置命令如下：

```
RMV AFDNSCHKTPALL:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除所有需要进行防欺诈检查的DNS报文类型（RMV-AFDNSCHKTPALL）_05543948.md`
