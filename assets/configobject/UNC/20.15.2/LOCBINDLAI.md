---
id: UNC@20.15.2@ConfigObject@LOCBINDLAI
type: ConfigObject
name: LOCBINDLAI（UPF位置信息与UPF优先支持的LAI范围的绑定关系）
nf: UNC
version: 20.15.2
object_name: LOCBINDLAI
object_kind: binding
applicable_nf:
- GGSN
status: active
---

# LOCBINDLAI（UPF位置信息与UPF优先支持的LAI范围的绑定关系）

## 说明

**适用NF：GGSN**

该命令用于增加UPF位置信息与UPF优先支持的LAI范围的绑定关系。

在用户激活时，SMF从激活请求中获取用户位置信息，在为用户选择UPF时，会优先选择包含用户位置信息的已绑定LAI域的UPF，以获得更好的服务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LOCBINDLAI]] · ADD LOCBINDLAI
- [[command/UNC/20.15.2/LST-LOCBINDLAI]] · LST LOCBINDLAI
- [[command/UNC/20.15.2/RMV-LOCBINDLAI]] · RMV LOCBINDLAI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UPF位置信息与UPF优先支持的LAI范围的绑定关系（RMV-LOCBINDLAI）_96242798.md`
- 原始手册：`evidence/UNC/20.15.2/增加UPF位置信息与UPF优先支持的LAI范围的绑定关系（ADD-LOCBINDLAI）_96241682.md`
- 原始手册：`evidence/UNC/20.15.2/查询UPF位置信息与UPF优先支持的LAI范围的绑定关系（LST-LOCBINDLAI）_96242187.md`
