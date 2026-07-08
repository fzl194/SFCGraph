---
id: UDG@20.15.2@MMLCommand@RTR NETYPE
type: MMLCommand
name: RTR NETYPE（恢复 NeType默认值）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: NETYPE
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- NE信息管理
- NE类型管理
status: active
---

# RTR NETYPE（恢复 NeType默认值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

恢复以license购买量上报的网元形态。

## 注意事项

该命令执行后立即生效。该命令执行后UDGNRMINTF表记录无法自动更新，需要根据具体网元形态使用SET NETYPE命令更新。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NETYPE]] ·  NeType默认值（NETYPE）

## 使用实例

恢复以license上报的网元形态：

```
RTR　NETYPE:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-NETYPE.md`
