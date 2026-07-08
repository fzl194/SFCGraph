---
id: UNC@20.15.2@ConfigObject@SRROUTERELAYTUNNEL
type: ConfigObject
name: SRROUTERELAYTUNNEL（静态路由迭代隧道功能开关）
nf: UNC
version: 20.15.2
object_name: SRROUTERELAYTUNNEL
object_kind: global_setting
status: active
---

# SRROUTERELAYTUNNEL（静态路由迭代隧道功能开关）

## 说明

该命令用于设置静态路由迭代隧道功能开关。

缺省情况下，静态路由只能迭代到出接口和下一跳，不会迭代到隧道。配置了该命令后，静态路由将优先迭代到LSP隧道，如果没有LSP隧道，静态路由也可以迭代到出接口和下一跳。

该命令和SET ROUTERELAYTUNNEL命令迭代隧道使能开关不能同时配置为TRUE。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SRROUTERELAYTUNNEL]] · LST SRROUTERELAYTUNNEL
- [[command/UNC/20.15.2/SET-SRROUTERELAYTUNNEL]] · SET SRROUTERELAYTUNNEL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询静态路由迭代隧道功能开关（LST-SRROUTERELAYTUNNEL）_50281734.md`
- 原始手册：`evidence/UNC/20.15.2/设置静态路由迭代隧道功能开关（SET-SRROUTERELAYTUNNEL）_00866269.md`
