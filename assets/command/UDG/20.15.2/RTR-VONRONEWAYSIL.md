---
id: UDG@20.15.2@MMLCommand@RTR VONRONEWAYSIL
type: MMLCommand
name: RTR VONRONEWAYSIL（恢复单通检测的系统初始设置值）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VONRONEWAYSIL
command_category: 动作类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR单通检测
status: active
---

# RTR VONRONEWAYSIL（恢复单通检测的系统初始设置值）

## 功能

**适用NF：UPF**

该命令用于恢复单通检测信息的系统初始设置值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VONRONEWAYSIL]] · 单通检测的系统初始设置值（VONRONEWAYSIL）

## 使用实例

恢复单通检测信息的系统初始设置值：

```
RTR VONRONEWAYSIL:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复单通检测的系统初始设置值（RTR-VONRONEWAYSIL）_94614219.md`
