---
id: UDG@20.15.2@MMLCommand@ACT STOPDEASESSION
type: MMLCommand
name: ACT STOPDEASESSION（停止去活用户的处理）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: STOPDEASESSION
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 会话去活
status: active
---

# ACT STOPDEASESSION（停止去活用户的处理）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

执行DEA SESSION命令后，如果需要系统停止主动去激活用户时，执行该命令。执行该命令后，系统停止主动去激活用户。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [去活用户的处理（STOPDEASESSION）](configobject/UDG/20.15.2/STOPDEASESSION.md)

## 使用实例

停止手动批量去激活用户：

```
ACT STOPDEASESSION:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/停止去活用户的处理（ACT-STOPDEASESSION）_97358672.md`
