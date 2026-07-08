---
id: UDG@20.15.2@ConfigObject@REDIRAPPENDINFO
type: ConfigObject
name: REDIRAPPENDINFO（重定向携带信息）
nf: UDG
version: 20.15.2
object_name: REDIRAPPENDINFO
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# REDIRAPPENDINFO（重定向携带信息）

## 说明

**适用NF：PGW-U、UPF**

此命令用于运营商配置新的重定向携带信息。运营商可以选择在重定向的报文中是否携带原始URL、MSISDN、IMSI、IMEI、MSIP、时间戳信息以及自定义各信息前缀名称，并可以使用AES或blowfish算法对携带MSISDN、IMSI、IMEI、MSIP、时间戳信息进行加密。

## 操作本对象的命令

- [ADD REDIRAPPENDINFO](command/UDG/20.15.2/ADD-REDIRAPPENDINFO.md)
- [LST REDIRAPPENDINFO](command/UDG/20.15.2/LST-REDIRAPPENDINFO.md)
- [MOD REDIRAPPENDINFO](command/UDG/20.15.2/MOD-REDIRAPPENDINFO.md)
- [RMV REDIRAPPENDINFO](command/UDG/20.15.2/RMV-REDIRAPPENDINFO.md)

## 关联对象

- [IPFARMSERVER](configobject/UDG/20.15.2/IPFARMSERVER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改重定向携带信息（MOD-REDIRAPPENDINFO）_82837562.md`
- 原始手册：`evidence/UDG/20.15.2/删除重定向携带信息（RMV-REDIRAPPENDINFO）_86528788.md`
- 原始手册：`evidence/UDG/20.15.2/增加重定向携带信息（ADD-REDIRAPPENDINFO）_82837561.md`
- 原始手册：`evidence/UDG/20.15.2/查询重定向携带信息（LST-REDIRAPPENDINFO）_86528789.md`
