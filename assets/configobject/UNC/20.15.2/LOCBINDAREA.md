---
id: UNC@20.15.2@ConfigObject@LOCBINDAREA
type: ConfigObject
name: LOCBINDAREA（UPF位置信息与该UPF优先支持的服务区的绑定关系）
nf: UNC
version: 20.15.2
object_name: LOCBINDAREA
object_kind: binding
applicable_nf:
- SMF
- SGW-C
- GGSN
- PGW-C
status: active
---

# LOCBINDAREA（UPF位置信息与该UPF优先支持的服务区的绑定关系）

## 说明

**适用NF：SMF、SGW-C、GGSN、PGW-C**

该命令用于增加UPF位置信息与该UPF优先支持的服务区的绑定关系。

该命令配合ADD PNFSMFSERAREA使用，用于基于用户位置区信息选择UPF。ADD PNFSMFSERAREA配置了对端UPF为SMF提供的服务区域信息。一个UPF可能为SMF提供多个服务区域。

在用户激活时，SMF从激活请求中获取用户位置信息，从而获取用户所属的位置区名称。来自该位置区的用户可以优先匹配绑定服务区域的UPF，以获得更好的服务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LOCBINDAREA]] · ADD LOCBINDAREA
- [[command/UNC/20.15.2/LST-LOCBINDAREA]] · LST LOCBINDAREA
- [[command/UNC/20.15.2/RMV-LOCBINDAREA]] · RMV LOCBINDAREA

## 证据

- 原始手册：`evidence/UNC/20.15.2/LOCBINDAREA.md`
- 原始手册：`evidence/UNC/20.15.2/LOCBINDAREA.md`
- 原始手册：`evidence/UNC/20.15.2/LOCBINDAREA.md`
