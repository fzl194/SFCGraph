---
id: UNC@20.15.2@ConfigObject@AGFOUTFC
type: ConfigObject
name: AGFOUTFC（出局流控参数）
nf: UNC
version: 20.15.2
object_name: AGFOUTFC
object_kind: global_setting
applicable_nf:
- NCG
status: active
---

# AGFOUTFC（出局流控参数）

## 说明

**适用NF：NCG**

该命令用于设置出局流控参数。

当AGF转发消息给对端网元(如OCS或SCP)，对端网元出现异常无法处理计费请求时，为避免大量的异常消息导致服务内部资源过载，通过该命令设置流控参数，控制NCG转发计费消息到对端网元的频率，减少服务内部资源的消耗和对对端网元的冲击压力。

该命令有4种模式：全局流控，会话级流控，隔离全部OCS，按消息步长流控。

1）会话级流控模式：会话级流控模式，分为3种状态：正常状态、流控状态、待决状态。当设置为会话级流控模式时，。

正常状态或待决状态下：AGF会转发在线计费消息给对端网元。

流控状态下：AGF则会直接代应答该会话的在线消息。

2）全局流控模式：全局流控模式，也分为3种状态:正常状态、流控状态、待决状态。当设置为全局流控模式时，。

正常状态下：AGF会转发所有的在线计费消息给对端网元。

流控状态下：AGF会直接代应答转发给该对端网元的所有在线消息。

待决状态：AGF会转发所有的在线计费消息给对端网元，拥塞计数次数达到阈值，会直接进入拥塞状态。

3）隔离全部OCS模式。当设置为隔离全部OCS模式时，AGF会直接代应答所有的在线消息，不转发给对端网元。

4）消息步长流控模式。当设置为消息步长流控模式时，在线计费消息按照条数间隔转发OCS。

## 操作本对象的命令

- [LST AGFOUTFC](command/UNC/20.15.2/LST-AGFOUTFC.md)
- [SET AGFOUTFC](command/UNC/20.15.2/SET-AGFOUTFC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询出局流控参数（LST-AGFOUTFC）_32847667.md`
- 原始手册：`evidence/UNC/20.15.2/设置出局流控参数（SET-AGFOUTFC）_87446492.md`
