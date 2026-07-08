---
id: UDG@20.15.2@ConfigObject@HTTPSTATUS
type: ConfigObject
name: HTTPSTATUS（HTTP状态码判定配置）
nf: UDG
version: 20.15.2
object_name: HTTPSTATUS
object_kind: entity
status: active
---

# HTTPSTATUS（HTTP状态码判定配置）

## 说明

![](增加HTTP状态码判定配置（ADD HTTPSTATUS）_67769736.assets/notice_3.0-zh-cn.png)

执行该命令会改变HTTP特定场景下的行为，可能导致业务受损。

该命令用于设置HTTP收到特定状态码时，是否执行对应场景下的动作。

> **说明**
> - 该命令执行后立即生效。
>
> - 故障下一跳，指的是HTTP在间接路由模式下，收到近端SCP/SEPP回复的指定状态码时，向网元上报近端SCP/SEPP故障。HTTP内部产生状态码并向网元上报近端SCP/SEPP故障的场景，不受本命令控制。
> - HTTP收到4XX、5XX状态码时，已默认执行故障下一跳场景的动作，无需本命令设置。
>
> - 最多可输入1024条记录。

## 操作本对象的命令

- [ADD HTTPSTATUS](command/UDG/20.15.2/ADD-HTTPSTATUS.md)
- [LST HTTPSTATUS](command/UDG/20.15.2/LST-HTTPSTATUS.md)
- [MOD HTTPSTATUS](command/UDG/20.15.2/MOD-HTTPSTATUS.md)
- [RMV HTTPSTATUS](command/UDG/20.15.2/RMV-HTTPSTATUS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改HTTP状态码判定配置（MOD-HTTPSTATUS）_04329849.md`
- 原始手册：`evidence/UDG/20.15.2/删除HTTP状态码判定配置（RMV-HTTPSTATUS）_04250405.md`
- 原始手册：`evidence/UDG/20.15.2/增加HTTP状态码判定配置（ADD-HTTPSTATUS）_67769736.md`
- 原始手册：`evidence/UDG/20.15.2/查询HTTP状态码判定配置（LST-HTTPSTATUS）_67609928.md`
