---
id: UNC@20.15.2@MMLCommand@MOD GBIPLOCENDPT
type: MMLCommand
name: MOD GBIPLOCENDPT（修改本地端点配置）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD GBIPLOCENDPT（修改本地端点配置）

## 功能

**适用网元：SGSN**

该命令用于在Gb OVER IP时修改一个NSE下的一条本端端点配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令只能修改本端端点权重记录和“描述”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于设置端点所在的网络服务实体标识。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无<br>说明：必须已经配置成IP承载类型的NSE。 |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| LIPV4 | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置本端使用的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时才生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| LIPV6 | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置本端PCU使用的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时才生效。<br>数据来源：整网规划<br>取值范围： ::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| LUP | 本端UDP端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于设置本端使用的UDP端口号。<br>数据来源：整网规划<br>取值范围：1024～65535<br>默认值：无 |
| SW | 信令权重 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>取值范围：0～255<br>默认值：无<br>说明：在NSE为IP动态配置类型时，信令权重可以通过相关流程下发PCU。 |
| DW | 数据权重 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>说明：- 在NSE为IP动态配置类型时，数据权重可以通过相关流程下发PCU。<br>- 当取值为0时，表示权重因子是0，不被选择。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端端点名称，标识本端端点。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBIPLOCENDPT]] · 本地端点配置（GBIPLOCENDPT）

## 使用实例

1. 修改IPv4地址为192.168.2.1、UDP端口为2001的本端端点的信令权重为12，数据权重为12，对应BSC1：
  MOD GBIPLOCENDPT: NSEI=600, IPT=IPV4, LIPV4="192.168.2.1", LUP=2001, SW=12, DW=12, DESC="FOR BSC1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改本地端点配置(MOD-GBIPLOCENDPT)_72345611.md`
