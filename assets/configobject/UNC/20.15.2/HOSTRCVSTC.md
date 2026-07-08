---
id: UNC@20.15.2@ConfigObject@HOSTRCVSTC
type: ConfigObject
name: HOSTRCVSTC（接收方向协议报文统计计数）
nf: UNC
version: 20.15.2
object_name: HOSTRCVSTC
object_kind: action
status: active
---

# HOSTRCVSTC（接收方向协议报文统计计数）

## 说明

该命令用于查询接收方向协议报文统计计数。

当查询类型为IF_STC时，只显示统计计数非零的前十的接口统计信息，当不指定PROTTYPE查询时，查询结果不受开关控制。

当查询类型为PROT_STC，不指定IFNAME参数时，查询所有接口的统计信息；当指定IFNAME参数时，可以查询指定接口的统计信息。

查询之前需先配置全局或者接口协议报文统计配置；当删除全局或者接口协议报文统计配置时对应的统计计数将被清零。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-HOSTRCVSTC]] · DSP HOSTRCVSTC
- [[command/UNC/20.15.2/RTR-HOSTRCVSTC]] · RTR HOSTRCVSTC

## 证据

- 原始手册：`evidence/UNC/20.15.2/HOSTRCVSTC.md`
- 原始手册：`evidence/UNC/20.15.2/HOSTRCVSTC.md`
