---
id: UNC@20.15.2@ConfigObject@DNSS
type: ConfigObject
name: DNSS（DNS服务器）
nf: UNC
version: 20.15.2
object_name: DNSS
object_kind: entity
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# DNSS（DNS服务器）

## 说明

**适用网元：SGSN、MME** **、AMF**

该命令用于增加一个DNS域名解析服务器。DNS服务器是网络中专门提供域名解析服务的服务器。

域名解析在4G系统中通常用于附着时根据APN解析P-GW地址和S-GW地址，Inter TAU时根据GUTI解析对端MME IP地址，Handover时根据TAI解析对端MME IP地址。

域名解析顺序：首先查找主机上HOSTFILE中的记录（通过 [**ADD IPV4DNSH**](../DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) 添加）。如果没有相应的记录，再查找DNS Cache中的记录。如果没有相应的记录，再向DNS服务器发送解析请求进行解析。

## 操作本对象的命令

- [ADD DNSS](command/UNC/20.15.2/ADD-DNSS.md)
- [DSP DNSS](command/UNC/20.15.2/DSP-DNSS.md)
- [LST DNSS](command/UNC/20.15.2/LST-DNSS.md)
- [MOD DNSS](command/UNC/20.15.2/MOD-DNSS.md)
- [RMV DNSS](command/UNC/20.15.2/RMV-DNSS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改DNS服务器(MOD-DNSS)_72225577.md`
- 原始手册：`evidence/UNC/20.15.2/删除DNS服务器(RMV-DNSS)_26145898.md`
- 原始手册：`evidence/UNC/20.15.2/增加DNS服务器(ADD-DNSS)_72345497.md`
- 原始手册：`evidence/UNC/20.15.2/显示DNS服务器状态(DSP-DNSS)_72345499.md`
- 原始手册：`evidence/UNC/20.15.2/查询DNS服务器(LST-DNSS)_26305708.md`
