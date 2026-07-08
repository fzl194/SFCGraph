---
id: UDG@20.15.2@ConfigObject@PATHDWNALMGLO
type: ConfigObject
name: PATHDWNALMGLO（单条路径断告警抑制参数全局配置）
nf: UDG
version: 20.15.2
object_name: PATHDWNALMGLO
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# PATHDWNALMGLO（单条路径断告警抑制参数全局配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

由于现网传输的原因， eNodeB/gNodeB可能偶然出现路径中断，而由于短时间内的单条链路故障，对业务影响可控，客户并不特别关注，给客户的维护造成困扰。故而对于偶然闪断的链路，进行告警抑制，当中断超过一定的次数时，再上报此链路的故障告警。该命令用来设置ALM-81018 GTPU路径断告警抑制参数。

## 操作本对象的命令

- [LST PATHDWNALMGLO](command/UDG/20.15.2/LST-PATHDWNALMGLO.md)
- [SET PATHDWNALMGLO](command/UDG/20.15.2/SET-PATHDWNALMGLO.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询单条路径断告警抑制参数全局配置（LST-PATHDWNALMGLO）_82837864.md`
- 原始手册：`evidence/UDG/20.15.2/设置单条路径断告警抑制参数的全局配置（SET-PATHDWNALMGLO）_82837863.md`
