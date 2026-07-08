---
id: UNC@20.15.2@ConfigObject@USRPROFCHARGE
type: ConfigObject
name: USRPROFCHARGE（User Profile的计费配置）
nf: UNC
version: 20.15.2
object_name: USRPROFCHARGE
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# USRPROFCHARGE（User Profile的计费配置）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用来设置User Profile实例的计费配置，具体为：

1、为User Profile实例配置在线计费、离线计费方式以及融合计费方式。

2、为User Profile实例绑定离线计费模板。

3、为User Profile实例绑定DCC模板。

4、为User Profile实例绑定CC模板。

5、为User Profile实例绑定费率切换组。

6、为User Profile实例绑定计费属性实例。

## 操作本对象的命令

- [LST USRPROFCHARGE](command/UNC/20.15.2/LST-USRPROFCHARGE.md)
- [SET USRPROFCHARGE](command/UNC/20.15.2/SET-USRPROFCHARGE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询User-Profile的计费配置（LST-USRPROFCHARGE）_09896815.md`
- 原始手册：`evidence/UNC/20.15.2/设置User-Profile的计费配置（SET-USRPROFCHARGE）_09896814.md`
