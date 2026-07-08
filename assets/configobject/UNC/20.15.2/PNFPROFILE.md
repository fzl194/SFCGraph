---
id: UNC@20.15.2@ConfigObject@PNFPROFILE
type: ConfigObject
name: PNFPROFILE（对端NF实例概述信息）
nf: UNC
version: 20.15.2
object_name: PNFPROFILE
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- NRF
- SGW-C
- PGW-C
- GGSN
status: active
---

# PNFPROFILE（对端NF实例概述信息）

## 说明

![](增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.assets/notice_3.0-zh-cn_2.png)

若NF类型为NfUPF，参数PRIORITY只有在UPSELECTFLAG中的PRIORITYFLAG开关打开时才会生效，会影响SMF对当前UPF实例的选择；若修改值未遵照组网需求，则会导致SMF选择该UPF产生非预期结果。

若NF类型为NfUPF，参数FQDN不允许配置为空格，否则会影响该配置记录的导出；若修改值未遵照组网需求，则会导致SMF选择该UPF后产生非预期结果。

**适用NF：AMF、SMF、NSSF、SMSF、NCG、NRF、SGW-C、PGW-C、GGSN**

该命令用于增加本地配置的对端NF实例的概述信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFPROFILE]] · ADD PNFPROFILE
- [[command/UNC/20.15.2/LST-PNFPROFILE]] · LST PNFPROFILE
- [[command/UNC/20.15.2/MOD-PNFPROFILE]] · MOD PNFPROFILE
- [[command/UNC/20.15.2/RMV-PNFPROFILE]] · RMV PNFPROFILE

## 证据

- 原始手册：`evidence/UNC/20.15.2/PNFPROFILE.md`
- 原始手册：`evidence/UNC/20.15.2/PNFPROFILE.md`
- 原始手册：`evidence/UNC/20.15.2/PNFPROFILE.md`
- 原始手册：`evidence/UNC/20.15.2/PNFPROFILE.md`
