---
id: UNC@20.15.2@ConfigObject@PGWHOSTNAME
type: ConfigObject
name: PGWHOSTNAME（逻辑接口的PGW主机名）
nf: UNC
version: 20.15.2
object_name: PGWHOSTNAME
object_kind: entity
applicable_nf:
- PGW-C
status: active
---

# PGWHOSTNAME（逻辑接口的PGW主机名）

## 说明

**适用NF：PGW-C**

此命令用于添加PGW-C逻辑接口主机名。该配置体现在PGW-C发送给Diameter AAA的授权请求消息AAR的PDN GW Identity中。用户从non-3GPP网络切换到3GPP网络时，MME需要根据hostname选择PGW-C，因此PGW-C上hostname的配置需要与DNS上的相关配置保持一致。

根据网络规划，当需要修改逻辑接口主机名时，需要先执行RMV PGWHOSTNAME命令，再执行该命令。

## 操作本对象的命令

- [ADD PGWHOSTNAME](command/UNC/20.15.2/ADD-PGWHOSTNAME.md)
- [LST PGWHOSTNAME](command/UNC/20.15.2/LST-PGWHOSTNAME.md)
- [RMV PGWHOSTNAME](command/UNC/20.15.2/RMV-PGWHOSTNAME.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除逻辑接口的PGW主机名（RMV-PGWHOSTNAME）_64343908.md`
- 原始手册：`evidence/UNC/20.15.2/增加逻辑接口的PGW主机名（ADD-PGWHOSTNAME）_64343865.md`
- 原始手册：`evidence/UNC/20.15.2/查询逻辑接口的PGW主机名（LST-PGWHOSTNAME）_64343889.md`
