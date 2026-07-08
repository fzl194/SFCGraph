---
id: UDG@20.15.2@MMLCommand@DSP SRVIP
type: MMLCommand
name: DSP SRVIP（查询服务IP）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SRVIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 路由管理
- 服务实例地址
status: active
---

# DSP SRVIP（查询服务IP）

## 功能

查询业务VNFC的某个服务实例地址信息。用于核对业务VNFC的服务实例地址、CSLB的服务实例以及VNRS的路由是否一致。 CSLB查询到的一条服务实例地址对应VNRS上查询到的一条路由。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONSUMERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在窗口下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得网元节点号即为服务VNFC ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967296。<br>默认值：无 |
| SRVINSTID | 服务实例ID | 可选必选说明：必选参数<br>参数含义：服务实例地址归属的服务实例ID，通过<br>**[DSP LBSRVINST](../../服务实例管理/服务实例/查询LB服务实例（DSP LBSRVINST）_29627060.md)**<br>获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967296。<br>默认值：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：IP地址的类型<br>数据来源：本端规划<br>取值范围：<br>- “IPV4(IPV4) ”<br>- “IPV6(IPV6) ”<br>默认值：无 |
| DSTIPV4 | 目的IPV4 | 可选必选说明：条件必选参数<br>参数含义：目的IPV4地址<br>前提条件：该参数在“IP类型”参数配置为“IPV4”后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| DSTIPV6 | 目的IPV6 | 可选必选说明：条件必选参数<br>参数含义：目的IPV6地址<br>前提条件：该参数在“IP类型”参数配置为“IPV6”后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| IPV4MASK | IPV4掩码 | 可选必选说明：条件必选参数<br>参数含义：目的IPV4的地址掩码。<br>前提条件：该参数在“IP类型”参数配置为“IPV4”后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| IPV6MASK | IPV6掩码 | 可选必选说明：条件必选参数<br>参数含义：目的IPV6的地址掩码。<br>前提条件：该参数在“IP类型”参数配置为“IPV6”后生效。<br>数据来源：本端规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：VPN名称<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0~31。公网填“_public_”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVIP]] · 服务IP（SRVIP）

## 使用实例

- 查询服务IP信息的命令如下：DSP SRVIP: CONSUMERVNFCID=4, SRVINSTID=84, IPTYPE=IPV4, DSTIPV4="192.168.243.2", IPV4MASK="255.255.255.255", VPNNAME="_public_";
  ```
  %%DSP SRVIP: CONSUMERVNFCID=4, SRVINSTID=84, IPTYPE=IPV4, DSTIPV4="192.168.243.2", IPV4MASK="255.255.255.255", VPNNAME="_public_";%%
  RETCODE = 0  操作成功。

  操作结果如下：
  -------------------------
  服务VNFC ID = 4
  服务实例ID = 84
  业务IP类型 = 主机类型业务地址
  IP类型 = IPV4
  CSLB目的IPV4 = 192.168.243.2
  CSLB目的IPV6 = 2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
  CSLB IPV4掩码 = 255.255.255.255
  CSLB IPV6掩码 = ::
  CSLB IP VPN名称 = _public_
  CSLB V4路由下一跳 = 0.0.0.0
  CSLB V6路由下一跳 = 2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
  路由发布策略 = 1
  路由类型 = 信令路由类型
  路由优先级 = 0
  容灾组ID = 0
  (结果个数 = 1)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询服务IP（DSP-SRVIP）_29627067.md`
