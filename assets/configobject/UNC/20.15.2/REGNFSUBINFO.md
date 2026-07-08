---
id: UNC@20.15.2@ConfigObject@REGNFSUBINFO
type: ConfigObject
name: REGNFSUBINFO（订阅信息）
nf: UNC
version: 20.15.2
object_name: REGNFSUBINFO
object_kind: entity
applicable_nf:
- NRF
status: active
---

# REGNFSUBINFO（订阅信息）

## 说明

![](删除订阅信息（DEL REGNFSUBINFO）_09652587.assets/notice_3.0-zh-cn_2.png)

删除NF订阅信息，会导致NRF不再推送对应订阅内容的变更消息，删除之前请联系华为技术工程师进行风险评估。

**适用NF：NRF**

该命令用于删除NF在NRF上的订阅信息。如订阅请求方NF已经向NRF发送了去订阅消息，但由于请求方NF或NRF处理异常，可以执行此命令删除订阅信息。

## 操作本对象的命令

- [DEL REGNFSUBINFO](command/UNC/20.15.2/DEL-REGNFSUBINFO.md)
- [DSP REGNFSUBINFO](command/UNC/20.15.2/DSP-REGNFSUBINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除订阅信息（DEL-REGNFSUBINFO）_09652587.md`
- 原始手册：`evidence/UNC/20.15.2/显示NF订阅信息（DSP-REGNFSUBINFO）_09653819.md`
