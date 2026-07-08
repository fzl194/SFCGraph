---
id: UDG@20.15.2@ConfigObject@SECPOLICYAPPLNK
type: ConfigObject
name: SECPOLICYAPPLNK（应用联动默认动作）
nf: UDG
version: 20.15.2
object_name: SECPOLICYAPPLNK
object_kind: global_setting
status: active
---

# SECPOLICYAPPLNK（应用联动默认动作）

## 说明

该命令用于设置应用联动的缺省动作。

执行SET SECPOLICYAPPLNK命令可以设置应用层联动功能对上送CPU的报文的默认处理方式。当需要进行应用层协议攻击分析时，可以将协议报文的处理方式配置成Min_to_cp模式，这样就可以获取上送的协议报文，从而进行攻击溯源。

缺省情况下，应用层联动功能是使能的。

只有应用层联动使能情况下，此命令才有效。

## 操作本对象的命令

- [DSP SECPOLICYAPPLNK](command/UDG/20.15.2/DSP-SECPOLICYAPPLNK.md)
- [SET SECPOLICYAPPLNK](command/UDG/20.15.2/SET-SECPOLICYAPPLNK.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示应用联动默认动作（DSP-SECPOLICYAPPLNK）_50120690.md`
- 原始手册：`evidence/UDG/20.15.2/设置应用联动默认动作（SET-SECPOLICYAPPLNK）_49801822.md`
