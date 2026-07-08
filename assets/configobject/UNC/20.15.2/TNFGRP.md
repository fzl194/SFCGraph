---
id: UNC@20.15.2@ConfigObject@TNFGRP
type: ConfigObject
name: TNFGRP（目标NF组）
nf: UNC
version: 20.15.2
object_name: TNFGRP
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
status: active
---

# TNFGRP（目标NF组）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于增加目标NF组的配置。

目标NF组是由一个或者多个NF实例组成的负荷分担的集群，可以为特定用户群（比如指定号段、指定位置、请求DNN等）提供业务接入服务。

## 操作本对象的命令

- [ADD TNFGRP](command/UNC/20.15.2/ADD-TNFGRP.md)
- [LST TNFGRP](command/UNC/20.15.2/LST-TNFGRP.md)
- [RMV TNFGRP](command/UNC/20.15.2/RMV-TNFGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除目标NF组（RMV-TNFGRP）_09652293.md`
- 原始手册：`evidence/UNC/20.15.2/增加目标NF组（ADD-TNFGRP）_09651791.md`
- 原始手册：`evidence/UNC/20.15.2/查询目标NF组（LST-TNFGRP）_09652113.md`
