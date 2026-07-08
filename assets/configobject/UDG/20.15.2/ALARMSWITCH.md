---
id: UDG@20.15.2@ConfigObject@ALARMSWITCH
type: ConfigObject
name: ALARMSWITCH（安全事件告警开关）
nf: UDG
version: 20.15.2
object_name: ALARMSWITCH
object_kind: global_setting
status: active
---

# ALARMSWITCH（安全事件告警开关）

## 说明

此命令用于打开或关闭安全事件告警开关。安全事件包括高危操作和鉴权失败。

- 高危操作：是指在MML界面执行已经添加了二次授权的命令。需要进行二次授权的MML命令可以通过**LST SECAUTHMEM**命令查询。
- 鉴权失败：是指用户成功登录到系统后，在页面访问操作或执行MML命令，系统会先进行角色鉴权。若用户角色不满足当前操作要求的角色集类型，系统会提示鉴权失败。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-ALARMSWITCH]] · LST ALARMSWITCH
- [[command/UDG/20.15.2/SET-ALARMSWITCH]] · SET ALARMSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/ALARMSWITCH.md`
- 原始手册：`evidence/UDG/20.15.2/ALARMSWITCH.md`
