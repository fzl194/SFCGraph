---
id: UDG@20.15.2@ConfigObject@APNIMSSIGFLTR
type: ConfigObject
name: APNIMSSIGFLTR（APN的IMS分类器）
nf: UDG
version: 20.15.2
object_name: APNIMSSIGFLTR
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# APNIMSSIGFLTR（APN的IMS分类器）

## 说明

**适用NF：PGW-U、UPF**

![](添加APN的IMS分类器（ADD APNIMSSIGFLTR）_82837825.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认添加规则后合法的IMS信令报文都能命中其中一条规则。

该命令用于配置APN下的IMS信令专用上下文的Filter。使用VoLTE语音业务时，需要使用该命令配置IMS信令专用上下文的Filter来设置包的过滤规则。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-APNIMSSIGFLTR]] · ADD APNIMSSIGFLTR
- [[command/UDG/20.15.2/LST-APNIMSSIGFLTR]] · LST APNIMSSIGFLTR
- [[command/UDG/20.15.2/MOD-APNIMSSIGFLTR]] · MOD APNIMSSIGFLTR
- [[command/UDG/20.15.2/RMV-APNIMSSIGFLTR]] · RMV APNIMSSIGFLTR

## 关联对象

- [[configobject/UDG/20.15.2/APN]] · APN

## 证据

- 原始手册：`evidence/UDG/20.15.2/APNIMSSIGFLTR.md`
- 原始手册：`evidence/UDG/20.15.2/APNIMSSIGFLTR.md`
- 原始手册：`evidence/UDG/20.15.2/APNIMSSIGFLTR.md`
- 原始手册：`evidence/UDG/20.15.2/APNIMSSIGFLTR.md`
