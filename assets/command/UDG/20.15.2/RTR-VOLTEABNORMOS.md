---
id: UDG@20.15.2@MMLCommand@RTR VOLTEABNORMOS
type: MMLCommand
name: RTR VOLTEABNORMOS（恢复MOS值的异常门限为系统初始设置值）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VOLTEABNORMOS
command_category: 动作类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE MOS值的异常门限值
status: active
---

# RTR VOLTEABNORMOS（恢复MOS值的异常门限为系统初始设置值）

## 功能

**适用NF：PGW-U**

该命令用于恢复异常MOS值的门限值为系统初始设置值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [MOS值的异常门限为系统初始设置值（VOLTEABNORMOS）](configobject/UDG/20.15.2/VOLTEABNORMOS.md)

## 使用实例

恢复异常MOS值的门限值为系统初始设置值：

```
RTR VOLTEABNORMOS:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复MOS值的异常门限为系统初始设置值（RTR-VOLTEABNORMOS）_57538683.md`
