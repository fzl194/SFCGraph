---
id: UNC@20.15.2@MMLCommand@LST NSARATVALUE
type: MMLCommand
name: LST NSARATVALUE（查询NSA用户的RAT值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSARATVALUE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- NSA用户RAT值
status: active
---

# LST NSARATVALUE（查询NSA用户的RAT值）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于查询终端作为NSA用户时，UNC给周边网元发送消息中RAT信元携带的值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSARATVALUE]] · NSA用户的RAT值（NSARATVALUE）

## 使用实例

查询终端作为NSA用户时，UNC给周边网元发送的消息中RAT信元携带的值：

```
LST NSARATVALUE:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSARATVALUE.md`
