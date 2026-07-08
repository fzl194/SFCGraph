---
id: UDG@20.15.2@ConfigObject@PATHDWNALMSEG
type: ConfigObject
name: PATHDWNALMSEG（单条路径断告警抑制参数的分段配置）
nf: UDG
version: 20.15.2
object_name: PATHDWNALMSEG
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# PATHDWNALMSEG（单条路径断告警抑制参数的分段配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

由于现网传输的原因，部分eNodeB/gNodeB可能偶然出现中断，而由于短时间内的单条链路故障，对业务影响可控，客户并不特别关注，但是给客户的维护人员造成困扰。故而对于偶然闪断的链路，进行告警抑制，当中断超过一定的次数时，再上报此链路的故障告警（ALM-81018 GTPU路径断）。该命令用来配置指定eNodeB/gNodeB地址段内的单条路径断告警抑制。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-PATHDWNALMSEG]] · ADD PATHDWNALMSEG
- [[command/UDG/20.15.2/LST-PATHDWNALMSEG]] · LST PATHDWNALMSEG
- [[command/UDG/20.15.2/MOD-PATHDWNALMSEG]] · MOD PATHDWNALMSEG
- [[command/UDG/20.15.2/RMV-PATHDWNALMSEG]] · RMV PATHDWNALMSEG

## 证据

- 原始手册：`evidence/UDG/20.15.2/PATHDWNALMSEG.md`
- 原始手册：`evidence/UDG/20.15.2/PATHDWNALMSEG.md`
- 原始手册：`evidence/UDG/20.15.2/PATHDWNALMSEG.md`
- 原始手册：`evidence/UDG/20.15.2/PATHDWNALMSEG.md`
