---
id: UDG@20.15.2@ConfigObject@QOSCARBURST
type: ConfigObject
name: QOSCARBURST（用户做car的参数）
nf: UDG
version: 20.15.2
object_name: QOSCARBURST
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# QOSCARBURST（用户做car的参数）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加用户流量管理时的突发尺寸（即令牌桶的深度）与流量速率对应关系的配置。用户流量速率与这个对应关系表进行比较得到对应的突发尺寸。配置这个突发尺寸是为了限制出现突发流量时所能支持的最大值，超过了这个值就会被丢弃，从而达到限制带宽的目的。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-QOSCARBURST]] · ADD QOSCARBURST
- [[command/UDG/20.15.2/LST-QOSCARBURST]] · LST QOSCARBURST
- [[command/UDG/20.15.2/MOD-QOSCARBURST]] · MOD QOSCARBURST
- [[command/UDG/20.15.2/RMV-QOSCARBURST]] · RMV QOSCARBURST

## 证据

- 原始手册：`evidence/UDG/20.15.2/QOSCARBURST.md`
- 原始手册：`evidence/UDG/20.15.2/QOSCARBURST.md`
- 原始手册：`evidence/UDG/20.15.2/QOSCARBURST.md`
- 原始手册：`evidence/UDG/20.15.2/QOSCARBURST.md`
