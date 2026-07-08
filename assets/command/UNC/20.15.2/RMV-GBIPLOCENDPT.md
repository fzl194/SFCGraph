---
id: UNC@20.15.2@MMLCommand@RMV GBIPLOCENDPT
type: MMLCommand
name: RMV GBIPLOCENDPT（删除本端端点配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GBIPLOCENDPT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb over IP管理
- 本端IP端点配置
status: active
---

# RMV GBIPLOCENDPT（删除本端端点配置）

## 功能

**适用网元：SGSN**

该参数用于在Gb OVER IP时删除一个NSE下一个IP地址下的一条或者多条本端端点记录。

## 注意事项

- 该命令执行立即生效。
- 删除后该本端端点对应的链路也自动删除，业务会切换到其它可用的链路上，对业务无影响，但会增加其它链路的负担，请谨慎操作。
- 如果删除本端最后一个端点之后，再次添加端点可能导致添加的端点不是BSC侧server地址，导致通信中断，请谨慎使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于设置端点所在的网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置IP地址类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| LIPV4 | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置本端使用的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>为<br>“IPV4(IPv4)”<br>时才生效。<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| LIPV6 | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置本端PCU使用的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>为<br>“IPV6(IPv6)”<br>时才生效。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| LUP | 本端UDP端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于设置本端使用的UDP端口号。<br>取值范围：1024～65535<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBIPLOCENDPT]] · 本地端点配置（GBIPLOCENDPT）

## 使用实例

1. 删除NSE为600的IPv4地址为192.168.2.1、UDP端口为2001的本端端点记录：
  RMV GBIPLOCENDPT: NSEI=600, IPT=IPV4, LIPV4="192.168.2.1", LUP=2001;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GBIPLOCENDPT.md`
