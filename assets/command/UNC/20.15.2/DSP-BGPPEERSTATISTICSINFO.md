---
id: UNC@20.15.2@MMLCommand@DSP BGPPEERSTATISTICSINFO
type: MMLCommand
name: DSP BGPPEERSTATISTICSINFO（查询BGP对等体统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BGPPEERSTATISTICSINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP对等体路由统计信息
status: active
---

# DSP BGPPEERSTATISTICSINFO（查询BGP对等体统计信息）

## 功能

该命令用于显示BGP IPv4对等体统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：ipv4uni |
| SOURCEIFNAME | 多源接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用来给定多源对等体的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：仅支持Ethernet及其子接口类型，不区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BGPPEERSTATISTICSINFO]] · BGP对等体统计信息（BGPPEERSTATISTICSINFO）

## 使用实例

显示BGP IPv4对等体统计信息：

```
DSP BGPPEERSTATISTICSINFO:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
VPN实例名称    地址族类型            对等体地址     多源接口名称      可达路由数量    不可达路由数量    过策略前路由数量    过策略后路由数量  最优路由数量   策略拒绝路由数量   AS环路路由数量    AS联盟环路路由数量  簇环路路由数量  无效源路由器ID路由数量
_public_       IPv4uni               10.2.2.2       NULL              0               0                 0                   0                 0              0                  0                 0                   0               0
vpna           IPv4uni               10.2.2.2       NULL              0               0                 0                   0                 0              0                  0                 0                   0               0
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BGP对等体统计信息（DSP-BGPPEERSTATISTICSINFO）_50280882.md`
