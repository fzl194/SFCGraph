---
id: UNC@20.15.2@ConfigObject@USEROFFLOAD
type: ConfigObject
name: USEROFFLOAD（用户迁移）
nf: UNC
version: 20.15.2
object_name: USEROFFLOAD
object_kind: action
applicable_nf:
- MME
status: active
---

# USEROFFLOAD（用户迁移）

## 说明

**适用网元：MME**

S-GW或P-GW发生故障时，本命令用于立即启动单个用户业务迁移功能，其中业务迁移是指将用户业务迁移至正常的S-GW，或者去激活PDN使用户在其他正常的P-GW上重新激活PDN，本命令主要用于测试场景。

## 操作本对象的命令

- [[command/UNC/20.15.2/STR-USEROFFLOAD]] · STR USEROFFLOAD

## 证据

- 原始手册：`evidence/UNC/20.15.2/执行用户迁移(STR-USEROFFLOAD)_72225763.md`
