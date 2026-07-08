---
id: UDG@20.15.2@ConfigObject@FLTBINDFLOWF
type: ConfigObject
name: FLTBINDFLOWF（流过滤器的过滤器绑定关系）
nf: UDG
version: 20.15.2
object_name: FLTBINDFLOWF
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# FLTBINDFLOWF（流过滤器的过滤器绑定关系）

## 说明

**适用NF：PGW-U、UPF**

该命令用于新增过滤器与流过滤器绑定关系，使用该过滤条件的业务可以成功匹配该流过滤器的L34层过滤条件。

## 操作本对象的命令

- [ADD FLTBINDFLOWF](command/UDG/20.15.2/ADD-FLTBINDFLOWF.md)
- [LST FLTBINDFLOWF](command/UDG/20.15.2/LST-FLTBINDFLOWF.md)
- [RMV FLTBINDFLOWF](command/UDG/20.15.2/RMV-FLTBINDFLOWF.md)

## 关联对象

- [FILTER](configobject/UDG/20.15.2/FILTER.md)
- [FILTERIPV6](configobject/UDG/20.15.2/FILTERIPV6.md)
- [FLOWFILTER](configobject/UDG/20.15.2/FLOWFILTER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除流过滤器的过滤器绑定关系（RMV-FLTBINDFLOWF）_82837367.md`
- 原始手册：`evidence/UDG/20.15.2/增加流过滤器的过滤器绑定关系（ADD-FLTBINDFLOWF）_82837366.md`
- 原始手册：`evidence/UDG/20.15.2/查询流过滤器的过滤器绑定关系（LST-FLTBINDFLOWF）_82837368.md`
