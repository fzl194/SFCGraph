---
id: UNC@20.15.2@MMLCommand@STP SMFEXITUDMBYPASS
type: MMLCommand
name: STP SMFEXITUDMBYPASS（停止会话退出UDM Bypass状态任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: SMFEXITUDMBYPASS
command_category: 动作类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- UDM Bypass管理
- 退出UDM Bypass
status: active
---

# STP SMFEXITUDMBYPASS（停止会话退出UDM Bypass状态任务）

## 功能

**适用NF：SMF**

该命令用于停止退出UDM Bypass。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [会话退出UDM Bypass状态任务（SMFEXITUDMBYPASS）](configobject/UNC/20.15.2/SMFEXITUDMBYPASS.md)

## 使用实例

当需要停止会话退出UDM Bypass任务，执行如下命令：

```
STP SMFEXITUDMBYPASS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止会话退出UDM-Bypass状态任务（STP-SMFEXITUDMBYPASS）_58800313.md`
