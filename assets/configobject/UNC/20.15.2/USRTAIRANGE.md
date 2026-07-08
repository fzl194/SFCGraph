---
id: UNC@20.15.2@ConfigObject@USRTAIRANGE
type: ConfigObject
name: USRTAIRANGE（用户TAI区域）
nf: UNC
version: 20.15.2
object_name: USRTAIRANGE
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# USRTAIRANGE（用户TAI区域）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加用户TAI区域配置。该配置为用户区域范围，包含1个或多个用户区域。语音用户建立N7会话时，其用户区域（TAI）会匹配到该配置的某一条记录，从而根据配置PCFSSCOPEBIND匹配该用户区域可用的PCF业务服务区，选择可用PCF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-USRTAIRANGE]] · ADD USRTAIRANGE
- [[command/UNC/20.15.2/LST-USRTAIRANGE]] · LST USRTAIRANGE
- [[command/UNC/20.15.2/MOD-USRTAIRANGE]] · MOD USRTAIRANGE
- [[command/UNC/20.15.2/RMV-USRTAIRANGE]] · RMV USRTAIRANGE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户TAI区域（MOD-USRTAIRANGE）_35519279.md`
- 原始手册：`evidence/UNC/20.15.2/删除用户TAI区域（RMV-USRTAIRANGE）_88377452.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户TAI区域（ADD-USRTAIRANGE）_88537092.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户TAI区域（LST-USRTAIRANGE）_35519277.md`
