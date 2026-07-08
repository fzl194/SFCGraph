---
id: UNC@20.15.2@MMLCommand@ADD MGMDSSMAP
type: MMLCommand
name: ADD MGMDSSMAP（添加IGMP SSM映射配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MGMDSSMAP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP SSM映射策略
status: active
---

# ADD MGMDSSMAP（添加IGMP SSM映射配置）

## 功能

该命令用来创建IGMP SSM映射配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 需要首先在公网或VPN实例下配置ADD MCASTENABLE命令。
- 当主机不支持IGMPv3，只支持IGMPv1或IGMPv2组报告时，无法加入SSM范围的组播组。
- 只有在接口下使能了SSM映射，即执行ADD MGMDIF命令且SSMAPENABLE为TRUE之后，配置的SSM源/组地址映射表项才能生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| ISSSMMAPINGMASK | 掩码递增 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否配置掩码递增。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：配置组地址掩码长度。<br>- TRUE：配置组地址掩码地址。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| SSMMAPINGGRP | 组地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SSMMAPINGMASK | 组播地址掩码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSSMMAPINGMASK”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于表示组播地址掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| MASKLEN | 组地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSSMMAPINGMASK”配置为“FALSE”时为必选参数。<br>参数含义：该参数用于表示掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为4～32。<br>默认值：无 |
| SRCADDR | 源地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示源地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MGMDSSMAP]] · IGMP SSM映射配置（MGMDSSMAP）

## 使用实例

创建IGMP SSM映射配置(10.8.8.8, 239.5.5.5)：

```
ADD MGMDSSMAP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,ISSSMMAPINGMASK=TRUE,SSMMAPINGGRP="239.5.5.5",SRCADDR="10.8.8.8",SSMMAPINGMASK="255.255.255.0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MGMDSSMAP.md`
