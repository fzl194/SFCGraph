---
id: UNC@20.15.2@MMLCommand@RMV IPV6GPMEM
type: MMLCommand
name: RMV IPV6GPMEM（删除IPv6群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPV6GPMEM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- IP群组管理
- IP群组成员配置
status: active
---

# RMV IPV6GPMEM（删除IPv6群组成员）

## 功能

**适用网元：SGSN、MME**

该命令用于删除IP群组成员配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPGPID | IP群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP群组标识。<br>前提条件：“IP群组标识”已经通过<br>[**ADD IPGP**](../IP群组配置/增加IP群组(ADD IPGP)_18995796.md)<br>配置。<br>数据来源：本端规划<br>取值范围：1-255<br>默认值：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：本端规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。 |
| IPV6MSK | IPV6地址前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IPv6地址的前缀的长度。<br>数据来源：本端规划<br>取值范围：0~128<br>默认值：无<br>配置原则：0是无效掩码。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6GPMEM]] · IPv6群组成员（IPV6GPMEM）

## 使用实例

删除IPv6群组成员，IP群组标识为1，IP地址为 2001:db8:: ，IPV6地址前缀长度为61：

RMV IPV6GPMEM: IPGPID=1, IPV6="2001:db8::", IPV6MSK=64;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IPV6GPMEM.md`
