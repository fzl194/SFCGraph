---
id: UDG@20.15.2@MMLCommand@ADD BGPPEERGROUPAFPRE
type: MMLCommand
name: ADD BGPPEERGROUPAFPRE（增加BGP对等体组条件路由匹配前缀）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: BGPPEERGROUPAFPRE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体组条件路由匹配前缀
status: active
---

# ADD BGPPEERGROUPAFPRE（增加BGP对等体组条件路由匹配前缀）

## 功能

该命令用于添加BGP对等体组条件路由匹配前缀。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 该命令执行的前提需要BGPPEERGROUPAF中参数DEFAULTRTADVENABLE为TRUE，DEFAULTRTMATCHMODE为match all或match any。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>默认值：无 |
| GROUPNAME | 对等体组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定相应的对等体组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST BGPPEERGROUP命令查看可用对等体组名。 |
| DEFAULTRTADDRESS | 指定一个缺省路由条件匹配的前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定满足所有条件路由时发送的缺省地址前缀。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DEFAULTRTMASK | 指定一个缺省路由条件匹配的掩码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定缺省前缀的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：和DEFAULTRTADDRESS配合使用。 |

## 操作的配置对象

- [BGP对等体组条件路由匹配前缀（BGPPEERGROUPAFPRE）](configobject/UDG/20.15.2/BGPPEERGROUPAFPRE.md)

## 使用实例

为对等体组添加条件路由匹配前缀：

```
SET BGP:ASNUM="100",BGPENABLE=TRUE;
ADD BGPPEERGROUP:VRFNAME="_public_",AFTYPE=public,GROUPNAME="asdf";
MOD BGPPEERGROUPAF:VRFNAME="_public_",AFTYPE=ipv4uni,GROUPNAME="asdf",DEFAULTRTADVENABLE=TRUE,DEFAULTRTMATCHMODE=matchall;
ADD BGPPEERGROUPAFPRE:VRFNAME="_public_",AFTYPE=ipv4uni,GROUPNAME="asdf",DEFAULTRTADDRESS="10.11.11.11",DEFAULTRTMASK=32;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加BGP对等体组条件路由匹配前缀（ADD-BGPPEERGROUPAFPRE）_49961050.md`
