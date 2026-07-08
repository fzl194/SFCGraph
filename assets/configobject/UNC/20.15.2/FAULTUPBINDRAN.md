---
id: UNC@20.15.2@ConfigObject@FAULTUPBINDRAN
type: ConfigObject
name: FAULTUPBINDRAN（N3接口故障网元组绑定）
nf: UNC
version: 20.15.2
object_name: FAULTUPBINDRAN
object_kind: binding
applicable_nf:
- SGW-C
- SMF
status: active
---

# FAULTUPBINDRAN（N3接口故障网元组绑定）

## 说明

![](增加N3接口故障网元组绑定（ADD FAULTUPBINDRAN）_93542772.assets/notice_3.0-zh-cn_2.png)

该命令可能导致SMF无法选择指定的UPF。

**适用NF：SGW-C、SMF**

该命令用于添加N3接口故障UPF组与故障RAN组的绑定关系，当N3接口出现故障，如果故障UPF组与故障RAN组绑定，SMF在为通过该RAN组绑定的RAN接入的用户选择UPF时，会自动过滤掉与该UPF组绑定的所有UPF。

## 操作本对象的命令

- [ADD FAULTUPBINDRAN](command/UNC/20.15.2/ADD-FAULTUPBINDRAN.md)
- [LST FAULTUPBINDRAN](command/UNC/20.15.2/LST-FAULTUPBINDRAN.md)
- [MOD FAULTUPBINDRAN](command/UNC/20.15.2/MOD-FAULTUPBINDRAN.md)
- [RMV FAULTUPBINDRAN](command/UNC/20.15.2/RMV-FAULTUPBINDRAN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改N3接口故障网元组绑定（MOD-FAULTUPBINDRAN）_39777021.md`
- 原始手册：`evidence/UNC/20.15.2/删除N3接口故障网元组绑定（RMV-FAULTUPBINDRAN）_93222844.md`
- 原始手册：`evidence/UNC/20.15.2/增加N3接口故障网元组绑定（ADD-FAULTUPBINDRAN）_93542772.md`
- 原始手册：`evidence/UNC/20.15.2/查询N3接口故障网元组绑定（LST-FAULTUPBINDRAN）_38422727.md`
