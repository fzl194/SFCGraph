---
id: UNC@20.15.2@MMLCommand@RMV DAMPROUTE
type: MMLCommand
name: RMV DAMPROUTE（删除振荡抑制路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DAMPROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 振荡抑制路由
status: active
---

# RMV DAMPROUTE（删除振荡抑制路由）

## 功能

该命令用于删除路由振荡抑制的配置参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| PEERTYPE | 对等体类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体类型是EBGP还是IBGP。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ebgp：EBGP。<br>- ibgp：IBGP。<br>默认值：ebgp |

## 操作的配置对象

- [振荡抑制路由（DAMPROUTE）](configobject/UNC/20.15.2/DAMPROUTE.md)

## 使用实例

删除公网下IPv4单播地址族的振荡抑制作用：

```
RMV DAMPROUTE:VRFNAME="_public_",AFTYPE=ipv4uni;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除振荡抑制路由（RMV-DAMPROUTE）_50120806.md`
