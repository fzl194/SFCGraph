---
id: UDG@20.15.2@ConfigObject@AUTOLOGPOLICY
type: ConfigObject
name: AUTOLOGPOLICY（日志自动备份策略）
nf: UDG
version: 20.15.2
object_name: AUTOLOGPOLICY
object_kind: global_setting
status: active
---

# AUTOLOGPOLICY（日志自动备份策略）

## 说明

本命令用于设置日志自动备份到第三方服务器的备份策略。备份策略是指自动备份审计日志到第三方服务器的备份周期、备份SFTP服务器参数等信息。

> **说明**
> - 该命令存在系统初始记录，参数OPERATORTPYE(操作类型)的初始设定值为OFF(关闭)。
> - 根据备份周期进行备份，备份日志内容包含操作日志5000条、安全日志5000条和系统日志5000条。
> - SFTP服务器端口默认使用22，如果实际环境中端口有变更需要使用**[ADD FWRULE](../../系统管理/路由管理/代理管理/增加转发规则（ADD FWRULE）_01524840.md)**命令增加转发规则。

## 操作本对象的命令

- [LST AUTOLOGPOLICY](command/UDG/20.15.2/LST-AUTOLOGPOLICY.md)
- [SET AUTOLOGPOLICY](command/UDG/20.15.2/SET-AUTOLOGPOLICY.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询日志自动备份策略（LST-AUTOLOGPOLICY）_89951696.md`
- 原始手册：`evidence/UDG/20.15.2/设置日志自动备份策略（SET-AUTOLOGPOLICY）_89632096.md`
