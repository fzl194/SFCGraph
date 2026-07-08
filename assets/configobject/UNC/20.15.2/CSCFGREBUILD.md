---
id: UNC@20.15.2@ConfigObject@CSCFGREBUILD
type: ConfigObject
name: CSCFGREBUILD（对特定配置的缓存重建）
nf: UNC
version: 20.15.2
object_name: CSCFGREBUILD
object_kind: action
applicable_nf:
- PGW-C
- SGW-C
- AMF
- SMF
- GGSN
status: active
---

# CSCFGREBUILD（对特定配置的缓存重建）

## 说明

**适用NF：PGW-C、SGW-C、AMF、SMF、GGSN**

该命令用于启动业务进程对特定配置的缓存重建。

当发现本地配置缓存和OM的配置数据不一致时，可以使用该命令。

## 操作本对象的命令

- [STR CSCFGREBUILD](command/UNC/20.15.2/STR-CSCFGREBUILD.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动对特定配置的缓存重建（STR-CSCFGREBUILD）_24015956.md`
