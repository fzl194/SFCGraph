---
id: UDG@20.15.2@MMLCommand@RTR VOLTEMOSALMTHD
type: MMLCommand
name: RTR VOLTEMOSALMTHD（恢复异常MOS告警阈值为系统初始设置值）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VOLTEMOSALMTHD
command_category: 动作类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- MOS值异常的用户比例告警阈值
status: active
---

# RTR VOLTEMOSALMTHD（恢复异常MOS告警阈值为系统初始设置值）

## 功能

**适用NF：PGW-U**

该命令用于恢复MOS值异常的呼叫比例告警阈值和恢复告警阈值为系统初始设置值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VOLTEMOSALMTHD]] · 异常MOS告警阈值为系统初始设置值（VOLTEMOSALMTHD）

## 使用实例

恢复MOS值异常的呼叫比例告警阈值和恢复告警阈值为系统初始设置值：

```
RTR VOLTEMOSALMTHD:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-VOLTEMOSALMTHD.md`
