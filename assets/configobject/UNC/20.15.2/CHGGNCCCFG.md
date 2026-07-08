---
id: UNC@20.15.2@ConfigObject@CHGGNCCCFG
type: ConfigObject
name: CHGGNCCCFG（Gn接口计费属性选择策略）
nf: UNC
version: 20.15.2
object_name: CHGGNCCCFG
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# CHGGNCCCFG（Gn接口计费属性选择策略）

## 说明

**适用网元：SGSN**

该命令用于增加 “SPECIAL_USER(指定用户)” 的Gn接口计费属性选择策略。对于签约用户级计费属性和签约APN级计费属性，根据签约有效、签约无效和未签约三种场景分别进行处理。在进行策略选择的时候，使用先APN级后用户级的顺序将签约的计费属性与配置中的有效计费属性进行匹配，如果匹配结果是签约信息有效，则SGSN在向GGSN发出的Create PDP Context Request消息中直接携带签约的计费属性，否则根据配置信息，选择相应的策略进行处理。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CHGGNCCCFG]] · ADD CHGGNCCCFG
- [[command/UNC/20.15.2/LST-CHGGNCCCFG]] · LST CHGGNCCCFG
- [[command/UNC/20.15.2/MOD-CHGGNCCCFG]] · MOD CHGGNCCCFG
- [[command/UNC/20.15.2/RMV-CHGGNCCCFG]] · RMV CHGGNCCCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Gn接口计费属性选择策略(MOD-CHGGNCCCFG)_72225051.md`
- 原始手册：`evidence/UNC/20.15.2/删除Gn接口计费属性选择策略(RMV-CHGGNCCCFG)_26145370.md`
- 原始手册：`evidence/UNC/20.15.2/增加Gn接口计费属性选择策略(ADD-CHGGNCCCFG)_72344971.md`
- 原始手册：`evidence/UNC/20.15.2/查询Gn接口计费属性选择策略(LST-CHGGNCCCFG)_26305186.md`
