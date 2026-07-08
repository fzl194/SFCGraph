---
id: UNC@20.15.2@MMLCommand@STP HSSBPEXIT
type: MMLCommand
name: STP HSSBPEXIT（停止用户退出HSS BYPASS状态）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: HSSBPEXIT
command_category: 动作类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS故障BYPASS功能
status: active
---

# STP HSSBPEXIT（停止用户退出HSS BYPASS状态）

## 功能

**适用网元：MME**

该命令用于停止用户手动退出HSS BYPASS状态的任务。当系统中执行了用户退出HSS BYPASS状态( **[STR HSSBPEXIT](启动用户退出HSS BYPASS状态(STR HSSBPEXIT)_20995641.md)** )命令时，希望中途停止手动退出HSS BYPASS状态任务，可以执行该命令。

## 注意事项

- 该命令执行后立即生效。
- 相关license授权并开启后，此命令配置才能执行（License部件编码：LKV2HSSBP01）。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HSSBPEXIT]] · 用户退出HSS BYPASS状态（HSSBPEXIT）

## 使用实例

停止用户退出HSS BYPASS状态任务，可用如下命令。

```
STP HSSBPEXIT:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STP-HSSBPEXIT.md`
