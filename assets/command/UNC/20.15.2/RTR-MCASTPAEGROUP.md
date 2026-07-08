---
id: UNC@20.15.2@MMLCommand@RTR MCASTPAEGROUP
type: MMLCommand
name: RTR MCASTPAEGROUP（清除组播组引流信息表项）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: MCASTPAEGROUP
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MRM
- 组播组引流信息
status: active
---

# RTR MCASTPAEGROUP（清除组播组引流信息表项）

## 功能

该命令用来清除组播组引流信息表项。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| PAEGROUPID | PAE Group索引 | 可选必选说明：可选参数<br>参数含义：该参数用来表示PAE Group索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：如果不输入该参数，则表示清除所有的PAE表项。 |
| GRPADDR | 组地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用来表示组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PAEJOINTYPE | 引流类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示引流类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPTV：IPTV模式。<br>- BIDIR-CPE：BIDIR-CPE模式。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MCASTPAEGROUP]] · 组播组引流信息（MCASTPAEGROUP）

## 使用实例

清除组播引流信息：

```
RTR MCASTPAEGROUP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,PAEJOINTYPE=IPTV;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-MCASTPAEGROUP.md`
