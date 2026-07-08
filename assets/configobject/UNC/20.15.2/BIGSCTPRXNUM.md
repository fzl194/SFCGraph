---
id: UNC@20.15.2@ConfigObject@BIGSCTPRXNUM
type: ConfigObject
name: BIGSCTPRXNUM（大端模式SCTP接收缓冲区参数）
nf: UNC
version: 20.15.2
object_name: BIGSCTPRXNUM
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# BIGSCTPRXNUM（大端模式SCTP接收缓冲区参数）

## 说明

![](设置大端模式SCTP接收缓冲区参数(SET BIGSCTPRXNUM)_26238016.assets/notice_3.0-zh-cn_2.png)

修改参数需要复位SGP进程才能生效，如果配置不合理会导致进程启动故障。

**适用网元：MME**

该命令用于设置大端模式SCTP接收缓冲区参数。缓冲区分为大缓冲区和小缓冲区，缓冲区分块规格包含max块、med块和min块。使用大缓冲区的接口有Iu（M3UA协议）、S6a/S6d（Diameter协议）、SBc、SGs和SLs；使用小缓冲区的接口有S1-MME和N2。SCTP会将接收到的报文根据大小存放到合适的块内。该命令只控制使用大缓冲区的max块个数。

该命令的使用场景：当CBC发送的消息超过64K时，可通过本命令设置SCTP接收缓冲区参数以支持MME处理大规格消息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-BIGSCTPRXNUM]] · LST BIGSCTPRXNUM
- [[command/UNC/20.15.2/SET-BIGSCTPRXNUM]] · SET BIGSCTPRXNUM

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询大端模式SCTP接收缓冲区参数(LST-BIGSCTPRXNUM)_61676129.md`
- 原始手册：`evidence/UNC/20.15.2/设置大端模式SCTP接收缓冲区参数(SET-BIGSCTPRXNUM)_26238016.md`
