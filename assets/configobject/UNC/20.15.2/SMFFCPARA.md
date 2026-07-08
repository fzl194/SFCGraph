---
id: UNC@20.15.2@ConfigObject@SMFFCPARA
type: ConfigObject
name: SMFFCPARA（SMF自保流控参数）
nf: UNC
version: 20.15.2
object_name: SMFFCPARA
object_kind: global_setting
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
status: active
---

# SMFFCPARA（SMF自保流控参数）

## 说明

![](设置SMF自保流控参数（SET SMFFCPARA）_48054029.assets/notice_3.0-zh-cn_2.png)

配置下发的原因值可能会对终端行为产生影响，对性能指标的统计值产生影响，在配置前请联系华为技术支持工程师评估影响。

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于修改SMF流程控制参数。当用户的消息被流控丢弃，SMF通过本命令控制下发给终端的原因值，一方面确保终端后续的正常接入，另一方面防止终端继续发起相应的流程对已经触发流控的设备造成进一步的冲击。

## 操作本对象的命令

- [LST SMFFCPARA](command/UNC/20.15.2/LST-SMFFCPARA.md)
- [SET SMFFCPARA](command/UNC/20.15.2/SET-SMFFCPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMF自保流控参数（LST-SMFFCPARA）_01214230.md`
- 原始手册：`evidence/UNC/20.15.2/设置SMF自保流控参数（SET-SMFFCPARA）_48054029.md`
