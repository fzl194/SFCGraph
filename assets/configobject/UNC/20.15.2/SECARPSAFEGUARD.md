---
id: UNC@20.15.2@ConfigObject@SECARPSAFEGUARD
type: ConfigObject
name: SECARPSAFEGUARD（ARP双向分离）
nf: UNC
version: 20.15.2
object_name: SECARPSAFEGUARD
object_kind: global_setting
status: active
---

# SECARPSAFEGUARD（ARP双向分离）

## 说明

该命令用于设置ARP双向分离。

应答报文是本机向其他设备发出的ARP请求报文得到的正常应答，所以只要能够判定其是本机发出的，可以认定并不是攻击报文。所以要解决瞬时超过设备处理能力范围的大流量ARP攻击问题，可以将ARP请求和ARP应答分开处理。

针对ARP请求进行“无状态应答”，即直接在转发层面进行ARP应答，之后不产生ARP表项及相关的状态，不上送CPU进行处理。

针对ARP应答只上送CPU请求过的ARP报文，CPU没有发出的ARP请求产生的ARP应答报文将被丢弃，可以有效保证CPU请求过的正常主机的ARP请求报文正常处理。

## 操作本对象的命令

- [LST SECARPSAFEGUARD](command/UNC/20.15.2/LST-SECARPSAFEGUARD.md)
- [SET SECARPSAFEGUARD](command/UNC/20.15.2/SET-SECARPSAFEGUARD.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询ARP双向分离（LST-SECARPSAFEGUARD）_49961834.md`
- 原始手册：`evidence/UNC/20.15.2/设置ARP双向分离（SET-SECARPSAFEGUARD）_00440345.md`
