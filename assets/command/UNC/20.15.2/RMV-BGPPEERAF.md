---
id: UNC@20.15.2@MMLCommand@RMV BGPPEERAF
type: MMLCommand
name: RMV BGPPEERAF（删除BGP对等体地址族）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BGPPEERAF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体地址族
status: active
---

# RMV BGPPEERAF（删除BGP对等体地址族）

## 功能

该命令用于删除BGP IPv4或IPv6对等体地址族。

![](删除BGP对等体地址族（RMV BGPPEERAF）_00441309.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该操作会导致对等体重新连接。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| ADDRESSTYPE | 地址类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4。<br>- ipv6：IPv6。<br>默认值：无 |
| REMOTEADDRESS | IPv4对等体地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn” 或 “ipv6vpn”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为必选参数。<br>参数含义：该参数用于指定连接对等体的IPv4接口地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| REMOTEADDRESSV6 | IPv6对等体地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为必选参数。<br>参数含义：该参数用于指定连接对等体的IPv6接口地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [BGP对等体地址族（BGPPEERAF）](configobject/UNC/20.15.2/BGPPEERAF.md)

## 使用实例

- 删除BGP IPv4对等体地址族：
  ```
  RMV BGPPEERAF:VRFNAME="_public_",AFTYPE=ipv4uni,REMOTEADDRESS="10.2.2.2";
  ```
- 删除BGP IPv6对等体地址族：
  ```
  RMV BGPPEERAF:VRFNAME="_public_",AFTYPE=ipv6uni,ADDRESSTYPE=ipv6,REMOTEADDRESSV6="2001:db8:1:1:1:1:1:1";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BGP对等体地址族（RMV-BGPPEERAF）_00441309.md`
