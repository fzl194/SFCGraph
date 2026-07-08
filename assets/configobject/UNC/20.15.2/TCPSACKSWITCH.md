---
id: UNC@20.15.2@ConfigObject@TCPSACKSWITCH
type: ConfigObject
name: TCPSACKSWITCH（TCP SACK开关配置）
nf: UNC
version: 20.15.2
object_name: TCPSACKSWITCH
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# TCPSACKSWITCH（TCP SACK开关配置）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

SET TcpSackSwitch命令用来修改Gx，Gy接口TCP协议是否支持SACK选项。

## 操作本对象的命令

- [LST TCPSACKSWITCH](command/UNC/20.15.2/LST-TCPSACKSWITCH.md)
- [SET TCPSACKSWITCH](command/UNC/20.15.2/SET-TCPSACKSWITCH.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TCP-SACK开关配置（LST-TCPSACKSWITCH）_09897244.md`
- 原始手册：`evidence/UNC/20.15.2/设置TCP-SACK开关配置（SET-TCPSACKSWITCH）_09897243.md`
