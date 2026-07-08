---
id: UDG@20.15.2@ConfigObject@MESYS
type: ConfigObject
name: MESYS（复位网元服务）
nf: UDG
version: 20.15.2
object_name: MESYS
object_kind: action
status: active
---

# MESYS（复位网元服务）

## 说明

![](复位网元服务（RST MESYS）_72247081.assets/notice_3.0-zh-cn.png)

- 复位网元服务可能导致业务呼损，请确认是否继续操作。
- 三方CaaS场景该命令依赖LCM配套版本，其它场景无此限制。
- 该命令属于“网元ID”为“0”下的业务，参数“网元ID”输入“0”时重建Pod为异步操作，命令返回操作成功后1-3min刷新页面失败可判断重建Pod成功，反之则失败；参数“网元ID”输入非“0”时重建Pod为同步操作。

本命令用于对指定的网元进行复位。RST MESYS会将指定网元下的POD全部重建。

## 操作本对象的命令

- [RST MESYS](command/UDG/20.15.2/RST-MESYS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/复位网元服务（RST-MESYS）_72247081.md`
