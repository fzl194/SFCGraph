---
id: UNC@20.15.2@ConfigObject@ACSPEERCFG
type: ConfigObject
name: ACSPEERCFG（或停止ACS与远端设备的配置同步）
nf: UNC
version: 20.15.2
object_name: ACSPEERCFG
object_kind: action
status: active
---

# ACSPEERCFG（或停止ACS与远端设备的配置同步）

## 说明

![](启动或停止ACS与远端设备的配置同步(SYN ACSPEERCFG)_87242094.assets/notice_3.0-zh-cn_2.png)

该命令需要大约5分钟完成，命令执行期间系统的操作维护类命令无法执行，且会导致系统CPU和内存升高，如在话务高峰期需谨慎执行。

该命令用于手动开始或停止ACS服务向其他微服务执行配置同步操作。当其他微服务与ACS服务配置不一致时，可使用该命令进行手动配置同步，将ACS的配置强制同步给其他微服务。

> **说明**
> ACS服务会在每日凌晨3:00向其他微服务进行自动配置同步。当触发配置同步时，可能会导致网元CPU和内存持续较高。

## 操作本对象的命令

- [[command/UNC/20.15.2/SYN-ACSPEERCFG]] · SYN ACSPEERCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动或停止ACS与远端设备的配置同步(SYN-ACSPEERCFG)_87242094.md`
