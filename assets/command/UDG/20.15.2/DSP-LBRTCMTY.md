---
id: UDG@20.15.2@MMLCommand@DSP LBRTCMTY
type: MMLCommand
name: DSP LBRTCMTY（查询路由团体属性信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LBRTCMTY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 路由管理
- 路由团体属性信息
status: active
---

# DSP LBRTCMTY（查询路由团体属性信息）

## 功能

查询路由团体属性信息。团体属性是一组有相同特征的目的地址的集合。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN名称。VPN名称可以通过VNRS的<br>**[LST IPRUREACH](../../../../VNRS功能管理/IP服务/路由管理/无线路由管理/RU到网关的可达性/查询RU到网关的可达性检测配置（LST IPRUREACH）_00440741.md)**<br>查询VPN Name字段获取<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0~31。<br>默认值：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址的类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPv4) ”<br>- “IPV6(IPv6) ”<br>默认值：无 |
| PEERADDRIPV4 | 对端设备IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端设备的IPv4地址。对端设备的IPv4地址可以通过VNRS的<br>**[LST IPRUREACH](../../../../VNRS功能管理/IP服务/路由管理/无线路由管理/RU到网关的可达性/查询RU到网关的可达性检测配置（LST IPRUREACH）_00440741.md)**<br>查询Destination Address字段获取。<br>前提条件：该参数在“IP类型”参数配置为“IPV4”后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| PEERADDRIPV6 | 对端设备IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端设备的IPv6地址。对端设备的IPv6地址可以通过VNRS的<br>**[LST IPRUREACH](../../../../VNRS功能管理/IP服务/路由管理/无线路由管理/RU到网关的可达性/查询RU到网关的可达性检测配置（LST IPRUREACH）_00440741.md)**<br>查询Destination Address字段获取。<br>前提条件：该参数在“IP类型”参数配置为“IPV6”后生效。<br>数据来源：全网规划。<br>取值围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LBRTCMTY]] · 路由团体属性信息（LBRTCMTY）

## 使用实例

查询路由团体属性的命令如下：

```
%%DSP LBRTCMTY: VPNNAME="vrf1", IPTYPE=IPV4, PEERADDRIPV4="192.168.1.1";%%
RETCODE = 0  操作成功。

操作结果如下：
-------------------------
VPN名称 = vrf1
IP类型 = IPV4
对端设备IPv4地址 = 192.168.1.1
团体属性 = 20
路由Tag = 64
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LBRTCMTY.md`
