---
id: UDG@20.15.2@ConfigObject@IMSIBINDPOD
type: ConfigObject
name: IMSIBINDPOD（IMSI和Pod的绑定关系）
nf: UDG
version: 20.15.2
object_name: IMSIBINDPOD
object_kind: binding
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# IMSIBINDPOD（IMSI和Pod的绑定关系）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

用于将某IMSI的用户绑定到特定的POD上激活。

本命令通常是在现网扩容需要测试新扩容的POD是否能够正常工作时使用，不建议用于日常场景。

## 操作本对象的命令

- [ADD IMSIBINDPOD](command/UDG/20.15.2/ADD-IMSIBINDPOD.md)
- [LST IMSIBINDPOD](command/UDG/20.15.2/LST-IMSIBINDPOD.md)
- [MOD IMSIBINDPOD](command/UDG/20.15.2/MOD-IMSIBINDPOD.md)
- [RMV IMSIBINDPOD](command/UDG/20.15.2/RMV-IMSIBINDPOD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IMSI和Pod的绑定关系（MOD-IMSIBINDPOD）_64015276.md`
- 原始手册：`evidence/UDG/20.15.2/删除IMSI和Pod的绑定关系（RMV-IMSIBINDPOD）_64015277.md`
- 原始手册：`evidence/UDG/20.15.2/增加IMSI和Pod绑定关系（ADD-IMSIBINDPOD）_64015275.md`
- 原始手册：`evidence/UDG/20.15.2/查询IMSI和Pod绑定关系（LST-IMSIBINDPOD）_64015278.md`
