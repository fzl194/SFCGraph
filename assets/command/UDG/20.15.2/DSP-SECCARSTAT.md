---
id: UDG@20.15.2@MMLCommand@DSP SECCARSTAT
type: MMLCommand
name: DSP SECCARSTAT（显示安全CAR功能丢弃上送CPU报文的详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SECCARSTAT
command_category: 查询类
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

# DSP SECCARSTAT（显示安全CAR功能丢弃上送CPU报文的详细信息）

## 功能

该命令用来显示丢弃的报文的和上送CPU的报文的详细情况。当CPU利用率很高时，通过执行此命令，可以显示各个协议上送CPU的报文被丢弃的数目，从而关闭那些上送报文过多且无需启动的协议。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- Index：索引策略。<br>- UserFlow：用户自定义流策略。<br>- Protocol：协议策略。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Index”、“Tcpip”、“Protocol” 或 “UserFlow”时为必选参数。<br>参数含义：安全策略类型索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：<br>- 如果SECPOLICYTYPE选择WhiteList/BlackList/WhiteListV6，则本参数不选，否则必选。如果SECPOLICYTYPE选择Tcpip，则SECPOLICYTYPEID仅可以为3=tcpsyn、4=fragment，如果SECPOLICYTYPE选择Protocol，则SECPOLICYTYPEID仅可以选择2=bfd、3=bgp、10=icmp、14=ldp、19=ospf、32=arp、74=gre、43=arp-miss、27=ssh-server、26=ssh-client、46=bgpv6、51=icmpv6、73=na、72=ns、47=ospfv3、69=ra、71=rs、70=mld、5=dhcp、68=dhcpv6。<br>- 如果SECPOLICYTYPE选择Index，需要根据DSP SECCARINFO查看安全CAR系统ID并在[35，1658]区间，[125，158]区间除外。如果SECPOLICYTYPE选择UserFlow，本参数在[1，32]之间。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SECCARSTAT]] · 安全CAR功能丢弃上送CPU报文的详细信息（SECCARSTAT）

## 使用实例

显示ARP-MISS消息统计情况：

```
DSP SECCARSTAT:SECPOLICYTYPE=Protocol,SECPOLICYTYPEID=43;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
               RU名称  = VNODE_VNRS_VNFC_IPU_0064
         安全策略类型  =  协议策略
     安全策略类型编号  =  43
       应用层联动使能  =  TRUE
             协议使能  =  FALSE
   应用层联动默认动作  =  传给CPU
     通过包数（历史）  =  1139
         丢弃报文总数  =  0
 承诺信息速率（kbps）  =  256
承诺突发尺寸（bytes）  =  100000
               优先级  =  低
   安全最小包补偿长度  =  128
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SECCARSTAT.md`
