---
id: UNC@20.15.2@ConfigObject@LOCUPDQOS
type: ConfigObject
name: LOCUPDQOS（本地更新QoS值）
nf: UNC
version: 20.15.2
object_name: LOCUPDQOS
object_kind: entity
applicable_nf:
- GGSN
- PGW-C
- SGW-C
status: active
---

# LOCUPDQOS（本地更新QoS值）

## 说明

**适用NF：GGSN、PGW-C、SGW-C**

该命令用于控制将发送给左侧网元消息中的QoS值替换成本命令配置的值。消息包括Create PDP Context Response（Quality of Service Profile），Update PDP Context Request（Quality of Service Profile），Update PDP Context Response（Quality of Service Profile），Create Session Response（APN-AMBR），Update Bearer Request（APN-AMBR）。

当现网中某APN业务出现异常导致发送大量数据包时，可以通过本命令限制该APN下所有用户的带宽，待异常解决后需要删除本配置然后手动踢用户来恢复终端的带宽。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LOCUPDQOS]] · ADD LOCUPDQOS
- [[command/UNC/20.15.2/LST-LOCUPDQOS]] · LST LOCUPDQOS
- [[command/UNC/20.15.2/MOD-LOCUPDQOS]] · MOD LOCUPDQOS
- [[command/UNC/20.15.2/RMV-LOCUPDQOS]] · RMV LOCUPDQOS

## 证据

- 原始手册：`evidence/UNC/20.15.2/LOCUPDQOS.md`
- 原始手册：`evidence/UNC/20.15.2/LOCUPDQOS.md`
- 原始手册：`evidence/UNC/20.15.2/LOCUPDQOS.md`
- 原始手册：`evidence/UNC/20.15.2/LOCUPDQOS.md`
