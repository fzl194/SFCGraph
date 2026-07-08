---
id: UDG@20.15.2@ConfigObject@CELLSERVICE
type: ConfigObject
name: CELLSERVICE（微服务主备实例倒换）
nf: UDG
version: 20.15.2
object_name: CELLSERVICE
object_kind: action
status: active
---

# CELLSERVICE（微服务主备实例倒换）

## 说明

![](微服务主备实例倒换（SWP CELLSERVICE）_84680846.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

多实例主备部署的微服务，当微服务主实例发生异常时，手动执行该命令实现微服务主备实例倒换。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行该命令可能会造成业务的短时中断。
> - 执行完该命令后，建议执行[**DSP MSSWPREC**](显示微服务主实例切换历史记录（DSP MSSWPREC）_63033396.md)命令观察微服务主备实例倒换是否成功。

## 操作本对象的命令

- [[command/UDG/20.15.2/SWP-CELLSERVICE]] · SWP CELLSERVICE

## 证据

- 原始手册：`evidence/UDG/20.15.2/微服务主备实例倒换（SWP-CELLSERVICE）_84680846.md`
