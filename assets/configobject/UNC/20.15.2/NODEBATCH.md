---
id: UNC@20.15.2@ConfigObject@NODEBATCH
type: ConfigObject
name: NODEBATCH（节点批量复位）
nf: UNC
version: 20.15.2
object_name: NODEBATCH
object_kind: action
status: active
---

# NODEBATCH（节点批量复位）

## 说明

![](节点批量复位（RST NODEBATCH）_73743460.assets/notice_3.0-zh-cn_2.png)

- 执行该命令会批量复位指定网元ID下的所有非Stopped状态的节点，影响节点上的业务，请慎重使用该命令。
- 在存储故障期间，执行该命令批量复位节点后，这些节点以及节点中的容器和进程，在存储恢复前都无法启动。
- 在扩容后30min内进行批量复位，存在不对扩容节点复位的问题，当出现此情况时，请执行**[RST NODE](节点复位（RST NODE）_71765322.md)**对未复位的节点进行复位。
- 在缩容后30min内进行批量复位，存在批量复位不生效或者失败的问题，当出现此情况时，请在缩容30min后再次进行批量复位操作，或者通过**[DSP NODE](节点查询（DSP NODE）_71678755.md)**查询节点信息，通过**[RST NODE](节点复位（RST NODE）_71765322.md)**对未复位的节点进行复位。
- 执行该命令批量复位节点后会重新加载适配包资源。复位前未关闭MML前台界面，可能会影响MML适配包加载，导致MML命令执行失败，此时需要清理浏览器缓存，再刷新界面即可正常执行MML命令。

本命令用于复位指定网元ID下的所有节点。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 操作本对象的命令

- [[command/UNC/20.15.2/RST-NODEBATCH]] · RST NODEBATCH

## 证据

- 原始手册：`evidence/UNC/20.15.2/NODEBATCH.md`
