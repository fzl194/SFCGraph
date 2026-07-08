---
id: UDG@20.15.2@ConfigObject@HTTPSRVLBSW
type: ConfigObject
name: HTTPSRVLBSW（HTTP服务端负载重均衡功能）
nf: UDG
version: 20.15.2
object_name: HTTPSRVLBSW
object_kind: global_setting
status: active
---

# HTTPSRVLBSW（HTTP服务端负载重均衡功能）

## 说明

![](设置HTTP服务端负载重均衡功能（SET HTTPSRVLBSW）_29291779.assets/notice_3.0-zh-cn.png)

系统触发负载重均衡处理过程中会在服务端主动发起链路释放，客户端在感知到链路释放以后会触发链路重建，链路重建过程中会有业务抖动。

该命令用于设置HTTP服务端负载重均衡功能开关以及监控参数和门限，当开关打开时系统会基于该命令设置的采样周期和采样次数定时采样各个HTTP进程的负载，并基于多次采样的结果监控各个HTTP进程的负载，在监控到需要重均衡时系统自动发起负载重均衡处理。

> **说明**
> - 该命令执行后立即生效。
>
> - 此命令调整服务端负载均衡的功能生效范围仅限单个POD内，如果期望服务端链路整系统负载均衡，请使用[**SET TLBGLBCONF**](../整系统负载管理/全局属性/设置TLB全局配置（SET TLBGLBCONF）_69954926.md)命令打开TLB开关。
> - 此命令中的LBFUNSWITCH开关配置与TLBGLBCONF（TLB全局属性）中的TLBGLBSW开关不能同时打开，若期望打开LBFUNSWITCH开关则请先执行[**LST TLBGLBCONF**](../整系统负载管理/全局属性/查询TLB全局配置（LST TLBGLBCONF）_15834601.md)命令确认TLBGLBSW配置为OFF。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | LBFUNSWITCH | RELBDEVTHD | RELBMAXTHD |
> | --- | --- | --- |
> | OFF | 10 | 60 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-HTTPSRVLBSW]] · LST HTTPSRVLBSW
- [[command/UDG/20.15.2/SET-HTTPSRVLBSW]] · SET HTTPSRVLBSW

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP服务端负载重均衡功能（LST-HTTPSRVLBSW）_29053331.md`
- 原始手册：`evidence/UDG/20.15.2/设置HTTP服务端负载重均衡功能（SET-HTTPSRVLBSW）_29291779.md`
