---
id: UDG@20.15.2@MMLCommand@RMV BWMRULEGLBALL
type: MMLCommand
name: RMV BWMRULEGLBALL（删除所有全局带宽管理规则）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: BWMRULEGLBALL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理规则
status: active
---

# RMV BWMRULEGLBALL（删除所有全局带宽管理规则）

## 功能

**适用NF：PGW-U、UPF**

![](删除所有全局带宽管理规则（RMV BWMRULEGLBALL）_08452607.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除所有BwmRuleGlobal会影响用户业务访问，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除所有全局业务带宽管理规则。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/BWMRULEGLBALL]] · 所有全局带宽管理规则（BWMRULEGLBALL）

## 使用实例

假如运营商需要删除所有已配置的全局带宽管理规则：

```
RMV BWMRULEGLBALL:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-BWMRULEGLBALL.md`
