---
id: UDG@20.15.2@ConfigObject@UPGTPPATH
type: ConfigObject
name: UPGTPPATH（路径相关属性）
nf: UDG
version: 20.15.2
object_name: UPGTPPATH
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# UPGTPPATH（路径相关属性）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](设置GTP路径相关属性（SET UPGTPPATH）_82837227.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置UPF主动向对端网元发送GTP请求消息的重发时间间隔和最大尝试发送次数，如果配置不合理，可能导致用户激活失败或资源残留。

该命令用来设置GTP协议配置属性。包括当前系统是否开启GTP路径管理黑白名单功能、系统支持的GTP路径管理名单属性（可配置为黑名单或白名单），主动发送GTP心跳消息的开关属性与发送间隔、主动向对端网元（gNodeB、eNodeB、UPF、S-GW、P-GW或可信非3GPP接入网关）发送GTP请求消息的重发时间间隔和最大尝试发送次数（请求消息包括Echo Request等消息）、路径断告警产生后去激活上下文的开关属性，当去激活上下文的开关打开时，配置心跳检测消息的发送次数。

## 操作本对象的命令

- [LST UPGTPPATH](command/UDG/20.15.2/LST-UPGTPPATH.md)
- [SET UPGTPPATH](command/UDG/20.15.2/SET-UPGTPPATH.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询路径相关属性（LST-UPGTPPATH）_82837228.md`
- 原始手册：`evidence/UDG/20.15.2/设置GTP路径相关属性（SET-UPGTPPATH）_82837227.md`
