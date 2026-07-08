---
id: UNC@20.15.2@MMLCommand@LST UPFRDSCLIENTIP
type: MMLCommand
name: LST UPFRDSCLIENTIP（查询中转UPF与Radius客户端的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFRDSCLIENTIP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- UPF中转Radius客户端IP
status: active
---

# LST UPFRDSCLIENTIP（查询中转UPF与Radius客户端的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询中转UPF与Radius客户端的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTYPE | 客户端类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RADIUS客户端类型。<br>数据来源：本端规划<br>取值范围：<br>- “AUTHENTICATION（鉴权客户端）”：表示鉴权客户端。<br>- “ACCOUNTING（计费客户端）”：表示计费客户端。<br>- “ACCT_AND_AUTH（计费和鉴权客户端）”：表示计费和鉴权客户端。<br>默认值：无<br>配置原则：无 |
| IPVERSION | 客户端IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RADIUS客户端IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”：IPv4<br>- “IPV6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| CLIENTIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定RADIUS客户端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CLIENTIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定RADIUS客户端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFRDSCLIENTIP]] · 中转UPF与Radius客户端的绑定关系（UPFRDSCLIENTIP）

## 使用实例

如果想要查询UPF中转Radius客户端IP配置信息：

```
LST UPFRDSCLIENTIP:;
RETCODE = 0  操作成功

结果如下
--------
  客户端类型  =  鉴权服务器
客户端IP版本  =  IPv4
  UP实例标识  =  up1
     VPN实例  =  NULL
客户端IP地址  =  192.168.10.1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPFRDSCLIENTIP.md`
