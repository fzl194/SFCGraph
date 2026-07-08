---
id: UNC@20.15.2@ConfigObject@IUAUTHCIPH
type: ConfigObject
name: IUAUTHCIPH（Iu模式用户安全参数）
nf: UNC
version: 20.15.2
object_name: IUAUTHCIPH
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# IUAUTHCIPH（Iu模式用户安全参数）

## 说明

![](增加Iu模式用户安全参数(ADD IUAUTHCIPH)_72225327.assets/notice_3.0-zh-cn_2.png)

不开启鉴权功能将导致身份未被鉴别的UE接入系统，引发系统内UE发生串号，计费错误等问题。

**适用网元：SGSN**

该命令用于增加3G鉴权加密的配置。 UNC 可以结合运营商的配置要求和协议规范决定是否使用鉴权加密。针对SGSN节点可能遇到的所有需要鉴权的流程， UNC 均设置了开关加以控制，运营商可以通过配置决定这些流程是否需要鉴权。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IUAUTHCIPH]] · ADD IUAUTHCIPH
- [[command/UNC/20.15.2/LST-IUAUTHCIPH]] · LST IUAUTHCIPH
- [[command/UNC/20.15.2/MOD-IUAUTHCIPH]] · MOD IUAUTHCIPH
- [[command/UNC/20.15.2/RMV-IUAUTHCIPH]] · RMV IUAUTHCIPH

## 证据

- 原始手册：`evidence/UNC/20.15.2/IUAUTHCIPH.md`
- 原始手册：`evidence/UNC/20.15.2/IUAUTHCIPH.md`
- 原始手册：`evidence/UNC/20.15.2/IUAUTHCIPH.md`
- 原始手册：`evidence/UNC/20.15.2/IUAUTHCIPH.md`
