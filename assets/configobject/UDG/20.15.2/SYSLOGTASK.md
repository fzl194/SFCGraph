---
id: UDG@20.15.2@ConfigObject@SYSLOGTASK
type: ConfigObject
name: SYSLOGTASK（上报任务）
nf: UDG
version: 20.15.2
object_name: SYSLOGTASK
object_kind: entity
status: active
---

# SYSLOGTASK（上报任务）

## 说明

![](设置上报任务（SET SYSLOGTASK）_36611107.assets/notice_3.0-zh-cn.png)

该命令为高危命令，设置Syslog任务参数，可能存在安全风险及影响Syslog服务器通信，具体参考参数说明，请谨慎执行。

本命令用于增加或者修改向Syslog服务端上报任务。

与 OM Portal 界面 “ 系统 > Syslog管理 ” 中配置作用相同。

> **说明**
> - 该命令存在系统初始记录，参数“ENABLE”的初始设置值为“DISABLE”。
> - 该命令下发时，如果命令携带的“SysLog服务器IP地址”参数对应的配置不存在，且当前已有的非网管Syslog配置记录数小于3，则会直接新增相关配置；否则返回错误码“101115 任务数量达到上限3个”。
> - 该命令不允许对网管Syslog日志收集服务器的配置进行变更。
> - 配置Syslog任务生效需要一定时间，建议执行该命令操作时间间隔1分钟。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SYSLOGTASK]] · LST SYSLOGTASK
- [[command/UDG/20.15.2/RMV-SYSLOGTASK]] · RMV SYSLOGTASK
- [[command/UDG/20.15.2/SET-SYSLOGTASK]] · SET SYSLOGTASK

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除上报任务（RMV-SYSLOGTASK）_02790369.md`
- 原始手册：`evidence/UDG/20.15.2/查询上报任务（LST-SYSLOGTASK）_36709385.md`
- 原始手册：`evidence/UDG/20.15.2/设置上报任务（SET-SYSLOGTASK）_36611107.md`
