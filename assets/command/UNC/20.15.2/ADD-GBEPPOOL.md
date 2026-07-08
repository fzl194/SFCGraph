---
id: UNC@20.15.2@MMLCommand@ADD GBEPPOOL
type: MMLCommand
name: ADD GBEPPOOL（增加IP地址到地址池）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GBEPPOOL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 16
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- Gb地址池管理
status: active
---

# ADD GBEPPOOL（增加IP地址到地址池）

## 功能

**适用网元：SGSN**

此命令用于增加IP地址到Gb地址池，作为自动配置功能的Gb业务IP使用，地址池整系统唯一。

此地址池中的IP地址既可以作为NSE动态流程协商的地址，也可以作为NSE的本端端点进行业务传输。

此命令只适用于Gb over IP自动配置的场景。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为16。
- 如果要使用自动配置功能，至少配置端点池中一个IP地址。
- 如果新添加的IP地址是Gb本端端点的IP地址，且Gb本端端点的端口与[**SET GBLOCPORTRGE**](../本端端点端口号管理/设置本端端口号选择范围(SET GBLOCPORTRGE)_26146000.md)的预置端口相同，则添加失败。
- IP地址和vpn名称必须在SERVICEIP表中已经配置，可以用[**LST SERVICEIP**](../../../业务IP管理/业务IP/查询业务IP(LST SERVICEIP)_72226047.md)查询。
- 一个Gb IP地址只能配置一条记录，且只能归属一个分组。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待添加的IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待添加到地址池中的IPv4地址。<br>前提条件：<br>- 该参数在“ IP类型 ”设置为“IPV4(IPv4)”时生效。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>配置原则：<br>- 有效的IPV4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPV4地址必须是A、B或者C类地址。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待添加到地址池中的IPv6地址。<br>前提条件：<br>- 该参数在“ IP类型 ”设置为“IPV6(IPv6)”时生效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>说明：目前不支持IPV6地址的配置。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待添加到地址池中的IP地址描述信息。<br>数据来源：整网规划<br>取值范围：0～33位字符串<br>默认值：无 |
| VPNNAME | vpn名称 | 可选必选说明：可选参数<br>参数含义：VPN名称。<br>数据来源：全网规划<br>取值范围：0～31位字符串。<br>默认值：无 |
| GROUPID | 组号 | 可选必选说明：可选参数<br>参数含义：本参数用于指定Gb IP地址的组号，用于不同的BSC设备需要使用不同网段的USN侧Gb IP地址场景。BSC侧将预置端点的IP地址配置为期望使用的USN侧对应分组下的任一Gb IP地址，USN将在此分组下分配SGSN侧的Gb本端IP端点给该BSC服务。<br>数据来源：本端规划<br>取值范围：0～15。<br>默认值：0 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBEPPOOL]] · 地址池中IP地址（GBEPPOOL）

## 使用实例

增加一个 “IP类型” 为 “IPV4(IPv4)” ， “IPv4地址” 为 “192.168.4.101” ， “描述信息” 为 “DEFAULT” 的IP到地址池：

ADD GBEPPOOL: IPTYPE=IPV4, IPV4="192.168.4.101", DESC="DEFAULT";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IP地址到地址池(ADD-GBEPPOOL)_26145998.md`
