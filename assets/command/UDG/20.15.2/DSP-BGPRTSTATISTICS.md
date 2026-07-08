---
id: UDG@20.15.2@MMLCommand@DSP BGPRTSTATISTICS
type: MMLCommand
name: DSP BGPRTSTATISTICS（查询BGP路由统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BGPRTSTATISTICS
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP路由统计信息
status: active
---

# DSP BGPRTSTATISTICS（查询BGP路由统计信息）

## 功能

该命令用于查询BGP路由统计信息，可用于查询BGP路由总数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | BGP地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：ipv4uni |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BGPRTSTATISTICS]] · BGP路由统计信息（BGPRTSTATISTICS）

## 使用实例

查询BGP路由统计信息：

```
DSP BGPRTSTATISTICS:VRFNAME="vrf1";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
BGP路由统计信息  =
VPN-Instance           : vrf1
Router ID              : 10.1.1.1
Total Number of Routes : 4
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-BGPRTSTATISTICS.md`
