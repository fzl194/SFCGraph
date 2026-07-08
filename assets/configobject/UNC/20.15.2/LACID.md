---
id: UNC@20.15.2@ConfigObject@LACID
type: ConfigObject
name: LACID（LAC组内绑定的LAC号段）
nf: UNC
version: 20.15.2
object_name: LACID
object_kind: entity
applicable_nf:
- GGSN
status: active
---

# LACID（LAC组内绑定的LAC号段）

## 说明

**适用NF：GGSN**

该命令用来在LAC组内绑定LAC号段。当需要在指定LAC组内绑定某个LAC号段时，使用该命令。SMF对来自某个LAC号段的用户进行虚拟APN的映射，将不同位置区域映射到不同的真实APN，真实APN下配置特定的IP地址池，以此建立用户IP地址与用户位置区域的对应关系，以便其它设备根据用户的IP地址做相应的策略控制。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LACID]] · ADD LACID
- [[command/UNC/20.15.2/LST-LACID]] · LST LACID
- [[command/UNC/20.15.2/RMV-LACID]] · RMV LACID

## 证据

- 原始手册：`evidence/UNC/20.15.2/LACID.md`
- 原始手册：`evidence/UNC/20.15.2/LACID.md`
- 原始手册：`evidence/UNC/20.15.2/LACID.md`
