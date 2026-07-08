---
id: UDG@20.15.2@ConfigObject@UPDIAMETERPARA
type: ConfigObject
name: UPDIAMETERPARA（Diameter参数）
nf: UDG
version: 20.15.2
object_name: UPDIAMETERPARA
object_kind: global_setting
applicable_nf:
- UPF
status: active
---

# UPDIAMETERPARA（Diameter参数）

## 说明

**适用NF：UPF**

该命令用于设置是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送。

如果希望UPF在发送携带Destination-Host AVP的消息时，如果直连路径不存在或直连路径故障，尝试通过Destination-Realm来查找路由发送，则可将该参数使能。

## 操作本对象的命令

- [LST UPDIAMETERPARA](command/UDG/20.15.2/LST-UPDIAMETERPARA.md)
- [SET UPDIAMETERPARA](command/UDG/20.15.2/SET-UPDIAMETERPARA.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Diameter参数（LST-UPDIAMETERPARA）_45432710.md`
- 原始手册：`evidence/UDG/20.15.2/设置Diameter参数（SET-UPDIAMETERPARA）_97080173.md`
