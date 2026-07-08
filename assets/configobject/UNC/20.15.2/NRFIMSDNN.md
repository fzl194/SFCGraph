---
id: UNC@20.15.2@ConfigObject@NRFIMSDNN
type: ConfigObject
name: NRFIMSDNN（IMS PCF的DNN）
nf: UNC
version: 20.15.2
object_name: NRFIMSDNN
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFIMSDNN（IMS PCF的DNN）

## 说明

**适用NF：NRF**

该命令用于配置IMS PCF支持的DNN信息。

独立部署的IMS PCF无号段信息（注册、配置和导入都无号段），即支持所有的号段。该PCF需使用此命令配置其支持的DNN，从而NRF认为PCF是独立部署的，可以正常处理业务。

如果不配置此命令，NRF可能会认为此PCF不是独立部署，没有支持的号段信息，从而屏蔽此PCF不被其他NF发现或检索以及在发生变更时通知已订阅的NF，并上报“ALM-100249 号段类NF无号段告警”，影响PCF的正常业务处理。NRF的上述判断通过SET NRFFUNCSW命令中NFNOSEGALARMSW开关控制。

## 操作本对象的命令

- [ADD NRFIMSDNN](command/UNC/20.15.2/ADD-NRFIMSDNN.md)
- [LST NRFIMSDNN](command/UNC/20.15.2/LST-NRFIMSDNN.md)
- [RMV NRFIMSDNN](command/UNC/20.15.2/RMV-NRFIMSDNN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMS-PCF的DNN（RMV-NRFIMSDNN）_96242888.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMS-PCF的DNN（ADD-NRFIMSDNN）_96241770.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMS-PCF的DNN（LST-NRFIMSDNN）_96242306.md`
