# 删除接口IPv6地址（RMV IFIPV6ADDRESS）

- [命令功能](#ZH-CN_CONCEPT_0000001550280978__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550280978__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550280978__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550280978__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550280978__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550280978)

该命令用于删除接口的IPv6地址，包括逻辑接口及物理接口。

#### [注意事项](#ZH-CN_CONCEPT_0000001550280978)

- 该命令执行后立即生效。
- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口，Eth-Trunk接口，Eth-Trunk子接口以及Loopback口，Tunnel口上配置。
- 该命令执行后可能会触发ALM-139591684告警。
- 如果接口下IPv6地址是通过DHCPv6分配的，无法通过该命令删除地址。使用RMV DHCP6CLIENT命令删除DHCPv6客户端后会关联删除接口地址。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550280978)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550280978)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于配置接口IPv6地址。如果想要修改接口的IPv6地址，需要使用RMV IFIPV6ADDRESS将该地址删除后，使用ADD IFIPV6ADDRESS添加新地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备是否在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| PREFIXLEN | IPv6地址前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于配置接口IPv6地址前缀。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备是否在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| ADDRTYPE | IPv6地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置接口IPv6地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- global：全球单播地址。<br>- linkLocal：链路本地地址。<br>- anycast：任播地址。<br>默认值：global |
| IDGENTYPE | IPv6地址计算类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置接口IPv6地址计算类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- none：None。<br>- cga：CGA。<br>- eui64：Eui64。<br>默认值：none |

#### [使用实例](#ZH-CN_CONCEPT_0000001550280978)

删除接口下指定IPv6地址：

```
RMV IFIPV6ADDRESS:IFNAME="Ethernet64/0/3",IPV6ADDRESS="2001:db8::11";
```
