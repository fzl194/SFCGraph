---
id: UNC@20.15.2@MMLCommand@DSP GTPUPATHINFO
type: MMLCommand
name: DSP GTPUPATHINFO（显示GTPU路径信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPUPATHINFO
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N4 GTP-U管理
- N4 GTP-U路径管理
status: active
---

# DSP GTPUPATHINFO（显示GTPU路径信息）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询当前SMF的N4接口GTPU路径状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询GTPU路径数据的参数类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（所有路径）<br>- IPADDR（对端GTPU地址）<br>- NFINSTANCENAME（UP唯一标识）<br>默认值：无<br>配置原则：无 |
| ID | UPF实例名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFINSTANCENAME"时为条件必选参数。<br>参数含义：该参数用于指定UPF的实例名称，用于唯一标识一个UP。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"IPADDR"时为条件必选参数。<br>参数含义：该参数用于指定GTPU的IP类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| IPADDRV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定GTPU对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPADDRV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定GTPU对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPUPATHINFO]] · GTPU路径（GTPUPATHINFO）

## 使用实例

若需要查询所有SMF的GTPU路径状态。

```
DSP GTPUPATHINFO: QUERYTYPE=ALL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示GTPU路径信息（DSP-GTPUPATHINFO）_58840349.md`
