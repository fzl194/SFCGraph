---
id: UNC@20.15.2@ConfigObject@ROUTERELAYTUNNEL
type: ConfigObject
name: ROUTERELAYTUNNEL（路由迭代隧道功能开关）
nf: UNC
version: 20.15.2
object_name: ROUTERELAYTUNNEL
object_kind: global_setting
status: active
---

# ROUTERELAYTUNNEL（路由迭代隧道功能开关）

## 说明

该命令用于设置路由迭代隧道功能开关。

缺省情况下，非标签公网BGP路由、静态路由只能迭代到出接口和下一跳，不会迭代到隧道。配置了该特性后，上述路由将优先迭代到LSP隧道，如果没有LSP隧道，上述路由也可以迭代到出接口和下一跳。

该命令和SET SRROUTERELAYTUNNEL命令迭代隧道使能开关不能同时配置为TRUE。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-ROUTERELAYTUNNEL]] · LST ROUTERELAYTUNNEL
- [[command/UNC/20.15.2/SET-ROUTERELAYTUNNEL]] · SET ROUTERELAYTUNNEL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询路由迭代隧道功能开关（LST-ROUTERELAYTUNNEL）_50281618.md`
- 原始手册：`evidence/UNC/20.15.2/设置路由迭代隧道功能开关（SET-ROUTERELAYTUNNEL）_00865701.md`
