---
id: UDG@20.15.2@ConfigObject@HTTPPATH
type: ConfigObject
name: HTTPPATH（测试HTTP链路）
nf: UDG
version: 20.15.2
object_name: HTTPPATH
object_kind: action
status: active
---

# HTTPPATH（测试HTTP链路）

## 说明

该命令用于在完成系统配置后，接入业务前，探测本端与对端能否成功建立HTTP/HTTPS连接。

> **说明**
> - 该命令最长耗时15s，只支持逐个探测对端，不支持同时探测多个对端，即只能串行执行探测命令。
> - 该命令在SBILINK微服务扩缩容或故障等情况下，存在实际正常的链路探测不通，建议在探测失败时，多次尝试。

## 操作本对象的命令

- [[command/UDG/20.15.2/TST-HTTPPATH]] · TST HTTPPATH

## 证据

- 原始手册：`evidence/UDG/20.15.2/HTTPPATH.md`
