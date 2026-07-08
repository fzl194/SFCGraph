---
id: UDG@20.15.2@MMLCommand@RMV BGPPEERGROUP
type: MMLCommand
name: RMV BGPPEERGROUP（删除BGP对等体组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: BGPPEERGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体组
status: active
---

# RMV BGPPEERGROUP（删除BGP对等体组）

## 功能

该命令用于删除IPv4或IPv6地址族下的对等体组。

## 注意事项

- 该命令执行后立即生效。
- 删除对等体组会删除该对等体组下的所有对等体。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| GROUPNAME | 对等体组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对等体组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| AFTYPE | 对等体组地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该对等体组支持的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- public：公网地址族。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>- noaf：不指定地址族。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BGPPEERGROUP]] · BGP对等体组（BGPPEERGROUP）

## 使用实例

- 在名称为“vrf1”的BGP VPN实例下删除IPv4地址族下指定对等体组asdf：
  ```
  RMV BGPPEERGROUP:VRFNAME="vrf1",GROUPNAME="asdf",AFTYPE=ipv4uni;
  ```
- 在名称为“vrf1”的BGP VPN实例下删除IPv6地址族下指定对等体组asdf：
  ```
  RMV BGPPEERGROUP:VRFNAME="vrf1",GROUPNAME="asdf",AFTYPE=ipv6uni;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-BGPPEERGROUP.md`
