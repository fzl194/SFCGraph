---
id: UDG@20.15.2@MMLCommand@DSP BGPERRORDISCARD
type: MMLCommand
name: DSP BGPERRORDISCARD（查询BGP的错误信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BGPERRORDISCARD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP的错误信息
status: active
---

# DSP BGPERRORDISCARD（查询BGP的错误信息）

## 功能

该命令用于查询BGP的错误信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| REMOTEADDRESS | 对端地址 | 可选必选说明：可选参数<br>参数含义：对端地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SOURCEIFNAME | 多源接口名称 | 可选必选说明：可选参数<br>参数含义：多源对等体的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：仅支持Ethernet及其子接口类型，不区分大小写。 |

## 操作的配置对象

- [BGP的错误信息（BGPERRORDISCARD）](configobject/UDG/20.15.2/BGPERRORDISCARD.md)

## 使用实例

查询BGP的错误信息：

```
DSP BGPERRORDISCARD:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
BGP的错误信息  =
BGP Discard Info Counts:
Routes received with cluster ID loop : 0
Routes received with as path count over limit : 0
Routes advertised with as path count over limit : 0
Routes received with As loop : 0
Routes received with Zero RD(0:0) : 0
Routes received with no prefix : 0
Routes received with error path-attribute : 0
Routes received with originator ID loop : 0

BGP Discard info:(IPv4 Unicast)
Routes received with cluster ID loop : 0
Routes received with as path count over limit : 0
Routes advertised with as path count over limit : 0
Routes received with As loop : 0
Routes received with Zero RD(0:0) : 0
Routes received with error path-attribute : 0
Routes received with originator ID loop : 0

No discard record.

BGP Discard info:(IPv4 VPNv4)
Routes received with cluster ID loop : 0
Routes received with as path count over limit : 0
Routes advertised with as path count over limit : 0
Routes received with As loop : 0
Routes received with Zero RD(0:0) : 0
Routes received with error path-attribute : 0
Routes received with originator ID loop : 0

No discard record.

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BGP的错误信息（DSP-BGPERRORDISCARD）_50281314.md`
