---
id: UNC@20.15.2@ConfigObject@S1SMARTRULE
type: ConfigObject
name: S1SMARTRULE（S1模式信令抑制规则）
nf: UNC
version: 20.15.2
object_name: S1SMARTRULE
object_kind: entity
applicable_nf:
- MME
status: active
---

# S1SMARTRULE（S1模式信令抑制规则）

## 说明

**适用网元：MME**

该命令用于添加基于用户终端类型的S1模式信令抑制规则：包含附着、服务请求、PDN连接建立流程异常时的抑制措施、唤醒措施、拒绝原因和分离原因。当系统检测到用户信令异常时，按照配置的抑制措施进行抑制，对于已经抑制的用户，达到唤醒条件后，进行唤醒，允许重新接入业务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-S1SMARTRULE]] · ADD S1SMARTRULE
- [[command/UNC/20.15.2/LST-S1SMARTRULE]] · LST S1SMARTRULE
- [[command/UNC/20.15.2/MOD-S1SMARTRULE]] · MOD S1SMARTRULE
- [[command/UNC/20.15.2/RMV-S1SMARTRULE]] · RMV S1SMARTRULE

## 证据

- 原始手册：`evidence/UNC/20.15.2/S1SMARTRULE.md`
- 原始手册：`evidence/UNC/20.15.2/S1SMARTRULE.md`
- 原始手册：`evidence/UNC/20.15.2/S1SMARTRULE.md`
- 原始手册：`evidence/UNC/20.15.2/S1SMARTRULE.md`
