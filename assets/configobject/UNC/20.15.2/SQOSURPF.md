---
id: UNC@20.15.2@ConfigObject@SQOSURPF
type: ConfigObject
name: SQOSURPF（流行为安全URPF）
nf: UNC
version: 20.15.2
object_name: SQOSURPF
object_kind: entity
status: active
---

# SQOSURPF（流行为安全URPF）

## 说明

该命令用来增加流行为下的URPF（单播反向路由转发）配置。

一般情况下，网元设备接收到报文，获取报文的目的地址，针对目的地址查找路由。如果找到了就转发报文，否则丢弃该报文。URPF通过获取报文的源地址和入接口，以源地址为目的地址，在转发表中查找源地址对应的接口是否与入接口匹配，如果不匹配，认为源地址是伪装的，丢弃该报文。通过这种方式，URPF就能有效地防范网络中通过修改源地址而进行的恶意攻击行为的发生。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SQOSURPF]] · ADD SQOSURPF
- [[command/UNC/20.15.2/LST-SQOSURPF]] · LST SQOSURPF
- [[command/UNC/20.15.2/MOD-SQOSURPF]] · MOD SQOSURPF
- [[command/UNC/20.15.2/RMV-SQOSURPF]] · RMV SQOSURPF

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改流行为安全URPF（MOD-SQOSURPF）_50121458.md`
- 原始手册：`evidence/UNC/20.15.2/删除流行为安全URPF（RMV-SQOSURPF）_49961998.md`
- 原始手册：`evidence/UNC/20.15.2/增加流行为安全URPF（ADD-SQOSURPF）_50280766.md`
- 原始手册：`evidence/UNC/20.15.2/查询流行为安全URPF（LST-SQOSURPF）_00841749.md`
