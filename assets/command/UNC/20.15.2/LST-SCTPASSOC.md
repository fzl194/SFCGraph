---
id: UNC@20.15.2@MMLCommand@LST SCTPASSOC
type: MMLCommand
name: LST SCTPASSOC（查询SCTP耦联测量对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPASSOC
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- SCTP管理
- SCTP测量对象
status: active
---

# LST SCTPASSOC（查询SCTP耦联测量对象）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询SCTP耦联测量对象。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJECTID | SCTP偶联测量对象实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP耦联测量对象实例标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～200。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP耦联测量对象的IP地址类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALADDRIPV4 | 本端主IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：该参数用于指定SCTP耦联本端主IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERADDRIPV4 | 对端主IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：该参数用于指定SCTP耦联对端主IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALADDRIPV6 | 本端主IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：该参数用于指定SCTP耦联本端主IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERADDRIPV6 | 对端主IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：该参数用于指定SCTP耦联对端主IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPASSOC]] · SCTP耦联信息（SCTPASSOC）

## 使用实例

查询SCTP耦联测量对象：

```
LST SCTPASSOC: OBJECTID=1;
```

```

RETCODE = 0  操作成功。

SCTP耦联测量对象
----------------
SCTP偶联测量对象实例标识  =  1
            本端主IP地址  =  192.168.1.23
            本端子IP地址  =  192.168.1.24
            对端主IP地址  =  192.168.2.23
            对端子IP地址  =  192.168.2.24
              本端端口号  =  0
              对端端口号  =  3868
                 VPN实例  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCTPASSOC.md`
