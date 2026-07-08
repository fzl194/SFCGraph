---
id: UNC@20.15.2@ConfigObject@NRFIGNDISCPARA
type: ConfigObject
name: NRFIGNDISCPARA（NF服务发现忽略参数规则）
nf: UNC
version: 20.15.2
object_name: NRFIGNDISCPARA
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFIGNDISCPARA（NF服务发现忽略参数规则）

## 说明

![](增加NF服务发现忽略参数规则（ADD NRFIGNDISCPARA）_98328634.assets/notice_3.0-zh-cn_2.png)

按NFTYPE配置服务发现忽略参数后，服务发现会忽略该请求参数，可能会导致服务发现返回实际不可用的网元，影响业务引流。

**适用NF：NRF**

该命令用于增加NF服务发现忽略参数配置。按NFTYPE配置服务发现忽略参数后，服务发现会忽略该请求参数。

当NF因自身原因携带无用服务发现参数进行发现，导致在NRF匹配到非预期网元或服务发现结果为空时，可通过配置此命令忽略该参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFIGNDISCPARA]] · ADD NRFIGNDISCPARA
- [[command/UNC/20.15.2/LST-NRFIGNDISCPARA]] · LST NRFIGNDISCPARA
- [[command/UNC/20.15.2/RMV-NRFIGNDISCPARA]] · RMV NRFIGNDISCPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFIGNDISCPARA.md`
- 原始手册：`evidence/UNC/20.15.2/NRFIGNDISCPARA.md`
- 原始手册：`evidence/UNC/20.15.2/NRFIGNDISCPARA.md`
