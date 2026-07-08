---
id: UNC@20.15.2@ConfigObject@APNDIAMAAAGRP
type: ConfigObject
name: APNDIAMAAAGRP（APN的Diameter AAA服务器组）
nf: UNC
version: 20.15.2
object_name: APNDIAMAAAGRP
object_kind: entity
applicable_nf:
- PGW-C
status: active
---

# APNDIAMAAAGRP（APN的Diameter AAA服务器组）

## 说明

**适用NF：PGW-C**

此命令用于将Diameter AAA组绑定到指定APN上。当指定APN下需要建立non-3GPP会话时，操作员可以执行此命令将Diameter AAA组绑定到APN上，当该APN的用户激活时，系统选择将该分组下的Diameter AAA进行业务处理。

## 操作本对象的命令

- [ADD APNDIAMAAAGRP](command/UNC/20.15.2/ADD-APNDIAMAAAGRP.md)
- [LST APNDIAMAAAGRP](command/UNC/20.15.2/LST-APNDIAMAAAGRP.md)
- [MOD APNDIAMAAAGRP](command/UNC/20.15.2/MOD-APNDIAMAAAGRP.md)
- [RMV APNDIAMAAAGRP](command/UNC/20.15.2/RMV-APNDIAMAAAGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN的Diameter-AAA服务器组（MOD-APNDIAMAAAGRP）_64343895.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN的Diameter-AAA服务器组（RMV-APNDIAMAAAGRP）_64343900.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN的Diameter-AAA服务器组（ADD-APNDIAMAAAGRP）_64343817.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN的Diameter-AAA服务器组（LST-APNDIAMAAAGRP）_64343875.md`
