---
id: UDG@20.15.2@ConfigObject@CMFDATA
type: ConfigObject
name: CMFDATA（强制推送集群管理数据）
nf: UDG
version: 20.15.2
object_name: CMFDATA
object_kind: action
status: active
---

# CMFDATA（强制推送集群管理数据）

## 说明

![](强制推送集群管理数据（SYN CMFDATA）_99312746.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行后可能引起性能下降，且频繁操作会导致CPU升高，请谨慎使用并联系华为技术支持协助操作。

该命令用于集群管理服务向客户端强制同步集群管理数据。

> **说明**
> - 等待180s集群管理数据同步完成后生效
>
> - 该命令用于数据不一致导致紧急问题时强制推送全量集群管理数据，非紧急情况下请勿执行。
> - 为避免频繁执行对系统性能产生冲击，该命令在三分钟之内只能执行一次。

## 操作本对象的命令

- [SYN CMFDATA](command/UDG/20.15.2/SYN-CMFDATA.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/强制推送集群管理数据（SYN-CMFDATA）_99312746.md`
