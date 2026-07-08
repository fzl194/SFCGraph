---
id: UNC@20.15.2@ConfigObject@GTPUPATHINFO
type: ConfigObject
name: GTPUPATHINFO（GTPU路径）
nf: UNC
version: 20.15.2
object_name: GTPUPATHINFO
object_kind: entity
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
status: active
---

# GTPUPATHINFO（GTPU路径）

## 说明

![](删除GTPU路径（DEL GTPUPATHINFO）_14280394.assets/notice_3.0-zh-cn_2.png)

执行该命令会删除GTPU路径，影响基于该接口的业务，可能会引起业务呼损。

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于手动删除GTPU路径。

## 操作本对象的命令

- [DEL GTPUPATHINFO](command/UNC/20.15.2/DEL-GTPUPATHINFO.md)
- [DSP GTPUPATHINFO](command/UNC/20.15.2/DSP-GTPUPATHINFO.md)
- [TST GTPUPATHINFO](command/UNC/20.15.2/TST-GTPUPATHINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GTPU路径（DEL-GTPUPATHINFO）_14280394.md`
- 原始手册：`evidence/UNC/20.15.2/显示GTPU路径信息（DSP-GTPUPATHINFO）_58840349.md`
- 原始手册：`evidence/UNC/20.15.2/测试GTPU路径（TST-GTPUPATHINFO）_13960454.md`
