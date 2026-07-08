---
id: UDG@20.15.2@ConfigObject@SERVICESTAT
type: ConfigObject
name: SERVICESTAT（业务统计配置）
nf: UDG
version: 20.15.2
object_name: SERVICESTAT
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# SERVICESTAT（业务统计配置）

## 说明

**适用NF：PGW-U、UPF**

![](增加业务统计配置（ADD SERVICESTAT）_82837843.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于添加基于业务的性能统计对象组合，配置是否统计HTTP协议和DNS协议的请求次数、成功/错误响应次数和响应时延等。

同一个性能统计对象组合中所包含的协议和规则是“与”的关系，报文必须同时匹配中才能上报，而协议与协议、规则与规则之间是“或”的关系。

如果性能统计对象添加了基于用户接入属性相关的配置，用户激活时会先进行用户接入属性的匹配，匹配中后才会进行后续的协议、规则的匹配。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-SERVICESTAT]] · ADD SERVICESTAT
- [[command/UDG/20.15.2/LST-SERVICESTAT]] · LST SERVICESTAT
- [[command/UDG/20.15.2/MOD-SERVICESTAT]] · MOD SERVICESTAT
- [[command/UDG/20.15.2/RMV-SERVICESTAT]] · RMV SERVICESTAT

## 证据

- 原始手册：`evidence/UDG/20.15.2/SERVICESTAT.md`
- 原始手册：`evidence/UDG/20.15.2/SERVICESTAT.md`
- 原始手册：`evidence/UDG/20.15.2/SERVICESTAT.md`
- 原始手册：`evidence/UDG/20.15.2/SERVICESTAT.md`
