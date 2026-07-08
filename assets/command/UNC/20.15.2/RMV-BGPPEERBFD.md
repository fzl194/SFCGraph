---
id: UNC@20.15.2@MMLCommand@RMV BGPPEERBFD
type: MMLCommand
name: RMV BGPPEERBFD（删除BGP对等体BFD检测）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BGPPEERBFD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体BFD检测
status: active
---

# RMV BGPPEERBFD（删除BGP对等体BFD检测）

## 功能

该命令用于删除IPv4或IPv6对等体的BFD检测。

## 注意事项

- 该命令执行后立即生效。
- 当命令参数仅指定VPN实例名称和对等体地址时，仅去使能对等体上的BFD功能。当指定其他参数时，此时恢复对应参数为默认值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| ADDRESSTYPE | 地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4。<br>- ipv6：IPv6。<br>默认值：无 |
| PEERADDR | IPv4对等体地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为必选参数。<br>参数含义：该参数用于指定连接对等体的IPv4接口地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PEERADDRV6 | IPv6对等体地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为必选参数。<br>参数含义：该参数用于指定连接对等体的IPv6接口地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |
| ISBFDBLOCK | 使能BFD Block功能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。<br>参数含义：该参数用于指定是否阻止对等体从对等体组中继承BFD功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| MULTIPLIER | 检测时间倍数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。<br>参数含义：该参数用于指定BFD会话的检测时间倍数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无 |
| ISBFDENABLE | 使能BFD | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。<br>参数含义：该参数用于指定是否使能BFD检测。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| RXINTERVAL | 最小接收间隔时间（ms） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。<br>参数含义：该参数用于指定该BFD的期望接收时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| TXINTERVAL | 最小发送间隔时间（ms） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。<br>参数含义：该参数用于指定该BFD的期望发送时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| ISSINGLEHOP | 使能单跳模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。<br>参数含义：single-hop-prefer参数用来在IBGP对等体之间创建BFD会话时优先使用单跳检测，用于对等体之间的IP连通性检测，即对于IBGP的指定接口上只存在一个BFD会话。此参数用于和其他厂商设备连接时，保证本端和对端采用相同的检测方式。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BGPPEERBFD]] · BGP对等体BFD检测（BGPPEERBFD）

## 使用实例

- 在名称为“vrf1”的BGP VPN实例下删除对等体10.2.2.2的BFD检测：
  ```
  RMV BGPPEERBFD:VRFNAME="vrf1",ADDRESSTYPE=ipv4,PEERADDR="10.2.2.2",ISBFDENABLE=TRUE,ISSINGLEHOP=TRUE;
  ```
- 在名称为“vrf1”的BGP VPN实例下删除对等体2001:db8:1:1:1:1:1:1的BFD检测：
  ```
  RMV BGPPEERBFD:VRFNAME="vrf1",ADDRESSTYPE=ipv6,PEERADDRV6="2001:db8:1:1:1:1:1:1",ISBFDENABLE=TRUE,ISSINGLEHOP=TRUE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BGP对等体BFD检测（RMV-BGPPEERBFD）_00841533.md`
