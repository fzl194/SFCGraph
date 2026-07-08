---
id: UDG@20.15.2@ConfigObject@SNSSAIUPINTF
type: ConfigObject
name: SNSSAIUPINTF（网络切片和逻辑接口绑定关系）
nf: UDG
version: 20.15.2
object_name: SNSSAIUPINTF
object_kind: entity
applicable_nf:
- UPF
status: active
---

# SNSSAIUPINTF（网络切片和逻辑接口绑定关系）

## 说明

**适用NF：UPF**

![](增加网络切片和逻辑接口绑定关系（ADD SNSSAIUPINTF）_51061265.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令会导致切片用户使用的逻辑接口发生变化，可能会导致业务链路不通。

该命令用于给指定的网络切片选择标识绑定一个N3逻辑接口。

## 操作本对象的命令

- [ADD SNSSAIUPINTF](command/UDG/20.15.2/ADD-SNSSAIUPINTF.md)
- [LST SNSSAIUPINTF](command/UDG/20.15.2/LST-SNSSAIUPINTF.md)
- [MOD SNSSAIUPINTF](command/UDG/20.15.2/MOD-SNSSAIUPINTF.md)
- [RMV SNSSAIUPINTF](command/UDG/20.15.2/RMV-SNSSAIUPINTF.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改网络切片和逻辑接口绑定关系（MOD-SNSSAIUPINTF）_51061266.md`
- 原始手册：`evidence/UDG/20.15.2/删除网络切片和逻辑接口绑定关系（RMV-SNSSAIUPINTF）_51061267.md`
- 原始手册：`evidence/UDG/20.15.2/增加网络切片和逻辑接口绑定关系（ADD-SNSSAIUPINTF）_51061265.md`
- 原始手册：`evidence/UDG/20.15.2/查询网络切片和逻辑接口绑定关系（LST-SNSSAIUPINTF）_51061268.md`
