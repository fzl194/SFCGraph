---
id: UNC@20.15.2@ConfigObject@LOCBINDS1TAI
type: ConfigObject
name: LOCBINDS1TAI（UPF位置信息与UPF优先支持的4G TAI范围的绑定关系）
nf: UNC
version: 20.15.2
object_name: LOCBINDS1TAI
object_kind: binding
applicable_nf:
- SGW-C
status: active
---

# LOCBINDS1TAI（UPF位置信息与UPF优先支持的4G TAI范围的绑定关系）

## 说明

**适用NF：SGW-C**

该命令用于增加UPF位置信息与UPF优先支持的TAI范围的绑定关系。

在用户激活时，SMF从激活请求中获取用户位置信息，在为用户选择UPF时，会优先选择包含用户位置信息的已绑定TAI域的UPF，以获得更好的服务。

## 操作本对象的命令

- [ADD LOCBINDS1TAI](command/UNC/20.15.2/ADD-LOCBINDS1TAI.md)
- [LST LOCBINDS1TAI](command/UNC/20.15.2/LST-LOCBINDS1TAI.md)
- [RMV LOCBINDS1TAI](command/UNC/20.15.2/RMV-LOCBINDS1TAI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UPF位置信息与UPF优先支持的4G-TAI范围的绑定关系（RMV-LOCBINDS1TAI）_96242800.md`
- 原始手册：`evidence/UNC/20.15.2/增加UPF位置信息与UPF优先支持的4G-TAI范围的绑定关系（ADD-LOCBINDS1TAI）_96241684.md`
- 原始手册：`evidence/UNC/20.15.2/查询UPF位置信息与UPF优先支持的4G-TAI范围的绑定关系（LST-LOCBINDS1TAI）_96242189.md`
