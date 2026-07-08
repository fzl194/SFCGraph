---
id: UDG@20.15.2@ConfigObject@FLOWFILTER
type: ConfigObject
name: FLOWFILTER（流过滤器）
nf: UDG
version: 20.15.2
object_name: FLOWFILTER
object_kind: entity
applicable_nf:
- PGW-U
- UPF
uniqueness_keys:
- - FLOWFILTERNAME
status: active
---

# FLOWFILTER（流过滤器）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加流过滤器。通过FlowFilter下定义L34层Filter、L7层协议、L7层过滤条件等过滤条件组合来实现规则中业务流过滤条件的定义，匹配L34层过滤条件、L7层协议、L7层过滤条件均成功的业务可以命中该流过滤器。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-FLOWFILTER]] · ADD FLOWFILTER
- [[command/UDG/20.15.2/LST-FLOWFILTER]] · LST FLOWFILTER
- [[command/UDG/20.15.2/MOD-FLOWFILTER]] · MOD FLOWFILTER
- [[command/UDG/20.15.2/RMV-FLOWFILTER]] · RMV FLOWFILTER

## 关联对象

- [[configobject/UDG/20.15.2/ADCPARA]] · ADCPARA
- [[configobject/UDG/20.15.2/BLACKLISTRULE]] · BLACKLISTRULE
- [[configobject/UDG/20.15.2/FILTERGROUP]] · FILTERGROUP
- [[configobject/UDG/20.15.2/FLTBINDFLOWF]] · FLTBINDFLOWF
- [[configobject/UDG/20.15.2/PROTBINDFLOWF]] · PROTBINDFLOWF
- [[configobject/UDG/20.15.2/RULE]] · RULE

## 证据

- 原始手册：`evidence/UDG/20.15.2/FLOWFILTER.md`
- 原始手册：`evidence/UDG/20.15.2/FLOWFILTER.md`
- 原始手册：`evidence/UDG/20.15.2/FLOWFILTER.md`
- 原始手册：`evidence/UDG/20.15.2/FLOWFILTER.md`
