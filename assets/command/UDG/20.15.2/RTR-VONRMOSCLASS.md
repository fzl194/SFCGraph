---
id: UDG@20.15.2@MMLCommand@RTR VONRMOSCLASS
type: MMLCommand
name: RTR VONRMOSCLASS（恢复MOS分类区间值）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VONRMOSCLASS
command_category: 动作类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR MOS分类
status: active
---

# RTR VONRMOSCLASS（恢复MOS分类区间值）

## 功能

**适用NF：UPF**

该命令用于恢复MOS分类区间边界值为系统初始设置值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [MOS分类区间值（VONRMOSCLASS）](configobject/UDG/20.15.2/VONRMOSCLASS.md)

## 使用实例

恢复MOS分类区间边界值为系统初始设置值，初始值见SET VONRABNORMOS：

```
RTR VONRMOSCLASS:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复MOS分类区间值（RTR-VONRMOSCLASS）_91295982.md`
