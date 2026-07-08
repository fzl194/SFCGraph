---
id: UNC@20.15.2@ConfigObject@DNS
type: ConfigObject
name: DNS（DNS运行参数）
nf: UNC
version: 20.15.2
object_name: DNS
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# DNS（DNS运行参数）

## 说明

**适用网元：SGSN、MME**

该命令用于设置DNS域名解析流程相关参数，如发送查询报文后等待服务器应答的时长、超时重发次数等参数。DNS解析器（SPP进程上负责域名解析的实体）向DNS服务器发送域名解析请求，获取对应的IP地址信息的时候会依照这些参数进行处理。

同时，DNS探测开关、DNS探测间隔、缺省探测域名等参数也用于服务器状态探测。当DNS探测开关打开时，DNS解析器会定期向已配置的DNS服务器发送探测查询报文，并根据响应状况更新服务器状态，以避免解析域名时向一个已经故障的服务器发送查询请求报文。

系统每隔3s（缺省）发送一次探测报文以检测DNS服务器是否故障。不管DNS服务器是否故障，连续3次（缺省故障门限）DNS服务器没有响应，系统就会上报DNS服务器对应的DNS链路故障告警。

DNS服务器是否故障完全由探测报文确定，与DNS解析请求是否成功无关。发送间隔、故障门限等可通过此命令进行配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DNS]] · LST DNS
- [[command/UNC/20.15.2/SET-DNS]] · SET DNS
- [[command/UNC/20.15.2/TST-DNS]] · TST DNS

## 证据

- 原始手册：`evidence/UNC/20.15.2/DNS.md`
- 原始手册：`evidence/UNC/20.15.2/DNS.md`
- 原始手册：`evidence/UNC/20.15.2/DNS.md`
