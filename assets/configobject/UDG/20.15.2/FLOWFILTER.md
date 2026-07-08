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

- [ADD FLOWFILTER](command/UDG/20.15.2/ADD-FLOWFILTER.md)
- [LST FLOWFILTER](command/UDG/20.15.2/LST-FLOWFILTER.md)
- [MOD FLOWFILTER](command/UDG/20.15.2/MOD-FLOWFILTER.md)
- [RMV FLOWFILTER](command/UDG/20.15.2/RMV-FLOWFILTER.md)

## 关联对象

- [ADCPARA](configobject/UDG/20.15.2/ADCPARA.md)
- [BLACKLISTRULE](configobject/UDG/20.15.2/BLACKLISTRULE.md)
- [FILTERGROUP](configobject/UDG/20.15.2/FILTERGROUP.md)
- [FLTBINDFLOWF](configobject/UDG/20.15.2/FLTBINDFLOWF.md)
- [PROTBINDFLOWF](configobject/UDG/20.15.2/PROTBINDFLOWF.md)
- [RULE](configobject/UDG/20.15.2/RULE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改流过滤器（MOD-FLOWFILTER）_82837362.md`
- 原始手册：`evidence/UDG/20.15.2/删除流过滤器（RMV-FLOWFILTER）_82837363.md`
- 原始手册：`evidence/UDG/20.15.2/增加流过滤器（ADD-FLOWFILTER）_82837361.md`
- 原始手册：`evidence/UDG/20.15.2/查询流过滤器（LST-FLOWFILTER）_82837364.md`
