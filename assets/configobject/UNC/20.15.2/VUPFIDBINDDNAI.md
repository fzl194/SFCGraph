---
id: UNC@20.15.2@ConfigObject@VUPFIDBINDDNAI
type: ConfigObject
name: VUPFIDBINDDNAI（虚拟UPF实例标识的DNAI）
nf: UNC
version: 20.15.2
object_name: VUPFIDBINDDNAI
object_kind: binding
applicable_nf:
- SMF
status: active
---

# VUPFIDBINDDNAI（虚拟UPF实例标识的DNAI）

## 说明

**适用NF：SMF**

该命令用于增加虚拟UPF实例标识的DNAI。

在主锚点和辅锚点会话共部署或者多辅锚点会话共部署的场景下，SMF给虚拟UPF实例标识配置DNAI，并在辅锚点会话中下发到U面，U面根据该DNAI给辅锚点会话分配相应的VPN。

## 操作本对象的命令

- [ADD VUPFIDBINDDNAI](command/UNC/20.15.2/ADD-VUPFIDBINDDNAI.md)
- [LST VUPFIDBINDDNAI](command/UNC/20.15.2/LST-VUPFIDBINDDNAI.md)
- [RMV VUPFIDBINDDNAI](command/UNC/20.15.2/RMV-VUPFIDBINDDNAI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除虚拟UPF实例标识的DNAI（RMV-VUPFIDBINDDNAI）_96243050.md`
- 原始手册：`evidence/UNC/20.15.2/增加虚拟UPF实例标识的DNAI（ADD-VUPFIDBINDDNAI）_76311127.md`
- 原始手册：`evidence/UNC/20.15.2/查询虚拟UPF实例标识的DNAI（LST-VUPFIDBINDDNAI）_96242534.md`
