---
id: UNC@20.15.2@ConfigObject@DYNDIAMAAA
type: ConfigObject
name: DYNDIAMAAA（动态Diameter AAA服务器）
nf: UNC
version: 20.15.2
object_name: DYNDIAMAAA
object_kind: query_target
applicable_nf:
- PGW-C
status: active
---

# DYNDIAMAAA（动态Diameter AAA服务器）

## 说明

**适用NF：PGW-C**

此命令用于显示动态Diameter AAA主机列表项。一次最多显示2000条记录，超过2000条记录将不再显示。

- 如果指定主机名，则显示指定的动态Diameter AAA表项。
- 如果不指定主机名，则显示所有动态Diameter AAA主机表项。

## 操作本对象的命令

- [DSP DYNDIAMAAA](command/UNC/20.15.2/DSP-DYNDIAMAAA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示动态Diameter-AAA服务器（DSP-DYNDIAMAAA）_96241958.md`
