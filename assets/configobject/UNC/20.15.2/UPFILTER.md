---
id: UNC@20.15.2@ConfigObject@UPFILTER
type: ConfigObject
name: UPFILTER（UPF过滤组）
nf: UNC
version: 20.15.2
object_name: UPFILTER
object_kind: entity
applicable_nf:
- SMF
status: active
---

# UPFILTER（UPF过滤组）

## 说明

**适用NF：SMF**

该命令用于为UPF添加一个过滤组，并将过滤组ID、DNN、UP节点这三者进行绑定。

UPF节点在不同的DNN下可以拥有不同的过滤器组，因此过滤组绑定参数必须包含DNN。

通过增加一个过滤组可以使得UPF在侦测到满足该过滤组条件的数据流后可以执行特定的操作，比如丢弃。

过滤组具体的参数可以通过LST FILTERGP查询。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-UPFILTER]] · ADD UPFILTER
- [[command/UNC/20.15.2/LST-UPFILTER]] · LST UPFILTER
- [[command/UNC/20.15.2/RMV-UPFILTER]] · RMV UPFILTER

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UPF过滤组（RMV-UPFILTER）_09654423.md`
- 原始手册：`evidence/UNC/20.15.2/增加UPF过滤组（ADD-UPFILTER）_09651422.md`
- 原始手册：`evidence/UNC/20.15.2/查询UPF过滤组（LST-UPFILTER）_09651375.md`
