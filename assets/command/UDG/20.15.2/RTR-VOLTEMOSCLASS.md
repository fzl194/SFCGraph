---
id: UDG@20.15.2@MMLCommand@RTR VOLTEMOSCLASS
type: MMLCommand
name: RTR VOLTEMOSCLASS（恢复MOS分类区间值）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VOLTEMOSCLASS
command_category: 动作类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE MOS分类
status: active
---

# RTR VOLTEMOSCLASS（恢复MOS分类区间值）

## 功能

**适用NF：PGW-U**

该命令用于恢复MOS分类区间边界值为系统初始设置值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VOLTEMOSCLASS]] · MOS分类区间值（VOLTEMOSCLASS）

## 使用实例

恢复MOS分类区间边界值为系统初始设置值：

```
RTR VOLTEMOSCLASS:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-VOLTEMOSCLASS.md`
