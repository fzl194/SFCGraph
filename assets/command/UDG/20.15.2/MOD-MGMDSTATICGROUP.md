---
id: UDG@20.15.2@MMLCommand@MOD MGMDSTATICGROUP
type: MMLCommand
name: MOD MGMDSTATICGROUP（修改IGMP静态组配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: MGMDSTATICGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP静态组播组配置
status: active
---

# MOD MGMDSTATICGROUP（修改IGMP静态组配置）

## 功能

该命令用来修改IGMP静态组配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| ISSTEPGRPVALUE | 是否配置掩码信息 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否配置掩码信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不配置组播掩码和长度。<br>- TRUE：配置组播掩码或者长度。<br>默认值：无 |
| STATICGRP | 静态组地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用来表示静态组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| ISSOURCEADDR | 源地址标志位 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用来表示源地址标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不输入源地址。<br>- TRUE：输入源地址。<br>默认值：无 |
| SRCADDR | 静态组的源地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSOURCEADDR”配置为“TRUE”时为必选参数。<br>参数含义：该参数用来表示静态组的源地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| ISSTEPGRPMASK | 掩码递增 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSTEPGRPVALUE”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于表示是否配置掩码递增。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：配置组地址掩码长度。<br>- TRUE：配置组地址掩码地址。<br>默认值：无 |
| INCSTEPGRPMASK | 组地址递增掩码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSTEPGRPMASK”配置为“TRUE”时为必选参数。<br>参数含义：该参数用来表示组地址递增掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| MASKLEN | 静态组的组地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSTEPGRPMASK”配置为“FALSE”时为必选参数。<br>参数含义：该参数用来表示静态组的组地址掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～32。<br>默认值：无 |
| TOTALNUM | 静态组的配置个数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSTEPGRPMASK”配置为“TRUE” 或 “FALSE”时为必选参数。<br>参数含义：该参数用来表示静态组的配置个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～512。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MGMDSTATICGROUP]] · IGMP静态组配置（MGMDSTATICGROUP）

## 使用实例

修改源为10.0.10.1，组地址为239.0.0.1的IGMP静态组，32位掩码遍历组10个：

```
MOD MGMDSTATICGROUP: VRFNAME="_public_", ADDRESSFAMILY=ipv4unicast, IFNAME="Ethernet64/0/5", STATICGRP="239.0.0.1", ISSOURCEADDR=TRUE, SRCADDR="10.0.10.1",ISSTEPGRPVALUE=TRUE, ISSTEPGRPMASK=TRUE, INCSTEPGRPMASK="0.0.0.1", TOTALNUM=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-MGMDSTATICGROUP.md`
