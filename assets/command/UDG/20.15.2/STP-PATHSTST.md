---
id: UDG@20.15.2@MMLCommand@STP PATHSTST
type: MMLCommand
name: STP PATHSTST（停止批量路径探测）
nf: UDG
version: 20.15.2
verb: STP
object_keyword: PATHSTST
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP路径测试
- 批量路径探测
status: active
---

# STP PATHSTST（停止批量路径探测）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来停止UPF与UPF之间、UPF与gNodeB之间、SGW-U与eNodeB之间、SGW-U与RNC之间、PGW-U与RNC之间、UPF与SMF之间、PGW-U与SGW-U之间数据面路径的批量探测。

## 注意事项

- 该命令执行后立即生效。
- 批量探测信号发送次数有默认值，如果不停止发送，则发送完毕默认次数后，自动停止发送。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PATHSTST]] · 批量路径探测（PATHSTST）

## 使用实例

停止本次探测：

```
STP PATHSTST:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/STP-PATHSTST.md`
