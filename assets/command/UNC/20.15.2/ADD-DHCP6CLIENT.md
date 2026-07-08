---
id: UNC@20.15.2@MMLCommand@ADD DHCP6CLIENT
type: MMLCommand
name: ADD DHCP6CLIENT（增加DHCPv6客户端）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DHCP6CLIENT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCPv6客户端配置
status: active
---

# ADD DHCP6CLIENT（增加DHCPv6客户端）

## 功能

该命令用于添加DHCPv6客户端。设备作为DHCPv6客户端，在接口上配置该命令后，设备将通过DHCPv6有状态方式从DHCPv6服务器自动获取IPv6地址。接口上使能DHCPv6客户端，需保证接口上有link-local地址，否则无法正常申请到地址。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 每个接口处理单元IPU（Interface Process Unit）支持DHCPv6客户端数目为1024。
- 该命令在Ethernet接口上配置执行。
- 该命令将侦听转发面546端口号的UDP报文。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ISDHCPV6CENABLE | DHCPv6客户端使能 | 可选必选说明：可选参数<br>参数含义：该参数用于标识DHCPv6客户端是否使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。TRUE表示使能，FALSE表示不使能。<br>默认值：TRUE |
| ADDRMODE | 地址模式 | 可选必选说明：可选参数<br>参数含义：该参数用于标识申请的地址是主机地址还是网段地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HOST_MODE：主机地址模式。<br>- NETWOKSEGMENT_MODE：网段地址模式。<br>默认值：HOST_MODE |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DHCP6CLIENT]] · DHCPv6客户端（DHCP6CLIENT）

## 使用实例

- 使能接口IPv6功能和接口上配置本地链路地址：
  ```
  SET IFIPV6ENABLE: IFNAME="Ethernet64/0/4", ENABLEFLAG=TRUE, AUTOLINKLOCAL=TRUE;
  ```
- 添加DHCPv6客户端：
  ```
  ADD DHCP6CLIENT: IFNAME="Ethernet64/0/4", ISDHCPV6CENABLE=TRUE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DHCP6CLIENT.md`
