---
id: UNC@20.15.2@MMLCommand@MOD L3VPNINST
type: MMLCommand
name: MOD L3VPNINST（修改L3VPN实例）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: L3VPNINST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- L3VPN管理
- L3VPN实例
status: active
---

# MOD L3VPNINST（修改L3VPN实例）

## 功能

该命令用于修改L3VPN实例参数。

## 注意事项

- 该命令执行后立即生效。
- 需要修改参数的L3VPN实例必须已配置。
- 不能修改VPN实例__mpp_vpn_inner__、__mpp_vpn_inner_server__的配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| VRFDESCRIPTION | VPN实例描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述L3VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～242。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 可以带空格的描述性语句。<br>- VRFDESCRIPTION不能在公网下配置。 |
| ROUTERID | 路由器ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定Router ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。取值为一个IPv4地址。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- ROUTERID只能在公网下配置。修改该参数后请重置相关协议以更新Router ID。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/L3VPNINST]] · L3VPN实例（L3VPNINST）

## 使用实例

修改名称为“vrf1”的VPN实例描述：

```
MOD L3VPNINST: VRFNAME="vrf1", VRFDESCRIPTION="description change";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改L3VPN实例（MOD-L3VPNINST）_00840733.md`
