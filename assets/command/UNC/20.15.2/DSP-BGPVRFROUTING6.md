---
id: UNC@20.15.2@MMLCommand@DSP BGPVRFROUTING6
type: MMLCommand
name: DSP BGPVRFROUTING6（查询BGP VPN IPv6路由表）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BGPVRFROUTING6
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP VPN IPv6路由表
status: active
---

# DSP BGPVRFROUTING6（查询BGP VPN IPv6路由表）

## 功能

该命令用于显示BGP VPN实例IPv6路由表。此命令最多查询5000条路由。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：ipv6uni<br>配置原则：AFTYPE指定为ipv6vpn时，VRFNAME需指定为_public_。 |
| NETWORKPREFIX | BGP路由的前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询路由的前缀信息。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：配置该参数时，需要同时配置PERFIXMASK指定路由的前缀长度。 |
| PERFIXMASK | 前缀掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：配置NETWORKPREFIX参数时，需要配置本参数指定路由的前缀长度。 |
| PEERADDR | 对等体地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。取值为一个IPv4或IPv6地址。<br>默认值：无<br>配置原则：配置本参数时，需要同时配置ADVORRECV参数。 |
| SOURCEIFNAME | 多源对等体接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定多源对等体接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：配置本参数时，需要同时配置PEERADDR参数。 |
| ADVORRECV | 发布或接收路由 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询发布或接收路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- advertised：发布路由。<br>- received：接收路由。<br>默认值：无<br>配置原则：配置本参数时，需要同时配置PEERADDR参数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BGPVRFROUTING6]] · BGP VPN IPv6路由表（BGPVRFROUTING6）

## 使用实例

显示BGP VPN实例IPv6路由表：

```
DSP BGPVRFROUTING6:VRFNAME="_public_",AFTYPE=ipv6uni;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
   VPN实例名称  =  _public_
    地址族类型  =  IPv6uni
 BGP路由的前缀  =  2001:db8:1:1:1:1:1:1
      前缀掩码  =  128
    下一跳地址  =  2001:db8:2:2:2:2:2:2
    本地优先级  =  0
    协议首选值  =  0
    AS路径列表  =  NULL
      路由来源  =  IGP
    路由度量值  =  0
路由标志字符串  =   *>
  路由标识的值  =  NULL
    发送对等体  =  Not advertised to any peer yet
    路由时间戳  =  1133
      团体属性  =  NULL
  扩展团体属性  =  NULL
      源对等体  =  0.0.0.0
  路由出接口名  =  InLoopBack0
      源路由器  =  0.0.0.0
      簇ID列表  =  NULL
对等体路由器ID  =  0.0.0.0
    迭代下一跳  =  2001:db8:2:2:2:2:2:2
    聚合者AS号  =  0
    聚合者标识  =  0.0.0.0
      路由类型  =  8
  路由引入表ID  =  1
    路由优先级  =  0
路由未优选原因  =  NULL
      原子聚合  =  FALSE
   接收Path ID  =  NULL
    发布下一跳  =  2001:db8:2:2:2:2:2:1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BGP-VPN-IPv6路由表（DSP-BGPVRFROUTING6）_49802254.md`
