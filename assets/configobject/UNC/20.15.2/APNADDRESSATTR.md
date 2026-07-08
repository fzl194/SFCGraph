---
id: UNC@20.15.2@ConfigObject@APNADDRESSATTR
type: ConfigObject
name: APNADDRESSATTR（基于APN的地址分配属性）
nf: UNC
version: 20.15.2
object_name: APNADDRESSATTR
object_kind: global_setting
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# APNADDRESSATTR（基于APN的地址分配属性）

## 说明

![](设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.assets/notice_3.0-zh-cn_2.png)

设置SUPPORTIPV4参数或SUPPORTIPV6参数为DISABLE（不使能）时，请同时设置SUPPORTPRIOR和IPTYPEFORDUALIP参数。否则，仅设置SUPPORTIPV4为DISABLE（不使能），会基于配置原则自动修改IPTYPEFORDUALIP为IPV6。仅设置SUPPORTIPV6为DISABLE（不使能），会基于配置原则自动修改SUPPORTPRIOR和IPTYPEFORDUALIP为IPV4。

**适用NF：SMF、PGW-C、GGSN**

该命令用于以APN的粒度控制地址分配属性。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-APNADDRESSATTR]] · LST APNADDRESSATTR
- [[command/UNC/20.15.2/SET-APNADDRESSATTR]] · SET APNADDRESSATTR

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于APN的地址分配属性（LST-APNADDRESSATTR）_09651663.md`
- 原始手册：`evidence/UNC/20.15.2/设置基于APN的地址分配属性（SET-APNADDRESSATTR）_33845575.md`
