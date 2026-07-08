---
id: UNC@20.15.2@ConfigObject@UERADIOCAPLEN
type: ConfigObject
name: UERADIOCAPLEN（UE Radio Capability信元长度）
nf: UNC
version: 20.15.2
object_name: UERADIOCAPLEN
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# UERADIOCAPLEN（UE Radio Capability信元长度）

## 说明

![](设置UE Radio Capability信元信息（SET UERADIOCAPLEN）_24956656.assets/notice_3.0-zh-cn_2.png)

如果设置UE Radio Capability信元长度上限过小，AMF无法存储UE Radio Capability信元内容，反之，AMF的内存有增大的风险。执行此命令前，请通过DSP UERADIOCAPLEN获取UE Radio Capability信元长度信息并联系华为技术支持协助配置。

**适用NF：AMF**

该命令用于设置AMF上存储UE Radio Capability到数据库的信元长度上限和不同IMEI设备型号核准号码的最大个数，设置存储UE Radio Capability到内存的开关及参数信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-UERADIOCAPLEN]] · CLR UERADIOCAPLEN
- [[command/UNC/20.15.2/DSP-UERADIOCAPLEN]] · DSP UERADIOCAPLEN
- [[command/UNC/20.15.2/LST-UERADIOCAPLEN]] · LST UERADIOCAPLEN
- [[command/UNC/20.15.2/SET-UERADIOCAPLEN]] · SET UERADIOCAPLEN

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UE-Radio-Capability信元长度（DSP-UERADIOCAPLEN）_71436533.md`
- 原始手册：`evidence/UNC/20.15.2/查询UE-Radio-Capability信元配置（LST-UERADIOCAPLEN）_71436545.md`
- 原始手册：`evidence/UNC/20.15.2/清除UE-Radio-Capability信元长度统计信息（CLR-UERADIOCAPLEN）_71436527.md`
- 原始手册：`evidence/UNC/20.15.2/设置UE-Radio-Capability信元信息（SET-UERADIOCAPLEN）_24956656.md`
