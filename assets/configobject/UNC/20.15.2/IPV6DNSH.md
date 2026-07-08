---
id: UNC@20.15.2@ConfigObject@IPV6DNSH
type: ConfigObject
name: IPV6DNSH（IPV6 DNS Hostfile记录）
nf: UNC
version: 20.15.2
object_name: IPV6DNSH
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IPV6DNSH（IPV6 DNS Hostfile记录）

## 说明

**适用网元：SGSN、MME**

该命令用于配置网元接口所对应的IPv6地址信息，该信息用于网元选择时DNS查询功能。

如果配置了多个IP地址，域名解析结果中将会根据 “PRIORITY（优先级）” 和 “WEIGHT（权重）” 进行先后次序排列：

1. 优先级别高的排前面。
2. 同一优先级别的再按照权重来选择，权重越大，则排在前面的概率越高。

## 操作本对象的命令

- [ADD IPV6DNSH](command/UNC/20.15.2/ADD-IPV6DNSH.md)
- [LST IPV6DNSH](command/UNC/20.15.2/LST-IPV6DNSH.md)
- [MOD IPV6DNSH](command/UNC/20.15.2/MOD-IPV6DNSH.md)
- [RMV IPV6DNSH](command/UNC/20.15.2/RMV-IPV6DNSH.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IPV6-DNS-Hostfile记录(MOD-IPV6DNSH)_26305696.md`
- 原始手册：`evidence/UNC/20.15.2/删除IPV6-DNS-Hostfile记录(RMV-IPV6DNSH)_72225565.md`
- 原始手册：`evidence/UNC/20.15.2/增加IPV6-DNS-Hostfile记录(ADD-IPV6DNSH)_26145886.md`
- 原始手册：`evidence/UNC/20.15.2/查询IPV6-DNS-Hostfile记录(LST-IPV6DNSH)_72345487.md`
