---
id: UNC@20.15.2@ConfigObject@NRFBNDWDFCPARA
type: ConfigObject
name: NRFBNDWDFCPARA（NRF带宽流控配置）
nf: UNC
version: 20.15.2
object_name: NRFBNDWDFCPARA
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFBNDWDFCPARA（NRF带宽流控配置）

## 说明

**适用NF：NRF**

该命令用于设置NRF带宽流控功能开关和相关阈值配置，在SCP&NRF融合部署场景下，当NRF收到SCP服务发现请求过多导致带宽不足时，可配置此命令防止网络带宽不足引起的业务失败。

## 操作本对象的命令

- [LST NRFBNDWDFCPARA](command/UNC/20.15.2/LST-NRFBNDWDFCPARA.md)
- [SET NRFBNDWDFCPARA](command/UNC/20.15.2/SET-NRFBNDWDFCPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF带宽流控配置（LST-NRFBNDWDFCPARA）_19010713.md`
- 原始手册：`evidence/UNC/20.15.2/设置NRF带宽流控功能参数（SET-NRFBNDWDFCPARA）_68371714.md`
