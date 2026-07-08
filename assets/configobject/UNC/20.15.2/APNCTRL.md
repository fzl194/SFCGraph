---
id: UNC@20.15.2@ConfigObject@APNCTRL
type: ConfigObject
name: APNCTRL（APN控制参数配置）
nf: UNC
version: 20.15.2
object_name: APNCTRL
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# APNCTRL（APN控制参数配置）

## 说明

**适用网元：SGSN、MME**

该命令用于增加基于APN的信令拥塞控制和固定终端寻呼优化的控制参数，基于APN的信令拥塞控制的控制参数包括 “签约APN” 、 “APN优先级” 、 “Backoff Timer分配开关” 、 “附着拒绝原因值” 和 “识别异常附着行为的门限(次/小时)” ，固定终端寻呼优化的控制参数包括 “签约APN” 和 “Ready Timer定时器时长” 。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNCTRL]] · ADD APNCTRL
- [[command/UNC/20.15.2/LST-APNCTRL]] · LST APNCTRL
- [[command/UNC/20.15.2/MOD-APNCTRL]] · MOD APNCTRL
- [[command/UNC/20.15.2/RMV-APNCTRL]] · RMV APNCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN控制参数配置(MOD-APNCTRL)_26305282.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN控制参数配置(RMV-APNCTRL)_72225151.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN控制参数配置(ADD-APNCTRL)_26145470.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN控制参数配置(LST-APNCTRL)_72345069.md`
