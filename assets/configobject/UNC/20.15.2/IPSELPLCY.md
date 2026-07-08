---
id: UNC@20.15.2@ConfigObject@IPSELPLCY
type: ConfigObject
name: IPSELPLCY（IP地址选择策略）
nf: UNC
version: 20.15.2
object_name: IPSELPLCY
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IPSELPLCY（IP地址选择策略）

## 说明

**适用网元：SGSN、MME**

该命令用于增加S10、S11、Gn/Gp、S5/S8、S3、S4、Sv接口的IP地址选择策略。

在IPv6改造过程中，可以针对整系统和用户粒度进行IP地址策略控制。

其中GU接口是指Gn/Gp接口，LTE接口是指S10、S11、S5/S8、S3、S4、Sv接口。

## 操作本对象的命令

- [ADD IPSELPLCY](command/UNC/20.15.2/ADD-IPSELPLCY.md)
- [LST IPSELPLCY](command/UNC/20.15.2/LST-IPSELPLCY.md)
- [MOD IPSELPLCY](command/UNC/20.15.2/MOD-IPSELPLCY.md)
- [RMV IPSELPLCY](command/UNC/20.15.2/RMV-IPSELPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IP地址选择策略(MOD-IPSELPLCY)_26305272.md`
- 原始手册：`evidence/UNC/20.15.2/删除IP地址选择策略(RMV-IPSELPLCY)_72345059.md`
- 原始手册：`evidence/UNC/20.15.2/增加IP地址选择策略(ADD-IPSELPLCY)_72225141.md`
- 原始手册：`evidence/UNC/20.15.2/查询IP地址选择策略(LST-IPSELPLCY)_26145462.md`
