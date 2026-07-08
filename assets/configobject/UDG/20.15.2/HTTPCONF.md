---
id: UDG@20.15.2@ConfigObject@HTTPCONF
type: ConfigObject
name: HTTPCONF（HTTP属性）
nf: UDG
version: 20.15.2
object_name: HTTPCONF
object_kind: global_setting
status: active
---

# HTTPCONF（HTTP属性）

## 说明

![](设置HTTP属性（SET HTTPCONF）_83972196.assets/notice_3.0-zh-cn.png)

该命令中SIGNALROUTING参数用于设置信令路由开关，信令路由功能下HTTP性能降低，可能影响正常业务，不建议开启使用。 该命令中MAXCLIENTSTREAM参数用于设置最大并发流上限，值配置过大或过小均会造成HTTP性能降低，可能影响正常业务，建议直接使用默认值。 该命令中HttpLogLevel参数用于设置http-server日志级别，如果配置成DEBUG或INFO或WARN，则会造成性能下降，可能影响正常业务，建议直接使用默认值。 该命令中TcpLogLevel参数用于设置tcp-process日志级别，如果配置成DEBUG或INFO或WARN或ERROR，则会造成性能下降，可能影响正常业务，建议直接使用默认值。

该命令用于设置HTTP协议层的属性，该属性设置后整系统生效。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SIGNALROUTING | HTTPLOGLEVEL | TCPLOGLEVEL | DETECTINTERVAL | LOADREPINTERVAL | LINKAGINGTIME | CLIENTRCVRSPTMT | SERVERRCVBDTMT | SERVERSNDRSPTMT | PINGSWITCH | PINGINTVAL | PINGPROBES | KEEPALIVESW | KEEPALIVETIME | KEEPALIVEINTVL | KEEPALIVEPROBES | MAXBODYSIZE | MAXJSONLEAFNUM | TCPSEDELTIME | MAXCLIENTSTREAM | INITLINKINTVL | IPDETECTSW | PERFSTATSW | LINKSETRECOVERTIME | CONFCHECKSW | LINKCHECKSW | COMPRESSTH | REQCBFCSW | SYNREXINTERVAL | SYNREXTIMES | ESTABREXTIMES | BACKOFFINTERVAL | HTTPVERSIONSW | HTTPGOAWAYSW |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | FALSE | ERROR | FATAL | 720 | 10 | 10 | 5 | 3 | 5 | TRUE | 60 | 3 | ON | 1800 | 5 | 5 | 2 | 16000 | 3 | 0 | 200 | TRUE | TRUE | 30 | TRUE | TRUE | 60 | TRUE | 500 | 0 | 12 | 100 | FALSE | FALSE |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-HTTPCONF]] · LST HTTPCONF
- [[command/UDG/20.15.2/SET-HTTPCONF]] · SET HTTPCONF

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP属性（LST-HTTPCONF）_28971839.md`
- 原始手册：`evidence/UDG/20.15.2/设置HTTP属性（SET-HTTPCONF）_83972196.md`
