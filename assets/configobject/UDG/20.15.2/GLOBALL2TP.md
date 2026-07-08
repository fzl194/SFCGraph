---
id: UDG@20.15.2@ConfigObject@GLOBALL2TP
type: ConfigObject
name: GLOBALL2TP（L2TP配置）
nf: UDG
version: 20.15.2
object_name: GLOBALL2TP
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# GLOBALL2TP（L2TP配置）

## 说明

**适用NF：PGW-U、UPF**

该命令用于设置L2TP的缺省属性，包括：L2TP隧道本端名称、HELLO报文发送开关、HELLO报文重发间隔和报文重发次数。创建L2TP隧道有两种方式：一是根据鉴权服务器返回的L2TP属性创建；二是根据本地配置的L2TP组创建。

当用户接入系统时，系统向鉴权服务器发起对用户的鉴权。当鉴权服务器上为用户设置了L2TP的相关属性，则会返回给系统，系统根据鉴权服务器（AAA）返回的属性创建L2TP隧道。AAA返回的L2TP属性中不包含Client-Auth-ID（即LAC名称）属性场景，系统将使用本命令设置的缺省本端名称发起隧道连接；隧道创建后将使用本命令设置的缺省HELLO报文重发间隔发送HELLO报文以检测隧道的连通性。

当鉴权服务器上没有为用户设置L2TP的相关属性，但用户所在APN已使能L2TP功能，并且用户名中携带的域名匹配L2TP组中配置的域名时，将根据由ADD L2TPGROUP命令进行本地配置的L2TP组创建L2TP隧道。L2TP组中没有配置本端名称场景，系统将使用本命令设置的缺省本端名称发起隧道连接。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-GLOBALL2TP]] · LST GLOBALL2TP
- [[command/UDG/20.15.2/SET-GLOBALL2TP]] · SET GLOBALL2TP

## 证据

- 原始手册：`evidence/UDG/20.15.2/GLOBALL2TP.md`
- 原始手册：`evidence/UDG/20.15.2/GLOBALL2TP.md`
