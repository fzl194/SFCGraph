---
id: UNC@20.15.2@MMLCommand@DSP BGPVRF
type: MMLCommand
name: DSP BGPVRF（查询BGP VPN简要信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BGPVRF
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP VPN简要信息
status: active
---

# DSP BGPVRF（查询BGP VPN简要信息）

## 功能

该命令用于查询BGP VPN简要信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | BGP地址族类型 | 可选必选说明：可选参数<br>参数含义：BGP地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPVRF]] · BGP VPN实例（BGPVRF）

## 使用实例

查询BGP VPN简要信息：

```
DSP BGPVRF:AFTYPE=ipv4uni;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
BGP VPN简要信息  =
VPN-Instance(IPv4-family):
VPN-Instance Name   _public_
Peer Num   1
Route Num   5

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BGPVRF.md`
