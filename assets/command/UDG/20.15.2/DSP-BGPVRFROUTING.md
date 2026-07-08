---
id: UDG@20.15.2@MMLCommand@DSP BGPVRFROUTING
type: MMLCommand
name: DSP BGPVRFROUTING（查询BGP VPN路由表）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BGPVRFROUTING
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP VPN路由表命令
status: active
---

# DSP BGPVRFROUTING（查询BGP VPN路由表）

## 功能

该命令用于显示BGP VPN实例IPv4路由表。此命令最多查询5000条路由。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：VRFNAME指定为_public_时，查询公网路由。VRFNAME不指定时，查询所有私网VPN路由。 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>默认值：ipv4uni<br>配置原则：AFTYPE指定为ipv4vpn时，VRFNAME需指定为_public_。 |
| NETWORKPREFIX | BGP路由的前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询路由的前缀信息。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：配置该参数时，需要同时配置PERFIXMASK指定路由的掩码长度。 |
| PERFIXMASK | 前缀掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询路由的前缀掩码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：配置NETWORKPREFIX参数时，需要配置本参数指定路由的掩码长度。 |
| PEERADDR | 对等体地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：配置本参数时，需要同时配置ADVORRECV参数。 |
| SOURCEIFNAME | 多源对等体接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定多源对等体接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：配置本参数时，需要同时配置PEERADDR参数。 |
| ADVORRECV | 发布或接收路由 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询发布或接收路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- advertised：发布路由。<br>- received：接收路由。<br>默认值：无<br>配置原则：配置本参数时，需要同时配置PEERADDR参数。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BGPVRFROUTING]] · BGP VPN路由表（BGPVRFROUTING）

## 使用实例

查询BGP VPN实例IPv4路由表：

```
DSP BGPVRFROUTING:VRFNAME="_public_",AFTYPE=ipv4uni;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
   VPN实例名称  =  _public_
    地址族类型  =  IPv4uni
 BGP路由的前缀  =  10.10.222.10
      前缀掩码  =  32
    下一跳地址  =  0.0.0.0
    本地优先级  =  0
    协议首选值  =  0
    AS路径列表  =  NULL
      路由来源  =  IGP
    路由度量值  =  0
路由标志字符串  =  *>
  路由标识的值  =  0:0
    发送对等体  =  10.2.2.2
    路由时间戳  =  7
      团体属性  =  <12345:65535>
  扩展团体属性  =  NULL
      源对等体  =  0.0.0.0
  路由出接口名  =  NULL0
      源路由器  =  0.0.0.0
      簇ID列表  =  NULL
对等体路由器ID  =  0.0.0.0
    迭代下一跳  =  0.0.0.0
    聚合者AS号  =  0
    聚合者标识  =  0.0.0.0
      路由类型  =  4
  路由引入表ID  =  0
    路由优先级  =  60
路由未优选原因  =  NULL
      原子聚合  =  FALSE
    接收路径ID  =  NULL
    发布下一跳  =  10.2.2.1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-BGPVRFROUTING.md`
