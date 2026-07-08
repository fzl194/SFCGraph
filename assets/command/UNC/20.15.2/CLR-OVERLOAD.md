---
id: UNC@20.15.2@MMLCommand@CLR OVERLOAD
type: MMLCommand
name: CLR OVERLOAD（清除过载控制记录信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: OVERLOAD
command_category: 动作类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 过载控制信息维护
status: active
---

# CLR OVERLOAD（清除过载控制记录信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来清除过载控制的信息。当需要用户在下次激活时能成为正常的用户，从而让用户获得正常的业务服务，需要清除过载控制的信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/OVERLOAD]] · 过载控制记录信息（OVERLOAD）

## 使用实例

为了让用户下次能正常激活，需要删除信令抑制列表。清空信令抑制列表中的记录信息：

```
CLR OVERLOAD:
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除过载控制记录信息（CLR-OVERLOAD）_82242443.md`
