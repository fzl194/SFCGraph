---
id: UNC@20.15.2@ConfigObject@ARPEPS2PRER8
type: ConfigObject
name: ARPEPS2PRER8（EPS ARP到Pre-R8 ARP的映射规则）
nf: UNC
version: 20.15.2
object_name: ARPEPS2PRER8
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- GGSN
status: active
---

# ARPEPS2PRER8（EPS ARP到Pre-R8 ARP的映射规则）

## 说明

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于配置Gn接口和Gx接口之间ARP的映射值。

在Gn接口，ARP对应QoSProfile信元中的Allocation/Retention priority字段（3GPP R99 及之后）或Precedence class字段（3GPP R97/R98），取值范围为1~3。在Gx接口，ARP定义有专门的AVP（属性值对），取值范围为1~15。Gn接口和Gx接口的取值范围不一致，需要进行映射。

假设本命令配置的ARP高优先级上限（HIGH）为H，ARP中优先级上限（MEDIUM）为M，则ARP映射规则如下：

在Gn接口到Gx接口方向上，ARP为1时映射为1，ARP为2时映射为H+1，ARP为3时映射为M+1。在Gx接口到Gn接口方向上，ARP在<1，H>、<H+1，M>、<M+1，15>范围之内分别映射到1，2和3。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-ARPEPS2PRER8]] · LST ARPEPS2PRER8
- [[command/UNC/20.15.2/SET-ARPEPS2PRER8]] · SET ARPEPS2PRER8

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询EPS-ARP到Pre-R8-ARP的映射规则（LST-ARPEPS2PRER8）_09652234.md`
- 原始手册：`evidence/UNC/20.15.2/设置EPS-ARP到Pre-R8-ARP的映射规则（SET-ARPEPS2PRER8）_09652254.md`
