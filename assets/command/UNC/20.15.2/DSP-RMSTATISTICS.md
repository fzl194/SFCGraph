---
id: UNC@20.15.2@MMLCommand@DSP RMSTATISTICS
type: MMLCommand
name: DSP RMSTATISTICS（显示IP路由统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RMSTATISTICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- IP路由表统计
status: active
---

# DSP RMSTATISTICS（显示IP路由统计）

## 功能

该命令用于显示IP路由表的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示路由所属VPN实例的地址族信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：公网需要输入_public_，默认查询所有VPN，不支持空格。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RMSTATISTICS]] · IP路由统计（RMSTATISTICS）

## 使用实例

显示IP路由表的统计信息：

```
DSP RMSTATISTICS: ADDRESSFAMILY=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
VPN实例名称          路由协议名字    路由总数    活跃路由数    添加路由数    删除路由数    释放路由数

_public_             直连路由        4           4             4             0             0
_public_             静态路由        1           1             1             0             0
_public_             OSPF路由        0           0             0             0             0
_public_             BGP路由         0           0             0             0             0
_public_             UNR             0           0             0             0             0
_public_             无线路由        0           0             0             0             0
_public_             汇总路由        5           5             5             0             0
__mpp_vpn_inner__    直连路由        4           4             4             0             0
__mpp_vpn_inner__    静态路由        0           0             0             0             0
__mpp_vpn_inner__    OSPF路由        0           0             0             0             0
__mpp_vpn_inner__    BGP路由         0           0             0             0             0
__mpp_vpn_inner__    UNR             0           0             0             0             0
__mpp_vpn_inner__    无线路由        0           0             0             0             0
__mpp_vpn_inner__    汇总路由        4           4             4             0             0
(结果个数 = 12)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RMSTATISTICS.md`
