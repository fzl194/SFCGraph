---
id: UDG@20.15.2@MMLCommand@STP PDNROUTETST
type: MMLCommand
name: STP PDNROUTETST（停止PDN侧路由探测）
nf: UDG
version: 20.15.2
verb: STP
object_keyword: PDNROUTETST
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- PDN侧路由探测
status: active
---

# STP PDNROUTETST（停止PDN侧路由探测）

## 功能

**适用NF：PGW-U、UPF**

该命令用来控制UPF停止向PDN服务器发送探测消息，立刻结束探测。

## 注意事项

- 该命令执行后立即生效。
- 执行此命令后，UPF会立刻停止向PDN服务器发送探测消息，UPF的未被探测到的发布路由网段将不会被探测到。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PDNROUTETST]] · PDN侧路由探测（PDNROUTETST）

## 使用实例

停止探测路由是否可达：

```
STP PDNROUTETST:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/停止PDN侧路由探测（STP-PDNROUTETST）_70824403.md`
