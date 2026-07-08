---
id: UNC@20.15.2@ConfigObject@DNSCACHE
type: ConfigObject
name: DNSCACHE（DNS Cache）
nf: UNC
version: 20.15.2
object_name: DNSCACHE
object_kind: query_target
applicable_nf:
- SGSN
- MME
status: active
---

# DNSCACHE（DNS Cache）

## 说明

**适用网元：SGSN、MME**

该命令用于查看DNS在各个进程上的Cache信息，以及HOSTFILE信息。DNS Cache是使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。DNS Cache分为一级Cache和二级Cache。一级Cache保存在SPP进程上，二级Cache保存在添加了DNSLE（参见 [**ADD DNSLE**](../DNS本端实体管理/增加DNS实体绑定DNS Client IP(ADD DNSLE)_72225567.md) ）的SPU上对应的1号SGP进程上。HOSTFILE信息是通过 [**ADD IPV4DNSH**](../DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) 、 [**ADD IPV6DNSH**](../DNS Hostfile管理/增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md) 或 [**ADD DNSN**](../DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) 配置的数据。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-DNSCACHE]] · DSP DNSCACHE

## 证据

- 原始手册：`evidence/UNC/20.15.2/DNSCACHE.md`
