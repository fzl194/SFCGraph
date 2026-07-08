---
id: UNC@20.15.2@ConfigObject@TLSPARA
type: ConfigObject
name: TLSPARA（TLS参数）
nf: UNC
version: 20.15.2
object_name: TLSPARA
object_kind: entity
status: active
---

# TLSPARA（TLS参数）

## 说明

![](增加TLS参数（ADD TLSPARA）_84132096.assets/notice_3.0-zh-cn_2.png)

该命令中CIPHER参数用于选择安全算法，DHE相关的算法性能较差，在大量建链场景下会导致本端CPU占用过高以及长时间无法建链的问题，请谨慎使用，建议选择ECDHE算法。

开启服务化接口的TLS协议时，需要配置详细的TLS上下文参数，该命令用于增加一组TLS参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-TLSPARA]] · ADD TLSPARA
- [[command/UNC/20.15.2/LST-TLSPARA]] · LST TLSPARA
- [[command/UNC/20.15.2/MOD-TLSPARA]] · MOD TLSPARA
- [[command/UNC/20.15.2/RMV-TLSPARA]] · RMV TLSPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/TLSPARA.md`
- 原始手册：`evidence/UNC/20.15.2/TLSPARA.md`
- 原始手册：`evidence/UNC/20.15.2/TLSPARA.md`
- 原始手册：`evidence/UNC/20.15.2/TLSPARA.md`
