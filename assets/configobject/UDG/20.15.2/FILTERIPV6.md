---
id: UDG@20.15.2@ConfigObject@FILTERIPV6
type: ConfigObject
name: FILTERIPV6（IPv6过滤器）
nf: UDG
version: 20.15.2
object_name: FILTERIPV6
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# FILTERIPV6（IPv6过滤器）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加过滤器，其中包含三、四层的协议、源端口号、目的端口号、源IPv6地址和目的IPv6地址等。数据报文通过时，系统会根据过滤器选择到对应的规则，然后执行选中规则对应的计费策略和动作策略。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-FILTERIPV6]] · ADD FILTERIPV6
- [[command/UDG/20.15.2/MOD-FILTERIPV6]] · MOD FILTERIPV6

## 关联对象

- [[configobject/UDG/20.15.2/FLTBINDFLOWF]] · FLTBINDFLOWF
- [[configobject/UDG/20.15.2/IPLIST]] · IPLIST

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPv6过滤器（MOD-FILTERIPV6）_86528791.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPv6过滤器（ADD-FILTERIPV6）_82837350.md`
