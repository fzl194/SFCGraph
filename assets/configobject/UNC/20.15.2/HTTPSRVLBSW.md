---
id: UNC@20.15.2@ConfigObject@HTTPSRVLBSW
type: ConfigObject
name: HTTPSRVLBSW（HTTP服务端负载重均衡功能）
nf: UNC
version: 20.15.2
object_name: HTTPSRVLBSW
object_kind: global_setting
status: active
---

# HTTPSRVLBSW（HTTP服务端负载重均衡功能）

## 说明

![](设置HTTP服务端负载重均衡功能（SET HTTPSRVLBSW）_29291779.assets/notice_3.0-zh-cn_2.png)

系统触发负载重均衡处理过程中会在服务端主动发起链路释放，客户端在感知到链路释放以后会触发链路重建，链路重建过程中会有业务抖动。

该命令用于设置HTTP服务端负载重均衡功能开关以及监控参数和门限，当开关打开时系统会基于该命令设置的采样周期和采样次数定时采样各个HTTP进程的负载，并基于多次采样的结果监控各个HTTP进程的负载，在监控到需要重均衡时系统自动发起负载重均衡处理。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-HTTPSRVLBSW]] · LST HTTPSRVLBSW
- [[command/UNC/20.15.2/SET-HTTPSRVLBSW]] · SET HTTPSRVLBSW

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP服务端负载重均衡功能（LST-HTTPSRVLBSW）_29053331.md`
- 原始手册：`evidence/UNC/20.15.2/设置HTTP服务端负载重均衡功能（SET-HTTPSRVLBSW）_29291779.md`
