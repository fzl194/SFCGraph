---
id: UDG@20.15.2@ConfigObject@GIREDIRECTPARA
type: ConfigObject
name: GIREDIRECTPARA（单一Gi重定向信息）
nf: UDG
version: 20.15.2
object_name: GIREDIRECTPARA
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# GIREDIRECTPARA（单一Gi重定向信息）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用来配置指定VPN下的IPv4或IPv6报文Gi重定向参数，在需要控制UE之间互访的恶意攻击报文和需要通过网关将报文重定向来保证网络的安全的场景下使用此命令。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-GIREDIRECTPARA]] · ADD GIREDIRECTPARA
- [[command/UDG/20.15.2/LST-GIREDIRECTPARA]] · LST GIREDIRECTPARA
- [[command/UDG/20.15.2/MOD-GIREDIRECTPARA]] · MOD GIREDIRECTPARA
- [[command/UDG/20.15.2/RMV-GIREDIRECTPARA]] · RMV GIREDIRECTPARA

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改单一Gi重定向信息（MOD-GIREDIRECTPARA）_82837770.md`
- 原始手册：`evidence/UDG/20.15.2/删除单一Gi重定向信息（RMV-GIREDIRECTPARA）_86526574.md`
- 原始手册：`evidence/UDG/20.15.2/查询单一Gi重定向信息（LST-GIREDIRECTPARA）_82837769.md`
- 原始手册：`evidence/UDG/20.15.2/添加单一Gi重定向信息（ADD-GIREDIRECTPARA）_82837767.md`
