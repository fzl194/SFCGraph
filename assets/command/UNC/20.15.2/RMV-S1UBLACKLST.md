---
id: UNC@20.15.2@MMLCommand@RMV S1UBLACKLST
type: MMLCommand
name: RMV S1UBLACKLST（删除S1-U IP地址黑名单记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1UBLACKLST
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1-U黑名单管理
- S1-U黑名单维护
status: active
---

# RMV S1UBLACKLST（删除S1-U IP地址黑名单记录）

## 功能

**适用网元：MME**

暂不支持本命令。该命令用于删除S1-U IP地址黑名单记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型，标识S1-U黑名单IP地址的类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要配置的S1-U IPv4黑名单地址。<br>前提条件：该参数在"IP类型"参数配置为"IPV4"后生效。<br>数据来源：整网规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要配置的S1-U IPv6黑名单地址。<br>前提条件：该参数在"IP类型"参数配置为"IPV6"后生效。<br>数据来源：整网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1UBLACKLST]] · S1-U IP地址黑名单记录（S1UBLACKLST）

## 使用实例

删除一条S1-U黑名单记录，IP地址为10.1.1.1：

RMV S1UBLACKLST: IPTYPE=IPV4, IPV4="10.1.1.1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-S1UBLACKLST.md`
