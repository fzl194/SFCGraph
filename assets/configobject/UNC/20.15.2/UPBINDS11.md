---
id: UNC@20.15.2@ConfigObject@UPBINDS11
type: ConfigObject
name: UPBINDS11（SGW-U与SGW-C侧S11接口的绑定关系）
nf: UNC
version: 20.15.2
object_name: UPBINDS11
object_kind: binding
applicable_nf:
- SGW-C
status: active
---

# UPBINDS11（SGW-U与SGW-C侧S11接口的绑定关系）

## 说明

**适用NF：SGW-C**

该命令用于增加SGW-U与SGW-C侧S11接口的绑定关系。

在切换场景下，如果SGW-C不能获取到用户的TAI信息，可以根据该绑定关系为用户选择满足条件的UPF。

该命令必须配置符合实际组网的UPF与S11的绑定关系，否则GW-U故障隔离功能不可用。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-UPBINDS11]] · ADD UPBINDS11
- [[command/UNC/20.15.2/LST-UPBINDS11]] · LST UPBINDS11
- [[command/UNC/20.15.2/MOD-UPBINDS11]] · MOD UPBINDS11
- [[command/UNC/20.15.2/RMV-UPBINDS11]] · RMV UPBINDS11

## 证据

- 原始手册：`evidence/UNC/20.15.2/UPBINDS11.md`
- 原始手册：`evidence/UNC/20.15.2/UPBINDS11.md`
- 原始手册：`evidence/UNC/20.15.2/UPBINDS11.md`
- 原始手册：`evidence/UNC/20.15.2/UPBINDS11.md`
