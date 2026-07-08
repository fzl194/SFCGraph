---
id: UNC@20.15.2@MMLCommand@LST MGMDSTATICGROUP
type: MMLCommand
name: LST MGMDSTATICGROUP（查询IGMP静态组配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MGMDSTATICGROUP
command_category: 查询类
effect_mode: ''
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

# LST MGMDSTATICGROUP（查询IGMP静态组配置）

## 功能

该命令用来查询IGMP静态组配置。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| STATICGRP | 静态组地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用来表示静态组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| ISSOURCEADDR | 源地址标志位 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用来表示源地址标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不输入源地址。<br>- TRUE：输入源地址。<br>默认值：无 |
| SRCADDR | 静态组的源地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSOURCEADDR”配置为“TRUE”时为必选参数。<br>参数含义：该参数用来表示静态组的源地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| ISSTEPGRPVALUE | 是否配置掩码信息 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否配置掩码信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不配置组播掩码和长度。<br>- TRUE：配置组播掩码或者长度。<br>默认值：无 |
| ISSTEPGRPMASK | 掩码递增 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSTEPGRPVALUE”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于表示是否配置掩码递增。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：配置组地址掩码长度。<br>- TRUE：配置组地址掩码地址。<br>默认值：无 |
| INCSTEPGRPMASK | 组地址递增掩码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSTEPGRPMASK”配置为“TRUE”时为必选参数。<br>参数含义：该参数用来表示组地址递增掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| MASKLEN | 静态组的组地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSTEPGRPMASK”配置为“FALSE”时为必选参数。<br>参数含义：该参数用来表示静态组的组地址掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～32。<br>默认值：无 |

## 操作的配置对象

- [IGMP静态组配置（MGMDSTATICGROUP）](configobject/UNC/20.15.2/MGMDSTATICGROUP.md)

## 使用实例

查询IGMP静态组配置：

```
LST MGMDSTATICGROUP: VRFNAME="_public_", ADDRESSFAMILY=ipv4unicast, IFNAME="Ethernet64/0/5",ISSTEPGRPVALUE=FALSE, ISSOURCEADDR=FALSE;
```

```
RETCODE = 0  操作成功。

结果如下
--------
     VPN实例名称  =  _public_
          地址族  =  IPv4单播
        接口名称  =  Ethernet64/0/5
      静态组地址  =  239.0.0.1
  静态组的源地址  =  192.168.0.1
  组地址递增掩码  =  0.0.0.1
静态组的配置个数  =  2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IGMP静态组配置（LST-MGMDSTATICGROUP）_49961718.md`
