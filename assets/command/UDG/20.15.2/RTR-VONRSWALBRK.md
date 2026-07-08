---
id: UDG@20.15.2@MMLCommand@RTR VONRSWALBRK
type: MMLCommand
name: RTR VONRSWALBRK（恢复VoNR滑窗相关的参数）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VONRSWALBRK
command_category: 动作类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR吞字断续配置
status: active
---

# RTR VONRSWALBRK（恢复VoNR滑窗相关的参数）

## 功能

**适用NF：UPF**

该命令用户恢复VoNR滑窗相关的参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VONRSWALBRK]] · VoNR滑窗相关的参数（VONRSWALBRK）

## 使用实例

恢复VoNR滑窗相关的参数：

```
RTR VONRSWALBRK:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-VONRSWALBRK.md`
