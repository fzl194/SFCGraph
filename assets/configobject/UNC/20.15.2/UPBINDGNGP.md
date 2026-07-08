---
id: UNC@20.15.2@ConfigObject@UPBINDGNGP
type: ConfigObject
name: UPBINDGNGP（GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系）
nf: UNC
version: 20.15.2
object_name: UPBINDGNGP
object_kind: binding
applicable_nf:
- GGSN
- PGW-C
status: active
---

# UPBINDGNGP（GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系）

## 说明

**适用NF：GGSN、PGW-C**

该命令用于增加GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系。

该命令必须配置符合实际组网的GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系，否则GW-U故障隔离功能不可用。

## 操作本对象的命令

- [ADD UPBINDGNGP](command/UNC/20.15.2/ADD-UPBINDGNGP.md)
- [LST UPBINDGNGP](command/UNC/20.15.2/LST-UPBINDGNGP.md)
- [MOD UPBINDGNGP](command/UNC/20.15.2/MOD-UPBINDGNGP.md)
- [RMV UPBINDGNGP](command/UNC/20.15.2/RMV-UPBINDGNGP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GGSN与Gn_Gp接口或PGW-U与S5_S8接口的绑定关系（MOD-UPBINDGNGP）_96242705.md`
- 原始手册：`evidence/UNC/20.15.2/删除GGSN与Gn_Gp接口或PGW-U与S5_S8接口的绑定关系（RMV-UPBINDGNGP）_96243040.md`
- 原始手册：`evidence/UNC/20.15.2/增加GGSN与Gn_Gp接口或PGW-U与S5_S8接口的绑定关系（ADD-UPBINDGNGP）_78029307.md`
- 原始手册：`evidence/UNC/20.15.2/查询GGSN与Gn_Gp接口或PGW-U与S5_S8接口的绑定关系（LST-UPBINDGNGP）_96242519.md`
