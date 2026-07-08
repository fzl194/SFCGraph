# 设置UNC发送的UDP报文中是否携带checksum（SET UDPCHECKSUM）

- [命令功能](#ZH-CN_MMLREF_0000001193899600__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001193899600__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001193899600__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001193899600__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001193899600)

**适用NF：PGW-C、GGSN、SMF**

该命令用来配置UNC发送的UDP报文是否携带checksum。

## [注意事项](#ZH-CN_MMLREF_0000001193899600)

- 该命令执行后立即生效。

- 在现网中与对端网元对接时，由于对端网元的处理方式不同，对接可能会失败。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UDPTYPE | SWITCH |
| --- | --- |
| DHCP | DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001193899600)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001193899600)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UDPTYPE | UDP Type | 可选必选说明：必选参数<br>参数含义：指定是何种类型的报文。<br>数据来源：本端规划<br>取值范围：<br>- DHCP（表示DHCP报文）<br>默认值：无。<br>配置原则：无 |
| SWITCH | Checksum开关 | 可选必选说明：可选参数<br>参数含义：指定UNC发送的UDP报文中是否携带checksum。<br>数据来源：对端协商<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UDPCHECKSUM查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001193899600)

配置DHCP报文携带checksum：

```
SET UDPCHECKSUM:UDPTYPE=DHCP,SWITCH=ENABLE;
```
