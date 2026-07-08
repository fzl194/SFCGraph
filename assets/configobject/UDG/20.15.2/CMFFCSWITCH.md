---
id: UDG@20.15.2@ConfigObject@CMFFCSWITCH
type: ConfigObject
name: CMFFCSWITCH（CMF流控开关配置数据）
nf: UDG
version: 20.15.2
object_name: CMFFCSWITCH
object_kind: global_setting
status: active
---

# CMFFCSWITCH（CMF流控开关配置数据）

## 说明

该命令用于配置CMF流控功能开关。

> **说明**
> - 该命令执行后立即生效。
>
> - CMF Pod单节点部署时不支持CMF流控，第三方CaaS场景不支持CMF流控，CSPEdge裸机场景不支持CMF流控。
> - 虚机场景下流控功能开关开启时，CMF Pod的CPU或CMF Pod所在节点的CPU满足任一起控条件，则触发CMF流控。
> - FST裸机场景下流控功能开关开启时，CMF Pod的CPU或CMF Pod所关联的SuperPod的CPU满足任一起控条件，则触发CMF流控。
> - 流控功能开关关闭时，不触发CMF流控。
> - 执行本命令时，FCSWITCH的取值不能为“未设置”，否则将导致配置下发失败。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FCSWITCH |
> | --- |
> | NOTSET |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-CMFFCSWITCH]] · LST CMFFCSWITCH
- [[command/UDG/20.15.2/SET-CMFFCSWITCH]] · SET CMFFCSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CMF流控开关配置数据（LST-CMFFCSWITCH）_84010349.md`
- 原始手册：`evidence/UDG/20.15.2/设置CMF流控开关（SET-CMFFCSWITCH）_37011290.md`
