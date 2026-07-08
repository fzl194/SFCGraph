---
id: UNC@20.15.2@ConfigObject@MMEIPTOMMEPOOL
type: ConfigObject
name: MMEIPTOMMEPOOL（MME IP）
nf: UNC
version: 20.15.2
object_name: MMEIPTOMMEPOOL
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# MMEIPTOMMEPOOL（MME IP）

## 说明

**适用NF：SGW-C、PGW-C**

该命令用于为已配置的MME POOL绑定地址，并设置该IP的描述、是否为备份和端口号。假设运营商需要在MME/SGW-C故障或者重启场景PGW-C保留会话，并在有下行数据和信令时触发恢复操作，需要执行该操作。

## 操作本对象的命令

- [ADD MMEIPTOMMEPOOL](command/UNC/20.15.2/ADD-MMEIPTOMMEPOOL.md)
- [LST MMEIPTOMMEPOOL](command/UNC/20.15.2/LST-MMEIPTOMMEPOOL.md)
- [MOD MMEIPTOMMEPOOL](command/UNC/20.15.2/MOD-MMEIPTOMMEPOOL.md)
- [RMV MMEIPTOMMEPOOL](command/UNC/20.15.2/RMV-MMEIPTOMMEPOOL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MME-IP（MOD-MMEIPTOMMEPOOL）_31453519.md`
- 原始手册：`evidence/UNC/20.15.2/删除MME-IP（RMV-MMEIPTOMMEPOOL）_31453521.md`
- 原始手册：`evidence/UNC/20.15.2/增加MME-IP（ADD-MMEIPTOMMEPOOL）_31453389.md`
- 原始手册：`evidence/UNC/20.15.2/查询MME-IP（LST-MMEIPTOMMEPOOL）_31453515.md`
