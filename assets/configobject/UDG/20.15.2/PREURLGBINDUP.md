---
id: UDG@20.15.2@ConfigObject@PREURLGBINDUP
type: ConfigObject
name: PREURLGBINDUP（用户模板的前缀URL组绑定关系）
nf: UDG
version: 20.15.2
object_name: PREURLGBINDUP
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# PREURLGBINDUP（用户模板的前缀URL组绑定关系）

## 说明

**适用NF：PGW-U、UPF**

该命令用于新增用户模板与前缀URL组的绑定关系，若用户使用的用户模板中绑定了一个或多个前缀URL组，且当前用户访问的业务为前缀URL业务，则会启动前缀URL的过滤。若访问的业务命中前缀URL，则会进行URL的截断，使用前缀URL之后的内容作为URL，进行计费和业务控制处理。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-PREURLGBINDUP]] · ADD PREURLGBINDUP
- [[command/UDG/20.15.2/LST-PREURLGBINDUP]] · LST PREURLGBINDUP
- [[command/UDG/20.15.2/RMV-PREURLGBINDUP]] · RMV PREURLGBINDUP

## 证据

- 原始手册：`evidence/UDG/20.15.2/PREURLGBINDUP.md`
- 原始手册：`evidence/UDG/20.15.2/PREURLGBINDUP.md`
- 原始手册：`evidence/UDG/20.15.2/PREURLGBINDUP.md`
