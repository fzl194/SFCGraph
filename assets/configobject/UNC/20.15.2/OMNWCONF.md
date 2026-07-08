---
id: UNC@20.15.2@ConfigObject@OMNWCONF
type: ConfigObject
name: OMNWCONF（OM网络探测参数）
nf: UNC
version: 20.15.2
object_name: OMNWCONF
object_kind: entity
status: active
---

# OMNWCONF（OM网络探测参数）

## 说明

![](配置OM网络探测参数（MOD OMNWCONF）_58550741.assets/notice_3.0-zh-cn_2.png)

网络探测参数修改可能导致OMLB服务主备倒换，可能 **导致网管或VNFM断链** ；关闭网络探测时，会导致OM网络故障无法检测。

用于配置OM网络故障探测参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-OMNWCONF]] · LST OMNWCONF
- [[command/UNC/20.15.2/MOD-OMNWCONF]] · MOD OMNWCONF

## 证据

- 原始手册：`evidence/UNC/20.15.2/OMNWCONF.md`
- 原始手册：`evidence/UNC/20.15.2/OMNWCONF.md`
