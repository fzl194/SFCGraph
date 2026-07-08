---
id: UNC@20.15.2@ConfigObject@IMSIBINDUPFADDR
type: ConfigObject
name: IMSIBINDUPFADDR（用户和UPF地址的绑定关系）
nf: UNC
version: 20.15.2
object_name: IMSIBINDUPFADDR
object_kind: binding
applicable_nf:
- GGSN
- SGW-C
- PGW-C
- SMF
status: active
---

# IMSIBINDUPFADDR（用户和UPF地址的绑定关系）

## 说明

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于增加用户和UPF地址的绑定关系。在拨测场景下如果用户需要使用绑定的UPF地址建立PFCP会话，系统支持添加一个用户和UPF地址的绑定关系，同时也支持添加连续IMSI号段用户和UPF地址的绑定关系。

## 操作本对象的命令

- [ADD IMSIBINDUPFADDR](command/UNC/20.15.2/ADD-IMSIBINDUPFADDR.md)
- [LST IMSIBINDUPFADDR](command/UNC/20.15.2/LST-IMSIBINDUPFADDR.md)
- [MOD IMSIBINDUPFADDR](command/UNC/20.15.2/MOD-IMSIBINDUPFADDR.md)
- [RMV IMSIBINDUPFADDR](command/UNC/20.15.2/RMV-IMSIBINDUPFADDR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户和UPF地址的绑定关系（MOD-IMSIBINDUPFADDR）_99921812.md`
- 原始手册：`evidence/UNC/20.15.2/删除用户和UPF地址的绑定关系（RMV-IMSIBINDUPFADDR）_99761844.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户和UPF地址的绑定关系（ADD-IMSIBINDUPFADDR）_49962077.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户和UPF的绑定关系（LST-IMSIBINDUPFADDR）_50121885.md`
