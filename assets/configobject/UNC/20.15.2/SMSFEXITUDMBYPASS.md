---
id: UNC@20.15.2@ConfigObject@SMSFEXITUDMBYPASS
type: ConfigObject
name: SMSFEXITUDMBYPASS（用户退出UDM Bypass任务）
nf: UNC
version: 20.15.2
object_name: SMSFEXITUDMBYPASS
object_kind: action
applicable_nf:
- SMSF
status: active
---

# SMSFEXITUDMBYPASS（用户退出UDM Bypass任务）

## 说明

![](停止用户退出UDM Bypass任务（STP SMSFEXITUDMBYPASS）_04735169.assets/notice_3.0-zh-cn_2.png)

当启动用户退出UDM Bypass任务时，CPU和内存使用率会升高，和周边网元交互消息量增大，待用户退出UDM Bypass任务完成后，系统会恢复正常。

**适用NF：SMSF**

该命令用于启动用户退出UDM Bypass任务。当UDM故障已恢复但用户尚未退出UDM Bypass状态时，可以执行该命令使用户退出UDM Bypass状态。

## 操作本对象的命令

- [STP SMSFEXITUDMBYPASS](command/UNC/20.15.2/STP-SMSFEXITUDMBYPASS.md)
- [STR SMSFEXITUDMBYPASS](command/UNC/20.15.2/STR-SMSFEXITUDMBYPASS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止用户退出UDM-Bypass任务（STP-SMSFEXITUDMBYPASS）_04735169.md`
- 原始手册：`evidence/UNC/20.15.2/启动用户退出UDM-Bypass任务（STR-SMSFEXITUDMBYPASS）_54655106.md`
