---
id: UDG@20.15.2@MMLCommand@RTR FUIENRICHMENT
type: MMLCommand
name: RTR FUIENRICHMENT（恢复FUI增强参数）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: FUIENRICHMENT
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- FUI重定向控制
- FUI增强
status: active
---

# RTR FUIENRICHMENT（恢复FUI增强参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于恢复FUI增强参数。控制处理重定向动作，当URL是由OCS下发的FUI URL时，可根据配置判断是否绑定重定向携带信息名称。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [FUI增强参数（FUIENRICHMENT）](configobject/UDG/20.15.2/FUIENRICHMENT.md)

## 使用实例

假如运营商想要恢复默认配置，即报文中不携带URL等信息，使用此命令：

```
RTR FUIENRICHMENT:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复FUI增强参数（RTR-FUIENRICHMENT）_82837536.md`
