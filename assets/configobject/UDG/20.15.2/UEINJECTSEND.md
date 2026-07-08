---
id: UDG@20.15.2@ConfigObject@UEINJECTSEND
type: ConfigObject
name: UEINJECTSEND（发送UE灌包）
nf: UDG
version: 20.15.2
object_name: UEINJECTSEND
object_kind: action
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# UEINJECTSEND（发送UE灌包）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](发送UE灌包（ACT UEINJECTSEND）_82837098.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，使能UE灌包功能会导致CPU负载率增高和对应UE的计费问题，需使能灌包操作前确认是否可以实施此操作。

该命令用于配置是否向指定UE执行下行灌包。

## 操作本对象的命令

- [[command/UDG/20.15.2/ACT-UEINJECTSEND]] · ACT UEINJECTSEND

## 证据

- 原始手册：`evidence/UDG/20.15.2/发送UE灌包（ACT-UEINJECTSEND）_82837098.md`
