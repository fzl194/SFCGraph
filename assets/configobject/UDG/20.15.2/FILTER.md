---
id: UDG@20.15.2@ConfigObject@FILTER
type: ConfigObject
name: FILTER（过滤器）
nf: UDG
version: 20.15.2
object_name: FILTER
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# FILTER（过滤器）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加过滤器，其中包含三、四层的协议、源端口号、目的端口号、源IP地址和目的IP地址等。数据报文通过时，系统会根据过滤器选择到对应的规则，然后执行选中规则对应的计费策略和动作策略。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-FILTER]] · ADD FILTER
- [[command/UDG/20.15.2/LST-FILTER]] · LST FILTER
- [[command/UDG/20.15.2/MOD-FILTER]] · MOD FILTER
- [[command/UDG/20.15.2/RMV-FILTER]] · RMV FILTER

## 关联对象

- [[configobject/UDG/20.15.2/FLTBINDFLOWF]] · FLTBINDFLOWF
- [[configobject/UDG/20.15.2/HOST]] · HOST
- [[configobject/UDG/20.15.2/IPLIST]] · IPLIST

## 证据

- 原始手册：`evidence/UDG/20.15.2/FILTER.md`
- 原始手册：`evidence/UDG/20.15.2/FILTER.md`
- 原始手册：`evidence/UDG/20.15.2/FILTER.md`
- 原始手册：`evidence/UDG/20.15.2/FILTER.md`
