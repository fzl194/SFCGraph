# 增加中转UPF与Radius服务器的绑定关系（ADD UPFRDSSVR）

- [命令功能](#ZH-CN_MMLREF_0000001135636449__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135636449__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135636449__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135636449__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001135636449)

![](增加中转UPF与Radius服务器的绑定关系（ADD UPFRDSSVR）_35636449.assets/notice_3.0-zh-cn_2.png)

新增中转UPF与RADIUS服务器的绑定关系，若中转UPF绑定的RADIUS Server IP与直连的RADIUS Server IP相同会造成直连RADIUS场景业务受损等问题。

**适用NF：PGW-C、SMF**

该命令用来新增中转UPF与Radius服务器的绑定关系。当SMF与Radius服务器不能直连时，采用通过UPF与Radius服务器连接的方式进行鉴权或者计费。

## [注意事项](#ZH-CN_MMLREF_0000001135636449)

- 该命令执行后立即生效。

- 当新增中转UPF连接RADIUS服务器时，需要先使用ADD RADIUSCLIENTIP或ADD APNRDSCLIENTIP命令为该服务器所属的RADIUS服务器组配置Client IP接口。
- 直连RADIUS服务器与经UPF中转的RADIUS服务器的RADIUS Server IP不可以相同，否则会造成直连RADIUS场景业务受损。

- 最多可输入8000条记录。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。

#### [操作用户权限](#ZH-CN_MMLREF_0000001135636449)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135636449)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERTYPE | 服务器类型 | 可选必选说明：必选参数<br>参数含义：指定RADIUS服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- “AUTHENTICATION（鉴权服务器）”：表示鉴权服务器。<br>- “ACCOUNTING（计费服务器）”：表示计费服务器。<br>默认值：无<br>配置原则：无 |
| IPVERSION | 服务器IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS服务器IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”：IPv4<br>- “IPV6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| SERVERIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：RADIUS服务器IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD RDSSVR**](../Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)<br>命令配置生成。 |
| SERVERIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：RADIUS服务器IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD RDSSVR**](../Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)<br>命令配置生成。 |
| UPLISTNAME | UP列表名称 | 可选必选说明：必选参数<br>参数含义：指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0000001135636449)

当新增UPF中转RADIUS服务器，本端需要根据对端服务器新增配置时：新增服务器类型为计费，服务器地址为“192.168.10.1”，UP列表名称为“uplist1”：

```
ADD UPFRDSSVR: SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="192.168.10.1", UPLISTNAME="uplist1";
```
