---
id: UNC@20.15.2@ConfigObject@ATTACKDEFEND
type: ConfigObject
name: ATTACKDEFEND（攻击防范参数）
nf: UNC
version: 20.15.2
object_name: ATTACKDEFEND
object_kind: global_setting
status: active
---

# ATTACKDEFEND（攻击防范参数）

## 说明

该命令用于设置攻击防范参数，包含使能参数与CAR值参数；攻击防范通过分析本机上送IP报文的格式和内容，针对不同类型的攻击报文，采用不同的处理方法。

如果是畸形报文，则对其进行丢弃处理。

如果是分片报文，限制分片报文的速率，防止分片报文对CPU造成攻击，占用过多CPU和系统资源。

如果是SYN Flood报文，限制TCP-syn报文的速率，防止CPU处理TCP-syn报文占用过多资源。

如果是UDP Flood报文，对特定端口发送的UDP报文直接丢弃。

如果是ICMP Flood报文，限制ICMP-Flood报文的上送速率，防止CPU处理ICMP-Flood报文占用过多资源。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-ATTACKDEFEND]] · LST ATTACKDEFEND
- [[command/UNC/20.15.2/SET-ATTACKDEFEND]] · SET ATTACKDEFEND

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询攻击防范参数（LST-ATTACKDEFEND）_49961062.md`
- 原始手册：`evidence/UNC/20.15.2/设置攻击防范参数（SET-ATTACKDEFEND）_49961362.md`
