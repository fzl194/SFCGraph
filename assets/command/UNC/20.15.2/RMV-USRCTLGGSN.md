---
id: UNC@20.15.2@MMLCommand@RMV USRCTLGGSN
type: MMLCommand
name: RMV USRCTLGGSN（删除手工恢复GGSN地址）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRCTLGGSN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GGSN容灾功能
status: active
---

# RMV USRCTLGGSN（删除手工恢复GGSN地址）

## 功能

**适用网元：SGSN**

此命令用于删除已配置的手工恢复GGSN地址。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，指定的GGSN在故障恢复后无需手动恢复就会重新被启用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：此参数指定要删除的GGSN地址的IP类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：此参数指定待删除的GGSN网元的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时生效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>说明：“0.0.0.0”和“255.255.255.255”是无效的IP地址。<br>配置原则：<br>- IPv4地址不能为0.0.0.0、255.255.255.255和0.x.y.z。<br>- IPv4地址不能为组播地址（如：224.x.y.z）和环回地址(如：127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：此参数指定待删除的GGSN网元的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时生效。<br>取值范围： ::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRCTLGGSN]] · 手工恢复GGSN地址（USRCTLGGSN）

## 使用实例

删除需手工恢复GGSN地址192.168.66.6：

RMV USRCTLGGSN: IPT=IPV4, IPV4="192.168.66.6";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-USRCTLGGSN.md`
