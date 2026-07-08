---
id: UDG@20.15.2@MMLCommand@RTR MGMDGROUP
type: MMLCommand
name: RTR MGMDGROUP（清除IGMP加入组信息）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: MGMDGROUP
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP组播组信息
status: active
---

# RTR MGMDGROUP（清除IGMP加入组信息）

## 功能

该命令用来清除IGMP加入组信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| ALLFLAG | 是否清除所有DGMP组信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否清除所有DGMP组信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：清除指定信息。<br>- TRUE：清除所有信息。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ALLFLAG”配置为“FALSE”时为必选参数。<br>参数含义：该参数用来表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| GRPADDR | 组地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ALLFLAG”配置为“FALSE”时为必选参数。<br>参数含义：该参数用来表示组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| ISSSMAPPING | 组标记 | 可选必选说明：可选参数<br>参数含义：该参数用来表示组标记，区分是Report建立的组还是SSM映射建立的组。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MGMDGROUP]] · IGMP加入组信息（MGMDGROUP）

## 使用实例

清除IGMP加入组信息：

```
RTR MGMDGROUP: VRFNAME="_public_", ADDRESSFAMILY=ipv4unicast, ALLFLAG=FALSE, IFNAME="Ethernet64/0/5", GRPADDR="239.0.0.1", ISSSMAPPING=FALSE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除IGMP加入组信息（RTR-MGMDGROUP）_00866349.md`
