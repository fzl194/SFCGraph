---
id: UNC@20.15.2@ConfigObject@SRVNODERAT
type: ConfigObject
name: SRVNODERAT（SGSN/SGW IP与RAT类型间的映射关系）
nf: UNC
version: 20.15.2
object_name: SRVNODERAT
object_kind: entity
applicable_nf:
- GGSN
status: active
---

# SRVNODERAT（SGSN/SGW IP与RAT类型间的映射关系）

## 说明

**适用NF：GGSN**

该命令用来配置SGSN的IP地址段与RAT类型间的映射关系表。在根据SGSN的IP地址映射RAT类型时，需要用到映射表。获取RAT类型用于从虚拟APN映射到真实APN、匹配user-profile进行业务、计费控制。

## 操作本对象的命令

- [ADD SRVNODERAT](command/UNC/20.15.2/ADD-SRVNODERAT.md)
- [LST SRVNODERAT](command/UNC/20.15.2/LST-SRVNODERAT.md)
- [MOD SRVNODERAT](command/UNC/20.15.2/MOD-SRVNODERAT.md)
- [RMV SRVNODERAT](command/UNC/20.15.2/RMV-SRVNODERAT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SGSN_SGW-IP与RAT类型间的映射关系（MOD-SRVNODERAT）_09652673.md`
- 原始手册：`evidence/UNC/20.15.2/删除SGSN_SGW-IP与RAT类型间的映射关系（RMV-SRVNODERAT）_09653671.md`
- 原始手册：`evidence/UNC/20.15.2/增加SGSN_SGW-IP与RAT类型间的映射关系（ADD-SRVNODERAT）_09653221.md`
- 原始手册：`evidence/UNC/20.15.2/查询SGSN_SGW-IP与RAT类型间的映射关系（LST-SRVNODERAT）_09653057.md`
