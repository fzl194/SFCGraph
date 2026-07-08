---
id: UNC@20.15.2@ConfigObject@NASCMPT
type: ConfigObject
name: NASCMPT（NAS兼容性参数）
nf: UNC
version: 20.15.2
object_name: NASCMPT
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# NASCMPT（NAS兼容性参数）

## 说明

**适用NF：AMF**

该命令用于为NAS（Non-Access-Stratum protocol）设置兼容性控制参数。NAS是AMF与UE之间的应用协议，通过本命令可以控制AMF是否在该协议层的下行消息中携带指定的可选信元。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NASCMPT]] · LST NASCMPT
- [[command/UNC/20.15.2/SET-NASCMPT]] · SET NASCMPT

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NAS兼容性参数（LST-NASCMPT）_11472420.md`
- 原始手册：`evidence/UNC/20.15.2/设置NAS兼容性参数（SET-NASCMPT）_58192283.md`
