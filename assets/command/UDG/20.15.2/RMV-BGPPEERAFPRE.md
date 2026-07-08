---
id: UDG@20.15.2@MMLCommand@RMV BGPPEERAFPRE
type: MMLCommand
name: RMV BGPPEERAFPRE（删除BGP对等体条件路由匹配前缀）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: BGPPEERAFPRE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体条件路由匹配前缀
status: active
---

# RMV BGPPEERAFPRE（删除BGP对等体条件路由匹配前缀）

## 功能

该命令用于删除条件路由的匹配前缀。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于给定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>默认值：无 |
| REMOTEADDRESS | 对等体地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由器对等体的对端地址或地址段。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DEFAULTRTADDRESS | 指定一个缺省路由条件匹配的前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定满足所有条件路由时发送的缺省地址前缀。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DEFAULTRTMASK | 指定一个缺省路由条件匹配的掩码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定缺省前缀的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BGPPEERAFPRE]] · BGP对等体条件路由匹配前缀（BGPPEERAFPRE）

## 使用实例

删除条件路由的匹配前缀：

```
RMV BGPPEERAFPRE:VRFNAME="_public_",AFTYPE=ipv4uni,REMOTEADDRESS="10.2.2.2",DEFAULTRTADDRESS="10.11.11.11",DEFAULTRTMASK=32;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-BGPPEERAFPRE.md`
