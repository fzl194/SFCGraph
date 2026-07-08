---
id: UNC@20.15.2@ConfigObject@DIAMETERPARA
type: ConfigObject
name: DIAMETERPARA（Diameter参数）
nf: UNC
version: 20.15.2
object_name: DIAMETERPARA
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# DIAMETERPARA（Diameter参数）

## 说明

**适用NF：PGW-C、SMF**

该命令用于设置是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送。

如果希望UNC在发送携带Destination-Host AVP的消息时，如果直连路径不存在或直连路径故障，尝试通过Destination-Realm来查找路由发送，则可将该参数使能。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DIAMETERPARA]] · LST DIAMETERPARA
- [[command/UNC/20.15.2/SET-DIAMETERPARA]] · SET DIAMETERPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/DIAMETERPARA.md`
- 原始手册：`evidence/UNC/20.15.2/DIAMETERPARA.md`
