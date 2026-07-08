---
id: UNC@20.15.2@ConfigObject@MMECFG
type: ConfigObject
name: MMECFG（发送MME配置信息）
nf: UNC
version: 20.15.2
object_name: MMECFG
object_kind: action
applicable_nf:
- MME
status: active
---

# MMECFG（发送MME配置信息）

## 说明

![](发送MME配置信息 (SND MMECFG)_72225769.assets/notice_3.0-zh-cn_2.png)

该命令执行后会改变eNodeB上该MME权重。

**适用网元：MME**

MME组Pool时，单个eNodeB会连接多个MME。该命令用于存储BYPASS状态时应急配置或针对特定MME调测。

## 操作本对象的命令

- [SND MMECFG](command/UNC/20.15.2/SND-MMECFG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/发送MME配置信息-(SND-MMECFG)_72225769.md`
