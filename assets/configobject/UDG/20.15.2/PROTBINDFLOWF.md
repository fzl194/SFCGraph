---
id: UDG@20.15.2@ConfigObject@PROTBINDFLOWF
type: ConfigObject
name: PROTBINDFLOWF（流过滤器协议绑定关系）
nf: UDG
version: 20.15.2
object_name: PROTBINDFLOWF
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# PROTBINDFLOWF（流过滤器协议绑定关系）

## 说明

**适用NF：PGW-U、UPF**

该命令用于向流过滤器中新增协议与流过滤器绑定关系，使用该protocol的业务会在流过滤器协议层级的匹配流程时可以匹配成功。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-PROTBINDFLOWF]] · ADD PROTBINDFLOWF
- [[command/UDG/20.15.2/LST-PROTBINDFLOWF]] · LST PROTBINDFLOWF
- [[command/UDG/20.15.2/MOD-PROTBINDFLOWF]] · MOD PROTBINDFLOWF
- [[command/UDG/20.15.2/RMV-PROTBINDFLOWF]] · RMV PROTBINDFLOWF

## 关联对象

- [[configobject/UDG/20.15.2/FLOWFILTER]] · FLOWFILTER
- [[configobject/UDG/20.15.2/L7FILTER]] · L7FILTER

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改流过滤器协议绑定关系（MOD-PROTBINDFLOWF）_82837371.md`
- 原始手册：`evidence/UDG/20.15.2/删除流过滤器协议绑定关系（RMV-PROTBINDFLOWF）_82837372.md`
- 原始手册：`evidence/UDG/20.15.2/增加流过滤器协议绑定关系（ADD-PROTBINDFLOWF）_82837370.md`
- 原始手册：`evidence/UDG/20.15.2/查询流过滤器协议绑定关系（LST-PROTBINDFLOWF）_82837373.md`
