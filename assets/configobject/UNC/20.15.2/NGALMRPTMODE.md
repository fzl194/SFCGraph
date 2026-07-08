---
id: UNC@20.15.2@ConfigObject@NGALMRPTMODE
type: ConfigObject
name: NGALMRPTMODE（5G告警上报模式）
nf: UNC
version: 20.15.2
object_name: NGALMRPTMODE
object_kind: global_setting
applicable_nf:
- AMF
- SMF
status: active
---

# NGALMRPTMODE（5G告警上报模式）

## 说明

![](设置5G告警上报模式（SET NGALMRPTMODE）_19478936.assets/notice_3.0-zh-cn_2.png)

若配置告警类型为NG-RAN 链路故障、NG-RAN 节点不可达、批量PFCP链路故障或批量PFCP对端节点不可达，且修改批量告警上报开关时，可能会影响已有的告警，配置该命令时，请联系华为技术支持。

将开关由开修改为关时，已有的批量告警会转为单条告警上报。如果当时存在大量告警，会对系统产生冲击。

将开关由关修改为开时，已有的告警可能会残留。

**适用NF：AMF、SMF**

该命令用于设置5G告警的上报模式。如果系统内某一个告警大量产生时，会对系统的性能和告警台产生冲击，此时可以根据实际的需求，配置告警的上报模式，可以有效降低大量告警对系统的影响。

## 操作本对象的命令

- [LST NGALMRPTMODE](command/UNC/20.15.2/LST-NGALMRPTMODE.md)
- [SET NGALMRPTMODE](command/UNC/20.15.2/SET-NGALMRPTMODE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G告警上报模式（LST-NGALMRPTMODE）_19478933.md`
- 原始手册：`evidence/UNC/20.15.2/设置5G告警上报模式（SET-NGALMRPTMODE）_19478936.md`
