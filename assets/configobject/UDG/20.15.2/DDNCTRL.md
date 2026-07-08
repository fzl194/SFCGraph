---
id: UDG@20.15.2@ConfigObject@DDNCTRL
type: ConfigObject
name: DDNCTRL（DDN控制策略）
nf: UDG
version: 20.15.2
object_name: DDNCTRL
object_kind: global_setting
applicable_nf:
- SGW-U
- UPF
status: active
---

# DDNCTRL（DDN控制策略）

## 说明

**适用NF：SGW-U、UPF**

该命令用来控制报文DDN触发策略。可以通过设置TCP信令报文或流的动作为阻塞的报文不触发DDN消息，来降低呼叫负载。其中TCP信令报文包含FIN，FIN ACK，RST，RST ACK报文。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DDNCTRL]] · LST DDNCTRL
- [[command/UDG/20.15.2/SET-DDNCTRL]] · SET DDNCTRL

## 证据

- 原始手册：`evidence/UDG/20.15.2/DDNCTRL.md`
- 原始手册：`evidence/UDG/20.15.2/DDNCTRL.md`
