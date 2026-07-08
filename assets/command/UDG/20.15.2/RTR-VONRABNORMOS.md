---
id: UDG@20.15.2@MMLCommand@RTR VONRABNORMOS
type: MMLCommand
name: RTR VONRABNORMOS（恢复MOS值的异常门限为系统初始设置值）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VONRABNORMOS
command_category: 动作类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR MOS值的异常门限值
status: active
---

# RTR VONRABNORMOS（恢复MOS值的异常门限为系统初始设置值）

## 功能

**适用NF：UPF**

该命令用于恢复MOS值的异常门限值为系统初始设置值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VONRABNORMOS]] · MOS值的异常门限为系统初始设置值（VONRABNORMOS）

## 使用实例

恢复异常MOS值的门限值为系统初始设置值，初始值见SET VONRABNORMOS：

```
RTR VONRABNORMOS:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复MOS值的异常门限为系统初始设置值（RTR-VONRABNORMOS）_94774059.md`
