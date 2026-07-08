---
id: UDG@20.15.2@MMLCommand@RTR GLBNSHHDNPLY
type: MMLCommand
name: RTR GLBNSHHDNPLY（恢复NSH头增强全局策略）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: GLBNSHHDNPLY
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- NSH头增强
- NSH全局策略
status: active
---

# RTR GLBNSHHDNPLY（恢复NSH头增强全局策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于恢复NSH头增强全局策略为系统初始设置值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBNSHHDNPLY]] · NSH头增强全局策略（GLBNSHHDNPLY）

## 使用实例

恢复NSH头增强全局策略为系统初始设置值：

```
RTR GLBNSHHDNPLY:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-GLBNSHHDNPLY.md`
