---
id: UDG@20.15.2@MMLCommand@RTR VOLTESWALBRK
type: MMLCommand
name: RTR VOLTESWALBRK（恢复VoLTE滑窗相关的参数）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VOLTESWALBRK
command_category: 动作类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE吞字断续配置
status: active
---

# RTR VOLTESWALBRK（恢复VoLTE滑窗相关的参数）

## 功能

**适用NF：PGW-U**

该命令用户恢复VoLTE滑窗相关的参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VOLTESWALBRK]] · VoLTE滑窗相关的参数（VOLTESWALBRK）

## 使用实例

恢复VoLTE滑窗相关的参数：

```
RTR VOLTESWALBRK:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复VoLTE滑窗相关的参数（RTR-VOLTESWALBRK）_57738489.md`
