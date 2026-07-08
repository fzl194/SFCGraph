---
id: UNC@20.15.2@ConfigObject@LOCBINDN2TAI
type: ConfigObject
name: LOCBINDN2TAI（UPF位置信息与UPF优先支持的5G TAI范围的绑定关系）
nf: UNC
version: 20.15.2
object_name: LOCBINDN2TAI
object_kind: binding
applicable_nf:
- SMF
status: active
---

# LOCBINDN2TAI（UPF位置信息与UPF优先支持的5G TAI范围的绑定关系）

## 说明

**适用NF：SMF**

该命令用于增加UPF位置信息与UPF优先支持的TAI范围的绑定关系。

在用户激活时，SMF从激活请求中获取用户位置信息，在为用户选择UPF时，会优先选择包含用户位置信息的已绑定TAI域的UPF，以获得更好的服务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LOCBINDN2TAI]] · ADD LOCBINDN2TAI
- [[command/UNC/20.15.2/LST-LOCBINDN2TAI]] · LST LOCBINDN2TAI
- [[command/UNC/20.15.2/RMV-LOCBINDN2TAI]] · RMV LOCBINDN2TAI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UPF位置信息与UPF优先支持的5G-TAI范围的绑定关系（RMV-LOCBINDN2TAI）_96242799.md`
- 原始手册：`evidence/UNC/20.15.2/增加UPF位置信息与UPF优先支持的5G-TAI范围的绑定关系（ADD-LOCBINDN2TAI）_96241683.md`
- 原始手册：`evidence/UNC/20.15.2/查询UPF位置信息与UPF优先支持的5G-TAI范围的绑定关系（LST-LOCBINDN2TAI）_96242188.md`
