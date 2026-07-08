---
id: UNC@20.15.2@ConfigObject@NRFFUNCSW
type: ConfigObject
name: NRFFUNCSW（NRF功能开关）
nf: UNC
version: 20.15.2
object_name: NRFFUNCSW
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFFUNCSW（NRF功能开关）

## 说明

![](设置NRF功能开关（SET NRFFUNCSW）_09651606.assets/notice_3.0-zh-cn_2.png)

开关设置将会导致以下影响:

- PROFILELITESW、DISCFILTEREXSW开关打开可能导致服务发现结果信息缺失。
- NOTILITESW开关打开可能导致通知结果信息缺失。
- DISCFILTERSW、DISCFILTERUNDSW开关关闭可能导致服务发现返回实际不可用的网元。
- DATACHKSW开关打开可能影响NRF性能。
- AMFAVLENSW开关打开可能导致服务发现AMF失败。
- PATCHNOTIFYSW开关打开可能导致通知对端处理失败。
- NOTIFYALLSEGSW开关打开可能影响通知时NRF的性能。
- NFMFCSWITCH、DISCFCSWITCH开关关闭导致NRF流控功能不可用。
- DISCCACHESW、SNSSAICACHESW开关关闭影响服务发现性能。

**适用NF：NRF**

该命令用于设置NRF的各类功能开关。运营商可以根据需要设置NRF的不同功能。

## 操作本对象的命令

- [LST NRFFUNCSW](command/UNC/20.15.2/LST-NRFFUNCSW.md)
- [SET NRFFUNCSW](command/UNC/20.15.2/SET-NRFFUNCSW.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF功能开关（LST-NRFFUNCSW）_09652285.md`
- 原始手册：`evidence/UNC/20.15.2/设置NRF功能开关（SET-NRFFUNCSW）_09651606.md`
