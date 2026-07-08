---
id: UNC@20.15.2@ConfigObject@NGRANCTX
type: ConfigObject
name: NGRANCTX（NG-RAN上下文）
nf: UNC
version: 20.15.2
object_name: NGRANCTX
object_kind: action
applicable_nf:
- AMF
status: active
---

# NGRANCTX（NG-RAN上下文）

## 说明

![](清除NG-RAN上下文（CLR NGRANCTX）_09651514.assets/notice_3.0-zh-cn_2.png)

执行本命令将导致AMF释放与指定NG-RAN之间的SCTP连接，同时会释放通过该NG-RAN接入的用户上下文或基站上下文，从而导致业务中断。

**适用NF：AMF**

该命令用于在AMF上清除指定的NG-RAN上下文。

## 操作本对象的命令

- [CLR NGRANCTX](command/UNC/20.15.2/CLR-NGRANCTX.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除NG-RAN上下文（CLR-NGRANCTX）_09651514.md`
