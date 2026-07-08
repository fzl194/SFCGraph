---
id: UNC@20.15.2@ConfigObject@SEGTBLINFO
type: ConfigObject
name: SEGTBLINFO（号段表信息）
nf: UNC
version: 20.15.2
object_name: SEGTBLINFO
object_kind: query_target
applicable_nf:
- NRF
status: active
---

# SEGTBLINFO（号段表信息）

## 说明

**适用NF：NRF**

该命令用于查询所有A、B表的主备状态及NF的号段支持等信息。

当需要通过号段配置文件方式刷新NF支持的号段信息时，可以通过此命令查看备表的状态信息，进而执行ACT SEGFILE命令进行备表的激活。

若要查询所有的记录，请不要输入参数；若要查询特定号段类型的记录，请输入“号段类型”参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-SEGTBLINFO]] · DSP SEGTBLINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示号段表信息（DSP-SEGTBLINFO）_09651717.md`
