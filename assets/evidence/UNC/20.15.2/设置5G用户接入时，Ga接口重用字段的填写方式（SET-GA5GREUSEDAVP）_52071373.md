# 设置5G用户接入时，Ga接口重用字段的填写方式（SET GA5GREUSEDAVP）

- [命令功能](#ZH-CN_MMLREF_0252071373__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0252071373__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0252071373__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0252071373__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0252071373)

**适用NF：SMF、PGW-C**

该命令用于控制Ga接口对接过程中可能产生的不兼容因素。

## [注意事项](#ZH-CN_MMLREF_0252071373)

- 该命令执行后立即生效。

- 该命令只做话单字段填写控制，不参与计费条件改变判断。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RAT | ULI | ULIFIXVALUE | QOS | QOSFIXVALUE | SERVINGNODETYPE |
| --- | --- | --- | --- | --- | --- |
| REALVALUE | REALVALUE | 1812f470ffff12f470ffffffff | REALVALUE | 08-4807001e848000195460 | REALVALUE |

#### [操作用户权限](#ZH-CN_MMLREF_0252071373)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0252071373)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RAT | 无线接入技术 | 可选必选说明：可选参数<br>参数含义：控制用户RAT为NR时，离线话单是否支持通过rATType字段携带用户真实的RAT。当该参数取值为REALVALUE时，rATType字段取值根据SET/LST NRRATVALUE设置；当该参数取值为FIXVALUE时，rATType字段取值固定为EUTRAN(6)。<br>数据来源：本端规划<br>取值范围：<br>- REALVALUE（携带真实用户信息）<br>- FIXVALUE（携带固定用户信息）<br>- DISABLE（不携带用户信息）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GA5GREUSEDAVP查询当前参数配置值。<br>配置原则：无 |
| ULI | 用户位置信息 | 可选必选说明：可选参数<br>参数含义：控制用户RAT为NR时，离线话单是否支持通过userLocationInformation字段携带用户真实的位置信息。<br>数据来源：本端规划<br>取值范围：<br>- REALVALUE（携带真实用户信息）<br>- FIXVALUE（携带固定用户信息）<br>- DISABLE（不携带用户信息）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GA5GREUSEDAVP查询当前参数配置值。<br>配置原则：<br>5G接入，配置SET GA5GREUSEDAVP，ULI=FIXVALUE时，话单及所有容器携带ULI信息，ULI填写方式不受BIT922软参控制。 |
| ULIFIXVALUE | 用户位置信息固定值 | 可选必选说明：该参数在"ULI"配置为"FIXVALUE"时为条件必选参数。<br>参数含义：设置用户RAT为NR时话单中ULI需要填写的固定值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是12~26。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GA5GREUSEDAVP查询当前参数配置值。<br>配置原则：<br>- 配置的用户位置信息可以是TAI，或者ECGI，或是同时TAI和ECGI，格式需要符合29274定义。<br>- 前两个字符必须为“18”或“08”或“10”，标识位置类型。整个字符串长度必须为26，12，16。 |
| QOS | QoS | 可选必选说明：可选参数<br>参数含义：控制用户RAT为NR时，离线话单中QoS信息的携带方式。<br>数据来源：本端规划<br>取值范围：<br>- REALVALUE（携带真实用户信息）<br>- FIXVALUE（携带固定用户信息）<br>- DISABLE（不携带用户信息）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GA5GREUSEDAVP查询当前参数配置值。<br>配置原则：无 |
| QOSFIXVALUE | QoS固定值 | 可选必选说明：该参数在"QOS"配置为"FIXVALUE"时为条件必选参数。<br>参数含义：设置用户RAT为NR时话单中QoS需要填写的固定值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是23。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GA5GREUSEDAVP查询当前参数配置值。<br>配置原则：<br>- 配置的用户QoS为R8格式，需要符合29061定义。<br>- 前三个字符必须为“08-”，整个字符串固定长度为23。 |
| SERVINGNODETYPE | 服务节点类型 | 可选必选说明：可选参数<br>参数含义：控制用户RAT为NR时，离线话单是否支持通过servingNodeType字段携带用户真实的服务节点类型。当该参数取值为FIXVALUE时，servingNodeType字段取值固定为GTPSGW(2)。<br>数据来源：本端规划<br>取值范围：<br>- REALVALUE（携带真实用户信息）<br>- FIXVALUE（携带固定用户信息）<br>- DISABLE（不携带用户信息）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GA5GREUSEDAVP查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0252071373)

假设运营商需要Ga接口支持5G用户接入，期望PGW-CDR/SGW-CDR中RAT重用字段携带固定值EUTRAN(6)，可以执行该命令：

```
SET GA5GREUSEDAVP: RAT=FIXVALUE;
```
