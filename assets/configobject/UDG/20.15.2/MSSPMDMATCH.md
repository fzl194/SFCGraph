---
id: UDG@20.15.2@ConfigObject@MSSPMDMATCH
type: ConfigObject
name: MSSPMDMATCH（端口报文匹配统计信息）
nf: UDG
version: 20.15.2
object_name: MSSPMDMATCH
object_kind: global_setting
status: active
---

# MSSPMDMATCH（端口报文匹配统计信息）

## 说明

![](设置端口报文统计开关（SET MSSPMDMATCH）_80692277.assets/notice_3.0-zh-cn.png)

本命令用于使能端口按规则统计报文开关，开启会降低性能，且在用户指定的时间后自动去使能，默认时间是30分钟。

该命令用于设置端口报文规则匹配开关，是诊断开关命令。当端口收发报文异常或者端口流量不通的时候，可以开关打开规则匹配，协助问题定位。

使用包记录功能时，不能对记录的文件做迁移、删除操作，否则会导致包记录功能失效。如果需要清空文件重新记录，只需要关闭所有端口的包记录开关后再打开即可。

默认记录前64字节报文内容，记录文件默认路径/home，单个文件大小20MB，所有文件可占用磁盘空间100MB，可通过MANO注入修改默认配置，其中记录报文长度最大可配64字节。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-MSSPMDMATCH]] · DSP MSSPMDMATCH
- [[command/UDG/20.15.2/SET-MSSPMDMATCH]] · SET MSSPMDMATCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示端口报文匹配统计信息（DSP-MSSPMDMATCH）_32309725.md`
- 原始手册：`evidence/UDG/20.15.2/设置端口报文统计开关（SET-MSSPMDMATCH）_80692277.md`
