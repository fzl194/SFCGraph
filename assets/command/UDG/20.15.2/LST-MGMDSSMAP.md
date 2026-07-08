---
id: UDG@20.15.2@MMLCommand@LST MGMDSSMAP
type: MMLCommand
name: LST MGMDSSMAP（查询IGMP SSM映射配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MGMDSSMAP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP SSM映射策略
status: active
---

# LST MGMDSSMAP（查询IGMP SSM映射配置）

## 功能

该命令用来查询IGMP SSM映射配置。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| SSMMAPINGGRP | 组地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用于表示组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [IGMP SSM映射配置（MGMDSSMAP）](configobject/UDG/20.15.2/MGMDSSMAP.md)

## 使用实例

查询IGMP SSM映射配置：

```
LST MGMDSSMAP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
 VPN实例名称  =  _public_
      地址族  =  IPv4单播
      组地址  =  239.5.5.5
组播地址掩码  =  255.255.255.0
      源地址  =  10.8.8.8
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IGMP-SSM映射配置（LST-MGMDSSMAP）_00601125.md`
