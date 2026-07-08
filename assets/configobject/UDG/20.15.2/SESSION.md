---
id: UDG@20.15.2@ConfigObject@SESSION
type: ConfigObject
name: SESSION（用户会话）
nf: UDG
version: 20.15.2
object_name: SESSION
object_kind: action
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SESSION（用户会话）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](去活用户会话（DEA SESSION）_82837084.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，当批量去激活用户时，系统负荷增大，CPU使用率会有一定程度的升高。待去激活完成后，系统会恢复正常。当批量去激活方式完成之后，需要将已锁定的组、APN等解锁，否则后续使用该组、APN等激活的用户会激活失败。

该命令用于去激活用户，假设运营商需要去激活用户，可选择apn、TRUNK、imsi、msisdn、imei、userprofile、NF、NodeId等方式去活用户。即当需要手动在系统上去激活用户时，使用该命令。

## 操作本对象的命令

- [DEA SESSION](command/UDG/20.15.2/DEA-SESSION.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/去活用户会话（DEA-SESSION）_82837084.md`
