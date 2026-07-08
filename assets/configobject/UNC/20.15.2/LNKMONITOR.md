---
id: UNC@20.15.2@ConfigObject@LNKMONITOR
type: ConfigObject
name: LNKMONITOR（链路频繁闪断监控配置）
nf: UNC
version: 20.15.2
object_name: LNKMONITOR
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# LNKMONITOR（链路频繁闪断监控配置）

## 说明

**适用网元：SGSN、MME**

本命令用于设置当系统中大量链路频繁闪断时是否上报告警提示，以及大量链路频繁闪断的告警上报条件。

当前仅支持S1链路的频繁闪断监控，其原理说明如下：当系统中的S1链路发生瞬间闪断，闪断时间小于防闪断定时器时长时，系统不会有告警提示。但当某条链路频繁闪断时，会上报此链路频繁闪断的异常事件，并记录文件。当短时间内系统中有大量链路发生频繁闪断时，对系统业务会有明显影响，需要告警提示。

> **说明**
> - 防闪断定时器时长默认40s，可通过[**SET S1APPARA**](../../../S1接口管理/S1AP协议参数/设置S1AP协议参数(SET S1APPARA)_72225935.md)命令的“防闪断定时器(s)”参数进行配置。
> - 频繁闪断指某条链路在T时间内闪断5次及以上，T的取值与“防闪断定时器(s)”取值有关：当“防闪断定时器(s)”小于等于1分钟时，T取5分钟；当“防闪断定时器(s)”超过1分钟时，T取5倍“防闪断定时器(s)”时长。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-LNKMONITOR]] · LST LNKMONITOR
- [[command/UNC/20.15.2/SET-LNKMONITOR]] · SET LNKMONITOR

## 证据

- 原始手册：`evidence/UNC/20.15.2/LNKMONITOR.md`
- 原始手册：`evidence/UNC/20.15.2/LNKMONITOR.md`
