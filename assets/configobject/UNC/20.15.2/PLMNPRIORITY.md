---
id: UNC@20.15.2@ConfigObject@PLMNPRIORITY
type: ConfigObject
name: PLMNPRIORITY（获取PLMN优先级）
nf: UNC
version: 20.15.2
object_name: PLMNPRIORITY
object_kind: global_setting
applicable_nf:
- PGW-C
- SGW-C
- GGSN
status: active
---

# PLMNPRIORITY（获取PLMN优先级）

## 说明

**适用NF：PGW-C、SGW-C、GGSN**

由于PGW一般是根据运营商的不同进行设置的，因此PGW的HPLMN可以直接通过ADD NGHPLMN进行设置。此时PGW只知道自身的PLMN还不足以判断用户是本地用户还是漫游用户，还需要知道SGW一侧的PLMN。由于SGW是根据用户的位置进行选择的，因此为适应位置上的变化，PGW要根据SGW具体的位置获知SGW一侧的PLMN。通过本指令可以更改PGW获取SGW一侧PLMN的方式的优先级。使用该命令配置获取SGSN/S-GW的PLMN信息的优先级。PGW根据优先级依次获取SGSN/S-GW的PLMN，直到获取成功为止。

## 操作本对象的命令

- [LST PLMNPRIORITY](command/UNC/20.15.2/LST-PLMNPRIORITY.md)
- [SET PLMNPRIORITY](command/UNC/20.15.2/SET-PLMNPRIORITY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询获取PLMN优先级（LST-PLMNPRIORITY）_09652282.md`
- 原始手册：`evidence/UNC/20.15.2/设置获取PLMN优先级（SET-PLMNPRIORITY）_09653827.md`
