---
id: UNC@20.15.2@ConfigObject@NRFBIGPKGPARA
type: ConfigObject
name: NRFBIGPKGPARA（NRF大包控制参数）
nf: UNC
version: 20.15.2
object_name: NRFBIGPKGPARA
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFBIGPKGPARA（NRF大包控制参数）

## 说明

![](设置NRF大包控制参数（SET NRFBIGPKGPARA）_86184327.assets/notice_3.0-zh-cn_2.png)

MAXREGSEGNUM、MAXDISCSEGNUM、MAXPKGSIZE参数配置过小，服务发现结果会过大，将会导致服务发现失败。

**适用NF：NRF**

该命令用于配置NRF大包控制参数，用于预防报文过大而导致NRF资源过载。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFBIGPKGPARA]] · LST NRFBIGPKGPARA
- [[command/UNC/20.15.2/SET-NRFBIGPKGPARA]] · SET NRFBIGPKGPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF大包控制参数（LST-NRFBIGPKGPARA）_86184260.md`
- 原始手册：`evidence/UNC/20.15.2/设置NRF大包控制参数（SET-NRFBIGPKGPARA）_86184327.md`
