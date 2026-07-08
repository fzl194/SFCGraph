---
id: UNC@20.15.2@MMLCommand@RMV BGPPEER
type: MMLCommand
name: RMV BGPPEER（删除BGP对等体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BGPPEER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体
status: active
---

# RMV BGPPEER（删除BGP对等体）

## 功能

该命令用于删除IPv4或IPv6地址类型的对等体及其相关参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| ADDRESSTYPE | 地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- noaf：不指定地址族。<br>- ipv4：IPv4。<br>- ipv6：IPv6。<br>默认值：无 |
| PEERADDR | IPv4对等体地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“noaf” 或 “ipv4”时为必选参数。<br>参数含义：该参数用于指定连接对等体的IPv4接口地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PEERADDRV6 | IPv6对等体地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为必选参数。<br>参数含义：该参数用于指定连接对等体的IPv6接口地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPPEER]] · BGP对等体（BGPPEER）

## 使用实例

- 在名称为“vrf1”的BGP VPN实例下删除指定对等体10.2.2.2：
  ```
  RMV BGPPEER:VRFNAME="vrf1",ADDRESSTYPE=ipv4,PEERADDR="10.2.2.2";
  ```
- 在名称为“vrf1”的BGP VPN实例下删除指定对等体2001:db8:1:1:1:1:1:1：
  ```
  RMV BGPPEER:VRFNAME="vrf1",ADDRESSTYPE=ipv6,PEERADDRV6="2001:db8:1:1:1:1:1:1";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BGPPEER.md`
