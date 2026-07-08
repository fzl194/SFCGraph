---
id: UDG@20.15.2@ConfigObject@L2TPN4KEY
type: ConfigObject
name: L2TPN4KEY（L2TP N4密码配置）
nf: UDG
version: 20.15.2
object_name: L2TPN4KEY
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# L2TPN4KEY（L2TP N4密码配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置L2TP N4密码配置（SET L2TPN4KEY）_64015280.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，需要与SMF的配置保持一致，否则可能会导致L2TP用户激活失败。

该命令用于配置N4接口L2TP私有信元PCO info和Tunnel info的密钥。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-L2TPN4KEY]] · LST L2TPN4KEY
- [[command/UDG/20.15.2/SET-L2TPN4KEY]] · SET L2TPN4KEY

## 证据

- 原始手册：`evidence/UDG/20.15.2/L2TPN4KEY.md`
- 原始手册：`evidence/UDG/20.15.2/L2TPN4KEY.md`
