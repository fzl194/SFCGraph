---
id: UNC@20.15.2@MMLCommand@STP VLRFAULTEXIT
type: MMLCommand
name: STP VLRFAULTEXIT（停止用户退出VLR故障增强状态）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: VLRFAULTEXIT
command_category: 动作类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- VLR故障增强功能
status: active
---

# STP VLRFAULTEXIT（停止用户退出VLR故障增强状态）

## 功能

**适用网元：MME**

该命令用于停止用户退出VLR故障增强状态的任务。当系统中执行了用户退出VLR故障增强状态( [STR VLRFAULTEXIT](启动用户退出VLR故障增强状态(STR VLRFAULTEXIT)_92963924.md) )命令时，希望中途停止退出VLR故障增强状态任务，可以执行该命令。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [用户退出VLR故障增强状态（VLRFAULTEXIT）](configobject/UNC/20.15.2/VLRFAULTEXIT.md)

## 使用实例

停止用户退出VLR故障增强状态任务，可用如下命令。

```
STP VLRFAULTEXIT:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止用户退出VLR故障增强状态(STP-VLRFAULTEXIT)_93021280.md`
