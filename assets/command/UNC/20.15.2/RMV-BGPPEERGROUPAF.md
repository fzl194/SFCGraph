---
id: UNC@20.15.2@MMLCommand@RMV BGPPEERGROUPAF
type: MMLCommand
name: RMV BGPPEERGROUPAF（删除BGP对等体组地址族）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BGPPEERGROUPAF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体组地址族
status: active
---

# RMV BGPPEERGROUPAF（删除BGP对等体组地址族）

## 功能

该命令用于删除BGP对等体组地址族。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于给定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| GROUPNAME | 对等体组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定相应的对等体组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST BGPPEERGROUP命令查看可用对等体组名。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPPEERGROUPAF]] · BGP对等体组地址族（BGPPEERGROUPAF）

## 使用实例

- 删除相应对等体组的IPv4地址族：
  ```
  RMV BGPPEERGROUPAF:VRFNAME="_public_",GROUPNAME="asdf",AFTYPE=ipv4uni;
  ```
- 删除相应对等体组的IPv6地址族：
  ```
  RMV BGPPEERGROUPAF:VRFNAME="_public_",GROUPNAME="asdf",AFTYPE=ipv6uni;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BGPPEERGROUPAF.md`
