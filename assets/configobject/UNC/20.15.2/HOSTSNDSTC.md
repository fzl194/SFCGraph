---
id: UNC@20.15.2@ConfigObject@HOSTSNDSTC
type: ConfigObject
name: HOSTSNDSTC（发送方向协议报文统计计数）
nf: UNC
version: 20.15.2
object_name: HOSTSNDSTC
object_kind: action
status: active
---

# HOSTSNDSTC（发送方向协议报文统计计数）

## 说明

该命令用于查询发送方向协议报文统计计数。

查询之前需先配置全局协议报文统计配置；当删除全局协议报文统计配置时对应的统计计数将被清零。

当查询类型为RU_STC，不指定RUNAME参数时，查询所有资源单元的统计信息，当指定RUNAME参数时，可以查询指定资源单元的统计信息；不指定PROTTYPE参数时，查询所有协议类型的统计信息，当指定PROTTYPE参数时，可以查询指定协议类型的统计信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-HOSTSNDSTC]] · DSP HOSTSNDSTC
- [[command/UNC/20.15.2/RTR-HOSTSNDSTC]] · RTR HOSTSNDSTC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询发送方向协议报文统计计数（DSP-HOSTSNDSTC）_50281690.md`
- 原始手册：`evidence/UNC/20.15.2/清除发送方向协议报文统计计数（RTR-HOSTSNDSTC）_00866117.md`
