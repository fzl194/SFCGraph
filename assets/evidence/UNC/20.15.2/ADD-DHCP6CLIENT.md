# 增加DHCPv6客户端（ADD DHCP6CLIENT）

- [命令功能](#ZH-CN_CONCEPT_0000001550120726__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550120726__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550120726__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550120726__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550120726__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550120726)

该命令用于添加DHCPv6客户端。设备作为DHCPv6客户端，在接口上配置该命令后，设备将通过DHCPv6有状态方式从DHCPv6服务器自动获取IPv6地址。接口上使能DHCPv6客户端，需保证接口上有link-local地址，否则无法正常申请到地址。

#### [注意事项](#ZH-CN_CONCEPT_0000001550120726)

- 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 每个接口处理单元IPU（Interface Process Unit）支持DHCPv6客户端数目为1024。
- 该命令在Ethernet接口上配置执行。
- 该命令将侦听转发面546端口号的UDP报文。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550120726)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550120726)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ISDHCPV6CENABLE | DHCPv6客户端使能 | 可选必选说明：可选参数<br>参数含义：该参数用于标识DHCPv6客户端是否使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。TRUE表示使能，FALSE表示不使能。<br>默认值：TRUE |
| ADDRMODE | 地址模式 | 可选必选说明：可选参数<br>参数含义：该参数用于标识申请的地址是主机地址还是网段地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HOST_MODE：主机地址模式。<br>- NETWOKSEGMENT_MODE：网段地址模式。<br>默认值：HOST_MODE |

#### [使用实例](#ZH-CN_CONCEPT_0000001550120726)

- 使能接口IPv6功能和接口上配置本地链路地址：
  ```
  SET IFIPV6ENABLE: IFNAME="Ethernet64/0/4", ENABLEFLAG=TRUE, AUTOLINKLOCAL=TRUE;
  ```
- 添加DHCPv6客户端：
  ```
  ADD DHCP6CLIENT: IFNAME="Ethernet64/0/4", ISDHCPV6CENABLE=TRUE;
  ```
