---
id: UNC@20.15.2@MMLCommand@MOD SRVNODERAT
type: MMLCommand
name: MOD SRVNODERAT（修改SGSN/SGW IP与RAT类型间的映射关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SRVNODERAT
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取RAT管理
- IP地址映射RAT
status: active
---

# MOD SRVNODERAT（修改SGSN/SGW IP与RAT类型间的映射关系）

## 功能

**适用NF：GGSN**

该命令用来修改SGSN的IP与RAT类型间的映射关系表。当运营商需要改变一SGSN的IP地址段对应的RAT类型时，使用此命令。修改RAT类型用于从虚拟APN映射到真实APN、匹配UserProfile进行业务、计费控制。

## 注意事项

- 该命令执行后立即生效。

- 修改配置后，可能导致用户的RAT类型发生变化，会影响用户的计费和业务控制。
- 当系统中存在的SGSN的IP地址段与命令输入的IP地址段相同时，命令生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置IP地址版本类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4。<br>- “IPV6（IPV6）”：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SRVNODESTARTV4 | Service Node的起始IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IP地址段的起始IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODEENDV4 | Service Node的结束IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IP地址段的结束IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODESTARTV6 | Service Node的起始IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IP地址段的起始IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SRVNODEENDV6 | Service Node的结束IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IP地址段的结束IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| RATTYPE | RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAT类型。<br>数据来源：全网规划<br>取值范围：<br>- “UTRAN（UTRAN）”：表示无线接入类型为UTRAN。<br>- “GERAN（GERAN）”：表示无线接入类型为GERAN。<br>- “WLAN（WLAN）”：表示无线接入类型为WLAN。<br>- “GAN（GAN）”：表示无线接入类型为GAN。<br>- “EUTRAN（EUTRAN）”：表示无线接入类型为EUTRAN。<br>- “NULL（NULL）”：NULL<br>- “EUTRAN_NB_IOT（EUTRAN_NB_IOT）”：表示无线接入类型为EUTRAN-NB-IoT。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVNODERAT]] · SGSN/SGW IP与RAT类型间的映射关系（SRVNODERAT）

## 使用实例

当运营商需要修改映射表中一SGSN IP地址段对应的RAT类型时，可按如下配置：

```
MOD SRVNODERAT: IPVERSION=IPV4, SRVNODESTARTV4="10.1.1.1", SRVNODEENDV4="10.2.2.2", RATTYPE=WLAN;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SRVNODERAT.md`
