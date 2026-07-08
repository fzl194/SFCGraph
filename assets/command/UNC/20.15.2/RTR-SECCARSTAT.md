---
id: UNC@20.15.2@MMLCommand@RTR SECCARSTAT
type: MMLCommand
name: RTR SECCARSTAT（清除承诺访问速率具体信息）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: SECCARSTAT
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- CAR统计
status: active
---

# RTR SECCARSTAT（清除承诺访问速率具体信息）

## 功能

该命令用来清除承诺访问速率。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- Index：索引策略。<br>- UserFlow：用户自定义流策略。<br>- Protocol：协议策略。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Index”、“Tcpip”、“Protocol” 或 “UserFlow”时为必选参数。<br>参数含义：安全策略类型索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：<br>- 如果SECPOLICYTYPE选择WhiteList/BlackList/WhiteListV6，则本参数不选，否则必选。如果SECPOLICYTYPE选择Tcpip，则SECPOLICYTYPEID仅可以为3=tcpsyn、4=fragment，如果SECPOLICYTYPE选择Protocol，则SECPOLICYTYPEID仅可以选择2=bfd、3=bgp、10=icmp、14=ldp、19=ospf、32=arp、74=gre、43=arp-miss、27=ssh-server、26=ssh-client、46=bgpv6、51=icmpv6、73=na、72=ns、47=ospfv3、69=ra、71=rs、70=mld、5=dhcp、68=dhcpv6。<br>- 如果SECPOLICYTYPE选择Index，需要根据DSP SECCARINFO查看安全CAR系统ID并在[35，1658]区间，[125，158]区间除外。如果SECPOLICYTYPE选择UserFlow，本参数在[1，32]之间。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECCARSTAT]] · 安全CAR功能丢弃上送CPU报文的详细信息（SECCARSTAT）

## 使用实例

清除承诺访问速率：

```
RTR SECCARSTAT:SECPOLICYTYPE=Protocol,SECPOLICYTYPEID=74;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除承诺访问速率具体信息（RTR-SECCARSTAT）_50280698.md`
