---
id: UDG@20.15.2@ConfigObject@MULTIDNNPARA
type: ConfigObject
name: MULTIDNNPARA（MultiDNN参数）
nf: UDG
version: 20.15.2
object_name: MULTIDNNPARA
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# MULTIDNNPARA（MultiDNN参数）

## 说明

**适用NF：PGW-U、UPF**

![](设置MultiDNN参数（SET MULTIDNNPARA）_71934848.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，N4RPTSW若设为DISABLE，则不会在N4偶联消息中上报当前的双DNN功能，系统将不支持双DNN会话。

该命令用于配置MultiDNN参数。

## 操作本对象的命令

- [LST MULTIDNNPARA](command/UDG/20.15.2/LST-MULTIDNNPARA.md)
- [SET MULTIDNNPARA](command/UDG/20.15.2/SET-MULTIDNNPARA.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示MultiDNN参数（LST-MULTIDNNPARA）_70853530.md`
- 原始手册：`evidence/UDG/20.15.2/设置MultiDNN参数（SET-MULTIDNNPARA）_71934848.md`
