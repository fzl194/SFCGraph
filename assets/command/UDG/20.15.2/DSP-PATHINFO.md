---
id: UDG@20.15.2@MMLCommand@DSP PATHINFO
type: MMLCommand
name: DSP PATHINFO（查询路径信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PATHINFO
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP协议参数管理
- 查询路径信息
status: active
---

# DSP PATHINFO（查询路径信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询路径信息。

## 注意事项

- 当参数中PeerIPv4或PeerIPv6不指定时，执行该命令将不会获取该路径上的上下文数目。
- 由于业务规格限制，当前不支持一次性全量查询，单次查询上限为一万条数据，需要执行多次命令才能完成所有路径资源信息查询，路径信息依次顺延。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路径IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定路径的对端ipv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定对端ipv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路径查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOL：指定路径查询类型为GTP路径。<br>- PROXY：指定路径查询类型为Proxy路径。<br>- HISTORY：查询路径历史状态。<br>默认值：无<br>配置原则：无 |
| PROTOCOLTYPE | 协议版本 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于指定路径的协议版本信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GTPV1：指定GTP协议版本为V1版本。<br>- PFCP：指定PFCP协议版本。<br>- TM：指定TM协议版本。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [路径信息（PATHINFO）](configobject/UDG/20.15.2/PATHINFO.md)

## 使用实例

在需要查看路径信息，比如本端地址，对端网元地址，协议版本，VPN实例名与路径上的用户数等信息时，使用此命令：

```
DSP PATHINFO:;
```

```

RETCODE = 0  操作成功。

 结果如下：
 ----------------------------
路径类型      路径状态  IP版本类型  本端IPv4地址  对端IPv4地址  本端IPv6地址  对端IPv6地址  协议版本  VPN实例名  信令路径r  数据路径  
SIG PATH ONLY  UP          IPV4             127.16.0.0         192.168.0.0        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.1         192.168.0.1        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.2         192.168.0.2        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.3         192.168.0.3        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.4         192.168.0.4        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.5         192.168.0.5        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.6         192.168.0.6        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.7         192.168.0.7        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.8         192.168.0.8        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.0.9         192.168.0.9        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.1.0         192.168.1.1        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.1.1         192.168.1.2        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.1.2         192.168.1.3        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.1.3         192.168.1.4        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.1.4         192.168.1.5        ::                  ::                 PFCP           NULL               0                   0                    
SIG PATH ONLY  UP          IPV4             127.16.1.5         192.168.1.6        ::                  ::                 PFCP           NULL               0                   0                    
(结果个数 = 16)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询路径信息（DSP-PATHINFO）_82837223.md`
