---
id: UNC@20.15.2@MMLCommand@RMV LINKMODULE
type: MMLCommand
name: RMV LINKMODULE（删除LinkModule表记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LINKMODULE
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- LinkModule表管理
status: active
---

# RMV LINKMODULE（删除LinkModule表记录）

## 功能

![](删除LinkModule表记录（RMV LINKMODULE）_41583989.assets/notice_3.0-zh-cn_2.png)

该命令为高危命令，执行不当会导致链路丢失。

**适用NF：NCG**

该命令用于删除LinkModule表中的残留记录。

## 注意事项

- 该命令执行后立即生效。
- 该命令用于删除[**DSP ACTRL**](../../业务配置管理/接入控制/显示CGF与对端网元链路状态（DSP ACTRL）_51174236.md)命令查询结果和ALM-82008 GSN对vCG无响应告警之外的残留记录 。
- 如果删除记录为有效记录，5分钟之后会自动恢复有效记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示LinkModule表的IP类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：无<br>配置原则：无。 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4”时为条件必选参数。<br>参数含义：该参数用于表示LinkModule表的IPv4地址。可以通过OPR DBGCMDPRXY调测命令“vcg show linkmodule”查询要删除的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0-255.255.255.255。<br>默认值：无<br>配置原则：无。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6”时为条件必选参数。<br>参数含义：该参数用于表示LinkModule表的IPv6地址。<br>可以通过OPR DBGCMDPRXY调测命令“vcg show linkmodule”查询要删除的IPv6地址。数据来源：本端规划<br>取值范围：IPv6地址类型。::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：无。 |

## 操作的配置对象

- [LinkModule表记录（LINKMODULE）](configobject/UNC/20.15.2/LINKMODULE.md)

## 使用实例

删除LinkModule表中指定IP的记录：

```
RMV LINKMODULE: IPTYPE=IPV4, IPV4="10.31.14.3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除LinkModule表记录（RMV-LINKMODULE）_41583989.md`
