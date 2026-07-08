---
id: UNC@20.15.2@ConfigObject@FILTERGP
type: ConfigObject
name: FILTERGP（过滤组）
nf: UNC
version: 20.15.2
object_name: FILTERGP
object_kind: entity
applicable_nf:
- SMF
status: active
---

# FILTERGP（过滤组）

## 说明

**适用NF：SMF**

该命令用于增加过滤组，用于用户激活会话时，为支持ULCL或BP功能的UP增加一组过滤器。

过滤组是过滤器的集合，供UPF使用，为ULCL或BP增加一组过滤规则。

过滤器用于在用户激活会话时，为以下类型的UPF配置业务数据流过滤规则，如数据流的方向、远端IP地址以及UE端IP地址等。UPF根据该规则进行数据流的过滤筛选或者执行特定转发动作。

具备分流功能可以将本地业务转发到本地会话锚点UPF上的ULCL UPF。

具备分叉点功能可以将IPv6多宿主PDU会话数据转发到不同本地会话锚点UPF上的BP UPF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-FILTERGP]] · ADD FILTERGP
- [[command/UNC/20.15.2/LST-FILTERGP]] · LST FILTERGP
- [[command/UNC/20.15.2/MOD-FILTERGP]] · MOD FILTERGP
- [[command/UNC/20.15.2/RMV-FILTERGP]] · RMV FILTERGP

## 证据

- 原始手册：`evidence/UNC/20.15.2/FILTERGP.md`
- 原始手册：`evidence/UNC/20.15.2/FILTERGP.md`
- 原始手册：`evidence/UNC/20.15.2/FILTERGP.md`
- 原始手册：`evidence/UNC/20.15.2/FILTERGP.md`
