---
id: UNC@20.15.2@ConfigObject@N40APIVER
type: ConfigObject
name: N40APIVER（N40接口协议版本和需要使用的FeatureList）
nf: UNC
version: 20.15.2
object_name: N40APIVER
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# N40APIVER（N40接口协议版本和需要使用的FeatureList）

## 说明

![](设置N40接口协议版本和需要使用的FeatureList（SET N40APIVER）_31773565.assets/notice_3.0-zh-cn_2.png)

此操作会修改N40接口的功能和信元携带能力，如果CHF不支持对应的功能或信元，将无法正常处理SMF发送的消息。

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置N40接口协议版本、需要使用的FeatureList和是否携带指定消息属性。

不同运营商对N40接口有不同的协议版本要求，SMF支持根据现网实际情况配置指定N40接口支持的协议版本，并支持在该协议版本基础上叠加指定的增加功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-N40APIVER]] · LST N40APIVER
- [[command/UNC/20.15.2/SET-N40APIVER]] · SET N40APIVER

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N40接口协议版本和需要使用的FeatureList（LST-N40APIVER）_31773563.md`
- 原始手册：`evidence/UNC/20.15.2/设置N40接口协议版本和需要使用的FeatureList（SET-N40APIVER）_31773565.md`
