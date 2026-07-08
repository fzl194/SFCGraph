---
id: UDG@20.15.2@ConfigObject@PODCONFIG
type: ConfigObject
name: PODCONFIG（POD配置查询）
nf: UDG
version: 20.15.2
object_name: PODCONFIG
object_kind: global_setting
status: active
---

# PODCONFIG（POD配置查询）

## 说明

![](POD配置设置（SET PODCONFIG）_95117138.assets/notice_3.0-zh-cn.png)

设置系统的修复Pod功能开关状态，可能会导致业务受到影响，请谨慎使用该命令。

本命令用于设置系统的修复Pod功能开关状态。

> **说明**
> - “修复开关”的系统初始值为“ON”。
> - 当服务实例出现异常时，“修复开关”由“OFF”设置为“ON”，系统会在30分钟后对故障Pod进行修复。
> - “修复开关”打开时，如果服务实例出现异常从注册中心下线，那么服务治理模块会修复异常实例所在Pod来自愈业务；“修复开关”关闭时，不会修复异常实例所在的Pod。
> - 在网元应用升级或回退、补丁安装或回退过程中，“修复开关”应当处于关闭状态，因此请勿执行此命令。

## 操作本对象的命令

- [DSP PODCONFIG](command/UDG/20.15.2/DSP-PODCONFIG.md)
- [SET PODCONFIG](command/UDG/20.15.2/SET-PODCONFIG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/POD配置查询（DSP-PODCONFIG）_95277150.md`
- 原始手册：`evidence/UDG/20.15.2/POD配置设置（SET-PODCONFIG）_95117138.md`
