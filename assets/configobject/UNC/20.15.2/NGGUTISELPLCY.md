---
id: UNC@20.15.2@ConfigObject@NGGUTISELPLCY
type: ConfigObject
name: NGGUTISELPLCY（AMF区域GUTI选网控制策略）
nf: UNC
version: 20.15.2
object_name: NGGUTISELPLCY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGGUTISELPLCY（AMF区域GUTI选网控制策略）

## 说明

**适用NF：AMF**

该命令用于增加AMF区域GUTI选网功能控制策略。AMF可基于当前用户的位置以及号段、签约切片、签约Ue Usage Type信息，控制是否需要将用户通过分配GUTI的方式重新注册到指定的AMF。

在大网和园区共享RAN场景下，大网AMF可以通过本地配置将园区用户在大网AMF注册成功后，通过分配给园区用户的GUTI中携带园区AMF的SET ID和POINTER的方式将园区用户重新注册到园区AMF上。

## 操作本对象的命令

- [ADD NGGUTISELPLCY](command/UNC/20.15.2/ADD-NGGUTISELPLCY.md)
- [LST NGGUTISELPLCY](command/UNC/20.15.2/LST-NGGUTISELPLCY.md)
- [MOD NGGUTISELPLCY](command/UNC/20.15.2/MOD-NGGUTISELPLCY.md)
- [RMV NGGUTISELPLCY](command/UNC/20.15.2/RMV-NGGUTISELPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改AMF区域GUTI选网控制策略（MOD-NGGUTISELPLCY）_13939889.md`
- 原始手册：`evidence/UNC/20.15.2/删除AMF区域GUTI选网控制策略（RMV-NGGUTISELPLCY）_13939897.md`
- 原始手册：`evidence/UNC/20.15.2/增加AMF区域GUTI选网控制策略（ADD-NGGUTISELPLCY）_14059345.md`
- 原始手册：`evidence/UNC/20.15.2/查询AMF区域GUTI选网控制策略（LST-NGGUTISELPLCY）_13939881.md`
